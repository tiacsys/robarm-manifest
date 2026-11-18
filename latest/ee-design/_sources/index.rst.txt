EE Requirements and Design
==========================

This document holds the electrical requirements of the robot arm and the electrical design that
meets them.

.. note::

   This is a skeleton. The content comes in Phase 6.

What will go here
-----------------

* the EE requirements, written as EARS sentences, each refining a system requirement;
* the design of each PCBA: schematic sheets, bill of materials, and the nets compared with the
  system interfaces (all read from the KiCad files);
* the wiring of each prototype setup (NUCLEO-G474RE board, breakout boards, servos and
  potentiometers);
* the EE test cases and their results.

In iteration 1 this is one document. It will be split into a requirements document, one document
per PCBA, one per prototype setup, and test documents once that content exists.

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
