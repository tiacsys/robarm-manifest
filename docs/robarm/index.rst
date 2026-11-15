Robot Arm: Project Overview
===========================

This is the start page of the robot arm documents. The robot arm is the worked example of
XDMOD (Cross-Domain MODeling): a leader arm that a person moves by hand, and a follower arm
that copies its moves. Iteration 1 covers the whole system at the requirements level, and one
joint from end to end, down to Zephyr firmware on a NUCLEO-G474RE board.

The documents below form one linked set. Each one lives in the repo that owns its content, and
this page is built together with all of them from one west workspace. The manifest repo
(``robarm-manifest``) pins the version of every repo, so the set always fits together.

Documents
---------

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Area
     - Document
     - Repo
   * - System
     - :external+se-req:doc:`index`
     - ``robarm-syseng``
   * -
     - :external+se-arch:doc:`index`
     - ``robarm-syseng``
   * - Software
     - :external+sw-req:doc:`index`
     - ``robarm-sw``
   * -
     - :external+sw-arch:doc:`index`
     - ``robarm-sw``
   * -
     - `SW API and Implementation <../sw-api/index.html>`__ (Doxygen)
     - ``robarm-sw``
   * -
     - :external+sw-test-spec:doc:`index`
     - ``robarm-sw``
   * -
     - :external+sw-test-report:doc:`index`
     - ``robarm-sw``
   * - Electrical
     - :external+ee-design:doc:`index`
     - ``robarm-ee``
   * - Mechanical
     - :external+me-design:doc:`index`
     - ``robarm-me``
   * - Integration
     - :external+int-test-spec:doc:`index`
     - ``robarm-integration``
   * -
     - :external+int-test-report:doc:`index`
     - ``robarm-integration``

The XDMOD manual (methods, trace model, ID scheme) will be added to this set once it exists.

Get the workspace
-----------------

You need git and Python 3.12 or newer. Start in an empty folder. It becomes the workspace root,
and every command runs from there.

.. code-block:: sh

   git clone https://github.com/tiacsys/robarm-manifest
   robarm-manifest/scripts/bootstrap.sh --role <role>

The script creates ``.venv`` with west, runs ``west init`` and ``west update``, installs
``curatrix`` from xdmod, and then runs ``curatrix bootstrap --role <role>``. That sets up the
repos, tools and agent files for the role. Pick the role that matches your work:

.. list-table::
   :header-rows: 1
   :widths: 15 35 50

   * - Role
     - Group filter
     - You get
   * - ``syseng``
     - (manifest default)
     - xdmod, zdocs, affirmatrix, robarm-syseng, SYSMOD and PLEML libraries, Zephyr
   * - ``ee``
     - ``+ee``
     - the above, plus robarm-ee and the KiCad libraries (no 3D models)
   * - ``ee3d``
     - ``+ee,+kicad-3d``
     - like ``ee``, plus the KiCad 3D models (about 1.8 GB)
   * - ``me``
     - ``+me,+freecad-parts``
     - the default set, plus robarm-me and the FreeCAD parts library (about 5.7 GB)
   * - ``sw``
     - ``+sw``
     - the default set, plus robarm-sw
   * - ``integration``
     - ``+ee,+me,+sw,+integration``
     - every repo, without the big libraries
   * - ``full``
     - all groups
     - everything, including the big libraries (local full builds and baselines)

To change the role later, run ``curatrix bootstrap --role <other>``. Then ``curatrix doctor``
checks the setup.

Reports
-------

.. toctree::
   :maxdepth: 1

   trace-report
   coverage-matrix
   change-report
   decisions
