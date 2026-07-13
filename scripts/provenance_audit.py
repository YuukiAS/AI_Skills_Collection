#!/usr/bin/env python3
"""Audit external source integration history and temporary intake hygiene."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from skill_utils import ROOT


DEFAULT_HISTORY = ROOT / "docs" / "provenance" / "INTEGRATION_HISTORY.md"
DEFAULT_INTAKE = ROOT / "docs" / "provenance" / "AI_RESOURCES_INTAKE_V3_6.md"
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
INTAKE_COLUMNS = [
    "notion_page",
    "type",
    "readable_evidence",
    "public_source_verification",
    "decision",
    "target",
    "integration_commit",
    "utilized_reconciled",
    "note",
]
INTAKE_DECISIONS = {
    "merged",
    "partially-merged",
    "reference-only",
    "reviewed-not-adopted",
    "unresolved-asset",
    "rejected",
}
NON_ADOPTED_DECISIONS = {"reviewed-not-adopted", "unresolved-asset", "rejected"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PENDING_RE = re.compile(r"\bpending-[A-Za-z0-9.-]+\b")
INTAKE_PREFIXES = (".tmp/skill-intake/", ".tmp/archive/", "build/skill-intake/", ".codex_tmp_notion_images/")


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
    pending_tokens = {
        token
        for row in rows
        if len(row) == len(EXPECTED_COLUMNS)
        for token in PENDING_RE.findall(row[7])
    }
    closure_text = "\n".join(
        " ".join(row)
        for row in rows
        if len(row) == len(EXPECTED_COLUMNS) and row[5] in {"closed", "closure"}
    )
    for token in sorted(pending_tokens):
        if token not in closure_text:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: {token} has no closure row")
    return errors


def audit_intake_table(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing intake file: {path.relative_to(ROOT).as_posix()}"]
    header, rows = parse_rows(path)
    if header != INTAKE_COLUMNS:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: unexpected columns {header}")
        return errors
    if len(rows) != 14:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: expected 14 intake rows, found {len(rows)}")
    for index, row in enumerate(rows, start=1):
        if len(row) != len(INTAKE_COLUMNS):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} has {len(row)} columns")
            continue
        notion_page, page_type, evidence, public_check, decision, target, integration_commit, utilized, note = row
        for label, value in {
            "notion_page": notion_page,
            "type": page_type,
            "readable_evidence": evidence,
            "public_source_verification": public_check,
            "decision": decision,
            "target": target,
            "integration_commit": integration_commit,
            "utilized_reconciled": utilized,
            "note": note,
        }.items():
            if not value:
                errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} missing {label}")
        if decision not in INTAKE_DECISIONS:
            errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} invalid decision {decision}")
        if integration_commit.startswith("pending-"):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} has pending integration commit")
        if decision not in NON_ADOPTED_DECISIONS:
            primary_target = target.split()[0]
            if primary_target != "none" and not (ROOT / primary_target).exists():
                errors.append(f"{path.relative_to(ROOT).as_posix()}: row {index} target does not exist: {primary_target}")
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
    parser.add_argument("--intake", default=str(DEFAULT_INTAKE), help="Path to v3.6 intake markdown")
    parser.add_argument("--check", action="store_true", help="Exit non-zero on audit errors")
    args = parser.parse_args()
    path = Path(args.history)
    if not path.is_absolute():
        path = ROOT / path
    intake_path = Path(args.intake)
    if not intake_path.is_absolute():
        intake_path = ROOT / intake_path
    errors = audit_history(path) + audit_intake_table(intake_path) + audit_intake_not_tracked()
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("provenance audit passed")
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
