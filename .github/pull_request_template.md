## What and why

<!-- What does this PR change, and why? Link the issue it closes: "Closes #N". -->

## Sibling PRs

<!-- A change across repos uses the same branch name in every repo (D52). List every PR of this
change, in merge order (syseng, then ee / me / sw, then integration, then this manifest PR).
Write "none" if there are none. -->

- 

## Affected needs

<!-- Needs (IDs) that this PR adds, changes, retires or re-links, e.g. SYS-REQ-0012.
For a pin bump: the needs that change in the full set (see the needs-diff report of CI). -->

- 

## Checklist

- [ ] `curatrix check robarm-manifest --stage local` passes (run from the workspace root)
- [ ] Pins are full commit SHAs (Zephyr: a tag), and only the intended pins moved
- [ ] `docs/documents.yaml` matches the registries of the repos whose documents changed
- [ ] FreeCAD review report: if a sibling PR changes `.FCStd` files, its report is attached to
      that PR (built locally for now, D63/D135)
- [ ] Every commit has a `Co-Authored-By` trailer if an agent wrote it (D51)

<!-- Provenance (D72): a PR text written by an agent ends with this line, outside the comment:
🤖 Generated with [Claude Code](https://claude.com/claude-code)
-->
