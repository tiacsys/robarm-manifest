Harnesses
=========

This document describes every cable of the electrical assembly: one section per harness folder
``harness/<cable>/`` with its WireViz file ``<cable>.yml`` and the cable def of the EE model it
implements (XD-ADR-0127). Each section has the same parts: the ends and the ports they mate with,
the WireViz diagram, the pin-to-pin wiring and the harness bill of materials.

The ends, the wiring and the BOM are read from the YAML in plain Python and appear in every build.
The diagram comes from the local ``curatrix cam robarm-ee`` output (every board and harness of the
repo); CI and Pages builds do not have it, and a local build names the cables whose run is missing
or from an older commit.

.. xd-harnesses::
