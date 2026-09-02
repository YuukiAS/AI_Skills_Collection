#!/usr/bin/env python3
"""Runtime helpers for the scientific-rewrite skill.

The helpers keep the production route observable: a long-form rewrite is
prepared as document-level map stages, per-unit meaning/fidelity stages,
bounded example selection, unit writer packets, exact/semantic checks, a
candidate-only reader packet, and final assembly metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = ROOT / "references" / "seed-transformations.json"
RUNTIME_SCHEMA = "SCIENTIFIC_REWRITE_MULTISTAGE_RECEIPT_V1"
PACKET_SCHEMA = "SCIENTIFIC_REWRITE_STAGE_PACKET_V1"
OPENAI_API_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5.6-terra"
SEMANTIC_STATUSES = {
    "preserved",
    "narrowed",
    "broadened",
    "reversed",
    "invented",
    "omitted",
    "reattributed",
}

NUMBER_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:\.\d+)?(?:%|‰)?(?![\w.])")
DATE_RE = re.compile(r"\b(?:20\d{2}|19\d{2})(?:[-/年](?:0?[1-9]|1[0-2]))?(?:[-/月](?:0?[1-9]|[12]\d|3[01]))?日?\b")
UNIT_RE = re.compile(r"(?<![A-Za-z])\d+(?:\.\d+)?\s?(?:ms|s|min|h|GB|MB|KB|B|mm|cm|m|kg|g|mg|μm|um|%|℃|°C)\b")
CITATION_RE = re.compile(r"(?:\[[0-9,\-\s]+\]|\([A-Z][A-Za-z-]+(?: et al\.)?,\s*(?:19|20)\d{2}\)|doi:\s*10\.\S+)", re.IGNORECASE)
CODE_RE = re.compile(r"`[^`]+`")
PATH_RE = re.compile(r"(?:^|(?<=\s))(?:[./~]?[\w.-]+/[\w./-]+)(?=$|\s|[，。；,;)])")
FORMULA_RE = re.compile(r"(\$\$.*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))", re.DOTALL)
FORMAL_NAME_RE = re.compile(r"\b[A-Z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+|[A-Z][A-Za-z0-9]*)+\b")


@dataclass(frozen=True)
class RewriteUnit:
    unit_id: str
    heading: str
    start_line: int
    end_line: int
    text: str
    literal_invariants: list[dict[str, str]]


@dataclass(frozen=True)
class StageRecord:
    stage_id: str
    responsibility: str
    unit_id: str | None
    input_sha256: str
    output_sha256: str
    selected_example_ids: list[str]
    model_call: bool
    plaintext_committed: bool


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def classify_literal_role(kind: str, text: str) -> str:
    trace_like = kind in {"path"}
    trace_like = trace_like or (kind == "code" and any(token in text for token in ["/", "--", ".json", ".py", ".sh"]))
    if trace_like:
        return "relocatable-trace"
    return "inline-critical"


def unique_spans(kind: str, matches: Iterable[str]) -> list[dict[str, str]]:
    seen: set[str] = set()
    spans: list[dict[str, str]] = []
    for raw in matches:
        text = raw.strip()
        if not text or text in seen:
            continue
        seen.add(text)
        spans.append({"kind": kind, "text": text, "role": classify_literal_role(kind, text)})
    return spans


def extract_literal_invariants(text: str) -> list[dict[str, str]]:
    spans: list[dict[str, str]] = []
    spans.extend(unique_spans("formula", (m.group(0) for m in FORMULA_RE.finditer(text))))
    spans.extend(unique_spans("code", (m.group(0) for m in CODE_RE.finditer(text))))
    spans.extend(unique_spans("citation", (m.group(0) for m in CITATION_RE.finditer(text))))
    spans.extend(unique_spans("date", (m.group(0) for m in DATE_RE.finditer(text))))
    spans.extend(unique_spans("unit", (m.group(0) for m in UNIT_RE.finditer(text))))
    spans.extend(unique_spans("number", (m.group(0) for m in NUMBER_RE.finditer(text))))
    spans.extend(unique_spans("path", (m.group(0) for m in PATH_RE.finditer(text))))
    spans.extend(unique_spans("formal_name", (m.group(0) for m in FORMAL_NAME_RE.finditer(text))))
    return spans


def split_markdown_units(text: str) -> list[RewriteUnit]:
    lines = text.splitlines()
    starts: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if match:
            starts.append((index, match.group(2)))
    if not starts:
        stripped = text.strip()
        return [
            RewriteUnit(
                unit_id="unit-001",
                heading="document",
                start_line=1,
                end_line=max(1, len(lines)),
                text=stripped,
                literal_invariants=extract_literal_invariants(stripped),
            )
        ]

    units: list[RewriteUnit] = []
    for pos, (start, heading) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        unit_text = "\n".join(lines[start:end]).strip()
        units.append(
            RewriteUnit(
                unit_id=f"unit-{pos + 1:03d}",
                heading=heading,
                start_line=start + 1,
                end_line=end,
                text=unit_text,
                literal_invariants=extract_literal_invariants(unit_text),
            )
        )
    return units


def load_seed_library(path: Path = DEFAULT_LIBRARY) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("seed transformation library must be a JSON list")
    return data


def _score_example(example: dict[str, str], filters: dict[str, str]) -> tuple[int, int, str]:
    score = 0
    for key, value in filters.items():
        if not value:
            continue
        candidate = str(example.get(key, ""))
        if candidate == value:
            score += 3
        elif value in candidate or candidate in value:
            score += 1
    high_risk_penalty = 0 if example.get("fidelity_risk") == filters.get("fidelity_risk") else 1
    return (-score, high_risk_penalty, example.get("id", ""))


def select_examples(library: list[dict[str, str]], limit: int = 4, **filters: str) -> list[dict[str, str]]:
    if limit < 1:
        raise ValueError("limit must be positive")
    ranked = sorted(library, key=lambda item: _score_example(item, filters))
    selected: list[dict[str, str]] = []
    seen_functions: set[str] = set()
    for item in ranked:
        function = item.get("discourse_function", "")
        if function in seen_functions and len(selected) < min(3, limit):
            continue
        selected.append(item)
        seen_functions.add(function)
        if len(selected) == limit:
            break
    if len(selected) < min(limit, len(ranked)):
        selected_ids = {item.get("id") for item in selected}
        for item in ranked:
            if item.get("id") not in selected_ids:
                selected.append(item)
                if len(selected) == limit:
                    break
    return selected


def verify_exact(
    source: str,
    candidate: str,
    ledger: list[dict[str, str]] | None = None,
    *,
    reader_core: str | None = None,
) -> dict[str, object]:
    invariants = ledger if ledger is not None else extract_literal_invariants(source)
    missing = []
    misplaced_inline = []
    core = candidate if reader_core is None else reader_core
    for invariant in invariants:
        text = invariant["text"]
        if text not in candidate:
            missing.append(invariant)
        elif invariant.get("role") == "inline-critical" and text not in core:
            misplaced_inline.append(invariant)
    return {
        "ok": not missing and not misplaced_inline,
        "checked_count": len(invariants),
        "missing": missing,
        "misplaced_inline": misplaced_inline,
    }


def document_map(text: str, units: list[RewriteUnit]) -> dict[str, Any]:
    headings = [unit.heading for unit in units]
    literals = extract_literal_invariants(text)
    return {
        "audience": "technically trained reader who has not followed the repository audit history",
        "document_purpose": "meaning-preserving reader-facing rewrite of an existing scientific or technical document",
        "section_roles": [{"unit_id": unit.unit_id, "heading": unit.heading} for unit in units],
        "terminology": sorted({span["text"] for span in literals if span["kind"] == "formal_name"}),
        "cross_section_dependencies": headings,
        "major_claims": _sentences_with_markers(text, ("说明", "显示", "支持", "不能", "需要", "结果", "比较"))[:12],
        "caveats_uncertainty": _sentences_with_markers(text, ("可能", "限制", "不确定", "不能", "尚未", "negative", "caveat"))[:12],
        "major_conclusions": _sentences_with_markers(text, ("因此", "所以", "结论", "下一步", "GO", "STOP"))[:8],
        "literal_protected_inventory": literals,
    }


def _sentences_with_markers(text: str, markers: tuple[str, ...]) -> list[str]:
    sentences = [part.strip() for part in re.split(r"(?<=[。！？.!?])\s+|\n+", text) if part.strip()]
    selected = [part for part in sentences if any(marker in part for marker in markers)]
    return selected or sentences[: min(5, len(sentences))]


def infer_unit_filters(unit: RewriteUnit) -> dict[str, str]:
    lowered = unit.text.lower()
    if any(token in lowered for token in ["结果", "dice", "hd95", "gap", "pass", "fail"]):
        discourse = "result-interpretation"
        problem = "log-narration"
        risk = "high"
    elif any(token in lowered for token in ["比较", "vs", "fedfisher", "fedlpa", "odal", "baseline"]):
        discourse = "comparison"
        problem = "unclear-comparator"
        risk = "high"
    elif any(token in lowered for token in ["限制", "不能", "不确定", "可能", "caveat"]):
        discourse = "caveat"
        problem = "conclusion-upgrade-risk"
        risk = "high"
    elif any(token in lowered for token in ["路径", "commit", "checkpoint", "audit", "provenance"]):
        discourse = "method-explanation"
        problem = "workflow-language"
        risk = "medium"
    else:
        discourse = "transition"
        problem = "reader-effort"
        risk = "medium"
    return {
        "scene": "scientific-report",
        "discourse_function": discourse,
        "rewrite_problem": problem,
        "fidelity_risk": risk,
        "register": "formal-technical",
    }


def meaning_card(unit: RewriteUnit, doc_map: dict[str, Any], previous_heading: str = "", next_heading: str = "") -> dict[str, Any]:
    literals = unit.literal_invariants
    return {
        "unit_id": unit.unit_id,
        "audience": doc_map["audience"],
        "purpose": f"rewrite the argument unit headed {unit.heading!r} without changing its scientific meaning",
        "claims": _sentences_with_markers(unit.text, ("说明", "显示", "支持", "不能", "需要", "结果", "比较"))[:6],
        "evidence_results": _sentences_with_markers(unit.text, ("=", "%", "seed", "Dice", "HD95", "gap", "结果", "证据"))[:6],
        "conditions_comparators": _sentences_with_markers(unit.text, ("vs", "相比", "比较", "条件", "baseline", "FedFisher", "FedLPA", "ODAL"))[:6],
        "caveats_uncertainty_negative_findings": _sentences_with_markers(unit.text, ("可能", "限制", "不能", "不确定", "尚未", "未观察"))[:6],
        "attribution": _sentences_with_markers(unit.text, ("本文", "已有", "原文", "报告", "观察"))[:4],
        "literal_protected": literals,
        "terminology": sorted({span["text"] for span in literals if span["kind"] == "formal_name"}),
        "previous_next_relation": {"previous": previous_heading, "next": next_heading},
        "reader_takeaway": _reader_takeaway(unit),
    }


def _reader_takeaway(unit: RewriteUnit) -> str:
    clean_heading = re.sub(r"^[#\s]+", "", unit.heading).strip() or unit.unit_id
    return f"读者应理解 {clean_heading} 这一部分的判断、证据和限制，而不是先解码内部流程标签。"


def coverage_check(unit: RewriteUnit, card: dict[str, Any]) -> dict[str, Any]:
    card_text = canonical_json(card)
    important = []
    for sentence in _sentences_with_markers(unit.text, ("=", "%", "不能", "可能", "限制", "比较", "结果", "GO", "STOP")):
        important.append({"text": sentence, "covered": sentence in card_text or any(token in card_text for token in extract_keywords(sentence))})
    missing = [item for item in important if not item["covered"]]
    return {"ok": not missing, "important_count": len(important), "missing": missing}


def extract_keywords(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}|[0-9]+(?:\.[0-9]+)?%?", text)
    return tokens[:8]


def writer_packet(
    unit: RewriteUnit,
    doc_map: dict[str, Any],
    card: dict[str, Any],
    examples: list[dict[str, str]],
    previous_tail: str,
    next_preview: str,
) -> dict[str, Any]:
    return {
        "schema": PACKET_SCHEMA,
        "stage": "unit-writer",
        "unit_id": unit.unit_id,
        "compact_document_map": {
            "audience": doc_map["audience"],
            "document_purpose": doc_map["document_purpose"],
            "section_roles": doc_map["section_roles"],
            "major_claims": doc_map["major_claims"][:5],
            "caveats_uncertainty": doc_map["caveats_uncertainty"][:5],
        },
        "current_original_unit": unit.text,
        "meaning_card": card,
        "fidelity_ledger": {
            "literal_items": unit.literal_invariants,
            "semantic_status_values": sorted(SEMANTIC_STATUSES),
            "critical_violations_allowed": 0,
        },
        "previous_rewritten_tail": previous_tail[-600:],
        "next_source_preview": next_preview[:600],
        "selected_transformations": examples,
        "selected_example_ids": [item["id"] for item in examples],
        "examples_are_factual_sources": False,
    }


def deterministic_unit_rewrite(unit: RewriteUnit) -> dict[str, str]:
    trace_lines = []
    core_lines = []
    for line in unit.text.splitlines():
        line_literals = extract_literal_invariants(line)
        if line_literals and all(item["role"] == "relocatable-trace" for item in line_literals):
            trace_lines.append(line)
        else:
            core_lines.append(line)
    reader_core = "\n".join(core_lines).strip() or unit.text.strip()
    trace_appendix = "\n".join(trace_lines).strip()
    return {"reader_core": reader_core, "technical_trace": trace_appendix}


def semantic_audit(source: str, candidate: str) -> dict[str, Any]:
    missing_literals = verify_exact(source, candidate)["missing"]
    status = "preserved" if not missing_literals else "omitted"
    critical = [
        {
            "status": "omitted",
            "source_evidence": item["text"],
            "candidate_evidence": "",
            "reason": "literal invariant missing from candidate",
        }
        for item in missing_literals
    ]
    return {
        "statuses": [status],
        "critical_violations": critical,
        "critical_violation_count": len(critical),
        "allowed_status_values": sorted(SEMANTIC_STATUSES),
    }


def reader_review_packet(candidate: str, audience: str) -> dict[str, Any]:
    return {
        "schema": PACKET_SCHEMA,
        "stage": "candidate-only-reader-review",
        "source_visible": False,
        "audience": audience,
        "candidate_sha256": sha256_text(candidate),
        "questions": [
            "what problem is being studied",
            "what current evidence means",
            "what remains uncertain",
            "why the next comparison or experiment is needed",
            "what result would support GO or STOP",
        ],
    }


def stage_record(
    *,
    stage_id: str,
    responsibility: str,
    unit_id: str | None,
    input_payload: Any,
    output_payload: Any,
    selected_example_ids: list[str] | None = None,
    model_call: bool = False,
) -> StageRecord:
    return StageRecord(
        stage_id=stage_id,
        responsibility=responsibility,
        unit_id=unit_id,
        input_sha256=sha256_text(canonical_json(input_payload)),
        output_sha256=sha256_text(canonical_json(output_payload)),
        selected_example_ids=selected_example_ids or [],
        model_call=model_call,
        plaintext_committed=False,
    )


def call_stage_model(
    *,
    driver: str,
    prompt: str,
    payload: Any,
    model: str,
    api_key: str,
) -> str:
    if driver != "openai-responses":
        return ""
    return call_openai_text(prompt, canonical_json(payload), model=model, api_key=api_key).strip()


def build_openai_request(prompt: str, source: str, *, model: str) -> dict[str, Any]:
    return {
        "model": model,
        "store": False,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_text", "text": source},
                ],
            }
        ],
    }


def call_openai_text(
    prompt: str,
    source: str,
    *,
    model: str,
    api_key: str,
    timeout: float = 120.0,
    opener: Callable[..., Any] | None = None,
) -> str:
    if not api_key:
        raise RuntimeError("OpenAI API key unavailable for staged scientific rewrite")
    request_payload = build_openai_request(prompt, source, model=model)
    body = canonical_json(request_payload).encode("utf-8")
    request = urllib.request.Request(
        OPENAI_API_URL,
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    urlopen = urllib.request.urlopen if opener is None else opener
    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"OpenAI staged rewrite failed closed: HTTP {getattr(exc, 'code', 'UNKNOWN')}") from exc
    status = payload.get("status")
    if status and status != "completed":
        raise RuntimeError(f"OpenAI staged rewrite did not complete: {status}")
    output = payload.get("output_text")
    if isinstance(output, str) and output.strip():
        return output
    for item in payload.get("output", []):
        for content in item.get("content", []):
            text = content.get("text")
            if isinstance(text, str) and text.strip():
                return text
    raise RuntimeError("OpenAI staged rewrite returned empty text")


def run_multistage(
    source: str,
    *,
    driver: str = "template",
    model: str = DEFAULT_MODEL,
    api_key: str = "",
    stage_dir: Path | None = None,
    smoke_role: str = "",
) -> dict[str, Any]:
    if driver not in {"template", "openai-responses"}:
        raise ValueError("driver must be template or openai-responses")
    units = split_markdown_units(source)
    library = load_seed_library()
    records: list[StageRecord] = []
    packets: list[dict[str, Any]] = []
    doc_map = document_map(source, units)
    doc_map_model_output = call_stage_model(
        driver=driver,
        prompt=(
            "Map the document purpose, intended reader, argument-unit roles, key terms, "
            "claims, caveats and decision points. Do not rewrite any prose."
        ),
        payload={"source": source, "unit_index": [asdict(unit) for unit in units]},
        model=model,
        api_key=api_key,
    )
    records.append(
        stage_record(
            stage_id="document-map",
            responsibility="map document purpose, audience, section roles, terminology, claims and caveats; no prose rewrite",
            unit_id=None,
            input_payload={"source_sha256": sha256_text(source)},
            output_payload={
                "map": doc_map,
                "model_output_sha256": sha256_text(doc_map_model_output) if doc_map_model_output else "",
                "model_output_chars": len(doc_map_model_output),
            },
            model_call=bool(doc_map_model_output),
        )
    )
    rewritten_units: list[dict[str, str]] = []
    previous_tail = ""
    for index, unit in enumerate(units):
        previous_heading = units[index - 1].heading if index else ""
        next_heading = units[index + 1].heading if index + 1 < len(units) else ""
        card = meaning_card(unit, doc_map, previous_heading, next_heading)
        coverage = coverage_check(unit, card)
        meaning_model_output = call_stage_model(
            driver=driver,
            prompt=(
                "Create a Meaning Card and Fidelity Ledger for this single argument unit. "
                "Preserve claims, caveats, comparators, quantitative literals and decision logic. Do not rewrite the unit."
            ),
            payload={"unit": asdict(unit), "document_map": doc_map},
            model=model,
            api_key=api_key,
        )
        records.append(
            stage_record(
                stage_id=f"{unit.unit_id}-meaning-card",
                responsibility="derive Meaning Card and Fidelity Ledger for one argument unit; no prose rewrite",
                unit_id=unit.unit_id,
                input_payload={"unit": asdict(unit), "document_map_sha256": sha256_text(canonical_json(doc_map))},
                output_payload={
                    "meaning_card": card,
                    "coverage": coverage,
                    "model_output_sha256": sha256_text(meaning_model_output) if meaning_model_output else "",
                    "model_output_chars": len(meaning_model_output),
                },
                model_call=bool(meaning_model_output),
            )
        )
        filters = infer_unit_filters(unit)
        examples = select_examples(library, limit=4, **filters)
        records.append(
            stage_record(
                stage_id=f"{unit.unit_id}-example-selection",
                responsibility="select 2-4 positive transformations by metadata; never inject the full seed library",
                unit_id=unit.unit_id,
                input_payload={"filters": filters, "library_size": len(library)},
                output_payload={"selected_example_ids": [item["id"] for item in examples]},
                selected_example_ids=[item["id"] for item in examples],
            )
        )
        next_preview = units[index + 1].text if index + 1 < len(units) else ""
        packet = writer_packet(unit, doc_map, card, examples, previous_tail, next_preview)
        packets.append(packet)
        if stage_dir:
            write_json(stage_dir / f"{unit.unit_id}.writer-packet.json", packet)
        if driver == "openai-responses":
            prompt = (
                "Rewrite only the current argument unit into natural Chinese scientific prose. "
                "Preserve all facts, numbers, formulas, citations, formal names, caveats, comparators, "
                "attribution and conclusion strength. Use the selected transformations only as style-operation examples. "
                "Return only the rewritten unit."
            )
            rewritten_text = call_openai_text(prompt, canonical_json(packet), model=model, api_key=api_key)
            unit_result = {"reader_core": rewritten_text.strip(), "technical_trace": ""}
        else:
            unit_result = deterministic_unit_rewrite(unit)
        combined_unit = "\n\n".join(part for part in [unit_result["reader_core"], unit_result["technical_trace"]] if part)
        exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=unit_result["reader_core"])
        semantic = semantic_audit(unit.text, combined_unit)
        if not exact["ok"] or semantic["critical_violation_count"]:
            pre_repair_exact = exact
            pre_repair_semantic = semantic
            repair_model_output = call_stage_model(
                driver=driver,
                prompt=(
                    "Repair only the current rewritten unit to fix the exact literal or semantic violations. "
                    "Do not add new claims and do not rewrite unrelated units."
                ),
                payload={"unit": asdict(unit), "candidate": combined_unit, "exact": exact, "semantic": semantic},
                model=model,
                api_key=api_key,
            )
            records.append(
                stage_record(
                    stage_id=f"{unit.unit_id}-targeted-repair",
                    responsibility="repair only the affected unit after exact or semantic violation",
                    unit_id=unit.unit_id,
                    input_payload={"exact": exact, "semantic": semantic},
                    output_payload={
                        "repair_status": "required",
                        "model_output_sha256": sha256_text(repair_model_output) if repair_model_output else "",
                        "model_output_chars": len(repair_model_output),
                    },
                    model_call=bool(repair_model_output),
                )
            )
            if repair_model_output:
                unit_result = {"reader_core": repair_model_output.strip(), "technical_trace": ""}
                combined_unit = unit_result["reader_core"]
                exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=unit_result["reader_core"])
                semantic = semantic_audit(unit.text, combined_unit)
                records.append(
                    stage_record(
                        stage_id=f"{unit.unit_id}-post-repair-audit",
                        responsibility="re-audit the repaired current unit before assembly",
                        unit_id=unit.unit_id,
                        input_payload={
                            "pre_repair_exact": pre_repair_exact,
                            "pre_repair_semantic": pre_repair_semantic,
                            "repair_output_sha256": sha256_text(repair_model_output),
                        },
                        output_payload={"exact": exact, "semantic": semantic},
                        model_call=False,
                    )
                )
        records.append(
            stage_record(
                stage_id=f"{unit.unit_id}-writer",
                responsibility="rewrite one argument unit from original source plus Meaning Card and selected examples",
                unit_id=unit.unit_id,
                input_payload=packet,
                output_payload=unit_result,
                selected_example_ids=[item["id"] for item in examples],
                model_call=driver == "openai-responses",
            )
        )
        audit_model_output = call_stage_model(
            driver=driver,
            prompt=(
                "Audit the current rewritten unit against the source unit for exact literal preservation "
                "and semantic relation status. Use only allowed statuses and report critical violations."
            ),
            payload={"source_unit": unit.text, "candidate_unit": combined_unit, "exact": exact, "semantic": semantic},
            model=model,
            api_key=api_key,
        )
        records.append(
            stage_record(
                stage_id=f"{unit.unit_id}-literal-semantic-audit",
                responsibility="verify exact literal preservation and semantic claim/relation status for the current unit",
                unit_id=unit.unit_id,
                input_payload={"source_sha256": sha256_text(unit.text), "candidate_sha256": sha256_text(combined_unit)},
                output_payload={
                    "exact": exact,
                    "semantic": semantic,
                    "model_output_sha256": sha256_text(audit_model_output) if audit_model_output else "",
                    "model_output_chars": len(audit_model_output),
                },
                model_call=bool(audit_model_output),
            )
        )
        rewritten_units.append(unit_result)
        previous_tail = unit_result["reader_core"]
    reader_core = "\n\n".join(item["reader_core"] for item in rewritten_units if item["reader_core"]).strip()
    traces = "\n\n".join(item["technical_trace"] for item in rewritten_units if item["technical_trace"]).strip()
    candidate = reader_core
    if traces:
        candidate = f"{reader_core}\n\n## Technical / Evidence Appendix\n\n{traces}\n"
    reader_packet = reader_review_packet(candidate, doc_map["audience"])
    if stage_dir:
        write_json(stage_dir / "candidate-only-reader-review.packet.json", reader_packet)
    reader_model_output = call_stage_model(
        driver=driver,
        prompt=(
            "Review this candidate text only for reader comprehension. The source text is intentionally not visible. "
            "Answer whether the candidate explains the problem, evidence, uncertainty, next comparison and GO/STOP condition."
        ),
        payload=reader_packet,
        model=model,
        api_key=api_key,
    )
    records.append(
        stage_record(
            stage_id="candidate-only-reader-review",
            responsibility="review candidate only against reader questions; source is not visible",
            unit_id=None,
            input_payload=reader_packet,
            output_payload={
                "source_visible": False,
                "candidate_sha256": sha256_text(candidate),
                "model_output_sha256": sha256_text(reader_model_output) if reader_model_output else "",
                "model_output_chars": len(reader_model_output),
            },
            model_call=bool(reader_model_output),
        )
    )
    assembly_model_output = call_stage_model(
        driver=driver,
        prompt=(
            "Check final assembly coherence across rewritten units, transitions and terminology. "
            "Do not rewrite the whole document; report only assembly issues if any."
        ),
        payload={
            "unit_count": len(units),
            "candidate_sha256": sha256_text(candidate),
            "unit_candidate_hashes": [sha256_text(item["reader_core"]) for item in rewritten_units],
        },
        model=model,
        api_key=api_key,
    )
    records.append(
        stage_record(
            stage_id="final-assembly-coherence",
            responsibility="final assembly of rewritten units and transition/terminology check without whole-document free rewrite",
            unit_id=None,
            input_payload={"unit_count": len(units), "candidate_sha256": sha256_text(candidate)},
            output_payload={
                "reader_core_sha256": sha256_text(reader_core),
                "technical_trace_sha256": sha256_text(traces),
                "model_output_sha256": sha256_text(assembly_model_output) if assembly_model_output else "",
                "model_output_chars": len(assembly_model_output),
            },
            model_call=bool(assembly_model_output),
        )
    )
    receipt = {
        "schema": RUNTIME_SCHEMA,
        "runtime": "scientific-rewrite.multistage.v1",
        "driver": driver,
        "model": model if driver == "openai-responses" else "",
        "store": False,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "smoke_role": smoke_role,
        "source_sha256": sha256_text(source),
        "candidate_sha256": sha256_text(candidate),
        "unit_count": len(units),
        "stage_count": len(records),
        "model_call_count": sum(1 for item in records if item.model_call),
        "whole_document_writer_call": False,
        "seed_library_size": len(library),
        "max_examples_per_unit": max((len(packet["selected_example_ids"]) for packet in packets), default=0),
        "full_seed_library_injected": any(len(packet["selected_example_ids"]) == len(library) for packet in packets),
        "stage_records": [asdict(item) for item in records],
        "private_plaintext_committed": False,
    }
    return {"candidate": candidate, "receipt": receipt, "packets": packets}


def command_prepare(args: argparse.Namespace) -> None:
    text = load_text(Path(args.source))
    units = split_markdown_units(text)
    print(json.dumps({"units": [asdict(unit) for unit in units]}, ensure_ascii=False, indent=2))


def command_select_examples(args: argparse.Namespace) -> None:
    library = load_seed_library(Path(args.library))
    selected = select_examples(
        library,
        limit=args.limit,
        scene=args.scene,
        discourse_function=args.discourse_function,
        rewrite_problem=args.rewrite_problem,
        fidelity_risk=args.fidelity_risk,
        register=args.register,
    )
    print(json.dumps({"examples": selected}, ensure_ascii=False, indent=2))


def command_verify_exact(args: argparse.Namespace) -> None:
    source = load_text(Path(args.source))
    candidate = load_text(Path(args.candidate))
    ledger = None
    if args.ledger:
        ledger = json.loads(Path(args.ledger).read_text(encoding="utf-8"))
    report = verify_exact(source, candidate, ledger)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["ok"]:
        raise SystemExit(1)


def command_run_staged(args: argparse.Namespace) -> None:
    source = load_text(Path(args.source))
    api_key = (
        os.environ.get("OPENAI_TEXT_TRANSFORM_API_KEY", "")
        or os.environ.get("OPENAI_REVIEW_API_KEY", "")
        or os.environ.get("OPENAI_API_KEY", "")
    )
    stage_dir = Path(args.stage_dir) if args.stage_dir else None
    result = run_multistage(
        source,
        driver=args.driver,
        model=args.model,
        api_key=api_key,
        stage_dir=stage_dir,
        smoke_role=args.smoke_role,
    )
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result["candidate"], encoding="utf-8")
    write_json(Path(args.receipt), result["receipt"])
    if args.print_receipt:
        print(json.dumps(result["receipt"], ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare")
    prepare.add_argument("--source", required=True)
    prepare.set_defaults(func=command_prepare)

    select = subparsers.add_parser("select-examples")
    select.add_argument("--library", default=str(DEFAULT_LIBRARY))
    select.add_argument("--scene", default="")
    select.add_argument("--discourse-function", default="")
    select.add_argument("--rewrite-problem", default="")
    select.add_argument("--fidelity-risk", default="")
    select.add_argument("--register", default="")
    select.add_argument("--limit", type=int, default=4)
    select.set_defaults(func=command_select_examples)

    verify = subparsers.add_parser("verify-exact")
    verify.add_argument("--source", required=True)
    verify.add_argument("--candidate", required=True)
    verify.add_argument("--ledger")
    verify.set_defaults(func=command_verify_exact)

    staged = subparsers.add_parser("run-staged")
    staged.add_argument("--source", required=True)
    staged.add_argument("--output", required=True)
    staged.add_argument("--receipt", required=True)
    staged.add_argument("--stage-dir")
    staged.add_argument("--driver", choices=["template", "openai-responses"], default="template")
    staged.add_argument("--model", default=os.environ.get("OPENAI_TEXT_TRANSFORM_MODEL", DEFAULT_MODEL))
    staged.add_argument("--smoke-role", default="")
    staged.add_argument("--print-receipt", action="store_true")
    staged.set_defaults(func=command_run_staged)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
