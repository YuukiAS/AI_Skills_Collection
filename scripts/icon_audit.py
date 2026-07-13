#!/usr/bin/env python3
"""Audit marketplace and active-skill icon metadata."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from skill_utils import ROOT, active_skill_records


CONFIG = ROOT / "scripts" / "codex_marketplace_config.json"
SVG_SCRIPT_RE = re.compile(r"<\s*script|\bon\w+\s*=", re.IGNORECASE)


def load_config() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def check_svg(path: Path, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing icon: {path.relative_to(ROOT).as_posix()}")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    if "<svg" not in text:
        errors.append(f"not an svg: {path.relative_to(ROOT).as_posix()}")
    if SVG_SCRIPT_RE.search(text):
        errors.append(f"unsafe svg content: {path.relative_to(ROOT).as_posix()}")


def marketplace_errors() -> list[str]:
    errors: list[str] = []
    config = load_config()
    for plugin in config.get("plugins", []):
        name = plugin.get("name", "<unknown>")
        icon = plugin.get("composerIcon")
        if not icon:
            errors.append(f"plugin {name}: missing composerIcon")
            continue
        icon_path = ROOT / str(icon).removeprefix("./")
        check_svg(icon_path, errors)
        source = icon_path.with_name("source.json")
        if not source.exists():
            errors.append(f"plugin {name}: missing icon source.json")
        else:
            try:
                payload = json.loads(source.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{source.relative_to(ROOT).as_posix()}: invalid JSON: {exc}")
            else:
                for field in ("source", "license", "created_at"):
                    if not payload.get(field):
                        errors.append(f"{source.relative_to(ROOT).as_posix()}: missing {field}")
    return errors


def active_skill_errors() -> list[str]:
    errors: list[str] = []
    for record in active_skill_records(include_archive=False):
        skill_dir = ROOT / record["path"]
        assets = skill_dir / "assets"
        if not assets.exists():
            continue
        for svg in assets.glob("*.svg"):
            check_svg(svg, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=["marketplace", "active-skills"], default="marketplace")
    parser.add_argument("--contact-sheet", help="Reserved path for a future generated contact sheet")
    parser.add_argument("--check", action="store_true", help="Exit non-zero on audit errors")
    args = parser.parse_args()

    errors = marketplace_errors() if args.scope == "marketplace" else active_skill_errors()
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print(f"{args.scope}: icon audit passed")
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
