<a id="expl-sysmod-and-sysml"></a>

# SYSMOD and SysML v2

XDMOD uses the SYSMOD method by Tim Weilkiens for systems engineering ([*SYSMOD is the main method r... (XD-ADR-0007)*](decisions/method.html.md#XD-ADR-0007)), and writes the
system model in SysML v2 textual notation ([*SysML v2 textual notation f... (XD-ADR-0001)*](decisions/method.html.md#XD-ADR-0001)).

## Why SYSMOD

SYSMOD gives a fixed order of steps and names for their work products: problem statement,
stakeholders, needs, system context, use cases, requirements, and the functional, logical and
product architecture. XDMOD keeps SYSMOD’s order and names, so the SYSMOD website
([https://mbse4u.com/sysmod/](https://mbse4u.com/sysmod/)) and its examples apply directly. The SYSMOD v5 library
(`mbse4u/sysmod-sysmlv2`) is a west project pinned at a commit, not a copy ([*The SYSMOD library is a pin... (XD-ADR-0077)*](decisions/method.html.md#XD-ADR-0077)).

## Two worlds: text and model

- **Text that people review lives in sphinx-needs**: stakeholder needs, requirements, test
  specifications ([*Requirements in sphinx-needs (XD-ADR-0005)*](decisions/method.html.md#XD-ADR-0005)).
- **Structure and behaviour live in SysML**: context, use cases, architecture, allocations,
  variants.

The two worlds meet through **generated stubs** ([*Read-only requirement stubs... (XD-ADR-0036)*](decisions/method.html.md#XD-ADR-0036)). A tool reads the needs and writes a
package of read-only stubs: a `concern` for each stakeholder need and a `requirement` for each
system requirement ([*Small corrections from rese... (XD-ADR-0057)*](decisions/traces.html.md#XD-ADR-0057) (b)). Model elements refer to requirements through these stubs,
for example with `satisfy`. Nobody edits the stubs by hand; a check compares them with the
needs ([*SysML stubs match the needs (XD-CHECK-0015)*](../reference/checks.html.md#XD-CHECK-0015)).

The other way, model elements come back into the documents as generated needs. A model element
becomes a need only when it takes part in a trace link ([*Only linked model elements ... (XD-ADR-0118)*](decisions/method.html.md#XD-ADR-0118)). The definition holds the
ID; its usages are listed in an `instances` field ([*The definition holds the tr... (XD-ADR-0117)*](decisions/method.html.md#XD-ADR-0117)). The model extractor writes
`generated/model-needs.json`, which is committed and checked ([*model.json and model-needs.... (XD-CHECK-0017)*](../reference/checks.html.md#XD-CHECK-0017)).

## Requirement values

SYSMOD’s requirement boilerplates give requirements machine-readable values. XDMOD keeps the EARS
sentence for people ([*Requirements use EARS (XD-ADR-0009)*](decisions/method.html.md#XD-ADR-0009), [*EARS for system and domain ... (XD-ADR-0039)*](decisions/method.html.md#XD-ADR-0039)) and adds value fields next to it: `quantity`,
`unit`, `min`, `max`, `nominal` ([*Requirement values are need... (XD-ADR-0076)*](decisions/method.html.md#XD-ADR-0076)). The stub carries them as attributes, so a
model constraint or a test can read them. Checks compare the fields with the sentence
([*Requirement values agree wi... (XD-RULE-0036)*](rules/checks.html.md#XD-RULE-0036), [*Requirements use EARS patterns (XD-RULE-0037)*](rules/checks.html.md#XD-RULE-0037)).

## Problem statement and objectives

The problem statement is a stakeholder need with `category: problem` ([*The problem statement is a ... (XD-ADR-0074)*](decisions/method.html.md#XD-ADR-0074)). System
objectives are stakeholder needs with `category: objective` ([*System objectives are stake... (XD-ADR-0075)*](decisions/method.html.md#XD-ADR-0075)). Other needs and
objectives link to the problem statement with `addresses`.

## The chain of contexts

SYSMOD builds a chain of contexts, each one specialising the one before: idea, specification,
functional, logical and product context. Later contexts inherit actors and ports. XDMOD includes
a short functional architecture: functions realize use cases, and logical elements realize
functions ([*A short functional architec... (XD-ADR-0078)*](decisions/method.html.md#XD-ADR-0078)). Each system element (`SYS-EL`) carries a `layer`: `context`,
`functional`, `logical` or `product`.

## Toolchain

The model is checked with the OMG SysML v2 Pilot Implementation, run through `jshell`, which
also exports the model as JSON ([*SysML toolchain: the OMG Pi... (XD-ADR-0058)*](decisions/method.html.md#XD-ADR-0058)). XDMOD’s own Python tools read that JSON. curatrix
stores a compact form of it in `generated/model.json`, so later steps (views, variants, needs)
need no Java. The model must parse with 0 errors ([*The SysML model parses with... (XD-RULE-0035)*](rules/checks.html.md#XD-RULE-0035), [*the Pilot parses the model ... (XD-CHECK-0016)*](../reference/checks.html.md#XD-CHECK-0016)).

Views of the model are SysML `view` definitions with an `@XdView` annotation ([*View definitions live in th... (XD-ADR-0085)*](decisions/method.html.md#XD-ADR-0085)).
curatrix renders them as editable `.drawio.svg` files ([*Views are committed as edit... (XD-ADR-0087)*](decisions/method.html.md#XD-ADR-0087)).

The step-by-step mapping from SYSMOD steps to files and documents is in
[SYSMOD mapping](../reference/sysmod-mapping.html.md).
