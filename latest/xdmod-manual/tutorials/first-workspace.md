<a id="tut-first-workspace"></a>

# Your first workspace

#### NOTE
This tutorial is a skeleton. It is completed in Phase 6 on the real robot-arm repos.

## Goal

You set up a workspace for one role, run the checks of one repo, and open its documents in a
browser. At the end you know where everything lives and which command does what.

## What you need

- git and Python 3.12 or newer.
- An empty folder. It becomes the **workspace root**. Every command runs from there
  ([*All commands run from the w... (XD-ADR-0060)*](../explanation/decisions/repos.md#XD-ADR-0060)).
- The name of the project’s manifest repo. In the examples it is `robarm-manifest`, the
  manifest of the robot-arm example.

## Steps

1. Clone the manifest repo and run its bootstrap script with your role:
   ```sh
   git clone https://github.com/tiacsys/robarm-manifest
   robarm-manifest/scripts/bootstrap.sh --role syseng
   ```

   The script makes `.venv` with west, runs `west init` and `west update`, installs
   curatrix from xdmod, and then runs `curatrix bootstrap --role syseng`. The roles are listed
   in [Make a change across repos](../howto/cross-repo-change.md) and in the workspace reference.
2. Load the workspace environment into your shell:
   ```sh
   eval "$(.venv/bin/curatrix env)"
   ```
3. Check the setup. `doctor` lists every tool with its installed and pinned version and
   fails on a mismatch:
   ```sh
   curatrix doctor
   ```
4. Run the checks of one repo. They run locally with one command ([*Every check runs locally (XD-RULE-0032)*](../explanation/rules/checks.md#XD-RULE-0032)), every tool
   under a memory limit and a timeout ([*Every tool runs under limits (XD-RULE-0044)*](../explanation/rules/checks.md#XD-RULE-0044)):
   ```sh
   curatrix check robarm-syseng --stage local
   ```

   The summary is in `build/robarm-syseng/checks/summary.json`. For each failure curatrix
   prints the command that reproduces it.
5. Build the documents of the repo and open them:
   ```sh
   curatrix docs robarm-syseng --open
   ```

   The HTML is in `build/robarm-syseng/docs/deploy/html/<doc-id>/`. All build output goes
   below `build/` ([*Build output only under build/ (XD-RULE-0040)*](../explanation/rules/checks.md#XD-RULE-0040)).

## What you learned

- The workspace root holds `.west/`, `.venv/`, `build/` and all repos ([*One west topdir at the work... (XD-ADR-0061)*](../explanation/decisions/repos.md#XD-ADR-0061)).
- `curatrix` is the one command layer for people, agents and CI ([*One framework tool: curatrix (XD-ADR-0089)*](../explanation/decisions/checks.md#XD-ADR-0089)).
- `west update` moves repos back to their pins. While you work on branches, use
  `curatrix update` instead.

Next: [Your first requirement, end to end](first-requirement.md).
