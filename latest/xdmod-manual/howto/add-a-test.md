<a id="howto-add-a-test"></a>

# Add a test

Use this guide when you add a test case and want its results to count as evidence.

## Where the test lives

Tests live by what they verify ([*Tests live by what they verify (XD-ADR-0104)*](../explanation/decisions/traces.md#XD-ADR-0104)):

- A test that verifies a system requirement or an interface is a system test case (`INT-STC`)
  or an integration test case (`INT-ITC`) in the integration repo, even if it touches one
  domain only.
- A test of a domain requirement stays in its domain repo: `SW-TC`, `EE-TC` or `ME-TC`.

## Steps

1. Write the test case with a `verifies` link to the requirement. For authored test cases
   (rst):
   ```rst
   .. int-itc:: Servo PWM on the joint connector
      :id: INT-ITC-NEW-pwm
      :verifies: SYS-IF-0002
   ```

   For Zephyr tests, the ID goes into the ZTEST comment and is written there by a tool
   ([*SW test case IDs come from ... (XD-ADR-0073)*](../explanation/decisions/traces.md#XD-ADR-0073)); the `\verifies` tag makes the link.
2. If the test runs only on some configurations, set `configs`.
3. Issue the ID:
   ```sh
   curatrix ids fix robarm-integration
   ```
4. Run the test. Results become test result needs (`TR-<test case ID>-<run hash>`) with a
   `result_of` link to the test case and the `config` they ran on.

## Evidence rules

- HIL results carry the firmware hash and the SHAs of all pinned repos ([*HIL results carry the firmw... (XD-RULE-0012)*](../explanation/rules/trace.md#XD-RULE-0012),
  [*HIL results carry firmware ... (XD-CHECK-0005)*](../reference/checks.md#XD-CHECK-0005)).
- Evidence counts only from commits on `main` or baseline tags ([*Evidence only from main or ... (XD-ADR-0053)*](../explanation/decisions/checks.md#XD-ADR-0053)). Runs on PR
  branches are previews.
- A result whose SHAs no longer match the pins is stale and doesn’t count ([*Only valid evidence counts (XD-RULE-0013)*](../explanation/rules/trace.md#XD-RULE-0013),
  [*stale evidence (R5a) (XD-CHECK-0011)*](../reference/checks.md#XD-CHECK-0011)).
- Every requirement needs a `verifies` link ([*Every requirement is verified (XD-RULE-0009)*](../explanation/rules/trace.md#XD-RULE-0009), [*every requirement verified ... (XD-CHECK-0007)*](../reference/checks.md#XD-CHECK-0007)).

#### NOTE
The run-record schema and the extraction of `TR` needs from test reports are being
built (task 4.5a). Until then, test reports show the sphinx-test-reports needs.

## Checks

```sh
curatrix check robarm-integration --stage local
```
