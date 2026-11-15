# robarm-manifest

The west manifest of the robot arm, the worked example of
[XDMOD](https://github.com/tiacsys/xdmod) (Cross-Domain MODeling).

This repo does three things:

- It **pins the version of every repo** in the workspace (`west.yml` and `submanifests/`). It is
  the only place that does that.
- It **builds the full linked document set** (`docs/`): the project overview `robarm` plus every
  document of the other robarm repos.
- It **holds the baselines**: a tag `baseline/vX.Y.Z` is one fixed set of repo versions.

## Get the workspace

You need git and Python 3.12 or newer. Start in an empty folder. It becomes the workspace root,
and every command runs from there.

```sh
git clone https://github.com/tiacsys/robarm-manifest
robarm-manifest/scripts/bootstrap.sh --role <role>
```

The script creates `.venv` with west, runs `west init -l robarm-manifest` and `west update`,
installs `curatrix` from xdmod, and then runs `curatrix bootstrap --role <role>`. That turns on
the groups of the role, runs `west update` again, installs the tools, and copies the agent
files.

| Role | Group filter | You get |
|---|---|---|
| `syseng` | (manifest default) | xdmod, zdocs, affirmatrix, robarm-syseng, SYSMOD and PLEML libraries, Zephyr |
| `ee` | `+ee` | the above, plus robarm-ee and the KiCad libraries (no 3D models) |
| `ee3d` | `+ee,+kicad-3d` | like `ee`, plus the KiCad 3D models (about 1.8 GB) |
| `me` | `+me,+freecad-parts` | the default set, plus robarm-me and the FreeCAD parts library (about 5.7 GB) |
| `sw` | `+sw` | the default set, plus robarm-sw |
| `integration` | `+ee,+me,+sw,+integration` | every repo, without the big libraries |
| `full` | all groups | everything, including the big libraries |

To change the role later, run `curatrix bootstrap --role <other>`. `curatrix doctor` checks the
setup. While you work on branches, use `curatrix update` instead of `west update`: plain
`west update` moves every repo back to its pinned commit.

## Workspace layout

```
<workspace>/
  robarm-manifest/   xdmod/   robarm-syseng/  robarm-ee/  robarm-me/  robarm-sw/  robarm-integration/
  tools/zdocs/  tools/affirmatrix/
  libs/sysmod-sysmlv2/  libs/pleml/  libs/kicad/*/  libs/freecad/
  zephyr/  modules/hal/...
  .venv/  .west/  build/
```

## What is in this repo

| Path | What |
|---|---|
| `west.yml` | the main manifest; imports `submanifests/` and sets the minimal default group filter |
| `submanifests/*.yml` | the projects, one file per area: framework, Zephyr, EE, ME, SW, integration |
| `scripts/bootstrap.sh` | first-time setup; a copy of `xdmod/templates/bootstrap.sh` (do not edit the copy) |
| `docs/` | registry of the full document set (`documents.yaml`) and the `robarm` overview document |
| `checks.yaml` | what `curatrix check robarm-manifest` runs |
| `ids.yaml` | ID ledger; this repo owns the project decisions `PRJ-DEC` |
| `requirements.txt`, `tools.yaml` | what this repo needs from pip (west) and as other tools (nothing yet) |
| `claude/` | rules for agents that work in this repo |
| `.github/` | CI (calls the reusable check workflow in xdmod), Pages publishing, the workspace action, the pull request template |
| `scripts/pages/` | puts one version of the full set into the Pages site; the version switcher |

## Common commands

Run them from the workspace root.

```sh
curatrix docs full                              # build the full document set into build/full/
curatrix check robarm-manifest --stage local    # the checks of this repo
```

## Published documentation

The full document set is on GitHub Pages: <https://tiacsys.github.io/robarm-manifest/>.
The workflow `.github/workflows/pages.yml` builds it (`curatrix docs full`, integration role, at
the pins, without CAD content) and publishes it to the branch `gh-pages`:

| Folder | Built from |
|---|---|
| `latest/` | every push to `main` |
| `vX.Y.Z/` | the tag `baseline/vX.Y.Z`; one folder per baseline. It is only rewritten by an explicit re-run of the workflow on that tag |

`versions.json` at the site root lists the versions. Every page loads `version-switcher.js` from
the root, which offers the same page in another version. A publish replaces only its own folder.
Do not edit `gh-pages` by hand. Pull requests get the HTML as a workflow artifact instead.

## Changing pins

Pins move through pull requests on this repo. A change across repos has one PR per repo and,
after they are merged, one PR here that moves the pins together. Library and Zephyr upgrades are
their own PRs.

## Licence

Apache-2.0 (see `LICENSE`).
