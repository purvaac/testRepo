"""Make the top-level modules importable from tests.

Explicit rather than relying on pytest's rootdir sys.path insertion, and
bytecode writing is off because the sandbox mounts the repo read-only.
"""

import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(__file__))
