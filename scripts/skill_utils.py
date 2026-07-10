#!/usr/bin/env python3
"""Shared helpers for AI_Skills_Collection maintenance scripts."""

from __future__ import annotations

import json
import os
import re
import shutil
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
REPO_SKILLS_DIR = Path(".agents") / "skills"
USER_SKILLS_ROOT = Path.home() / ".agents" / "skills"
LEGACY_PROJECT_SKILLS_DIR = Path(".codex") / "skills"
SYSTEM_SCOPE_NAMES = {".system", "system", "core"}
CANONICAL_SCOPES = {
    "domains": "domain",
    "domain": "domain",
    "tools": "tool",
    "reusable": "tool",
    "writing": "writing",
    "science": "science",
    "research": "science",
    "projects": "project",
    "project": "project",
    "core": "core",
    "system": "core",
}


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
    lines = raw.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if indent != 0:
            index += 1
            continue

        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", stripped)
        if not match:
            index += 1
            continue
        key, value = match.groups()
        if value != "":
            meta[key] = parse_scalar(value)
            index += 1
            continue

        nested: list[str] = []
        index += 1
        while index < len(lines):
            nested_line = lines[index]
            if not nested_line.strip() or nested_line.lstrip().startswith("#"):
                index += 1
                continue
            nested_indent = len(nested_line) - len(nested_line.lstrip(" "))
            if nested_indent <= indent:
                break
            nested.append(nested_line)
            index += 1

        if not nested:
            meta[key] = None
            continue
        if all(item.strip().startswith("- ") for item in nested):
            meta[key] = [parse_scalar(item.strip()[2:]) for item in nested]
            continue

        nested_dict: dict[str, Any] = {}
        for item in nested:
            item_stripped = item.strip()
            nested_match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", item_stripped)
            if nested_match:
                nested_key, nested_value = nested_match.groups()
                nested_dict[nested_key] = parse_scalar(nested_value)
        meta[key] = nested_dict

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
        "source_repo_url",
        "source_path",
        "source_ref",
        "source_imported_at",
        "source_license",
        "source_note",
        "trusted",
        "requires_network",
        "writes_files",
        "executes_code",
        "secrets_needed",
        "last_reviewed",
        "profile_tags",
        "recommended_scope",
        "license",
        "source_skills",
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
        rel_parts = path.relative_to(SKILLS_ROOT).parts
        if any(part.startswith(".") for part in rel_parts):
            continue
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


def normalize_list(value: Any) -> list[Any]:
    if value in (None, "", {}):
        return []
    if isinstance(value, list):
        return value
    return [value]


def infer_taxonomy(skill_file: Path) -> dict[str, str]:
    rel_dir = skill_rel_dir(skill_file)
    rel_parts = rel_dir.parts
    parts = rel_parts[1:] if rel_parts and rel_parts[0] == "skills" else rel_parts
    raw_scope = parts[0] if parts else ""
    scope = CANONICAL_SCOPES.get(raw_scope, raw_scope)
    domain = ""
    category = ""
    subcategory = ""
    slug = parts[-1] if parts else ""

    if raw_scope in {"domains", "domain"} and len(parts) >= 3:
        domain = parts[1]
        if len(parts) >= 4:
            subcategory = "/".join(parts[2:-1])
        category = f"domain/{domain}" + (f"/{subcategory}" if subcategory else "")
    elif raw_scope == "writing" and len(parts) >= 3:
        category = parts[1]
        subcategory = category
        domain = "writing" if category == "core" else f"{category}-writing"
    elif raw_scope in {"science", "research"} and len(parts) >= 3:
        category = parts[1]
        subcategory = category
        domain = f"research-{category}"
    elif raw_scope in {"tools", "reusable"} and len(parts) >= 3:
        category = parts[1]
        subcategory = category
        domain = category
    elif raw_scope in {"projects", "project"} and len(parts) >= 3:
        category = parts[1]
        subcategory = category
        domain = parts[1].lower()
    elif raw_scope in SYSTEM_SCOPE_NAMES and len(parts) >= 2:
        scope = "core"
        category = "codex-system" if parts[0] == ".system" else parts[1]
        subcategory = category
        domain = "core"
    elif len(parts) >= 2:
        category = parts[1]
        subcategory = category
        domain = category

    selector = "/".join(part for part in (scope, domain if scope == "domain" else category, slug) if part)
    return {
        "scope": scope,
        "domain": domain,
        "category": category,
        "subcategory": subcategory,
        "slug": slug,
        "selector": selector,
        "relative_selector": "/".join(parts),
    }


