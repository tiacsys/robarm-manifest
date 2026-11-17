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

The repo’s model files are read as one set, after the libraries, so their order does not matter
([*Domain repos refine the sys... (XD-ADR-0130)*](decisions/domains.html.md#XD-ADR-0130)).

## Domain models

The EE and ME repos have their own model in `model/` ([*Domain repos refine the sys... (XD-ADR-0130)*](decisions/domains.html.md#XD-ADR-0130)). A domain def
specializes the system def it realizes and one base def of the xdmod library `XdDomain`
(`Pcba`, `ExternalPart`, `Cable`, `Assembly`; `ConnectorPort`, `PinSignal`,
`MechanicalPort` for ports):

```text
part def <'EE-PCBA-0012'> JointControllerBoard :> RobArmProduct::JointController, XdDomain::Pcba {
    port :>> servoOut : ServoHeader;
}
port def <'EE-PORT-0003'> ServoHeader :> RobArmInterfaces::ServoIf, XdDomain::ConnectorPort {
    :>> connector = "JST-XH-3";
    out port :>> pwm : Pin { :>> pin = "1"; :>> net = "SERVO_PWM"; }
}
```

The domain repo’s `checks.yaml` lists the system model files as `model.libraries` and the
system repo’s committed `generated/model.json` as `model.upstream`. `curatrix gen model`
emits the `EE-PCBA`, `EE-PORT`, `EE-HAR`, `ME-ASM` and `ME-PORT` needs and derives their
links from `:>`: `realizes` to a `SYS-EL`, `conforms` to a `SYS-IF`, and `part_of` from a
port def to the board or assembly that has a port of it ([*curatrix checks conformance... (XD-ADR-0132)*](decisions/domains.html.md#XD-ADR-0132), [*Need kinds EE-PORT, ME-PORT... (XD-ADR-0133)*](decisions/domains.html.md#XD-ADR-0133)).
[*domain model conforms to it... (XD-CHECK-0033)*](../reference/checks.html.md#XD-CHECK-0033) checks conformance ([*Domain models conform to th... (XD-RULE-0047)*](rules/trace.html.md#XD-RULE-0047)). A conjugated port `~X` is
redefined by a conjugated `~Y` with `Y :> X`. A domain need gets the `configs` of the
`SYS-CFG` s that configure the system elements it realizes.

A variant of a board or assembly specializes the board or assembly def and
`XdDomain::DomainVariant`; `variantName` is its name in KiCad (an assembly variant in the
`.kicad_pro`) or FreeCAD (a row of the configuration table). It has no ID of its own: a
specialization between two domain defs makes no trace link. A dependency from the variant names the
configurations and the system usages it serves ([*Variants: the domain varian... (XD-ADR-0136)*](decisions/domains.html.md#XD-ADR-0136)):

```text
part def JointBoardAlt :> JointBoard, XdDomain::DomainVariant { :>> variantName = "alt"; }
dependency from JointBoardAlt to MyConfigs::proto, MyProduct::Arm::joint1, MyProduct::Arm::joint2;
```

Each dependency serves every pair of its configurations and usages; write one dependency per
group, and name at least one of each in every dependency. The pairs a board must serve are built
per system def it realizes: the usages of that def times the configurations that configure it (all
configurations if none does). Nobody writes the table “configuration → variant per usage”: [*variants across levels: one... (XD-CHECK-0034)*](../reference/checks.html.md#XD-CHECK-0034) computes it
against the system repo’s committed model (`model.upstream`), writes it into its log
(`build/<area>/checks/variants-across-levels.md`) and checks [*One domain variant per conf... (XD-RULE-0048)*](rules/variants.html.md#XD-RULE-0048): exactly one
variant per configuration and usage, every named variant in the KiCad project or FreeCAD
configuration table, and Zephyr board variants by name (the Zephyr board name is the KiCad project
name in lower case with `-` as `_`; `outer/inner` counts as `inner`; a Zephyr board without
such a project is ignored). The domain repo switches it on with a `variants:`
section in `checks.yaml`. At most two variants per board or assembly; a variant that names no
configuration is not checked in iteration 1.

Views of the model are SysML `view` definitions with an `@XdView` annotation ([*View definitions live in th... (XD-ADR-0085)*](decisions/method.html.md#XD-ADR-0085)).
curatrix renders them as editable `.drawio.svg` files ([*Views are committed as edit... (XD-ADR-0087)*](decisions/method.html.md#XD-ADR-0087)).

The step-by-step mapping from SYSMOD steps to files and documents is in
[SYSMOD mapping](../reference/sysmod-mapping.html.md).
