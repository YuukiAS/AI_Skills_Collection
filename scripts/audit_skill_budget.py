#!/usr/bin/env python3
"""Audit active skill budget for profiles or project-local installations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from skill_utils import (
    AGENTS_END,
    AGENTS_START,
    MANIFEST_NAME,
    ROOT,
    audit_records,
    load_profiles,
    normalize_project_path,
    profile_skill_files,
    skill_record,
)


def managed_agents_block(project: Path) -> str:
    path = project / "AGENTS.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    if AGENTS_START in text and AGENTS_END in text:
        return AGENTS_START + text.split(AGENTS_START, 1)[1].split(AGENTS_END, 1)[0] + AGENTS_END
    return ""


def records_for_profile(profile_path: Path) -> tuple[str, list[dict]]:
    data = json.loads(profile_path.read_text(encoding="utf-8"))
    records = [skill_record(path) for path in profile_skill_files(data)]
    return str(data.get("name") or profile_path.stem), records


def records_for_project(project: Path) -> tuple[str, list[dict], str, int]:
    manifest_path = project / ".codex" / "skills" / MANIFEST_NAME
    if not manifest_path.exists():
        raise SystemExit(f"missing project manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    records = []
    for item in manifest.get("installed_skills", []):
        source = Path(item["source"]) / "SKILL.md"
        if source.exists():
            records.append(skill_record(source))
    return str(manifest.get("profile") or "unknown"), records, managed_agents_block(project), len(manifest.get("installed_skills", []))


def print_audit(label: str, records: list[dict], agents_text: str = "", project_count: int | None = None) -> int:
    audit = audit_records(records, agents_text)
    print(f"\n== {label} ==")
    print(f"active_skill_count: {audit['active_skill_count']}")
    if project_count is not None:
        print(f"project_local_skills: {project_count}")
    print(f"description_total_chars: {audit['description_total_chars']}")
    print(f"duplicate_description_count: {audit['duplicate_description_count']}")
    print(f"agents_block_chars: {audit['agents_block_chars']}")
    print(f"scope_distribution: {json.dumps(audit['scope_distribution'], ensure_ascii=False, sort_keys=True)}")
    print("longest_descriptions:")
    for item in audit["longest_descriptions"]:
        print(f"  - {item['chars']:>4} {item['path']}")
    if audit["warnings"]:
        print("warnings:")
        for warning in audit["warnings"]:
            print(f"  WARNING: {warning}")
    else:
        print("warnings: none")
    return 1 if audit["warnings"] else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", nargs="?", help="Profile JSON path to audit")
    parser.add_argument("--all", action="store_true", help="Audit every profile")
    parser.add_argument("--project", help="Audit an installed project")
    args = parser.parse_args()

    exit_code = 0
    if args.all:
        for path in sorted((ROOT / "profiles").glob("*.json")):
            label, records = records_for_profile(path)
            exit_code |= print_audit(label, records)
        return exit_code
    if args.project:
        project = normalize_project_path(args.project)
        label, records, block, count = records_for_project(project)
        return print_audit(f"project:{project} profile:{label}", records, block, count)
    if args.profile:
        path = Path(args.profile)
        if not path.is_absolute():
            path = ROOT / path
        label, records = records_for_profile(path)
        return print_audit(label, records)
    parser.error("provide --all, --project, or a profile JSON path")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