def skill_selectors(rel_dir: Path, taxonomy: dict[str, str], flat_name: str, name: str) -> set[str]:
    parts = rel_dir.parts[1:] if rel_dir.parts and rel_dir.parts[0] == "skills" else rel_dir.parts
    scope = taxonomy["scope"]
    domain = taxonomy["domain"]
    category = taxonomy["category"]
    subcategory = taxonomy["subcategory"]
    slug = taxonomy["slug"]
    selectors = {
        "/".join(parts),
        rel_dir.as_posix(),
        flat_name,
        name,
        taxonomy["selector"],
        taxonomy["relative_selector"],
    }
    if scope == "domain":
        selectors.add(f"domain/{domain}/{slug}")
        selectors.add(f"domains/{domain}/{slug}")
        if subcategory:
            selectors.add(f"domain/{domain}/{subcategory}/{slug}")
            selectors.add(f"domains/{domain}/{subcategory}/{slug}")
        selectors.add(f"skills/domain/{domain}/{slug}")
    elif scope == "tool":
        selectors.add(f"tool/{domain}/{slug}")
        selectors.add(f"tools/{domain}/{slug}")
        selectors.add(f"reusable/{domain}/{slug}")
        selectors.add(f"skills/reusable/{domain}/{slug}")
    elif scope == "writing":
        selectors.add(f"writing/{subcategory}/{slug}")
        selectors.add(f"writing/{slug}")
        if subcategory == "core":
            selectors.add(f"reusable/writing/{slug}")
            selectors.add(f"skills/reusable/writing/{slug}")
    elif scope == "science":
        selectors.add(f"science/{subcategory}/{slug}")
        selectors.add(f"research/{subcategory}/{slug}")
        selectors.add(f"skills/research/{subcategory}/{slug}")
    elif scope == "project":
        selectors.add(f"project/{domain}/{slug}")
        selectors.add(f"projects/{domain}/{slug}")
        selectors.add(f"skills/project/{domain}/{slug}")
    elif scope == "core":
        selectors.add(f"core/{category}/{slug}")
        selectors.add(f"system/{category}/{slug}")
        selectors.add(f"skills/system/{category}/{slug}")
    if name == "writing-fidelity":
        selectors.update(
            {
                "source-faithful-writing-final-pass",
                "reusable/writing/source-faithful-writing-final-pass",
                "skills/reusable/writing/source-faithful-writing-final-pass",
            }
        )
    elif name == "scientific-prose":
        selectors.update({"scientific-evidence-prose", "reusable/writing/scientific-evidence-prose"})
    elif name == "chinese-prose":
        selectors.update({"natural-chinese-final-pass", "reusable/writing/natural-chinese-final-pass"})
    return selectors


def skill_record(skill_file: Path, include_body: bool = False) -> dict[str, Any]:
    rel_dir = skill_rel_dir(skill_file)
    taxonomy = infer_taxonomy(skill_file)
    scope = taxonomy["scope"]
    category = taxonomy["category"]
    domain = taxonomy["domain"]
    subcategory = taxonomy["subcategory"]
    slug = taxonomy["slug"]
    meta, body = read_frontmatter(skill_file)
    status = str(meta.get("status") or ("archived" if "archive" in skill_file.parts else "active"))
    flat_name = skill_flat_name(skill_file.parent)
    source_selector = "/".join(rel_dir.parts[1:])
    record: dict[str, Any] = {
        "id": ".".join(part for part in (scope, domain or category, slug) if part),
        "name": str(meta.get("name") or slug),
        "path": rel_dir.as_posix(),
        "flat_name": flat_name,
        "scope": scope,
        "domain": domain,
        "category": category,
        "subcategory": subcategory,
        "slug": slug,
        "install_selector": taxonomy["selector"],
        "description": str(meta.get("description") or ""),
        "status": status,
        "provenance": meta.get("provenance", "unknown"),
        "source_repo_url": meta.get("source_repo_url", ""),
        "source_path": meta.get("source_path", ""),
        "source_ref": meta.get("source_ref", ""),
        "source_imported_at": meta.get("source_imported_at", ""),
        "source_license": meta.get("source_license", ""),
        "source_note": meta.get("source_note", ""),
        "source_skills": normalize_list(meta.get("source_skills", [])),
        "trusted": bool(meta.get("trusted", False)),
        "requires_network": bool(meta.get("requires_network", False)),
        "writes_files": bool(meta.get("writes_files", True)),
        "executes_code": bool(meta.get("executes_code", False)),
        "secrets_needed": normalize_list(meta.get("secrets_needed", [])),
        "last_reviewed": meta.get("last_reviewed", ""),
        "profile_tags": normalize_list(meta.get("profile_tags", [])),
        "recommended_scope": meta.get("recommended_scope", "project"),
        "selectors": sorted(skill_selectors(rel_dir, taxonomy, flat_name, str(meta.get("name") or slug)) - {""}),
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


def detect_git_root(start: Path | None = None) -> tuple[Path, bool]:
    base = (start or Path.cwd()).resolve()
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=base, text=True, stderr=subprocess.DEVNULL)
        return Path(out.strip()).resolve(), True
    except Exception:
        return base, False


