#!/usr/bin/env python3
"""Build and validate the Codex App marketplace publication layer."""

from __future__ import annotations

import argparse
import filecmp
import json
import re
import shutil
import stat
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any

from skill_utils import ROOT, SKILLS_ROOT, read_frontmatter


CODEX_ROOT = ROOT / "plugins" / "codex"
PLUGIN_PAYLOAD_ROOT = CODEX_ROOT / "plugins"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
OLD_NESTED_MARKETPLACE_PATH = CODEX_ROOT / ".agents" / "plugins" / "marketplace.json"
CONFIG_PATH = ROOT / "scripts" / "codex_marketplace_config.json"
REPOSITORY_URL = "https://github.com/YuukiAS/AI_Skills_Collection"
MAX_MARKETPLACE_PLUGINS = 9
MAX_ACTIVE_SKILLS = 30
WINDOWS_PATH_BUDGET = 140
AUTHOR = {
    "name": "YuukiAS",
    "email": "humc2013@gmail.com",
    "url": "https://github.com/YuukiAS",
}

INSTALL_POLICIES = {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}
AUTH_POLICIES = {"ON_INSTALL", "ON_USE"}
IGNORE_NAMES = {
    ".git",
    ".hg",
    ".svn",
    ".DS_Store",
    "TODO.md",
    "todo.md",
    "Thumbs.db",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".nox",
}
IGNORE_SUFFIXES = (".pyc", ".pyo", ".swp", ".swo", "~")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
ARTIFACT_ID_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,30}[a-z0-9])?$")
SECRET_RE = re.compile(r"\b[A-Z][A-Z0-9_]*(?:API_KEY|TOKEN)\b")
EXPLICIT_SECRET_NAMES = {
    "OPENROUTER_API_KEY",
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "GEMINI_API_KEY",
}
BOOL_METADATA_FIELDS = ("trusted", "requires_network", "writes_files", "executes_code")
SCOPE_ORDER = {"project": 0, "user": 1, "global": 2}


class BuildError(RuntimeError):
    """Raised for expected build or validation failures."""


def load_marketplace_config() -> dict[str, Any]:
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise BuildError(f"missing Codex marketplace config: {relative(CONFIG_PATH)}") from exc
    except json.JSONDecodeError as exc:
        raise BuildError(f"{relative(CONFIG_PATH)}: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise BuildError(f"{relative(CONFIG_PATH)}: config must be a JSON object")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        raise BuildError(f"{relative(CONFIG_PATH)}: plugins must be a non-empty list")
    return data


def marketplace_plugins(config: dict[str, Any]) -> list[dict[str, Any]]:
    plugins = config.get("plugins", [])
    if not isinstance(plugins, list):
        raise BuildError(f"{relative(CONFIG_PATH)}: plugins must be a list")
    return plugins


def plugin_names(config: dict[str, Any]) -> set[str]:
    return {str(plugin.get("name") or "") for plugin in marketplace_plugins(config)}


def json_dump(data: dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def compact_description(description: str) -> str:
    text = description.strip()
    prefixes = (
        "Project-local profile for ",
        "Global workflow protocol for complex Codex tasks: ",
        "Lightweight global/local profile for ",
        "Tiny global bootstrap profile for ",
    )
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix) :]
            break
    if text:
        return text[0].upper() + text[1:]
    return "Curated Codex skills from AI_Skills_Collection."


def truncate_prompt(prompt: str) -> str:
    return prompt if len(prompt) <= 128 else prompt[:125].rstrip() + "..."


def keywords_for_plugin(plugin_name: str) -> list[str]:
    parts = [part for part in plugin_name.split("-") if part != "codex"]
    return sorted(set(["codex", "skills", *parts]))


def plugin_version(plugin: dict[str, Any], context: str) -> str:
    version = plugin.get("version")
    if not isinstance(version, str) or not SEMVER_RE.match(version):
        raise BuildError(f"{context}: version must be a valid semantic version")
    return version


def build_marketplace_entry(plugin: dict[str, Any]) -> dict[str, Any]:
    plugin_name = str(plugin["name"])
    return {
        "name": plugin_name,
        "source": {
            "source": "local",
            "path": f"./plugins/codex/plugins/{plugin_name}",
        },
        "policy": {
            "installation": str(plugin.get("installation") or "AVAILABLE"),
            "authentication": "ON_INSTALL",
        },
        "category": str(plugin.get("category") or "Productivity"),
    }


def build_marketplace(config: dict[str, Any]) -> dict[str, Any]:
    plugins = marketplace_plugins(config)
    return {
        "name": str(config.get("name") or "yuukias-ai-skills"),
        "interface": {
            "displayName": str(config.get("displayName") or "YuukiAS AI Skills"),
        },
        "plugins": [build_marketplace_entry(plugin) for plugin in plugins],
    }


def build_plugin_json(plugin: dict[str, Any]) -> dict[str, Any]:
    plugin_name = str(plugin["name"])
    context = f"plugin {plugin_name}"
    category = str(plugin.get("category") or "Productivity")
    display_name = str(plugin.get("displayName") or plugin_name.replace("-", " ").title())
    short_description = compact_description(str(plugin.get("description") or "Curated Codex App skills."))
    long_description = (
        f"{short_description} This plugin is generated from the Codex App marketplace "
        "configuration and contains a self-contained skill snapshot."
    )
    return {
        "name": plugin_name,
        "version": plugin_version(plugin, context),
        "description": short_description,
        "author": AUTHOR,
        "homepage": REPOSITORY_URL,
        "repository": REPOSITORY_URL,
        "keywords": keywords_for_plugin(plugin_name),
        "skills": "./skills/",
        "interface": {
            "displayName": display_name,
            "shortDescription": short_description,
            "longDescription": long_description,
            "developerName": "YuukiAS",
            "category": category,
            "capabilities": ["Skills"],
            "websiteURL": REPOSITORY_URL,
            "defaultPrompt": [truncate_prompt(str(prompt)) for prompt in plugin.get("defaultPrompt", [])[:3]],
            "brandColor": "#2563EB",
        },
    }


