import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(os.environ["ZDOCS_WEST_TOPDIR"]) / "xdmod" / "sphinx"))
from xdmod_conf import configure  # noqa: E402

configure(globals(), __file__, "Robot Arm: Project Overview")
