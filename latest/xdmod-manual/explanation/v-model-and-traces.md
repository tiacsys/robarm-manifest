<a id="expl-v-model-and-traces"></a>

# The V-model and trace links

XDMOD arranges the work products of a project along a V. The left side goes from stakeholder
needs down to the design of each domain. The right side goes from code and parts up to the system
tests. Trace links connect the two sides and the levels.

## The picture

Links point to the left and upwards. Each arrow is written on the artifact at its tail.

```text
SYS-STH  SYS-NEED <-addresses-- SYS-UC
            ^ refines
         SYS-REQ <------------ verifies ------------ INT-STC <-result_of- TR
            ^ satisfies     ^ refines
         SYS-EL (logical)   |            SYS-IF <-verifies-- INT-ITC <-result_of- TR
            ^ realizes      |               ^ conforms
         SYS-EL (product,  SW-REQ / EE-REQ / ME-REQ <-verifies-- SW-TC / EE-TC / ME-TC <-result_of- TR
                 150 %)          ^ satisfies
            ^ realizes        |
         SW-ARCH / EE-PCBA / EE-CMP / ME-ASM / ME-PART <-refines / part_of- SW-DD / EE-CMP / ME-PART
                                                   ^ implements (+ optional satisfies -> SW-REQ)
                                                SW-IMPL (code)
```

