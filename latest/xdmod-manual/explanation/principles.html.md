<a id="expl-principles"></a>

# Principles

XDMOD rests on a few ideas. Most rules in this manual follow from them.

## The concrete side holds the link

A trace link is written on the **more concrete** artifact and points to the more abstract one
([*Trace rule: the concrete si... (XD-ADR-0004)*](decisions/traces.html.md#XD-ADR-0004), refined by [*Link-type table and interfa... (XD-ADR-0030)*](decisions/traces.html.md#XD-ADR-0030)). In the V-model, links point from right to left and from
bottom to top: a test case says what it verifies, a design element says what it realizes, a
domain requirement says what it refines. The abstract side never lists its children. Backlinks
such as “refined by” or “verified by” are only ever computed by the tools ([*The concrete side holds the... (XD-RULE-0001)*](rules/trace.html.md#XD-RULE-0001)).

Why? The concrete artifact is the one that changes most often, and its author knows what it is
for. An upstream document stays stable while downstream work goes on, and many repos can add
links to it in parallel without touching it.

Each link type belongs to the need type that owns it ([*Link types are declared on ... (XD-RULE-0002)*](rules/trace.html.md#XD-RULE-0002)). There is no global link
table. A link written on the wrong side, to an unknown ID or to a wrong target type fails the
build. Peer domains (for example EE and SW) never link to each other: they both link to a shared
interface need in the systems engineering repo ([*Peer interfaces live in sys... (XD-RULE-0003)*](rules/trace.html.md#XD-RULE-0003)). Allocation is stored on the concrete
side, too ([*Allocation is stored on the... (XD-RULE-0004)*](rules/trace.html.md#XD-RULE-0004)).

## Generate, commit, check

Many files are made by tools: SysML stubs for requirements, needs extracted from the model and
from CAD files, views of the model. XDMOD **commits** these files and **checks** that they still
match their sources ([*Generated files are committ... (XD-RULE-0033)*](rules/checks.html.md#XD-RULE-0033)). That has three benefits:

- Reviewers see the generated change in the pull request, next to the change that caused it.
- CI does not need the heavy tools (Java, KiCad, FreeCAD) to see the full trace graph
  ([*CAD-derived needs are commi... (XD-ADR-0100)*](decisions/checks.html.md#XD-ADR-0100)).
- A stale file is a check failure, not a silent error.

Generated needs follow the same rules as authored needs ([*Generated needs follow the ... (XD-RULE-0006)*](rules/trace.html.md#XD-RULE-0006)).

## Text first, for people and agents

Everything that people review is text in git: reStructuredText for needs and documents
([*Requirements in sphinx-needs (XD-ADR-0005)*](decisions/method.html.md#XD-ADR-0005)), SysML v2 textual notation for the model ([*SysML v2 textual notation f... (XD-ADR-0001)*](decisions/method.html.md#XD-ADR-0001)), uncompressed FreeCAD files
and drawio views ([*Design files are stored unc... (XD-RULE-0039)*](rules/checks.html.md#XD-RULE-0039)). Agents edit and review this content the same way engineers do
([*Agents are first-class (XD-ADR-0003)*](decisions/workflow.html.md#XD-ADR-0003)). Diffs are readable, merges are possible, and every change goes through a pull
request.

## Documents come from the models

Documents pull content out of the design models, the way API documentation comes from code
comments ([*Documents extract content f... (XD-ADR-0017)*](decisions/documents.html.md#XD-ADR-0017)). Authored rst gives the structure and the prose; Sphinx extensions add
tables, pictures and needs from SysML, KiCad, FreeCAD, code and test results.

## Every check runs locally

Every check that CI runs can also run on your machine, with one command per repo, from the
workspace root ([*Every check also runs locally (XD-ADR-0040)*](decisions/checks.html.md#XD-ADR-0040), [*Every check runs locally (XD-RULE-0032)*](rules/checks.html.md#XD-RULE-0032)). Every tool runs under a memory limit and a timeout
([*A memory limit and a timeou... (XD-ADR-0064)*](decisions/checks.html.md#XD-ADR-0064), [*Every tool runs under limits (XD-RULE-0044)*](rules/checks.html.md#XD-RULE-0044)), so a runaway tool cannot stall the machine or other agents.

## IDs are stable

Every need has an ID like `SYS-REQ-0012` from the repo’s ledger ([*ID format DOMAIN-KIND-NNNN (XD-ADR-0071)*](decisions/traces.html.md#XD-ADR-0071)). An ID never
changes when its need is renamed or moved, and it is never issued again ([*IDs are never reused; retir... (XD-RULE-0020)*](rules/ids.html.md#XD-RULE-0020)). See
[ID scheme](../reference/id-scheme.html.md).
