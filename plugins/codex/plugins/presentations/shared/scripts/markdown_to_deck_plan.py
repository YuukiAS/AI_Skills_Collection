#!/usr/bin/env python3
"""Convert heading-structured Markdown into a minimal deck-plan JSON file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")


def markdown_to_deck_plan(markdown: str, title: str, output: str = "pptx") -> dict:
    slides = []
    current: dict | None = None
    for line_no, line in enumerate(markdown.splitlines(), start=1):
        match = HEADING_RE.match(line)
        if match:
            if current:
                slides.append(current)
            slide_no = len(slides) + 1
            heading = match.group(2).strip()
            current = {
                "id": f"s{slide_no:02d}",
                "title": heading,
                "key_message": heading,
                "source_anchors": [f"markdown:L{line_no}"],
                "content": [],
            }
            continue
        if current and line.strip():
            current["content"].append(line.strip())
    if current:
        slides.append(current)
    if not slides:
        slides.append({"id": "s01", "title": title, "key_message": title, "source_anchors": ["markdown:L1"], "content": []})
    return {
        "schema_version": 1,
        "metadata": {
            "title": title,
            "audience": "mixed",
            "mode": "research",
            "purpose": "group-meeting",
            "duration_minutes": max(5, len(slides) * 2),
            "language": "mixed",
            "template": "cuhk-default",
            "output": output,
            "source_files": [],
        },
        "slides": slides,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--title", default=None)
    parser.add_argument("--output", choices=["pptx", "tex", "pdf", "google-slides"], default="pptx")
    parser.add_argument("--write", type=Path, help="Write JSON deck plan to this path")
    args = parser.parse_args()
    title = args.title or args.markdown.stem.replace("-", " ").title()
    plan = markdown_to_deck_plan(args.markdown.read_text(encoding="utf-8"), title, args.output)
    text = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        args.write.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
