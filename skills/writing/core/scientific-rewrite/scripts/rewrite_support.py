#!/usr/bin/env python3
from pathlib import Path
import runpy

_TARGET = Path(__file__).resolve().parents[2] / "clear-writing/scripts/rewrite_support.py"
_exports = runpy.run_path(str(_TARGET), run_name="__main__" if __name__ == "__main__" else "clear_writing_rewrite_support")
if __name__ != "__main__":
    globals().update({key: value for key, value in _exports.items() if not key.startswith("__")})
