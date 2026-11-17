Board Library
=============

This library holds FreeCAD models of the robot arm's boards, one file per tagged board version and
variant. The electrical engineering repo (robarm-ee) writes them, the mechanical engineering repo
(robarm-me) reads them, so neither depends on the other's repo.

How a board version gets here
-----------------------------

1. The owner tags a board version in robarm-ee (``<board>/vX.Y.Z``). Previews and untagged
   commits never go into the library.
2. The EE agent runs ``curatrix cam robarm-ee <board> --library`` in a worktree set. It exports
   the board with ``kicad-cli pcb export step`` (per variant, without tracks), imports the STEP
   file headless into FreeCAD, sets the board's ``EE-PCBA`` ID, version and variant as properties,
   and saves the model uncompressed as ``boards/<board>/<board>-<version>[-<variant>].FCStd``.
3. The EE agent opens the pull request that adds the files. A file may be at most 5 MB.

An assembly in robarm-me links one fixed board version. When a newer version is here, the
robarm-me check reports it; moving an assembly to the new version is an ME change.

Board versions
--------------

.. board-versions::
