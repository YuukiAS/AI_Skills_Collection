#!/usr/bin/env python3
"""Shared helpers for AI_Skills_Collection maintenance scripts."""

from __future__ import annotations

import json
import os
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
PROFILES_ROOT = ROOT / "profiles"
MANIFEST_NAME = ".ai-skills-collection-manifest.json"
AGENTS_START = "<!-- AI_SKILLS_COLLECTION_START -->"
AGENTS_END = "<!-- AI_SKILLS_COLLECTION_END -->"


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value in {"null", "None", "~"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value.replace("'", '"'))
        except json.JSONDecodeError:
            return [part.strip().strip('"').strip("'") for part in value[1:-1].split(",") if part.strip()]
    return value


def read_frontmatter(skill_file: Path) -> tuple[dict[str, Any], str]:
    text = skill_file.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}, text
    try:
        _, raw, body = text.split("---", 2)
    except ValueError:
        return {}, text

    meta: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, meta)]
    last_key_at_indent: dict[int, str] = {}

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if stripped.startswith("- "):
            item = parse_scalar(stripped[2:])
            if isinstance(parent, list):
                parent.append(item)
            continue

        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", stripped)
        if not match:
            continue
        key, value = match.groups()
        if value == "":
            container: dict[str, Any] = {}
            if isinstance(parent, dict):
                parent[key] = container
            stack.append((indent, container))
            last_key_at_indent[indent] = key
        else:
            parsed = parse_scalar(value)
            if isinstance(parent, dict):
                parent[key] = parsed
            last_key_at_indent[indent] = key

    return meta, body.lstrip("\n")


def format_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or text.startswith(("{", "[", "#")) or ":" in text or text.lower() in {"true", "false", "null"}:
        return json.dumps(text, ensure_ascii=False)
    return text


def write_frontmatter(skill_file: Path, meta: dict[str, Any], body: str) -> None:
    preferred = [
        "name",
        "description",
        "status",
        "provenance",
        "trusted",
        "requires_network",
        "writes_files",
        "executes_code",
        "secrets_needed",
        "last_reviewed",
        "profile_tags",
        "recommended_scope",
        "license",
        "metadata",
    ]
    keys = [key for key in preferred if key in meta] + sorted(key for key in meta if key not in preferred)
    lines = ["---"]
    for key in keys:
        value = meta[key]
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {format_scalar(item)}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for sub_key, sub_value in value.items():
                lines.append(f"  {sub_key}: {format_scalar(sub_value)}")
        else:
            lines.append(f"{key}: {format_scalar(value)}")
    lines.append("---")
    lines.append("")
    skill_file.write_text("\n".join(lines) + body.lstrip("\n"), encoding="utf-8")


def iter_skill_files(include_archive: bool = False) -> list[Path]:
    files = []
    for path in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        if not include_archive and "archive" in path.parts:
            continue
        meta, _ = read_frontmatter(path)
        if not include_archive and meta.get("status") == "archived":
            continue
        files.append(path)
    return files


def skill_rel_dir(skill_file: Path) -> Path:
    return skill_file.parent.relative_to(ROOT)


def skill_flat_name(skill_dir: Path) -> str:
    rel = skill_dir.relative_to(SKILLS_ROOT) if skill_dir.is_relative_to(SKILLS_ROOT) else skill_dir.relative_to(ROOT)
    return "-".join(rel.parts)


