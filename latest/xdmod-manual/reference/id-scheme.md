<a id="ref-id-scheme"></a>

# ID scheme

Every need has an ID. IDs are stable, never reused, readable, and unique across the whole
workspace. They work in every tool: sphinx-needs, SysML short names, KiCad fields, FreeCAD
properties, Doxygen tags and test reports. The scheme is new; it does not reuse older ID schemes
([*A new ID prefix scheme (XD-ADR-0013)*](../explanation/decisions/traces.md#XD-ADR-0013)).

## Format

```text
<DOMAIN>-<KIND>-<NNNN>   e.g.  SYS-REQ-0012, SW-TC-0103, EE-CMP-0007, INT-ITC-0003
TR-<TESTCASE-ID>-<RUN>   e.g.  TR-SW-TC-0103-3f9a1c2e   (test results only)
```

- `DOMAIN`: `SYS`, `SW`, `EE`, `ME`, `INT` (integration and system verification),
  `XD` for the framework’s own items and `PRJ` for project-level items ([*ID format DOMAIN-KIND-NNNN (XD-ADR-0071)*](../explanation/decisions/traces.md#XD-ADR-0071),
  [*Decisions become sphinx-needs (XD-ADR-0109)*](../explanation/decisions/traces.md#XD-ADR-0109)).
- `KIND`: 2 to 5 capital letters. Domain and kind together name the need type.
- `NNNN`: a number with 4 digits, zero-padded, issued per kind. Above 9999 it simply grows.
- `RUN`: the first 8 hex digits of the run record’s hash (HIL runs) or of the JUnit file. So a
  test result is unique per run.
- A usage of a definition may get `<ID>.<n>` ([*The definition holds the tr... (XD-ADR-0117)*](../explanation/decisions/method.md#XD-ADR-0117)).
- Regex:
  `^((SYS|SW|EE|ME|INT|XD|PRJ)-[A-Z]{2,5}-[0-9]{4,}|TR-(SYS|SW|EE|ME|INT)-[A-Z]{2,5}-[0-9]{4,}-[0-9a-f]{8})$`

**No project code in the sources** ([*No project code in the sources (XD-ADR-0072)*](../explanation/decisions/traces.md#XD-ADR-0072)). All repos of a project share one ID space.
Where IDs leave the workspace (bundles, published `needs.json`, shared affirmatrix cases), the
exporting tool puts a project code in front, with `:` as the separator. Example (robot arm):
`RA:SYS-REQ-0012`.

## Kinds

Generated from curatrix and the needs configuration:

| Kind       | Need type                      | Directive   |
|------------|--------------------------------|-------------|
| `EE-CMP`   | Circuit Block / Component      | `ee-cmp`    |
| `EE-HAR`   | Wiring Harness                 | `ee-har`    |
| `EE-PCBA`  | PCBA                           | `ee-pcba`   |
| `EE-PORT`  | EE Port (connector)            | `ee-port`   |
| `EE-REQ`   | EE Requirement                 | `ee-req`    |
| `EE-TC`    | EE Test Case                   | `ee-tc`     |
| `INT-ITC`  | Integration Test Case          | `int-itc`   |
| `INT-STC`  | System Test Case               | `int-stc`   |
| `ME-ASM`   | Assembly                       | `me-asm`    |
| `ME-PART`  | Part                           | `me-part`   |
| `ME-PORT`  | ME Port (mechanical interface) | `me-port`   |
| `ME-REQ`   | ME Requirement                 | `me-req`    |
| `ME-TC`    | ME Test Case                   | `me-tc`     |
| `PRJ-DEC`  | Project Decision               | `prj-dec`   |
| `SW-ARCH`  | SW Architecture Element        | `sw-arch`   |
| `SW-DD`    | SW Detailed Design Element     | `sw-dd`     |
| `SW-IMPL`  | Code Unit                      | `sw-impl`   |
| `SW-REQ`   | SW Requirement                 | `sw-req`    |
| `SW-TC`    | SW Test Case                   | `sw-tc`     |
| `SYS-CFG`  | Configuration                  | `sys-cfg`   |
| `SYS-EL`   | System Model Element           | `sys-el`    |
| `SYS-FEAT` | Feature                        | `sys-feat`  |
| `SYS-IF`   | Interface                      | `sys-if`    |
| `SYS-NEED` | Stakeholder Need               | `sys-need`  |
| `SYS-REQ`  | System Requirement             | `sys-req`   |
| `SYS-STH`  | Stakeholder                    | `sys-sth`   |
| `SYS-UC`   | Use Case                       | `sys-uc`    |
| `SYS-VIEW` | (reserved, not a need)         |             |
| `XD-ADR`   | Framework Decision             | `xd-adr`    |
| `XD-CHECK` | curatrix Check                 | `xd-check`  |
| `XD-RULE`  | Method Rule                    | `xd-rule`   |

`SYS-VIEW` is a reserved kind that is not a need. It is only used as the SysML short name of a
view ([*View definitions live in th... (XD-ADR-0085)*](../explanation/decisions/method.md#XD-ADR-0085)). Its numbers still come from the ledger. Configurations and features have the
kinds `SYS-CFG` and `SYS-FEAT` ([*IDs for configurations and ... (XD-ADR-0097)*](../explanation/decisions/method.md#XD-ADR-0097)). SW test case IDs come from the ledger and a tool
writes them into the ZTEST comment ([*SW test case IDs come from ... (XD-ADR-0073)*](../explanation/decisions/traces.md#XD-ADR-0073)).

## Where the ID lives in each tool

| Tool               | Where the ID is written                                                                                                                                                                       | Read by                          |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| sphinx-needs (rst) | `:id:` of the directive                                                                                                                                                                       | Sphinx                           |
| SysML v2           | short name: `part def <'SYS-EL-0012'> ArmController { … }`; stubs use the<br/>requirement’s ID                                                                                                | Pilot JSON, then curatrix        |
| KiCad              | hidden symbol or sheet field `TraceID`; links in further hidden fields (`Realizes`,<br/>`Satisfies`, `Conforms`, `PartOf`)                                                                    | curatrix (plain Python)          |
| FreeCAD            | object properties `TraceID`, `Realizes`, `Satisfies`, `Conforms`, `PartOf`                                                                                                                    | `Document.xml`, read by curatrix |
| Doxygen / C        | `@xdid{SW-IMPL-0004}`, `\satisfies`, `\verifies`; test IDs in the ZTEST comment                                                                                                               | Doxygen XML, then zdocs          |
| Twister / JUnit    | the test case’s `SW-TC` ID in the test name or a property                                                                                                                                     | test reports, then `TR` needs    |
| Devicetree         | `trace-id` property of the project’s own binding, never on upstream nodes<br/>([*Small corrections from rese... (XD-ADR-0057)*](../explanation/decisions/traces.md#XD-ADR-0057) (f)) | the devicetree check             |

## The ledger

Each repo keeps one ledger file, `ids.yaml`. It lists **every number ever issued** per kind
that the repo owns, one per line. It is append-only. Listing every number (not just the last)
means that two PRs that issue the same number touch the same line, so git reports a conflict
([*ID collisions show up as gi... (XD-ADR-0122)*](../explanation/decisions/traces.md#XD-ADR-0122)).

```yaml
# Every number issued per kind, one per line. Append-only.
SYS-REQ:
  - 41
  - 42
SYS-NEED:
  - 17
SYS-FEAT: []       # owned, nothing issued yet
```

A kind with nothing issued yet is written `KIND: []`. That line makes the repo the owner of
the kind.

## Issuing IDs

- **Placeholders.** Write a need with a placeholder ID of the form `<KIND>-NEW-<tag>`, for
  example the kind `SYS-REQ` followed by `-NEW-a`. Then run
  `curatrix ids fix <repo>`. It replaces every placeholder with the next free number
  (`max(ledger, IDs in the sources) + 1`) and adds it to the ledger. The same placeholder gets
  the same ID in every file.
- `curatrix ids new <KIND> [FILE]` issues one ID, and with `FILE` replaces that file’s first
  placeholder of the kind.
- Never invent a number. Never reuse one.
- **Parallel PRs.** Two PRs may issue the same number. The second to rebase gets a ledger
  conflict. Rerun `curatrix ids fix`, which renumbers that PR’s new IDs. Rulesets require PRs
  to be up to date with `main` before merge, so the duplicate check runs on the combined state.
- **Retiring.** A retired need keeps its ID with `status: retired` ([*Small corrections from rese... (XD-ADR-0057)*](../explanation/decisions/traces.md#XD-ADR-0057) (e),
  [*Retiring generated needs (XD-ADR-0119)*](../explanation/decisions/traces.md#XD-ADR-0119)). When it is finally deleted, the ledger still holds its number.

## Rules

<a id="needtable-reference/id-scheme-0"></a>

| ID                                                                       | Title                                          |
|--------------------------------------------------------------------------|------------------------------------------------|
| [XD-RULE-0015](../explanation/rules/ids.md#XD-RULE-0015) | An ID matches the scheme and its need type     |
| [XD-RULE-0016](../explanation/rules/ids.md#XD-RULE-0016) | IDs are unique                                 |
| [XD-RULE-0017](../explanation/rules/ids.md#XD-RULE-0017) | No placeholders on main                        |
| [XD-RULE-0018](../explanation/rules/ids.md#XD-RULE-0018) | The ledger is never behind the sources         |
| [XD-RULE-0019](../explanation/rules/ids.md#XD-RULE-0019) | Test report IDs are mapped to TR IDs           |
| [XD-RULE-0020](../explanation/rules/ids.md#XD-RULE-0020) | IDs are never reused; retire before you delete |
- [*An ID matches the scheme an... (XD-RULE-0015)*](../explanation/rules/ids.md#XD-RULE-0015) is checked by [*IDs match the scheme and th... (XD-CHECK-0003)*](checks.md#XD-CHECK-0003).
- [*IDs are unique (XD-RULE-0016)*](../explanation/rules/ids.md#XD-RULE-0016) is checked by [*no duplicate IDs across doc... (XD-CHECK-0010)*](checks.md#XD-CHECK-0010) across documents and in the full set.
- [*No placeholders on main (XD-RULE-0017)*](../explanation/rules/ids.md#XD-RULE-0017) is checked by [*no placeholder IDs (XD-CHECK-0013)*](checks.md#XD-CHECK-0013).
- [*The ledger is never behind ... (XD-RULE-0018)*](../explanation/rules/ids.md#XD-RULE-0018) is checked by [*IDs in the sources are in t... (XD-CHECK-0014)*](checks.md#XD-CHECK-0014).
- [*IDs are never reused; retir... (XD-RULE-0020)*](../explanation/rules/ids.md#XD-RULE-0020) is helped by [*tombstones of deleted gener... (XD-CHECK-0012)*](checks.md#XD-CHECK-0012) (tombstones of deleted generated needs).
- [*Test report IDs are mapped ... (XD-RULE-0019)*](../explanation/rules/ids.md#XD-RULE-0019) is applied by the test-report extractor.
