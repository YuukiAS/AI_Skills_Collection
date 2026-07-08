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
from pathlib import Path
from typing import Any

from skill_utils import ROOT, SKILLS_ROOT, load_profiles, skill_flat_name


CODEX_ROOT = ROOT / "plugins" / "codex"
MARKETPLACE_PATH = CODEX_ROOT / ".agents" / "plugins" / "marketplace.json"
REPOSITORY_URL = "https://github.com/YuukiAS/AI_Skills_Collection"
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
TEXT_SUFFIXES = {
    "",
    ".cfg",
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".ts",
    ".txt",
    ".yaml",
    ".yml",
}

CATEGORY_BY_PROFILE = {
    "codex-core-global": "Developer Tools",
    "codex-workflow-core": "Developer Tools",
    "codex-skill-maintenance": "Developer Tools",
    "codex-webdev": "Web Development",
    "codex-research-writing": "Research",
    "codex-writing-style": "Research",
    "codex-bayesian-jsdm": "Research",
    "codex-cardiacnexus": "Research",
    "codex-bioinformatics-light": "Research",
}

DISPLAY_NAME_BY_PROFILE = {
    "codex-bayesian-jsdm": "Bayesian JSDM Toolkit",
    "codex-bioinformatics-light": "Bioinformatics Light Toolkit",
    "codex-cardiacnexus": "CardiacNexus Imaging Toolkit",
    "codex-core-global": "Core Skill Installer",
    "codex-research-writing": "Research Writing Toolkit",
    "codex-skill-maintenance": "Skill Maintenance Toolkit",
    "codex-webdev": "Web Development Toolkit",
    "codex-workflow-core": "Workflow Protocol Core",
    "codex-writing-style": "Writing Style and Fidelity",
}

PROMPTS_BY_PROFILE = {
    "codex-bayesian-jsdm": [
        "Help me build and diagnose a Bayesian model.",
        "Review this JSDM or HMSC workflow.",
        "Prepare theorem-heavy manuscript guidance.",
    ],
    "codex-bioinformatics-light": [
        "Plan a common bioinformatics analysis.",
        "Review this single-cell workflow.",
        "Help me choose the right omics tool.",
    ],
    "codex-cardiacnexus": [
        "Review this CardiacNexus pipeline change.",
        "Help with CMR image processing.",
        "Check this DICOM or NIfTI workflow.",
    ],
    "codex-core-global": [
        "Install project-local skills safely.",
        "Create or update a Codex skill.",
        "Set up this repo's skill profile.",
    ],
    "codex-research-writing": [
        "Revise this research manuscript.",
        "Plan a literature review.",
        "Check citations, figures, and PDFs.",
    ],
    "codex-skill-maintenance": [
        "Validate this skill repository change.",
        "Update registry and profile metadata.",
        "Review a new skill for packaging.",
    ],
    "codex-webdev": [
        "Build a responsive React interface.",
        "Audit this frontend with browser tests.",
        "Implement this Figma handoff.",
    ],
    "codex-workflow-core": [
        "Run a verified implementation workflow.",
        "Find the source of truth before editing.",
        "Check completion gates for this task.",
    ],
    "codex-writing-style": [
        "Make this scientific prose clearer.",
        "Polish this Chinese technical text.",
        "Render and check a CJK math PDF.",
    ],
}


class BuildError(RuntimeError):
    """Raised for expected build or validation failures."""


