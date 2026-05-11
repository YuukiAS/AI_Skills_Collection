#!/usr/bin/env python3
"""Generate registry.json from SKILL.md files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
REGISTRY = ROOT / "registry.json"


def read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}

    try:
        _, raw, _ = text.split("---", 2)
    except ValueError:
        return {}

    parsed = yaml.safe_load(raw) or {}
    return parsed if isinstance(parsed, dict) else {}


def skill_record(skill_file: Path) -> dict[str, object]:
    rel_dir = skill_file.parent.relative_to(ROOT)
    parts = rel_dir.parts
    scope = parts[1] if len(parts) > 1 else ""
    category = parts[2] if len(parts) > 2 else ""
    slug = parts[-1]
    meta = read_frontmatter(skill_file)
    name = meta.get("name") or slug
    description = meta.get("description") or ""

    return {
        "id": ".".join(part for part in (scope, category, slug) if part),
        "name": str(name),
        "path": rel_dir.as_posix(),
        "scope": scope,
        "category": category,
        "description": str(description),
        "status": "active",
    }


def main() -> None:
    records = [
        skill_record(path)
        for path in sorted(SKILLS_ROOT.rglob("SKILL.md"))
        if "archive" not in path.parts
    ]
    output = {
        "version": "1.0.0",
        "description": "Generated skill registry for AI_Skills_Collection.",
        "skill_count": len(records),
        "skills": records,
    }
    REGISTRY.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {REGISTRY.relative_to(ROOT)} with {len(records)} skills")


if __name__ == "__main__":
    main()
