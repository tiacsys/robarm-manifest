#!/usr/bin/env python3
"""Put one version of the full document set into the GitHub Pages site (D55).

Layout of the site (the `gh-pages` branch, research/zdocs.md §8, bridle's pattern):

    index.html               redirect to latest/ (or to the newest baseline while there is no latest)
    versions.json            the list the switcher reads: latest first, then baselines, newest first
    version-switcher.js      the switcher; every HTML page of every version loads it
    .nojekyll                Pages must not run Jekyll (it would drop Sphinx's _static/ folders)
    latest/<doc-id>/...      the full set built from main
    v0.1.0/<doc-id>/...      the full set built from tag baseline/v0.1.0, one folder per baseline

Only the folder of the given version is replaced; every other version folder stays as it is.
zdocs HTML links are relative, so a build works unchanged in any folder.

Usage (from the workspace root):
    python3 robarm-manifest/scripts/pages/site.py --site <gh-pages checkout> \
        --html build/full/docs/deploy/html --version latest --ref main --sha <sha>
"""

import argparse
import datetime
import json
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SWITCHER = "version-switcher.js"
MARKER = 'id="xdmod-version-switcher"'
LANDING_DOC = "robarm"          # the project overview document of the full set
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")


def version_key(name):
    """Sort key: latest first, then baselines by SemVer, newest first."""
    if name == "latest":
        return (0, ())
    nums = tuple(-int(n) for n in re.match(r"v(\d+)\.(\d+)\.(\d+)", name).groups())
    pre = name.partition("-")[2]
    return (1, nums, 0 if not pre else 1, pre)  # a release sorts before its pre-releases


def redirect(target, title):
    return (
        "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\">\n"
        f"<title>{title}</title>\n"
        f"<meta http-equiv=\"refresh\" content=\"0; url={target}\">\n"
        f"<link rel=\"canonical\" href=\"{target}\">\n"
        f"</head><body><p><a href=\"{target}\">{title}</a></p></body></html>\n"
    )


def inject(html_file, root_rel):
    """Add the switcher script to one HTML page; root_rel is the path from the page to the site root."""
    text = html_file.read_text(encoding="utf-8", errors="surrogateescape")
    if MARKER in text:
        return False
    tag = (f'<script {MARKER} src="{root_rel}/{SWITCHER}" data-site-root="{root_rel}" defer>'
           "</script>\n")
    idx = text.lower().rfind("</head>")
    if idx < 0:
        return False
    html_file.write_text(text[:idx] + tag + text[idx:], encoding="utf-8", errors="surrogateescape")
    return True


def add_version(site, html, version):
    dest = site / version
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(html, dest)
    docs = sorted(p.name for p in dest.iterdir() if (p / "index.html").is_file())
    landing = LANDING_DOC if LANDING_DOC in docs else (docs[0] if docs else "")
    (dest / "index.html").write_text(
        redirect(f"{landing}/index.html" if landing else ".", f"Robot Arm documentation ({version})"))
    n = 0
    for f in dest.rglob("*.html"):
        rel = os.path.relpath(site, f.parent).replace(os.sep, "/")
        n += inject(f, rel)
    return docs, n


def update_versions(site, version, ref, sha):
    path = site / "versions.json"
    data = json.loads(path.read_text()) if path.exists() else {}
    entries = {e["name"]: e for e in data.get("versions", [])}
    if version:
        entries[version] = {
            "name": version,
            "ref": ref,
            "sha": sha,
            "published": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
    # A version is listed iff its folder exists (a folder removed by hand drops out on the next run).
    names = [n for n in entries if (site / n / "index.html").is_file()]
    names.sort(key=version_key)
    data = {
        "comment": "Written by robarm-manifest/.github/workflows/pages.yml (scripts/pages/site.py).",
        "versions": [entries[n] for n in names],
    }
    path.write_text(json.dumps(data, indent=2) + "\n")
    return names


def write_root(site, names):
    shutil.copyfile(HERE / SWITCHER, site / SWITCHER)
    (site / ".nojekyll").write_text("")
    target = "latest/" if "latest" in names else (f"{names[0]}/" if names else "versions.json")
    (site / "index.html").write_text(redirect(target, "Robot Arm documentation"))
    (site / "README.md").write_text(
        "# GitHub Pages of robarm-manifest\n\n"
        "This branch is written by the `pages` workflow (`.github/workflows/pages.yml` on `main`).\n"
        "Do not edit it by hand. `latest/` is built from `main`, `vX.Y.Z/` from the tag\n"
        "`baseline/vX.Y.Z`; `versions.json` lists them for the version switcher.\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", required=True, type=Path, help="checkout of the gh-pages branch")
    ap.add_argument("--html", type=Path, help="build/full/docs/deploy/html of the full-set build")
    ap.add_argument("--version", help="'latest' or 'vX.Y.Z'")
    ap.add_argument("--ref", default="", help="git ref the build came from (main, baseline/vX.Y.Z)")
    ap.add_argument("--sha", default="", help="manifest commit of the build")
    a = ap.parse_args(argv)

    if bool(a.html) != bool(a.version):
        ap.error("--html and --version go together (leave both out to refresh only the root files)")
    if a.version and a.version != "latest" and not VERSION_RE.match(a.version):
        ap.error(f"version {a.version!r} is neither 'latest' nor vX.Y.Z")
    a.site.mkdir(parents=True, exist_ok=True)

    if a.version:
        if not a.html.is_dir():
            ap.error(f"{a.html} is not a directory")
        docs, n = add_version(a.site, a.html, a.version)
        print(f"{a.version}/: {len(docs)} documents ({', '.join(docs)}), switcher added to {n} pages")
    names = update_versions(a.site, a.version, a.ref, a.sha)
    write_root(a.site, names)
    print(f"versions.json: {', '.join(names) or '(none)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
