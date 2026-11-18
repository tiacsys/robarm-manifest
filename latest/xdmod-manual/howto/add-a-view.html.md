<a id="howto-add-a-view"></a>

# Add a view

Use this guide when you want a diagram of the model in the docs. Views come from the model:
nobody draws model content by hand ([*Views as drawio files rende... (XD-ADR-0002)*](../explanation/decisions/method.html.md#XD-ADR-0002), [*View definitions live in th... (XD-ADR-0085)*](../explanation/decisions/method.html.md#XD-ADR-0085)).

## Steps

1. Define the view in `model/views.sysml` as a SysML `view` with `@XdView` metadata. Its
   short name is a `SYS-VIEW` ID, a reserved kind that is not a need:
   ```text
   view <'SYS-VIEW-NEW-joint'> jointView {
       @XdView { kind = "interconnection"; root = "RobArm::JointModule"; }
       expose RobArm::JointModule::**;
   }
   ```
2. Issue the ID and build the view:
   ```sh
   curatrix ids fix robarm-syseng
   curatrix gen model robarm-syseng
   curatrix views build robarm-syseng --view jointView
   ```

   This writes `views/jointView.drawio.svg`: the picture with the drawio diagram embedded
   ([*Views are committed as edit... (XD-ADR-0087)*](../explanation/decisions/method.html.md#XD-ADR-0087)). Commit it.
3. Show it in a document:
   ```rst
   .. sysml-view:: /views/jointView.drawio.svg
      :caption: Joint module
   ```

   The document’s `conf.py` must list `(REPO, "views/*.drawio.svg")` in `generated`.
4. Optional: arrange the boxes by hand.
   ```sh
   curatrix launch drawio robarm-syseng/views/jointView.drawio.svg
   curatrix views normalize robarm-syseng/views/jointView.drawio.svg
   ```

   Layout is not model content. The check compares content, not geometry ([*Small corrections from rese... (XD-ADR-0057)*](../explanation/decisions/traces.html.md#XD-ADR-0057) (a)).

## Checks

- [*views match the model (cont... (XD-CHECK-0018)*](../reference/checks.html.md#XD-CHECK-0018): content matches the model, the diagram is uncompressed, geometry is sane and
  the picture is fresh. It needs no browser.
-  [*.FCStd uncompressed; drawio... (XD-CHECK-0025)*](../reference/checks.html.md#XD-CHECK-0025): no compressed diagrams ([*Design files are stored unc... (XD-RULE-0039)*](../explanation/rules/checks.html.md#XD-RULE-0039)).

#### NOTE
curatrix builds the view kinds `interconnection` and `decomposition`, and the
SysML v2 standard views `general`, `actionflow`, `statetransition` and `usecases`.
A `general` view shows what its `expose` and `filter` select; `show` limits the
relationships it draws and `compartments` (`all`, `none`, `root`, `doc`, or a list
such as `all,doc`) the lists inside the boxes. `between` names two or more packages: the
view then shows only the relations between them (a view across two domains). In an
`interconnection` view, `show` names the ports to draw. `direction` (`DOWN`,
`RIGHT`, `LEFT`, `UP`) sets the layout direction; the default depends on the kind
(`RIGHT` for `interconnection` and `context`, `UP` for `allocation` and
`variants`, `DOWN` for the others). Every drawing must fit a 4:3 or 16:9
page, upright or across (a width to height ratio from 9:16 to 16:9). When it does not,
`views build` turns the layout by 90 degrees, wraps long chains and moves the legend, and
reports the ratio; `RIGHT!` forbids turning. If no layout fits, split the view.
Between a domain model and the system model: `allocation` (`root` = a package or a
def) draws the domain’s boards, harnesses, assemblies and ports with the system elements and
interfaces they realize or conform to, exactly the trace links of the generated needs;
`variants` (`root` = a board or assembly def) its variants, their `variantName` and the
configurations and usages each serves. `context` is the `interconnection` view of the
system context part. Keeping manual layout
across rebuilds is iteration 2 ([*Scope moved to iteration 2 (XD-ADR-0037)*](../explanation/decisions/scope.html.md#XD-ADR-0037)). Trace graphs use `needflow`, not drawio
([*Trace graphs with needflow (XD-ADR-0086)*](../explanation/decisions/method.html.md#XD-ADR-0086)).

## Pitfalls

- `views build` needs node, elkjs and Firefox. They are installed by the bootstrap; it runs
  locally only.
- After saving in drawio, always run `views normalize`. The pre-commit hook insists.
