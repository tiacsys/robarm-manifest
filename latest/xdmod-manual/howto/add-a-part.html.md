<a id="howto-add-a-part"></a>

# Add a FreeCAD part or assembly

Use this guide when you add a FreeCAD part (`ME-PART`) or assembly (`ME-ASM`) that takes part
in trace links.

## Steps

1. Start FreeCAD with the launcher. It uses a workspace-local config that saves `.FCStd` files
   **uncompressed** and points at the pinned parts library ([*FreeCAD files uncompressed,... (XD-ADR-0056)*](../explanation/decisions/checks.html.md#XD-ADR-0056), [*Pinned, isolated component ... (XD-ADR-0080)*](../explanation/decisions/repos.html.md#XD-ADR-0080)):
   ```sh
   curatrix launch freecad robarm-me/parts/link.FCStd
   ```
2. Add string properties in the group `Trace` to the part or assembly object: `TraceID`,
   `Realizes`, `Satisfies`, `Conforms`, `PartOf`, `Status`, `Configs`. They mean the
   same as the KiCad fields ([Add a PCBA or circuit block](add-a-pcba.html.md)).
3. Set the `TraceID` to a real ID. Placeholders inside `.FCStd` files are refused, so issue
   the ID first:
   ```sh
   curatrix ids new ME-PART --repo robarm-me
   ```
4. Keep parameters in a spreadsheet with aliases. The `freecad-params` directive shows them in
   the docs, also in CI.
5. Regenerate the CAD needs and the semantic JSON, and commit both with the part:
   ```sh
   curatrix gen cad-needs robarm-me
   curatrix gen freecad-json robarm-me
   ```

## Checks

-  [*.FCStd uncompressed; drawio... (XD-CHECK-0025)*](../reference/checks.html.md#XD-CHECK-0025): the `.FCStd` is stored uncompressed ([*Design files are stored unc... (XD-RULE-0039)*](../explanation/rules/checks.html.md#XD-RULE-0039)).
- [*cad-needs.json matches the ... (XD-CHECK-0019)*](../reference/checks.html.md#XD-CHECK-0019): `cad-needs.json` matches the FreeCAD files.
- [*generated files record the ... (XD-CHECK-0020)*](../reference/checks.html.md#XD-CHECK-0020): the generated files record the tool versions that made them.

For review, `git diff` shows `.FCStd` changes as semantic JSON through the textconv driver
that the bootstrap installs. GitHub does not, so reviewers read the committed JSON.

#### NOTE
The full review report (drawing SVGs, image diff, 3D views) stays local in iteration 1
([*Scope cuts for iteration 1 (XD-ADR-0124)*](../explanation/decisions/scope.html.md#XD-ADR-0124)). Publishing it as a Pages preview ([*FreeCAD review report as a ... (XD-ADR-0098)*](../explanation/decisions/scope.html.md#XD-ADR-0098)) comes later. TechDraw and GLB
exports are not implemented yet.

## Pitfalls

- `.FCStd` files can’t be merged. On a conflict, take one side and redo the other change.
- An unchanged save still changes the file. The pre-commit hook warns when a `.FCStd` changed
  but its semantic JSON didn’t.
