#!/usr/bin/env python3
"""Compatibility wrapper for scripts/skills.py install."""

from __future__ import annotations

import argparse

from skills import main as skills_main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project")
    parser.add_argument("--profile", default="auto", help="Profile name; 'auto' is kept for compatibility and maps to codex-skill-maintenance in this repo")
    parser.add_argument("--intent", default="", help="Ignored compatibility option")
    parser.add_argument("--mode", choices=("symlink", "copy"), default="symlink")
    parser.add_argument("--write-agents-md", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--global", dest="global_install", action="store_true", help="Compatibility alias for --target user")
    parser.add_argument("--prune-global", action="store_true", help="Compatibility alias for --prune-managed with --global")
    parser.add_argument("--repair-project-codex-symlink", action="store_true", help="Ignored; repo installs now use .agents/skills")
    args = parser.parse_args()

    profile = args.profile
    if profile == "auto":
        profile = "codex-skill-maintenance"
    argv = ["install", "--target", "user" if args.global_install else "repo", "--profile", profile, "--mode", args.mode]
    if args.project and not args.global_install:
        argv.extend(["--project", args.project])
    if args.write_agents_md:
        argv.append("--write-agents-md")
    if args.dry_run:
        argv.append("--dry-run")
    if args.prune_global:
        argv.append("--prune-managed")
    return skills_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
