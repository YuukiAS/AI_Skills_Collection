#!/usr/bin/env python3
"""Select compatible gold scientific composition records for a page job."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "references" / "research_gold_composition_index.json"


def load_records(path: Path = INDEX) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["records"]


def _tokens(*parts: str) -> set[str]:
    text = " ".join(part or "" for part in parts).replace("_", " ").replace("-", " ").lower()
    return {token for token in "".join(ch if ch.isalnum() else " " for ch in text).split() if token}


def score_record(record: dict, query: dict) -> tuple[int, list[str], list[str]]:
    reasons: list[str] = []
    exclusions: list[str] = []
    score = 0

    page_function = (query.get("page_function") or "").upper()
    if page_function:
        if record["page_function"] == page_function:
            score += 5
            reasons.append("page_function exact match")
        elif page_function.lower() in " ".join(record["scientific_jobs"]).lower():
            score += 3
            reasons.append("page_function matches scientific job")
        else:
            exclusions.append("page_function mismatch")

    domain = query.get("domain_family")
    if domain:
        if domain in record["domain_families"]:
            score += 3
            reasons.append("domain_family match")
        elif "general_research" in record["domain_families"]:
            score += 1
            reasons.append("general research fallback")
        else:
            exclusions.append("domain_family mismatch")

    requested_density = query.get("density")
    if requested_density and requested_density == record["content_capacity"]["density"]:
        score += 1
        reasons.append("density match")

    panel_count = query.get("panel_count")
    if panel_count is not None:
        capacity = record["content_capacity"]["panel_count"]
        if capacity == panel_count:
            score += 2
            reasons.append("panel_count exact match")
        elif capacity and panel_count and abs(capacity - panel_count) <= 2:
            score += 1
            reasons.append("panel_count near match")
        elif panel_count >= 3 and capacity == 0:
            exclusions.append("panel_count incompatible")

    q_tokens = _tokens(query.get("scientific_object", ""), query.get("evidence_type", ""), query.get("dominant_object_type", ""))
    r_tokens = _tokens(
        record["primary_scientific_object_role"],
        record["page_function"],
        record["composition_family"],
        " ".join(record["scientific_jobs"]),
        " ".join(record["selection_keywords"]),
    )
    overlap = q_tokens & r_tokens
    if q_tokens:
        if overlap:
            score += min(5, len(overlap))
            reasons.append(f"scientific object overlap: {', '.join(sorted(overlap)[:5])}")
        else:
            exclusions.append("no scientific-object overlap")

    query_text = " ".join(str(value).lower() for value in query.values() if value is not None)
    rejected_text = " ".join(record.get("rejected_for_jobs", [])).lower()
    for rejected in record.get("rejected_for_jobs", []):
        rejected_tokens = _tokens(rejected)
        if rejected_tokens and rejected_tokens.issubset(_tokens(query_text)):
            exclusions.append(f"semantic incompatibility: query matches rejected job '{rejected}'")

    if exclusions:
        return (0, reasons, exclusions)
    return (score, reasons, exclusions)


def select_records(query: dict, limit: int = 3, records: list[dict] | None = None) -> dict:
    records = records or load_records()
    candidates = []
    excluded = []
    for record in records:
        score, reasons, exclusions = score_record(record, query)
        if score > 0 and not exclusions:
            candidates.append({
                "gold_id": record["gold_id"],
                "reference_id": record["reference_id"],
                "source_id": record["source_id"],
                "page_function": record["page_function"],
                "composition_family": record["composition_family"],
                "primary_bbox": record["primary_bbox"],
                "score": score,
                "compatibility_reasons": reasons,
                "rights_reuse_boundary": record["rights_reuse_boundary"],
            })
        else:
            excluded.append({
                "gold_id": record["gold_id"],
                "reference_id": record["reference_id"],
                "exclusion_reasons": exclusions or ["score below threshold"],
            })
    candidates.sort(key=lambda item: (-item["score"], item["gold_id"]))
    return {
        "schema": "RESEARCH_GOLD_COMPOSITION_SELECTION_V1",
        "query": query,
        "matches": candidates[:limit],
        "excluded": excluded,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-function", required=True)
    parser.add_argument("--scientific-object", required=True)
    parser.add_argument("--domain-family", choices=["statistics", "biostatistics", "medical_imaging", "general_research"], required=True)
    parser.add_argument("--dominant-object-type", default="")
    parser.add_argument("--evidence-type", default="")
    parser.add_argument("--density", choices=["low", "moderate", "high"], default=None)
    parser.add_argument("--panel-count", type=int, default=None)
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    payload = select_records({
        "page_function": args.page_function,
        "scientific_object": args.scientific_object,
        "domain_family": args.domain_family,
        "dominant_object_type": args.dominant_object_type,
        "evidence_type": args.evidence_type,
        "density": args.density,
        "panel_count": args.panel_count,
    }, limit=args.limit)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["matches"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
