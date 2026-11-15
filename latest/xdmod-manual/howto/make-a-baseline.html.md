<a id="howto-make-a-baseline"></a>

# Make a baseline

Use this guide when you want a fixed, released set of repo versions. A **baseline** is a tag
`baseline/vX.Y.Z` of the manifest repo; a **bundle** is the package of outputs built from it
([*Terms: baseline and bundle (XD-ADR-0034)*](../explanation/decisions/repos.html.md#XD-ADR-0034), [*SemVer tags and baseline tags (XD-ADR-0047)*](../explanation/decisions/repos.html.md#XD-ADR-0047)).

## Steps

1. Merge the open bump PR, so the manifest pins the latest `main` of every repo.
2. Use a workspace with the `full` role, so all CAD content is there ([*CI runs without CAD content (XD-ADR-0049)*](../explanation/decisions/checks.html.md#XD-ADR-0049)).
3. Run the baseline gates for every repo, then the full set:
   ```sh
   curatrix check robarm-syseng --stage baseline --base <last-baseline-needs>
   curatrix check robarm-manifest --stage baseline --base <last-baseline-needs>
   ```

   `--base` points at the `needs.json` files of the last baseline.
4. Fix what fails. The baseline stage is stricter than `local` and `pr`:
   - [*no links to retired needs (... (XD-CHECK-0008)*](../reference/checks.html.md#XD-CHECK-0008): links to retired needs fail now; the grace period ends ([*Links to retired needs are ... (XD-RULE-0011)*](../explanation/rules/trace.html.md#XD-RULE-0011),
     [*A grace period for retired ... (XD-ADR-0068)*](../explanation/decisions/traces.html.md#XD-ADR-0068)).
   - [*suspect links against the l... (XD-CHECK-0024)*](../reference/checks.html.md#XD-CHECK-0024): open suspect links fail ([*Suspect links are reviewed ... (XD-RULE-0014)*](../explanation/rules/trace.html.md#XD-RULE-0014)).
   - [*generated files record the ... (XD-CHECK-0020)*](../reference/checks.html.md#XD-CHECK-0020): generated files must record the pinned tool versions.
   - [*stale evidence (R5a) (XD-CHECK-0011)*](../reference/checks.html.md#XD-CHECK-0011): stale evidence doesn’t count ([*Only valid evidence counts (XD-RULE-0013)*](../explanation/rules/trace.html.md#XD-RULE-0013)).
   - [*every requirement verified ... (XD-CHECK-0007)*](../reference/checks.html.md#XD-CHECK-0007): missing verification is a warning in iteration 1 ([*Verification coverage is a ... (XD-ADR-0090)*](../explanation/decisions/checks.html.md#XD-ADR-0090)).
5. Tag the manifest repo with an annotated tag and push it:
   ```sh
   git -C robarm-manifest tag -a baseline/v0.1.0 -m "baseline v0.1.0"
   git -C robarm-manifest push origin baseline/v0.1.0
   ```
6. Create the GitHub release. Its assets are the outputs (docs, later CAM data and firmware).

#### NOTE
Bundles, CAM output and PDF documents come in iteration 2 ([*Scope moved to iteration 2 (XD-ADR-0037)*](../explanation/decisions/scope.html.md#XD-ADR-0037)). The docs of
each baseline are hosted next to `main` on Pages ([*Docs hosting on GitHub Page... (XD-ADR-0048)*](../explanation/decisions/documents.html.md#XD-ADR-0048)); multi-version hosting is
still being built.

## Pitfalls

- Tombstones in `generated/retired-needs.json` are dropped at the next baseline. Remove the
  links to them before you tag.
- Only a person makes baselines. Agents may prepare the gate results.
