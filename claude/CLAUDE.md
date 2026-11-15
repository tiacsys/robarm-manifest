# robarm-manifest: rules for agents

Read the workspace rules first (`<workspace>/CLAUDE.md`, copied from `xdmod/launch/CLAUDE.md`).
This file adds what is special about the manifest repo.

## What this repo is

The west manifest of the robot-arm workspace, the full document set, and the baselines
(`xdmod/claude/framework/repo-topology.md`). Layout: `README.md`.

## Rules

1. **This repo is the only place that pins revisions** (D39). No other repo has a `west.yml`.
   - Our repos (xdmod, robarm-*) and the libraries are pinned by full commit SHA. Zephyr is
     pinned by tag.
   - Pins of xdmod and robarm-* move through bump PRs, after the upstream PRs are merged. Do not
     pin a branch name or a PR branch, except zdocs (see the comment in
     `submanifests/00-framework.yml`).
   - The bump bot (`.github/workflows/bump.yml`) owns the branch `bump/auto` and rebuilds it from
     `main` on every run. Do not push to it; change `scripts/bump.py` instead. It finds pins by
     the line layout `- name:` / `remote: tiacsys` / `revision: <sha>`; keep that layout.
   - Library and Zephyr upgrades are their own PRs.
2. **Groups decide what a role gets** (`repo-topology.md` §4). West makes a project active as
   soon as ONE of its groups is enabled. So a big library carries only its own group
   (`kicad-3d`, `freecad-parts`), never also `ee` or `me`. Projects without groups are active in
   every role.
3. **Keep the default group filter minimal** (D93): framework, syseng and Zephyr.
4. **Paths** (D91): design repos at the top level, tools under `tools/`, libraries under `libs/`.
5. **`scripts/bootstrap.sh` is a copy** of `xdmod/templates/bootstrap.sh` (D118). Change the
   template in xdmod and copy it here; never edit the copy alone. CK-H5 warns when they differ.
6. **`docs/documents.yaml` lists every document of the set once.** Each entry mirrors the entry
   in the owning repo's registry (same id, title, prefix, kind). When a repo adds, renames or
   removes a document, change this registry in the same change (with the same branch name).
7. **Project decisions** are `prj-dec` needs in `docs/robarm/decisions.rst`, with IDs from
   `ids.yaml` (`curatrix ids new PRJ-DEC`). Every mention of a decision in rst is a `:need:`
   reference (D120).

## Checks

From the workspace root:

```sh
.venv/bin/west manifest --validate              # manifest syntax and imports
curatrix docs full                              # full document set into build/full/
curatrix check robarm-manifest --stage local    # all checks of this repo
```

The full set needs every robarm repo, so build it in the `integration` or `full` role.

## Pitfalls

- `west update` moves every project back to its pin (detached HEAD). On branches use
  `curatrix update` (`west update -k`).
- Zephyr's own manifest is imported with an allowlist (`cmsis_6`, `hal_stm32`). A new HAL module
  must be added to that list in `submanifests/10-zephyr.yml`.
- A document id that is also a group id breaks the docs configure step (zdocs makes a
  `<group>-<builder>` target). Group ids start with `g-`.
