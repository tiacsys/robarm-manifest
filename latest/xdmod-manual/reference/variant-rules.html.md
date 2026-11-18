<a id="ref-variant-rules"></a>

# Variant rules

These rules check a variant model: the feature model, the product models of the configurations,
and the trace links between variant elements ([*Variant rules (XD-ADR-0095)*](../explanation/decisions/method.html.md#XD-ADR-0095)). All are errors. curatrix checks them
with [*variant rules F1, F2, V1-V5 (XD-CHECK-0009)*](checks.html.md#XD-CHECK-0009) (`curatrix pleml check` runs them alone; `curatrix variants` without `list` is its old name, kept for one release); the SysML Pilot checks none of them.
They run locally, in PR CI of the systems engineering repo, and in the full set. Background:
[Variants](../explanation/variants.html.md).

<a id="needtable-reference/variant-rules-0"></a>

| ID                                                                       | Rule   | Title                                          |
|--------------------------------------------------------------------------|--------|------------------------------------------------|
| [XD-RULE-0021](../explanation/rules/variants.html.md#XD-RULE-0021) | F1     | A configuration respects its feature tree      |
| [XD-RULE-0022](../explanation/rules/variants.html.md#XD-RULE-0022) | F2     | Feature constraints hold                       |
| [XD-RULE-0023](../explanation/rules/variants.html.md#XD-RULE-0023) | V1     | One product model per configuration            |
| [XD-RULE-0024](../explanation/rules/variants.html.md#XD-RULE-0024) | V2     | Every variation is bound                       |
| [XD-RULE-0025](../explanation/rules/variants.html.md#XD-RULE-0025) | V3     | A variation is bound to its own variant        |
| [XD-RULE-0026](../explanation/rules/variants.html.md#XD-RULE-0026) | V4     | The chosen variant is enabled                  |
| [XD-RULE-0027](../explanation/rules/variants.html.md#XD-RULE-0027) | V5     | Exactly one variant per variation              |
| [XD-RULE-0028](../explanation/rules/variants.html.md#XD-RULE-0028) | V6     | Model constraints hold in each product model   |
| [XD-RULE-0029](../explanation/rules/variants.html.md#XD-RULE-0029) | T1     | configs matches the source                     |
| [XD-RULE-0030](../explanation/rules/variants.html.md#XD-RULE-0030) | T2     | realizes respects configurations               |
| [XD-RULE-0031](../explanation/rules/variants.html.md#XD-RULE-0031) | T3     | Coverage counts per configuration              |
| [XD-RULE-0048](../explanation/rules/variants.html.md#XD-RULE-0048) |        | One domain variant per configuration and usage |

## Notes

- [*A configuration respects it... (XD-RULE-0021)*](../explanation/rules/variants.html.md#XD-RULE-0021) and [*Feature constraints hold (XD-RULE-0022)*](../explanation/rules/variants.html.md#XD-RULE-0022) check the **feature model**: a configuration sets only features of
  its tree, feature groups keep their multiplicity, and every `requires`, `xor` or
  `implies` constraint holds in every configuration.
- [*One product model per confi... (XD-RULE-0023)*](../explanation/rules/variants.html.md#XD-RULE-0023) to [*Exactly one variant per var... (XD-RULE-0027)*](../explanation/rules/variants.html.md#XD-RULE-0027) check the **product models**: one product model per configuration,
  every variation bound to one of its own variants, the chosen variant enabled by the
  configuration, and exactly one variant enabled per variation.
- [*The chosen variant is enabled (XD-RULE-0026)*](../explanation/rules/variants.html.md#XD-RULE-0026): several feature bindings on one element mean **AND**. PLEML does not say this, so
  it is an XDMOD convention.
- [*Model constraints hold in e... (XD-RULE-0028)*](../explanation/rules/variants.html.md#XD-RULE-0028) checks the `assert constraint` statements of the 150 % model in each product model
  (simple `==`, `implies`, `and`, `or` only).
- [*configs matches the source (XD-RULE-0029)*](../explanation/rules/variants.html.md#XD-RULE-0029) to [*Coverage counts per configu... (XD-RULE-0031)*](../explanation/rules/variants.html.md#XD-RULE-0031) check **traces**: `configs` of a generated need equals what the
  source says; a `realizes` link needs the source’s `configs` to be a subset of the target’s;
  a test result counts for a requirement in a configuration only under the coverage rule
  ([*Coverage per configuration (XD-ADR-0094)*](../explanation/decisions/method.html.md#XD-ADR-0094)).

## What curatrix checks today

Iteration 1 checks [*A configuration respects it... (XD-RULE-0021)*](../explanation/rules/variants.html.md#XD-RULE-0021), [*Feature constraints hold (XD-RULE-0022)*](../explanation/rules/variants.html.md#XD-RULE-0022) and [*One product model per confi... (XD-RULE-0023)*](../explanation/rules/variants.html.md#XD-RULE-0023) to [*Exactly one variant per var... (XD-RULE-0027)*](../explanation/rules/variants.html.md#XD-RULE-0027) ([*Scope cuts for iteration 1 (XD-ADR-0124)*](../explanation/decisions/scope.html.md#XD-ADR-0124)).
[*Model constraints hold in e... (XD-RULE-0028)*](../explanation/rules/variants.html.md#XD-RULE-0028), [*configs matches the source (XD-RULE-0029)*](../explanation/rules/variants.html.md#XD-RULE-0029), [*realizes respects configura... (XD-RULE-0030)*](../explanation/rules/variants.html.md#XD-RULE-0030) and [*Coverage counts per configu... (XD-RULE-0031)*](../explanation/rules/variants.html.md#XD-RULE-0031) come when the product configuration has real
content.

Example (robot arm): a configuration that chooses both `prototypeBuild` and `productBuild`
breaks [*Feature constraints hold (XD-RULE-0022)*](../explanation/rules/variants.html.md#XD-RULE-0022) (the two features are `xor`). A product model that binds the variation
`controller` to `customPcba` in the prototype configuration breaks [*The chosen variant is enabled (XD-RULE-0026)*](../explanation/rules/variants.html.md#XD-RULE-0026), because
`customPcba` is bound to `productBuild`.
