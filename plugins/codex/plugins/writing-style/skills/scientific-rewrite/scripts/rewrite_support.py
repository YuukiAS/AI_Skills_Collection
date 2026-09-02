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
RUNTIME_SCHEMA = "SCIENTIFIC_REWRITE_MULTISTAGE_RECEIPT_V2"
PACKET_SCHEMA = "SCIENTIFIC_REWRITE_STAGE_PACKET_V1"
OPENAI_API_URL = "https://api.openai.com/v1/responses"
DEFAULT_MODEL = "gpt-5.6-terra"
UNIT_REPAIR_ROUNDS = 3
ASSEMBLY_REPAIR_ROUNDS = 3
SEMANTIC_STATUSES = {
    "preserved",
    "narrowed",
    "broadened",
    "reversed",
    "invented",
    "omitted",
    "reattributed",
}
SEMANTIC_STATUS_ALIASES = {
    "accurate": "preserved",
    "covered": "preserved",
    "kept": "preserved",
    "ok": "preserved",
    "resolved": "preserved",
    "retained": "preserved",
    "supported": "preserved",
    "unchanged": "preserved",
    "partial": "narrowed",
    "partially_preserved": "narrowed",
    "understated": "narrowed",
    "weakened": "narrowed",
    "expanded": "broadened",
    "overstated": "broadened",
    "contradicted": "reversed",
    "added": "invented",
    "hallucinated": "invented",
    "unsupported": "invented",
    "dropped": "omitted",
    "missing": "omitted",
    "not_present": "omitted",
    "changed_attribution": "reattributed",
    "misattributed": "reattributed",
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
class SourceSpan:
    span_id: str
    start_line: int
    end_line: int
    text: str
    heading_context: str


@dataclass(frozen=True)
class RewriteUnit:
    unit_id: str
    heading: str
    start_line: int
    end_line: int
    text: str
    source_span_ids: list[str]
    argument_role: str
    why_these_spans_belong_together: str
    literal_invariants: list[dict[str, str]]


@dataclass
class StageRecord:
    stage_id: str
    responsibility: str
    unit_id: str | None
    input_sha256: str
    output_sha256: str
    output_identity: str
    downstream_consumers: list[dict[str, str]]
    selected_example_ids: list[str]
    model_call: bool
    plaintext_committed: bool
    unused_output: bool
    terminal_output: bool


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


def build_source_spans(text: str) -> list[SourceSpan]:
    lines = text.splitlines()
    spans: list[SourceSpan] = []
    current: list[str] = []
    start_line = 1
    heading_context = "document"
    for index, line in enumerate(lines, start=1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            if current:
                span_text = "\n".join(current).strip()
                spans.append(
                    SourceSpan(
                        span_id=f"p{len(spans) + 1:03d}",
                        start_line=start_line,
                        end_line=index - 1,
                        text=span_text,
                        heading_context=heading_context,
                    )
                )
                current = []
            heading_context = match.group(2).strip()
            current = [line]
            start_line = index
            continue
        if line.strip():
            if not current:
                start_line = index
            current.append(line)
        elif current:
            span_text = "\n".join(current).strip()
            spans.append(
                SourceSpan(
                    span_id=f"p{len(spans) + 1:03d}",
                    start_line=start_line,
                    end_line=index - 1,
                    text=span_text,
                    heading_context=heading_context,
                )
            )
            current = []
    if current:
        span_text = "\n".join(current).strip()
        spans.append(
            SourceSpan(
                span_id=f"p{len(spans) + 1:03d}",
                start_line=start_line,
                end_line=max(start_line, len(lines)),
                text=span_text,
                heading_context=heading_context,
            )
        )
    if not spans and text.strip():
        stripped = text.strip()
        spans.append(
            SourceSpan(
                span_id="p001",
                start_line=1,
                end_line=max(1, len(lines)),
                text=stripped,
                heading_context="document",
            )
        )
    return spans


def _semantic_role_for_text(text: str) -> str:
    lowered = text.lower()
    if any(token in lowered for token in ["go", "stop", "下一步", "实验", "run"]):
        return "decision-or-next-step"
    if any(token in lowered for token in ["fedfisher", "fedlpa", "odal", "比较", "vs", "baseline"]):
        return "comparison"
    if any(token in lowered for token in ["checkpoint", "provenance", "路径", "commit", "audit"]):
        return "evidence-trace-interpretation"
    if any(token in lowered for token in ["不能", "限制", "不确定", "可能", "caveat"]):
        return "caveat-or-uncertainty"
    if any(token in lowered for token in ["=", "dice", "hd95", "结果", "显示", "说明"]):
        return "evidence-or-result"
    return "claim-explanation"


def deterministic_segmentation(spans: list[SourceSpan]) -> dict[str, Any]:
    units: list[dict[str, Any]] = []
    pending: list[SourceSpan] = []
    pending_role = ""

    def flush() -> None:
        nonlocal pending, pending_role
        if not pending:
            return
        units.append(
            {
                "unit_id": f"unit-{len(units) + 1:03d}",
                "source_span_ids": [span.span_id for span in pending],
                "argument_role": pending_role or _semantic_role_for_text("\n".join(span.text for span in pending)),
                "why_these_spans_belong_together": "contiguous source spans with the same local argument role",
            }
        )
        pending = []
        pending_role = ""

    for span in spans:
        role = _semantic_role_for_text(span.text)
        should_flush = False
        if pending and role != pending_role:
            should_flush = True
        if pending and len(pending) >= 3:
            should_flush = True
        if pending and sum(len(item.text) for item in pending) + len(span.text) > 3200:
            should_flush = True
        if should_flush:
            flush()
        pending.append(span)
        pending_role = role
    flush()
    return {"units": units}


def units_from_segmentation(spans: list[SourceSpan], segmentation: dict[str, Any]) -> list[RewriteUnit]:
    span_by_id = {span.span_id: span for span in spans}
    units: list[RewriteUnit] = []
    seen_spans: set[str] = set()
    for index, raw in enumerate(segmentation.get("units", []), start=1):
        span_ids = [str(item) for item in raw.get("source_span_ids", [])]
        selected = [span_by_id[span_id] for span_id in span_ids if span_id in span_by_id]
        if not selected:
            raise ValueError(f"segmentation unit {index} has no valid source_span_ids")
        seen_spans.update(span.span_id for span in selected)
        unit_text = "\n\n".join(span.text for span in selected).strip()
        heading = selected[0].heading_context or f"unit-{index:03d}"
        units.append(
            RewriteUnit(
                unit_id=str(raw.get("unit_id") or f"unit-{index:03d}"),
                heading=heading,
                start_line=min(span.start_line for span in selected),
                end_line=max(span.end_line for span in selected),
                text=unit_text,
                source_span_ids=[span.span_id for span in selected],
                argument_role=str(raw.get("argument_role") or _semantic_role_for_text(unit_text)),
                why_these_spans_belong_together=str(raw.get("why_these_spans_belong_together") or ""),
                literal_invariants=extract_literal_invariants(unit_text),
            )
        )
    missing = sorted(set(span_by_id) - seen_spans)
    if missing:
        raise ValueError(f"segmentation omitted source spans: {', '.join(missing[:8])}")
    return units


def split_markdown_units(text: str) -> list[RewriteUnit]:
    spans = build_source_spans(text)
    return units_from_segmentation(spans, deterministic_segmentation(spans))


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


def restore_exact_literals(writer_result: dict[str, Any], exact: dict[str, Any]) -> dict[str, Any]:
    repaired = dict(writer_result)
    reader_core = str(repaired.get("reader_core", "")).strip()
    technical_trace = str(repaired.get("technical_trace", "")).strip()
    inline_missing: list[str] = []
    trace_missing: list[str] = []
    for item in list(exact.get("missing", [])) + list(exact.get("misplaced_inline", [])):
        if not isinstance(item, dict):
            continue
        text = str(item.get("text", "")).strip()
        if not text:
            continue
        target = inline_missing if item.get("role") == "inline-critical" else trace_missing
        if text not in target:
            target.append(text)
    if inline_missing:
        restored = "保留原文精确项：" + "；".join(inline_missing)
        reader_core = "\n\n".join(part for part in [reader_core, restored] if part)
    if trace_missing:
        restored = "保留原文精确项：" + "；".join(trace_missing)
        technical_trace = "\n\n".join(part for part in [technical_trace, restored] if part)
    repaired["reader_core"] = reader_core
    repaired["technical_trace"] = technical_trace
    return repaired


def restore_semantic_findings(
    writer_result: dict[str, Any],
    semantic: dict[str, Any],
    propositions: list[dict[str, Any]],
) -> dict[str, Any]:
    if not semantic_requires_repair(semantic):
        return writer_result
    proposition_by_id = {str(item["proposition_id"]): item for item in propositions}
    target_ids: set[str] = set()
    for finding in semantic.get("findings", []) or []:
        if not isinstance(finding, dict):
            continue
        status = str(finding.get("status", ""))
        severity = str(finding.get("severity", ""))
        if severity not in {"critical", "blocker"} and status not in {"reversed", "invented", "omitted", "reattributed"}:
            continue
        prop_id = str(finding.get("proposition_id", ""))
        if prop_id in proposition_by_id:
            target_ids.add(prop_id)
            continue
        finding_spans = {str(span_id) for span_id in finding.get("source_span_ids", []) or []}
        for proposition in propositions:
            if finding_spans.intersection(str(span_id) for span_id in proposition.get("source_span_ids", [])):
                target_ids.add(str(proposition["proposition_id"]))
    candidate_text = "\n\n".join(part for part in [writer_result["reader_core"], writer_result.get("technical_trace", "")] if part)
    if not target_ids:
        target_ids = {
            str(proposition["proposition_id"])
            for proposition in propositions
            if str(proposition.get("source_excerpt", "")).strip()
            and str(proposition.get("source_excerpt", "")).strip() not in candidate_text
        }
    restored_lines = []
    for prop_id in sorted(target_ids):
        excerpt = str(proposition_by_id[prop_id].get("source_excerpt", "")).strip()
        if excerpt and excerpt not in candidate_text:
            restored_lines.append(f"- {excerpt}")
    if not restored_lines:
        return writer_result
    repaired = dict(writer_result)
    repaired["reader_core"] = repaired["reader_core"].rstrip() + "\n\n补充保真信息：\n" + "\n".join(restored_lines)
    covered = {str(item) for item in repaired.get("source_coverage_ids", []) or []}
    covered.update(target_ids)
    repaired["source_coverage_ids"] = sorted(covered)
    repaired["runtime_restored_semantic_proposition_ids"] = sorted(target_ids)
    return repaired


def document_map(text: str, spans: list[SourceSpan]) -> dict[str, Any]:
    headings = [span.heading_context for span in spans]
    literals = extract_literal_invariants(text)
    return {
        "audience": "technically trained reader who has not followed the repository audit history",
        "document_purpose": "meaning-preserving reader-facing rewrite of an existing scientific or technical document",
        "core_research_question": "What the current scientific evidence supports, what remains uncertain, and what decision follows next.",
        "section_roles": [
            {"section_id": f"section-{index:03d}", "source_span_ids": [span.span_id], "role": _semantic_role_for_text(span.text)}
            for index, span in enumerate(spans, start=1)
        ],
        "terminology_contract": sorted({span["text"] for span in literals if span["kind"] == "formal_name"}),
        "cross_section_dependencies": headings,
        "major_claims": [
            {"claim_id": f"claim-{index:03d}", "normalized_meaning": item, "source_span_ids": [spans[min(index - 1, len(spans) - 1)].span_id] if spans else []}
            for index, item in enumerate(_sentences_with_markers(text, ("说明", "显示", "支持", "不能", "需要", "结果", "比较"))[:12], start=1)
        ],
        "major_evidence": [
            {"evidence_id": f"evidence-{index:03d}", "normalized_meaning": item, "source_span_ids": [spans[min(index - 1, len(spans) - 1)].span_id] if spans else []}
            for index, item in enumerate(_sentences_with_markers(text, ("=", "%", "seed", "Dice", "HD95", "gap", "证据"))[:12], start=1)
        ],
        "major_uncertainties": [
            {"uncertainty_id": f"uncertainty-{index:03d}", "normalized_meaning": item, "source_span_ids": [spans[min(index - 1, len(spans) - 1)].span_id] if spans else []}
            for index, item in enumerate(_sentences_with_markers(text, ("可能", "限制", "不确定", "不能", "尚未", "negative", "caveat"))[:12], start=1)
        ],
        "major_negative_findings": [],
        "major_decisions": [
            {"decision_id": f"decision-{index:03d}", "normalized_meaning": item, "source_span_ids": [spans[min(index - 1, len(spans) - 1)].span_id] if spans else []}
            for index, item in enumerate(_sentences_with_markers(text, ("因此", "所以", "结论", "下一步", "GO", "STOP"))[:8], start=1)
        ],
        "reader_core_priorities": [
            "research question",
            "current evidence",
            "interpretation limits",
            "comparisons",
            "next experiment",
            "GO/STOP conditions",
        ],
        "trace_material_categories": ["path", "checkpoint locator", "repository locator", "audit detail", "implementation identity"],
        "literal_protected_inventory": literals,
    }


def _sentences_with_markers(text: str, markers: tuple[str, ...]) -> list[str]:
    sentences = [part.strip() for part in re.split(r"(?<=[。！？.!?])\s+|\n+", text) if part.strip()]
    selected = [part for part in sentences if any(marker in part for marker in markers)]
    return selected or sentences[: min(5, len(sentences))]


def proposition_inventory(unit: RewriteUnit) -> list[dict[str, Any]]:
    markers_by_kind = {
        "claim": ("说明", "显示", "支持", "认为", "表明", "证明"),
        "evidence": ("=", "%", "Dice", "HD95", "结果", "证据", "seed"),
        "condition": ("如果", "条件", "保持", "使用", "从", "在"),
        "comparator": ("vs", "相比", "比较", "FedFisher", "FedLPA", "ODAL", "pooled", "FedAvg"),
        "caveat": ("可能", "限制", "不能", "不确定", "尚未", "不足"),
        "decision": ("因此", "下一步", "GO", "STOP", "停止", "启动"),
        "attribution": ("已有", "文献", "本文", "报告", "AISTATS", "NeurIPS"),
    }
    candidates = []
    for kind, markers in markers_by_kind.items():
        for sentence in _sentences_with_markers(unit.text, markers)[:4]:
            candidates.append((kind, sentence))
    if not candidates:
        candidates.append(("claim", unit.text[:600]))
    seen: set[tuple[str, str]] = set()
    propositions: list[dict[str, Any]] = []
    for kind, sentence in candidates:
        key = (kind, sentence)
        if key in seen:
            continue
        seen.add(key)
        propositions.append(
            {
                "proposition_id": f"{unit.unit_id}-prop-{len(propositions) + 1:03d}",
                "kind": kind,
                "source_span_ids": unit.source_span_ids,
                "source_text_sha256": sha256_text(sentence),
                "source_excerpt": sentence[:240],
                "required": True,
            }
        )
    return propositions


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
    propositions = proposition_inventory(unit)
    filters = infer_unit_filters(unit)
    return {
        "unit_id": unit.unit_id,
        "reader_job": "explain the local scientific argument in natural Chinese while preserving the source facts",
        "plain_meaning": _reader_takeaway(unit),
        "claims": [
            {
                "claim_id": f"claim-{index:03d}",
                "normalized_meaning": item["source_excerpt"],
                "source_span_ids": item["source_span_ids"],
                "source_proposition_ids": [item["proposition_id"]],
                "strength": "same-as-source",
            }
            for index, item in enumerate([p for p in propositions if p["kind"] == "claim"], start=1)
        ],
        "evidence": [
            {
                "evidence_id": f"evidence-{index:03d}",
                "normalized_meaning": item["source_excerpt"],
                "source_span_ids": item["source_span_ids"],
                "source_proposition_ids": [item["proposition_id"]],
                "supports_claim_ids": ["claim-001"] if any(p["kind"] == "claim" for p in propositions) else [],
            }
            for index, item in enumerate([p for p in propositions if p["kind"] == "evidence"], start=1)
        ],
        "conditions": [
            {"normalized_meaning": item["source_excerpt"], "source_span_ids": item["source_span_ids"], "source_proposition_ids": [item["proposition_id"]]}
            for item in propositions
            if item["kind"] == "condition"
        ],
        "comparators": [
            {"normalized_meaning": item["source_excerpt"], "source_span_ids": item["source_span_ids"], "source_proposition_ids": [item["proposition_id"]]}
            for item in propositions
            if item["kind"] == "comparator"
        ],
        "uncertainty": [
            {"normalized_meaning": item["source_excerpt"], "source_span_ids": item["source_span_ids"], "source_proposition_ids": [item["proposition_id"]]}
            for item in propositions
            if item["kind"] == "caveat"
        ],
        "caveats": [
            {"normalized_meaning": item["source_excerpt"], "source_span_ids": item["source_span_ids"], "source_proposition_ids": [item["proposition_id"]]}
            for item in propositions
            if item["kind"] == "caveat"
        ],
        "negative_findings": [],
        "attribution": [
            {"normalized_meaning": item["source_excerpt"], "source_span_ids": item["source_span_ids"], "source_proposition_ids": [item["proposition_id"]]}
            for item in propositions
            if item["kind"] == "attribution"
        ],
        "decision_logic": [
            {"normalized_meaning": item["source_excerpt"], "source_span_ids": item["source_span_ids"], "source_proposition_ids": [item["proposition_id"]]}
            for item in propositions
            if item["kind"] == "decision"
        ],
        "terminology": sorted({span["text"] for span in literals if span["kind"] == "formal_name"}),
        "literal_items": [span for span in literals if span["role"] == "inline-critical"],
        "relocatable_trace_items": [span for span in literals if span["role"] == "relocatable-trace"],
        "relation_to_previous": previous_heading,
        "relation_to_next": next_heading,
        "rewrite_problem": filters["rewrite_problem"],
        "discourse_function": filters["discourse_function"],
        "fidelity_risk": filters["fidelity_risk"],
        "register": filters["register"],
        "reader_takeaway": _reader_takeaway(unit),
    }


def _reader_takeaway(unit: RewriteUnit) -> str:
    clean_heading = re.sub(r"^[#\s]+", "", unit.heading).strip() or unit.unit_id
    return f"读者应理解 {clean_heading} 这一部分的判断、证据和限制，而不是先解码内部流程标签。"


def coverage_check(unit: RewriteUnit, card: dict[str, Any]) -> dict[str, Any]:
    required = proposition_inventory(unit)
    represented: set[str] = set()
    semantic_fields = [
        "claims",
        "evidence",
        "conditions",
        "comparators",
        "uncertainty",
        "caveats",
        "negative_findings",
        "attribution",
        "decision_logic",
    ]
    for field in semantic_fields:
        for item in card.get(field, []) or []:
            represented.update(str(pid) for pid in item.get("source_proposition_ids", []) or [])
    missing = [item for item in required if item["required"] and item["proposition_id"] not in represented]
    return {
        "ok": not missing,
        "required_proposition_count": len(required),
        "covered_proposition_ids": sorted(represented),
        "missing_propositions": missing,
    }


def extract_keywords(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}|[0-9]+(?:\.[0-9]+)?%?", text)
    return tokens[:8]


def require_fields(payload: dict[str, Any], fields: list[str], stage: str) -> None:
    missing = [field for field in fields if field not in payload]
    if missing:
        raise RuntimeError(f"{stage} structured output missing fields: {', '.join(missing)}")


def require_list(payload: dict[str, Any], field: str, stage: str) -> list[Any]:
    value = payload.get(field)
    if not isinstance(value, list):
        raise RuntimeError(f"{stage}.{field} must be a list")
    return value


def require_string(payload: dict[str, Any], field: str, stage: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        raise RuntimeError(f"{stage}.{field} must be a non-empty string")
    return value


def parse_json_object(raw: str, stage: str) -> dict[str, Any]:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{stage} returned malformed JSON") from exc
    if not isinstance(payload, dict):
        raise RuntimeError(f"{stage} must return a JSON object")
    return payload


def validate_source_span_ids(ids: list[Any], known_ids: set[str], stage: str) -> list[str]:
    normalized = [str(item) for item in ids]
    if not normalized:
        raise RuntimeError(f"{stage} must bind to at least one source span id")
    unknown = sorted(set(normalized) - known_ids)
    if unknown:
        raise RuntimeError(f"{stage} references unknown source span ids: {', '.join(unknown[:8])}")
    return normalized


def normalize_document_map(raw: dict[str, Any], spans: list[SourceSpan]) -> dict[str, Any]:
    stage = "document-map"
    fields = [
        "audience",
        "document_purpose",
        "core_research_question",
        "section_roles",
        "major_claims",
        "major_evidence",
        "major_uncertainties",
        "major_negative_findings",
        "major_decisions",
        "cross_section_dependencies",
        "terminology_contract",
        "reader_core_priorities",
        "trace_material_categories",
    ]
    require_fields(raw, fields, stage)
    for field in ["audience", "document_purpose", "core_research_question"]:
        require_string(raw, field, stage)
    known_ids = {span.span_id for span in spans}
    for field in [
        "section_roles",
        "major_claims",
        "major_evidence",
        "major_uncertainties",
        "major_negative_findings",
        "major_decisions",
    ]:
        for index, item in enumerate(require_list(raw, field, stage), start=1):
            if not isinstance(item, dict):
                raise RuntimeError(f"{stage}.{field}[{index}] must be an object")
            if "source_span_ids" in item:
                item["source_span_ids"] = validate_source_span_ids(item["source_span_ids"], known_ids, f"{stage}.{field}[{index}]")
    for field in ["cross_section_dependencies", "terminology_contract", "reader_core_priorities", "trace_material_categories"]:
        require_list(raw, field, stage)
    return raw


def normalize_segmentation(raw: dict[str, Any], spans: list[SourceSpan]) -> dict[str, Any]:
    stage = "argument-segmentation"
    units = require_list(raw, "units", stage)
    known_ids = {span.span_id for span in spans}
    seen: set[str] = set()
    for index, unit in enumerate(units, start=1):
        if not isinstance(unit, dict):
            raise RuntimeError(f"{stage}.units[{index}] must be an object")
        require_string(unit, "unit_id", f"{stage}.units[{index}]")
        span_ids = validate_source_span_ids(unit.get("source_span_ids", []), known_ids, f"{stage}.units[{index}]")
        unit["source_span_ids"] = span_ids
        require_string(unit, "argument_role", f"{stage}.units[{index}]")
        require_string(unit, "why_these_spans_belong_together", f"{stage}.units[{index}]")
        seen.update(span_ids)
        if len(span_ids) > 5:
            raise RuntimeError(f"{stage}.units[{index}] has more than 5 source spans")
    missing = sorted(known_ids - seen)
    if missing:
        raise RuntimeError(f"{stage} omitted source spans: {', '.join(missing[:8])}")
    if len(spans) >= 3 and sum(len(span.text) for span in spans) > 2500 and len(units) == 1:
        raise RuntimeError(f"{stage} collapsed a long multi-span source into one argument unit")
    return {"units": units}


def _collect_card_proposition_ids(card: dict[str, Any]) -> set[str]:
    represented: set[str] = set()
    for field in [
        "claims",
        "evidence",
        "conditions",
        "comparators",
        "uncertainty",
        "caveats",
        "negative_findings",
        "attribution",
        "decision_logic",
    ]:
        for item in card.get(field, []) or []:
            if isinstance(item, dict):
                represented.update(str(pid) for pid in item.get("source_proposition_ids", []) or [])
    return represented


def _infer_card_item_proposition_ids(item: dict[str, Any], propositions: list[dict[str, Any]]) -> list[str]:
    item_spans = {str(span_id) for span_id in item.get("source_span_ids", [])}
    matched = [
        str(proposition["proposition_id"])
        for proposition in propositions
        if item_spans and item_spans.intersection(str(span_id) for span_id in proposition.get("source_span_ids", []))
    ]
    if matched:
        return sorted(set(matched))
    return sorted(str(proposition["proposition_id"]) for proposition in propositions)


def _meaning_card_field_for_proposition(proposition: dict[str, Any]) -> str:
    kind = str(proposition.get("kind", "claim"))
    if kind == "evidence":
        return "evidence"
    if kind == "condition":
        return "conditions"
    if kind == "comparator":
        return "comparators"
    if kind == "caveat":
        return "caveats"
    if kind == "attribution":
        return "attribution"
    if kind == "decision":
        return "decision_logic"
    return "claims"


def normalize_meaning_card(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    stage = f"{unit.unit_id}-meaning-card"
    fields = [
        "unit_id",
        "reader_job",
        "plain_meaning",
        "claims",
        "evidence",
        "conditions",
        "comparators",
        "uncertainty",
        "caveats",
        "negative_findings",
        "attribution",
        "decision_logic",
        "terminology",
        "literal_items",
        "relocatable_trace_items",
        "relation_to_previous",
        "relation_to_next",
        "rewrite_problem",
        "discourse_function",
        "reader_takeaway",
    ]
    require_fields(raw, fields, stage)
    if str(raw["unit_id"]) != unit.unit_id:
        raise RuntimeError(f"{stage} returned mismatched unit_id")
    require_string(raw, "reader_job", stage)
    require_string(raw, "plain_meaning", stage)
    known_spans = set(unit.source_span_ids)
    known_props = {item["proposition_id"] for item in propositions}
    for field in [
        "claims",
        "evidence",
        "conditions",
        "comparators",
        "uncertainty",
        "caveats",
        "negative_findings",
        "attribution",
        "decision_logic",
    ]:
        for index, item in enumerate(require_list(raw, field, stage), start=1):
            if not isinstance(item, dict):
                raise RuntimeError(f"{stage}.{field}[{index}] must be an object")
            require_string(item, "normalized_meaning", f"{stage}.{field}[{index}]")
            item["source_span_ids"] = validate_source_span_ids(item.get("source_span_ids", []), known_spans, f"{stage}.{field}[{index}]")
            prop_ids = [str(pid) for pid in item.get("source_proposition_ids", [])]
            if not prop_ids:
                prop_ids = _infer_card_item_proposition_ids(item, propositions)
                item["source_proposition_ids"] = prop_ids
                item["runtime_inferred_source_proposition_ids"] = True
            unknown_props = sorted(set(prop_ids) - known_props)
            if unknown_props:
                raise RuntimeError(f"{stage}.{field}[{index}] references unknown proposition ids: {', '.join(unknown_props[:8])}")
    proposition_by_id = {item["proposition_id"]: item for item in propositions}
    missing_props = sorted(known_props - _collect_card_proposition_ids(raw))
    if missing_props:
        for prop_id in missing_props:
            proposition = proposition_by_id[prop_id]
            field = _meaning_card_field_for_proposition(proposition)
            raw[field].append(
                {
                    "normalized_meaning": proposition["source_excerpt"],
                    "source_span_ids": proposition["source_span_ids"],
                    "source_proposition_ids": [prop_id],
                    "runtime_completed_from_source_proposition": True,
                }
            )
        raw["runtime_completed_missing_proposition_ids"] = missing_props
    for field in ["terminology", "literal_items", "relocatable_trace_items"]:
        require_list(raw, field, stage)
    return raw


def normalize_writer_result(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    stage = f"{unit.unit_id}-writer"
    require_fields(raw, ["reader_core", "technical_trace", "source_coverage_ids", "relocated_trace_ids"], stage)
    require_string(raw, "reader_core", stage)
    if not isinstance(raw.get("technical_trace"), str):
        raise RuntimeError(f"{stage}.technical_trace must be a string")
    known_props = {item["proposition_id"] for item in propositions}
    covered = {str(item) for item in raw.get("source_coverage_ids", [])}
    missing = sorted(known_props - covered)
    if missing:
        raise RuntimeError(f"{stage} output omitted source_coverage_ids: {', '.join(missing[:8])}")
    known_trace = {item["text"] for item in unit.literal_invariants if item.get("role") == "relocatable-trace"}
    relocated = [str(item) for item in raw.get("relocated_trace_ids", [])]
    if unit.literal_invariants and known_trace and not raw.get("technical_trace") and not any(trace in raw["reader_core"] for trace in known_trace):
        raise RuntimeError(f"{stage} did not preserve visible relocatable trace in reader_core or technical_trace")
    raw["relocated_trace_ids"] = relocated
    return raw


def canonical_semantic_status(status: Any) -> str:
    token = str(status or "").strip().lower().replace("-", "_").replace(" ", "_")
    if token in SEMANTIC_STATUSES:
        return token
    if token in SEMANTIC_STATUS_ALIASES:
        return SEMANTIC_STATUS_ALIASES[token]
    raise RuntimeError("semantic status is invalid")


def normalize_semantic_audit(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    stage = f"{unit.unit_id}-semantic-audit"
    require_fields(raw, ["decision", "findings"], stage)
    if raw["decision"] not in {"PASS", "REVISE"}:
        raise RuntimeError(f"{stage}.decision must be PASS or REVISE")
    known_props = {item["proposition_id"] for item in propositions}
    critical = 0
    for index, finding in enumerate(require_list(raw, "findings", stage), start=1):
        if not isinstance(finding, dict):
            raise RuntimeError(f"{stage}.findings[{index}] must be an object")
        try:
            status = canonical_semantic_status(finding.get("status"))
        except RuntimeError:
            raise RuntimeError(f"{stage}.findings[{index}].status is invalid")
        finding["status"] = status
        prop_id = str(finding.get("proposition_id", ""))
        if prop_id and prop_id not in known_props:
            raise RuntimeError(f"{stage}.findings[{index}] references unknown proposition_id")
        severity = str(finding.get("severity", ""))
        if severity in {"critical", "blocker"} or status in {"reversed", "invented", "omitted", "reattributed"}:
            critical += 1
    raw["critical_violation_count"] = critical
    return raw


def semantic_requires_repair(semantic: dict[str, Any]) -> bool:
    return int(semantic.get("critical_violation_count", 0)) > 0


def normalize_reader_review(raw: dict[str, Any], known_unit_ids: set[str]) -> dict[str, Any]:
    stage = "candidate-only-reader-review"
    require_fields(raw, ["decision", "questions", "findings"], stage)
    if raw["decision"] not in {"PASS", "REVISE"}:
        raise RuntimeError(f"{stage}.decision must be PASS or REVISE")
    has_unanswerable_question = False
    for index, question in enumerate(require_list(raw, "questions", stage), start=1):
        if not isinstance(question, dict):
            raise RuntimeError(f"{stage}.questions[{index}] must be an object")
        answerable = question.get("answerable")
        if isinstance(answerable, str):
            normalized = answerable.strip().lower().strip(".。!！")
            false_markers = {
                "false",
                "no",
                "n",
                "0",
                "not answerable",
                "cannot answer",
                "can't answer",
                "unable",
                "unanswerable",
                "partial",
                "partially",
                "unclear",
                "unknown",
                "不可回答",
                "不能回答",
                "无法回答",
                "部分可回答",
                "不清楚",
                "未知",
            }
            if normalized in false_markers:
                question["answerable"] = False
            elif normalized in {"true", "yes", "y", "1", "answerable", "可回答", "可以回答"}:
                question["answerable"] = True
            else:
                question["answerable"] = False
        elif not isinstance(answerable, bool):
            question["answerable"] = False
        if question["answerable"] is False:
            has_unanswerable_question = True
        inferred_answer = question.get("inferred_answer")
        if isinstance(inferred_answer, str) and inferred_answer.strip():
            question["inferred_answer"] = inferred_answer.strip()
        elif inferred_answer is None or inferred_answer == "":
            question["inferred_answer"] = "未提供可回答性说明；按不可回答处理。"
            question["answerable"] = False
            has_unanswerable_question = True
        else:
            question["inferred_answer"] = str(inferred_answer).strip() or "未提供可回答性说明；按不可回答处理。"
    if raw["decision"] == "PASS" and has_unanswerable_question:
        raw["decision"] = "REVISE"
    for index, finding in enumerate(require_list(raw, "findings", stage), start=1):
        if not isinstance(finding, dict):
            raise RuntimeError(f"{stage}.findings[{index}] must be an object")
        unit_id = str(finding.get("unit_id", ""))
        if unit_id and unit_id not in known_unit_ids:
            raise RuntimeError(f"{stage}.findings[{index}] references unknown unit_id")
    return raw


def normalize_assembly_review(raw: dict[str, Any], known_unit_ids: set[str]) -> dict[str, Any]:
    stage = "final-assembly-coherence"
    require_fields(raw, ["decision", "findings"], stage)
    if raw["decision"] not in {"PASS", "REVISE"}:
        raise RuntimeError(f"{stage}.decision must be PASS or REVISE")
    for index, finding in enumerate(require_list(raw, "findings", stage), start=1):
        if not isinstance(finding, dict):
            raise RuntimeError(f"{stage}.findings[{index}] must be an object")
        unit_id = str(finding.get("unit_id", ""))
        if unit_id and unit_id not in known_unit_ids:
            raise RuntimeError(f"{stage}.findings[{index}] references unknown unit_id")
    return raw


def normalize_assembly_repair(raw: dict[str, Any], known_unit_ids: set[str], expected_finding_ids: set[str] | None = None) -> dict[str, Any]:
    stage = "final-assembly-targeted-repair"
    require_fields(raw, ["reader_core", "technical_trace", "applied_finding_ids"], stage)
    require_string(raw, "reader_core", stage)
    if not isinstance(raw.get("technical_trace"), str):
        raise RuntimeError(f"{stage}.technical_trace must be a string")
    applied = raw.get("applied_finding_ids")
    if not isinstance(applied, list):
        raise RuntimeError(f"{stage}.applied_finding_ids must be a list")
    raw["applied_finding_ids"] = [str(item) for item in applied]
    if expected_finding_ids:
        missing = sorted(expected_finding_ids - set(raw["applied_finding_ids"]))
        if missing:
            raise RuntimeError(f"{stage}.applied_finding_ids omitted findings: {', '.join(missing[:8])}")
    for index, unit_id in enumerate(raw.get("touched_unit_ids", []) or [], start=1):
        if str(unit_id) not in known_unit_ids:
            raise RuntimeError(f"{stage}.touched_unit_ids[{index}] references unknown unit_id")
    return raw


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
            "core_research_question": doc_map["core_research_question"],
            "section_roles": doc_map["section_roles"],
            "major_claims": doc_map["major_claims"][:5],
            "major_evidence": doc_map["major_evidence"][:5],
            "major_uncertainties": doc_map["major_uncertainties"][:5],
            "major_decisions": doc_map["major_decisions"][:5],
            "reader_core_priorities": doc_map["reader_core_priorities"],
            "trace_material_categories": doc_map["trace_material_categories"],
        },
        "current_original_unit": unit.text,
        "current_source_span_ids": unit.source_span_ids,
        "argument_role": unit.argument_role,
        "why_these_spans_belong_together": unit.why_these_spans_belong_together,
        "meaning_card": card,
        "source_propositions": proposition_inventory(unit),
        "fidelity_ledger": {
            "literal_items": unit.literal_invariants,
            "semantic_status_values": sorted(SEMANTIC_STATUSES),
            "critical_violations_allowed": 0,
            "trace_relocation_allowed": True,
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
    return {
        "reader_core": reader_core,
        "technical_trace": trace_appendix,
        "source_coverage_ids": [item["proposition_id"] for item in proposition_inventory(unit)],
        "relocated_trace_ids": [item["text"] for item in unit.literal_invariants if item.get("role") == "relocatable-trace" and item["text"] in trace_appendix],
    }


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
        "decision": "PASS" if not critical else "REVISE",
        "statuses": [status],
        "findings": [
            {
                "finding_id": f"finding-{index:03d}",
                "proposition_id": "",
                "status": item["status"],
                "source_span_ids": [],
                "candidate_evidence": item["candidate_evidence"],
                "severity": "critical",
                "repair_instruction": item["reason"],
            }
            for index, item in enumerate(critical, start=1)
        ],
        "critical_violation_count": len(critical),
        "allowed_status_values": sorted(SEMANTIC_STATUSES),
    }


def reader_review_packet(candidate: str, audience: str) -> dict[str, Any]:
    return {
        "schema": PACKET_SCHEMA,
        "stage": "candidate-only-reader-review",
        "source_visible": False,
        "audience": audience,
        "candidate_text": candidate,
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
    terminal_output: bool = False,
) -> StageRecord:
    output_sha = sha256_text(canonical_json(output_payload))
    return StageRecord(
        stage_id=stage_id,
        responsibility=responsibility,
        unit_id=unit_id,
        input_sha256=sha256_text(canonical_json(input_payload)),
        output_sha256=output_sha,
        output_identity=f"{stage_id}.output:{output_sha}",
        downstream_consumers=[],
        selected_example_ids=selected_example_ids or [],
        model_call=model_call,
        plaintext_committed=False,
        unused_output=not terminal_output,
        terminal_output=terminal_output,
    )


def bind_consumer(records: list[StageRecord], producer_stage_id: str, consumer_stage_id: str, input_binding: str) -> None:
    for record in records:
        if record.stage_id == producer_stage_id:
            record.downstream_consumers.append({"stage_id": consumer_stage_id, "input_binding": input_binding})
            record.unused_output = False
            return
    raise RuntimeError(f"Cannot bind missing producer stage: {producer_stage_id}")


def validate_dataflow(receipt: dict[str, Any]) -> dict[str, Any]:
    stage_ids = {record["stage_id"] for record in receipt.get("stage_records", [])}
    unused = [
        record["stage_id"]
        for record in receipt.get("stage_records", [])
        if record.get("model_call") and record.get("unused_output") and not record.get("terminal_output")
    ]
    dangling = [
        {"producer_stage_id": record.get("stage_id"), "consumer_stage_id": consumer.get("stage_id")}
        for record in receipt.get("stage_records", [])
        for consumer in record.get("downstream_consumers", [])
        if consumer.get("stage_id") not in stage_ids
    ]
    return {"ok": not unused and not dangling, "unused_model_outputs": unused, "dangling_consumers": dangling}


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


def build_openai_request(prompt: str, source: str, *, model: str, response_schema: dict[str, Any] | None = None) -> dict[str, Any]:
    request = {
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
    if response_schema:
        request["text"] = {
            "format": {
                "type": "json_schema",
                "name": response_schema["name"],
                "description": response_schema.get("description", ""),
                "schema": response_schema["schema"],
                "strict": False,
            }
        }
    return request


def call_openai_text(
    prompt: str,
    source: str,
    *,
    model: str,
    api_key: str,
    timeout: float = 120.0,
    opener: Callable[..., Any] | None = None,
    response_schema: dict[str, Any] | None = None,
) -> str:
    if not api_key:
        raise RuntimeError("OpenAI API key unavailable for staged scientific rewrite")
    request_payload = build_openai_request(prompt, source, model=model, response_schema=response_schema)
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


def json_response_schema(name: str, required: list[str]) -> dict[str, Any]:
    string_fields = {
        "audience",
        "document_purpose",
        "core_research_question",
        "unit_id",
        "reader_job",
        "plain_meaning",
        "relation_to_previous",
        "relation_to_next",
        "rewrite_problem",
        "discourse_function",
        "reader_takeaway",
        "reader_core",
        "technical_trace",
    }
    list_fields = {
        "section_roles",
        "major_claims",
        "major_evidence",
        "major_uncertainties",
        "major_negative_findings",
        "major_decisions",
        "cross_section_dependencies",
        "terminology_contract",
        "reader_core_priorities",
        "trace_material_categories",
        "units",
        "claims",
        "evidence",
        "conditions",
        "comparators",
        "uncertainty",
        "caveats",
        "negative_findings",
        "attribution",
        "decision_logic",
        "terminology",
        "literal_items",
        "relocatable_trace_items",
        "source_coverage_ids",
        "relocated_trace_ids",
        "findings",
        "questions",
    }
    properties: dict[str, Any] = {}
    for field in required:
        if field == "decision":
            properties[field] = {"type": "string", "enum": ["PASS", "REVISE"]}
        elif field in string_fields:
            properties[field] = {"type": "string", "minLength": 1}
        elif field in list_fields:
            if field == "findings" and "semantic_audit" in name:
                properties[field] = {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": True,
                        "properties": {
                            "status": {"type": "string", "enum": sorted(SEMANTIC_STATUSES)},
                            "proposition_id": {"type": "string"},
                            "severity": {"type": "string"},
                        },
                    },
                }
            else:
                properties[field] = {"type": "array"}
        else:
            properties[field] = {}
    return {
        "name": name,
        "description": f"Structured {name} stage output.",
        "schema": {
            "type": "object",
            "additionalProperties": True,
            "required": required,
            "properties": properties,
        },
    }


def response_schema_name(stage: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", stage.replace("-", "_")).strip("_") or "stage"
    if len(safe) <= 64:
        return safe
    digest = hashlib.sha256(safe.encode("utf-8")).hexdigest()[:10]
    return f"{safe[:53]}_{digest}"


def call_openai_json(
    stage: str,
    prompt: str,
    payload: Any,
    *,
    model: str,
    api_key: str,
    required: list[str],
) -> dict[str, Any]:
    strict_prompt = (
        f"{prompt}\n\nReturn one valid JSON object only. Do not wrap it in Markdown. "
        f"The JSON object must contain these top-level fields: {', '.join(required)}. "
        "Every required string field must be a non-empty concrete value. "
        "If a value is implicit in the source, infer a concise value from the source instead of returning an empty string. "
        "Every required list field must be a JSON array, empty only when the source truly has no such item."
    )
    raw = call_openai_text(
        strict_prompt,
        canonical_json(payload),
        model=model,
        api_key=api_key,
        response_schema=json_response_schema(response_schema_name(stage), required),
    )
    return parse_json_object(raw, stage)


def call_openai_json_validated(
    stage: str,
    prompt: str,
    payload: Any,
    *,
    model: str,
    api_key: str,
    required: list[str],
    validator: Callable[[dict[str, Any]], dict[str, Any]],
    retries: int = 1,
) -> dict[str, Any]:
    last_error = ""
    for attempt in range(retries + 1):
        stage_prompt = prompt
        if attempt:
            stage_prompt = (
                f"{prompt}\n\nYour previous JSON for stage `{stage}` failed validation: {last_error}. "
                "Return a corrected JSON object only. Do not omit required fields, do not use empty strings for required semantic labels, "
                "and keep all identifiers bound to the supplied source_span_ids/proposition_ids."
            )
        try:
            return validator(
                call_openai_json(
                    stage,
                    stage_prompt,
                    payload,
                    model=model,
                    api_key=api_key,
                    required=required,
                )
            )
        except RuntimeError as exc:
            last_error = str(exc)
    raise RuntimeError(f"{stage} failed structured validation after retry: {last_error}")


def deterministic_reader_review(candidate: str, unit_ids: list[str]) -> dict[str, Any]:
    required_context = {
        "provenance": ["来源", "来路", "从哪里来"],
        "estimand": ["实际回答", "要回答", "研究问题"],
        "resource contract": ["资源", "可用", "约束"],
        "controlled-drift axis": ["漂移", "变化", "距离"],
    }
    findings = []
    lowered = candidate.lower()
    for marker, context_terms in required_context.items():
        if marker in lowered and not any(term in candidate for term in context_terms):
            findings.append(
                {
                    "finding_id": f"reader-{len(findings) + 1:03d}",
                    "unit_id": "",
                    "category": "unexplained_abstraction",
                    "evidence": f"candidate keeps {marker} without a concrete reader-facing explanation",
                    "repair_instruction": "explain the concrete research meaning before formal labels",
                }
            )
    return {
        "decision": "REVISE" if findings else "PASS",
        "questions": [
            {
                "question_id": "reader-question-001",
                "answerable": not findings,
                "inferred_answer": "candidate explains the research problem, evidence, uncertainty, next step and GO/STOP condition",
                "supporting_candidate_span": candidate[:240],
            }
        ],
        "findings": findings,
    }


def deterministic_assembly_review(candidate: str) -> dict[str, Any]:
    return {"decision": "PASS", "findings": [] if candidate.strip() else [{"finding_id": "assembly-001", "unit_id": "", "category": "empty", "repair_instruction": "candidate is empty"}]}


def deterministic_assembly_repair(reader_core: str, technical_trace: str, review: dict[str, Any]) -> dict[str, Any]:
    finding_ids = [str(item.get("finding_id", "")) for item in review.get("findings", []) if isinstance(item, dict)]
    repaired_core = reader_core.strip()
    if not repaired_core:
        repaired_core = "候选文本为空，无法完成最终组装。"
    return {
        "reader_core": repaired_core,
        "technical_trace": technical_trace.strip(),
        "applied_finding_ids": [item for item in finding_ids if item],
        "touched_unit_ids": sorted(
            {
                str(item.get("unit_id", ""))
                for item in review.get("findings", [])
                if isinstance(item, dict) and str(item.get("unit_id", "")).strip()
            }
        ),
    }


def apply_textual_repair(unit_result: dict[str, Any], instruction: str) -> dict[str, Any]:
    repaired = dict(unit_result)
    reader_core = repaired["reader_core"]
    if "provenance" in reader_core.lower() and "来源" not in reader_core:
        reader_core = "先看 checkpoint 的来源和训练历史是否重叠，再判断这次结果到底能说明什么。\n\n" + reader_core
    if "estimand" in reader_core.lower() and "实际回答" not in reader_core:
        reader_core = "先说明这个实验实际回答的问题，再保留必要的 formal label。\n\n" + reader_core
    note = instruction.strip()
    if note and note not in reader_core:
        reader_core = reader_core.rstrip() + "\n\n" + note
    repaired["reader_core"] = reader_core
    return repaired


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
    spans = build_source_spans(source)
    library = load_seed_library()
    records: list[StageRecord] = []
    packets: list[dict[str, Any]] = []
    doc_map_input = {"source": source, "source_spans": [asdict(span) for span in spans]}
    if driver == "openai-responses":
        doc_map_required = [
            "audience",
            "document_purpose",
            "core_research_question",
            "section_roles",
            "major_claims",
            "major_evidence",
            "major_uncertainties",
            "major_negative_findings",
            "major_decisions",
            "cross_section_dependencies",
            "terminology_contract",
            "reader_core_priorities",
            "trace_material_categories",
        ]
        doc_map = call_openai_json_validated(
            "document-map",
            (
                "Map the document purpose, intended reader, section roles, terminology, "
                "major claims, evidence, caveats, negative findings, decisions, reader priorities, "
                "and trace-material categories. Do not rewrite prose. "
                "Use non-empty concise strings for audience, document_purpose, and core_research_question. "
                "For objects that refer to source material, include source_span_ids from the supplied source_spans."
            ),
            doc_map_input,
            model=model,
            api_key=api_key,
            required=doc_map_required,
            validator=lambda raw: normalize_document_map(raw, spans),
        )
    else:
        doc_map = normalize_document_map(document_map(source, spans), spans)
    records.append(
        stage_record(
            stage_id="document-map",
            responsibility="map document purpose, audience, section roles, terminology, claims and caveats; no prose rewrite",
            unit_id=None,
            input_payload={"source_span_ids": [span.span_id for span in spans], "source_sha256": sha256_text(source)},
            output_payload=doc_map,
            model_call=driver == "openai-responses",
        )
    )

    segmentation_input = {"document_map": doc_map, "source_spans": [asdict(span) for span in spans]}
    if driver == "openai-responses":
        segmentation = call_openai_json_validated(
            "argument-segmentation",
            (
                "Segment the source into argument units. Use source_span_ids. "
                "A unit is normally one small subsection or 2-5 tightly related paragraphs. "
                "Do not collapse long multi-span text into one unit. "
                "Every units[] item must contain a non-empty unit_id, source_span_ids, argument_role, "
                "and why_these_spans_belong_together."
            ),
            segmentation_input,
            model=model,
            api_key=api_key,
            required=["units"],
            validator=lambda raw: normalize_segmentation(raw, spans),
        )
    else:
        segmentation = normalize_segmentation(deterministic_segmentation(spans), spans)
    records.append(
        stage_record(
            stage_id="argument-segmentation",
            responsibility="create argument units from source spans and the validated document map",
            unit_id=None,
            input_payload={"document_map_identity": records[-1].output_identity, "source_span_ids": [span.span_id for span in spans]},
            output_payload=segmentation,
            model_call=driver == "openai-responses",
        )
    )
    bind_consumer(records, "document-map", "argument-segmentation", "document_map")
    units = units_from_segmentation(spans, segmentation)

    rewritten_units: list[dict[str, str]] = []
    unit_cards: dict[str, dict[str, Any]] = {}
    unit_propositions: dict[str, list[dict[str, Any]]] = {}
    unit_gate_stage_ids: dict[str, str] = {}
    unit_candidate_stage_ids: dict[str, str] = {}
    previous_tail = ""
    for index, unit in enumerate(units):
        previous_heading = units[index - 1].heading if index else ""
        next_heading = units[index + 1].heading if index + 1 < len(units) else ""
        propositions = proposition_inventory(unit)
        unit_propositions[unit.unit_id] = propositions
        card_input = {
            "unit": asdict(unit),
            "document_map": doc_map,
            "source_propositions": propositions,
            "previous_heading": previous_heading,
            "next_heading": next_heading,
        }
        if driver == "openai-responses":
            meaning_required = [
                "unit_id",
                "reader_job",
                "plain_meaning",
                "claims",
                "evidence",
                "conditions",
                "comparators",
                "uncertainty",
                "caveats",
                "negative_findings",
                "attribution",
                "decision_logic",
                "terminology",
                "literal_items",
                "relocatable_trace_items",
                "relation_to_previous",
                "relation_to_next",
                "rewrite_problem",
                "discourse_function",
                "reader_takeaway",
            ]
            card = call_openai_json_validated(
                f"{unit.unit_id}-meaning-card",
                (
                    "Create a structured Meaning Card and Fidelity Ledger for this single argument unit. "
                    "Normalize the meaning into natural Chinese concepts; do not copy source sentence order as the semantic representation. "
                    "Bind every required source proposition id to a semantic item. Do not rewrite prose. "
                    "At least one semantic item across claims/evidence/conditions/comparators/uncertainty/caveats/"
                    "negative_findings/attribution/decision_logic must cover every supplied source_proposition_id. "
                    "Each semantic item must include non-empty normalized_meaning, source_span_ids, and source_proposition_ids."
                ),
                card_input,
                model=model,
                api_key=api_key,
                required=meaning_required,
                validator=lambda raw, unit=unit, propositions=propositions: normalize_meaning_card(raw, unit, propositions),
            )
        else:
            card = normalize_meaning_card(meaning_card(unit, doc_map, previous_heading, next_heading), unit, propositions)
        coverage = coverage_check(unit, card)
        if not coverage["ok"]:
            raise RuntimeError(f"{unit.unit_id}-meaning-card failed proposition coverage")
        records.append(
            stage_record(
                stage_id=f"{unit.unit_id}-meaning-card",
                responsibility="derive Meaning Card and Fidelity Ledger for one argument unit; no prose rewrite",
                unit_id=unit.unit_id,
                input_payload={"unit": asdict(unit), "document_map_identity": records[0].output_identity, "source_propositions": propositions},
                output_payload={"meaning_card": card, "coverage": coverage},
                model_call=driver == "openai-responses",
            )
        )
        bind_consumer(records, "document-map", f"{unit.unit_id}-meaning-card", "document_map")
        bind_consumer(records, "argument-segmentation", f"{unit.unit_id}-meaning-card", "argument_unit")
        unit_cards[unit.unit_id] = card
        filters = {
            "scene": "scientific-report",
            "discourse_function": str(card.get("discourse_function") or infer_unit_filters(unit)["discourse_function"]),
            "rewrite_problem": str(card.get("rewrite_problem") or infer_unit_filters(unit)["rewrite_problem"]),
            "fidelity_risk": str(card.get("fidelity_risk") or infer_unit_filters(unit)["fidelity_risk"]),
            "register": str(card.get("register") or "formal-technical"),
        }
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
        bind_consumer(records, f"{unit.unit_id}-meaning-card", f"{unit.unit_id}-example-selection", "meaning_card_metadata")
        next_preview = units[index + 1].text if index + 1 < len(units) else ""
        packet = writer_packet(unit, doc_map, card, examples, previous_tail, next_preview)
        packets.append(packet)
        if stage_dir:
            write_json(stage_dir / f"{unit.unit_id}.writer-packet.json", packet)
        if driver == "openai-responses":
            unit_result = call_openai_json_validated(
                f"{unit.unit_id}-writer",
                (
                    "Rewrite only the current argument unit. Return structured JSON with reader_core and technical_trace. "
                    "Use the validated Document Map and Meaning Card as the organization authority while keeping the original unit as fact authority. "
                    "Do not follow source sentence order when it makes the reader decode audit/process labels first. "
                    "Relocate trace-heavy exact paths or implementation identifiers into technical_trace when appropriate. "
                    "source_coverage_ids must include every supplied source proposition id."
                ),
                packet,
                model=model,
                api_key=api_key,
                required=["reader_core", "technical_trace", "source_coverage_ids", "relocated_trace_ids"],
                validator=lambda raw, unit=unit, propositions=propositions: normalize_writer_result(raw, unit, propositions),
            )
        else:
            unit_result = normalize_writer_result(deterministic_unit_rewrite(unit), unit, propositions)
        writer_stage_id = f"{unit.unit_id}-writer"
        records.append(
            stage_record(
                stage_id=writer_stage_id,
                responsibility="rewrite one argument unit from original source plus Meaning Card and selected examples",
                unit_id=unit.unit_id,
                input_payload=packet,
                output_payload=unit_result,
                selected_example_ids=[item["id"] for item in examples],
                model_call=driver == "openai-responses",
            )
        )
        bind_consumer(records, f"{unit.unit_id}-meaning-card", writer_stage_id, "meaning_card")
        bind_consumer(records, f"{unit.unit_id}-example-selection", writer_stage_id, "selected_transformations")
        current_candidate_stage_id = writer_stage_id
        combined_unit = "\n\n".join(part for part in [unit_result["reader_core"], unit_result["technical_trace"]] if part)
        exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=unit_result["reader_core"])
        semantic_input = {"source_unit": unit.text, "candidate": unit_result, "meaning_card": card, "exact": exact}
        if driver == "openai-responses":
            semantic = call_openai_json_validated(
                f"{unit.unit_id}-semantic-audit",
                (
                    "Audit semantic preservation for this unit. Check polarity, scope, conditions, comparators, causality, uncertainty, "
                    "attribution, negative findings, decision logic and conclusion strength. Return PASS or REVISE with findings. "
                    "Each finding must use one of these statuses: preserved, narrowed, broadened, reversed, invented, omitted, reattributed."
                ),
                semantic_input,
                model=model,
                api_key=api_key,
                required=["decision", "findings"],
                validator=lambda raw, unit=unit, propositions=propositions: normalize_semantic_audit(raw, unit, propositions),
            )
        else:
            semantic = normalize_semantic_audit(semantic_audit(unit.text, combined_unit), unit, propositions)
        audit_stage_id = f"{unit.unit_id}-literal-semantic-audit"
        records.append(
            stage_record(
                stage_id=audit_stage_id,
                responsibility="verify exact literal preservation and semantic claim/relation status for the current unit",
                unit_id=unit.unit_id,
                input_payload={"source_sha256": sha256_text(unit.text), "candidate": unit_result, "meaning_card_identity": records[-2].output_identity},
                output_payload={"exact": exact, "semantic": semantic},
                model_call=driver == "openai-responses",
            )
        )
        bind_consumer(records, current_candidate_stage_id, audit_stage_id, "candidate")
        last_audit_stage_id = audit_stage_id
        repair_attempts = 0
        while (not exact["ok"] or semantic_requires_repair(semantic)) and repair_attempts < UNIT_REPAIR_ROUNDS:
            repair_attempts += 1
            pre_repair_exact = exact
            pre_repair_semantic = semantic
            repair_payload = {
                "unit": asdict(unit),
                "candidate": unit_result,
                "meaning_card": card,
                "exact": exact,
                "semantic": semantic,
            }
            if driver == "openai-responses":
                repaired = call_openai_json_validated(
                    f"{unit.unit_id}-targeted-repair",
                    (
                        "Repair only the current rewritten unit. Preserve all source facts and return the same structured writer JSON fields. "
                        "Do not rewrite unrelated units. source_coverage_ids must include every supplied source proposition id. "
                        "If exact.missing lists literal strings, copy those exact strings into reader_core or technical_trace. "
                        "If semantic.findings lists critical omissions, condition changes, comparator changes, uncertainty changes, "
                        "conclusion-strength changes, attribution changes, or invented claims, repair those exact findings against the source unit."
                    ),
                    repair_payload,
                    model=model,
                    api_key=api_key,
                    required=["reader_core", "technical_trace", "source_coverage_ids", "relocated_trace_ids"],
                    validator=lambda raw, unit=unit, propositions=propositions: normalize_writer_result(raw, unit, propositions),
                )
            else:
                repaired = normalize_writer_result(apply_textual_repair(unit_result, "保留原文中遗漏的事实和限制。"), unit, propositions)
            records.append(
                stage_record(
                    stage_id=f"{unit.unit_id}-targeted-repair-{repair_attempts}",
                    responsibility="repair only the affected unit after exact or semantic violation",
                    unit_id=unit.unit_id,
                    input_payload=repair_payload,
                    output_payload=repaired,
                    model_call=driver == "openai-responses",
                )
            )
            repair_stage_id = records[-1].stage_id
            bind_consumer(records, current_candidate_stage_id, repair_stage_id, "candidate")
            bind_consumer(records, last_audit_stage_id, repair_stage_id, "audit_findings")
            unit_result = repaired
            current_candidate_stage_id = repair_stage_id
            combined_unit = "\n\n".join(part for part in [unit_result["reader_core"], unit_result["technical_trace"]] if part)
            exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=unit_result["reader_core"])
            if not exact["ok"]:
                restored = restore_exact_literals(unit_result, exact)
                records.append(
                    stage_record(
                        stage_id=f"{unit.unit_id}-exact-literal-restoration-{repair_attempts}",
                        responsibility="restore missing exact literals from source ledger after model repair",
                        unit_id=unit.unit_id,
                        input_payload={"pre_restore_exact": exact, "repair_output_identity": records[-1].output_identity},
                        output_payload=restored,
                        model_call=False,
                    )
                )
                restore_stage_id = records[-1].stage_id
                bind_consumer(records, current_candidate_stage_id, restore_stage_id, "model_repair_candidate")
                unit_result = restored
                current_candidate_stage_id = restore_stage_id
                combined_unit = "\n\n".join(part for part in [unit_result["reader_core"], unit_result["technical_trace"]] if part)
                exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=unit_result["reader_core"])
            if semantic_requires_repair(semantic):
                restored = restore_semantic_findings(unit_result, semantic, propositions)
                if restored is not unit_result:
                    records.append(
                        stage_record(
                            stage_id=f"{unit.unit_id}-semantic-source-restoration-{repair_attempts}",
                            responsibility="restore source-backed proposition text for unresolved critical semantic findings before re-audit",
                            unit_id=unit.unit_id,
                            input_payload={
                                "pre_restore_semantic": semantic,
                                "candidate_output_identity": records[-1].output_identity,
                            },
                            output_payload=restored,
                            model_call=False,
                        )
                    )
                    restore_stage_id = records[-1].stage_id
                    bind_consumer(records, current_candidate_stage_id, restore_stage_id, "candidate_before_semantic_restoration")
                    bind_consumer(records, last_audit_stage_id, restore_stage_id, "semantic_findings")
                    unit_result = restored
                    current_candidate_stage_id = restore_stage_id
                    combined_unit = "\n\n".join(part for part in [unit_result["reader_core"], unit_result["technical_trace"]] if part)
                    exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=unit_result["reader_core"])
            if driver == "openai-responses":
                semantic = call_openai_json_validated(
                    f"{unit.unit_id}-post-repair-semantic-audit",
                    (
                        "Re-audit semantic preservation after targeted repair. Return PASS or REVISE with findings. "
                        "Each finding must use one of these statuses: preserved, narrowed, broadened, reversed, invented, omitted, reattributed."
                    ),
                    {"source_unit": unit.text, "candidate": unit_result, "meaning_card": card, "exact": exact},
                    model=model,
                    api_key=api_key,
                    required=["decision", "findings"],
                    validator=lambda raw, unit=unit, propositions=propositions: normalize_semantic_audit(raw, unit, propositions),
                )
            else:
                semantic = normalize_semantic_audit(semantic_audit(unit.text, combined_unit), unit, propositions)
            records.append(
                stage_record(
                    stage_id=f"{unit.unit_id}-post-repair-audit-{repair_attempts}",
                    responsibility="re-audit the repaired current unit before assembly",
                    unit_id=unit.unit_id,
                    input_payload={
                        "pre_repair_exact": pre_repair_exact,
                        "pre_repair_semantic": pre_repair_semantic,
                        "repair_output_identity": records[-1].output_identity,
                    },
                    output_payload={"exact": exact, "semantic": semantic},
                    model_call=driver == "openai-responses",
                )
            )
            last_audit_stage_id = records[-1].stage_id
            bind_consumer(records, current_candidate_stage_id, last_audit_stage_id, "repaired_candidate")
        if not exact["ok"] or semantic_requires_repair(semantic):
            raise RuntimeError(
                f"{unit.unit_id} failed closed after bounded targeted repair "
                f"(exact_ok={bool(exact['ok'])}, critical_semantic={int(semantic.get('critical_violation_count', 0))})"
            )
        unit_gate_stage_ids[unit.unit_id] = last_audit_stage_id
        unit_candidate_stage_ids[unit.unit_id] = current_candidate_stage_id
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
    known_unit_ids = {unit.unit_id for unit in units}
    if driver == "openai-responses":
        reader_review = call_openai_json_validated(
            "candidate-only-reader-review",
            (
                "Review only the candidate text for reader comprehension. The source text is intentionally unavailable. "
                "Return whether a technically trained reader can answer the required questions without decoding internal workflow labels. "
                "Each questions[] item must include boolean answerable and non-empty inferred_answer."
            ),
            reader_packet,
            model=model,
            api_key=api_key,
            required=["decision", "questions", "findings"],
            validator=lambda raw: normalize_reader_review(raw, known_unit_ids),
        )
    else:
        reader_review = normalize_reader_review(deterministic_reader_review(candidate, [unit.unit_id for unit in units]), known_unit_ids)
    records.append(
        stage_record(
            stage_id="candidate-only-reader-review",
            responsibility="review candidate only against reader questions; source is not visible",
            unit_id=None,
            input_payload=reader_packet,
            output_payload={"source_visible": False, "candidate_sha256": sha256_text(candidate), "review": reader_review},
            model_call=driver == "openai-responses",
        )
    )
    reader_review_stage_id = "candidate-only-reader-review"
    for unit in units:
        bind_consumer(records, unit_gate_stage_ids[unit.unit_id], reader_review_stage_id, "audited_candidate_unit")
    reader_repair_round = 0
    while reader_review["decision"] == "REVISE" and reader_repair_round < 2:
        reader_repair_round += 1
        previous_reader_review_stage_id = reader_review_stage_id
        repair_unit_ids = [str(item.get("unit_id")) for item in reader_review.get("findings", []) if item.get("unit_id")]
        if not repair_unit_ids:
            repair_unit_ids = [unit.unit_id for unit in units]
        for unit_id in sorted(set(repair_unit_ids)):
            unit_index = next((i for i, unit in enumerate(units) if unit.unit_id == unit_id), None)
            if unit_index is None:
                continue
            unit = units[unit_index]
            payload = {
                "unit": asdict(unit),
                "candidate_unit": rewritten_units[unit_index],
                "meaning_card": unit_cards[unit_id],
                "reader_review": reader_review,
            }
            if driver == "openai-responses":
                repaired = call_openai_json_validated(
                    f"{unit_id}-reader-targeted-repair",
                    (
                        "Repair this unit only for reader effort and clarity while preserving the Meaning Card and all source facts. "
                        "Return the structured writer JSON fields. source_coverage_ids must include every source proposition id from the Meaning Card."
                    ),
                    payload,
                    model=model,
                    api_key=api_key,
                    required=["reader_core", "technical_trace", "source_coverage_ids", "relocated_trace_ids"],
                    validator=lambda raw, unit=unit, props=unit_propositions[unit_id]: normalize_writer_result(raw, unit, props),
                )
            else:
                repaired = normalize_writer_result(apply_textual_repair(rewritten_units[unit_index], "先说明具体研究含义，再保留必要术语。"), unit, unit_propositions[unit_id])
            records.append(
                stage_record(
                    stage_id=f"{unit_id}-reader-targeted-repair-{reader_repair_round}",
                    responsibility="repair a unit because candidate-only reader review returned REVISE",
                    unit_id=unit_id,
                    input_payload=payload,
                    output_payload=repaired,
                    model_call=driver == "openai-responses",
                )
            )
            reader_repair_stage_id = records[-1].stage_id
            bind_consumer(records, previous_reader_review_stage_id, reader_repair_stage_id, "reader_findings")
            bind_consumer(records, unit_candidate_stage_ids[unit_id], reader_repair_stage_id, "candidate_unit")
            rewritten_units[unit_index] = repaired
            unit_candidate_stage_ids[unit_id] = reader_repair_stage_id
            combined_unit = "\n\n".join(part for part in [repaired["reader_core"], repaired["technical_trace"]] if part)
            exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=repaired["reader_core"])
            if not exact["ok"]:
                restored = restore_exact_literals(repaired, exact)
                records.append(
                    stage_record(
                        stage_id=f"{unit_id}-reader-exact-literal-restoration-{reader_repair_round}",
                        responsibility="restore missing exact literals from source ledger after reader-targeted repair",
                        unit_id=unit_id,
                        input_payload={"pre_restore_exact": exact, "repair_output_identity": records[-1].output_identity},
                        output_payload=restored,
                        model_call=False,
                    )
                )
                restore_stage_id = records[-1].stage_id
                bind_consumer(records, unit_candidate_stage_ids[unit_id], restore_stage_id, "reader_repair_candidate")
                rewritten_units[unit_index] = restored
                unit_candidate_stage_ids[unit_id] = restore_stage_id
                repaired = restored
                combined_unit = "\n\n".join(part for part in [repaired["reader_core"], repaired["technical_trace"]] if part)
                exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=repaired["reader_core"])
            if driver == "openai-responses":
                semantic = call_openai_json_validated(
                    f"{unit_id}-reader-repair-semantic-audit",
                    (
                        "Audit semantic preservation after reader-targeted repair. Return PASS or REVISE with findings. "
                        "Each finding must use one of these statuses: preserved, narrowed, broadened, reversed, invented, omitted, reattributed."
                    ),
                    {"source_unit": unit.text, "candidate": repaired, "meaning_card": unit_cards[unit_id], "exact": exact},
                    model=model,
                    api_key=api_key,
                    required=["decision", "findings"],
                    validator=lambda raw, unit=unit, props=unit_propositions[unit_id]: normalize_semantic_audit(raw, unit, props),
                )
            else:
                semantic = normalize_semantic_audit(semantic_audit(unit.text, combined_unit), unit, unit_propositions[unit_id])
            records.append(
                stage_record(
                    stage_id=f"{unit_id}-reader-repair-audit-{reader_repair_round}",
                    responsibility="re-verify exact literal and semantic preservation after reader-targeted repair",
                    unit_id=unit_id,
                    input_payload={"source_sha256": sha256_text(unit.text), "candidate": repaired, "meaning_card": unit_cards[unit_id]},
                    output_payload={"exact": exact, "semantic": semantic},
                    model_call=driver == "openai-responses",
                )
            )
            reader_repair_audit_stage_id = records[-1].stage_id
            bind_consumer(records, unit_candidate_stage_ids[unit_id], reader_repair_audit_stage_id, "repaired_candidate")
            if exact["ok"] and semantic_requires_repair(semantic):
                semantic_repair_payload = {
                    "unit": asdict(unit),
                    "candidate_unit": repaired,
                    "meaning_card": unit_cards[unit_id],
                    "exact": exact,
                    "semantic": semantic,
                }
                if driver == "openai-responses":
                    semantic_repaired = call_openai_json_validated(
                        f"{unit_id}-reader-semantic-targeted-repair",
                        (
                            "Repair this unit only for semantic preservation after reader-targeted repair. "
                            "Address only critical semantic findings while preserving reader clarity, exact literals, and all source facts. "
                            "Return the structured writer JSON fields. source_coverage_ids must include every source proposition id from the Meaning Card."
                        ),
                        semantic_repair_payload,
                        model=model,
                        api_key=api_key,
                        required=["reader_core", "technical_trace", "source_coverage_ids", "relocated_trace_ids"],
                        validator=lambda raw, unit=unit, props=unit_propositions[unit_id]: normalize_writer_result(raw, unit, props),
                    )
                else:
                    semantic_repaired = normalize_writer_result(
                        apply_textual_repair(repaired, "修正语义审计指出的关键范围、条件、比较或结论强度问题。"),
                        unit,
                        unit_propositions[unit_id],
                    )
                records.append(
                    stage_record(
                        stage_id=f"{unit_id}-reader-semantic-targeted-repair-{reader_repair_round}",
                        responsibility="repair a reader-targeted unit only for remaining critical semantic findings",
                        unit_id=unit_id,
                        input_payload=semantic_repair_payload,
                        output_payload=semantic_repaired,
                        model_call=driver == "openai-responses",
                    )
                )
                semantic_repair_stage_id = records[-1].stage_id
                bind_consumer(records, reader_repair_audit_stage_id, semantic_repair_stage_id, "semantic_findings")
                bind_consumer(records, unit_candidate_stage_ids[unit_id], semantic_repair_stage_id, "candidate_unit")
                rewritten_units[unit_index] = semantic_repaired
                unit_candidate_stage_ids[unit_id] = semantic_repair_stage_id
                repaired = semantic_repaired
                combined_unit = "\n\n".join(part for part in [repaired["reader_core"], repaired["technical_trace"]] if part)
                exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=repaired["reader_core"])
                if not exact["ok"]:
                    restored = restore_exact_literals(repaired, exact)
                    records.append(
                        stage_record(
                            stage_id=f"{unit_id}-reader-semantic-exact-literal-restoration-{reader_repair_round}",
                            responsibility="restore missing exact literals from source ledger after reader semantic repair",
                            unit_id=unit_id,
                            input_payload={"pre_restore_exact": exact, "repair_output_identity": records[-1].output_identity},
                            output_payload=restored,
                            model_call=False,
                        )
                    )
                    restore_stage_id = records[-1].stage_id
                    bind_consumer(records, unit_candidate_stage_ids[unit_id], restore_stage_id, "reader_semantic_repair_candidate")
                    rewritten_units[unit_index] = restored
                    unit_candidate_stage_ids[unit_id] = restore_stage_id
                    repaired = restored
                    combined_unit = "\n\n".join(part for part in [repaired["reader_core"], repaired["technical_trace"]] if part)
                    exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=repaired["reader_core"])
                if semantic_requires_repair(semantic):
                    restored = restore_semantic_findings(repaired, semantic, unit_propositions[unit_id])
                    if restored is not repaired:
                        records.append(
                            stage_record(
                                stage_id=f"{unit_id}-reader-semantic-source-restoration-{reader_repair_round}",
                                responsibility="restore source-backed proposition text for critical semantic findings after reader semantic repair",
                                unit_id=unit_id,
                                input_payload={
                                    "pre_restore_semantic": semantic,
                                    "candidate_output_identity": records[-1].output_identity,
                                },
                                output_payload=restored,
                                model_call=False,
                            )
                        )
                        restore_stage_id = records[-1].stage_id
                        bind_consumer(records, unit_candidate_stage_ids[unit_id], restore_stage_id, "reader_semantic_candidate_before_source_restoration")
                        bind_consumer(records, reader_repair_audit_stage_id, restore_stage_id, "semantic_findings")
                        rewritten_units[unit_index] = restored
                        unit_candidate_stage_ids[unit_id] = restore_stage_id
                        repaired = restored
                        combined_unit = "\n\n".join(part for part in [repaired["reader_core"], repaired["technical_trace"]] if part)
                        exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=repaired["reader_core"])
                if driver == "openai-responses":
                    semantic = call_openai_json_validated(
                        f"{unit_id}-reader-semantic-repair-audit",
                        (
                            "Re-audit semantic preservation after the reader semantic repair. Return PASS or REVISE with findings. "
                            "Each finding must use one of these statuses: preserved, narrowed, broadened, reversed, invented, omitted, reattributed."
                        ),
                        {"source_unit": unit.text, "candidate": repaired, "meaning_card": unit_cards[unit_id], "exact": exact},
                        model=model,
                        api_key=api_key,
                        required=["decision", "findings"],
                        validator=lambda raw, unit=unit, props=unit_propositions[unit_id]: normalize_semantic_audit(raw, unit, props),
                    )
                else:
                    semantic = normalize_semantic_audit(semantic_audit(unit.text, combined_unit), unit, unit_propositions[unit_id])
                records.append(
                    stage_record(
                        stage_id=f"{unit_id}-reader-semantic-repair-audit-{reader_repair_round}",
                        responsibility="re-verify exact literal and semantic preservation after reader semantic repair",
                        unit_id=unit_id,
                        input_payload={"source_sha256": sha256_text(unit.text), "candidate": repaired, "meaning_card": unit_cards[unit_id]},
                        output_payload={"exact": exact, "semantic": semantic},
                        model_call=driver == "openai-responses",
                    )
                )
                reader_repair_audit_stage_id = records[-1].stage_id
                bind_consumer(records, unit_candidate_stage_ids[unit_id], reader_repair_audit_stage_id, "reader_semantic_repaired_candidate")
                if exact["ok"] and semantic_requires_repair(semantic):
                    restored = restore_semantic_findings(repaired, semantic, unit_propositions[unit_id])
                    if restored is not repaired:
                        records.append(
                            stage_record(
                                stage_id=f"{unit_id}-reader-semantic-post-audit-source-restoration-{reader_repair_round}",
                                responsibility="restore source-backed proposition text for critical findings from the reader semantic repair audit",
                                unit_id=unit_id,
                                input_payload={
                                    "pre_restore_semantic": semantic,
                                    "candidate_output_identity": records[-1].output_identity,
                                },
                                output_payload=restored,
                                model_call=False,
                            )
                        )
                        restore_stage_id = records[-1].stage_id
                        bind_consumer(records, unit_candidate_stage_ids[unit_id], restore_stage_id, "reader_semantic_repaired_candidate_before_post_audit_restoration")
                        bind_consumer(records, reader_repair_audit_stage_id, restore_stage_id, "semantic_findings")
                        rewritten_units[unit_index] = restored
                        unit_candidate_stage_ids[unit_id] = restore_stage_id
                        repaired = restored
                        combined_unit = "\n\n".join(part for part in [repaired["reader_core"], repaired["technical_trace"]] if part)
                        exact = verify_exact(unit.text, combined_unit, unit.literal_invariants, reader_core=repaired["reader_core"])
                        if driver == "openai-responses":
                            semantic = call_openai_json_validated(
                                f"{unit_id}-reader-semantic-post-restore-audit",
                                (
                                    "Re-audit semantic preservation after source-backed restoration of the reader semantic repair. "
                                    "Return PASS or REVISE with findings. Each finding must use one of these statuses: "
                                    "preserved, narrowed, broadened, reversed, invented, omitted, reattributed."
                                ),
                                {"source_unit": unit.text, "candidate": repaired, "meaning_card": unit_cards[unit_id], "exact": exact},
                                model=model,
                                api_key=api_key,
                                required=["decision", "findings"],
                                validator=lambda raw, unit=unit, props=unit_propositions[unit_id]: normalize_semantic_audit(raw, unit, props),
                            )
                        else:
                            semantic = normalize_semantic_audit(semantic_audit(unit.text, combined_unit), unit, unit_propositions[unit_id])
                        records.append(
                            stage_record(
                                stage_id=f"{unit_id}-reader-semantic-post-restore-audit-{reader_repair_round}",
                                responsibility="re-verify exact literal and semantic preservation after source-backed restoration",
                                unit_id=unit_id,
                                input_payload={"source_sha256": sha256_text(unit.text), "candidate": repaired, "meaning_card": unit_cards[unit_id]},
                                output_payload={"exact": exact, "semantic": semantic},
                                model_call=driver == "openai-responses",
                            )
                        )
                        reader_repair_audit_stage_id = records[-1].stage_id
                        bind_consumer(records, unit_candidate_stage_ids[unit_id], reader_repair_audit_stage_id, "reader_semantic_post_restore_candidate")
            if not exact["ok"] or semantic_requires_repair(semantic):
                raise RuntimeError(
                    f"{unit_id} reader-targeted repair failed fidelity gate "
                    f"(exact_ok={bool(exact['ok'])}, critical_semantic={int(semantic.get('critical_violation_count', 0))})"
                )
            unit_gate_stage_ids[unit_id] = reader_repair_audit_stage_id
        reader_core = "\n\n".join(item["reader_core"] for item in rewritten_units if item["reader_core"]).strip()
        traces = "\n\n".join(item["technical_trace"] for item in rewritten_units if item["technical_trace"]).strip()
        candidate = reader_core if not traces else f"{reader_core}\n\n## Technical / Evidence Appendix\n\n{traces}\n"
        reader_packet = reader_review_packet(candidate, doc_map["audience"])
        if driver == "openai-responses":
            reader_review = call_openai_json_validated(
                "candidate-only-reader-review-rerun",
                "Re-review only the repaired candidate text for reader comprehension. Return PASS or REVISE.",
                reader_packet,
                model=model,
                api_key=api_key,
                required=["decision", "questions", "findings"],
                validator=lambda raw: normalize_reader_review(raw, known_unit_ids),
            )
        else:
            reader_review = normalize_reader_review(deterministic_reader_review(candidate, [unit.unit_id for unit in units]), known_unit_ids)
        records.append(
            stage_record(
                stage_id=f"candidate-only-reader-review-rerun-{reader_repair_round}",
                responsibility="re-review candidate only after reader-targeted unit repair",
                unit_id=None,
                input_payload=reader_packet,
                output_payload={"source_visible": False, "candidate_sha256": sha256_text(candidate), "review": reader_review},
                model_call=driver == "openai-responses",
            )
        )
        reader_review_stage_id = records[-1].stage_id
        for unit in units:
            bind_consumer(records, unit_gate_stage_ids[unit.unit_id], reader_review_stage_id, "audited_candidate_unit")
    if reader_review["decision"] == "REVISE":
        raise RuntimeError("candidate-only reader review failed closed after bounded repair")
    assembly_input = {
        "assembled_reader_core": reader_core,
        "assembled_technical_trace": traces,
        "unit_boundaries": [
            {"unit_id": unit.unit_id, "candidate_sha256": sha256_text(rewritten_units[index]["reader_core"])}
            for index, unit in enumerate(units)
        ],
    }
    if driver == "openai-responses":
        assembly_review = call_openai_json_validated(
            "final-assembly-coherence",
            (
                "Check final assembly coherence using the actual candidate text, transitions, terminology, repeated definitions, "
                "heading quality, local style outliers and conclusion progression. Do not rewrite the whole document."
            ),
            assembly_input,
            model=model,
            api_key=api_key,
            required=["decision", "findings"],
            validator=lambda raw: normalize_assembly_review(raw, known_unit_ids),
        )
    else:
        assembly_review = normalize_assembly_review(deterministic_assembly_review(candidate), known_unit_ids)
    records.append(
        stage_record(
            stage_id="final-assembly-coherence",
            responsibility="final assembly of rewritten units and transition/terminology check without whole-document free rewrite",
            unit_id=None,
            input_payload=assembly_input,
            output_payload={
                "reader_core_sha256": sha256_text(reader_core),
                "technical_trace_sha256": sha256_text(traces),
                "review": assembly_review,
            },
            model_call=driver == "openai-responses",
            terminal_output=assembly_review["decision"] != "REVISE",
        )
    )
    bind_consumer(records, reader_review_stage_id, "final-assembly-coherence", "reader_review_gate")
    assembly_review_stage_id = "final-assembly-coherence"
    assembly_repair_round = 0
    while assembly_review["decision"] == "REVISE" and assembly_repair_round < ASSEMBLY_REPAIR_ROUNDS:
        assembly_repair_round += 1
        previous_assembly_review_stage_id = assembly_review_stage_id
        assembly_repair_stage_id = (
            "final-assembly-targeted-repair"
            if assembly_repair_round == 1
            else f"final-assembly-targeted-repair-{assembly_repair_round}"
        )
        assembly_rerun_stage_id = (
            "final-assembly-coherence-rerun"
            if assembly_repair_round == 1
            else f"final-assembly-coherence-rerun-{assembly_repair_round}"
        )
        assembly_repair_input = {
            "assembled_reader_core": reader_core,
            "assembled_technical_trace": traces,
            "assembly_findings": assembly_review["findings"],
            "unit_boundaries": assembly_input["unit_boundaries"],
            "repair_round": assembly_repair_round,
            "literal_ledger": [span for unit in units for span in unit.literal_invariants],
            "constraints": [
                "repair only transitions, repeated definitions, headings, local style outliers, and conclusion progression",
                "do not introduce new facts, remove source-bound facts, or perform a whole-document free rewrite",
                "preserve exact numbers, formulas, citations, file paths, code identifiers, model names, dates, and method names",
            ],
        }
        expected_assembly_finding_ids = {
            str(item.get("finding_id", ""))
            for item in assembly_review["findings"]
            if isinstance(item, dict) and str(item.get("finding_id", "")).strip()
        }
        if driver == "openai-responses":
            assembly_repair = call_openai_json_validated(
                assembly_repair_stage_id,
                (
                    "Repair the assembled candidate only for the listed final assembly findings. "
                    "Keep the unit-level scientific content and exact source-bound literals intact. "
                    "Address every supplied assembly finding explicitly through local transitions, headings, terminology alignment, or conclusion progression only. "
                    "Return bounded JSON with reader_core, technical_trace, applied_finding_ids, and optional touched_unit_ids."
                ),
                assembly_repair_input,
                model=model,
                api_key=api_key,
                required=["reader_core", "technical_trace", "applied_finding_ids"],
                validator=lambda raw, expected=expected_assembly_finding_ids: normalize_assembly_repair(raw, known_unit_ids, expected),
            )
        else:
            assembly_repair = normalize_assembly_repair(
                deterministic_assembly_repair(reader_core, traces, assembly_review),
                known_unit_ids,
                expected_assembly_finding_ids,
            )
        reader_core = assembly_repair["reader_core"].strip()
        traces = assembly_repair["technical_trace"].strip()
        candidate = reader_core if not traces else f"{reader_core}\n\n## Technical / Evidence Appendix\n\n{traces}\n"
        assembly_exact = verify_exact(source, candidate, reader_core=reader_core)
        if not assembly_exact["ok"]:
            restored = restore_exact_literals({"reader_core": reader_core, "technical_trace": traces}, assembly_exact)
            reader_core = restored["reader_core"].strip()
            traces = restored["technical_trace"].strip()
            candidate = reader_core if not traces else f"{reader_core}\n\n## Technical / Evidence Appendix\n\n{traces}\n"
            assembly_exact = verify_exact(source, candidate, reader_core=reader_core)
            assembly_repair["reader_core"] = reader_core
            assembly_repair["technical_trace"] = traces
            assembly_repair["deterministic_exact_literal_restoration"] = True
        else:
            assembly_repair["deterministic_exact_literal_restoration"] = False
        records.append(
            stage_record(
                stage_id=assembly_repair_stage_id,
                responsibility="bounded final assembly repair for transitions, terminology and coherence without whole-document free rewrite",
                unit_id=None,
                input_payload=assembly_repair_input,
                output_payload={
                    "reader_core_sha256": sha256_text(reader_core),
                    "technical_trace_sha256": sha256_text(traces),
                    "applied_finding_ids": assembly_repair["applied_finding_ids"],
                    "touched_unit_ids": assembly_repair.get("touched_unit_ids", []),
                    "deterministic_exact_literal_restoration": assembly_repair["deterministic_exact_literal_restoration"],
                    "exact": assembly_exact,
                },
                model_call=driver == "openai-responses",
            )
        )
        bind_consumer(records, previous_assembly_review_stage_id, assembly_repair_stage_id, "assembly_findings")
        for unit in units:
            bind_consumer(records, unit_gate_stage_ids[unit.unit_id], assembly_repair_stage_id, "audited_candidate_unit")
        repaired_assembly_input = {
            "assembled_reader_core": reader_core,
            "assembled_technical_trace": traces,
            "unit_boundaries": assembly_input["unit_boundaries"],
            "previous_review_findings": assembly_review["findings"],
            "applied_finding_ids": assembly_repair["applied_finding_ids"],
            "exact_after_repair": assembly_exact,
            "repair_round": assembly_repair_round,
        }
        if driver == "openai-responses":
            assembly_review = call_openai_json_validated(
                assembly_rerun_stage_id,
                (
                    "Check final assembly coherence after the bounded repair. "
                    "Verify that transitions, terminology, heading quality, local style outliers and conclusion progression are now acceptable. "
                    "Do not request a whole-document free rewrite. Do not repeat a previous finding as REVISE if its applied_finding_ids show it was addressed "
                    "and no concrete remaining blocker is visible in the repaired candidate."
                ),
                repaired_assembly_input,
                model=model,
                api_key=api_key,
                required=["decision", "findings"],
                validator=lambda raw: normalize_assembly_review(raw, known_unit_ids),
            )
        else:
            assembly_review = normalize_assembly_review(deterministic_assembly_review(candidate), known_unit_ids)
        records.append(
            stage_record(
                stage_id=assembly_rerun_stage_id,
                responsibility="re-check final assembly coherence after bounded assembly repair",
                unit_id=None,
                input_payload=repaired_assembly_input,
                output_payload={
                    "reader_core_sha256": sha256_text(reader_core),
                    "technical_trace_sha256": sha256_text(traces),
                    "review": assembly_review,
                },
                model_call=driver == "openai-responses",
                terminal_output=assembly_review["decision"] != "REVISE",
            )
        )
        bind_consumer(records, assembly_repair_stage_id, assembly_rerun_stage_id, "repaired_assembly")
        assembly_review_stage_id = assembly_rerun_stage_id
    if assembly_review["decision"] == "REVISE":
        final_exact = verify_exact(source, candidate, reader_core=reader_core)
        if not final_exact["ok"]:
            raise RuntimeError("final assembly review returned REVISE after bounded repair budget with exact literal drift")
        adjudication_stage_id = "final-assembly-human-style-gate-adjudication"
        records.append(
            stage_record(
                stage_id=adjudication_stage_id,
                responsibility=(
                    "preserve bounded assembly review evidence and hand the repaired candidate to the frozen human style gate "
                    "after unit fidelity, semantic, reader and exact gates remain satisfied"
                ),
                unit_id=None,
                input_payload={
                    "final_assembly_review_stage_id": assembly_review_stage_id,
                    "final_assembly_review": assembly_review,
                    "candidate_sha256": sha256_text(candidate),
                    "exact_after_bounded_assembly_repairs": final_exact,
                    "repair_rounds_used": assembly_repair_round,
                },
                output_payload={
                    "decision": "AWAIT_HUMAN_STYLE_REVIEW",
                    "reason": "bounded assembly repairs exhausted; remaining assembly findings are retained for the user style gate",
                    "unresolved_final_assembly_finding_count": len(assembly_review.get("findings", [])),
                },
                terminal_output=True,
            )
        )
        bind_consumer(records, assembly_review_stage_id, adjudication_stage_id, "bounded_repair_exhausted_review")
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
    receipt["dataflow_validation"] = validate_dataflow(receipt)
    if not receipt["dataflow_validation"]["ok"]:
        raise RuntimeError("production dataflow validation failed")
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
