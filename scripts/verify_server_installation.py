#!/usr/bin/env python3
"""Server-local smoke verification for AI_Skills_Collection installs."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import skills
from skill_utils import MANIFEST_NAME, ROOT, read_frontmatter


DEFAULT_PROFILE = "server-research-baseline"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_PAYLOAD_ROOT = ROOT / "plugins" / "codex" / "plugins"
OPTIONAL_COMMANDS = (
    "git",
    "xelatex",
    "kpsewhich",
    "latexmk",
    "pandoc",
    "sbatch",
    "squeue",
    "sinfo",
    "scontrol",
)
OPTIONAL_PYTHON_MODULES = ("pptx",)


def add_check(checks: list[dict[str, Any]], name: str, ok: bool, detail: str = "") -> None:
    checks.append({"name": name, "ok": bool(ok), "detail": detail})


def path_is_within(path: Path, base: Path) -> bool:
    try:
        path.resolve().relative_to(base.resolve())
    except ValueError:
        return False
    return True


def real_home_reasons(path: Path) -> list[str]:
    resolved = path.expanduser().resolve()
    reasons: list[str] = []
    default_home = (Path.home() / ".codex").resolve()
    if resolved == default_home:
        reasons.append(f"matches default Codex home {default_home}")
    env_home = os.environ.get("CODEX_HOME")
    if env_home and resolved == Path(env_home).expanduser().resolve():
        reasons.append(f"matches current CODEX_HOME {resolved}")
    if path.exists() and not path_is_within(path, Path(tempfile.gettempdir())):
        reasons.append("existing non-temporary path")
    return reasons


@contextmanager
def temporary_codex_home(requested: str | None, allow_real_home: bool, keep: bool) -> Iterator[tuple[Path, bool]]:
    """Yield a Codex home path and whether it was auto-created."""

    previous = os.environ.get("CODEX_HOME")
    created_temp: Path | None = None
    if requested:
        home = Path(requested).expanduser().resolve()
        reasons = real_home_reasons(home)
        if reasons and not allow_real_home:
            raise SystemExit(
                "refusing to use a real or existing Codex home without --allow-real-home: "
                + "; ".join(reasons)
        )
        auto_created = False
    else:
        home = Path(tempfile.mkdtemp(prefix="ai-skills-codex-home-smoke.")).resolve()
        created_temp = home
        auto_created = True

    os.environ["CODEX_HOME"] = str(home)
    try:
        yield home, auto_created
    finally:
        if previous is None:
            os.environ.pop("CODEX_HOME", None)
        else:
            os.environ["CODEX_HOME"] = previous
        if created_temp is not None and not keep:
            shutil.rmtree(created_temp, ignore_errors=True)


def install_to_codex_home(args: argparse.Namespace) -> dict[str, Any]:
    profiles = list(args.profile or [])
    domains = list(args.domain or [])
    categories = list(args.category or [])
    selected_skills = list(args.skill or [])
    if not (profiles or domains or categories or selected_skills):
        profiles = [DEFAULT_PROFILE]
    install_args = argparse.Namespace(
        target="codex-home",
        project=None,
        profile=profiles,
        domain=domains,
        category=categories,
        skill=selected_skills,
        mode=args.mode,
        dry_run=False,
        yes=True,
        prune_managed=True,
        write_agents_md=False,
        json=True,
    )
    return skills.install_result(install_args)


def validate_installed_manifest(manifest: dict[str, Any], checks: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    skills_root = Path(str(manifest.get("skills_root") or ""))
    add_check(checks, "manifest-target", manifest.get("target") == "codex-home", str(manifest.get("target")))
    add_check(checks, "skills-root-exists", skills_root.exists(), str(skills_root))
    manifest_path = skills_root / MANIFEST_NAME
    add_check(checks, "manifest-written", manifest_path.exists(), str(manifest_path))
    installed = manifest.get("installed_skills", [])
    add_check(checks, "installed-skill-count", bool(installed), str(len(installed)))

    for item in installed:
        dest_name = str(item.get("dest") or "")
        skill_dir = skills_root / dest_name
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{dest_name}: missing SKILL.md")
            continue
        meta, _body = read_frontmatter(skill_file)
        if not meta.get("name"):
            errors.append(f"{dest_name}: missing name frontmatter")
        if not meta.get("description"):
            errors.append(f"{dest_name}: missing description frontmatter")
        for field in ("icon_small", "icon_large"):
            icon = meta.get(field)
            if not icon:
                errors.append(f"{dest_name}: missing {field}")
                continue
            icon_path = skill_dir / str(icon)
            if not icon_path.exists():
                errors.append(f"{dest_name}: missing {field} file {icon}")
        if item.get("mode") == "copy" and skill_dir.is_symlink():
            errors.append(f"{dest_name}: expected copied directory, found symlink")
    add_check(checks, "installed-frontmatter-and-icons", not errors, f"errors={len(errors)}")
    return errors


def validate_marketplace_payload(checks: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if not MARKETPLACE_PATH.exists():
        add_check(checks, "marketplace-manifest", False, str(MARKETPLACE_PATH))
        return [f"missing marketplace manifest: {MARKETPLACE_PATH.relative_to(ROOT)}"]
    try:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        add_check(checks, "marketplace-manifest", False, str(exc))
        return [f"invalid marketplace JSON: {exc}"]
    plugins = marketplace.get("plugins", [])
    add_check(checks, "marketplace-manifest", bool(plugins), f"plugins={len(plugins)}")
    for plugin in plugins:
        name = str(plugin.get("name") or "<unknown>")
        source = plugin.get("source", {}) if isinstance(plugin.get("source"), dict) else {}
        rel = str(source.get("path") or "")
        plugin_root = (ROOT / rel.removeprefix("./")).resolve()
        if not plugin_root.exists():
            errors.append(f"plugin {name}: missing payload path {rel}")
            continue
        plugin_json = plugin_root / ".codex-plugin" / "plugin.json"
        if not plugin_json.exists():
            errors.append(f"plugin {name}: missing .codex-plugin/plugin.json")
        skills_dir = plugin_root / "skills"
        if not skills_dir.exists():
            errors.append(f"plugin {name}: missing skills directory")
        if not list(skills_dir.rglob("SKILL.md")):
            errors.append(f"plugin {name}: no SKILL.md in payload")
    add_check(checks, "marketplace-payload", not errors, f"errors={len(errors)}")
    return errors


def local_tooling_report() -> dict[str, Any]:
    return {
        "commands": {name: shutil.which(name) for name in OPTIONAL_COMMANDS},
        "python": {
            "executable": sys.executable,
            "version": sys.version.split()[0],
            "modules": {name: importlib.util.find_spec(name) is not None for name in OPTIONAL_PYTHON_MODULES},
        },
    }


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    errors: list[str] = []
    warnings: list[str] = []
    with temporary_codex_home(args.codex_home, args.allow_real_home, args.keep) as (home, auto_created):
        result = install_to_codex_home(args)
        manifest = result["manifest"]
        errors.extend(validate_installed_manifest(manifest, checks))
        errors.extend(validate_marketplace_payload(checks))
        tooling = local_tooling_report()
        missing_optional_commands = [name for name, path in tooling["commands"].items() if not path]
        missing_optional_modules = [name for name, present in tooling["python"]["modules"].items() if not present]
        if missing_optional_commands:
            warnings.append("optional commands not found: " + ", ".join(missing_optional_commands))
        if missing_optional_modules:
            warnings.append("optional Python modules not found: " + ", ".join(missing_optional_modules))
        report = {
            "schema_version": 1,
            "kind": "ai-skills-server-local-installation-smoke",
            "ok": not errors and all(check["ok"] for check in checks),
            "codex_home": str(home),
            "auto_created_codex_home": auto_created,
            "kept_codex_home": bool(args.keep),
            "selection": manifest.get("install_request", {}),
            "manifest_path": result["manifest_path"],
            "installed_skill_count": len(manifest.get("installed_skills", [])),
            "install_mode_counts": manifest.get("install_mode_counts", {}),
            "collection_commit": manifest.get("collection_commit"),
            "checks": checks,
            "warnings": warnings,
            "errors": errors,
            "tooling": tooling,
        }
        return report


def print_human(report: dict[str, Any]) -> None:
    print(f"ok: {report['ok']}")
    print(f"codex_home: {report['codex_home']}")
    print(f"manifest: {report['manifest_path']}")
    print(f"installed_skill_count: {report['installed_skill_count']}")
    for check in report["checks"]:
        status = "PASS" if check["ok"] else "FAIL"
        detail = f" ({check['detail']})" if check.get("detail") else ""
        print(f"{status}: {check['name']}{detail}")
    for warning in report["warnings"]:
        print(f"WARNING: {warning}")
    for error in report["errors"]:
        print(f"ERROR: {error}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Verify AI_Skills_Collection installation locally on this server. "
            "This does not log in, SSH, call Codex App, or submit Slurm jobs."
        )
    )
    parser.add_argument("--profile", action="append", default=[], help=f"Profile to install; defaults to {DEFAULT_PROFILE}")
    parser.add_argument("--domain", action="append", default=[], help="Domain selector to install; repeatable")
    parser.add_argument("--category", action="append", default=[], help="Category selector to install; repeatable")
    parser.add_argument("--skill", action="append", default=[], help="Precise skill selector to install; repeatable")
    parser.add_argument("--mode", choices=["copy", "symlink"], default="copy", help="Install mode for the smoke target")
    parser.add_argument("--codex-home", help="Codex home to use. Omit for an auto-created temporary home")
    parser.add_argument("--allow-real-home", action="store_true", help="Allow writing to an existing or real Codex home")
    parser.add_argument("--keep", action="store_true", help="Keep an auto-created temporary Codex home for inspection")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    report = build_report(args)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_human(report)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
