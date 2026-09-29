#!/usr/bin/env python3
"""Frozen Stage 1 Presentations routing contract."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from typing import Any


BUILT_IN_TEMPLATES = ("cuhk-research", "course-standard")
EDITABLE_FORMATS = ("ppt", "pptx", "powerpoint", "slides", "google slides", "editable")
BEAMER_FORMATS = ("beamer", "latex", "latex slides", "tex", ".tex", "academic pdf")
RESEARCH_TERMS = ("research", "group meeting", "seminar", "paper talk", "journal club", "defense", "qe", "oral", "phd", "组会", "论文", "答辩", "研究")
TEACHING_TERMS = ("tutorial", "lecture", "teaching", "courseware", "classroom", "lesson", "课件", "课程", "教学")
BUSINESS_TERMS = ("business", "executive", "product", "strategy", "client", "management", "管理层", "产品策略", "客户")
LOCAL_EDIT_TERMS = ("existing deck", "existing ppt", "current deck", "local edit", "minor edit", "revise this ppt", "现有 ppt", "第 6 页", "改短")
PLAN_ONLY_TERMS = ("outline only", "storyline only", "plan only", "deck plan", "逐页 storyline", "只先给", "不生成")
LOCKED_TEMPLATE_TERMS = ("official template", "locked template", "conference template", "provided template", "按这个会议官方模板")


@dataclass(frozen=True)
class Stage1Route:
    route: str
    adapter: str
    template: str | None
    output: str
    ratio: str | None
    artifact_claim: str
    reason: str


def _contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def _explicit_ratio(text: str) -> str | None:
    if re.search(r"\b16\s*:\s*9\b|\b169\b|wide", text):
        return "16:9"
    if re.search(r"\b4\s*:\s*3\b|\b43\b", text):
        return "4:3"
    return None


def _explicit_beamer(text: str) -> bool:
    return any(term in text for term in ("beamer", "latex slides", ".tex", "overleaf", "academic pdf"))


def _output_tokens(explicit_output: str | None) -> set[str]:
    value = (explicit_output or "").lower().strip()
    if not value:
        return set()
    return {value, value.lstrip(".").replace("-", " ")}


def route_request(prompt: str, *, explicit_output: str | None = None, existing_deck: bool = False, locked_template: bool = False) -> Stage1Route:
    text = prompt.lower()
    ratio = _explicit_ratio(text)
    outputs = _output_tokens(explicit_output)
    explicit_beamer = bool(outputs.intersection(BEAMER_FORMATS)) or _explicit_beamer(text)
    if _contains_any(text, PLAN_ONLY_TERMS):
        return Stage1Route("plan-only", "deck-plan", None, "plan", None, "no generated artifact claim", "plan-only request")
    if existing_deck or _contains_any(text, LOCAL_EDIT_TERMS):
        return Stage1Route("local-edit", "official-editable-surface", None, "preserve-existing", "preserve-existing", "no artifact claim until edited surface is produced", "existing/local edit preserves current format/template/ratio")
    if locked_template or _contains_any(text, LOCKED_TEMPLATE_TERMS):
        return Stage1Route("external-locked-template", "pass-through", None, "preserve-locked", "preserve-locked", "pass-through locked input", "external locked template is not a built-in template")
    if outputs.intersection(EDITABLE_FORMATS) or _contains_any(text, EDITABLE_FORMATS):
        return Stage1Route("editable", "official-editable-surface", None, "pptx/slides", ratio, "editable adapter required", "explicit editable output")
    if _contains_any(text, BUSINESS_TERMS):
        return Stage1Route("editable", "official-editable-surface", None, "pptx/slides", ratio, "editable adapter required", "business/executive route remains editable")
    if _contains_any(text, TEACHING_TERMS):
        return Stage1Route("beamer", "course-standard-beamer", "course-standard", "tex+pdf", ratio or "4:3", "source plus rendered PDF after render-owner QA", "teaching route")
    if _contains_any(text, RESEARCH_TERMS):
        return Stage1Route("beamer", "cuhk-research-beamer", "cuhk-research", "tex+pdf", ratio or "16:9", "source plus rendered PDF after render-owner QA", "research route")
    if explicit_beamer:
        return Stage1Route("beamer", "course-standard-beamer", "course-standard", "tex+pdf", ratio or "4:3", "source plus rendered PDF after render-owner QA", "generic non-branded Beamer")
    return Stage1Route("editable", "official-editable-surface", None, "pptx/slides", ratio, "editable adapter required", "unspecified general deck defaults to editable surface unless research/teaching context is present")


def built_in_template_manifest() -> dict[str, Any]:
    return {
        "schema": "PRESENTATIONS_STAGE1_BUILT_IN_TEMPLATE_MANIFEST_V1",
        "built_in_templates": list(BUILT_IN_TEMPLATES),
        "course_standard": {
            "default_ratio": "4:3",
            "explicit_ratios": ["4:3", "16:9"],
            "same_template_identity_for_16_9": True,
            "canonical_source_status": "WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE",
            "canonical_source_owner": "independent standard-Beamer task",
            "template_body_in_this_task": False,
        },
        "render_environment_owner": "render-chinese-math-pdf",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--output")
    parser.add_argument("--existing-deck", action="store_true")
    parser.add_argument("--locked-template", action="store_true")
    args = parser.parse_args()
    route = route_request(args.prompt, explicit_output=args.output, existing_deck=args.existing_deck, locked_template=args.locked_template)
    print(json.dumps({"route": asdict(route), "template_manifest": built_in_template_manifest()}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
