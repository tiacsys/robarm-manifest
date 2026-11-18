<a id="expl-multi-repo"></a>

# Many repos, one workspace

An XDMOD project lives in several git repos: one per engineering domain, one for integration,
one manifest, and the framework itself. They are managed together as one **west workspace**
([*A multi-repo workspace with... (XD-ADR-0006)*](decisions/repos.md#XD-ADR-0006)). The diagrams in
[XDMOD as a SysML model](framework-model.md#expl-framework-model) show each repo with its files, and what flows between them.

## Why several repos

Each domain has its own tools, reviewers and pace. Separate repos keep their histories, checks
and permissions apart, while the trace links still connect them. Example (robot arm): the repos
`robarm-syseng`, `robarm-ee`, `robarm-me`, `robarm-sw` and `robarm-integration`, with
`robarm-manifest` as the manifest and `xdmod` as the framework ([*Names: XDMOD, -trix tools, ... (XD-ADR-0042)*](decisions/repos.md#XD-ADR-0042)).

- The **systems engineering** repo holds needs, requirements, the SysML model and views. It is
  upstream of every domain.
- Each **domain** repo (EE, ME, SW) holds its requirements, design and domain tests.
- The **integration** repo holds the system and integration tests, the HIL setups and the
  orphan evidence branch ([*An integration repo for sys... (XD-ADR-0066)*](decisions/repos.md#XD-ADR-0066)). A test that verifies a system requirement or an interface
  lives there, even if it touches one domain only ([*Tests live by what they verify (XD-ADR-0104)*](decisions/traces.md#XD-ADR-0104)).
- The **manifest** repo pins every other repo ([*A dedicated manifest repo (XD-ADR-0011)*](decisions/repos.md#XD-ADR-0011)), builds the full document set, and
  holds the baselines.
- **xdmod** is in every workspace that uses the framework ([*xdmod is in every workspace (XD-ADR-0059)*](decisions/repos.md#XD-ADR-0059)).

## The manifest pins everything

The manifest repo is the **only** place that pins revisions ([*The manifest is the only pl... (XD-ADR-0033)*](decisions/repos.md#XD-ADR-0033)). Framework and design
repos and libraries are pinned by commit SHA; third-party trees such as Zephyr may be pinned by
tag. No other repo has its own `west.yml`.

The manifest is split into **submanifests**, one per area, and its projects carry **groups**
([*West submanifests and proje... (XD-ADR-0079)*](decisions/repos.md#XD-ADR-0079)). Each role checks out only what it needs, through west’s group filter. The default
filter is minimal: framework, systems engineering and Zephyr ([*A minimal default group filter (XD-ADR-0084)*](decisions/repos.md#XD-ADR-0084)). A role always gets its
upstream repos and the framework. The integration role gets everything except the big CAD
libraries ([*The integration role (XD-ADR-0082)*](decisions/repos.md#XD-ADR-0082)). Component libraries are pinned west projects too, isolated from any
user-global setup ([*Pinned, isolated component ... (XD-ADR-0080)*](decisions/repos.md#XD-ADR-0080)).

West rule to remember: a project is active as soon as **one** of its groups is enabled. So a big
library carries only its own group, never also the domain group.

## One workspace root

The workspace root is the west topdir ([*One west topdir at the work... (XD-ADR-0061)*](decisions/repos.md#XD-ADR-0061)). It holds `.west/`, `.venv/`, `build/`
and all repos. Design repos sit at the top level; dependencies go under `tools/` and `libs/`
([*Workspace paths (XD-ADR-0083)*](decisions/repos.md#XD-ADR-0083)). Every command runs from the root ([*All commands run from the w... (XD-ADR-0060)*](decisions/repos.md#XD-ADR-0060)). See [Workspace](../reference/workspace.md).

## A change across repos

1. **One branch name** in every repo the change touches ([*One branch name across repos (XD-ADR-0045)*](decisions/workflow.md#XD-ADR-0045)).
2. **One pull request per repo.** Each lists its sibling PRs.
3. **PR CI** checks each repo against its siblings. For each sibling it takes, in this order: a
   branch with the same name; the repo’s `main` if the manifest pin is an ancestor of it; the
   manifest pin ([*PR CI sibling resolution (XD-ADR-0116)*](decisions/checks.md#XD-ADR-0116)). So downstream PRs see upstream changes that are merged but not yet
   bumped.
4. **Merge upstream first**: systems engineering, then the domains, then integration. Framework
   changes merge before the repos that use them. Every PR is rebase-merged ([*Trunk-based merging with re... (XD-ADR-0043)*](decisions/workflow.md#XD-ADR-0043)).
5. **Bump bot.** A scheduled job in the manifest repo compares each repo’s `main` with its pin
   and opens or updates one bump PR ([*A bump bot for manifest pins (XD-ADR-0054)*](decisions/checks.md#XD-ADR-0054), [*The bump bot is a scheduled... (XD-ADR-0081)*](decisions/checks.md#XD-ADR-0081)). Because a PR opened with the job’s
   own token does not trigger CI, the job builds the full set itself and reports on the PR.

## Baselines and bundles

A **baseline** is a tag `baseline/vX.Y.Z` of the manifest repo: a fixed set of repo versions
([*Terms: baseline and bundle (XD-ADR-0034)*](decisions/repos.md#XD-ADR-0034), [*SemVer tags and baseline tags (XD-ADR-0047)*](decisions/repos.md#XD-ADR-0047)). A **bundle** is the package of outputs built from one baseline: docs,
CAM data, firmware, HIL results. Bundles come in iteration 2 ([*Scope moved to iteration 2 (XD-ADR-0037)*](decisions/scope.md#XD-ADR-0037)).

Before a baseline is tagged, the gates run: no links to retired needs ([*Links to retired needs are ... (XD-RULE-0011)*](rules/trace.md#XD-RULE-0011)), no open suspect
links ([*Suspect links are reviewed ... (XD-RULE-0014)*](rules/trace.md#XD-RULE-0014)), and a full local build with CAD content. The documentation is published on
GitHub Pages of the manifest repo, with `main` as “latest” and one folder per baseline
([*Docs hosting on GitHub Page... (XD-ADR-0048)*](decisions/documents.md#XD-ADR-0048)).

## Documents across repos

Each repo has its own zdocs registry ([*One zdocs registry per repo... (XD-ADR-0021)*](decisions/documents.md#XD-ADR-0021)), which also builds its upstream documents
locally from the west checkout, so links into upstream needs resolve ([*Upstream documents are buil... (XD-ADR-0029)*](decisions/documents.md#XD-ADR-0029)). The manifest
repo’s registry builds the full linked set. The XDMOD manual is part of that set; project
documents link to the manual, but the manual never links to a project ([*The XDMOD manual is part of... (XD-ADR-0101)*](decisions/documents.md#XD-ADR-0101)).
