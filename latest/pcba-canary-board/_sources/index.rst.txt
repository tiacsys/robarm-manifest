Canary Board (pcba-canary-board)
================================

This document describes the board ``canary-board``: the KiCad project
``pcba/canary-board/canary-board.kicad_pro`` and the board def of the EE model it implements. It was made
by ``curatrix new pcba``; every board document has the same sections (XD-ADR-0129). The tables come
from the KiCad files in plain Python; renderings, schematic and ERC/DRC findings come from the local
``curatrix cam`` output of the current commit and are not part of CI builds.

Overview
--------

.. xd-pcba-overview:: canary-board

Block diagram
-------------

The board def of the EE model with its connector ports (from the model; ``curatrix views build``):

.. sysml-view:: /views/canaryBoard.drawio.svg
   :caption: The canary board and its ports (view canaryBoard)

Variants
--------

.. xd-pcba-variants:: canary-board

.. sysml-view:: /views/canaryBoardVariants.drawio.svg
   :caption: The variants of the canary board in the EE model and what each serves (view canaryBoardVariants)

Renderings
----------

.. xd-pcba-renderings:: canary-board

Schematic
---------

.. xd-pcba-schematic:: canary-board

Stackup
-------

.. xd-pcba-stackup:: canary-board

Design rules
------------

.. xd-pcba-rules:: canary-board

Connectors
----------

.. xd-pcba-connectors:: canary-board

ERC and DRC findings
--------------------

.. xd-pcba-findings:: canary-board

Appendix: bill of materials
---------------------------

.. xd-pcba-bom:: canary-board
