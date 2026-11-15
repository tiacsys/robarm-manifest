<a id="howto-add-a-configuration"></a>

# Add a feature or configuration

Use this guide when the product line gets a new feature, a new variant at a variation point, or
a new configuration. Variants follow VAMOS in SysML v2 through PLEML ([*Variants follow VAMOS throu... (XD-ADR-0092)*](../explanation/decisions/method.html.md#XD-ADR-0092)).

## Steps

1. **Feature.** Add it to the feature model (`features.sysml`) with a `SYS-FEAT` short-name
   ID ([*IDs for configurations and ... (XD-ADR-0097)*](../explanation/decisions/method.html.md#XD-ADR-0097)). Add constraints such as `requires` or `xor` there.
2. **Variant.** In the 150 % product architecture (`product.sysml`), add the variant to its
   `variation part` and bind it to features with PLEML feature bindings. Several bindings on
   one element mean AND ([*The chosen variant is enabled (XD-RULE-0026)*](../explanation/rules/variants.html.md#XD-RULE-0026)).
3. **Configuration.** In `configs.sysml`, add the configuration with a `SYS-CFG` ID and
   exactly one product model that binds every variation ([*One product model per confi... (XD-RULE-0023)*](../explanation/rules/variants.html.md#XD-RULE-0023), [*Every variation is bound (XD-RULE-0024)*](../explanation/rules/variants.html.md#XD-RULE-0024)).
4. **Fields.** Elements that belong only to some configurations carry `configs`; requirements
   that apply only to some carry `where` ([*Variant fields configs, whe... (XD-ADR-0093)*](../explanation/decisions/method.html.md#XD-ADR-0093), [*Variants are expressed with... (XD-RULE-0005)*](../explanation/rules/trace.html.md#XD-RULE-0005)). Set `verification_scope`
   on requirements ([*Coverage per configuration (XD-ADR-0094)*](../explanation/decisions/method.html.md#XD-ADR-0094)).
5. Issue the IDs and regenerate:
   ```sh
   curatrix ids fix robarm-syseng
   curatrix gen model robarm-syseng
   curatrix variants robarm-syseng -v
   ```

## Checks

- [*variant rules F1, F2, V1-V5 (XD-CHECK-0009)*](../reference/checks.html.md#XD-CHECK-0009) runs the variant rules [*A configuration respects it... (XD-RULE-0021)*](../explanation/rules/variants.html.md#XD-RULE-0021), [*Feature constraints hold (XD-RULE-0022)*](../explanation/rules/variants.html.md#XD-RULE-0022) and [*One product model per confi... (XD-RULE-0023)*](../explanation/rules/variants.html.md#XD-RULE-0023) to [*Exactly one variant per var... (XD-RULE-0027)*](../explanation/rules/variants.html.md#XD-RULE-0027). All
  are errors.

#### NOTE
Iteration 1 checks [*A configuration respects it... (XD-RULE-0021)*](../explanation/rules/variants.html.md#XD-RULE-0021), [*Feature constraints hold (XD-RULE-0022)*](../explanation/rules/variants.html.md#XD-RULE-0022) and [*One product model per confi... (XD-RULE-0023)*](../explanation/rules/variants.html.md#XD-RULE-0023) to [*Exactly one variant per var... (XD-RULE-0027)*](../explanation/rules/variants.html.md#XD-RULE-0027) only
([*Scope cuts for iteration 1 (XD-ADR-0124)*](../explanation/decisions/scope.html.md#XD-ADR-0124)). [*Model constraints hold in e... (XD-RULE-0028)*](../explanation/rules/variants.html.md#XD-RULE-0028), the derivation of `configs` ([*configs matches the source (XD-RULE-0029)*](../explanation/rules/variants.html.md#XD-RULE-0029)), [*realizes respects configura... (XD-RULE-0030)*](../explanation/rules/variants.html.md#XD-RULE-0030),
[*Coverage counts per configu... (XD-RULE-0031)*](../explanation/rules/variants.html.md#XD-RULE-0031), the coverage per configuration and the per-configuration pages come later.

## Pitfalls

- The Pilot accepts models that break every variant rule. Only `curatrix variants` finds them.
- A `realizes` link from an element that exists in more configurations than its target breaks
  [*realizes respects configura... (XD-RULE-0030)*](../explanation/rules/variants.html.md#XD-RULE-0030) once that rule is checked.