def json_dump(data: dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def load_profiles_sorted() -> list[dict[str, Any]]:
    profiles = load_profiles()
    return [profiles[name] for name in sorted(profiles)]


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


def default_prompts(profile_name: str, description: str) -> list[str]:
    prompts = PROMPTS_BY_PROFILE.get(profile_name)
    if prompts:
        return [truncate_prompt(prompt) for prompt in prompts[:3]]
    return [truncate_prompt(f"Use {DISPLAY_NAME_BY_PROFILE.get(profile_name, profile_name)} for {compact_description(description).lower()}")]


def keywords_for_profile(profile_name: str) -> list[str]:
    parts = [part for part in profile_name.split("-") if part != "codex"]
    return sorted(set(["codex", "skills", *parts]))


def category_for_profile(profile_name: str) -> str:
    return CATEGORY_BY_PROFILE.get(profile_name, "Productivity")


def build_marketplace_entry(profile_name: str) -> dict[str, Any]:
    return {
        "name": profile_name,
        "source": {
            "source": "local",
            "path": f"./plugins/{profile_name}",
        },
        "policy": {
            "installation": "INSTALLED_BY_DEFAULT" if profile_name == "codex-core-global" else "AVAILABLE",
            "authentication": "ON_INSTALL",
        },
        "category": category_for_profile(profile_name),
    }


def build_marketplace(profiles: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "name": "yuukias-ai-skills",
        "interface": {
            "displayName": "YuukiAS AI Skills",
        },
        "plugins": [build_marketplace_entry(str(profile["name"])) for profile in profiles],
    }


def build_plugin_json(profile: dict[str, Any]) -> dict[str, Any]:
    profile_name = str(profile["name"])
    category = category_for_profile(profile_name)
    display_name = DISPLAY_NAME_BY_PROFILE.get(profile_name) or profile_name.replace("-", " ").title()
    description = str(profile.get("description") or "")
    short_description = compact_description(description)
    long_description = (
        f"{short_description} This plugin is generated from the `{profile_name}` profile "
        "and contains copied skill snapshots for Codex App marketplace installation."
    )
    return {
        "name": profile_name,
        "version": "1.0.0",
        "description": short_description,
        "author": AUTHOR,
        "homepage": REPOSITORY_URL,
        "repository": REPOSITORY_URL,
        "keywords": keywords_for_profile(profile_name),
        "skills": "./skills/",
        "interface": {
            "displayName": display_name,
            "shortDescription": short_description,
            "longDescription": long_description,
            "developerName": "YuukiAS",
            "category": category,
            "capabilities": ["Skills"],
            "websiteURL": REPOSITORY_URL,
            "defaultPrompt": default_prompts(profile_name, description),
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


def sanitize_generated_snapshot(path: Path) -> None:
    for item in path.rglob("*"):
        if not item.is_file() or item.is_symlink() or item.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = item.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        replacements = {
            "[TODO:": "[example:",
            "placeholders": "example values",
            "placeholder": "example value",
            "Placeholders": "Example values",
            "Placeholder": "Example value",
        }
        if not any(old in text for old in replacements):
            continue
        for old, new in replacements.items():
            text = text.replace(old, new)
        item.write_text(text, encoding="utf-8")


def resolve_profile_skill_dirs(profile: dict[str, Any]) -> list[Path]:
    skill_dirs: list[Path] = []
    for item in profile.get("skills", []):
        skill_dir = (ROOT / str(item)).resolve()
        if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").exists():
            raise BuildError(f"profile {profile.get('name')}: missing skill directory {item}")
        try:
            skill_dir.relative_to(SKILLS_ROOT.resolve())
        except ValueError as exc:
            raise BuildError(f"profile {profile.get('name')}: skill path is outside skills/: {item}") from exc
        if source_contains_symlink(skill_dir):
            raise BuildError(f"profile {profile.get('name')}: skill source contains a symlink: {item}")
        skill_dirs.append(skill_dir)
    if not skill_dirs:
        raise BuildError(f"profile {profile.get('name')}: profile has no skills")
    return skill_dirs


def generate_layer(target_root: Path) -> dict[str, Any]:
    profiles = load_profiles_sorted()
    if target_root.exists():
        shutil.rmtree(target_root)
    (target_root / ".agents" / "plugins").mkdir(parents=True, exist_ok=True)
    (target_root / "plugins").mkdir(parents=True, exist_ok=True)

    copied_skill_count = 0
    for profile in profiles:
        profile_name = str(profile["name"])
        plugin_root = target_root / "plugins" / profile_name
        manifest_dir = plugin_root / ".codex-plugin"
        skills_dir = plugin_root / "skills"
        manifest_dir.mkdir(parents=True, exist_ok=True)
        skills_dir.mkdir(parents=True, exist_ok=True)

        (manifest_dir / "plugin.json").write_text(json_dump(build_plugin_json(profile)), encoding="utf-8")
        for source_dir in resolve_profile_skill_dirs(profile):
            dest = skills_dir / skill_flat_name(source_dir)
            shutil.copytree(source_dir, dest, ignore=ignore_copy_names, copy_function=shutil.copy2)
            sanitize_generated_snapshot(dest)
            copied_skill_count += 1

    marketplace = build_marketplace(profiles)
    (target_root / ".agents" / "plugins" / "marketplace.json").write_text(json_dump(marketplace), encoding="utf-8")
    return {
        "profile_count": len(profiles),
        "plugin_count": len(profiles),
        "copied_skill_count": copied_skill_count,
        "marketplace_path": relative(target_root / ".agents" / "plugins" / "marketplace.json"),
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


def validate_plugin_json(plugin_dir: Path, profile: dict[str, Any], errors: list[str], warnings: list[str]) -> int:
    profile_name = str(profile["name"])
    plugin_json_path = plugin_dir / ".codex-plugin" / "plugin.json"
    payload = load_json(plugin_json_path, errors)
    if not isinstance(payload, dict):
        return 0

    if "[TODO:" in plugin_json_path.read_text(encoding="utf-8", errors="replace"):
        errors.append(f"{relative(plugin_json_path)}: must not contain [TODO: placeholders")
    if payload.get("name") != profile_name:
        errors.append(f"{relative(plugin_json_path)}: name must equal plugin directory name {profile_name}")
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
    expected_skill_dirs = [skills_dir / skill_flat_name(source_dir) for source_dir in resolve_profile_skill_dirs(profile)]
    found_skill_md = sorted(skills_dir.glob("*/SKILL.md")) if skills_dir.exists() else []
    if not found_skill_md:
        errors.append(f"{relative(skills_dir)}: each plugin must contain at least one copied SKILL.md")
    for expected_dir in expected_skill_dirs:
        if not (expected_dir / "SKILL.md").exists():
            errors.append(f"{relative(expected_dir)}: expected copied skill with SKILL.md")
    expected_names = {path.name for path in expected_skill_dirs}
    actual_names = {path.parent.name for path in found_skill_md}
    extras = sorted(actual_names - expected_names)
    if extras:
        warnings.append(f"{relative(skills_dir)}: extra skill directories not listed in profile: {', '.join(extras)}")
    return len(found_skill_md)


def validate_layer(root: Path = CODEX_ROOT) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    profiles = load_profiles_sorted()
    profile_by_name = {str(profile["name"]): profile for profile in profiles}

    assert_no_symlink(root, errors)
    marketplace = load_json(root / ".agents" / "plugins" / "marketplace.json", errors)
    copied_skill_count = 0
    plugin_count = 0

    if isinstance(marketplace, dict):
        if marketplace.get("name") != "yuukias-ai-skills":
            errors.append("plugins/codex/.agents/plugins/marketplace.json: name must be yuukias-ai-skills")
        interface = marketplace.get("interface")
        if not isinstance(interface, dict) or interface.get("displayName") != "YuukiAS AI Skills":
            errors.append("plugins/codex/.agents/plugins/marketplace.json: interface.displayName must be YuukiAS AI Skills")
        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list):
            errors.append("plugins/codex/.agents/plugins/marketplace.json: plugins must be a list")
            plugins = []
        plugin_count = len(plugins)
        if plugin_count != len(profiles):
            errors.append(
                f"plugins/codex/.agents/plugins/marketplace.json: expected {len(profiles)} plugin entries, found {plugin_count}"
            )
        seen_names: set[str] = set()
        for entry in plugins:
            if not isinstance(entry, dict):
                errors.append("plugins/codex/.agents/plugins/marketplace.json: every plugins[] entry must be an object")
                continue
            name = entry.get("name")
            if not isinstance(name, str):
                errors.append("plugins/codex/.agents/plugins/marketplace.json: every plugins[] entry needs a string name")
                continue
            seen_names.add(name)
            if name not in profile_by_name:
                errors.append(f"plugins/codex/.agents/plugins/marketplace.json: unknown profile plugin {name}")
                continue
            expected_source = {"source": "local", "path": f"./plugins/{name}"}
            if entry.get("source") != expected_source:
                errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} source must be {expected_source}")
            policy = entry.get("policy")
            if not isinstance(policy, dict):
                errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} policy must be an object")
            else:
                expected_install = "INSTALLED_BY_DEFAULT" if name == "codex-core-global" else "AVAILABLE"
                if policy.get("installation") != expected_install:
                    errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} installation must be {expected_install}")
                if policy.get("authentication") != "ON_INSTALL":
                    errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} authentication must be ON_INSTALL")
                if policy.get("installation") not in INSTALL_POLICIES:
                    errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} has invalid installation policy")
                if policy.get("authentication") not in AUTH_POLICIES:
                    errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} has invalid authentication policy")
            if entry.get("category") != category_for_profile(name):
                errors.append(f"plugins/codex/.agents/plugins/marketplace.json: {name} category is incorrect")
            plugin_dir = root / "plugins" / name
            if not plugin_dir.is_dir():
                errors.append(f"{relative(plugin_dir)}: marketplace source.path does not resolve to a real plugin directory")
            else:
                copied_skill_count += validate_plugin_json(plugin_dir, profile_by_name[name], errors, warnings)
        missing_names = sorted(set(profile_by_name) - seen_names)
        for name in missing_names:
            errors.append(f"plugins/codex/.agents/plugins/marketplace.json: missing profile plugin {name}")

    todo_matches = []
    if root.exists():
        for path in root.rglob("*"):
            if path.is_file() and not path.is_symlink():
                try:
                    if "[TODO:" in path.read_text(encoding="utf-8", errors="ignore"):
                        todo_matches.append(relative(path))
                except OSError:
                    pass
    if todo_matches:
        errors.append("plugins/codex contains [TODO: placeholders: " + ", ".join(sorted(todo_matches)))

    return {
        "profile_count": len(profiles),
        "plugin_count": plugin_count,
        "copied_skill_count": copied_skill_count,
        "marketplace_path": relative(root / ".agents" / "plugins" / "marketplace.json"),
        "errors": errors,
        "warnings": warnings,
    }


