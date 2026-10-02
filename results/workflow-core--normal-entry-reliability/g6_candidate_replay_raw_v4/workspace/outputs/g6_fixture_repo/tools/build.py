#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path


root = Path(__file__).resolve().parents[1]
source = (root / "src" / "message.txt").read_text(encoding="utf-8")
artifact = root / "dist" / "artifact.txt"
artifact.parent.mkdir(exist_ok=True)
artifact.write_text("built artifact:\n" + source, encoding="utf-8")
(root / "dist" / "artifact.sha256").write_text(
    hashlib.sha256(artifact.read_bytes()).hexdigest() + "\n",
    encoding="utf-8",
)
print(artifact)