def skill_record(skill_file: Path, include_body: bool = False) -> dict[str, Any]:
    rel_dir = skill_rel_dir(skill_file)
    parts = rel_dir.parts
    scope = parts[1] if len(parts) > 1 else ""
    category = parts[2] if len(parts) > 2 else ""
    slug = parts[-1]
    meta, body = read_frontmatter(skill_file)
    status = str(meta.get("status") or ("archived" if "archive" in skill_file.parts else "active"))
    record: dict[str, Any] = {
        "id": ".".join(part for part in (scope, category, slug) if part),
        "name": str(meta.get("name") or slug),
        "path": rel_dir.as_posix(),
        "flat_name": skill_flat_name(skill_file.parent),
        "scope": scope,
        "category": category,
        "description": str(meta.get("description") or ""),
        "status": status,
        "provenance": meta.get("provenance", "unknown"),
        "trusted": bool(meta.get("trusted", False)),
        "requires_network": bool(meta.get("requires_network", False)),
        "writes_files": bool(meta.get("writes_files", True)),
        "executes_code": bool(meta.get("executes_code", False)),
        "secrets_needed": meta.get("secrets_needed", []),
        "last_reviewed": meta.get("last_reviewed", ""),
        "profile_tags": meta.get("profile_tags", []),
        "recommended_scope": meta.get("recommended_scope", "project"),
    }
    if include_body:
        record["body"] = body
    return record


def load_profiles() -> dict[str, dict[str, Any]]:
    profiles: dict[str, dict[str, Any]] = {}
    if not PROFILES_ROOT.exists():
        return profiles
    for path in sorted(PROFILES_ROOT.glob("*.json")):
        if path.name == "README.md":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        name = data.get("name") or path.stem
        data["_path"] = path
        profiles[str(name)] = data
    return profiles


def resolve_skill_path(item: str) -> Path:
    path = (ROOT / item).resolve() if not Path(item).is_absolute() else Path(item)
    if path.is_dir() and (path / "SKILL.md").exists():
        return path / "SKILL.md"
    if path.name == "SKILL.md":
        return path
    return path / "SKILL.md"


def profile_skill_files(profile: dict[str, Any]) -> list[Path]:
    files: list[Path] = []
    for item in profile.get("skills", []):
        path = resolve_skill_path(str(item))
        if path.exists():
            files.append(path)
    return files


def normalize_project_path(raw: str) -> Path:
    expanded = os.path.expandvars(os.path.expanduser(raw))
    match = re.match(r"^([A-Za-z]):[\\/](.*)$", expanded)
    if match and os.name != "nt":
        drive, rest = match.groups()
        candidate = Path("/mnt") / drive.lower() / rest.replace("\\", "/")
        if candidate.exists() or candidate.parent.exists():
            return candidate.resolve()
    return Path(expanded).resolve()


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def audit_records(records: list[dict[str, Any]], agents_text: str = "") -> dict[str, Any]:
    descs = [str(record.get("description") or "") for record in records]
    norm_counts = Counter(re.sub(r"\W+", " ", desc.lower()).strip() for desc in descs if desc)
    scopes = Counter(str(record.get("scope") or "unknown") for record in records)
    categories = Counter(f"{record.get('scope')}/{record.get('category')}" for record in records)
    longest = sorted(records, key=lambda r: len(str(r.get("description") or "")), reverse=True)[:5]
    warnings: list[str] = []
    if len(records) > 35:
        warnings.append(f"profile_too_wide: {len(records)} active skills; split or remove low-frequency skills until <=35")
    total_desc = sum(len(desc) for desc in descs)
    if total_desc > 7000:
        warnings.append(f"description_budget_high: {total_desc} chars; compress descriptions or narrow the profile")
    for record in longest:
        if len(str(record.get("description") or "")) > 350:
            warnings.append(f"description_too_long: {record['path']} has {len(record['description'])} chars; keep <=350")
    duplicates = [desc for desc, count in norm_counts.items() if desc and count > 1]
    if duplicates:
        warnings.append(f"duplicate_descriptions: {len(duplicates)} repeated descriptions; merge or specialize triggers")
    if len(agents_text) > 12000:
        warnings.append(f"agents_block_too_long: {len(agents_text)} chars; shorten routing entries")
    return {
        "active_skill_count": len(records),
        "description_total_chars": total_desc,
        "longest_descriptions": [
            {"path": r["path"], "name": r["name"], "chars": len(str(r.get("description") or ""))}
            for r in longest
        ],
        "duplicate_description_count": len(duplicates),
        "scope_distribution": dict(scopes),
        "category_distribution": dict(categories),
        "agents_block_chars": len(agents_text),
        "warnings": warnings,
    }
