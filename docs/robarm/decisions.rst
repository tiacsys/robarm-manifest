Project Decisions
=================

Decisions about the robot arm project are recorded on this page as ``prj-dec`` needs, with IDs
``PRJ-DEC-nnnn`` from the ledger ``robarm-manifest/ids.yaml``. Decisions about the XDMOD method
itself are framework decisions (``xd-adr``) in the :external+xdmod-manual:doc:`XDMOD manual
<explanation/decisions/index>`. A project decision that applies or tailors a framework decision
``follows`` it.

The split: a decision is a **project decision** when it is only true for the robot arm: its
targets and scope, its hardware, its GitHub org, repos and settings, its licence, and its pinned
SDK. Everything that would hold for any other project that uses XDMOD (method, trace model, IDs,
checks, tools, repo pattern, workflow, agent rules) is a framework decision. ``legacy_id`` is the
decision's number in the planning log.

.. needtable::
   :types: prj-dec
   :columns: id;legacy_id as "Old ID";title;follows;decision_status as "Status";date
   :sort: id
   :style: table

.. prj-dec:: Iteration 1 is T-shaped
   :id: PRJ-DEC-0001
   :legacy_id: D4
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid

   Iteration 1 is **T-shaped**: broad at the requirements/system level, then end-to-end for **one joint**.

.. prj-dec:: One-joint end-to-end target on a real STM32G4 board
   :id: PRJ-DEC-0002
   :legacy_id: D8
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid

   One-joint E2E target: design artifacts plus **Zephyr firmware that builds and runs on a real STM32G4 board**, with the verification evidence traced back to requirements.

.. prj-dec:: Available hardware
   :id: PRJ-DEC-0003
   :legacy_id: D10
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid

   Available hardware: NUCLEO-G4 board, PCA9685 breakout, MCP3208 breakout, SG90 servos, potentiometers.

.. prj-dec:: The board is a NUCLEO-G474RE
   :id: PRJ-DEC-0004
   :legacy_id: D16
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :refines: PRJ-DEC-0002

   The board is a **NUCLEO-G474RE**.

.. prj-dec:: Leader and follower can be the same size
   :id: PRJ-DEC-0005
   :legacy_id: D18
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid

   The leader and follower **can be the same size**.

.. prj-dec:: The number of PCBAs is left to the SE work
   :id: PRJ-DEC-0006
   :legacy_id: D28
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0016

   The number of PCBAs is **left to the SE work** (trade study in Phase 6).

.. prj-dec:: Public repos in the tiacsys GitHub org
   :id: PRJ-DEC-0007
   :legacy_id: D48
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0012

   Repos live in the existing **tiacsys** GitHub org and are **public from day one**. CI can check out other repos without extra tokens.

.. prj-dec:: Every role checks out the full Zephyr tree
   :id: PRJ-DEC-0008
   :legacy_id: D87
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0079

   **Zephyr:** for now, every role checks out the full Zephyr tree, including roles that only build docs. A smaller doc-only subset may come later.

.. prj-dec:: robarm-manifest pins xdmod by SHA
   :id: PRJ-DEC-0009
   :legacy_id: D92
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0033, XD-ADR-0047

   robarm-manifest pins **xdmod by SHA** for now. Once xdmod has a stable release for other workspaces, it gets SemVer tags.