The same links, drawn from the SysML model of XDMOD, are in
[XDMOD as a SysML model](framework-model.md#expl-framework-model) (section *Trace links*).

The exact rules (which type may link to which, and how many links are required) are in
[Trace model](../reference/trace-model.md).

## Who holds the link

The more concrete side holds the link ([*The concrete side holds the... (XD-RULE-0001)*](rules/trace.md#XD-RULE-0001)). A requirement in the SW domain says which
system requirement it refines; a test case says which requirement it verifies; a part says
which system element it realizes. This keeps upstream documents stable while downstream repos
grow.

Peer domains do not link to each other. When EE and SW must agree on a pin map, or EE and ME on
a connector position, the agreement is an **interface** need (`SYS-IF`) in the systems
engineering repo. Both domains link to it with `conforms`, and tests of it are integration
tests ([*Link-type table and interfa... (XD-ADR-0030)*](decisions/traces.md#XD-ADR-0030), [*Tests live by what they verify (XD-ADR-0104)*](decisions/traces.md#XD-ADR-0104)).

Allocation is stored on the concrete side as well: a product element `realizes` the logical
element it was allocated from ([*Allocation is stored on the... (XD-RULE-0004)*](rules/trace.md#XD-RULE-0004)).

## Links across repos

Each repo builds its own documents plus its upstream documents from the west checkout, so a
link into an upstream need resolves in the local build ([*Upstream documents are buil... (XD-ADR-0029)*](decisions/documents.md#XD-ADR-0029)). Rules that need the whole
graph, such as “every system requirement is refined or satisfied” ([*Every system requirement is... (XD-RULE-0008)*](rules/trace.md#XD-RULE-0008)), run in curatrix’s
own graph check, because the sphinx-needs schema skips imported needs. They always run in the
full-set build.

## Graph rules

Beyond the shape of each need, XDMOD checks the graph:

- every system requirement is refined or satisfied ([*Every system requirement is... (XD-RULE-0008)*](rules/trace.md#XD-RULE-0008), [*every SYS-REQ refined or sa... (XD-CHECK-0006)*](../reference/checks.md#XD-CHECK-0006));
- every requirement is verified, per configuration ([*Every requirement is verified (XD-RULE-0009)*](rules/trace.md#XD-RULE-0009), [*every requirement verified ... (XD-CHECK-0007)*](../reference/checks.md#XD-CHECK-0007));
- no orphan design elements ([*No orphan design elements (XD-RULE-0010)*](rules/trace.md#XD-RULE-0010), a schema rule of the strict build, [*docs build strict (zdocs, s... (XD-CHECK-0001)*](../reference/checks.md#XD-CHECK-0001));
- links to retired needs are reported, with a grace period until the next baseline
  ([*Links to retired needs are ... (XD-RULE-0011)*](rules/trace.md#XD-RULE-0011), [*no links to retired needs (... (XD-CHECK-0008)*](../reference/checks.md#XD-CHECK-0008));
- HIL results carry the firmware hash and the pinned SHAs ([*HIL results carry the firmw... (XD-RULE-0012)*](rules/trace.md#XD-RULE-0012), a schema rule of the strict build, [*docs build strict (zdocs, s... (XD-CHECK-0001)*](../reference/checks.md#XD-CHECK-0001)), and only
  results that match the current pins count ([*Only valid evidence counts (XD-RULE-0013)*](rules/trace.md#XD-RULE-0013), [*stale evidence (R5a) (XD-CHECK-0011)*](../reference/checks.md#XD-CHECK-0011));
- suspect links are found and must be confirmed before a baseline ([*Suspect links are reviewed ... (XD-RULE-0014)*](rules/trace.md#XD-RULE-0014), [*suspect links against the l... (XD-CHECK-0024)*](../reference/checks.md#XD-CHECK-0024)).

## Suspect links

A link is **suspect** when its target changed after the link was last confirmed. Example: a
system requirement’s value changes from 50 ms to 20 ms; every SW requirement that refines it may
now be wrong.

Until the suspect-link tool affirmatrix is adapted ([*affirmatrix is adapted thro... (XD-ADR-0052)*](decisions/checks.md#XD-ADR-0052)), “last confirmed” means the
`needs.json` of the last baseline (for pull requests: of `main`). A change is a change in the
hashed fields: title, content, `status`, value fields and links ([*Suspect links before affirm... (XD-ADR-0121)*](decisions/checks.md#XD-ADR-0121)). In a pull
request, `curatrix needs-diff` lists the changed needs and the links that became suspect
([*needs-diff against the base... (XD-CHECK-0023)*](../reference/checks.md#XD-CHECK-0023)). Before a baseline every suspect link must be confirmed. Agents may prepare the
confirmation, but only a person’s commit counts ([*Only a human's commit affirms (XD-ADR-0051)*](decisions/workflow.md#XD-ADR-0051)).

## Retiring needs

A need is never just deleted. It first gets `status: retired` ([*Small corrections from rese... (XD-ADR-0057)*](decisions/traces.md#XD-ADR-0057) (e)). Links to it
stay valid until the next baseline, and the checks report them as warnings ([*A grace period for retired ... (XD-ADR-0068)*](decisions/traces.md#XD-ADR-0068)). The
baseline build fails while any such link remains. Generated needs take their status from their
source; if a source element is deleted without being retired, curatrix keeps a tombstone until
the next baseline ([*Retiring generated needs (XD-ADR-0119)*](decisions/traces.md#XD-ADR-0119), [*tombstones of deleted gener... (XD-CHECK-0012)*](../reference/checks.md#XD-CHECK-0012)).

## Evidence

Test results (`TR` needs) are the evidence on the right side of the V. A result counts only if
the SHAs it recorded (and the firmware hash) match the current pins on `main` or the baseline
being built ([*Evidence validity (XD-ADR-0120)*](decisions/checks.md#XD-ADR-0120)). Evidence is recorded only from commits on `main` or baseline tags;
runs on pull-request branches are previews ([*Evidence only from main or ... (XD-ADR-0053)*](decisions/checks.md#XD-ADR-0053)). HIL run records live on an orphan
evidence branch in the integration repo ([*An integration repo for sys... (XD-ADR-0066)*](decisions/repos.md#XD-ADR-0066)).

## Coverage per configuration

When a product line has several configurations, coverage is a matrix: requirements down,
configurations across ([*Coverage per configuration (XD-ADR-0094)*](decisions/method.md#XD-ADR-0094)). A requirement’s `verification_scope` says whether
evidence from any configuration counts (`logical`) or whether each applicable configuration
needs its own evidence (`config`). See [Variants](variants.md).
