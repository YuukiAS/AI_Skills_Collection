#!/usr/bin/env python3
"""Unified CLI for AI_Skills_Collection."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from skill_utils import (
    AGENTS_END,
    AGENTS_START,
    LEGACY_PROJECT_SKILLS_DIR,
    MANIFEST_NAME,
    REPO_SKILLS_DIR,
    ROOT,
    SKILLS_ROOT,
    USER_SKILLS_ROOT,
    active_skill_records,
    audit_records,
    codex_home,
    copy_or_link_skill,
    detect_git_root,
    git_commit,
    load_profiles,
    normalize_project_path,
    read_frontmatter,
    record_source_dir,
    select_records,
    target_skills_root,
    utc_now,
    write_frontmatter,
)


REGISTRY = ROOT / "registry.json"
DOCS = ROOT / "docs"
CATALOG = DOCS / "SKILL_CATALOG.md"
DOMAIN_DOCS = DOCS / "domains"
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
HIGH_RISK_DOMAINS = ("medical", "medicine", "finance", "legal", "system-ops")


def print_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def active_records_sorted(include_archive: bool = False) -> list[dict[str, Any]]:
    return sorted(active_skill_records(include_archive=include_archive), key=lambda r: (r["scope"], r["domain"], r["name"]))


def filtered_records(args: argparse.Namespace) -> list[dict[str, Any]]:
    records = active_records_sorted(include_archive=getattr(args, "include_archive", False))
    profiles = load_profiles()
    profile_paths: set[str] = set()
    if getattr(args, "profile", None):
        profile = profiles.get(args.profile)
        if not profile:
            raise SystemExit(f"unknown profile: {args.profile}")
        for item in profile.get("skills", []):
            profile_paths.add(str((ROOT / item).resolve()))

    def keep(record: dict[str, Any]) -> bool:
        if getattr(args, "domain", None) and record.get("domain") != args.domain and record.get("scope") != args.domain:
            return False
        if getattr(args, "scope", None) and record.get("scope") != args.scope:
            return False
        if getattr(args, "category", None) and args.category not in {record.get("category"), f"{record.get('scope')}/{record.get('domain')}"}:
            return False
        if getattr(args, "tag", None) and args.tag not in record.get("profile_tags", []):
            return False
        if getattr(args, "profile", None) and str((ROOT / record["path"]).resolve()) not in profile_paths:
            return False
        return True

    return [record for record in records if keep(record)]


def command_list(args: argparse.Namespace) -> int:
    records = filtered_records(args)
    if args.json:
        print_json({"skill_count": len(records), "skills": records})
        return 0
    for record in records:
        print(
            f"{record.get('install_selector', record['selectors'][0]):36} "
            f"{record['scope']:9} {record.get('domain') or '-':18} "
            f"{record['name']}: {record.get('description', '')}"
        )
    print(f"\n{len(records)} skills")
    return 0


def registry_data(include_archive: bool = False) -> dict[str, Any]:
    records = active_records_sorted(include_archive=include_archive)
    return {
        "version": "3.0.0",
        "generated_at": utc_now(),
        "description": "Generated skill registry for AI_Skills_Collection. Do not edit by hand.",
        "include_archive": bool(include_archive),
        "skill_count": len(records),
        "selectors": {
            "domains": sorted({str(r.get("domain")) for r in records if r.get("domain")}),
            "scopes": sorted({str(r.get("scope")) for r in records if r.get("scope")}),
            "categories": sorted({str(r.get("category")) for r in records if r.get("category")}),
        },
        "skills": records,
    }


def command_registry(args: argparse.Namespace) -> int:
    data = registry_data(include_archive=args.include_archive)
    if args.write:
        REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {REGISTRY.relative_to(ROOT)} with {data['skill_count']} skills")
    else:
        print_json(data)
    return 0


def install_command_hint(record: dict[str, Any], target: str = "repo") -> str:
    selector = str(record.get("install_selector") or record["selectors"][0])
    base = "python3 scripts/skills.py install"
    if target == "repo":
        return f"{base} --target repo --skill {selector} --mode symlink --write-agents-md"
    return f"{base} --target {target} --skill {selector} --mode symlink"


def catalog_markdown(records: list[dict[str, Any]]) -> str:
    lines = [
        "# Skill Catalog",
        "",
        f"Generated at `{utc_now()}` from `registry.json` metadata. Do not edit by hand.",
        "",
        "Budget warnings in this catalog are guidance for context hygiene; they do not make complete domain installation invalid.",
        "",
    ]
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[(str(record["scope"]), str(record.get("domain") or "unknown"), str(record.get("category") or "unknown"))].append(record)
    for (scope, domain, category), items in sorted(grouped.items()):
        lines.extend([f"## {scope} / {domain} / {category}", ""])
        lines.append("| Skill | Path | Description | Recommended scope | Network | Executes code | Writes files | Last reviewed | Install |")
        lines.append("|---|---|---|---|---:|---:|---:|---|---|")
        for r in sorted(items, key=lambda x: x["name"]):
            desc = str(r.get("description") or "").replace("|", "\\|")
            lines.append(
                f"| `{r['name']}` | `{r['path']}` | {desc} | `{r.get('recommended_scope', '')}` | "
                f"{bool(r.get('requires_network'))} | {bool(r.get('executes_code'))} | {bool(r.get('writes_files'))} | "
                f"`{r.get('last_reviewed', '')}` | `{install_command_hint(r)}` |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def domain_page(domain: str, records: list[dict[str, Any]]) -> str:
    active = [r for r in records if r.get("domain") == domain or r.get("scope") == domain]
    active.sort(key=lambda r: r["name"])
    selectors = " ".join(f"--skill {r.get('install_selector', r['selectors'][0])}" for r in active[:3])
    refs: list[str] = []
    for r in active:
        ref_dir = ROOT / r["path"] / "references"
        if ref_dir.exists():
            refs.extend(str(p.relative_to(ROOT)) for p in sorted(ref_dir.glob("*.md"))[:5])
    lines = [
        f"# {domain}",
        "",
        f"Active skills: {len(active)}",
        "",
        "## Install",
        "",
        "Complete domain install:",
        "",
        "```bash",
        f"python3 scripts/skills.py install --target repo --domain {domain} --mode symlink --write-agents-md",
        "```",
        "",
        "Install a few skills precisely:",
        "",
        "```bash",
        f"python3 scripts/skills.py install --target repo {selectors} --mode symlink --write-agents-md",
        "```",
        "",
        "Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.",
        "",
        "## Common Uses",
        "",
        "- Install the whole domain for a project where most tasks are in this area.",
        "- Use precise skill selectors when only one tool or workflow is needed.",
        "- Combine with profiles when a project needs a curated cross-domain set.",
        "",
        "## Skills",
        "",
    ]
    for r in active:
        lines.append(f"- `{r['name']}` (`{r['path']}`): {r.get('description', '')}")
    lines.extend(["", "## Main References", ""])
    if refs:
        for ref in sorted(set(refs)):
            lines.append(f"- `{ref}`")
    else:
        lines.append("- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.")
    return "\n".join(lines).rstrip() + "\n"


def command_catalog(args: argparse.Namespace) -> int:
    records = active_records_sorted(include_archive=False)
    text = catalog_markdown(records)
    if args.write:
        DOCS.mkdir(exist_ok=True)
        CATALOG.write_text(text, encoding="utf-8")
        DOMAIN_DOCS.mkdir(parents=True, exist_ok=True)
        for old_page in DOMAIN_DOCS.glob("*.md"):
            old_page.unlink()
        domains = sorted({str(r.get("domain")) for r in records if r.get("domain")})
        for domain in domains:
            (DOMAIN_DOCS / f"{domain}.md").write_text(domain_page(domain, records), encoding="utf-8")
        if "medicine-clinical" in domains:
            alias = domain_page("medicine-clinical", records).replace("# medicine-clinical", "# medical-knowledge", 1)
            alias += "\nAlias for registry domain `medicine-clinical`.\n"
            (DOMAIN_DOCS / "medical-knowledge.md").write_text(alias, encoding="utf-8")
        print(f"wrote {CATALOG.relative_to(ROOT)} and {len(domains)} domain pages")
    else:
        print(text)
    return 0


def infer_project(args: argparse.Namespace) -> tuple[Path, bool]:
    if getattr(args, "project", None):
        return normalize_project_path(args.project), True
    return detect_git_root(Path.cwd())


def codex_home_report(skills_root: Path) -> list[str]:
    info = codex_home_info(skills_root)
    return [
        f"detected CODEX_HOME: {info['detected_CODEX_HOME'] or '(unset)'}",
        f"resolved codex home: {info['resolved_codex_home']}",
        f"target skills root: {info['target_skills_root']}",
        f"config.toml exists: {info['config_toml_exists']}",
        f"skills root writable: {info['skills_root_writable']}",
        f"target class: {info['target_class']}",
    ]


def codex_home_info(skills_root: Path) -> dict[str, Any]:
    raw, home = codex_home()
    return {
        "detected_CODEX_HOME": raw or "",
        "resolved_codex_home": str(home),
        "target_skills_root": str(skills_root),
        "config_toml_exists": (home / "config.toml").exists(),
        "skills_root_writable": bool(
            (skills_root.exists() and os.access(skills_root, os.W_OK)) or os.access(skills_root.parent, os.W_OK)
        ),
        "target_class": "explicit legacy/advanced compatibility target",
    }


def agents_block(project: Path, target: str, install_kind: str, records: list[dict[str, Any]], mode: str, prune: bool) -> str:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[str(record.get("domain") or record.get("scope") or "other")].append(record)
    lines = [
        AGENTS_START,
        "# AI Skills Collection",
        "",
        f"Installed: `{utc_now()}`",
        f"Target: `{target}`",
        f"Install mode: `{install_kind}`",
        f"Project skills: `{REPO_SKILLS_DIR.as_posix()}/`",
        f"Central collection: `{ROOT.as_posix()}`",
        "",
        "When a task matches an installed skill, read that skill's `SKILL.md` before acting. Keep progressive disclosure: load `references/` only when the skill says they are relevant.",
        "",
        "## Skill Routing",
        "",
    ]
    for domain, items in sorted(groups.items()):
        lines.append(f"### {domain}")
        for record in sorted(items, key=lambda r: r["name"]):
            rel = REPO_SKILLS_DIR / record["flat_name"] / "SKILL.md"
            desc = str(record.get("description") or "").strip()
            if len(desc) > 220:
                desc = desc[:217].rstrip() + "..."
            lines.append(f"- `{record['name']}`: {desc} Path: `{rel.as_posix()}`")
        lines.append("")
    update_parts = ["python3", f"{ROOT.as_posix()}/scripts/skills.py", "install", "--target", "repo", "--mode", mode]
    if install_kind.startswith("profile:"):
        update_parts.extend(["--profile", install_kind.split(":", 1)[1]])
    elif install_kind.startswith("domain:"):
        update_parts.extend(["--domain", install_kind.split(":", 1)[1]])
    else:
        for record in records:
            update_parts.extend(["--skill", str(record.get("install_selector") or record["selectors"][0])])
    update_parts.append("--write-agents-md")
    if prune:
        update_parts.append("--prune-managed")
    lines.extend(
        [
            "## Skill Maintenance",
            "",
            f"- Update command: `{' '.join(update_parts)}`",
            f"- Managed manifest: `{(REPO_SKILLS_DIR / MANIFEST_NAME).as_posix()}`",
            "- The installer only manages paths recorded in that manifest.",
            "- User-created skills outside the manifest are never pruned.",
            AGENTS_END,
        ]
    )
    return "\n".join(lines) + "\n"


def update_agents(project: Path, block: str, dry_run: bool) -> None:
    path = project / "AGENTS.md"
    current = path.read_text(encoding="utf-8", errors="replace") if path.exists() else "# AGENTS.md\n\n"
    if AGENTS_START in current and AGENTS_END in current:
        before = current.split(AGENTS_START, 1)[0]
        after = current.split(AGENTS_END, 1)[1]
        new_text = before.rstrip() + "\n\n" + block + after.lstrip("\n")
    else:
        new_text = current.rstrip() + "\n\n" + block
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def prune_managed(manifest: dict[str, Any], desired: set[str], skills_root: Path, dry_run: bool) -> list[str]:
    removed: list[str] = []
    for item in manifest.get("installed_skills", []):
        dest = item.get("dest")
        if not dest or dest in desired:
            continue
        path = skills_root / dest
        if not path.exists() and not path.is_symlink():
            continue
        removed.append(dest)
        if dry_run:
            continue
        if path.is_symlink() or path.is_file():
            path.unlink()
        else:
            import shutil

            shutil.rmtree(path)
    return removed


def install_kind(args: argparse.Namespace) -> str:
    parts = []
    for profile in args.profile or []:
        parts.append(f"profile:{profile}")
    for domain in args.domain or []:
        parts.append(f"domain:{domain}")
    if args.category:
        parts.append("category:" + ",".join(args.category))
    if args.skill:
        parts.append("skills")
    return "mixed:" + "+".join(parts) if len(parts) > 1 else (parts[0] if parts else "explicit")


def command_install(args: argparse.Namespace) -> int:
    if not (args.profile or args.domain or args.category or args.skill):
        raise SystemExit("install requires --profile, --domain, --category, or --skill")
    records = select_records(args.profile, args.domain, args.category, args.skill)
    if not records:
        raise SystemExit("no active skills selected")

    project, project_was_explicit = infer_project(args)
    target_info: dict[str, Any] = {}
    output_warnings: list[str] = []
    if args.target == "repo":
        skills_root = target_skills_root("repo", project)
        if not project_was_explicit:
            _, is_git = detect_git_root(Path.cwd())
            if not is_git:
                output_warnings.append(f"current directory is not a git repo; using current directory as project: {project}")
    elif args.target == "user":
        skills_root = USER_SKILLS_ROOT
    else:
        skills_root = target_skills_root("codex-home")
        target_info = codex_home_info(skills_root)
        if not args.json:
            for line in codex_home_report(skills_root):
                print(line)

    manifest_path = skills_root / MANIFEST_NAME
    old_manifest = load_manifest(manifest_path)
    desired_dests = {str(r["flat_name"]) for r in records}
    removed: list[str] = []
    if args.prune_managed:
        removed = prune_managed(old_manifest, desired_dests, skills_root, args.dry_run)

    installed: list[dict[str, Any]] = []
    modes = Counter()
    for record in records:
        source_dir = record_source_dir(record)
        used_mode = copy_or_link_skill(source_dir, skills_root / record["flat_name"], args.mode, args.dry_run)
        modes[used_mode] += 1
        installed.append(
            {
                "name": record["name"],
                "path": record["path"],
                "dest": record["flat_name"],
                "source": str(source_dir.resolve()),
                "mode": used_mode,
                "selectors": record["selectors"],
            }
        )

    block = agents_block(project, args.target, install_kind(args), records, args.mode, args.prune_managed)
    if args.write_agents_md and args.target == "repo":
        update_agents(project, block, args.dry_run)
    elif args.write_agents_md and args.target != "repo":
        output_warnings.append("--write-agents-md is only applied for --target repo")

    audit = audit_records(records, block if args.target == "repo" else "")
    manifest = {
        "schema_version": 3,
        "target": args.target,
        "install_kind": install_kind(args),
        "installed_at": utc_now(),
        "collection_path": str(ROOT.resolve()),
        "collection_commit": git_commit(),
        "install_mode_requested": args.mode,
        "install_mode_counts": dict(modes),
        "project_path": str(project.resolve()) if args.target == "repo" else "",
        "skills_root": str(skills_root),
        "agents_md_managed": bool(args.write_agents_md and args.target == "repo"),
        "prune_managed": bool(args.prune_managed),
        "target_info": target_info,
        "audit": audit,
        "installed_skills": installed,
    }
    if not args.dry_run:
        skills_root.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.json:
        print_json({"dry_run": args.dry_run, "manifest": manifest, "removed": removed})
        return 0
    print(f"target: {args.target}")
    print(f"skills root: {skills_root}")
    print(f"selected skills: {len(records)}")
    print(f"mode: {args.mode} ({'dry run' if args.dry_run else ', '.join(f'{k}={v}' for k, v in modes.items())})")
    print(f"manifest: {manifest_path} ({'would write' if args.dry_run else 'written'})")
    if args.write_agents_md and args.target == "repo":
        print(f"AGENTS.md: {'would update' if args.dry_run else 'updated'}")
    if removed:
        print(f"pruned managed skills: {', '.join(removed)}")
    for warning in output_warnings:
        print(f"WARNING: {warning}")
    for warning in audit["warnings"]:
        print(f"WARNING: {warning}")
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    project, is_git = infer_project(args)
    raw, home = codex_home()
    repo_root = target_skills_root("repo", project)
    user_root = target_skills_root("user")
    codex_root = target_skills_root("codex-home")
    legacy_root = project / LEGACY_PROJECT_SKILLS_DIR
    data = {
        "current_directory": str(Path.cwd()),
        "detected_project_root": str(project),
        "project_root_is_git": is_git,
        "repo_skills_root": str(repo_root),
        "user_skills_root": str(user_root),
        "detected_CODEX_HOME": raw or "",
        "resolved_codex_home": str(home),
        "codex_home_skills_root": str(codex_root),
        "codex_home_config_exists": (home / "config.toml").exists(),
        "legacy_project_codex_skills_exists": legacy_root.exists() or legacy_root.is_symlink(),
        "repo_manifest_exists": (repo_root / MANIFEST_NAME).exists(),
        "user_manifest_exists": (user_root / MANIFEST_NAME).exists(),
        "codex_home_manifest_exists": (codex_root / MANIFEST_NAME).exists(),
        "recommended_commands": [
            "python3 scripts/skills.py select",
            "python3 scripts/skills.py install --target repo --profile codex-skill-maintenance --mode symlink --write-agents-md",
            "python3 scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md",
            "python3 scripts/skills.py install --target user --profile codex-core-global --mode symlink",
        ],
    }
    if args.json:
        print_json(data)
    else:
        for key, value in data.items():
            if isinstance(value, list):
                print(f"{key}:")
                for item in value:
                    print(f"  - {item}")
            else:
                print(f"{key}: {value}")
    return 0


def validate_eval_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.relative_to(ROOT)}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{path.relative_to(ROOT)}: eval file must be an object"]
    for key in ("positive", "negative", "near_miss"):
        if key in data and not isinstance(data[key], list):
            errors.append(f"{path.relative_to(ROOT)}: {key} must be a list")
    return errors


def command_validate(args: argparse.Namespace) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    seen: dict[str, list[str]] = defaultdict(list)
    for skill_file in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        rel = skill_file.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if "archive" in skill_file.parts:
            continue
        meta, _ = read_frontmatter(skill_file)
        if meta.get("status") == "archived":
            continue
        if not meta:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        name = str(meta.get("name") or "")
        desc = str(meta.get("description") or "")
        if not name:
            errors.append(f"{rel}: name is required")
        elif len(name) > 64 or not NAME_RE.match(name) or "--" in name:
            errors.append(f"{rel}: name must be <=64 chars, lowercase letters/digits/hyphen only, no edge/consecutive hyphen")
        elif name != skill_file.parent.name:
            errors.append(f"{rel}: name must match parent directory ({skill_file.parent.name})")
        if not desc:
            errors.append(f"{rel}: description is required")
        elif len(desc) > 1024:
            errors.append(f"{rel}: description exceeds official 1024 character limit")
        elif len(desc) > 350:
            warnings.append(f"{rel}: description is {len(desc)} chars; consider <=350")
        seen[name].append(str(rel))
        for field in ("secrets_needed", "profile_tags"):
            value = meta.get(field, [])
            if value in ("", None, {}):
                continue
            if not isinstance(value, list):
                warnings.append(f"{rel}: {field} should be a list")
        eval_path = skill_file.parent / "evals" / "trigger_queries.json"
        if eval_path.exists():
            errors.extend(validate_eval_file(eval_path))
    for name, paths in seen.items():
        if name and len(paths) > 1:
            errors.append(f"duplicate active skill name {name}: {', '.join(paths)}")

    profiles = load_profiles()
    for profile_name, profile in sorted(profiles.items()):
        skills = profile.get("skills")
        if not isinstance(skills, list) or not skills:
            errors.append(f"profile {profile_name}: missing non-empty skills list")
            continue
        for item in skills + list(profile.get("secondary_skills", [])):
            skill_path = ROOT / str(item) / "SKILL.md"
            if not skill_path.exists():
                errors.append(f"profile {profile_name}: missing skill path {item}")

    template = ROOT / "shared" / "templates" / "AGENTS.md.template"
    if not template.exists():
        errors.append("missing shared/templates/AGENTS.md.template")
    else:
        text = template.read_text(encoding="utf-8", errors="replace")
        if ".codex/skills" in text:
            errors.append("AGENTS template still refers to .codex/skills")
        if AGENTS_START not in text or AGENTS_END not in text:
            errors.append("AGENTS template missing managed block markers")

    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"validated {len(seen)} active skills, {len(profiles)} profiles, templates, and trigger eval scaffolds")
    return 0


def command_audit(args: argparse.Namespace) -> int:
    groups: list[tuple[str, list[dict[str, Any]], str]] = []
    if args.all:
        for name, profile in sorted(load_profiles().items()):
            records = select_records(profiles=[name])
            groups.append((f"profile:{name}", records, "profile"))
        for domain in sorted({str(r.get("domain")) for r in active_skill_records() if r.get("domain")}):
            records = select_records(domains=[domain])
            groups.append((f"domain:{domain}", records, "domain"))
    elif args.profile:
        groups.append((f"profile:{args.profile}", select_records(profiles=[args.profile]), "profile"))
    elif args.domain:
        groups.append((f"domain:{args.domain}", select_records(domains=[args.domain]), "domain"))
    elif args.skill:
        groups.append(("explicit:" + ",".join(args.skill), select_records(skills=args.skill), "explicit install"))
    else:
        groups.append(("all-active", active_skill_records(), "repository"))

    exit_code = 0
    target = getattr(args, "target", "repo")
    for label, records, kind in groups:
        audit = audit_records(records)
        high_risk = [r for r in records if any(str(r.get("domain", "")).startswith(prefix) for prefix in HIGH_RISK_DOMAINS)]
        print(f"\n== {label} ({kind}; target:{target}) ==")
        print(f"active_skill_count: {audit['active_skill_count']}")
        print(f"description_total_chars: {audit['description_total_chars']}")
        print(f"scope_distribution: {json.dumps(audit['scope_distribution'], ensure_ascii=False, sort_keys=True)}")
        print(f"domain_distribution: {json.dumps(audit['domain_distribution'], ensure_ascii=False, sort_keys=True)}")
        if target == "repo":
            print("target_budget_context: repo-specific .agents/skills; broader installs are acceptable when useful for this project")
        elif target == "user":
            print("target_budget_context: user-level $HOME/.agents/skills; prefer small reusable/core sets")
        else:
            print("target_budget_context: explicit legacy codex-home; keep small and avoid pruning unless manifest-managed")
        if audit["warnings"]:
            for warning in audit["warnings"]:
                print(f"WARNING: {warning} (budget warning; does not block domain/profile installation)")
        if high_risk:
            missing = [r["path"] for r in high_risk if not (ROOT / r["path"] / "references").exists()]
            if missing:
                print(f"WARNING: high-risk skills without references/source notes: {len(missing)}")
            for r in high_risk:
                if not r.get("requires_network"):
                    print(f"WARNING: {r['path']} should require authoritative/current source checking for high-risk claims")
        print("advice: narrow descriptions, split curated profiles, use explicit --skill selectors, or mention a skill with `$name` when budget warnings appear.")
    return exit_code


def command_new(args: argparse.Namespace) -> int:
    if not NAME_RE.match(args.name) or "--" in args.name:
        raise SystemExit("skill name must use lowercase letters, digits, and hyphen only")
    scope_aliases = {"domain": "domains", "tool": "tools", "reusable": "tools", "research": "science", "system": "core"}
    scope_dir = scope_aliases.get(args.scope, args.scope)
    parts = [SKILLS_ROOT, scope_dir]
    if scope_dir == "domains":
        if not args.domain:
            raise SystemExit("--domain is required with --scope domain")
        parts.append(args.domain)
        if args.category:
            parts.append(args.category)
    elif scope_dir in {"tools", "science"}:
        if not args.category:
            raise SystemExit(f"--category is required with --scope {args.scope}")
        parts.append(args.category)
    elif scope_dir == "writing":
        parts.append(args.category or "core")
    elif scope_dir == "projects":
        parts.append(args.domain or args.category or "general")
    elif scope_dir == "core":
        parts.append(args.category or "codex-system")
    elif args.category:
        parts.append(args.category)
    skill_dir = Path(*parts) / args.name
    skill_file = skill_dir / "SKILL.md"
    if skill_file.exists() and not args.force:
        raise SystemExit(f"skill already exists: {skill_dir.relative_to(ROOT)}")
    if not args.dry_run:
        skill_dir.mkdir(parents=True, exist_ok=True)
        for folder in args.with_dirs:
            (skill_dir / folder).mkdir(parents=True, exist_ok=True)
        meta = {
            "name": args.name,
            "description": args.description,
            "status": "active",
            "provenance": "user-authored",
            "trusted": False,
            "requires_network": bool(args.requires_network),
            "writes_files": True,
            "executes_code": False,
            "secrets_needed": [],
            "last_reviewed": utc_now().split("T", 1)[0],
            "profile_tags": [],
            "recommended_scope": "project",
        }
        body = f"""# {args.name}