def ignore_copy_names(_directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()
    for name in names:
        if name in IGNORE_NAMES or name.endswith(IGNORE_SUFFIXES):
            ignored.add(name)
    return ignored


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def generated_git_path(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return relative(path)


def generated_path_context(root: Path, path: Path, config: dict[str, Any]) -> dict[str, str]:
    context = {"plugin": "", "active_skill": "", "source_skill": ""}
    try:
        rel_parts = path.relative_to(root).parts
    except ValueError:
        return context
    if (
        len(rel_parts) < 6
        or rel_parts[0] != "plugins"
        or rel_parts[1] != "codex"
        or rel_parts[2] != "plugins"
        or rel_parts[4] != "skills"
    ):
        return context
    plugin_name = rel_parts[3]
    active_artifact = rel_parts[5]
    context["plugin"] = plugin_name
    plugin = next((item for item in marketplace_plugins(config) if item.get("name") == plugin_name), None)
    if not plugin:
        return context
    for entry in plugin_skill_entries(plugin):
        entry_context = f"plugin {plugin_name}"
        entry_type = entry.get("type")
        if entry_type == "copy":
            source = str(entry.get("source") or "")
            source_dir = resolve_skill_dir(source, entry_context)
            artifact_id = copy_entry_artifact_id(entry, source_dir, entry_context)
            if artifact_id == active_artifact:
                meta, _ = read_frontmatter(source_dir / "SKILL.md")
                context["active_skill"] = str(meta.get("name") or source_dir.name)
                context["source_skill"] = source
                return context
        elif entry_type == "aggregate":
            artifact_id = aggregate_entry_artifact_id(entry, entry_context)
            if artifact_id != active_artifact:
                continue
            active_name = str(entry.get("name") or "")
            context["active_skill"] = active_name
            if len(rel_parts) >= 8 and rel_parts[6] == "_src":
                source_id = rel_parts[7]
                sources = normalize_source_items(entry.get("source_skills") or [], f"{entry_context}:{active_name}")
                for source in sources:
                    if source["artifact_id"] == source_id:
                        context["source_skill"] = str(source["source"])
                        return context
            return context
    return context


def publication_paths(root: Path) -> list[Path]:
    return [
        root / ".agents" / "plugins" / "marketplace.json",
        root / "plugins" / "codex" / "plugins",
    ]


def iter_publication_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    marketplace = root / ".agents" / "plugins" / "marketplace.json"
    if marketplace.exists():
        paths.append(marketplace)
    payload_root = root / "plugins" / "codex" / "plugins"
    if payload_root.exists():
        paths.append(payload_root)
        paths.extend(sorted(payload_root.rglob("*")))
    old_marketplace = root / "plugins" / "codex" / ".agents" / "plugins" / "marketplace.json"
    if old_marketplace.exists():
        paths.append(old_marketplace)
    return paths


def path_report(root: Path = ROOT, limit: int = 20) -> dict[str, Any]:
    config = load_marketplace_config()
    files: list[dict[str, Any]] = []
    dirs: list[dict[str, Any]] = []
    for path in iter_publication_paths(root):
        rel = generated_git_path(root, path)
        row = {
            "path": rel,
            "length": len(rel),
            "kind": "dir" if path.is_dir() else "file",
            "over_budget": len(rel) > WINDOWS_PATH_BUDGET,
            **generated_path_context(root, path, config),
        }
        if path.is_dir():
            dirs.append(row)
        elif path.is_file() or path.is_symlink():
            files.append(row)
    files_sorted = sorted(files, key=lambda row: (-int(row["length"]), str(row["path"])))
    dirs_sorted = sorted(dirs, key=lambda row: (-int(row["length"]), str(row["path"])))
    over_budget = [row for row in files_sorted + dirs_sorted if row["over_budget"]]
    return {
        "budget": WINDOWS_PATH_BUDGET,
        "top_files": files_sorted[:limit],
        "top_dirs": dirs_sorted[:limit],
        "over_budget_count": len(over_budget),
        "over_budget": over_budget[:limit],
        "max_file_length": int(files_sorted[0]["length"]) if files_sorted else 0,
        "max_dir_length": int(dirs_sorted[0]["length"]) if dirs_sorted else 0,
    }


def path_budget_errors(root: Path = ROOT) -> list[str]:
    report = path_report(root)
    errors: list[str] = []
    for row in report["over_budget"]:
        errors.append(
            f"{row['path']}: path length {row['length']} exceeds Windows budget {WINDOWS_PATH_BUDGET} "
            f"(plugin={row['plugin'] or '-'}, active_skill={row['active_skill'] or '-'}, source_skill={row['source_skill'] or '-'})"
        )
    if report["over_budget_count"] > len(report["over_budget"]):
        errors.append(
            f"{report['over_budget_count'] - len(report['over_budget'])} additional generated paths exceed Windows budget {WINDOWS_PATH_BUDGET}"
        )
    return errors


def assert_path_budget(root: Path = ROOT) -> None:
    errors = path_budget_errors(root)
    if errors:
        raise BuildError("generated Codex marketplace paths exceed Windows budget:\n  " + "\n  ".join(errors))


def assert_no_symlink(path: Path, errors: list[str]) -> None:
    if path.is_symlink():
        errors.append(f"{relative(path)}: symlinks are not allowed in the Codex marketplace layer")
        return
    if not path.exists():
        return
    for item in path.rglob("*"):
        if item.is_symlink():
            errors.append(f"{relative(item)}: symlinks are not allowed in the Codex marketplace layer")


def source_contains_symlink(source_dir: Path) -> bool:
    return source_dir.is_symlink() or any(item.is_symlink() for item in source_dir.rglob("*"))


def read_required_skill_metadata(skill_dir: Path, context: str) -> dict[str, Any]:
    skill_file = skill_dir / "SKILL.md"
    meta, _ = read_frontmatter(skill_file)
    if not meta:
        raise BuildError(f"{context}: {relative(skill_file)} is missing YAML frontmatter")
    name = meta.get("name")
    if not isinstance(name, str) or not name:
        raise BuildError(f"{context}: {relative(skill_file)} must declare a non-empty frontmatter name")
    for field in BOOL_METADATA_FIELDS:
        if field not in meta or not isinstance(meta.get(field), bool):
            raise BuildError(f"{context}: {relative(skill_file)} {field} must be an explicit boolean")
    secrets = meta.get("secrets_needed", [])
    if secrets in (None, "", {}):
        secrets = []
    if not isinstance(secrets, list) or any(not isinstance(item, str) for item in secrets):
        raise BuildError(f"{context}: {relative(skill_file)} secrets_needed must be a list of strings")
    meta["secrets_needed"] = secrets
    scope = meta.get("recommended_scope")
    if scope not in SCOPE_ORDER:
        raise BuildError(
            f"{context}: {relative(skill_file)} recommended_scope must be one of {', '.join(SCOPE_ORDER)}"
        )
    audit_source_secret_declarations(skill_dir, meta, context)
    assert_no_source_todo(skill_dir, context)
    return meta


def iter_source_text_files(skill_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in IGNORE_NAMES for part in path.relative_to(skill_dir).parts):
            continue
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        paths.append(path)
    return paths


def assert_no_source_todo(skill_dir: Path, context: str) -> None:
    matches: list[str] = []
    for path in iter_source_text_files(skill_dir):
        if "[TODO:" in path.read_text(encoding="utf-8", errors="replace"):
            matches.append(relative(path))
    if matches:
        raise BuildError(f"{context}: source contains [TODO: placeholders: {', '.join(matches)}")


def audit_source_secret_declarations(skill_dir: Path, meta: dict[str, Any], context: str) -> None:
    declared = set(meta.get("secrets_needed") or [])
    found: set[str] = set()
    for path in iter_source_text_files(skill_dir):
        text = path.read_text(encoding="utf-8", errors="replace")
        found.update(SECRET_RE.findall(text))
    found.update(secret for secret in EXPLICIT_SECRET_NAMES if secret in found)
    missing = sorted(found - declared)
    if missing:
        raise BuildError(
            f"{context}: {relative(skill_dir / 'SKILL.md')} references secrets not declared in frontmatter: "
            + ", ".join(missing)
        )


def aggregate_metadata(source_dirs: list[Path], context: str) -> dict[str, Any]:
    metas = [read_required_skill_metadata(source_dir, context) for source_dir in source_dirs]
    return {
        "trusted": all(meta["trusted"] is True for meta in metas),
        "requires_network": any(meta["requires_network"] is True for meta in metas),
        "writes_files": any(meta["writes_files"] is True for meta in metas),
        "executes_code": any(meta["executes_code"] is True for meta in metas),
        "secrets_needed": sorted({secret for meta in metas for secret in meta.get("secrets_needed", [])}),
        "recommended_scope": min((str(meta["recommended_scope"]) for meta in metas), key=lambda item: SCOPE_ORDER[item]),
        "source_skills": [relative(source_dir) for source_dir in source_dirs],
    }


def resolve_skill_dir(item: str, context: str) -> Path:
    skill_dir = (ROOT / item).resolve()
    if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").exists():
        raise BuildError(f"{context}: missing skill directory {item}")
    try:
        skill_dir.relative_to(SKILLS_ROOT.resolve())
    except ValueError as exc:
        raise BuildError(f"{context}: skill path is outside skills/: {item}") from exc
    if source_contains_symlink(skill_dir):
        raise BuildError(f"{context}: skill source contains a symlink: {item}")
    return skill_dir


def skill_entry_name(entry: dict[str, Any]) -> str:
    entry_type = entry.get("type")
    if entry_type == "copy":
        source_dir = resolve_skill_dir(str(entry.get("source") or ""), "copy entry")
        meta = read_required_skill_metadata(source_dir, "copy entry")
        return str(meta["name"])
    if entry_type == "aggregate":
        return str(entry.get("name") or "")
    raise BuildError(f"unknown skill entry type: {entry_type}")


def plugin_skill_entries(plugin: dict[str, Any]) -> list[dict[str, Any]]:
    entries = plugin.get("skills")
    if not isinstance(entries, list) or not entries:
        raise BuildError(f"plugin {plugin.get('name')}: skills must be a non-empty list")
    return entries


def validate_artifact_id(value: str, context: str) -> str:
    if not ARTIFACT_ID_RE.match(value):
        raise BuildError(f"{context}: artifact_id must be lowercase kebab-case and <=32 characters")
    return value


def artifact_id_from_name(name: str, context: str) -> str:
    candidate = re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-")
    candidate = re.sub(r"-+", "-", candidate)
    if not candidate:
        raise BuildError(f"{context}: cannot derive artifact_id from empty name")
    if len(candidate) > 32:
        candidate = candidate[:32].rstrip("-")
    return validate_artifact_id(candidate, context)


def copy_entry_artifact_id(entry: dict[str, Any], source_dir: Path, context: str) -> str:
    explicit = entry.get("artifact_id")
    if explicit:
        return validate_artifact_id(str(explicit), context)
    meta = read_required_skill_metadata(source_dir, context)
    return artifact_id_from_name(str(meta.get("name") or source_dir.name), context)


def aggregate_entry_artifact_id(entry: dict[str, Any], context: str) -> str:
    explicit = entry.get("artifact_id")
    if explicit:
        return validate_artifact_id(str(explicit), context)
    return artifact_id_from_name(str(entry.get("name") or ""), context)


def source_item_source(item: Any, context: str) -> str:
    if isinstance(item, str):
        return item
    if isinstance(item, dict) and isinstance(item.get("source"), str):
        return str(item["source"])
    raise BuildError(f"{context}: source_skills entries must be strings or objects with source")


def source_item_artifact_id(item: Any, source_dir: Path, context: str) -> str:
    if isinstance(item, dict) and item.get("artifact_id"):
        return validate_artifact_id(str(item["artifact_id"]), context)
    meta = read_required_skill_metadata(source_dir, context)
    return artifact_id_from_name(str(meta.get("name") or source_dir.name), context)


def normalize_source_items(source_items: list[Any], context: str) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    seen: dict[str, str] = {}
    for item in source_items:
        source = source_item_source(item, context)
        source_dir = resolve_skill_dir(source, context)
        artifact_id = source_item_artifact_id(item, source_dir, context)
        if artifact_id in seen:
            raise BuildError(
                f"{context}: duplicate source artifact_id {artifact_id}: {seen[artifact_id]} and {source}"
            )
        seen[artifact_id] = source
        normalized.append({"source": source, "source_dir": source_dir, "artifact_id": artifact_id})
    return normalized


def artifact_dirs_for_plugin(plugin: dict[str, Any], context: str) -> dict[str, str]:
    used: dict[str, str] = {}
    result: dict[str, str] = {}
    for entry in plugin_skill_entries(plugin):
        entry_type = entry.get("type")
        if entry_type == "copy":
            source = str(entry.get("source") or "")
            source_dir = resolve_skill_dir(source, context)
            artifact_id = copy_entry_artifact_id(entry, source_dir, context)
            label = source
        elif entry_type == "aggregate":
            artifact_id = aggregate_entry_artifact_id(entry, context)
            label = str(entry.get("name") or "")
        else:
            raise BuildError(f"{context}: unknown skill entry type {entry_type}")
        if artifact_id in used:
            raise BuildError(f"{context}: duplicate artifact_id {artifact_id}: {used[artifact_id]} and {label}")
        used[artifact_id] = label
        result[label] = artifact_id
    return result


def yaml_list(name: str, items: list[str]) -> list[str]:
    if not items:
        return [f"{name}:"]
    return [f"{name}:"] + [f"  - {item}" for item in items]


def aggregate_skill_markdown(entry: dict[str, Any], sources: list[dict[str, Any]], metadata: dict[str, Any]) -> str:
    name = str(entry["name"])
    description = str(entry["description"])
    lines = [
        "---",
        f"name: {name}",
        f"description: {description}",
        "status: active",
        "provenance: generated",
        f"trusted: {str(metadata['trusted']).lower()}",
        f"requires_network: {str(metadata['requires_network']).lower()}",
        f"writes_files: {str(metadata['writes_files']).lower()}",
        f"executes_code: {str(metadata['executes_code']).lower()}",
    ]
    lines.extend(yaml_list("secrets_needed", metadata["secrets_needed"]))
    lines.append("last_reviewed: 2026-07-10")
    lines.append("profile_tags:")
    lines.append(f"recommended_scope: {metadata['recommended_scope']}")
    lines.extend(yaml_list("source_skills", metadata["source_skills"]))
    lines.extend(
        [
            "---",
            "",
            f"# {name}",
            "",
            "## Trigger Boundary",
            "",
            description,
            "",
            "Use this aggregate Codex App skill when the task matches one of the source workflows below.",
            "",
            "## Source Workflows",
            "",
        ]
    )
    for source in sources:
        source_dir = source["source_dir"]
        meta, _ = read_frontmatter(source_dir / "SKILL.md")
        source_name = str(meta.get("name") or source_dir.name)
        source_desc = str(meta.get("description") or "").strip()
        ref = f"_src/{source['artifact_id']}/source.md"
        if source_desc:
            lines.append(f"- `{source_name}`: {source_desc} Reference: `{ref}`")
        else:
            lines.append(f"- `{source_name}`. Reference: `{ref}`")
    lines.extend(
        [
            "",
            "## Workflow",
            "",
            "1. Choose the source workflow whose trigger boundary best matches the user request.",
            "2. Read that source workflow's `source.md` before acting.",
            "3. Load only the needed files under that workflow's copied references, scripts, assets, or evals.",
            "4. Follow the source workflow unless the current project gives stricter instructions.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def rename_nested_skill_files(reference_root: Path) -> None:
    for skill_file in sorted(reference_root.rglob("SKILL.md")):
        target = skill_file.with_name("source.md")
        if target.exists():
            raise BuildError(f"{relative(target)} already exists while renaming nested SKILL.md")
        skill_file.rename(target)


def copy_source_tree(source_dir: Path, dest: Path) -> None:
    shutil.copytree(source_dir, dest, ignore=ignore_copy_names, copy_function=shutil.copy2)


def generate_copy_skill(entry: dict[str, Any], skills_dir: Path, context: str) -> int:
    source_dir = resolve_skill_dir(str(entry.get("source") or ""), context)
    read_required_skill_metadata(source_dir, context)
    copy_source_tree(source_dir, skills_dir / copy_entry_artifact_id(entry, source_dir, context))
    return 1


def generate_aggregate_skill(entry: dict[str, Any], skills_dir: Path, context: str) -> tuple[int, int]:
    name = str(entry.get("name") or "")
    description = str(entry.get("description") or "")
    source_items = entry.get("source_skills")
    if not name or not re.match(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", name):
        raise BuildError(f"{context}: aggregate skill name must be lowercase kebab-case")
    if not description:
        raise BuildError(f"{context}: aggregate skill {name} needs a description")
    if not isinstance(source_items, list) or not source_items:
        raise BuildError(f"{context}: aggregate skill {name} needs source_skills")

    artifact_id = aggregate_entry_artifact_id(entry, context)
    aggregate_dir = skills_dir / artifact_id
    aggregate_dir.mkdir(parents=True, exist_ok=True)
    sources = normalize_source_items(source_items, f"{context}:{name}")
    source_dirs = [source["source_dir"] for source in sources]
    metadata = aggregate_metadata(source_dirs, f"{context}:{name}")
    (aggregate_dir / "SKILL.md").write_text(aggregate_skill_markdown(entry, sources, metadata), encoding="utf-8")
    for source in sources:
        source_dir = source["source_dir"]
        dest = aggregate_dir / "_src" / source["artifact_id"]
        copy_source_tree(source_dir, dest)
        rename_nested_skill_files(dest)
    return 1, len(source_dirs)


def skill_entry_generated_dir(entry: dict[str, Any], context: str) -> str:
    entry_type = entry.get("type")
    if entry_type == "copy":
        source_dir = resolve_skill_dir(str(entry.get("source") or ""), context)
        return copy_entry_artifact_id(entry, source_dir, context)
    if entry_type == "aggregate":
        return aggregate_entry_artifact_id(entry, context)
    raise BuildError(f"{context}: unknown skill entry type {entry_type}")


def active_skill_names(plugin: dict[str, Any]) -> list[str]:
    names: list[str] = []
    seen: set[str] = set()
    for entry in plugin_skill_entries(plugin):
        name = skill_entry_name(entry)
        if not name:
            raise BuildError(f"plugin {plugin.get('name')}: active skill name cannot be empty")
        if name in seen:
            raise BuildError(f"plugin {plugin.get('name')}: duplicate active skill {name}")
        seen.add(name)
        names.append(name)
    return names


def validate_config(config: dict[str, Any]) -> None:
    plugins = marketplace_plugins(config)
    plugin_seen: set[str] = set()
    active_seen: dict[str, list[tuple[str, str]]] = defaultdict(list)
    if len(plugins) > MAX_MARKETPLACE_PLUGINS:
        raise BuildError(f"Codex marketplace has {len(plugins)} plugins; maximum is {MAX_MARKETPLACE_PLUGINS}")
    for plugin in plugins:
        plugin_name = plugin.get("name")
        if not isinstance(plugin_name, str) or not plugin_name:
            raise BuildError(f"{relative(CONFIG_PATH)}: every plugin needs a non-empty string name")
        if plugin_name in plugin_seen:
            raise BuildError(f"{relative(CONFIG_PATH)}: duplicate plugin name {plugin_name}")
        plugin_seen.add(plugin_name)
        plugin_version(plugin, f"plugin {plugin_name}")
        artifact_dirs_for_plugin(plugin, f"plugin {plugin_name}")
        for entry in plugin_skill_entries(plugin):
            active_name = skill_entry_name(entry)
            if entry.get("type") == "copy":
                source_path = str(entry.get("source") or "")
            else:
                source_path = ", ".join(str(item) for item in entry.get("source_skills", []))
            active_seen[active_name].append((plugin_name, source_path))
    duplicates = {name: rows for name, rows in active_seen.items() if len(rows) > 1}
    if duplicates:
        parts: list[str] = []
        for name, rows in sorted(duplicates.items()):
            details = "; ".join(f"{plugin}: {source}" for plugin, source in rows)
            parts.append(f"{name} -> {details}")
        raise BuildError("duplicate marketplace active skill names: " + " | ".join(parts))
    if len(active_seen) > MAX_ACTIVE_SKILLS:
        raise BuildError(f"Codex marketplace has {len(active_seen)} active skills; maximum is {MAX_ACTIVE_SKILLS}")


def generate_layer(target_root: Path) -> dict[str, Any]:
    config = load_marketplace_config()
    plugins = marketplace_plugins(config)
    validate_config(config)
    marketplace_path = target_root / ".agents" / "plugins" / "marketplace.json"
    plugin_payload_root = target_root / "plugins" / "codex" / "plugins"
    old_nested_agents = target_root / "plugins" / "codex" / ".agents"

    if plugin_payload_root.exists():
        shutil.rmtree(plugin_payload_root)
    if old_nested_agents.exists():
        shutil.rmtree(old_nested_agents)
    marketplace_path.parent.mkdir(parents=True, exist_ok=True)
    plugin_payload_root.mkdir(parents=True, exist_ok=True)

    active_skill_count = 0
    source_skill_snapshot_count = 0
    for plugin in plugins:
        plugin_name = str(plugin["name"])
        plugin_root = plugin_payload_root / plugin_name
        manifest_dir = plugin_root / ".codex-plugin"
        skills_dir = plugin_root / "skills"
        manifest_dir.mkdir(parents=True, exist_ok=True)
        skills_dir.mkdir(parents=True, exist_ok=True)

        (manifest_dir / "plugin.json").write_text(json_dump(build_plugin_json(plugin)), encoding="utf-8")
        for entry in plugin_skill_entries(plugin):
            context = f"plugin {plugin_name}"
            if entry.get("type") == "copy":
                active_skill_count += generate_copy_skill(entry, skills_dir, context)
                source_skill_snapshot_count += 1
            elif entry.get("type") == "aggregate":
                active_delta, source_delta = generate_aggregate_skill(entry, skills_dir, context)
                active_skill_count += active_delta
                source_skill_snapshot_count += source_delta
            else:
                raise BuildError(f"{context}: unknown skill entry type {entry.get('type')}")
    if active_skill_count > MAX_ACTIVE_SKILLS:
        raise BuildError(f"Codex marketplace has {active_skill_count} active skills; maximum is {MAX_ACTIVE_SKILLS}")

    marketplace = build_marketplace(config)
    marketplace_path.write_text(json_dump(marketplace), encoding="utf-8")
    assert_path_budget(target_root)
    return {
        "plugin_count": len(plugins),
        "active_skill_count": active_skill_count,
        "source_skill_snapshot_count": source_skill_snapshot_count,
        "marketplace_path": relative(marketplace_path),
        "plugin_payload_path": relative(plugin_payload_root),
        "errors": [],
        "warnings": [],
    }


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{relative(path)}: file does not exist")
    except json.JSONDecodeError as exc:
        errors.append(f"{relative(path)}: invalid JSON: {exc}")
    return None


def validate_plugin_json(plugin_dir: Path, plugin: dict[str, Any], errors: list[str], warnings: list[str]) -> int:
    plugin_name = str(plugin["name"])
    plugin_json_path = plugin_dir / ".codex-plugin" / "plugin.json"
    payload = load_json(plugin_json_path, errors)
    if not isinstance(payload, dict):
        return 0

    if "[TODO:" in plugin_json_path.read_text(encoding="utf-8", errors="replace"):
        errors.append(f"{relative(plugin_json_path)}: must not contain [TODO: placeholders")
    if payload.get("name") != plugin_name:
        errors.append(f"{relative(plugin_json_path)}: name must equal plugin directory name {plugin_name}")
    expected_version = str(plugin.get("version") or "")
    if payload.get("version") != expected_version:
        errors.append(f"{relative(plugin_json_path)}: version must be {expected_version}")
    elif not SEMVER_RE.match(expected_version):
        errors.append(f"{relative(plugin_json_path)}: version must be a valid semantic version")
    if payload.get("skills") != "./skills/":
        errors.append(f"{relative(plugin_json_path)}: skills must be ./skills/")
    if payload.get("repository") != REPOSITORY_URL:
        errors.append(f"{relative(plugin_json_path)}: repository must be {REPOSITORY_URL}")
    if payload.get("homepage") != REPOSITORY_URL:
        errors.append(f"{relative(plugin_json_path)}: homepage must be {REPOSITORY_URL}")
    if payload.get("author") != AUTHOR:
        errors.append(f"{relative(plugin_json_path)}: author must match YuukiAS publisher metadata")

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        errors.append(f"{relative(plugin_json_path)}: interface must be an object")
    else:
        prompts = interface.get("defaultPrompt", [])
        if not isinstance(prompts, list):
            errors.append(f"{relative(plugin_json_path)}: interface.defaultPrompt must be a list")
        elif len(prompts) > 3:
            errors.append(f"{relative(plugin_json_path)}: interface.defaultPrompt must have at most 3 entries")
        else:
            for index, prompt in enumerate(prompts):
                if not isinstance(prompt, str):
                    errors.append(f"{relative(plugin_json_path)}: defaultPrompt[{index}] must be a string")
                elif len(prompt) > 128:
                    errors.append(f"{relative(plugin_json_path)}: defaultPrompt[{index}] exceeds 128 characters")

    skills_dir = plugin_dir / "skills"
    expected_dirs = [skill_entry_generated_dir(entry, f"plugin {plugin_name}") for entry in plugin_skill_entries(plugin)]
    expected_skill_dirs = [skills_dir / name for name in expected_dirs]
    found_skill_md = sorted(skills_dir.glob("*/SKILL.md")) if skills_dir.exists() else []
    if not found_skill_md:
        errors.append(f"{relative(skills_dir)}: each plugin must contain at least one copied SKILL.md")
    for expected_dir in expected_skill_dirs:
        if not (expected_dir / "SKILL.md").exists():
            errors.append(f"{relative(expected_dir)}: expected copied skill with SKILL.md")
    actual_dirs = {path.parent.name for path in found_skill_md}
    extras = sorted(actual_dirs - set(expected_dirs))
    if extras:
        warnings.append(f"{relative(skills_dir)}: extra active skill directories not listed in marketplace config: {', '.join(extras)}")
    if skills_dir.exists():
        for nested in sorted(skills_dir.rglob("SKILL.md")):
            rel_parts = nested.relative_to(skills_dir).parts
            if len(rel_parts) != 2:
                errors.append(f"{relative(nested)}: nested SKILL.md files are not allowed in the Codex marketplace layer")
    for entry in plugin_skill_entries(plugin):
        if entry.get("type") != "aggregate":
            continue
        active_dir = skills_dir / aggregate_entry_artifact_id(entry, f"plugin {plugin_name}")
        active_skill = active_dir / "SKILL.md"
        text = active_skill.read_text(encoding="utf-8", errors="replace") if active_skill.exists() else ""
        active_name = str(entry.get("name") or "")
        sources = normalize_source_items(entry.get("source_skills") or [], f"plugin {plugin_name}:{active_name}")
        seen_sources: set[str] = set()
        for source in sources:
            source_path = str(source["source"])
            if source_path in seen_sources:
                errors.append(f"{relative(active_skill)}: source snapshot copied more than once: {source_path}")
            seen_sources.add(source_path)
            ref = f"_src/{source['artifact_id']}/source.md"
            if ref not in text:
                errors.append(f"{relative(active_skill)}: missing source workflow reference {ref}")
            if not (active_dir / ref).exists():
                errors.append(f"{relative(active_dir / ref)}: aggregate source workflow file is missing")
    return len(found_skill_md)


def resolve_marketplace_source_path(root: Path, source: Any, plugin_name: str, errors: list[str]) -> Path | None:
    manifest_label = relative(root / ".agents" / "plugins" / "marketplace.json")
    if not isinstance(source, dict):
        errors.append(f"{manifest_label}: {plugin_name} source must be an object")
        return None
    if source.get("source") != "local":
        errors.append(f"{manifest_label}: {plugin_name} source.source must be local")
    source_path = source.get("path")
    if not isinstance(source_path, str):
        errors.append(f"{manifest_label}: {plugin_name} source.path must be a string")
        return None
    if not source_path.startswith("./"):
        errors.append(f"{manifest_label}: {plugin_name} source.path must start with ./")
        return None
    try:
        plugin_dir = (root / source_path[2:]).resolve()
        plugin_dir.relative_to(root.resolve())
    except ValueError:
        errors.append(f"{manifest_label}: {plugin_name} source.path escapes marketplace root: {source_path}")
        return None
    return plugin_dir


def validate_layer(root: Path = ROOT) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    config = load_marketplace_config()
    validate_config(config)
    configured_plugins = marketplace_plugins(config)
    plugin_by_name = {str(plugin["name"]): plugin for plugin in configured_plugins}
    marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    plugin_payload_root = root / "plugins" / "codex" / "plugins"
    old_marketplace = root / "plugins" / "codex" / ".agents" / "plugins" / "marketplace.json"

    assert_no_symlink(plugin_payload_root, errors)
    if marketplace_path.is_symlink():
        errors.append(f"{relative(marketplace_path)}: symlinks are not allowed in the Codex marketplace layer")
    if old_marketplace.exists():
        errors.append(f"{relative(old_marketplace)}: old nested marketplace manifest must not exist")
    marketplace = load_json(marketplace_path, errors)
    active_skill_count = 0
    plugin_count = 0
    generated_active_names: dict[str, list[tuple[str, str]]] = defaultdict(list)

    if isinstance(marketplace, dict):
        if marketplace.get("name") != config.get("name"):
            errors.append(f"{relative(marketplace_path)}: name must be {config.get('name')}")
        interface = marketplace.get("interface")
        if not isinstance(interface, dict) or interface.get("displayName") != config.get("displayName"):
            errors.append(
                f"{relative(marketplace_path)}: interface.displayName must be {config.get('displayName')}"
            )
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list):
            errors.append(f"{relative(marketplace_path)}: plugins must be a list")
            plugins = []
        plugin_count = len(plugins)
        if plugin_count != len(configured_plugins):
            errors.append(
                f"{relative(marketplace_path)}: expected {len(configured_plugins)} plugin entries, found {plugin_count}"
            )
        if plugin_count > MAX_MARKETPLACE_PLUGINS:
            errors.append(
                f"{relative(marketplace_path)}: expected at most {MAX_MARKETPLACE_PLUGINS} plugin entries, found {plugin_count}"
            )
        seen_names: set[str] = set()
        for entry in plugins:
            if not isinstance(entry, dict):
                errors.append(f"{relative(marketplace_path)}: every plugins[] entry must be an object")
                continue
            name = entry.get("name")
            if not isinstance(name, str):
                errors.append(f"{relative(marketplace_path)}: every plugins[] entry needs a string name")
                continue
            seen_names.add(name)
            if name not in plugin_by_name:
                errors.append(f"{relative(marketplace_path)}: unknown configured plugin {name}")
                continue
            configured = plugin_by_name[name]
            expected_source = {"source": "local", "path": f"./plugins/codex/plugins/{name}"}
            source = entry.get("source")
            if source != expected_source:
                errors.append(f"{relative(marketplace_path)}: {name} source must be {expected_source}")
            plugin_dir = resolve_marketplace_source_path(root, source, name, errors)
            policy = entry.get("policy")
            if not isinstance(policy, dict):
                errors.append(f"{relative(marketplace_path)}: {name} policy must be an object")
            else:
                expected_install = str(configured.get("installation") or "AVAILABLE")
                if policy.get("installation") != expected_install:
                    errors.append(f"{relative(marketplace_path)}: {name} installation must be {expected_install}")
                if policy.get("authentication") != "ON_INSTALL":
                    errors.append(f"{relative(marketplace_path)}: {name} authentication must be ON_INSTALL")
                if policy.get("installation") not in INSTALL_POLICIES:
                    errors.append(f"{relative(marketplace_path)}: {name} has invalid installation policy")
                if policy.get("authentication") not in AUTH_POLICIES:
                    errors.append(f"{relative(marketplace_path)}: {name} has invalid authentication policy")
            if entry.get("category") != str(configured.get("category") or "Productivity"):
                errors.append(f"{relative(marketplace_path)}: {name} category is incorrect")
            if plugin_dir is None:
                continue
            if not plugin_dir.is_dir():
                errors.append(f"{relative(plugin_dir)}: marketplace source.path does not resolve to a real plugin directory")
            elif plugin_dir.name != name:
                errors.append(f"{relative(plugin_dir)}: marketplace source.path directory name must match plugin name {name}")
            else:
                active_skill_count += validate_plugin_json(plugin_dir, plugin_by_name[name], errors, warnings)
                for skill_file in sorted((plugin_dir / "skills").glob("*/SKILL.md")):
                    meta, _ = read_frontmatter(skill_file)
                    active_name = str(meta.get("name") or "")
                    if active_name:
                        generated_active_names[active_name].append((name, relative(skill_file)))
        missing_names = sorted(set(plugin_by_name) - seen_names)
        for name in missing_names:
            errors.append(f"{relative(marketplace_path)}: missing configured plugin {name}")
    if active_skill_count > MAX_ACTIVE_SKILLS:
        errors.append(f"plugins/codex contains {active_skill_count} active skills; maximum is {MAX_ACTIVE_SKILLS}")

    todo_matches = []
    if plugin_payload_root.exists():
        for path in plugin_payload_root.rglob("*"):
            if path.is_file() and not path.is_symlink():
                try:
                    if "[TODO:" in path.read_text(encoding="utf-8", errors="ignore"):
                        todo_matches.append(relative(path))
                except OSError:
                    pass
    if todo_matches:
        errors.append("plugins/codex contains [TODO: placeholders: " + ", ".join(sorted(todo_matches)))

    errors.extend(path_budget_errors(root))

    duplicate_generated_names = {name: rows for name, rows in generated_active_names.items() if len(rows) > 1}
    for name, rows in sorted(duplicate_generated_names.items()):
        details = "; ".join(f"{plugin}: {path}" for plugin, path in rows)
        errors.append(f"duplicate generated active skill name {name}: {details}")

    return {
        "plugin_count": plugin_count,
        "active_skill_count": active_skill_count,
        "marketplace_path": relative(marketplace_path),
        "plugin_payload_path": relative(plugin_payload_root),
        "errors": errors,
        "warnings": warnings,
    }


def collect_files(root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for path in iter_publication_paths(root):
        if path.is_file() or path.is_symlink():
            files[path.relative_to(root).as_posix()] = path
    return files


def compare_layers(expected_root: Path, current_root: Path) -> list[str]:
    differences: list[str] = []
    expected_files = collect_files(expected_root)
    current_files = collect_files(current_root)
    for rel_path in sorted(set(expected_files) - set(current_files)):
        differences.append(f"missing: {rel_path}")
    for rel_path in sorted(set(current_files) - set(expected_files)):
        differences.append(f"extra: {rel_path}")
    for rel_path in sorted(set(expected_files) & set(current_files)):
        expected = expected_files[rel_path]
        current = current_files[rel_path]
        if expected.is_symlink() or current.is_symlink():
            differences.append(f"symlink differs: {rel_path}")
            continue
        if not filecmp.cmp(expected, current, shallow=False):
            differences.append(f"content differs: {rel_path}")
            continue
        expected_mode = stat.S_IMODE(expected.stat().st_mode)
        current_mode = stat.S_IMODE(current.stat().st_mode)
        if expected_mode != current_mode:
            differences.append(f"mode differs: {rel_path}")
    return differences


def check_layer() -> tuple[dict[str, Any], list[str]]:
    with tempfile.TemporaryDirectory(prefix="codex-marketplace-") as tmp:
        expected_root = Path(tmp) / "repo"
        summary = generate_layer(expected_root)
        summary["marketplace_path"] = relative(MARKETPLACE_PATH)
        summary["plugin_payload_path"] = relative(PLUGIN_PAYLOAD_ROOT)
        differences = compare_layers(expected_root, ROOT)
    if differences:
        summary["errors"] = [f"publication layer is not current ({len(differences)} differences)"]
    budget_errors = path_budget_errors(ROOT)
    if budget_errors:
        summary.setdefault("errors", []).extend(budget_errors)
    return summary, differences


def print_summary(summary: dict[str, Any], json_output: bool) -> None:
    if json_output:
        print(json_dump(summary), end="")
        return
    active = summary.get("active_skill_count", 0)
    snapshots = summary.get("source_skill_snapshot_count")
    snapshot_text = f" source_snapshots={snapshots}" if snapshots is not None else ""
    print(
        f"plugins={summary['plugin_count']} active_skills={active}{snapshot_text} "
        f"marketplace={summary['marketplace_path']} payload={summary.get('plugin_payload_path', relative(PLUGIN_PAYLOAD_ROOT))}"
    )
    for warning in summary.get("warnings", []):
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in summary.get("errors", []):
        print(f"ERROR: {error}", file=sys.stderr)


def print_path_report(report: dict[str, Any], json_output: bool) -> None:
    if json_output:
        print(json.dumps({"path_report": report}, ensure_ascii=False, indent=2) + "\n", end="")
        return
    print(f"Windows path budget: {report['budget']}")
    print(f"max_file_length={report['max_file_length']} max_dir_length={report['max_dir_length']} over_budget={report['over_budget_count']}")
    print("\nTop files:")
    for row in report["top_files"]:
        marker = " OVER" if row["over_budget"] else ""
        print(
            f"{row['length']:>3}{marker} {row['path']} "
            f"(plugin={row['plugin'] or '-'} active={row['active_skill'] or '-'} source={row['source_skill'] or '-'})"
        )
    print("\nTop directories:")
    for row in report["top_dirs"]:
        marker = " OVER" if row["over_budget"] else ""
        print(
            f"{row['length']:>3}{marker} {row['path']} "
            f"(plugin={row['plugin'] or '-'} active={row['active_skill'] or '-'} source={row['source_skill'] or '-'})"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the Codex marketplace manifest and plugin payload")
    parser.add_argument("--validate", action="store_true", help="Validate the current Codex marketplace publication")
    parser.add_argument("--check", action="store_true", help="Compare current publication files with a freshly generated publication")
    parser.add_argument("--path-report", action="store_true", help="Report longest generated paths and Windows budget status")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable summary")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    actions = [args.write, args.validate, args.check, args.path_report]
    if not any(actions):
        args.validate = True

    exit_code = 0
    summary: dict[str, Any] | None = None
    try:
        if args.write:
            summary = generate_layer(ROOT)
            if not args.json:
                print_summary(summary, False)
        if args.validate:
            summary = validate_layer(ROOT)
            if not args.json:
                print_summary(summary, False)
            if summary["errors"]:
                exit_code = 1
        if args.check:
            summary, differences = check_layer()
            if differences and not args.json:
                print("Codex marketplace publication layer is not current:", file=sys.stderr)
                for item in differences:
                    print(f"  {item}", file=sys.stderr)
            if not args.json:
                print_summary(summary, False)
            if differences or summary.get("errors"):
                exit_code = 1
        if args.path_report:
            report = path_report(ROOT)
            print_path_report(report, args.json)
            if report["over_budget_count"]:
                exit_code = 1
        if args.json:
            if args.path_report:
                return exit_code
            if summary is None:
                summary = validate_layer(ROOT)
            print_summary(summary, True)
    except BuildError as exc:
        summary = {
            "plugin_count": 0,
            "active_skill_count": 0,
            "source_skill_snapshot_count": 0,
            "marketplace_path": relative(MARKETPLACE_PATH),
            "plugin_payload_path": relative(PLUGIN_PAYLOAD_ROOT),
            "errors": [str(exc)],
            "warnings": [],
        }
        print_summary(summary, args.json)
        return 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
