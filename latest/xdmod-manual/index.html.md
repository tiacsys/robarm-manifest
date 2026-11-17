<a id="manual-index"></a>

# XDMOD Manual

**XDMOD** (Cross-Domain MODeling) is a method plus tools for developing a product across systems
engineering, software, electronics and mechanics, in many git repos, with people and AI agents
working side by side. It is built on SYSMOD and SysML v2 for the system model, sphinx-needs for
requirements and traces, zdocs for a linked document set, and west for the workspace. Its one
tool is `curatrix`.

XDMOD gives you three things:

1. **One trace graph across all domains.** Every need, model element, CAD part, code unit and
   test result has an ID, and the more concrete side holds each link. Checks find broken, missing
   and suspect links, in every repo and across the full set.
2. **Documents that come from the design.** Requirements, architecture, CAD and code produce one
   linked, versioned document set. Generated content is committed and checked, so it can’t drift.
3. **One workflow for humans and agents.** The same commands, checks and reviews apply to
   everyone. Agents propose; only a human’s commit affirms.

Examples in this manual come from the robot arm, the worked example of XDMOD. Every page reads
on its own without it.

## How to read this manual

The manual follows Diátaxis:

- [Tutorials](tutorials/index.html.md) walk you through your first workspace, requirement and change.
- [How-to guides](howto/index.html.md) are short recipes for one task each.
- [Reference](reference/index.html.md) lists the facts: trace model, ID scheme, checks, layouts.
- [Explanation](explanation/index.html.md) says why things are the way they are, and holds every framework
  decision and method rule as a need.

The command line and the Sphinx extensions are documented in the curatrix reference
(`xdmod-ref`).

For agents and other tools, the build also writes `llms.txt` (a list of all pages),
`llms-full.txt` (all pages in one file) and a Markdown copy of every page (`<page>.md`) next
to the HTML ([*Agent-readable docs with sp... (XD-ADR-0111)*](explanation/decisions/documents.html.md#XD-ADR-0111)). The needs themselves are best read from `needs.json`.

* [Tutorials](tutorials/index.html.md)
  * [Your first workspace](tutorials/first-workspace.html.md)
  * [Your first requirement, end to end](tutorials/first-requirement.html.md)
  * [Your first change](tutorials/first-change.html.md)
* [How-to guides](howto/index.html.md)
  * [Add a requirement](howto/add-a-requirement.html.md)
  * [Add a model element](howto/add-a-model-element.html.md)
  * [Add a view](howto/add-a-view.html.md)
  * [Add a PCBA or circuit block](howto/add-a-pcba.html.md)
  * [Add a FreeCAD part or assembly](howto/add-a-part.html.md)
  * [Add a feature or configuration](howto/add-a-configuration.html.md)
  * [Add a test](howto/add-a-test.html.md)
  * [Make a change across repos](howto/cross-repo-change.html.md)
  * [Make a co-design change (ME and EE)](howto/co-design-change.html.md)
  * [Work as an agent](howto/work-as-an-agent.html.md)
  * [Make a baseline](howto/make-a-baseline.html.md)
* [Reference](reference/index.html.md)
  * [Trace model](reference/trace-model.html.md)
  * [ID scheme](reference/id-scheme.html.md)
  * [Variant rules](reference/variant-rules.html.md)
  * [Checks](reference/checks.html.md)
  * [SYSMOD mapping](reference/sysmod-mapping.html.md)
  * [Repo layouts](reference/repo-layouts.html.md)
  * [Workspace](reference/workspace.html.md)
  * [Glossary](reference/glossary.html.md)
* [Explanation](explanation/index.html.md)
  * [Principles](explanation/principles.html.md)
  * [The V-model and trace links](explanation/v-model-and-traces.html.md)
  * [SYSMOD and SysML v2](explanation/sysmod-and-sysml.html.md)
  * [Variants](explanation/variants.html.md)
  * [Many repos, one workspace](explanation/multi-repo.html.md)
  * [Humans and agents](explanation/humans-and-agents.html.md)
  * [Decisions](explanation/decisions/index.html.md)
  * [Rules](explanation/rules/index.html.md)
