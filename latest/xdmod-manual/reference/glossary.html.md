<a id="ref-glossary"></a>

# Glossary

<a id="term-150-model"></a>

150 % model
: The product architecture with all variation points and all their variants. Each
  configuration picks one variant per variation point. See [Variants](../explanation/variants.html.md).

<a id="term-affirmation"></a>

affirmation
: A person’s confirmation that a suspect link is still correct. Agents may propose it; only a
  person’s commit counts.

<a id="term-affirmatrix"></a>

affirmatrix
: The suspect-link tool that XDMOD will use once it is adapted.

<a id="term-area"></a>

area
: The folder under `build/` that a build writes to: the repo name, `full` for the full
  set, the branch for worktree builds, or a named step.

<a id="term-backlink"></a>

backlink
: The reverse direction of a trace link, for example “verified by”. Backlinks are never
  written; the tools compute them.

<a id="term-baseline"></a>

baseline
: A tag `baseline/vX.Y.Z` of the manifest repo: a fixed set of repo versions. The baseline
  gates run before it is tagged.

<a id="term-bump-bot"></a>

bump bot
: A scheduled job in the manifest repo that moves the pins to the repos’ `main` and opens
  one bump PR.

<a id="term-bundle"></a>

bundle
: The package of outputs built from one baseline: documents, CAM data, firmware, HIL
  results. Iteration 2.

<a id="term-configuration"></a>

configuration
: One product of a product line: a choice of features with one product model. ID kind
  `SYS-CFG`.

<a id="term-curatrix"></a>

curatrix
: XDMOD’s command-line tool. It runs checks, generators, ID issuing, views, docs builds,
  bootstrap and launchers, every tool under limits.

<a id="term-EARS"></a>

EARS
: Easy Approach to Requirements Syntax: sentence patterns for requirements, such as “When
  <trigger>, the system shall <response>.”

<a id="term-evidence-branch"></a>

evidence branch
: An orphan branch in the integration repo that holds HIL run records. It is never merged.

<a id="term-feature"></a>

feature
: A property that distinguishes products of a product line, in the feature model. ID kind
  `SYS-FEAT`.

<a id="term-full-set"></a>

full set
: All documents of a project, built together from one workspace by the manifest repo.

<a id="term-generated-need"></a>

generated need
: A need extracted from a source (SysML, KiCad, FreeCAD, code, test results) instead of
  written in rst. It follows the same rules as authored needs.

<a id="term-HIL"></a>

HIL
: Hardware in the loop: tests that run firmware on real hardware.

<a id="term-ledger"></a>

ledger
: The file `ids.yaml` in each repo. It lists every ID number ever issued per kind.

<a id="term-manifest-repo"></a>

manifest repo
: The repo with the west manifest. It is the only place that pins revisions.

<a id="term-need"></a>

need
: An item managed by sphinx-needs, with an ID, a type, fields and links: a requirement, a
  design element, a test case, a decision, a rule.

<a id="term-placeholder"></a>

placeholder
: A temporary ID of the form `<KIND>-NEW-<tag>`. `curatrix ids fix` replaces it with a
  real ID.

<a id="term-PLEML"></a>

PLEML
: The SysML v2 library for product-line modelling from MBSE4U, the successor of VAMOS.

<a id="term-role"></a>

role
: A set of west groups that decides which repos a workspace checks out, for example `ee`
  or `integration`.

<a id="term-stub"></a>

stub
: A generated, read-only SysML element (`concern` or `requirement`) that stands for a
  need, so the model can refer to it.

<a id="term-suspect-link"></a>

suspect link
: A link whose target changed after the link was last confirmed.

<a id="term-SYSMOD"></a>

SYSMOD
: The systems engineering method by Tim Weilkiens that XDMOD follows.

<a id="term-tombstone"></a>

tombstone
: A record that curatrix keeps for a generated need whose source was deleted without
  retiring it first. It lasts until the next baseline.

<a id="term-trace-link"></a>

trace link
: A typed link from one need to another, written on the more concrete side.

<a id="term-VAMOS"></a>

VAMOS
: The variant method by Tim Weilkiens. XDMOD uses it through PLEML.

<a id="term-view"></a>

view
: A diagram of part of the SysML model, defined in the model and rendered by curatrix as an
  editable `.drawio.svg`.

<a id="term-west"></a>

west
: Zephyr’s tool for managing several git repos as one workspace.

<a id="term-worktree-set"></a>

worktree set
: A folder `.worktrees/<branch>/` with git worktrees of the repos, so an agent can work on
  a branch without touching the main checkouts.

<a id="term-zdocs"></a>

zdocs
: The documentation engine that builds and links the documents of all repos.
