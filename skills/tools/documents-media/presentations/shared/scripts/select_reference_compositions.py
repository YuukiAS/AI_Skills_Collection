#!/usr/bin/env python3
"""Select research slide composition exemplars without generating slides."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SHARED = Path(__file__).resolve().parents[1]
INDEX = SHARED / "references" / "research_slide_composition_index.json"


def tokens(value: str) -> set[str]:
    return {part.lower() for part in value.replace("/", " ").replace("-", " ").replace("_", " ").split() if len(part) > 2}


def load_records() -> list[dict[str, object]]:
    return json.loads(INDEX.read_text(encoding="utf-8"))["records"]


def score(record: dict[str, object], page_function: str | None, evidence_type: str | None, scientific_object: str | None) -> tuple[int, list[str]]:
    points = 0
    reasons: list[str] = []
    if page_function and str(record["page_function"]) == page_function:
        points += 20
        reasons.append(f"page_function={page_function}")
    if evidence_type and evidence_type.lower() in str(record["evidence_type"]).lower():
        points += 10
        reasons.append(f"evidence_type~={evidence_type}")
    if scientific_object:
        query_terms = tokens(scientific_object)
        record_terms = tokens(" ".join([
            str(record["scientific_object"]),
            " ".join(str(item) for item in record["portable_composition_lessons"]),
            str(record["layout_family"]),
        ]))
        overlap = sorted(query_terms & record_terms)
        if overlap:
            points += min(8, len(overlap) * 2)
            reasons.append("scientific_object_overlap=" + ",".join(overlap))
    if not any([page_function, evidence_type, scientific_object]):
        points = 1
        reasons.append("unfiltered")
    return points, reasons


def select(page_function: str | None, evidence_type: str | None, scientific_object: str | None, limit: int) -> list[dict[str, object]]:
    matches = []
    for record in load_records():
        points, reasons = score(record, page_function, evidence_type, scientific_object)
        if points > 0:
            matches.append((points, str(record["reference_id"]), record, reasons))
    matches.sort(key=lambda item: (-item[0], item[1]))
    output = []
    for points, _, record, reasons in matches[:limit]:
        primary = next(region for region in record["regions"] if region["region_id"] == record["primary_scientific_object_region_id"])
        output.append({
            "reference_id": record["reference_id"],
            "source_id": record["source_id"],
            "page_function": record["page_function"],
            "evidence_type": record["evidence_type"],
            "scientific_object": record["scientific_object"],
            "layout_family": record["layout_family"],
            "reading_flow": record["reading_flow"],
            "primary_object_area_ratio": record["primary_object_area_ratio"],
            "primary_bbox": primary["bbox"],
            "score": points,
            "match_reasons": reasons,
        })
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-function")
    parser.add_argument("--evidence-type")
    parser.add_argument("--scientific-object")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    print(json.dumps({
        "schema": "RESEARCH_SLIDE_COMPOSITION_SELECTION_V1",
        "query": {
            "page_function": args.page_function,
            "evidence_type": args.evidence_type,
            "scientific_object": args.scientific_object,
            "limit": args.limit,
        },
        "matches": select(args.page_function, args.evidence_type, args.scientific_object, args.limit),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
