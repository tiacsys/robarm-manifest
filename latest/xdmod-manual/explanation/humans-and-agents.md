<a id="expl-humans-and-agents"></a>

# Humans and agents

In XDMOD, AI agents are first-class: they author and review design content the same way human
engineers do, with the same tools ([*Agents are first-class (XD-ADR-0003)*](decisions/workflow.md#XD-ADR-0003)). The difference is who may **decide**.

## Roles

| Role              | Who                                    | Does                                                                                                        |
|-------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Owner             | a person                               | sets goals, makes decisions, reviews and merges every PR, affirms evidence, makes baselines                 |
| Domain engineer   | a person (SE, EE, ME, SW, integration) | authors and reviews content in their domain; affirms suspect links in their domain                          |
| Agent author      | an AI agent                            | authors content on a branch (requirements, model, CAD through scripts, code, tests,<br/>docs) and opens PRs |
| Agent reviewer    | an AI agent, not the author            | first-pass review of a PR against checklists; posts findings as PR comments                                 |
| Coordinator agent | the agent the owner talks to           | plans, splits work, starts other agents, gathers results, keeps the plan and the<br/>decision log           |

## Propose versus affirm

Agents analyse suspect links and prepare affirmations and verdicts. But **only a person’s commit
counts** as an affirmation or a verdict ([*Only a human's commit affirms (XD-ADR-0051)*](decisions/workflow.md#XD-ADR-0051)). The same holds for merging: the owner’s
review and merge is the approval ([*Agents work under the user'... (XD-ADR-0044)*](decisions/workflow.md#XD-ADR-0044)).

## What agents may and may not do

| Agents may                                                                                                                                                                                 | Agents may not                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| create branches, commit, push to their own branches                                                                                                                                        | merge PRs, push to `main`, force-push to other people’s branches                                                                                                                                                                                      |
| open PRs and issues and comment on them, with the provenance trailer ([*Provenance trailer on GitHu... (XD-ADR-0065)*](decisions/workflow.md#XD-ADR-0065))           | change repo or org settings, rulesets or secrets, or create or delete repos, without the<br/>owner’s approval of the concrete action list ([*GitHub admin by agents only... (XD-ADR-0112)*](decisions/workflow.md#XD-ADR-0112)) |
| add `Co-Authored-By`, and `Signed-off-by` in the owner’s name where a repo requires<br/>it ([*Sign-off by agents (XD-ADR-0108)*](decisions/workflow.md#XD-ADR-0108)) | affirm suspect links or give manual verdicts; they only propose them ([*Only a human's commit affirms (XD-ADR-0051)*](decisions/workflow.md#XD-ADR-0051))                                                                       |
| run any tool through curatrix, under limits ([*A memory limit and a timeou... (XD-ADR-0064)*](decisions/checks.md#XD-ADR-0064))                                    | run tools without limits, install system packages, use sudo                                                                                                                                                                                           |
| record HIL evidence from `main` or baseline commits ([*Evidence only from main or ... (XD-ADR-0053)*](decisions/checks.md#XD-ADR-0053))                            | record evidence from PR branches as anything but previews                                                                                                                                                                                             |
| post freely in the project’s own repos and in xdmod                                                                                                                                        | post on other repos (doc engine, tools, upstream projects) before the owner approved the<br/>draft ([*Posting approval outside ou... (XD-ADR-0113)*](decisions/workflow.md#XD-ADR-0113))                                        |

These limits are policy in iteration 1: agents work under the owner’s GitHub account
([*Agent limits are policy onl... (XD-ADR-0123)*](decisions/workflow.md#XD-ADR-0123)).

## Provenance

Every agent commit carries a `Co-Authored-By` trailer ([*Agents work under the user'... (XD-ADR-0044)*](decisions/workflow.md#XD-ADR-0044), [*Agent commits carry a trailer (XD-RULE-0042)*](rules/checks.md#XD-RULE-0042)). Everything an
agent posts on GitHub (issues, comments, PR texts, reviews) ends with the line
`🤖 Generated with [Claude Code](https://claude.com/claude-code)` ([*Provenance trailer on GitHu... (XD-ADR-0065)*](decisions/workflow.md#XD-ADR-0065)). The check
[*commit trailers on agent co... (XD-CHECK-0028)*](../reference/checks.md#XD-CHECK-0028) warns about commits without the trailer.

## Review by another agent

Every pull request in the project repos and in xdmod gets a review by an agent other than the
author, before the owner’s review ([*Every PR gets an agent review (XD-ADR-0115)*](decisions/workflow.md#XD-ADR-0115)).

## Working in parallel

Several agents can work at the same time. Two agents never edit the same repo checkout at once.
An agent that changes repos works in its own **git worktrees** under
`<ws>/.worktrees/<branch>/<repo>`, made with `curatrix work start` ([*Parallel agents work in git... (XD-ADR-0114)*](decisions/workflow.md#XD-ADR-0114)). Shared,
read-only parts (Zephyr, libraries, `.venv`) are not duplicated.

Each agent gets a short brief: its goal, the decisions that bind it, the files to read, its
output paths, and what it must not do. It returns a short report; the coordinator checks the
claims that matter before passing them on.

## Agent material in the repos

Each repo has a `claude/` folder with its own rules, skills and pitfalls ([*Agent material in each repo... (XD-ADR-0062)*](decisions/repos.md#XD-ADR-0062)). xdmod
holds the launch `CLAUDE.md` for the workspace root, and shared skills, commands and checklists.
The bootstrap copies the launch file to the root and links all skills and commands into
`<workspace>/.claude/` ([*The bootstrap assembles .cl... (XD-ADR-0103)*](decisions/repos.md#XD-ADR-0103)). See [Repo layouts](../reference/repo-layouts.md).
