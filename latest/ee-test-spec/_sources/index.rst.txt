EE Test Specification
=====================

This document lists the EE test cases (``EE-TC``) and the EE requirements each one verifies.

.. note::

   No EE test case yet: there is no EE requirement to verify (``ee-req``), and the canary board
   has no test of its own.

What will go here
-----------------

* the EE test cases (``.. ee-tc::``), each with the ``EE-REQ`` it verifies, its method (test,
  inspection, analysis, demonstration) and its setup;
* scripted bench tests of the boards (``tests/``, JUnit output), run on hardware like the
  integration tests.

What is not an EE test
----------------------

The design checks of ``curatrix check robarm-ee`` are not test cases: ERC and DRC (CK-F4a, CK-F4b),
the connector and harness ends against the EE model (CK-F1), the BOM fields (CK-F12). They check the
design files against rules, not a built board against a requirement, and verify no ``EE-REQ``.
Their results, with the accepted findings, are in the board documents (``pcba-<board>``, section
"ERC and DRC") and in the check run. The tests of the system and of the integrated arm are in
robarm-integration (``int-test-spec``).
