#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path


root = Path(__file__).resolve().parents[1]
artifact = root / "dist" / "artifact.txt"
expected = (root / "dist" / "artifact.sha256").read_text(encoding="utf-8").strip()
actual = hashlib.sha256(artifact.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit(f"hash mismatch: {actual} != {expected}")
print("check-ok", actual)
