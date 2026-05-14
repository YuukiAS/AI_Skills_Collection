#!/usr/bin/env python3
"""Install selected skills into a project-local .codex/skills directory."""

from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from pathlib import Path
from typing import Any

from skill_utils import (
    AGENTS_END,
    AGENTS_START,
    MANIFEST_NAME,
    ROOT,
    SKILLS_ROOT,
    audit_records,
    git_commit,
    load_profiles,
    normalize_project_path,
    profile_skill_files,
    read_frontmatter,
    skill_flat_name,
    skill_record,
    utc_now,
)


PROFILE_MARKERS: dict[str, dict[str, list[str]]] = {
    "codex-webdev": {
        "paths": ["package.json", "next.config", "tailwind.config", "src/app", "src/pages", "vite.config", "playwright", "figma"],
        "words": ["react", "next", "tailwind", "shadcn", "figma", "storybook", "playwright", "browser"],
        "intent": ["website", "web app", "frontend", "front-end", "react", "next.js", "tailwind", "landing page", "dashboard", "写网站", "前端", "网页", "做网站"],
    },
    "codex-cardiacnexus": {
        "paths": ["cardiacnexus", "cmr", "dicom", "nifti", "nii", "monai", "nnunet", "slurm", "ukb"],
        "words": ["cardiacnexus", "cmr", "dicom", "nifti", "monai", "nnU-Net", "ukb", "strain", "segmentation"],
        "intent": ["cardiacnexus", "cmr", "cardiac mri", "medical imaging", "dicom", "nifti", "monai", "nnunet", "nnU-Net", "ukb", "心脏", "医学影像"],
    },
    "codex-bayesian-jsdm": {
        "paths": ["trace", "jsdm", "hmsc", "stan", "pymc", "mcmc", "simulation", "manuscript", "theorem"],
        "words": ["trace", "jsdm", "hmsc", "bayesian", "stan", "pymc", "mcmc", "posterior", "theorem"],
        "intent": ["bayesian", "jsdm", "hmsc", "trace", "stan", "pymc", "mcmc", "posterior", "probabilistic", "simulation", "贝叶斯", "层级模型"],
    },
    "codex-research-writing": {
        "paths": ["manuscript", "paper", "latex", "bib", "references", "zotero", "slides", "review", "figures"],
        "words": ["manuscript", "paper", "latex", "bibliography", "zotero", "citation", "peer review", "supplement"],
        "intent": ["paper", "manuscript", "article", "literature review", "citation", "bibliography", "latex", "slides", "peer review", "写论文", "论文", "文献", "投稿"],
    },
    "codex-bioinformatics-light": {
        "paths": ["bioinformatics", "single-cell", "scrna", "rna-seq", "scanpy", "scvi", "vcf", "bam", "gtf", "genomics"],
        "words": ["bioinformatics", "single-cell", "rna-seq", "scanpy", "scvi", "vcf", "bam", "gtf", "genomics"],
        "intent": ["bioinformatics", "single-cell", "scrna", "rna-seq", "scanpy", "scvi", "vcf", "bam", "gtf", "genomics", "生信", "单细胞", "基因组"],
    },
}


def project_signals(project: Path) -> tuple[list[str], str]:
    paths: list[str] = []
    text_chunks: list[str] = []
    for path in sorted(project.rglob("*")):
        if len(paths) >= 2000:
            break
        rel = path.relative_to(project).as_posix()
        if any(part in {".git", ".codex", "node_modules", ".venv", "__pycache__"} for part in path.parts):
            continue
        paths.append(rel.lower())
        if path.is_file() and path.name.lower() in {"readme.md", "pyproject.toml", "package.json", "requirements.txt", "environment.yml"}:
            try:
                text_chunks.append(path.read_text(encoding="utf-8", errors="replace")[:12000].lower())
            except OSError:
                pass
    return paths, "\n".join(text_chunks)


