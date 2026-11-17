<a id="tut-first-change"></a>

# Your first change

#### NOTE
This tutorial is a skeleton. It is completed in Phase 6 on the real robot-arm repos.

## Goal

You change one requirement and retire another. You see what each check reports, read the change
impact, fix the downstream links, and prepare the affirmation of the suspect links.

## Steps

1. **Start a branch.** Use one branch name in every repo you touch ([*One branch name across repos (XD-ADR-0045)*](../explanation/decisions/workflow.html.md#XD-ADR-0045)):
   ```sh
   curatrix work start feat/latency robarm-syseng robarm-ee
   ```

   `curatrix work` is being added (task 4.4c); see [Make a change across repos](../howto/cross-repo-change.html.md).
2. **Change a requirement.** Edit the sentence and its value fields together ([*Requirement values agree wi... (XD-RULE-0036)*](../explanation/rules/checks.html.md#XD-RULE-0036)), e.g.
   `100 ms` becomes `50 ms` and `:max:` becomes `50`. A text change fails no build. Only
   the change impact shows it.
3. **Retire a requirement.** Set `:status: retired`. Never delete a need that others link to
   before it is retired ([*IDs are never reused; retir... (XD-RULE-0020)*](../explanation/rules/ids.html.md#XD-RULE-0020)). Links to it are reported as warnings until the next
   baseline ([*Links to retired needs are ... (XD-RULE-0011)*](../explanation/rules/trace.html.md#XD-RULE-0011), [*no links to retired needs (... (XD-CHECK-0008)*](../reference/checks.html.md#XD-CHECK-0008)).
4. **Regenerate** what depends on the needs:
   ```sh
   curatrix docs robarm-syseng
   curatrix gen all robarm-syseng
   ```
5. **Read the change impact.** Compare the needs before and after the change:
   ```sh
   curatrix needs-diff build/main-needs/ build/robarm-syseng/docs/deploy/html/ -o build/robarm-syseng/needs-diff.md
   ```

   It lists changed needs, direct and transitive **suspect** links, and dangling links
   ([*Suspect links are reviewed ... (XD-RULE-0014)*](../explanation/rules/trace.html.md#XD-RULE-0014)). In a PR, [*needs-diff against the base... (XD-CHECK-0023)*](../reference/checks.html.md#XD-CHECK-0023) writes the same report.
6. **Fix downstream.** Each downstream owner updates the links that pointed at the retired need,
   on the same branch name, and runs the checks of their repo.
7. **Affirm.** For each suspect link, an agent may prepare a proposal (reason and diff). Only a
   person’s commit affirms it ([*Only a human's commit affirms (XD-ADR-0051)*](../explanation/decisions/workflow.html.md#XD-ADR-0051)).
8. **Open the PRs**, one per repo, and list the sibling PRs in each; see
   [Make a change across repos](../howto/cross-repo-change.html.md).

## What you learned

- Structure errors fail the build at once. Content changes need the change-impact report.
- Retired needs keep their ID forever, and IDs are never reused.
