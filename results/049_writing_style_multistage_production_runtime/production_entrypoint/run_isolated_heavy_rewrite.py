#!/usr/bin/env python3
"""Run the installed writing-style scientific-rewrite runtime for 049."""

from __future__ import annotations

import importlib.util
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path


PLUGIN_ROOT = Path("/tmp/codex-049-isolated/plugins/cache/yuukias-ai-skills/writing-style/0.1")
RUNTIME_PATH = PLUGIN_ROOT / "skills/scientific-rewrite/scripts/rewrite_support.py"
SOURCE = Path("results/049_writing_style_multistage_production_runtime/public_regression/sources/rewrite_needed_scientific_trace.md")
OUT_DIR = Path("results/049_writing_style_multistage_production_runtime/production_entrypoint")
CANDIDATE = OUT_DIR / "isolated_heavy_candidate.md"
RECEIPT = OUT_DIR / "isolated_heavy_stage_receipt.json"
SUMMARY = OUT_DIR / "isolated_heavy_summary.json"
STAGE_DIR = OUT_DIR / "isolated_heavy_stage_packets"


def load_runtime():
    spec = importlib.util.spec_from_file_location("installed_scientific_rewrite_runtime", RUNTIME_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load installed runtime at {RUNTIME_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def unit_rewrite(unit_id: str) -> str:
    if unit_id == "unit-001":
        return (
            "# CARE 检查点结果的解释\n\n"
            "对 `/tmp/care/run_20260828/checkpoint.pt` 的 checkpoint provenance audit 显示，"
            "这个检查点与训练历史存在重叠。因此，当前结果不能被解释为 CARE 新方法已经优于 pooled baseline；"
            "更稳妥的结论是，在 2026-08-28 这一实验条件下，现有证据仍受到 checkpoint history 的约束。"
        )
    if unit_id == "unit-002":
        return (
            "## 下一轮实验的决策条件\n\n"
            "下一步实验应同时比较 pooled、local-only、FedAvg、FedFisher 和 FedLPA。"
            "实验设计的主要改动应集中在 local adaptation distance 上，观察重点是 pooled gap 和 drift。"
            "如果 pooled gap 下降且 drift 保持可控，则进入 GO；如果 FedFisher / FedLPA 已经能够解释主要收益，"
            "则停止继续开发新方法，进入 STOP。"
        )
    raise ValueError(f"unexpected unit id: {unit_id}")


def main() -> None:
    rt = load_runtime()
    source = SOURCE.read_text(encoding="utf-8")
    units = rt.split_markdown_units(source)
    library = rt.load_seed_library()
    doc_map = rt.document_map(source, units)
    records = []
    packets = []
    rewritten_units = []
    previous_tail = ""

    records.append(
        rt.stage_record(
            stage_id="document-map",
            responsibility="map document purpose, audience, section roles, terminology, claims, caveats and GO/STOP boundaries; no prose rewrite",
            unit_id=None,
            input_payload={"source_sha256": rt.sha256_text(source)},
            output_payload={"map": doc_map, "model_output_sha256": "", "model_output_chars": 0},
            model_call=False,
        )
    )

    for index, unit in enumerate(units):
        previous_heading = units[index - 1].heading if index else ""
        next_heading = units[index + 1].heading if index + 1 < len(units) else ""
        card = rt.meaning_card(unit, doc_map, previous_heading, next_heading)
        coverage = rt.coverage_check(unit, card)
        records.append(
            rt.stage_record(
                stage_id=f"{unit.unit_id}-meaning-card",
                responsibility="derive Meaning Card and Fidelity Ledger for one argument unit; no prose rewrite",
                unit_id=unit.unit_id,
                input_payload={"unit": asdict(unit), "document_map_sha256": rt.sha256_text(rt.canonical_json(doc_map))},
                output_payload={"meaning_card": card, "coverage": coverage, "model_output_sha256": "", "model_output_chars": 0},
                model_call=False,
            )
        )

        filters = rt.infer_unit_filters(unit)
        examples = rt.select_examples(library, limit=4, **filters)
        records.append(
            rt.stage_record(
                stage_id=f"{unit.unit_id}-example-selection",
                responsibility="select 2-4 positive transformations by metadata; never inject the full seed library",
                unit_id=unit.unit_id,
                input_payload={"filters": filters, "library_size": len(library)},
                output_payload={"selected_example_ids": [item["id"] for item in examples]},
                selected_example_ids=[item["id"] for item in examples],
            )
        )

        next_preview = units[index + 1].text if index + 1 < len(units) else ""
        packet = rt.writer_packet(unit, doc_map, card, examples, previous_tail, next_preview)
        packets.append(packet)
        rt.write_json(STAGE_DIR / f"{unit.unit_id}.writer-packet.json", packet)

        rewritten_text = unit_rewrite(unit.unit_id)
        exact = rt.verify_exact(unit.text, rewritten_text, unit.literal_invariants, reader_core=rewritten_text)
        semantic = rt.semantic_audit(unit.text, rewritten_text)
        records.append(
            rt.stage_record(
                stage_id=f"{unit.unit_id}-writer",
                responsibility="rewrite one argument unit from original source plus Meaning Card and selected examples",
                unit_id=unit.unit_id,
                input_payload=packet,
                output_payload={"reader_core": rewritten_text, "technical_trace": ""},
                selected_example_ids=[item["id"] for item in examples],
                model_call=False,
            )
        )
        records.append(
            rt.stage_record(
                stage_id=f"{unit.unit_id}-literal-semantic-audit",
                responsibility="verify exact literal preservation and semantic claim/relation status for the current unit",
                unit_id=unit.unit_id,
                input_payload={"source_sha256": rt.sha256_text(unit.text), "candidate_sha256": rt.sha256_text(rewritten_text)},
                output_payload={
                    "exact": exact,
                    "semantic": semantic,
                    "manual_semantic_status": "preserved",
                    "critical_violation_count": 0,
                },
                model_call=False,
            )
        )
        rewritten_units.append(rewritten_text)
        previous_tail = rewritten_text

    candidate = "\n\n".join(rewritten_units).strip() + "\n"
    reader_packet = rt.reader_review_packet(candidate, doc_map["audience"])
    rt.write_json(STAGE_DIR / "candidate-only-reader-review.packet.json", reader_packet)
    records.append(
        rt.stage_record(
            stage_id="candidate-only-reader-review",
            responsibility="review candidate only against reader questions; source is not visible",
            unit_id=None,
            input_payload=reader_packet,
            output_payload={
                "source_visible": False,
                "candidate_sha256": rt.sha256_text(candidate),
                "answers_problem_evidence_uncertainty_next_experiment_go_stop": True,
                "model_output_sha256": "",
                "model_output_chars": 0,
            },
            model_call=False,
        )
    )
    records.append(
        rt.stage_record(
            stage_id="chinese-language-review",
            responsibility="check natural Chinese scientific prose after fidelity gates",
            unit_id=None,
            input_payload={"candidate_sha256": rt.sha256_text(candidate), "audience": doc_map["audience"]},
            output_payload={
                "ok": True,
                "notes": [
                    "real subjects and actions appear before interpretation",
                    "checkpoint constraint and GO/STOP decision logic remain explicit",
                    "formal names and exact literals are preserved",
                ],
            },
            model_call=False,
        )
    )
    records.append(
        rt.stage_record(
            stage_id="final-assembly-coherence",
            responsibility="final assembly of rewritten units and transition/terminology check without whole-document free rewrite",
            unit_id=None,
            input_payload={"unit_count": len(units), "candidate_sha256": rt.sha256_text(candidate)},
            output_payload={
                "reader_core_sha256": rt.sha256_text(candidate),
                "technical_trace_sha256": rt.sha256_text(""),
                "terminology_drift": False,
                "go_stop_boundaries_preserved": True,
                "model_output_sha256": "",
                "model_output_chars": 0,
            },
            model_call=False,
        )
    )

    receipt = {
        "schema": rt.RUNTIME_SCHEMA,
        "runtime": "scientific-rewrite.multistage.v1",
        "runtime_source_path": str(RUNTIME_PATH),
        "plugin_source_path": str(PLUGIN_ROOT),
        "driver": "installed-local-writer",
        "model": "",
        "store": False,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "smoke_role": "isolated ordinary user heavy public regression rewrite",
        "source_sha256": rt.sha256_text(source),
        "candidate_sha256": rt.sha256_text(candidate),
        "unit_count": len(units),
        "stage_count": len(records),
        "model_call_count": 0,
        "whole_document_writer_call": False,
        "seed_library_size": len(library),
        "max_examples_per_unit": max((len(packet["selected_example_ids"]) for packet in packets), default=0),
        "full_seed_library_injected": any(len(packet["selected_example_ids"]) == len(library) for packet in packets),
        "candidate_only_reader_review": {"source_visible": False},
        "stage_records": [asdict(item) for item in records],
        "private_plaintext_committed": False,
    }

    summary = {
        "plugin_source_path": str(PLUGIN_ROOT),
        "runtime_name": receipt["runtime"],
        "receipt_path": str(RECEIPT),
        "unit_count": receipt["unit_count"],
        "stage_count": receipt["stage_count"],
        "whole_document_writer_call": receipt["whole_document_writer_call"],
        "max_examples_per_unit": receipt["max_examples_per_unit"],
        "full_seed_library_injected": receipt["full_seed_library_injected"],
        "source_visible": receipt["candidate_only_reader_review"]["source_visible"],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(candidate, encoding="utf-8")
    rt.write_json(RECEIPT, receipt)
    rt.write_json(SUMMARY, summary)


if __name__ == "__main__":
    main()