## Trigger Boundary

Use this skill only for the workflow described in the frontmatter description.

## Workflow

1. Clarify the concrete task and inputs.
2. Read only the relevant files under `references/` when domain details are needed.
3. Use scripts under `scripts/` for deterministic or repeated operations.
4. Validate outputs with project-specific tests or documented checks.

## References

- Read `references/overview.md` for domain background when the task requires more than the executable workflow.
- Read `references/source-notes.md` before making high-risk or time-sensitive claims.
"""
        write_frontmatter(skill_file, meta, body)
        if "references" in args.with_dirs:
            for name, title in {
                "overview.md": "Overview",
                "glossary.md": "Glossary",
                "checklists.md": "Checklists",
                "source-notes.md": "Source Notes",
            }.items():
                p = skill_dir / "references" / name
                if not p.exists():
                    p.write_text(f"# {title}\n\nAdd concise, dated, source-bounded notes here.\n", encoding="utf-8")
        if "evals" in args.with_dirs:
            eval_path = skill_dir / "evals" / "trigger_queries.json"
            eval_path.write_text(
                json.dumps({"positive": [], "negative": [], "near_miss": [], "notes": ""}, indent=2) + "\n",
                encoding="utf-8",
            )
    print(f"{'would create' if args.dry_run else 'created'} {skill_dir.relative_to(ROOT)}")
    return 0


def command_select(args: argparse.Namespace) -> int:
    try:
        from InquirerPy import inquirer
    except ImportError:
        print("Interactive selection requires InquirerPy.")
        print("Install it with: python3 -m pip install InquirerPy")
        print("Equivalent non-interactive examples:")
        print("  python3 scripts/skills.py install --target repo --domain bayesian --mode symlink --write-agents-md")
        print("  python3 scripts/skills.py install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md")
        return 2

    target = inquirer.select(
        message="Install target",
        choices=[
            {"name": "repo (recommended): current/specified repo .agents/skills", "value": "repo"},
            {"name": "user: $HOME/.agents/skills", "value": "user"},
            {"name": "codex-home: explicit legacy/advanced compatibility target", "value": "codex-home"},
        ],
        default="repo",
    ).execute()
    if target == "codex-home":
        confirm = inquirer.confirm(message="Use explicit codex-home compatibility target?", default=False).execute()
        if not confirm:
            print("aborted")
            return 1
    project, _ = detect_git_root(Path.cwd())
    if target == "repo":
        project_text = inquirer.text(message="Project path", default=str(project)).execute()
    else:
        project_text = str(project)
    strategy = inquirer.select(
        message="Install mode",
        choices=["profile", "domain", "single skills", "mixed selection"],
        default="profile",
    ).execute()
    profiles: list[str] = []
    domains: list[str] = []
    skills: list[str] = []
    records = active_skill_records()
    if strategy in {"profile", "mixed selection"}:
        profiles = inquirer.checkbox(message="Profiles", choices=sorted(load_profiles().keys())).execute()
    if strategy in {"domain", "mixed selection"}:
        domain_choices = sorted({str(r.get("domain")) for r in records if r.get("domain")})
        domains = inquirer.checkbox(message="Domains", choices=domain_choices).execute()
    if strategy in {"single skills", "mixed selection"}:
        query = inquirer.text(message="Search skills (empty for all)", default="").execute().lower()
        choices = []
        for r in records:
            selector = str(r.get("install_selector") or r["selectors"][0])
            text = f"{selector} | {r['name']} | {r.get('description','')} | scope={r.get('recommended_scope')} network={r.get('requires_network')} exec={r.get('executes_code')} writes={r.get('writes_files')} reviewed={r.get('last_reviewed')}"
            if not query or query in text.lower():
                choices.append({"name": text[:180], "value": selector})
        skills = inquirer.checkbox(message="Skills", choices=choices).execute()
    selected = select_records(profiles=profiles, domains=domains, skills=skills)
    if not selected:
        print("no skills selected")
        return 1
    mode = inquirer.select(message="Filesystem mode", choices=["symlink", "copy"], default="symlink").execute()
    write_agents = target == "repo" and inquirer.confirm(message="Write AGENTS.md managed block?", default=True).execute()
    prune = inquirer.confirm(message="Prune managed skills absent from this selection?", default=False).execute()
    summary = {
        "target": target,
        "project": project_text,
        "skills_root": str(target_skills_root(target, normalize_project_path(project_text))),
        "skill_count": len(selected),
        "mode": mode,
        "write_agents_md": write_agents,
        "prune_managed": prune,
        "uses_detected_codex_home": target == "codex-home",
    }
    print_json(summary)
    if not inquirer.confirm(message="Install with this summary?", default=False).execute():
        print("aborted")
        return 1
    install_args = argparse.Namespace(
        target=target,
        project=project_text,
        profile=profiles,
        domain=domains,
        category=[],
        skill=skills,
        mode=mode,
        dry_run=False,
        yes=True,
        prune_managed=prune,
        write_agents_md=write_agents,
        json=False,
    )
    return command_install(install_args)


def command_migrate_legacy(args: argparse.Namespace) -> int:
    project = normalize_project_path(args.project) if args.project else detect_git_root(Path.cwd())[0]
    legacy_root = project / LEGACY_PROJECT_SKILLS_DIR
    new_root = project / REPO_SKILLS_DIR
    raw, home = codex_home()
    if legacy_root.exists() or legacy_root.is_symlink():
        try:
            if legacy_root.resolve() == (home / "skills").resolve():
                raise SystemExit(f"refusing to migrate legacy path that resolves to global codex home: {legacy_root} -> {home / 'skills'}")
        except FileNotFoundError:
            pass
    manifest_path = legacy_root / MANIFEST_NAME
    if not manifest_path.exists():
        raise SystemExit(f"missing legacy manifest: {manifest_path}")
    old = json.loads(manifest_path.read_text(encoding="utf-8"))
    skills = []
    for item in old.get("installed_skills", []):
        selector = item.get("path") or item.get("source")
        if selector:
            source = Path(str(selector))
            if source.is_absolute() and source.name != "SKILL.md":
                try:
                    skills.append(str(source.relative_to(ROOT)))
                except ValueError:
                    pass
            else:
                skills.append(str(selector).removeprefix("skills/"))
    if not skills:
        for item in old.get("installed_skills", []):
            if item.get("name"):
                skills.append(item["name"])
    print(f"legacy root: {legacy_root}")
    print(f"new root: {new_root}")
    print(f"detected CODEX_HOME: {raw or '(unset)'}")
    print(f"skills to reinstall: {len(skills)}")
    ns = argparse.Namespace(
        target="repo",
        project=str(project),
        profile=[],
        domain=[],
        category=[],
        skill=skills,
        mode=args.mode,
        dry_run=args.dry_run,
        yes=args.yes,
        prune_managed=False,
        write_agents_md=True,
        json=False,
    )
    return command_install(ns)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("list", help="List skills")
    p.add_argument("--domain")
    p.add_argument("--scope")
    p.add_argument("--category")
    p.add_argument("--tag")
    p.add_argument("--profile")
    p.add_argument("--include-archive", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_list)

    p = sub.add_parser("catalog", help="Generate catalog docs")
    p.add_argument("--write", action="store_true")
    p.set_defaults(func=command_catalog)

    p = sub.add_parser("registry", help="Generate or print registry JSON")
    p.add_argument("--write", action="store_true")
    p.add_argument("--include-archive", action="store_true")
    p.set_defaults(func=command_registry)

    p = sub.add_parser("install", help="Install selected skills")
    p.add_argument("--target", choices=["repo", "user", "codex-home"], default="repo")
    p.add_argument("--project")
    p.add_argument("--profile", action="append", default=[])
    p.add_argument("--domain", action="append", default=[])
    p.add_argument("--category", action="append", default=[])
    p.add_argument("--skill", action="append", default=[])
    p.add_argument("--mode", choices=["symlink", "copy"], default="symlink")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--yes", action="store_true")
    p.add_argument("--prune-managed", action="store_true")
    p.add_argument("--no-prune", dest="prune_managed", action="store_false")
    p.add_argument("--write-agents-md", action="store_true")
    p.add_argument("--no-agents-md", dest="write_agents_md", action="store_false")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_install, prune_managed=False, write_agents_md=False)

    p = sub.add_parser("select", help="Interactive installer")
    p.set_defaults(func=command_select)

    p = sub.add_parser("new", help="Create a new central-library skill")
    p.add_argument("--scope", required=True, choices=["domain", "domains", "tool", "tools", "writing", "science", "research", "project", "projects", "core", "system", "reusable"])
    p.add_argument("--domain")
    p.add_argument("--category")
    p.add_argument("--name", required=True)
    p.add_argument("--description", required=True)
    p.add_argument("--with-dirs", nargs="*", default=["references", "evals"], choices=["references", "scripts", "assets", "evals"])
    p.add_argument("--requires-network", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=command_new)

    p = sub.add_parser("validate", help="Validate skills and profiles")
    p.set_defaults(func=command_validate)

    p = sub.add_parser("audit", help="Audit skill budgets and high-risk metadata")
    p.add_argument("--all", action="store_true")
    p.add_argument("--profile")
    p.add_argument("--domain")
    p.add_argument("--skill", action="append", default=[])
    p.add_argument("--target", choices=["repo", "user", "codex-home"], default="repo")
    p.add_argument("--run-agent-evals", action="store_true", help="Reserved; never enabled by default")
    p.set_defaults(func=command_audit)

    p = sub.add_parser("doctor", help="Inspect install paths and legacy state")
    p.add_argument("--project")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_doctor)

    p = sub.add_parser("migrate-legacy", help="Reinstall managed .codex/skills into .agents/skills")
    p.add_argument("--project")
    p.add_argument("--mode", choices=["symlink", "copy"], default="symlink")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--yes", action="store_true")
    p.set_defaults(func=command_migrate_legacy)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
