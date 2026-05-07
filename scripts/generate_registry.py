#!/usr/bin/env python3
"""Generate registry.json from SKILL.md files."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
REGISTRY = ROOT / "registry.json"


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        data[key.strip()] = value
    return data


def skill_record(skill_file: Path) -> dict[str, object]:
    rel_dir = skill_file.parent.relative_to(ROOT)
    parts = rel_dir.parts
    scope = parts[1] if len(parts) > 1 else ""
    category = parts[2] if len(parts) > 2 else ""
    slug = parts[-1]
    meta = read_frontmatter(skill_file)
    name = meta.get("name") or slug

    return {
        "id": ".".join(part for part in (scope, category, slug) if part),
        "name": name,
        "path": rel_dir.as_posix(),
        "scope": scope,
        "category": category,
        "description": meta.get("description", ""),
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
