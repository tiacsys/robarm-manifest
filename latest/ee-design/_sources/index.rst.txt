EE Design
=========

This document holds the electrical design of the robot arm: the board and cable defs of the EE
model, how they refine the system model, and an overview of the boards and harnesses. The EE
requirements are in the EE Requirements Specification (``ee-req``), the EE tests in ``ee-test-spec``
and ``ee-test-report`` (V-model split, tiacsys/xdmod#69 decision Q8). Each board has its own
document (``pcba-<board>``, in ``docs/pcbas/``); every cable is in the document ``harnesses``.

.. note::

   This is a skeleton. The content comes in Phase 6.

What will go here
-----------------

* the design decisions that span boards and harnesses (supply, buses, connectors), with the EE
  requirements each one meets;
* the wiring of each prototype setup (NUCLEO-G474RE board, breakout boards, servos and
  potentiometers), or a link to its ``proto-<name>`` document.

The boards and their connector ports are defs in the EE model (``model/``), which refines the
system model by specialization (XD-ADR-0130). Their needs and links come from the model.

How the EE model refines the system model: each board and harness realizes a system element,
connector ports conform to system interfaces (none on the canary), and a board conforms to its
space budget. The lines are the trace links of the needs below (XD-ADR-0132):

.. sysml-view:: /views/eeAllocation.drawio.svg
   :caption: EE elements and the system elements and interfaces they realize or conform to (view eeAllocation)

``EE-PORT-0002`` (the plug of the bought test lead) has no board and conforms to no system
interface; only the cable connects it.

The canary board with its connector (each board document shows its own block diagram):

.. sysml-view:: /views/canaryBoard.drawio.svg
   :caption: Block diagram of the canary board (view canaryBoard)


.. needimport:: /generated/model-needs.json

Circuit blocks and components with a trace ID become needs. They are imported here from the
generated file:

.. needimport:: /generated/cad-needs.json
