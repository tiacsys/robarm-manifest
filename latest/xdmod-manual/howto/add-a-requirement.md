<a id="howto-add-a-requirement"></a>

# Add a requirement

Use this guide when you add a system requirement (`sys-req`) or a domain requirement
(`sw-req`, `ee-req`, `me-req`).

## Steps

1. Open the requirements document of the repo that owns the requirement. System requirements
   live in the syseng repo; domain requirements in their domain repo.
2. Write the need with a **placeholder ID** of the form `<KIND>-NEW-<tag>`. Never invent a
   number ([*No placeholders on main (XD-RULE-0017)*](../explanation/rules/ids.md#XD-RULE-0017)).
   ```rst
   .. sys-req:: Follow latency
      :id: SYS-REQ-NEW-latency
      :refines: SYS-NEED-0003
      :ears: ubiquitous
      :category: performance
      :quantity: latency
      :unit: ms
      :max: 50
      :verification_method: test
      :verification_scope: logical

      The system shall move each follower joint within 50 ms of the leader joint.
   ```
3. Write the sentence in an **EARS** pattern ([*Requirements use EARS (XD-ADR-0009)*](../explanation/decisions/method.md#XD-ADR-0009), [*EARS for system and domain ... (XD-ADR-0039)*](../explanation/decisions/method.md#XD-ADR-0039)) and set `:ears:` to
   that pattern ([*Requirements use EARS patterns (XD-RULE-0037)*](../explanation/rules/checks.md#XD-RULE-0037)). Stakeholder needs may be plain statements.
4. Put every number of the sentence into the value fields (`quantity`, `unit`, `min`,
   `max`, `nominal`, [*Requirement values are need... (XD-ADR-0076)*](../explanation/decisions/method.md#XD-ADR-0076)). The check compares them with the sentence ([*Requirement values agree wi... (XD-RULE-0036)*](../explanation/rules/checks.md#XD-RULE-0036)).
5. Add the upstream link. A system requirement `refines` a stakeholder need. A domain
   requirement `refines` a system requirement or an interface. A domain requirement with no
   upstream link needs `:derived: true` and a `:rationale:`.
6. If the requirement applies only to some configurations, add `:where:` with the feature
   condition ([*Variant fields configs, whe... (XD-ADR-0093)*](../explanation/decisions/method.md#XD-ADR-0093)).
7. Issue the ID:
   ```sh
   curatrix ids fix robarm-syseng
   ```
8. For system requirements, rebuild the docs and the SysML stubs, so the model can refer to the
   new requirement ([*Read-only requirement stubs... (XD-ADR-0036)*](../explanation/decisions/method.md#XD-ADR-0036)):
   ```sh
   curatrix docs robarm-syseng
   curatrix gen stubs robarm-syseng
   ```

## Checks

```sh
curatrix check robarm-syseng --stage local
```

- [*no placeholder IDs (XD-CHECK-0013)*](../reference/checks.md#XD-CHECK-0013) and [*IDs in the sources are in t... (XD-CHECK-0014)*](../reference/checks.md#XD-CHECK-0014): no placeholders left, every ID is in the ledger.
- [*requirement values agree wi... (XD-CHECK-0021)*](../reference/checks.md#XD-CHECK-0021) and [*EARS pattern matches the se... (XD-CHECK-0022)*](../reference/checks.md#XD-CHECK-0022): value fields and EARS pattern agree with the sentence.
- [*SysML stubs match the needs (XD-CHECK-0015)*](../reference/checks.md#XD-CHECK-0015): the stubs match the needs.
- [*docs build strict (zdocs, s... (XD-CHECK-0001)*](../reference/checks.md#XD-CHECK-0001): the strict docs build; a missing `refines` fails it.

## Pitfalls

- Two PRs may issue the same number. The second one to rebase gets a ledger conflict. Take
  `main`’s ledger and run `curatrix ids fix` again ([*ID collisions show up as gi... (XD-ADR-0122)*](../explanation/decisions/traces.md#XD-ADR-0122)).
- Don’t delete a requirement. Set `:status: retired` first ([*IDs are never reused; retir... (XD-RULE-0020)*](../explanation/rules/ids.md#XD-RULE-0020)).