def codex_home() -> tuple[str | None, Path]:
    raw = os.environ.get("CODEX_HOME")
    if raw:
        return raw, normalize_project_path(raw)
    return None, Path.home() / ".codex"


def target_skills_root(target: str, project: Path | None = None) -> Path:
    if target == "repo":
        if project is None:
            project, _ = detect_git_root()
        return project / REPO_SKILLS_DIR
    if target == "user":
        return USER_SKILLS_ROOT
    if target == "codex-home":
        _, home = codex_home()
        return home / "skills"
    raise ValueError(f"unknown target: {target}")


def active_skill_records(include_archive: bool = False) -> list[dict[str, Any]]:
    return [skill_record(path) for path in iter_skill_files(include_archive=include_archive)]


def active_skill_files(include_archive: bool = False) -> list[Path]:
    return iter_skill_files(include_archive=include_archive)


def records_by_selector(include_archive: bool = False) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    for record in active_skill_records(include_archive=include_archive):
        for selector in record.get("selectors", []):
            mapping[str(selector)] = record
        mapping[record["path"]] = record
    return mapping


def record_source_dir(record: dict[str, Any]) -> Path:
    return ROOT / str(record["path"])


def select_records(
    profiles: list[str] | None = None,
    domains: list[str] | None = None,
    categories: list[str] | None = None,
    skills: list[str] | None = None,
    include_archive: bool = False,
) -> list[dict[str, Any]]:
    records = active_skill_records(include_archive=include_archive)
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add(record: dict[str, Any]) -> None:
        key = str(record["path"])
        if key not in seen and (include_archive or record.get("status") == "active"):
            selected.append(record)
            seen.add(key)

    profile_data = load_profiles()
    for profile_name in profiles or []:
        if profile_name not in profile_data:
            raise SystemExit(f"unknown profile: {profile_name}")
        for path in profile_skill_files(profile_data[profile_name]):
            add(skill_record(path))

    for domain in domains or []:
        domain_norm = domain.strip()
        if domain_norm == "medical-knowledge":
            domain_norm = "medicine-clinical"
        matched = [
            record
            for record in records
            if record.get("domain") == domain_norm
            or record.get("scope") == domain_norm
        ]
        if not matched:
            raise SystemExit(f"unknown domain selector: {domain}")
        for record in matched:
            add(record)

    for category in categories or []:
        category_norm = category.strip().strip("/")
        matched = [
            record
            for record in records
            if record.get("category") == category_norm
            or "/".join(str(record.get("path", "")).split("/")[1:-1]) == category_norm
            or category_norm in record.get("selectors", [])
        ]
        if not matched:
            raise SystemExit(f"unknown category selector: {category}")
        for record in matched:
            add(record)

    selector_map = records_by_selector(include_archive=include_archive)
    for selector in skills or []:
        key = selector.strip().strip("/")
        record = selector_map.get(key) or selector_map.get(f"skills/{key}")
        if not record:
            raise SystemExit(f"unknown skill selector: {selector}")
        add(record)

    return selected


def copy_or_link_skill(source_dir: Path, dest: Path, mode: str, dry_run: bool) -> str:
    if dry_run:
        return mode
    if dest.exists() or dest.is_symlink():
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        else:
            shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if mode == "copy":
        shutil.copytree(source_dir, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        return "copy"
    try:
        dest.symlink_to(source_dir, target_is_directory=True)
        return "symlink"
    except OSError as exc:
        shutil.copytree(source_dir, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        print(f"WARNING: symlink failed for {dest.name}; copied instead ({exc})")
        return "copy"


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
    categories = Counter(str(record.get("category") or "unknown") for record in records)
    domains = Counter(str(record.get("domain") or "unknown") for record in records)
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
        "domain_distribution": dict(domains),
        "category_distribution": dict(categories),
        "agents_block_chars": len(agents_text),
        "warnings": warnings,
    }
