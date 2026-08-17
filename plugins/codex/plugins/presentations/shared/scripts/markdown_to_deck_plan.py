#!/usr/bin/env python3
"""Convert heading-structured Markdown into a minimal deck-plan JSON file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")


def editability_for_output(output: str) -> str:
    return {
        "pptx": "editable",
        "google-slides": "editable",
        "tex": "source-editable",
        "pdf": "static",
    }[output]


def empty_evidence_board() -> dict:
    return {
        "available_figures": [],
        "medical_images": [],
        "qualitative_examples": [],
        "quantitative_plots": [],
        "model_diagrams": [],
        "equations": [],
        "experiment_logs": [],
        "failed_experiments": [],
        "literature_figures_to_redraw": [],
        "missing_evidence": [],
    }


def default_research_state(title: str) -> dict:
    return {
        "previous_question": f"What changed since the last discussion about {title}?",
        "prior_belief": "UNKNOWN until source evidence is reviewed.",
        "new_evidence": "UNKNOWN until the evidence board is populated.",
        "evidence_quality": "UNKNOWN until provenance, sample size, replication, and caveats are checked.",
        "belief_update": "UNKNOWN until evidence is compared with the prior belief.",
        "successes": "UNKNOWN until supported results are identified.",
        "failures": "UNKNOWN until failed experiments or negative evidence are identified.",
        "largest_uncertainty": "UNKNOWN until evidence gaps are ranked.",
        "frozen_items": "UNKNOWN until sufficiently supported decisions are identified.",
        "stop_items": "UNKNOWN until low-value routes are identified.",
        "next_discriminating_experiment": "UNKNOWN until competing explanations are named.",
        "decision_needed": "UNKNOWN until the supervisor decision is specified.",
    }


def enrich_research_group_slide(slide: dict) -> dict:
    enriched = dict(slide)
    enriched.update({
        "page_function": "RESEARCH_UPDATE",
        "required_evidence": ["source-tracked evidence or explicit missing-evidence note"],
        "source_evidence_ids": ["markdown"],
        "scientific_objects": ["research question", "source-backed observation"],
        "evidence_status": "partial",
        "uncertainty_status": "requires evidence-board review",
        "layout_rationale": "state-change slide; final layout must follow the scientific objects found in sources",
        "allowed_fallback": "missing evidence, next experiment, speaker notes, backup, or deletion",
        "forbidden_fallback": "rounded-card dashboard, giant empty table, decorative icon, or generic arrows",
        "qa_criteria": [
            "real scientific object is visible",
            "evidence source is named",
            "slide does not leak internal planning language",
        ],
    })
    return enriched


def markdown_to_deck_plan(markdown: str, title: str, output: str = "pptx", mode: str = "research") -> dict:
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
                "slide_purpose": "communicate one research update message",
                "visual_intent": "choose an evidence-bearing visual only if it supports the key message",
                "source_anchors": [f"markdown:L{line_no}"],
                "content": [],
            }
            continue
        if current and line.strip():
            current["content"].append(line.strip())
    if current:
        slides.append(current)
    if not slides:
        slides.append({
            "id": "s01",
            "title": title,
            "key_message": title,
            "slide_purpose": "communicate one research update message",
            "visual_intent": "choose an evidence-bearing visual only if it supports the key message",
            "source_anchors": ["markdown:L1"],
            "content": [],
        })
    plan = {
        "schema_version": 1,
        "metadata": {
            "title": title,
            "audience": "mixed",
            "mode": mode,
            "purpose": "group-meeting",
            "duration_minutes": max(5, len(slides) * 2),
            "language": "mixed",
            "template": "cuhk-default",
            "output": output,
            "editability": editability_for_output(output),
            "source_files": [],
        },
        "slides": slides,
    }
    if mode == "research-group-meeting":
        plan["research_state"] = default_research_state(title)
        plan["evidence_board"] = empty_evidence_board()
        plan["evidence_board"]["missing_evidence"].append({
            "id": "ME-001",
            "claim_or_question": "Populate source-backed evidence before final slide generation.",
            "rights_note": "No external assets copied by the Markdown adapter.",
        })
        plan["slides"] = [enrich_research_group_slide(slide) for slide in slides]
    return plan


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--title", default=None)
    parser.add_argument("--output", choices=["pptx", "tex", "pdf", "google-slides"], default="pptx")
    parser.add_argument("--mode", choices=["research", "research-group-meeting"], default="research")
    parser.add_argument("--write", type=Path, help="Write JSON deck plan to this path")
    args = parser.parse_args()
    title = args.title or args.markdown.stem.replace("-", " ").title()
    plan = markdown_to_deck_plan(args.markdown.read_text(encoding="utf-8"), title, args.output, args.mode)
    text = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
    if args.write:
        args.write.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
