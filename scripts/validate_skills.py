#!/usr/bin/env python3
"""Validate skill frontmatter and bundle layout."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"


def read_frontmatter(skill_file: Path) -> tuple[dict[str, Any] | None, str | None]:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return None, "missing YAML frontmatter"

    try:
        _, raw, _ = text.split("---", 2)
    except ValueError:
        return None, "unterminated YAML frontmatter"

    try:
        parsed = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        return None, f"invalid YAML frontmatter: {exc}"

    if not isinstance(parsed, dict):
        return None, "YAML frontmatter must be a mapping"
    return parsed, None


def validate_skill(skill_file: Path, names: dict[str, list[Path]]) -> list[str]:
    errors: list[str] = []
    rel = skill_file.relative_to(ROOT)

    if len(rel.parts) < 5:
        errors.append(f"skill is not under skills/<scope>/<category>/<skill>: {rel}")

    if not skill_file.read_text(encoding="utf-8", errors="replace").strip():
        errors.append(f"empty SKILL.md: {rel}")
        return errors

    meta, error = read_frontmatter(skill_file)
    if error:
        errors.append(f"{rel}: {error}")
        return errors

    assert meta is not None
    for key in ("name", "description"):
        value = meta.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{rel}: frontmatter field {key!r} must be a non-empty string")

    name = meta.get("name")
    if isinstance(name, str) and name.strip():
        names[name.strip()].append(rel)

    return errors


def validate_bundle(bundle_file: Path) -> list[str]:
    errors: list[str] = []
    rel = bundle_file.relative_to(ROOT)
    try:
        bundle = json.loads(bundle_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON in {rel}: {exc}"]

    include = bundle.get("include")
    if not isinstance(include, list):
        return [f"bundle missing include list: {rel}"]

    for item in include:
        if not isinstance(item, str):
            errors.append(f"bundle include item is not a string: {rel}")
            continue
        if not (ROOT / item).exists():
            errors.append(f"bundle path does not exist: {rel} -> {item}")

    return errors


def main() -> int:
    errors: list[str] = []
    names: dict[str, list[Path]] = defaultdict(list)

    for skill_file in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        if "archive" in skill_file.parts:
            continue
        errors.extend(validate_skill(skill_file, names))

    for name, paths in sorted(names.items()):
        if len(paths) > 1:
            joined = ", ".join(path.as_posix() for path in paths)
            errors.append(f"duplicate skill name {name!r}: {joined}")

    for bundle_file in sorted((ROOT / "bundles").glob("*.json")):
        errors.extend(validate_bundle(bundle_file))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("skills and bundles validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