def score_profiles(project: Path, intent: str = "") -> dict[str, dict[str, Any]]:
    if project.resolve() == ROOT.resolve() or (project / "registry.json").exists() and (project / "skills").exists():
        return {"codex-skill-maintenance": {"score": 100, "evidence": ["project is AI_Skills_Collection"]}}
    paths, text = project_signals(project)
    intent_text = intent.lower()
    joined_paths = "\n".join(paths)
    scores: dict[str, dict[str, Any]] = {}
    for profile, markers in PROFILE_MARKERS.items():
        score = 0
        evidence: list[str] = []
        for marker in markers["paths"]:
            if marker.lower() in joined_paths:
                score += 6
                evidence.append(f"path:{marker}")
        for marker in markers["words"]:
            if marker.lower() in text:
                score += 4
                evidence.append(f"text:{marker}")
        for marker in markers.get("intent", []):
            if marker.lower() in intent_text:
                score += 12
                evidence.append(f"intent:{marker}")
        scores[profile] = {"score": score, "evidence": evidence[:10]}
    if not any(item["score"] for item in scores.values()):
        scores["codex-research-writing"]["score"] = 1
        scores["codex-research-writing"]["evidence"].append("fallback:general project")
    return scores


def choose_profile(project: Path, requested: str, profiles: dict[str, dict[str, Any]], intent: str = "") -> tuple[str, list[str], dict[str, Any]]:
    if requested != "auto":
        if requested not in profiles:
            raise SystemExit(f"unknown profile: {requested}")
        return requested, [], {"requested": requested}
    scores = score_profiles(project, intent=intent)
    ranked = sorted(scores.items(), key=lambda item: item[1]["score"], reverse=True)
    primary = ranked[0][0]
    secondary: list[str] = []
    if len(ranked) > 1 and ranked[1][1]["score"] > 0 and ranked[1][1]["score"] >= max(8, ranked[0][1]["score"] * 0.75):
        secondary = [ranked[1][0]]
    return primary, secondary, {"scores": scores, "ranked": ranked}


def desired_skill_files(primary: str, secondary: list[str], profiles: dict[str, dict[str, Any]]) -> list[Path]:
    selected: list[Path] = []
    seen: set[Path] = set()
    for path in profile_skill_files(profiles[primary]):
        if path not in seen:
            selected.append(path)
            seen.add(path)
    for profile_name in secondary:
        for item in profiles[profile_name].get("secondary_skills", [])[:3]:
            path = ROOT / item / "SKILL.md"
            if path.exists() and path not in seen:
                selected.append(path)
                seen.add(path)
    return selected


def copy_or_link(source_dir: Path, dest: Path, mode: str, dry_run: bool) -> str:
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
        print(f"symlink failed for {dest.name}; copied instead ({exc})")
        return "copy"


def infer_commands(project: Path) -> list[str]:
    commands: list[str] = []
    if (project / "package.json").exists():
        commands.extend(["npm run lint", "npm test", "npm run build"])
    if (project / "pyproject.toml").exists():
        commands.extend(["python3 -m pytest", "python3 -m ruff check ."])
    elif (project / "requirements.txt").exists():
        commands.append("python3 -m pytest")
    if (project / "Makefile").exists():
        commands.append("make test")
    return commands[:6] or ["Use project-specific commands from README or package metadata."]


def agents_block(project: Path, profile: str, records: list[dict[str, Any]], managed: bool) -> str:
    lines = [
        AGENTS_START,
        "# AI Skills Collection",
        "",
        f"Profile: `{profile}`",
        f"Installed: `{utc_now()}`",
        f"Project skills: `.codex/skills/`",
        "",
        "When a task matches a skill below, read that skill's `SKILL.md` before acting. Do not read archived skills.",
        "",
        "## Skill Routing",
        "",
    ]
    for record in records:
        rel = Path(".codex/skills") / record["flat_name"] / "SKILL.md"
        desc = str(record.get("description") or "").strip()
        lines.append(f"- `{record['name']}`: {desc} Path: `{rel.as_posix()}`")
    lines.extend(["", "## Project Commands", ""])
    for command in infer_commands(project):
        lines.append(f"- `{command}`")
    lines.extend(
        [
            "",
            "## Skill Maintenance",
            "",
            "- To install or update this project's skills, run the central installer:",
            f"  `python3 {ROOT.as_posix()}/scripts/install_project_skills.py --project {project.as_posix()} --profile auto --mode symlink --write-agents-md`",
            "- The installer only manages paths recorded in `.codex/skills/.ai-skills-collection-manifest.json`.",
            "- It must not clean or rewrite global `~/.codex/skills` for project switching.",
            AGENTS_END,
        ]
    )
    return "\n".join(lines) + "\n"


