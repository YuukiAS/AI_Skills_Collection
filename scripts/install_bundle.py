#!/usr/bin/env python3
"""Legacy bundle installer.

Prefer scripts/install_project_skills.py for project-local skill installs. This
script is kept for compatibility with old bundle deployments.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def copy_path(source: Path, target_root: Path) -> None:
    rel = source.relative_to(ROOT)
    dest = target_root / rel
    if source.is_dir():
        if dest.exists():
            shutil.rmtree(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, dest, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)


def skill_dest_name(skill_dir: Path) -> str:
    rel = skill_dir.relative_to(ROOT)
    parts = rel.parts
    if len(parts) >= 4 and parts[0] == "skills":
        return "-".join(parts[1:])
    return skill_dir.name


def iter_skill_dirs(source: Path) -> list[Path]:
    if source.is_file():
        return []
    if (source / "SKILL.md").exists():
        return [source]
    return sorted(path.parent for path in source.rglob("SKILL.md"))


def copy_skill_flat(skill_dir: Path, target_root: Path) -> None:
    dest = target_root / skill_dest_name(skill_dir)
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill_dir, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", help="Path to a bundle JSON file, such as bundles/base.json")
    parser.add_argument("--target", required=True, help="Target directory to copy bundle contents into")
    parser.add_argument(
        "--mode",
        choices=("tree", "flat"),
        default="tree",
        help=(
            "tree preserves repository-relative paths; flat copies each skill "
            "directory directly under target with scope/category prefixes"
        ),
    )
    args = parser.parse_args()

    bundle_path = (ROOT / args.bundle).resolve() if not Path(args.bundle).is_absolute() else Path(args.bundle)
    target = Path(args.target).expanduser().resolve()
    global_skills = (Path.home() / ".codex" / "skills").resolve()
    if target == global_skills:
        print(
            "WARNING: installing broad bundles into global ~/.codex/skills can "
            "trigger skill budget warnings. Prefer codex-core-global plus "
            "project-local installs via scripts/install_project_skills.py."
        )

    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    for item in bundle["include"]:
        source = ROOT / item
        if not source.exists():
            raise FileNotFoundError(item)
        if args.mode == "flat" and source.parts[-1] != "palette":
            skill_dirs = iter_skill_dirs(source)
            if skill_dirs:
                for skill_dir in skill_dirs:
                    copy_skill_flat(skill_dir, target)
                print(f"installed {len(skill_dirs)} skills from {item}")
            else:
                copy_path(source, target)
                print(f"installed {item}")
        else:
            copy_path(source, target)
            print(f"installed {item}")

    print(f"bundle {bundle.get('name', bundle_path.stem)} installed to {target} ({args.mode} mode)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
