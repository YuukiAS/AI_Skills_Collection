#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def resolve_xelatex() -> str:
    found = shutil.which("xelatex")
    if found:
        return found
    tinytex = Path.home() / ".TinyTeX/bin/x86_64-linux/xelatex"
    if tinytex.exists():
        return str(tinytex)
    raise SystemExit("xelatex not found")


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: project_venue_render.py SOURCE OUTPUT WORK_DIR", file=sys.stderr)
        return 2
    source = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    work_dir = Path(sys.argv[3]).resolve()
    work_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        resolve_xelatex(),
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory",
        str(work_dir),
        str(source),
    ]
    for _ in range(2):
        proc = subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if proc.returncode != 0:
            print(proc.stdout, file=sys.stderr)
            return proc.returncode
    produced = work_dir / f"{source.stem}.pdf"
    if not produced.exists():
        print(f"missing produced PDF: {produced}", file=sys.stderr)
        return 1
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(produced, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
