<a id="adr-index"></a>

# Decisions

This part records every decision about the XDMOD framework. Each decision is a need of type
`xd-adr` (an *architecture decision record*), with an ID `XD-ADR-nnnn` from xdmod’s ledger
`ids.yaml`. Decisions that are only about one project that uses XDMOD (its hardware, its repos,
its GitHub settings, its licence) are kept in that project’s own documents, as `prj-dec` needs.
A project decision may `follows` a framework decision; a framework decision never links to a
project.

## How to read a decision

- `legacy_id` is the number the decision had in the planning log (`D1` to `D142`) before it
  became a need. Old texts and commit messages use these numbers.
- `date` is the day it was made.
- `decision_status` is `proposed` (written, but waiting for a spike or the owner), `accepted`, `revised` (a newer decision changed part of it) or
  `superseded` (a newer decision replaced it). Changed decisions are never deleted or edited
  into something new: they keep their need, and the newer decision holds the link to them
  (`refines`, `revises` or `supersedes`). The older need shows the link back as
  “refined by”, “revised by” or “superseded by”. This is the trace rule
  [*Trace rule: the concrete si... (XD-ADR-0004)*](traces.html.md#XD-ADR-0004) applied to decisions.
- Rules that a decision introduces are `xd-rule` needs that are `decided_by` it (see
  [Rules](../rules/index.html.md)).

## How to add a decision

1. Add an `xd-adr` need to the topic page it fits, with a placeholder ID
   (`<KIND>-NEW-<tag>`, see the ID scheme), `decision_status: accepted`, `status: valid` and today’s `date`.
2. If it changes an older decision, add `refines`, `revises` or `supersedes` with the older
   ID, and set the older need’s `decision_status`.
3. Run `curatrix ids fix xdmod` to issue the ID, then `curatrix check xdmod --stage local`.

* [Method and model](method.html.md)
* [Traces and IDs](traces.html.md)
* [Domain models and CAD](domains.html.md)
* [Documents](documents.html.md)
* [Repos and workspace](repos.html.md)
* [Checks, CI and evidence](checks.html.md)
* [Workflow and agents](workflow.html.md)
* [Scope and iterations](scope.html.md)

## All decisions

<a id="needtable-explanation/decisions/index-0"></a>

| ID                                                                     | Old ID   | Title                                                                    | Status     | Date       |
|------------------------------------------------------------------------|----------|--------------------------------------------------------------------------|------------|------------|
| [XD-ADR-0001](method.html.md#XD-ADR-0001) | D1       | SysML v2 textual notation for the system model                           | accepted   | 2026-11-14 |
| [XD-ADR-0002](method.html.md#XD-ADR-0002) | D2       | Views as drawio files rendered from the model                            | revised    | 2026-11-14 |
| [XD-ADR-0003](workflow.html.md#XD-ADR-0003) | D3       | Agents are first-class                                                   | accepted   | 2026-11-14 |
| [XD-ADR-0004](traces.html.md#XD-ADR-0004) | D5       | Trace rule: the concrete side holds the link                             | accepted   | 2026-11-14 |
| [XD-ADR-0005](method.html.md#XD-ADR-0005) | D6       | Requirements in sphinx-needs                                             | accepted   | 2026-11-14 |
| [XD-ADR-0006](repos.html.md#XD-ADR-0006) | D7       | A multi-repo workspace with west                                         | accepted   | 2026-11-14 |
| [XD-ADR-0007](method.html.md#XD-ADR-0007) | D9       | SYSMOD is the main method reference                                      | accepted   | 2026-11-14 |
| [XD-ADR-0008](method.html.md#XD-ADR-0008) | D11      | Prototypes are first-class                                               | accepted   | 2026-11-14 |
| [XD-ADR-0009](method.html.md#XD-ADR-0009) | D12      | Requirements use EARS                                                    | accepted   | 2026-11-14 |
| [XD-ADR-0010](documents.html.md#XD-ADR-0010) | D13      | The framework has its own Sphinx documentation                           | accepted   | 2026-11-14 |
| [XD-ADR-0011](repos.html.md#XD-ADR-0011) | D14      | A dedicated manifest repo                                                | accepted   | 2026-11-14 |
| [XD-ADR-0012](checks.html.md#XD-ADR-0012) | D15      | GitHub, GitHub Actions and pull requests                                 | accepted   | 2026-11-14 |
| [XD-ADR-0013](traces.html.md#XD-ADR-0013) | D17      | A new ID prefix scheme                                                   | accepted   | 2026-11-14 |
| [XD-ADR-0014](checks.html.md#XD-ADR-0014) | D19      | Tool versions of the reference machine                                   | accepted   | 2026-11-14 |
| [XD-ADR-0015](documents.html.md#XD-ADR-0015) | D20      | All content is in English                                                | accepted   | 2026-11-14 |
| [XD-ADR-0016](documents.html.md#XD-ADR-0016) | D21      | A set of linked Sphinx documents                                         | accepted   | 2026-11-14 |
| [XD-ADR-0017](documents.html.md#XD-ADR-0017) | D22      | Documents extract content from the models                                | accepted   | 2026-11-14 |
| [XD-ADR-0018](scope.html.md#XD-ADR-0018) | D23      | CAM data from CAD data is a framework task                               | revised    | 2026-11-14 |
| [XD-ADR-0019](scope.html.md#XD-ADR-0019) | D24      | All design outputs go into a bundle                                      | revised    | 2026-11-14 |
| [XD-ADR-0020](documents.html.md#XD-ADR-0020) | D25      | zdocs links the documents                                                | accepted   | 2026-11-14 |
| [XD-ADR-0021](documents.html.md#XD-ADR-0021) | D26      | One zdocs registry per repo, the full set in the manifest repo           | revised    | 2026-11-14 |
| [XD-ADR-0022](documents.html.md#XD-ADR-0022) | D27      | More documents: needs, test specs, prototype setups                      | accepted   | 2026-11-14 |
| [XD-ADR-0023](traces.html.md#XD-ADR-0023) | D29      | Trace IDs live inside the CAD files                                      | revised    | 2026-11-14 |
| [XD-ADR-0024](scope.html.md#XD-ADR-0024) | D30      | ME CAM output is 3MF and STL plus print settings                         | accepted   | 2026-11-14 |
| [XD-ADR-0025](checks.html.md#XD-ADR-0025) | D31      | Generated outputs are built by CI                                        | revised    | 2026-11-14 |
| [XD-ADR-0026](scope.html.md#XD-ADR-0026) | D32      | A bundle is one tag of the manifest repo                                 | superseded | 2026-11-14 |
| [XD-ADR-0027](documents.html.md#XD-ADR-0027) | D33      | No document control in iteration 1                                       | accepted   | 2026-11-14 |
| [XD-ADR-0028](documents.html.md#XD-ADR-0028) | D34      | Missing zdocs features become Sphinx extensions in xdmod                 | accepted   | 2026-11-14 |
| [XD-ADR-0029](documents.html.md#XD-ADR-0029) | D35      | Upstream documents are built locally                                     | accepted   | 2026-11-14 |
| [XD-ADR-0030](traces.html.md#XD-ADR-0030) | D36      | Link-type table and interface elements                                   | revised    | 2026-11-14 |
| [XD-ADR-0031](method.html.md#XD-ADR-0031) | D37      | Prototype and product are variants                                       | revised    | 2026-11-14 |
| [XD-ADR-0032](checks.html.md#XD-ADR-0032) | D38      | drawio files are committed and checked                                   | accepted   | 2026-11-14 |
| [XD-ADR-0033](repos.html.md#XD-ADR-0033) | D39      | The manifest is the only place that pins revisions                       | accepted   | 2026-11-14 |
| [XD-ADR-0034](repos.html.md#XD-ADR-0034) | D40      | Terms: baseline and bundle                                               | accepted   | 2026-11-14 |
| [XD-ADR-0035](scope.html.md#XD-ADR-0035) | D41      | FreeCAD storage is decided after research                                | accepted   | 2026-11-14 |
| [XD-ADR-0036](method.html.md#XD-ADR-0036) | D42      | Read-only requirement stubs in SysML                                     | accepted   | 2026-11-14 |
| [XD-ADR-0037](scope.html.md#XD-ADR-0037) | D43      | Scope moved to iteration 2                                               | revised    | 2026-11-14 |
| [XD-ADR-0038](checks.html.md#XD-ADR-0038) | D44      | Study affirmatrix for suspect links                                      | accepted   | 2026-11-14 |
| [XD-ADR-0039](method.html.md#XD-ADR-0039) | D45      | EARS for system and domain requirements                                  | accepted   | 2026-11-14 |
| [XD-ADR-0040](checks.html.md#XD-ADR-0040) | D46      | Every check also runs locally                                            | accepted   | 2026-11-14 |
| [XD-ADR-0041](checks.html.md#XD-ADR-0041) | D47      | GitHub CI builds docs and runs trace checks only                         | accepted   | 2026-11-14 |
| [XD-ADR-0042](repos.html.md#XD-ADR-0042) | D49      | Names: XDMOD, -trix tools, robarm- repos                                 | accepted   | 2026-11-14 |
| [XD-ADR-0043](workflow.html.md#XD-ADR-0043) | D50      | Trunk-based merging with rebase                                          | accepted   | 2026-11-14 |
| [XD-ADR-0044](workflow.html.md#XD-ADR-0044) | D51      | Agents work under the user's account                                     | accepted   | 2026-11-14 |
| [XD-ADR-0045](workflow.html.md#XD-ADR-0045) | D52      | One branch name across repos                                             | accepted   | 2026-11-14 |
| [XD-ADR-0046](workflow.html.md#XD-ADR-0046) | D53      | Planning with plan.md, issues and PRs                                    | accepted   | 2026-11-14 |
| [XD-ADR-0047](repos.html.md#XD-ADR-0047) | D54      | SemVer tags and baseline tags                                            | accepted   | 2026-11-14 |
| [XD-ADR-0048](documents.html.md#XD-ADR-0048) | D55      | Docs hosting on GitHub Pages with versions                               | accepted   | 2026-11-14 |
| [XD-ADR-0049](checks.html.md#XD-ADR-0049) | D56      | CI runs without CAD content                                              | accepted   | 2026-11-14 |
| [XD-ADR-0050](checks.html.md#XD-ADR-0050) | D57      | HIL evidence on an orphan branch                                         | revised    | 2026-11-14 |
| [XD-ADR-0051](workflow.html.md#XD-ADR-0051) | D58      | Only a human's commit affirms                                            | accepted   | 2026-11-14 |
| [XD-ADR-0052](checks.html.md#XD-ADR-0052) | D59      | affirmatrix is adapted through upstream issues and PRs                   | accepted   | 2026-11-14 |
| [XD-ADR-0053](checks.html.md#XD-ADR-0053) | D60      | Evidence only from main or baseline commits                              | accepted   | 2026-11-14 |
| [XD-ADR-0054](checks.html.md#XD-ADR-0054) | D61      | A bump bot for manifest pins                                             | accepted   | 2026-11-14 |
| [XD-ADR-0055](documents.html.md#XD-ADR-0055) | D62      | zdocs gaps are fixed upstream                                            | accepted   | 2026-11-14 |
| [XD-ADR-0056](checks.html.md#XD-ADR-0056) | D63      | FreeCAD files uncompressed, with textconv and a review report            | accepted   | 2026-11-14 |
| [XD-ADR-0057](traces.html.md#XD-ADR-0057) | D64      | Small corrections from research                                          | accepted   | 2026-11-14 |
| [XD-ADR-0058](method.html.md#XD-ADR-0058) | D65      | SysML toolchain: the OMG Pilot Implementation                            | accepted   | 2026-11-14 |
| [XD-ADR-0059](repos.html.md#XD-ADR-0059) | D66      | xdmod is in every workspace                                              | accepted   | 2026-11-14 |
| [XD-ADR-0060](repos.html.md#XD-ADR-0060) | D67      | All commands run from the workspace root                                 | accepted   | 2026-11-14 |
| [XD-ADR-0061](repos.html.md#XD-ADR-0061) | D68      | One west topdir at the workspace root                                    | accepted   | 2026-11-14 |
| [XD-ADR-0062](repos.html.md#XD-ADR-0062) | D69      | Agent material in each repo's claude/ folder                             | accepted   | 2026-11-14 |
| [XD-ADR-0063](repos.html.md#XD-ADR-0063) | D70      | The planning folder moves into xdmod                                     | accepted   | 2026-11-14 |
| [XD-ADR-0064](checks.html.md#XD-ADR-0064) | D71      | A memory limit and a timeout for every tool                              | accepted   | 2026-11-14 |
| [XD-ADR-0065](workflow.html.md#XD-ADR-0065) | D72      | Provenance trailer on GitHub posts                                       | accepted   | 2026-11-14 |
| [XD-ADR-0066](repos.html.md#XD-ADR-0066) | D73      | An integration repo for system tests and HIL                             | accepted   | 2026-11-14 |
| [XD-ADR-0067](traces.html.md#XD-ADR-0067) | D74      | Prototype wiring is EE content                                           | revised    | 2026-11-14 |
| [XD-ADR-0068](traces.html.md#XD-ADR-0068) | D75      | A grace period for retired needs                                         | accepted   | 2026-11-14 |
| [XD-ADR-0069](method.html.md#XD-ADR-0069) | D76      | SW architecture in rst in iteration 1                                    | accepted   | 2026-11-14 |
| [XD-ADR-0070](traces.html.md#XD-ADR-0070) | D77      | Code units implement design elements                                     | accepted   | 2026-11-14 |
| [XD-ADR-0071](traces.html.md#XD-ADR-0071) | D78      | ID format DOMAIN-KIND-NNNN                                               | accepted   | 2026-11-14 |
| [XD-ADR-0072](traces.html.md#XD-ADR-0072) | D79      | No project code in the sources                                           | accepted   | 2026-11-14 |
| [XD-ADR-0073](traces.html.md#XD-ADR-0073) | D80      | SW test case IDs come from the ledger                                    | accepted   | 2026-11-14 |
| [XD-ADR-0074](method.html.md#XD-ADR-0074) | D81      | The problem statement is a stakeholder need                              | accepted   | 2026-11-14 |
| [XD-ADR-0075](method.html.md#XD-ADR-0075) | D82      | System objectives are stakeholder needs                                  | accepted   | 2026-11-14 |
| [XD-ADR-0076](method.html.md#XD-ADR-0076) | D83      | Requirement values are need fields                                       | accepted   | 2026-11-14 |
| [XD-ADR-0077](method.html.md#XD-ADR-0077) | D84      | The SYSMOD library is a pinned west project                              | accepted   | 2026-11-14 |
| [XD-ADR-0078](method.html.md#XD-ADR-0078) | D85      | A short functional architecture                                          | accepted   | 2026-11-14 |
| [XD-ADR-0079](repos.html.md#XD-ADR-0079) | D86      | West submanifests and project groups                                     | accepted   | 2026-11-14 |
| [XD-ADR-0080](repos.html.md#XD-ADR-0080) | D88      | Pinned, isolated component libraries                                     | accepted   | 2026-11-14 |
| [XD-ADR-0081](checks.html.md#XD-ADR-0081) | D89      | The bump bot is a scheduled poll                                         | accepted   | 2026-11-14 |
| [XD-ADR-0082](repos.html.md#XD-ADR-0082) | D90      | The integration role                                                     | accepted   | 2026-11-14 |
| [XD-ADR-0083](repos.html.md#XD-ADR-0083) | D91      | Workspace paths                                                          | accepted   | 2026-11-14 |
| [XD-ADR-0084](repos.html.md#XD-ADR-0084) | D93      | A minimal default group filter                                           | accepted   | 2026-11-14 |
| [XD-ADR-0085](method.html.md#XD-ADR-0085) | D94      | View definitions live in the model                                       | accepted   | 2026-11-14 |
| [XD-ADR-0086](method.html.md#XD-ADR-0086) | D95      | Trace graphs with needflow                                               | accepted   | 2026-11-14 |
| [XD-ADR-0087](method.html.md#XD-ADR-0087) | D96      | Views are committed as editable SVG                                      | accepted   | 2026-11-14 |
| [XD-ADR-0088](method.html.md#XD-ADR-0088) | D97      | drawio desktop 31.7.0                                                    | accepted   | 2026-11-14 |
| [XD-ADR-0089](checks.html.md#XD-ADR-0089) | D98      | One framework tool: curatrix                                             | accepted   | 2026-11-14 |
| [XD-ADR-0090](checks.html.md#XD-ADR-0090) | D99      | Verification coverage is a warning in iteration 1                        | accepted   | 2026-11-14 |
| [XD-ADR-0091](checks.html.md#XD-ADR-0091) | D100     | Pre-commit hooks                                                         | accepted   | 2026-11-14 |
| [XD-ADR-0092](method.html.md#XD-ADR-0092) | D102     | Variants follow VAMOS through PLEML                                      | accepted   | 2026-11-14 |
| [XD-ADR-0093](method.html.md#XD-ADR-0093) | D103     | Variant fields configs, where and config                                 | accepted   | 2026-11-14 |
| [XD-ADR-0094](method.html.md#XD-ADR-0094) | D104     | Coverage per configuration                                               | accepted   | 2026-11-14 |
| [XD-ADR-0095](method.html.md#XD-ADR-0095) | D105     | Variant rules                                                            | accepted   | 2026-11-14 |
| [XD-ADR-0096](method.html.md#XD-ADR-0096) | D106     | One variant-aware document set                                           | accepted   | 2026-11-14 |
| [XD-ADR-0097](method.html.md#XD-ADR-0097) | D107     | IDs for configurations and features                                      | accepted   | 2026-11-14 |
| [XD-ADR-0098](scope.html.md#XD-ADR-0098) | D108     | FreeCAD review report as a Pages preview                                 | revised    | 2026-11-14 |
| [XD-ADR-0099](documents.html.md#XD-ADR-0099) | D109     | Test reports are separate documents                                      | accepted   | 2026-11-14 |
| [XD-ADR-0100](checks.html.md#XD-ADR-0100) | D110     | CAD-derived needs are committed                                          | accepted   | 2026-11-14 |
| [XD-ADR-0101](documents.html.md#XD-ADR-0101) | D111     | The XDMOD manual is part of the full set                                 | accepted   | 2026-11-14 |
| [XD-ADR-0102](documents.html.md#XD-ADR-0102) | D112     | One EE document per PCBA and per prototype configuration                 | revised    | 2026-11-14 |
| [XD-ADR-0103](repos.html.md#XD-ADR-0103) | D113     | The bootstrap assembles .claude/                                         | accepted   | 2026-11-14 |
| [XD-ADR-0104](traces.html.md#XD-ADR-0104) | D115     | Tests live by what they verify                                           | accepted   | 2026-11-14 |
| [XD-ADR-0105](checks.html.md#XD-ADR-0105) | D116     | The command layer is only curatrix                                       | accepted   | 2026-11-14 |
| [XD-ADR-0106](checks.html.md#XD-ADR-0106) | D117     | GUI tools get a memory limit only                                        | accepted   | 2026-11-14 |
| [XD-ADR-0107](repos.html.md#XD-ADR-0107) | D118     | bootstrap.sh is a copy of the xdmod template                             | accepted   | 2026-11-14 |
| [XD-ADR-0108](workflow.html.md#XD-ADR-0108) | D119     | Sign-off by agents                                                       | accepted   | 2026-11-14 |
| [XD-ADR-0109](traces.html.md#XD-ADR-0109) | D120     | Decisions become sphinx-needs                                            | accepted   | 2026-11-14 |
| [XD-ADR-0110](traces.html.md#XD-ADR-0110) | D121     | Method rules are needs                                                   | accepted   | 2026-11-14 |
| [XD-ADR-0111](documents.html.md#XD-ADR-0111) | D122     | Agent-readable docs with sphinx-llm                                      | accepted   | 2026-11-14 |
| [XD-ADR-0112](workflow.html.md#XD-ADR-0112) | D123     | GitHub admin by agents only after approval                               | accepted   | 2026-11-14 |
| [XD-ADR-0113](workflow.html.md#XD-ADR-0113) | D124     | Posting approval outside our repos                                       | accepted   | 2026-11-14 |
| [XD-ADR-0114](workflow.html.md#XD-ADR-0114) | D125     | Parallel agents work in git worktrees                                    | accepted   | 2026-11-14 |
| [XD-ADR-0115](workflow.html.md#XD-ADR-0115) | D126     | Every PR gets an agent review                                            | accepted   | 2026-11-14 |
| [XD-ADR-0116](checks.html.md#XD-ADR-0116) | D127     | PR CI sibling resolution                                                 | accepted   | 2026-11-14 |
| [XD-ADR-0117](method.html.md#XD-ADR-0117) | D128     | The definition holds the trace ID                                        | accepted   | 2026-11-14 |
| [XD-ADR-0118](method.html.md#XD-ADR-0118) | D129     | Only linked model elements become needs                                  | accepted   | 2026-11-14 |
| [XD-ADR-0119](traces.html.md#XD-ADR-0119) | D130     | Retiring generated needs                                                 | accepted   | 2026-11-14 |
| [XD-ADR-0120](checks.html.md#XD-ADR-0120) | D131     | Evidence validity                                                        | accepted   | 2026-11-14 |
| [XD-ADR-0121](checks.html.md#XD-ADR-0121) | D132     | Suspect links before affirmatrix                                         | accepted   | 2026-11-14 |
| [XD-ADR-0122](traces.html.md#XD-ADR-0122) | D133     | ID collisions show up as git conflicts                                   | accepted   | 2026-11-14 |
| [XD-ADR-0123](workflow.html.md#XD-ADR-0123) | D134     | Agent limits are policy only in iteration 1                              | accepted   | 2026-11-14 |
| [XD-ADR-0124](scope.html.md#XD-ADR-0124) | D135     | Scope cuts for iteration 1                                               | revised    | 2026-11-14 |
| [XD-ADR-0125](checks.html.md#XD-ADR-0125) |          | Checks that bite                                                         | accepted   | 2026-11-17 |
| [XD-ADR-0126](checks.html.md#XD-ADR-0126) |          | One accepted.yaml format, with Accepted-by                               | accepted   | 2026-11-17 |
| [XD-ADR-0127](documents.html.md#XD-ADR-0127) |          | WireViz for harnesses                                                    | accepted   | 2026-11-17 |
| [XD-ADR-0128](domains.html.md#XD-ADR-0128) |          | The domain model owns the IDs of boards, assemblies, ports and harnesses | accepted   | 2026-11-17 |
| [XD-ADR-0129](documents.html.md#XD-ADR-0129) |          | One document per board, harness and assembly                             | accepted   | 2026-11-17 |
| [XD-ADR-0130](domains.html.md#XD-ADR-0130) |          | Domain repos refine the system model by specialization                   | accepted   | 2026-11-17 |
| [XD-ADR-0131](domains.html.md#XD-ADR-0131) |          | SW reads the board pin maps from EE                                      | accepted   | 2026-11-17 |
| [XD-ADR-0132](domains.html.md#XD-ADR-0132) |          | curatrix checks conformance and derives the links                        | accepted   | 2026-11-17 |
| [XD-ADR-0133](domains.html.md#XD-ADR-0133) |          | Need kinds EE-PORT, ME-PORT and EE-HAR                                   | accepted   | 2026-11-17 |
| [XD-ADR-0134](domains.html.md#XD-ADR-0134) |          | ME writes board geometry into KiCad in a co-design change                | proposed   | 2026-11-17 |
| [XD-ADR-0135](domains.html.md#XD-ADR-0135) |          | External parts and prototype projects                                    | accepted   | 2026-11-17 |
| [XD-ADR-0136](domains.html.md#XD-ADR-0136) |          | Variants: the domain variant names what it serves                        | accepted   | 2026-11-17 |
| [XD-ADR-0137](domains.html.md#XD-ADR-0137) |          | FreeCAD assemblies: a skeleton document, values from the model           | accepted   | 2026-11-17 |
| [XD-ADR-0138](domains.html.md#XD-ADR-0138) |          | Who owns instance counts                                                 | accepted   | 2026-11-17 |
| [XD-ADR-0139](domains.html.md#XD-ADR-0139) |          | A board library repo for ME                                              | proposed   | 2026-11-17 |
| [XD-ADR-0140](repos.html.md#XD-ADR-0140) |          | Tags per board, assembly and harness, made by the owner                  | accepted   | 2026-11-17 |
| [XD-ADR-0141](repos.html.md#XD-ADR-0141) |          | Roles: EE gets FreeCAD, ME gets the KiCad files, SW gets the EE model    | accepted   | 2026-11-17 |
| [XD-ADR-0142](scope.html.md#XD-ADR-0142) |          | EE design output in iteration 1                                          | accepted   | 2026-11-17 |
| [XD-ADR-0143](scope.html.md#XD-ADR-0143) |          | ME design output in iteration 1                                          | accepted   | 2026-11-17 |
| [XD-ADR-0144](scope.html.md#XD-ADR-0144) |          | A PCB layout in iteration 1, without routing                             | accepted   | 2026-11-17 |
| [XD-ADR-0145](repos.html.md#XD-ADR-0145) |          | KiCad and FreeCAD never run outside curatrix; shims in .venv/bin         | accepted   | 2026-11-17 |
