<a id="expl-variants"></a>

# Variants

A project often builds more than one product from one design: a prototype and a product, a
small and a large version. XDMOD models these as **variants of one product line**, following
VAMOS ([*Variants follow VAMOS throu... (XD-ADR-0092)*](decisions/method.html.md#XD-ADR-0092)).

## VAMOS and PLEML

VAMOS, by Tim Weilkiens, is a variant method for SysML v1. XDMOD uses **PLEML** (MBSE4U, MIT
licence), its SysML v2 successor. PLEML is a west project pinned at a commit, next to the SYSMOD
library. SYSMOD v5 itself has no variant concept.

The parts of a variant model:

| Part                       | What it is                                                                                                                  |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Core                       | The variant-free functional and logical architecture.                                                                       |
| Feature model              | Features and feature groups, with constraints such as `requires` and `xor`.                                                 |
| 150 % product architecture | The product architecture with **variation points**. Each variation has variants, and<br/>each variant is bound to features. |
| Configurations             | A choice of features. Each configuration has exactly one product model.                                                     |

Example (robot arm): the feature group `buildKind` has the features `prototypeBuild` and
`productBuild`. The variation `controller` has the variants `nucleoBreakouts` (bound to
`prototypeBuild`) and `customPcba` (bound to `productBuild`). The configurations are
`prototype` (`SYS-CFG-0001`) and `product` (`SYS-CFG-0002`).

## Variant fields on needs

Needs carry their variant information in fields ([*Variant fields configs, whe... (XD-ADR-0093)*](decisions/method.html.md#XD-ADR-0093), [*Variants are expressed with... (XD-RULE-0005)*](rules/trace.html.md#XD-RULE-0005)):

- `configs` on product-layer system elements, domain design elements and test cases: the
  configurations the element belongs to. Empty means all.
- `where` on requirements: a feature condition, matching the EARS “Where <feature>, the system
  shall …” pattern. Empty means all configurations.
- `verification_scope` on requirements: `logical` or `config` (see below).
- `config` on test results: the one configuration the run was made on.

Configurations and features have their own ID kinds, `SYS-CFG` and `SYS-FEAT`
([*IDs for configurations and ... (XD-ADR-0097)*](decisions/method.html.md#XD-ADR-0097)). They are written as SysML short names.

## Why own checks

The SysML Pilot checks none of the variant rules: in a test it accepted every planted error. So
curatrix checks them itself ([*Variant rules (XD-ADR-0095)*](decisions/method.html.md#XD-ADR-0095), [*variant rules F1, F2, V1-V5 (XD-CHECK-0009)*](../reference/checks.html.md#XD-CHECK-0009)). The rules cover the feature model
([*A configuration respects it... (XD-RULE-0021)*](rules/variants.html.md#XD-RULE-0021), [*Feature constraints hold (XD-RULE-0022)*](rules/variants.html.md#XD-RULE-0022)), the product models ([*One product model per confi... (XD-RULE-0023)*](rules/variants.html.md#XD-RULE-0023) to [*Model constraints hold in e... (XD-RULE-0028)*](rules/variants.html.md#XD-RULE-0028)) and the trace links
([*configs matches the source (XD-RULE-0029)*](rules/variants.html.md#XD-RULE-0029) to [*Coverage counts per configu... (XD-RULE-0031)*](rules/variants.html.md#XD-RULE-0031)). They are listed in [Variant rules](../reference/variant-rules.html.md). Several feature
bindings on one element mean AND ([*The chosen variant is enabled (XD-RULE-0026)*](rules/variants.html.md#XD-RULE-0026)); PLEML does not say this, so it is an XDMOD
convention.

## Coverage per configuration

The coverage report is a requirement × configuration matrix ([*Coverage per configuration (XD-ADR-0094)*](decisions/method.html.md#XD-ADR-0094)). A cell is covered
when:

- `verification_scope: logical`: at least one test result from **any** configuration verifies
  the requirement. Example: SW logic tested on the prototype also counts for the product.
- `verification_scope: config`: at least one result with `config` = C verifies it, for each
  configuration C that the requirement’s `where` selects.

The verification rule [*Every requirement is verified (XD-RULE-0009)*](rules/trace.html.md#XD-RULE-0009) applies per cell.

## One document set

There is **one variant-aware document set** ([*One variant-aware document set (XD-ADR-0096)*](decisions/method.html.md#XD-ADR-0096)), not one set per variant. Documents show
the 150 % content with configuration badges. A generated page per configuration lists the
elements and requirements that apply to it, and its column of the coverage matrix.

## What iteration 1 covers

Iteration 1 starts with one feature group and the rules [*A configuration respects it... (XD-RULE-0021)*](rules/variants.html.md#XD-RULE-0021), [*Feature constraints hold (XD-RULE-0022)*](rules/variants.html.md#XD-RULE-0022) and [*One product model per confi... (XD-RULE-0023)*](rules/variants.html.md#XD-RULE-0023) to
[*Exactly one variant per var... (XD-RULE-0027)*](rules/variants.html.md#XD-RULE-0027) ([*Scope cuts for iteration 1 (XD-ADR-0124)*](decisions/scope.html.md#XD-ADR-0124)). The rule [*Model constraints hold in e... (XD-RULE-0028)*](rules/variants.html.md#XD-RULE-0028), the derivation of `configs` for [*configs matches the source (XD-RULE-0029)*](rules/variants.html.md#XD-RULE-0029), and
the pages per configuration come later.