def collect_files(root: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    if not root.exists():
        return files
    for path in sorted(root.rglob("*")):
        if path.is_file() or path.is_symlink():
            files[path.relative_to(root).as_posix()] = path
    return files


def compare_layers(expected_root: Path, current_root: Path) -> list[str]:
    differences: list[str] = []
    expected_files = collect_files(expected_root)
    current_files = collect_files(current_root)
    for rel_path in sorted(set(expected_files) - set(current_files)):
        differences.append(f"missing: plugins/codex/{rel_path}")
    for rel_path in sorted(set(current_files) - set(expected_files)):
        differences.append(f"extra: plugins/codex/{rel_path}")
    for rel_path in sorted(set(expected_files) & set(current_files)):
        expected = expected_files[rel_path]
        current = current_files[rel_path]
        if expected.is_symlink() or current.is_symlink():
            differences.append(f"symlink differs: plugins/codex/{rel_path}")
            continue
        if not filecmp.cmp(expected, current, shallow=False):
            differences.append(f"content differs: plugins/codex/{rel_path}")
            continue
        expected_mode = stat.S_IMODE(expected.stat().st_mode)
        current_mode = stat.S_IMODE(current.stat().st_mode)
        if expected_mode != current_mode:
            differences.append(f"mode differs: plugins/codex/{rel_path}")
    return differences


def check_layer() -> tuple[dict[str, Any], list[str]]:
    with tempfile.TemporaryDirectory(prefix="codex-marketplace-") as tmp:
        expected_root = Path(tmp) / "codex"
        summary = generate_layer(expected_root)
        summary["marketplace_path"] = relative(MARKETPLACE_PATH)
        differences = compare_layers(expected_root, CODEX_ROOT)
    if differences:
        summary["errors"] = [f"publication layer is not current ({len(differences)} differences)"]
    return summary, differences


def print_summary(summary: dict[str, Any], json_output: bool) -> None:
    if json_output:
        print(json_dump(summary), end="")
        return
    print(
        f"profiles={summary['profile_count']} plugins={summary['plugin_count']} "
        f"copied_skills={summary['copied_skill_count']} marketplace={summary['marketplace_path']}"
    )
    for warning in summary.get("warnings", []):
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in summary.get("errors", []):
        print(f"ERROR: {error}", file=sys.stderr)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate plugins/codex")
    parser.add_argument("--validate", action="store_true", help="Validate the current plugins/codex layer")
    parser.add_argument("--check", action="store_true", help="Compare plugins/codex with a freshly generated layer")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable summary")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    actions = [args.write, args.validate, args.check]
    if not any(actions):
        args.validate = True

    exit_code = 0
    summary: dict[str, Any] | None = None
    try:
        if args.write:
            summary = generate_layer(CODEX_ROOT)
            if not args.json:
                print_summary(summary, False)
        if args.validate:
            summary = validate_layer(CODEX_ROOT)
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
            if differences:
                exit_code = 1
        if args.json:
            if summary is None:
                summary = validate_layer(CODEX_ROOT)
            print_summary(summary, True)
    except BuildError as exc:
        summary = {
            "profile_count": 0,
            "plugin_count": 0,
            "copied_skill_count": 0,
            "marketplace_path": relative(MARKETPLACE_PATH),
            "errors": [str(exc)],
            "warnings": [],
        }
        print_summary(summary, args.json)
        return 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
