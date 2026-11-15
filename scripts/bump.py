#!/usr/bin/env python3
"""Bump bot logic (D61, D89, repo-topology.md §7.5): move the pins of xdmod and robarm-* to their main.

Reads submanifests/*.yml, asks GitHub for the `main` head of every pinned project that is xdmod or
robarm-* (remote tiacsys), and with --apply rewrites the `revision:` lines that differ. Tools,
libraries and Zephyr are never touched: their upgrades are deliberate PRs (D39).

Writes into --out:
    bump.json   [{"name", "file", "old", "new", "status", "ahead_by", "commits": [...]}]
    title.txt   "bump: robarm-ee -> abc1234, xdmod -> def5678" (empty if nothing to bump)
    body.md     the PR text (without the provenance trailer; the workflow adds it)

`status` comes from the GitHub compare API (pin...main): ahead (normal), diverged or behind (the pin
is not on main, e.g. it was a PR branch commit before a rebase merge; the PR text flags these). The
compare needs `gh` with a token; without it status is "unknown".

Stdlib only (runs on the bare runner before the workspace exists). Usage, from the workspace root:
    python3 robarm-manifest/scripts/bump.py --manifest robarm-manifest --out build/robarm-manifest/bump
    python3 robarm-manifest/scripts/bump.py --manifest robarm-manifest --out ... --apply
Exit code 0 in both cases; title.txt tells whether there is a bump.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

URL_BASE = "https://github.com/tiacsys"   # the `tiacsys` remote of the submanifests
NAME_RE = re.compile(r"^\s*-\s+name:\s*(\S+)\s*$")
FIELD_RE = re.compile(r"^(\s*)(remote|revision):\s*(\S+)(.*)$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
MAX_COMMITS = 30


def bumpable(name):
    return name == "xdmod" or name.startswith("robarm-")


def read_pins(manifest):
    """[(file, name, revision)] for the bumpable projects; parses the simple submanifest layout."""
    pins = []
    for f in sorted((manifest / "submanifests").glob("*.yml")):
        cur = {}
        for line in f.read_text().splitlines() + ["  - name: <end>"]:
            m = NAME_RE.match(line)
            if m:
                if cur and cur.get("remote") == "tiacsys" and bumpable(cur["name"]) and "revision" in cur:
                    pins.append((f, cur["name"], cur["revision"]))
                cur = {"name": m.group(1)}
                continue
            m = FIELD_RE.match(line)
            if m and cur:
                cur[m.group(2)] = m.group(3)
    return pins


def main_head(name):
    out = subprocess.run(["git", "ls-remote", f"{URL_BASE}/{name}", "refs/heads/main"],
                         capture_output=True, text=True, check=True, timeout=120).stdout.split()
    if not out or not SHA_RE.match(out[0]):
        raise SystemExit(f"{name}: no main branch on {URL_BASE}/{name}")
    return out[0]


def compare(name, old, new):
    """(status, ahead_by, [commit lines]) from the GitHub compare API; ('unknown', None, []) without gh."""
    if not shutil.which("gh"):
        return "unknown", None, []
    r = subprocess.run(["gh", "api", f"repos/tiacsys/{name}/compare/{old}...{new}"],
                       capture_output=True, text=True, timeout=120)
    if r.returncode:
        print(f"{name}: compare failed: {r.stderr.strip()}", file=sys.stderr)
        return "unknown", None, []
    d = json.loads(r.stdout)
    commits = [f"{c['sha'][:12]} {c['commit']['message'].splitlines()[0]}" for c in d.get("commits", [])]
    return d.get("status", "unknown"), d.get("ahead_by"), commits[-MAX_COMMITS:]


def apply(bumps):
    for f in sorted({b["path"] for b in bumps}):
        mine = {b["name"]: b for b in bumps if b["path"] == f}
        lines, name = [], None
        for line in f.read_text().splitlines(keepends=True):
            m = NAME_RE.match(line)
            if m:
                name = m.group(1)
            m = FIELD_RE.match(line)
            if m and name in mine and m.group(2) == "revision" and m.group(3) == mine[name]["old"]:
                line = line.replace(mine[name]["old"], mine[name]["new"], 1)
                mine[name]["done"] = True
            lines.append(line)
        f.write_text("".join(lines))
        missed = [n for n, b in mine.items() if not b.get("done")]
        if missed:
            raise SystemExit(f"{f}: could not rewrite the revision of {', '.join(missed)}")


def body(bumps, manifest_rel):
    out = ["Moves the pins of xdmod and the robarm repos to their `main` (bump bot, D61, D89).", "",
           "| Repo | Pin | → main | Commits | Compare |", "|---|---|---|---|---|"]
    for b in bumps:
        flag = "" if b["status"] in ("ahead", "unknown") else f" ⚠ {b['status']}"
        n = "?" if b["ahead_by"] is None else b["ahead_by"]
        out.append(f"| {b['name']} | `{b['old'][:12]}` | `{b['new'][:12]}` | {n}{flag} | "
                   f"[diff]({URL_BASE}/{b['name']}/compare/{b['old'][:12]}...{b['new'][:12]}) |")
    if any(b["status"] in ("diverged", "behind") for b in bumps):
        out += ["", "⚠ A pin that is *diverged* or *behind* was not on `main` (for example a PR branch "
                "commit before a rebase merge). Check that the new pin is what you want."]
    for b in bumps:
        if b["commits"]:
            out += ["", f"<details><summary>{b['name']}: commits</summary>", "", "```"]
            out += b["commits"] + ["```", "</details>"]
    out += ["", f"Files: {', '.join(sorted({f'`{manifest_rel}/{b['file']}`' for b in bumps}))}.",
            "The bot rebuilds this branch from `main` on every run (every 30 minutes); several bumps "
            "collect here. Tools, libraries and Zephyr are not bumped automatically.",
            "", "Review and merge by a human (D58, repo-topology.md §7.5). The full-set check reports "
            "as the commit status `full-set` and as a comment below."]
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", type=Path, default=Path("robarm-manifest"), help="manifest checkout")
    ap.add_argument("--out", type=Path, required=True, help="folder for bump.json, title.txt, body.md")
    ap.add_argument("--apply", action="store_true", help="rewrite the submanifests")
    ap.add_argument("--head", action="append", default=[], metavar="NAME=SHA",
                    help="use this main head instead of asking GitHub (tests)")
    a = ap.parse_args(argv)

    heads = dict(h.split("=", 1) for h in a.head)
    bumps = []
    for f, name, pin in read_pins(a.manifest):
        new = heads.get(name) or main_head(name)
        print(f"{name:20} pin {pin[:12]}  main {new[:12]}  {'BUMP' if new != pin else 'ok'}")
        if new == pin:
            continue
        status, ahead_by, commits = compare(name, pin, new)
        bumps.append({"name": name, "file": f.relative_to(a.manifest).as_posix(), "path": f,
                      "old": pin, "new": new, "status": status, "ahead_by": ahead_by, "commits": commits})

    a.out.mkdir(parents=True, exist_ok=True)
    title = ("bump: " + ", ".join(f"{b['name']} → {b['new'][:7]}" for b in bumps)) if bumps else ""
    (a.out / "title.txt").write_text(title + "\n" if title else "")
    (a.out / "body.md").write_text(body(bumps, a.manifest.name) if bumps else "")
    (a.out / "bump.json").write_text(json.dumps([{k: v for k, v in b.items() if k != "path"} for b in bumps],
                                                indent=2) + "\n")
    if bumps and a.apply:
        apply(bumps)
        print(f"rewrote {len(bumps)} pin(s)")
    print(title or "nothing to bump")
    return 0


if __name__ == "__main__":
    sys.exit(main())
