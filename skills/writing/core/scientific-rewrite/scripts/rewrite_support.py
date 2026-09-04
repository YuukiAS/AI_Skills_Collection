#!/usr/bin/env python3
"""Deterministic support for host-Codex scientific rewrites.

The helper is deliberately not a writer. The current host Codex session owns
document understanding, meaning cards, candidate prose, semantic self-audit,
repair, and assembly. This file provides only mechanical checks and
privacy-safe receipts for those host-authored stage artifacts.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any


RUNTIME_SCHEMA = "SCIENTIFIC_REWRITE_HOST_CODEX_STAGE_RECEIPT_V1"
RUNTIME_NAME = "scientific-rewrite.host-codex.v1"
REPO_ROOT = Path(__file__).resolve().parents[5]
SEED_LIBRARY = Path(__file__).resolve().parents[1] / "references" / "seed-transformations.json"
SEMANTIC_FIELDS = [
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
EVIDENCE_CLASSES = {
    "project_fact",
    "literature_fact",
    "research_interpretation",
    "candidate_method",
    "still_unverified",
}
INFORMATION_SHAPES = {
    "prose",
    "short_list",
    "table",
    "formula_walkthrough",
    "technical_trace",
}
ENGLISH_SPAN_CLASSES = {
    "exact_identity",
    "useful_recognition",
    "ordinary_reasoning",
}
LATIN_SPAN_INVENTORY_SCHEMA = "SCIENTIFIC_REWRITE_LATIN_SPAN_INVENTORY_V1"
RAW_LITERAL_DUMP_PATTERNS = [
    r"保留.{0,6}精确.{0,4}项",
    r"缺失.{0,4}精确.{0,4}项",
    r"literal\s+dump",
    r"raw\s+literal",
]


@dataclasses.dataclass(frozen=True)
class RewriteUnit:
    unit_id: str
    heading: str
    text: str
    start_line: int
    end_line: int
    literal_invariants: list[dict[str, str]]
    source_span_ids: list[str]
    argument_role: str
    why_these_spans_belong_together: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_seed_library(path: Path = SEED_LIBRARY) -> list[dict[str, Any]]:
    data = load_json(path)
    if not isinstance(data, list):
        raise RuntimeError("seed transformation library must be a JSON list")
    return data


def select_examples(
    library: list[dict[str, Any]],
    *,
    limit: int = 4,
    scene: str = "",
    discourse_function: str = "",
    rewrite_problem: str = "",
    fidelity_risk: str = "",
    register: str = "",
) -> list[dict[str, Any]]:
    if limit < 1:
        raise ValueError("limit must be positive")
    targets = {
        "scene": scene,
        "discourse_function": discourse_function,
        "rewrite_problem": rewrite_problem,
        "fidelity_risk": fidelity_risk,
        "register": register,
    }
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for item in library:
        score = sum(1 for key, value in targets.items() if value and item.get(key) == value)
        scored.append((score, str(item.get("id", "")), item))
    selected: list[dict[str, Any]] = []
    seen_functions: set[str] = set()
    for _score, _item_id, item in sorted(scored, key=lambda row: (-row[0], row[1])):
        if len(selected) >= limit:
            break
        function = str(item.get("discourse_function", ""))
        if len(selected) < min(2, limit) and function in seen_functions:
            continue
        selected.append(item)
        seen_functions.add(function)
    if len(selected) < min(limit, len(library)):
        chosen = {item.get("id") for item in selected}
        for _score, _item_id, item in sorted(scored, key=lambda row: (-row[0], row[1])):
            if len(selected) >= limit:
                break
            if item.get("id") not in chosen:
                selected.append(item)
                chosen.add(item.get("id"))
    return selected


def _literal_role(text: str) -> str:
    if "/" in text or text.startswith("`") or re.match(r"^[A-Za-z0-9_.-]+\.(json|md|py|pt|ckpt|txt)$", text):
        return "relocatable-trace"
    return "inline-critical"


def extract_literal_invariants(text: str) -> list[dict[str, str]]:
    atomic_specs = [
        r"`[^`\n]+`",
        r"(\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))",
        r"(?:^|\s)(/[^\s，。；；,]+)",
        r"(?:^|\s)([A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+)",
        r"\[[0-9,\-\s]+\]",
        r"\b[A-Za-z][A-Za-z0-9_]*=[0-9.]+\b",
        r"([𝑅𝑈𝑀𝜃𝑘𝑗𝑧𝑤𝐹𝐻𝐿ℓ𝑔𝑝𝑦𝑥𝐷𝛥𝑖∇⊤∣∑∫∥][^\n。；]*[=≈≤≥≪∑∫∥][^\n。；]*)",
    ]
    nested_specs = [
        r"\b\d{4}-\d{2}-\d{2}\b",
        r"\b\d+(?:\.\d+)?%?\b",
        r"\b[A-Z](?:&[A-Z][a-z]?)+\b",
        r"\b(?:[A-Z]{2,}[A-Za-z0-9-]*|[A-Za-z]+[A-Z][A-Za-z0-9-]*|[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)\b",
    ]
    seen: set[str] = set()
    literals: list[dict[str, str]] = []
    protected_spans: list[tuple[int, int]] = []

    def add_match(match: re.Match[str], *, protect: bool) -> None:
        group_index = 1 if match.lastindex else 0
        value = match.group(group_index).strip()
        start, end = match.span(group_index)
        if not value or value in seen:
            return
        if _span_overlaps((start, end), protected_spans):
            return
        seen.add(value)
        literals.append({"text": value, "sha256": sha256_text(value), "role": _literal_role(value)})
        if protect:
            protected_spans.append((start, end))

    for pattern in atomic_specs:
        for match in re.finditer(pattern, text):
            add_match(match, protect=True)
    for pattern in nested_specs:
        for match in re.finditer(pattern, text):
            add_match(match, protect=False)
    return literals


def _span_overlaps(span: tuple[int, int], protected_spans: list[tuple[int, int]]) -> bool:
    start, end = span
    return any(start < protected_end and end > protected_start for protected_start, protected_end in protected_spans)


def split_markdown_units(text: str, *, max_paragraphs_per_unit: int = 4) -> list[RewriteUnit]:
    lines = text.splitlines()
    blocks: list[tuple[str, int, int]] = []
    start: int | None = None
    current: list[str] = []
    for index, line in enumerate(lines, start=1):
        if line.strip():
            if start is None:
                start = index
            current.append(line)
        elif current:
            blocks.append(("\n".join(current).strip(), start or index, index - 1))
            start = None
            current = []
    if current:
        blocks.append(("\n".join(current).strip(), start or len(lines), len(lines)))

    units: list[RewriteUnit] = []
    group: list[tuple[str, int, int]] = []

    def flush() -> None:
        if not group:
            return
        unit_index = len(units) + 1
        unit_text = "\n\n".join(item[0] for item in group)
        heading = next((item[0] for item in group if item[0].lstrip().startswith("#")), "")
        start_line = group[0][1]
        end_line = group[-1][2]
        units.append(
            RewriteUnit(
                unit_id=f"unit-{unit_index:03d}",
                heading=heading,
                text=unit_text,
                start_line=start_line,
                end_line=end_line,
                literal_invariants=extract_literal_invariants(unit_text),
                source_span_ids=[f"span-{unit_index:03d}"],
                argument_role=_guess_argument_role(unit_text),
                why_these_spans_belong_together="bounded contiguous argument unit",
            )
        )
        group.clear()

    for block in blocks:
        is_heading = block[0].lstrip().startswith("#")
        if is_heading and group:
            flush()
        group.append(block)
        paragraph_count = sum(1 for item in group if not item[0].lstrip().startswith("#"))
        char_count = sum(len(item[0]) for item in group)
        if paragraph_count >= max_paragraphs_per_unit or char_count > 2800:
            flush()
    flush()
    return units


def _guess_argument_role(text: str) -> str:
    lowered = text.lower()
    if any(token in text for token in ["下一步", "GO", "STOP", "决策", "实验"]):
        return "decision-or-next-experiment"
    if any(token in text for token in ["比较", "vs", "基线", "方法", "机制"]):
        return "comparison"
    if any(token in text for token in ["结果", "证据", "指标", "观察到"]):
        return "evidence-or-result"
    if "uncertain" in lowered or "不确定" in text:
        return "uncertainty"
    return "scientific-explanation"


def proposition_inventory(unit: RewriteUnit) -> list[dict[str, Any]]:
    chunks = [part.strip() for part in re.split(r"(?<=[。！？；;])\s*", unit.text) if part.strip()]
    if not chunks:
        chunks = [unit.text.strip()]
    props: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks, start=1):
        props.append(
            {
                "proposition_id": f"{unit.unit_id}-prop-{index:03d}",
                "kind": _guess_argument_role(chunk),
                "source_span_ids": unit.source_span_ids,
                "source_text_sha256": sha256_text(chunk),
                "required": True,
            }
        )
    return props


def verify_exact(
    source: str,
    candidate: str,
    ledger: list[dict[str, str]] | None = None,
    *,
    reader_core: str | None = None,
) -> dict[str, Any]:
    invariants = ledger if ledger is not None else extract_literal_invariants(source)
    if _contains_raw_literal_dump(candidate):
        return {
            "schema": "SCIENTIFIC_REWRITE_EXACT_VERIFICATION_V1",
            "ok": False,
            "literal_count": len(invariants),
            "missing": [],
            "missing_inline_core": [],
            "raw_literal_dump": True,
        }
    missing: list[dict[str, str]] = []
    missing_inline_core: list[dict[str, str]] = []
    core = candidate if reader_core is None else reader_core
    for item in invariants:
        literal = item["text"]
        if literal not in candidate:
            missing.append(item)
        if item.get("role") == "inline-critical" and literal not in core:
            missing_inline_core.append(item)
    return {
        "schema": "SCIENTIFIC_REWRITE_EXACT_VERIFICATION_V1",
        "ok": not missing and not missing_inline_core,
        "literal_count": len(invariants),
        "missing": missing,
        "missing_inline_core": missing_inline_core,
        "raw_literal_dump": False,
    }


def _contains_raw_literal_dump(text: str) -> bool:
    return any(re.search(pattern, text, re.I) for pattern in RAW_LITERAL_DUMP_PATTERNS)


def reader_facing_core(candidate: str) -> str:
    lines = candidate.splitlines()
    kept: list[str] = []
    in_appendix = False
    appendix_heading = re.compile(r"^\s{0,3}#{1,6}\s+.*(?:technical|trace|appendix|evidence appendix|附录|技术细节|证据附录|复现|路径|文件身份)", re.I)
    any_heading = re.compile(r"^\s{0,3}#{1,6}\s+")
    for line in lines:
        if appendix_heading.search(line):
            in_appendix = True
            continue
        if in_appendix and any_heading.search(line) and not appendix_heading.search(line):
            in_appendix = False
        if not in_appendix:
            kept.append(line)
    return "\n".join(kept)


def _protected_text_mask(text: str) -> list[bool]:
    mask = [False] * len(text)
    patterns = [
        r"```[\s\S]*?```",
        r"`[^`\n]+`",
        r"\$\$[\s\S]*?\$\$",
        r"\$[^$\n]+\$",
        r"\\\[[\s\S]*?\\\]",
        r"\\\([\s\S]*?\\\)",
        r"\[[0-9,\-\s]+\]",
        r"https?://[^\s，。；,]+",
        r"(?<!\w)/(?:[^\s，。；,]+)",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text):
            for index in range(match.start(), min(match.end(), len(mask))):
                mask[index] = True
    return mask


def _is_machine_latin_span(value: str) -> bool:
    compact = value.replace(" ", "")
    if len(compact) >= 16 and re.fullmatch(r"[0-9a-fA-F]+", compact):
        return True
    if re.fullmatch(r"[A-Z0-9_]+", compact) and len(compact) >= 12:
        return True
    return False


def enumerate_latin_spans(candidate: str) -> dict[str, Any]:
    """Enumerate visible Latin-script spans outside code, math, paths, and citations."""
    mask = _protected_text_mask(candidate)
    spans: list[dict[str, Any]] = []
    pattern = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*(?:[ \t]+[A-Za-z][A-Za-z0-9_.-]*)*")
    for match in pattern.finditer(candidate):
        start, end = match.span()
        if any(mask[start:end]):
            continue
        text = match.group(0).strip()
        if not text or _is_machine_latin_span(text):
            continue
        span_sha = sha256_text(text)
        occurrence_seed = f"{start}:{end}:{text}"
        spans.append(
            {
                "occurrence_id": f"latin-{len(spans) + 1:04d}-{sha256_text(occurrence_seed)[:12]}",
                "start": start,
                "end": end,
                "text": text,
                "text_sha256": span_sha,
            }
        )
    return {
        "schema": LATIN_SPAN_INVENTORY_SCHEMA,
        "candidate_sha256": sha256_text(candidate),
        "span_count": len(spans),
        "spans": spans,
    }


def validate_latin_span_inventory(inventory: dict[str, Any], candidate: str) -> dict[str, Any]:
    expected = enumerate_latin_spans(candidate)
    if inventory.get("schema") != LATIN_SPAN_INVENTORY_SCHEMA:
        raise RuntimeError("latin_span_inventory schema mismatch")
    if inventory.get("candidate_sha256") != expected["candidate_sha256"]:
        raise RuntimeError("latin_span_inventory candidate_sha256 mismatch")
    spans = inventory.get("spans")
    if not isinstance(spans, list):
        raise RuntimeError("latin_span_inventory spans must be a list")
    projected = [
        {
            "occurrence_id": item.get("occurrence_id"),
            "start": item.get("start"),
            "end": item.get("end"),
            "text": item.get("text"),
            "text_sha256": item.get("text_sha256"),
        }
        for item in spans
    ]
    expected_projected = [
        {
            "occurrence_id": item["occurrence_id"],
            "start": item["start"],
            "end": item["end"],
            "text": item["text"],
            "text_sha256": item["text_sha256"],
        }
        for item in expected["spans"]
    ]
    if projected != expected_projected:
        raise RuntimeError("latin_span_inventory does not match mechanically enumerated spans")
    if inventory.get("span_count") != len(spans):
        raise RuntimeError("latin_span_inventory span_count mismatch")
    if len({item["occurrence_id"] for item in spans}) != len(spans):
        raise RuntimeError("latin_span_inventory occurrence ids must be unique")
    return {
        "ok": True,
        "span_count": len(spans),
        "text_sha256s": sorted({item["text_sha256"] for item in spans}),
    }


def reader_review_packet(candidate: str, audience: str) -> dict[str, Any]:
    return {
        "schema": "SCIENTIFIC_REWRITE_CANDIDATE_ONLY_READER_PACKET_V1",
        "source_visible": False,
        "audience": audience,
        "candidate_text": candidate,
        "reader_questions": [
            "What question is this passage trying to answer?",
            "What evidence is already available?",
            "What remains uncertain?",
            "What comparison or experiment resolves it?",
            "What result means GO or STOP?",
        ],
    }


def normalize_reader_review(raw: dict[str, Any], unit_ids: set[str] | None = None) -> dict[str, Any]:
    findings = raw.get("findings") or []
    questions = []
    for item in raw.get("questions") or []:
        answerable = item.get("answerable")
        if isinstance(answerable, str):
            answerable = answerable.strip().lower() in {"true", "yes", "pass", "answerable"}
        questions.append(
            {
                "answerable": bool(answerable),
                "inferred_answer": item.get("inferred_answer") or "未明确回答。",
            }
        )
    if unit_ids is not None:
        for finding in findings:
            unit_id = finding.get("unit_id")
            if unit_id and unit_id not in unit_ids:
                raise RuntimeError(f"reader finding references unknown unit: {unit_id}")
    decision = "PASS" if str(raw.get("decision", "")).upper() == "PASS" and not findings and all(q["answerable"] for q in questions) else "REVISE"
    return {"decision": decision, "questions": questions, "findings": findings}


def normalize_meaning_card(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    if raw.get("unit_id") != unit.unit_id:
        raise RuntimeError("meaning-card unit_id mismatch")
    if _contains_forbidden_source_copy_key(raw):
        raise RuntimeError("meaning-card contains forbidden source-copy field")
    for key in ["reader_job", "plain_meaning", "reader_takeaway", "rewrite_problem", "discourse_function"]:
        if not str(raw.get(key, "")).strip():
            raise RuntimeError(f"meaning-card missing required field: {key}")
        if _looks_like_source_copy(str(raw.get(key, "")), unit.text):
            raise RuntimeError(f"meaning-card {key} looks like copied source prose")
    valid_props = {item["proposition_id"] for item in propositions}
    covered: set[str] = set()
    for field in SEMANTIC_FIELDS:
        for item in raw.get(field, []):
            meaning = str(item.get("normalized_meaning", "")).strip()
            if not meaning:
                raise RuntimeError("meaning-card semantic item missing normalized_meaning")
            if _looks_like_source_copy(meaning, unit.text):
                raise RuntimeError("meaning-card semantic item looks like copied source prose")
            evidence_class = str(item.get("evidence_class", "")).strip()
            if evidence_class not in EVIDENCE_CLASSES:
                raise RuntimeError(f"meaning-card semantic item has invalid evidence_class: {evidence_class}")
            prop_ids = item.get("source_proposition_ids")
            if not prop_ids:
                raise RuntimeError("meaning-card semantic item missing source_proposition_ids")
            for prop_id in prop_ids:
                if prop_id not in valid_props:
                    raise RuntimeError(f"meaning-card references unknown proposition: {prop_id}")
                covered.add(prop_id)
    missing = sorted(valid_props - covered)
    if missing:
        raise RuntimeError("meaning-card omitted source propositions: " + ", ".join(missing))
    return raw


def _contains_forbidden_source_copy_key(value: Any) -> bool:
    if isinstance(value, dict):
        for key, item in value.items():
            if str(key) in {"source_excerpt", "source_text", "original_excerpt", "copied_source_excerpt"}:
                return True
            if _contains_forbidden_source_copy_key(item):
                return True
    if isinstance(value, list):
        return any(_contains_forbidden_source_copy_key(item) for item in value)
    return False


def _looks_like_source_copy(value: str, source: str) -> bool:
    normalized_value = re.sub(r"\s+", "", value)
    normalized_source = re.sub(r"\s+", "", source)
    return len(normalized_value) >= 24 and normalized_value in normalized_source


def normalize_semantic_audit(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    aliases = {"missing": "omitted", "partially-preserved": "narrowed", "changed": "broadened"}
    allowed = {"preserved", "narrowed", "broadened", "reversed", "invented", "omitted", "reattributed"}
    prop_ids = {item["proposition_id"] for item in propositions}
    findings = []
    critical = 0
    for finding in raw.get("findings", []):
        status = aliases.get(str(finding.get("status")), str(finding.get("status")))
        if status not in allowed:
            raise RuntimeError(f"semantic audit status is invalid: {status}")
        prop_id = finding.get("proposition_id")
        if prop_id and prop_id not in prop_ids:
            raise RuntimeError(f"semantic audit references unknown proposition: {prop_id}")
        normalized = dict(finding)
        normalized["status"] = status
        if normalized.get("severity") == "critical":
            critical += 1
        findings.append(normalized)
    decision = "PASS" if str(raw.get("decision", "")).upper() == "PASS" and critical == 0 and not findings else "REVISE"
    return {"decision": decision, "findings": findings, "critical_violation_count": critical}


def validate_dataflow(receipt: dict[str, Any]) -> dict[str, Any]:
    records = receipt.get("stage_records", [])
    stage_ids = {item.get("stage_id") for item in records}
    unused = [item.get("stage_id") for item in records if item.get("unused_output")]
    dangling: list[dict[str, str]] = []
    for item in records:
        for consumer in item.get("downstream_consumers", []):
            if consumer.get("stage_id") not in stage_ids:
                dangling.append({"from": item.get("stage_id", ""), "to": consumer.get("stage_id", "")})
    return {"ok": not unused and not dangling, "unused_outputs": unused, "dangling_consumers": dangling}


def validate_argument_coverage(source: str, units: list[dict[str, Any]]) -> dict[str, Any]:
    expected_spans = [span for unit in split_markdown_units(source) for span in unit.source_span_ids]
    owners: dict[str, list[str]] = {}
    for unit in units:
        unit_id = str(unit.get("unit_id"))
        source_span_ids = unit.get("source_span_ids") or []
        if not source_span_ids:
            raise RuntimeError(f"argument unit missing source_span_ids: {unit_id}")
        for span_id in source_span_ids:
            owners.setdefault(str(span_id), []).append(unit_id)
    missing = sorted(set(expected_spans) - set(owners))
    unknown = sorted(set(owners) - set(expected_spans))
    duplicates = {span_id: unit_ids for span_id, unit_ids in owners.items() if len(unit_ids) > 1}
    if missing:
        raise RuntimeError("argument plan omitted source spans: " + ", ".join(missing))
    if unknown:
        raise RuntimeError("argument plan references unknown source spans: " + ", ".join(unknown))
    if duplicates:
        raise RuntimeError("argument plan duplicates source spans: " + ", ".join(sorted(duplicates)))
    return {"ok": True, "source_span_count": len(expected_spans), "unit_count": len(units)}


def validate_reader_plan(reader_plan: dict[str, Any], document_map_sha256: str, units: list[dict[str, Any]]) -> dict[str, Any]:
    if reader_plan.get("document_map_sha256") != document_map_sha256:
        raise RuntimeError("reader_plan document_map_sha256 does not match current document map")
    reader_questions = reader_plan.get("reader_questions")
    if not isinstance(reader_questions, list) or not reader_questions:
        raise RuntimeError("reader_plan must contain reader_questions")
    bundles = reader_plan.get("bundles")
    if not isinstance(bundles, list) or not bundles:
        raise RuntimeError("reader_plan must contain bundles")
    bundle_order = [str(item) for item in reader_plan.get("bundle_order", [])]
    bundle_ids = [str(bundle.get("bundle_id")) for bundle in bundles]
    if set(bundle_order) != set(bundle_ids) or len(bundle_order) != len(bundle_ids):
        raise RuntimeError("reader_plan bundle_order must cover every bundle exactly once")
    if len(set(bundle_ids)) != len(bundle_ids):
        raise RuntimeError("reader_plan duplicates bundle ids")

    expected_units = {str(unit.get("unit_id")) for unit in units}
    expected_spans = {str(span_id) for unit in units for span_id in unit.get("source_span_ids", [])}
    unit_owners: dict[str, list[str]] = {}
    span_owners: dict[str, list[str]] = {}
    shape_counts = {shape: 0 for shape in INFORMATION_SHAPES}
    reshaped_count = 0
    non_contiguous_bundle_count = 0
    for bundle in bundles:
        bundle_id = str(bundle.get("bundle_id"))
        if not bundle_id or bundle_id == "None":
            raise RuntimeError("reader_plan bundle missing bundle_id")
        if not str(bundle.get("reader_question", "")).strip():
            raise RuntimeError(f"reader_plan bundle missing reader_question: {bundle_id}")
        if not str(bundle.get("reader_effort_action", "")).strip():
            raise RuntimeError(f"reader_plan bundle missing reader_effort_action: {bundle_id}")
        shape = str(bundle.get("information_shape", "")).strip()
        if shape not in INFORMATION_SHAPES:
            raise RuntimeError(f"reader_plan bundle has invalid information_shape: {shape}")
        shape_counts[shape] += 1
        if str(bundle.get("expansion_policy", "")).strip() in {"expand", "split", "table", "list"}:
            reshaped_count += 1
        for unit_id in bundle.get("unit_ids") or []:
            unit_owners.setdefault(str(unit_id), []).append(bundle_id)
        spans = [str(span_id) for span_id in (bundle.get("source_span_ids") or [])]
        if len(spans) > 1:
            numeric = []
            for span_id in spans:
                match = re.fullmatch(r"span-(\d+)", span_id)
                if match:
                    numeric.append(int(match.group(1)))
            if len(numeric) > 1 and sorted(numeric) != list(range(min(numeric), max(numeric) + 1)):
                non_contiguous_bundle_count += 1
        for span_id in spans:
            span_owners.setdefault(span_id, []).append(bundle_id)

    missing_units = sorted(expected_units - set(unit_owners))
    unknown_units = sorted(set(unit_owners) - expected_units)
    duplicate_units = {unit_id: owners for unit_id, owners in unit_owners.items() if len(owners) > 1}
    if missing_units:
        raise RuntimeError("reader_plan omitted argument units: " + ", ".join(missing_units))
    if unknown_units:
        raise RuntimeError("reader_plan references unknown argument units: " + ", ".join(unknown_units))
    if duplicate_units:
        raise RuntimeError("reader_plan duplicates argument units: " + ", ".join(sorted(duplicate_units)))

    missing_spans = sorted(expected_spans - set(span_owners))
    unknown_spans = sorted(set(span_owners) - expected_spans)
    duplicate_spans = {span_id: owners for span_id, owners in span_owners.items() if len(owners) > 1}
    if missing_spans:
        raise RuntimeError("reader_plan omitted source spans: " + ", ".join(missing_spans))
    if unknown_spans:
        raise RuntimeError("reader_plan references unknown source spans: " + ", ".join(unknown_spans))
    if duplicate_spans:
        raise RuntimeError("reader_plan duplicates source spans: " + ", ".join(sorted(duplicate_spans)))

    english_policy = reader_plan.get("english_span_policy")
    if not isinstance(english_policy, dict):
        raise RuntimeError("reader_plan missing english_span_policy")
    missing_classes = sorted(ENGLISH_SPAN_CLASSES - set(english_policy))
    if missing_classes:
        raise RuntimeError("reader_plan english_span_policy missing classes: " + ", ".join(missing_classes))
    for key in ENGLISH_SPAN_CLASSES:
        if not isinstance(english_policy.get(key), list):
            raise RuntimeError(f"reader_plan english_span_policy must use lists: {key}")

    return {
        "ok": True,
        "question_count": len(reader_questions),
        "bundle_count": len(bundles),
        "bundle_order": bundle_order,
        "information_shape_counts": shape_counts,
        "expanded_or_reshaped_bundle_count": reshaped_count,
        "non_contiguous_bundle_count": non_contiguous_bundle_count,
        "english_span_policy_classes": sorted(ENGLISH_SPAN_CLASSES),
    }


def validate_global_assembly(assembly: dict[str, Any], unit_ids: set[str]) -> dict[str, Any]:
    if not isinstance(assembly, dict):
        raise RuntimeError("missing final_assembly evidence")
    reader_order = [str(item) for item in assembly.get("reader_order_unit_ids", [])]
    if set(reader_order) != unit_ids or len(reader_order) != len(unit_ids):
        raise RuntimeError("global_assembly reader_order_unit_ids must cover every unit exactly once")
    strategy = str(assembly.get("strategy", "")).strip()
    if not strategy:
        raise RuntimeError("global_assembly missing strategy")
    if assembly.get("reader_plan_consumed") is not True:
        raise RuntimeError("global_assembly must consume the Reader Plan")
    source_order = [str(item) for item in assembly.get("source_unit_order", [])]
    planned_order = [str(item) for item in assembly.get("planned_reader_order", [])]
    if set(source_order) != unit_ids or len(source_order) != len(unit_ids):
        raise RuntimeError("global_assembly source_unit_order must cover every unit exactly once")
    if set(planned_order) != unit_ids or len(planned_order) != len(unit_ids):
        raise RuntimeError("global_assembly planned_reader_order must cover every unit exactly once")
    if not isinstance(assembly.get("information_shape_decisions"), list) or not assembly["information_shape_decisions"]:
        raise RuntimeError("global_assembly missing information_shape_decisions")
    return {
        "ok": True,
        "reader_order_unit_ids": reader_order,
        "source_unit_order": source_order,
        "planned_reader_order": planned_order,
        "reordered_from_source_order": reader_order != source_order,
        "strategy": strategy,
        "reader_plan_consumed": True,
        "information_shape_decision_count": len(assembly["information_shape_decisions"]),
    }


def validate_chinese_reader_pass(
    chinese_pass: dict[str, Any],
    final_candidate: str,
    *,
    latin_inventory: dict[str, Any],
    literal_invariants: list[dict[str, Any]],
) -> dict[str, Any]:
    if chinese_pass.get("candidate_sha256") != sha256_text(final_candidate):
        raise RuntimeError("chinese_reader_pass candidate_sha256 mismatch")
    if chinese_pass.get("source_visible") is not False:
        raise RuntimeError("chinese_reader_pass must be candidate-only")
    if str(chinese_pass.get("decision", "")).upper() != "PASS":
        raise RuntimeError("chinese_reader_pass decision must be PASS")
    for key in [
        "answerability",
        "reader_effort",
        "english_span_classification",
        "information_shape_check",
        "formula_context_check",
        "epistemic_boundary_check",
    ]:
        if not isinstance(chinese_pass.get(key), dict):
            raise RuntimeError(f"chinese_reader_pass missing object: {key}")
    reader_effort = chinese_pass["reader_effort"]
    if str(reader_effort.get("decision", "")).upper() != "PASS":
        raise RuntimeError("chinese_reader_pass reader_effort decision must be PASS")
    if reader_effort.get("minimum_reader_inference_burden") is not True:
        raise RuntimeError("chinese_reader_pass must check minimum reader inference burden")
    if reader_effort.get("not_compression_metric") is not True:
        raise RuntimeError("chinese_reader_pass must reject compression as the readability metric")
    english = chinese_pass["english_span_classification"]
    missing_classes = sorted(ENGLISH_SPAN_CLASSES - set(english))
    if missing_classes:
        raise RuntimeError("chinese_reader_pass english classification missing classes: " + ", ".join(missing_classes))
    spans = latin_inventory.get("spans", [])
    inventory_by_id = {str(item.get("occurrence_id")): item for item in spans}
    covered: dict[str, str] = {}
    exact_literal_shas = {str(item.get("sha256")) for item in literal_invariants}
    accepted_text_shas: set[str] = set()
    for key in ENGLISH_SPAN_CLASSES:
        if not isinstance(english.get(key), list):
            raise RuntimeError(f"chinese_reader_pass english classification must use lists: {key}")
        for entry in english[key]:
            if not isinstance(entry, dict):
                raise RuntimeError("chinese_reader_pass english classifications must use occurrence objects")
            occurrence_id = str(entry.get("occurrence_id", "")).strip()
            if occurrence_id not in inventory_by_id:
                raise RuntimeError(f"chinese_reader_pass references unknown Latin occurrence: {occurrence_id}")
            if occurrence_id in covered:
                raise RuntimeError(f"chinese_reader_pass duplicates Latin occurrence: {occurrence_id}")
            reason = str(entry.get("reason", "")).strip()
            if not reason:
                raise RuntimeError(f"chinese_reader_pass missing reason for Latin occurrence: {occurrence_id}")
            span = inventory_by_id[occurrence_id]
            if key == "exact_identity":
                identity_authority = str(entry.get("identity_authority", "")).strip()
                if not identity_authority and span.get("text_sha256") not in exact_literal_shas:
                    raise RuntimeError(f"exact_identity lacks identity authority: {occurrence_id}")
                accepted_text_shas.add(str(span.get("text_sha256")))
            elif key == "useful_recognition":
                chinese_context = str(entry.get("chinese_context", "")).strip()
                if not chinese_context:
                    raise RuntimeError(f"useful_recognition lacks Chinese context: {occurrence_id}")
                accepted_text_shas.add(str(span.get("text_sha256")))
            else:
                raise RuntimeError(f"ordinary_reasoning Latin occurrence remains unresolved: {occurrence_id}")
            covered[occurrence_id] = key
    missing_coverage = sorted(set(inventory_by_id) - set(covered))
    if missing_coverage:
        raise RuntimeError("chinese_reader_pass omitted Latin occurrences: " + ", ".join(missing_coverage))
    final_inventory = enumerate_latin_spans(final_candidate)
    unknown_final = [
        item["occurrence_id"]
        for item in final_inventory["spans"]
        if item["text_sha256"] not in accepted_text_shas
    ]
    if unknown_final:
        raise RuntimeError("final candidate has unclassified Latin spans after Chinese reader pass: " + ", ".join(unknown_final))
    return {
        "ok": True,
        "candidate_only": True,
        "decision": "PASS",
        "reader_effort_decision": "PASS",
        "english_span_policy_classes": sorted(ENGLISH_SPAN_CLASSES),
        "classified_latin_occurrence_count": len(covered),
        "final_latin_span_count": final_inventory["span_count"],
    }


def validate_host_stage_package(source: str, stage_dir: Path, *, candidate_path: Path | None = None) -> dict[str, Any]:
    required_files = [
        "document_map.json",
        "reader_plan.json",
        "argument_units.json",
        "fidelity_ledger.json",
        "selected_transformations.json",
        "self_audit.json",
        "final_assembly.json",
        "assembled_candidate_before_chinese_pass.md",
        "latin_span_inventory.json",
        "chinese_reader_pass.json",
        "final_candidate.md",
        "post_chinese_self_audit.json",
    ]
    missing_files = [name for name in required_files if not (stage_dir / name).is_file()]
    if missing_files:
        raise RuntimeError("missing host stage files: " + ", ".join(missing_files))

    document_map_path = stage_dir / "document_map.json"
    reader_plan_path = stage_dir / "reader_plan.json"
    argument_units_path = stage_dir / "argument_units.json"
    selected_transformations_path = stage_dir / "selected_transformations.json"
    self_audit_path = stage_dir / "self_audit.json"
    final_assembly_path = stage_dir / "final_assembly.json"
    assembled_before_path = stage_dir / "assembled_candidate_before_chinese_pass.md"
    latin_inventory_path = stage_dir / "latin_span_inventory.json"
    chinese_reader_pass_path = stage_dir / "chinese_reader_pass.json"
    post_chinese_self_audit_path = stage_dir / "post_chinese_self_audit.json"
    final_candidate_path = stage_dir / "final_candidate.md"

    document_map = load_json(document_map_path)
    reader_plan = load_json(reader_plan_path)
    argument_units = load_json(stage_dir / "argument_units.json")
    fidelity_ledger = load_json(stage_dir / "fidelity_ledger.json")
    selected_transformations = load_json(stage_dir / "selected_transformations.json")
    self_audit = load_json(stage_dir / "self_audit.json")
    final_assembly = load_json(final_assembly_path)
    latin_span_inventory = load_json(latin_inventory_path)
    chinese_reader_pass = load_json(chinese_reader_pass_path)
    post_chinese_self_audit = load_json(post_chinese_self_audit_path)
    assembled_before_chinese = assembled_before_path.read_text(encoding="utf-8")
    final_candidate = final_candidate_path.read_text(encoding="utf-8")
    if candidate_path is not None and final_candidate != candidate_path.read_text(encoding="utf-8"):
        raise RuntimeError("candidate path does not match stage final_candidate.md")

    source_sha = sha256_text(source)
    if document_map.get("source_sha256") and document_map["source_sha256"] != source_sha:
        raise RuntimeError("document_map source_sha256 does not match source")
    units = argument_units.get("units", [])
    if not units:
        raise RuntimeError("argument_units.json must contain at least one unit")
    unit_ids = {str(unit.get("unit_id")) for unit in units}
    argument_coverage = validate_argument_coverage(source, units)
    selected_by_unit = selected_transformations.get("by_unit", {})
    audit_units = {str(item.get("unit_id")): item for item in self_audit.get("unit_audits", [])}
    document_map_sha = sha256_bytes(document_map_path.read_bytes())
    reader_plan_validation = validate_reader_plan(reader_plan, document_map_sha, units)
    latin_inventory_validation = validate_latin_span_inventory(latin_span_inventory, assembled_before_chinese)
    candidate_unit_shas: dict[str, str] = {}
    mechanical_units = {unit.unit_id: unit for unit in split_markdown_units(source)}
    for unit in units:
        unit_id = str(unit.get("unit_id"))
        if not unit_id or unit_id == "None":
            raise RuntimeError("argument unit missing unit_id")
        unit_source_sha = str(unit.get("source_unit_sha256", ""))
        if not unit_source_sha:
            raise RuntimeError(f"argument unit missing source_unit_sha256: {unit_id}")
        card_path = stage_dir / "meaning_cards" / f"{unit_id}.json"
        candidate_unit_path = stage_dir / "candidate_units" / f"{unit_id}.md"
        if not card_path.is_file():
            raise RuntimeError(f"missing meaning card for {unit_id}")
        if not candidate_unit_path.is_file():
            raise RuntimeError(f"missing candidate unit for {unit_id}")
        semantic_audit_path = stage_dir / "semantic_audits" / f"{unit_id}.json"
        if not semantic_audit_path.is_file():
            raise RuntimeError(f"missing semantic audit for {unit_id}")
        card = load_json(card_path)
        if card.get("unit_id") != unit_id:
            raise RuntimeError(f"meaning card unit_id mismatch for {unit_id}")
        if card.get("source_unit_sha256") != unit_source_sha:
            raise RuntimeError(f"meaning card source hash mismatch for {unit_id}")
        if card.get("document_map_sha256") != document_map_sha:
            raise RuntimeError(f"meaning card does not bind current document map for {unit_id}")
        if unit_id in mechanical_units:
            normalize_meaning_card(card, mechanical_units[unit_id], proposition_inventory(mechanical_units[unit_id]))
        if unit_id not in selected_by_unit:
            raise RuntimeError(f"selected transformations missing unit: {unit_id}")
        candidate_unit_shas[unit_id] = sha256_bytes(candidate_unit_path.read_bytes())
        semantic_audit = load_json(semantic_audit_path)
        audit = audit_units.get(unit_id)
        if not audit:
            raise RuntimeError(f"self_audit missing unit audit: {unit_id}")
        if audit.get("candidate_unit_sha256") != candidate_unit_shas[unit_id]:
            raise RuntimeError(f"self_audit candidate hash mismatch for {unit_id}")
        if semantic_audit.get("candidate_unit_sha256") != candidate_unit_shas[unit_id]:
            raise RuntimeError(f"semantic audit candidate hash mismatch for {unit_id}")
        if semantic_audit.get("unit_id") != unit_id:
            raise RuntimeError(f"semantic audit unit_id mismatch for {unit_id}")
        if str(semantic_audit.get("decision", "")).upper() != "PASS":
            raise RuntimeError(f"host semantic audit file unresolved for {unit_id}")
        if str(audit.get("decision", "")).upper() != "PASS":
            raise RuntimeError(f"host semantic self-audit unresolved for {unit_id}")
    if str(self_audit.get("decision", "")).upper() not in {"PASS", "REVISE"}:
        raise RuntimeError("self_audit decision must be PASS or REVISE")
    if str(self_audit.get("decision", "")).upper() != "PASS":
        raise RuntimeError("host semantic self-audit has unresolved findings")
    if self_audit.get("final_candidate_sha256") != sha256_text(final_candidate):
        raise RuntimeError("self_audit final_candidate_sha256 mismatch")
    if final_assembly.get("assembled_candidate_sha256") != sha256_text(assembled_before_chinese):
        raise RuntimeError("final_assembly assembled_candidate_sha256 mismatch")
    if final_assembly.get("final_candidate_sha256") != sha256_text(final_candidate):
        raise RuntimeError("final_assembly final_candidate_sha256 mismatch")
    global_assembly = validate_global_assembly(final_assembly, unit_ids)
    plan_order = [
        str(unit_id)
        for bundle_id in reader_plan_validation["bundle_order"]
        for bundle in reader_plan.get("bundles", [])
        if str(bundle.get("bundle_id")) == bundle_id
        for unit_id in bundle.get("unit_ids", [])
    ]
    if global_assembly["reader_order_unit_ids"] != plan_order:
        raise RuntimeError("global_assembly reader order must follow reader_plan bundle order")
    chinese_reader = validate_chinese_reader_pass(
        chinese_reader_pass,
        final_candidate,
        latin_inventory=latin_span_inventory,
        literal_invariants=fidelity_ledger.get("literal_invariants") or [],
    )

    if post_chinese_self_audit.get("final_candidate_sha256") != sha256_text(final_candidate):
        raise RuntimeError("post_chinese_self_audit final_candidate_sha256 mismatch")
    for key in ["exact_verification_decision", "semantic_verification_decision", "reader_effort_decision"]:
        if str(post_chinese_self_audit.get(key, "")).upper() != "PASS":
            raise RuntimeError(f"post_chinese_self_audit unresolved: {key}")

    exact = verify_exact(source, final_candidate, fidelity_ledger.get("literal_invariants"), reader_core=reader_facing_core(final_candidate))
    stage_records = _stage_records(
        stage_dir,
        document_map,
        reader_plan,
        units,
        selected_transformations,
        self_audit,
        final_assembly,
        latin_span_inventory,
        chinese_reader_pass,
        post_chinese_self_audit,
        final_candidate,
    )
    receipt = {
        "schema": RUNTIME_SCHEMA,
        "runtime": RUNTIME_NAME,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "driver": "host-codex",
        "model_call_count": 0,
        "external_api_call_count": 0,
        "requires_openai_api_key": False,
        "whole_document_writer_call": False,
        "source_sha256": source_sha,
        "candidate_sha256": sha256_text(final_candidate),
        "unit_count": len(units),
        "stage_count": len(stage_records),
        "argument_coverage": argument_coverage,
        "reader_plan": reader_plan_validation,
        "global_assembly": global_assembly,
        "latin_span_inventory": {
            "ok": latin_inventory_validation["ok"],
            "span_count": latin_inventory_validation["span_count"],
            "inventory_sha256": sha256_bytes(latin_inventory_path.read_bytes()),
        },
        "chinese_reader_pass": chinese_reader,
        "stage_records": stage_records,
        "exact_verification": exact,
        "private_plaintext_committed": False,
    }
    receipt["dataflow_validation"] = validate_dataflow(receipt)
    if not receipt["dataflow_validation"]["ok"]:
        raise RuntimeError("host stage dataflow validation failed")
    if not exact["ok"]:
        raise RuntimeError("exact verification failed")
    return {"candidate": final_candidate, "receipt": receipt}


def _stage_records(
    stage_dir: Path,
    document_map: dict[str, Any],
    reader_plan: dict[str, Any],
    units: list[dict[str, Any]],
    selected_transformations: dict[str, Any],
    self_audit: dict[str, Any],
    final_assembly: dict[str, Any],
    latin_span_inventory: dict[str, Any],
    chinese_reader_pass: dict[str, Any],
    post_chinese_self_audit: dict[str, Any],
    final_candidate: str,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    records.append(_record("document-map", stage_dir / "document_map.json", ["reader-plan"]))
    records.append(_record("reader-plan", stage_dir / "reader_plan.json", ["argument-segmentation", "final-assembly", "chinese-reader-pass"]))
    records.append(_record("argument-segmentation", stage_dir / "argument_units.json", [f"{unit['unit_id']}-meaning-card" for unit in units]))
    for unit in units:
        unit_id = str(unit["unit_id"])
        records.append(_record(f"{unit_id}-meaning-card", stage_dir / "meaning_cards" / f"{unit_id}.json", [f"{unit_id}-example-selection", f"{unit_id}-writer"]))
        records.append(_record(f"{unit_id}-example-selection", stage_dir / "selected_transformations.json", [f"{unit_id}-writer"], unit_id=unit_id))
        records.append(_record(f"{unit_id}-writer", stage_dir / "candidate_units" / f"{unit_id}.md", [f"{unit_id}-semantic-self-audit"], unit_id=unit_id))
        records.append(_record(f"{unit_id}-semantic-self-audit", stage_dir / "semantic_audits" / f"{unit_id}.json", ["self-audit"], unit_id=unit_id))
    records.append(_record("self-audit", stage_dir / "self_audit.json", ["final-assembly"]))
    records.append(_record("final-assembly", stage_dir / "final_assembly.json", ["assembled-before-chinese-pass", "chinese-reader-pass"]))
    records.append(_record("assembled-before-chinese-pass", stage_dir / "assembled_candidate_before_chinese_pass.md", ["latin-span-inventory", "chinese-reader-pass"]))
    records.append(_record("latin-span-inventory", stage_dir / "latin_span_inventory.json", ["chinese-reader-pass"]))
    records.append(_record("chinese-reader-pass", stage_dir / "chinese_reader_pass.json", ["final-candidate", "post-chinese-self-audit"]))
    records.append(_record("post-chinese-self-audit", stage_dir / "post_chinese_self_audit.json", ["final-candidate"]))
    records.append(_record("final-candidate", stage_dir / "final_candidate.md", [], terminal=True))
    return records


def _record(stage_id: str, path: Path, consumers: list[str], *, unit_id: str | None = None, terminal: bool = False) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "stage_id": stage_id,
        "unit_id": unit_id,
        "output_identity": f"{stage_id}:{sha256_bytes(data)}",
        "output_sha256": sha256_bytes(data),
        "downstream_consumers": [{"stage_id": item, "input_binding": stage_id} for item in consumers],
        "model_call": False,
        "host_codex_authored": True,
        "plaintext_committed": False,
        "terminal_output": terminal,
        "unused_output": False,
    }


def run_multistage(*_args: Any, **_kwargs: Any) -> dict[str, Any]:
    raise RuntimeError("050 host-Codex route does not let the helper generate reader-facing prose; use validate_host_stage_package")


def response_schema_name(stage: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", stage).strip("_")
    digest = sha256_text(stage)[:10]
    return (safe[:50].rstrip("_") + "_" + digest)[:64]


def command_select_examples(args: argparse.Namespace) -> None:
    selected = select_examples(
        load_seed_library(),
        limit=args.limit,
        scene=args.scene,
        discourse_function=args.discourse_function,
        rewrite_problem=args.rewrite_problem,
        fidelity_risk=args.fidelity_risk,
        register=args.register,
    )
    print(json.dumps(selected, ensure_ascii=False, indent=2, sort_keys=True))


def command_verify_exact(args: argparse.Namespace) -> None:
    source = Path(args.source).read_text(encoding="utf-8")
    candidate = Path(args.candidate).read_text(encoding="utf-8")
    report = verify_exact(source, candidate)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    if not report["ok"]:
        raise SystemExit(1)


def command_validate_host_stage(args: argparse.Namespace) -> None:
    source = Path(args.source).read_text(encoding="utf-8")
    result = validate_host_stage_package(source, Path(args.stage_dir), candidate_path=Path(args.candidate) if args.candidate else None)
    if args.receipt:
        write_json(Path(args.receipt), result["receipt"])
    print(json.dumps(result["receipt"], ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    select = sub.add_parser("select-examples")
    select.add_argument("--limit", type=int, default=4)
    select.add_argument("--scene", default="")
    select.add_argument("--discourse-function", default="")
    select.add_argument("--rewrite-problem", default="")
    select.add_argument("--fidelity-risk", default="")
    select.add_argument("--register", default="")
    select.set_defaults(func=command_select_examples)

    verify = sub.add_parser("verify-exact")
    verify.add_argument("--source", required=True)
    verify.add_argument("--candidate", required=True)
    verify.set_defaults(func=command_verify_exact)

    validate = sub.add_parser("validate-host-stage")
    validate.add_argument("--source", required=True)
    validate.add_argument("--stage-dir", required=True)
    validate.add_argument("--candidate")
    validate.add_argument("--receipt")
    validate.set_defaults(func=command_validate_host_stage)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
