#!/usr/bin/env python3
"""Build renderer-neutral composition recipes from selected gold records."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import select_gold_compositions


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "references" / "research_gold_composition_index.json"


def _stable_sha(payload: dict) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _records_by_id() -> dict[str, dict]:
    records = json.loads(INDEX.read_text(encoding="utf-8"))["records"]
    return {record["gold_id"]: record for record in records}


def build_recipe(query: dict, *, force_gold_id: str | None = None, exclude_gold_id: str | None = None) -> dict:
    records = list(_records_by_id().values())
    if exclude_gold_id:
        records = [record for record in records if record["gold_id"] != exclude_gold_id]
    if force_gold_id:
        forced = _records_by_id()[force_gold_id]
        selection = select_gold_compositions.select_records(query, limit=1, records=[forced])
        if not selection["matches"]:
            raise ValueError(f"forced gold composition is not compatible with query: {force_gold_id}")
        record = forced
    else:
        selection = select_gold_compositions.select_records(query, limit=3, records=records)
        if not selection["matches"]:
            raise ValueError("no compatible gold composition record")
        record = _records_by_id()[selection["matches"][0]["gold_id"]]

    recipe = {
        "schema": "RESEARCH_GOLD_COMPOSITION_RECIPE_V1",
        "query": query,
        "selected_gold_id": record["gold_id"],
        "selected_reference_id": record["reference_id"],
        "source_identity": {
            "source_id": record["source_id"],
            "actual_page_number": record["actual_page_number"],
            "canonical_rendered_page_sha256": record["canonical_rendered_page_sha256"],
            "review_input_sha256": record["gold_admission_review_input_sha256"],
            "rights_reuse_boundary": record["rights_reuse_boundary"],
        },
        "composition_constraints": {
            "composition_family": record["composition_family"],
            "primary_scientific_object_role": record["primary_scientific_object_role"],
            "primary_bbox": record["primary_bbox"],
            "primary_object_area_ratio": record["primary_object_area_ratio"],
            "supporting_region_roles": record["supporting_region_roles"],
            "visual_hierarchy": record["visual_hierarchy"],
            "alignment_groups": record["alignment_groups"],
            "reading_flow": record["reading_flow"],
            "annotation_legend_caption_panel_relations": record["annotation_legend_caption_panel_relations"],
            "content_capacity": record["content_capacity"],
        },
        "audience_safe_instruction": {
            "layout_lesson": record["portable_composition_lesson"],
            "do_not_expose_internal_ids": True,
            "do_not_copy_source_pixels_or_branding": True,
        },
        "runtime_trace": {
            "runtime_selected": True,
            "actually_consumed_fields": [
                "primary_bbox",
                "visual_hierarchy",
                "alignment_groups",
                "reading_flow",
                "annotation_legend_caption_panel_relations",
                "content_capacity",
            ],
            "selection": selection,
        },
    }
    recipe["recipe_sha256"] = _stable_sha(recipe)
    return recipe


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-function", required=True)
    parser.add_argument("--scientific-object", required=True)
    parser.add_argument("--domain-family", choices=["statistics", "biostatistics", "medical_imaging", "general_research"], required=True)
    parser.add_argument("--dominant-object-type", default="")
    parser.add_argument("--evidence-type", default="")
    parser.add_argument("--density", choices=["low", "moderate", "high"], default=None)
    parser.add_argument("--panel-count", type=int, default=None)
    parser.add_argument("--force-gold-id")
    parser.add_argument("--exclude-gold-id")
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    query = {
        "page_function": args.page_function,
        "scientific_object": args.scientific_object,
        "domain_family": args.domain_family,
        "dominant_object_type": args.dominant_object_type,
        "evidence_type": args.evidence_type,
        "density": args.density,
        "panel_count": args.panel_count,
    }
    recipe = build_recipe(query, force_gold_id=args.force_gold_id, exclude_gold_id=args.exclude_gold_id)
    text = json.dumps(recipe, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
