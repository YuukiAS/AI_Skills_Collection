#!/usr/bin/env python3
"""Validate skill frontmatter, profiles, registry governance, and templates."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from skill_utils import (
    AGENTS_END,
    AGENTS_START,
    PROFILES_ROOT,
    ROOT,
    SKILLS_ROOT,
    iter_skill_files,
    load_profiles,
    profile_skill_files,
    read_frontmatter,
    resolve_skill_path,
    skill_record,
)


DESC_LIMIT = 350
DEFAULT_PROFILE_LIMIT = 35
SYSTEM_ALLOWED_PROFILES = {"codex-core-global", "codex-skill-maintenance"}


def normalized_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def validate_skill(skill_file: Path, names: dict[str, list[Path]], norm_names: dict[str, list[Path]]) -> list[str]:
    errors: list[str] = []
    rel = skill_file.relative_to(ROOT)
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return [f"empty SKILL.md: {rel}"]
    meta, _ = read_frontmatter(skill_file)
    if not meta:
        return [f"{rel}: missing or invalid YAML-like frontmatter"]
    for key in ("name", "description"):
        value = meta.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{rel}: frontmatter field {key!r} must be a non-empty string")
    name = str(meta.get("name") or "").strip()
    desc = str(meta.get("description") or "").strip()
    if len(desc) > DESC_LIMIT:
        errors.append(f"{rel}: description too long ({len(desc)} chars > {DESC_LIMIT}); keep trigger text concise")
    if name:
        names[name].append(rel)
        norm_names[normalized_name(name)].append(rel)
    if len(rel.parts) < 4:
        errors.append(f"{rel}: skill is not under skills/<scope>/<category>/<skill>")
    return errors


def validate_profile(profile_name: str, profile: dict[str, Any], archived_paths: set[str]) -> list[str]:
    errors: list[str] = []
    skills = profile.get("skills")
    if not isinstance(skills, list) or not skills:
        return [f"profile {profile_name}: missing non-empty skills list"]
    limit = int(profile.get("max_active_skills") or DEFAULT_PROFILE_LIMIT)
    if len(skills) > limit:
        errors.append(f"profile {profile_name}: {len(skills)} skills exceeds max_active_skills={limit}")
    for item in skills + list(profile.get("secondary_skills", [])):
        if not isinstance(item, str):
            errors.append(f"profile {profile_name}: skill reference is not a string: {item!r}")
            continue
        skill_file = resolve_skill_path(item)
        if not skill_file.exists():
            errors.append(f"profile {profile_name}: missing skill path {item}")
            continue
        rel = skill_file.parent.relative_to(ROOT).as_posix()
        record = skill_record(skill_file)
        if rel in archived_paths or record.get("status") == "archived":
            errors.append(f"profile {profile_name}: references archived skill {rel}")
        systemish = (
            rel.startswith("skills/system/")
            or "plugin" in rel
            or "installer" in rel
            or "mcp" in rel
            or "cursor-skills" in rel
        )
        if systemish and profile_name not in SYSTEM_ALLOWED_PROFILES:
            errors.append(f"profile {profile_name}: system/installer/plugin skill is only allowed in core or maintenance: {rel}")
    return errors


def validate_legacy_bundle(bundle_file: Path) -> list[str]:
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
        elif not (ROOT / item).exists():
            errors.append(f"bundle path does not exist: {rel} -> {item}")
    return errors


def validate_agents_template() -> list[str]:
    template = ROOT / "shared" / "templates" / "AGENTS.md.template"
    if not template.exists():
        return [f"missing AGENTS.md template: {template.relative_to(ROOT)}"]
    text = template.read_text(encoding="utf-8", errors="replace")
    if AGENTS_START not in text or AGENTS_END not in text:
        return [f"AGENTS.md template must include {AGENTS_START} and {AGENTS_END}"]
    return []


def main() -> int:
    errors: list[str] = []
    names: dict[str, list[Path]] = defaultdict(list)
    norm_names: dict[str, list[Path]] = defaultdict(list)
    archived_paths: set[str] = set()

    for skill_file in iter_skill_files(include_archive=True):
        meta, _ = read_frontmatter(skill_file)
        rel = skill_file.parent.relative_to(ROOT).as_posix()
        if "archive" in skill_file.parts or meta.get("status") == "archived":
            archived_paths.add(rel)
            continue
        errors.extend(validate_skill(skill_file, names, norm_names))

    for name, paths in sorted(names.items()):
        if len(paths) > 1:
            errors.append(f"duplicate skill name {name!r}: {', '.join(path.as_posix() for path in paths)}")
    for name, paths in sorted(norm_names.items()):
        if len(paths) > 1:
            errors.append(f"highly similar skill name {name!r}: {', '.join(path.as_posix() for path in paths)}")

    profiles = load_profiles()
    required = {
        "codex-core-global",
        "codex-webdev",
        "codex-research-writing",
        "codex-bayesian-jsdm",
        "codex-cardiacnexus",
        "codex-bioinformatics-light",
        "codex-skill-maintenance",
    }
    missing = required - set(profiles)
    if missing:
        errors.append(f"missing required profiles: {', '.join(sorted(missing))}")
    for name, profile in sorted(profiles.items()):
        errors.extend(validate_profile(name, profile, archived_paths))

    for bundle_file in sorted((ROOT / "bundles").glob("*.json")):
        errors.extend(validate_legacy_bundle(bundle_file))

    errors.extend(validate_agents_template())

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("skills, profiles, bundles, and AGENTS template validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
