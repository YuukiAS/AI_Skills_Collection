#!/usr/bin/env python3
"""Audit marketplace and active-skill icon metadata."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

from skill_utils import ROOT, active_skill_records, read_frontmatter


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


def repo_asset(path: str | None) -> Path | None:
    if not path:
        return None
    return ROOT / str(path).removeprefix("./")


def skill_asset(skill_dir: Path, path: str | None) -> Path | None:
    if not path:
        return None
    return skill_dir / str(path)


def marketplace_app_skill_errors() -> list[str]:
    errors: list[str] = []
    config = load_config()
    for plugin in config.get("plugins", []):
        plugin_name = plugin.get("name", "<unknown>")
        for entry in plugin.get("skills", []):
            entry_type = entry.get("type")
            if entry_type == "copy":
                source = entry.get("source")
                skill_dir = ROOT / str(source)
                meta, _ = read_frontmatter(skill_dir / "SKILL.md")
                for field in ("icon_small", "icon_large"):
                    icon = skill_asset(skill_dir, meta.get(field))
                    if icon is None:
                        errors.append(f"plugin {plugin_name} skill {source}: missing {field}")
                    else:
                        check_svg(icon, errors)
            elif entry_type == "aggregate":
                name = entry.get("name", "<unknown>")
                for field in ("icon_small", "icon_large"):
                    icon = repo_asset(entry.get(field))
                    if icon is None:
                        errors.append(f"plugin {plugin_name} aggregate {name}: missing {field}")
                    else:
                        check_svg(icon, errors)
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


def write_contact_sheet(path: Path) -> None:
    config = load_config()
    icons: list[tuple[str, str]] = []
    for plugin in config.get("plugins", []):
        icon = plugin.get("composerIcon")
        if icon:
            icons.append((str(plugin.get("name")), str(icon).removeprefix("./")))
        for entry in plugin.get("skills", []):
            if entry.get("type") == "aggregate" and entry.get("icon_small"):
                icons.append((str(entry.get("name")), str(entry.get("icon_small"))))
            elif entry.get("type") == "copy":
                skill_dir = ROOT / str(entry.get("source"))
                meta, _ = read_frontmatter(skill_dir / "SKILL.md")
                if meta.get("icon_small"):
                    icons.append((str(meta.get("name") or skill_dir.name), f"{entry.get('source')}/{meta.get('icon_small')}"))
    width = 640
    cell = 128
    rows = max(1, (len(icons) + 4) // 5)
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{rows * cell}" viewBox="0 0 {width} {rows * cell}">']
    lines.append('<rect width="100%" height="100%" fill="#ffffff"/>')
    for index, (label, icon) in enumerate(icons):
        x = (index % 5) * cell + 16
        y = (index // 5) * cell + 12
        href = Path(icon).as_posix()
        if not re.match(r"^[a-z]+:", href):
            href = Path(os.path.relpath(ROOT / icon, path.parent)).as_posix()
        lines.append(f'<image href="{href}" x="{x}" y="{y}" width="56" height="56"/>')
        lines.append(f'<text x="{x}" y="{y + 78}" font-size="10" font-family="Arial, sans-serif" fill="#111827">{label}</text>')
    lines.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=["marketplace", "active-skills"], default="marketplace")
    parser.add_argument("--contact-sheet", help="Reserved path for a future generated contact sheet")
    parser.add_argument("--check", action="store_true", help="Exit non-zero on audit errors")
    args = parser.parse_args()

    errors = marketplace_errors() + marketplace_app_skill_errors() if args.scope == "marketplace" else active_skill_errors()
    for error in errors:
        print(f"ERROR: {error}")
    if args.contact_sheet:
        write_contact_sheet(Path(args.contact_sheet))
    if not errors:
        print(f"{args.scope}: icon audit passed")
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