def update_agents(project: Path, block: str, dry_run: bool) -> None:
    path = project / "AGENTS.md"
    if path.exists():
        current = path.read_text(encoding="utf-8", errors="replace")
    else:
        current = "# AGENTS.md\n\n"
    if AGENTS_START in current and AGENTS_END in current:
        before = current.split(AGENTS_START, 1)[0]
        after = current.split(AGENTS_END, 1)[1]
        new_text = before.rstrip() + "\n\n" + block + after.lstrip("\n")
    else:
        new_text = current.rstrip() + "\n\n" + block
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")


def remove_stale(manifest: dict[str, Any], desired_dests: set[str], skills_root: Path, dry_run: bool) -> None:
    for item in manifest.get("installed_skills", []):
        dest = item.get("dest")
        if not dest or dest in desired_dests:
            continue
        path = skills_root / dest
        if not path.exists() and not path.is_symlink():
            continue
        print(f"remove stale managed skill: {dest}")
        if dry_run:
            continue
        if path.is_symlink() or path.is_file():
            path.unlink()
        else:
            shutil.rmtree(path)


def prune_global_to_profile(skills_root: Path, desired_dests: set[str], dry_run: bool) -> Path | None:
    """One-time migration helper: move non-profile global skills to a backup."""
    if not skills_root.exists():
        return None
    backup = skills_root.parent / f"skills-legacy-full-{utc_now().replace(':', '').replace('+', 'Z')}"
    moved = 0
    for child in sorted(skills_root.iterdir()):
        if child.name.startswith(".") or child.name in desired_dests:
            continue
        if not (child / "SKILL.md").exists() and not child.is_symlink():
            continue
        print(f"prune global skill to backup: {child.name}")
        moved += 1
        if dry_run:
            continue
        backup.mkdir(parents=True, exist_ok=True)
        shutil.move(str(child), str(backup / child.name))
    if moved:
        print(f"global backup: {backup} ({'dry run' if dry_run else 'created'})")
        return backup
    return None