.. prj-dec:: robarm-sw CI builds the firmware
   :id: PRJ-DEC-0010
   :legacy_id: D101
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0041, XD-ADR-0049

   **robarm-sw CI builds the firmware** with the Zephyr SDK, runs the devicetree-vs-model check (``CK-F2``, a command in robarm-sw's ``checks.yaml``), and runs unit tests on ``native_sim``. This is not CAD, so :need:`XD-ADR-0049` doesn't exclude it.

.. prj-dec:: robarm-sw is a Zephyr module
   :id: PRJ-DEC-0011
   :legacy_id: D114
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0006

   **robarm-sw is a Zephyr module** (``zephyr/module.yml`` with ``dts_root``/``board_root``).

.. prj-dec:: Phase 4 GitHub action list
   :id: PRJ-DEC-0012
   :legacy_id: D136
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0112, XD-ADR-0042

   **Phase 4 GitHub action list approved** (:need:`XD-ADR-0112`): create the 7 public repos (``xdmod``, ``robarm-manifest``, ``robarm-syseng``, ``robarm-ee``, ``robarm-me``, ``robarm-sw``, ``robarm-integration``); settings (rebase merge only, delete branch on merge, Issues and Projects on, Wiki off); org ruleset ``xdmod-main`` (PR required with no approval count, up-to-date branches, linear history, no force push or deletion, admin bypass; required checks added once CI exists); labels; issues in project "xd-mod" (#3); Pages on robarm-manifest. Phase 4 runs autonomously within this list.

.. prj-dec:: Licence: Apache-2.0 for all repos
   :id: PRJ-DEC-0013
   :legacy_id: D137
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid

   **Licence: Apache-2.0 for all repos** (code, models, CAD, docs).

.. prj-dec:: Zephyr SDK 1.0.1, ARM toolchain only
   :id: PRJ-DEC-0014
   :legacy_id: D138
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0014

   **Zephyr SDK 1.0.1, ARM toolchain only**, installed into ``.venv/opt/zephyr-sdk`` and recorded in robarm-sw's ``tools.yaml`` with sha256.

.. prj-dec:: The workspace root before west init
   :id: PRJ-DEC-0015
   :legacy_id: D139
   :date: 2026-11-14
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0061, XD-ADR-0083

   **Workspace root before ``west init``:** ``spike/``, ``zdocs-tests/`` and ``.venv-zdocs/`` move to ``archive/``. The ``zdocs/`` clone becomes the west project ``tools/zdocs``, pinned to the PR branches (task 4.3a). ``extra/`` and ``build/`` stay. Nothing is deleted.

.. prj-dec:: Phase 4 merge rights
   :id: PRJ-DEC-0016
   :legacy_id: D140
   :date: 2026-11-15
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0044, XD-ADR-0051

   **Phase 4 merge rights:** initial skeletons go straight to ``main`` of the new repos before the ruleset is switched on. After that, all Phase 4 work goes through PRs, and the coordinator agent may merge them in xdmod and robarm-* once CI is green and the agent review has no blocking findings. The owner gets a summary of each merge. This is a Phase 4 exception to :need:`XD-ADR-0044` and :need:`XD-ADR-0051`.

.. prj-dec:: Rulesets per repo
   :id: PRJ-DEC-0017
   :legacy_id: D141
   :date: 2026-11-15
   :decision_status: accepted
   :status: valid
   :refines: PRJ-DEC-0012
   :follows: XD-ADR-0043, XD-ADR-0122

   **Rulesets are per repo, not per org.** Org rulesets need the GitHub Team plan. Each of the 7 repos has the same ``xdmod-main`` ruleset on its default branch: PR required (0 approvals, rebase only), linear history, no force push, no deletion. The admin role may bypass **only through a PR** (no direct pushes to ``main``). Required status checks and "branches up to date" (:need:`XD-ADR-0122`) are added in task 4.4, once each repo's CI check names exist. Refines :need:`PRJ-DEC-0012`.

.. prj-dec:: Required status checks
   :id: PRJ-DEC-0018
   :legacy_id: D142
   :date: 2026-11-15
   :decision_status: accepted
   :status: valid
   :follows: XD-ADR-0122, XD-ADR-0040

   **Required checks (task 4.4):** in each repo's ``xdmod-main`` ruleset, required status checks with "branches up to date" (:need:`XD-ADR-0122`) from the GitHub Actions app: xdmod ``tests`` + ``check / check``; robarm-syseng, -ee, -me, -sw, -integration ``check / check``; robarm-manifest ``full-set`` (check run on normal PRs, commit status on bump PRs). CI installs the pinned Doxygen 1.18.0 from the release tarball, because Ubuntu's 1.9.8 breaks ``sw-api``.
