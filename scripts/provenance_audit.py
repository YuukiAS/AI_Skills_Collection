#!/usr/bin/env python3
"""Audit external source integration history and temporary intake hygiene."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from skill_utils import ROOT


DEFAULT_HISTORY = ROOT / "docs" / "provenance" / "INTEGRATION_HISTORY.md"
EXPECTED_COLUMNS = [
    "date",
    "source_type",
    "source",
    "revision",
    "permission/license",
    "decision",
    "target",
    "integration_commit",
    "note",
]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INTAKE_PREFIXES = (".tmp/skill-intake/", "build/skill-intake/", "archive/")


def parse_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    tables = [line for line in lines if line.startswith("|") and line.endswith("|")]
    if len(tables) < 2:
        return [], []
    header = [part.strip() for part in tables[0].strip("|").split("|")]
    rows: list[list[str]] = []
    for line in tables[2:]:
        rows.append([part.strip() for part in line.strip("|").split("|")])
    return header, rows


def tracked_files() -> list[str]:
    try:
        output = subprocess.check_output(["git", "-C", str(ROOT), "ls-files"], text=True)
    except (OSError, subprocess.CalledProcessError):
        return []
    return [line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()]


def audit_history(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing history file: {path.relative_to(ROOT).as_posix()}"]
    header, rows = parse_rows(path)
    if header != EXPECTED_COLUMNS:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: unexpected columns {header}")
    for index, row in enumerate(rows, start=1):
        if len(row) != len(EXPECTED_COLUMNS):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} has {len(row)} columns")
            continue
        date, source_type, source, revision, permission, decision, target, integration_commit, note = row
        if not DATE_RE.match(date):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} invalid date {date}")
        for label, value in {
            "source_type": source_type,
            "source": source,
            "revision": revision,
            "permission/license": permission,
            "decision": decision,
            "target": target,
            "integration_commit": integration_commit,
        }.items():
            if not value:
                errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} missing {label}")
        if note.lower().startswith("todo"):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} has unresolved note")
    return errors


def audit_intake_not_tracked() -> list[str]:
    errors: list[str] = []
    for path in tracked_files():
        if any(path.startswith(prefix) for prefix in INTAKE_PREFIXES):
            errors.append(f"temporary intake/archive path is tracked: {path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", default=str(DEFAULT_HISTORY), help="Path to integration history markdown")
    parser.add_argument("--check", action="store_true", help="Exit non-zero on audit errors")
    args = parser.parse_args()
    path = Path(args.history)
    if not path.is_absolute():
        path = ROOT / path
    errors = audit_history(path) + audit_intake_not_tracked()
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("provenance audit passed")
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