def project_install_root(project: Path, repair_global_link: bool, dry_run: bool) -> Path:
    codex_dir = project / ".codex"
    install_root = codex_dir / "skills"
    global_root = Path.home() / ".codex" / "skills"
    try:
        points_to_global = install_root.exists() and install_root.resolve() == global_root.resolve()
    except OSError:
        points_to_global = False
    if not points_to_global:
        return install_root

    if not repair_global_link:
        raise SystemExit(
            f"project skills path resolves to global skills: {install_root} -> {global_root}. "
            "Refusing project install. Move the project .codex symlink aside or rerun with "
            "--repair-project-codex-symlink to create a real project-local .codex directory."
        )

    backup = project / f".codex-global-link-backup-{utc_now().replace(':', '').replace('+', 'Z')}"
    print(f"repair project .codex global link: {codex_dir} -> backup {backup}")
    if dry_run:
        return install_root
    if codex_dir.is_symlink() or codex_dir.is_file():
        codex_dir.rename(backup)
    elif install_root.is_symlink() or install_root.is_file():
        install_root.rename(project / f".codex-skills-global-link-backup-{utc_now().replace(':', '').replace('+', 'Z')}")
    else:
        raise SystemExit(f"refusing to repair non-symlink project .codex path: {codex_dir}")
    codex_dir.mkdir(parents=True, exist_ok=True)
    return codex_dir / "skills"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=False, default=".", help="Target project root")
    parser.add_argument("--profile", default="auto", help="Profile name or auto")
    parser.add_argument("--intent", default="", help="Natural-language project purpose used by --profile auto")
    parser.add_argument("--mode", choices=("symlink", "copy"), default="symlink")
    parser.add_argument("--write-agents-md", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--global", dest="global_install", action="store_true", help="Install to ~/.codex/skills; use only for codex-core-global")
    parser.add_argument(
        "--prune-global",
        action="store_true",
        help="With --global codex-core-global only: move other global skills to a timestamped backup",
    )
    parser.add_argument(
        "--repair-project-codex-symlink",
        action="store_true",
        help="For project installs only: back up a project .codex symlink that points at global ~/.codex and create a local .codex",
    )
    args = parser.parse_args()

    profiles = load_profiles()
    project = normalize_project_path(args.project)
    if args.global_install:
        print("WARNING: global mode is for tiny bootstrap profiles only; do not use it to switch project skills.")
        if args.profile in {"auto", "codex-core-global"}:
            args.profile = "codex-core-global"
        if args.profile != "codex-core-global":
            raise SystemExit("--global is restricted to codex-core-global in this installer")
        project = Path.home()
        install_root = Path.home() / ".codex" / "skills"
    else:
        install_root = project_install_root(project, args.repair_project_codex_symlink, args.dry_run)
    if not project.exists() and not args.dry_run:
        raise SystemExit(f"project path does not exist: {project}")

    primary, secondary, decision = choose_profile(project, args.profile, profiles, intent=args.intent)
    files = desired_skill_files(primary, secondary, profiles)
    records = [skill_record(path) for path in files]
    desired_dests = {record["flat_name"] for record in records}

    if args.prune_global and not args.global_install:
        raise SystemExit("--prune-global requires --global")
    if args.prune_global and args.global_install:
        prune_global_to_profile(install_root, desired_dests, args.dry_run)

    manifest_path = install_root / MANIFEST_NAME
    old_manifest = {}
    if manifest_path.exists():
        old_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    remove_stale(old_manifest, desired_dests, install_root, args.dry_run)

    installed: list[dict[str, Any]] = []
    modes = Counter()
    for path, record in zip(files, records):
        dest_name = record["flat_name"]
        used_mode = copy_or_link(path.parent, install_root / dest_name, args.mode, args.dry_run)
        modes[used_mode] += 1
        installed.append(
            {
                "name": record["name"],
                "path": record["path"],
                "dest": dest_name,
                "source": str(path.parent.resolve()),
                "mode": used_mode,
            }
        )

    block = agents_block(project, primary, records, args.write_agents_md)
    if args.write_agents_md and not args.global_install:
        update_agents(project, block, args.dry_run)
    audit = audit_records(records, block)
    manifest = {
        "profile": primary,
        "secondary_profiles": secondary,
        "installed_at": utc_now(),
        "collection_path": str(ROOT.resolve()),
        "collection_commit": git_commit(),
        "install_mode_requested": args.mode,
        "install_mode_counts": dict(modes),
        "project_path": str(project.resolve()),
        "skills_root": str(install_root.resolve()),
        "agents_md_managed": bool(args.write_agents_md and not args.global_install),
        "audit": audit,
        "installed_skills": installed,
    }
    if not args.dry_run:
        install_root.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("profile scores:")
    if "scores" in decision:
        for name, item in sorted(decision["scores"].items(), key=lambda x: x[1]["score"], reverse=True):
            print(f"  {name}: {item['score']} ({', '.join(item['evidence'][:5]) or 'no markers'})")
    print(f"selected profile: {primary}")
    if secondary:
        print(f"secondary profile hints: {', '.join(secondary)}")
    print(f"installed skills: {len(records)} into {install_root} ({'dry run' if args.dry_run else ', '.join(f'{k}={v}' for k, v in modes.items())})")
    if args.write_agents_md and not args.global_install:
        print(f"AGENTS.md managed block: {'would update' if args.dry_run else 'updated'}")
    for warning in audit["warnings"]:
        print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
