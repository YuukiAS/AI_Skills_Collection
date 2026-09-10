#!/usr/bin/env python3
"""Mechanical support for the writing-style heavy Chinese rewrite route.

The helper validates host-authored semantic artifacts. It deliberately does not
write reader-facing prose, derive meanings from source excerpts, or score
naturalness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any


RUNTIME_SCHEMA = "SCIENTIFIC_REWRITE_HEAVY_ROUTE_RECEIPT_V2"
RUNTIME_NAME = "scientific-rewrite.meaning-realization.v2"
ROUTE_SELECTION_SCHEMA = "SCIENTIFIC_REWRITE_ROUTE_SELECTION_V1"
MEANING_MAP_SCHEMA = "SCIENTIFIC_REWRITE_MEANING_MAP_V1"
READER_PLAN_SCHEMA = "SCIENTIFIC_REWRITE_READER_PLAN_V1"
REALIZATION_PACKET_SCHEMA = "SCIENTIFIC_REWRITE_REALIZATION_PACKET_V1"
REPAIR_PACKET_SCHEMA = "SCIENTIFIC_REWRITE_REPAIR_PACKET_V1"
ASSEMBLY_PACKET_SCHEMA = "SCIENTIFIC_REWRITE_ASSEMBLY_PACKET_V1"
SEMANTIC_AUDIT_SCHEMA = "SCIENTIFIC_REWRITE_SEMANTIC_AUDIT_V1"

RAW_SOURCE_KEYS = {
    "raw_source",
    "source",
    "source_text",
    "source_prose",
    "source_excerpt",
    "source_quote",
    "source_quotation",
    "source_sentence",
    "source_paragraph",
    "source_preview",
    "source_tail",
    "original_text",
    "original_unit",
    "target_sentence",
    "target_rewrite_sentence",
    "previous_candidate",
    "manual_reference",
    "latin_span_inventory",
    "qa_ledger",
    "seed_template",
    "seed_templates",
}
FORBIDDEN_SOURCE_VALUE_KEYS = {
    "normalized_meaning",
    "plain_meaning",
    "reader_takeaway",
    "required_semantic_correction",
}
EXACT_ITEM_CATEGORIES = {
    "formula",
    "citation",
    "path",
    "command",
    "config",
    "code",
    "api",
    "package",
    "dataset",
    "metric",
    "algorithm",
    "model",
    "formal_identity",
    "machine_token",
    "user_protected",
    "number",
}
SEMANTIC_DRIFT_STATUSES = {
    "broadened",
    "narrowed",
    "reversed",
    "invented",
    "omitted",
    "reattributed",
}
CRITICAL_FINDING_TYPES = {
    "changed_comparator",
    "dropped_caveat",
    "lost_uncertainty",
    "changed_condition",
    "wrong_attribution",
    "strengthened_conclusion",
    "reversed_polarity",
    "invented_claim",
    "omitted_meaning",
}
INTERNAL_ROUTE_TERMS = {
    "scientific-rewrite",
    "Meaning Map",
    "Reader Plan",
    "REALIZE_MEANING",
    "stage package",
    "stage packet",
    "validate-host-stage",
    "validate-stage",
}
WORKFLOW_TRACE_LITERAL_PATTERNS = [
    r"\b[0-9a-f]{40}\b",
    r"(?:^|/)automation/reviewed_handoff(?:/|$)",
    r"(?:^|/)results/\d{3}[_/][^\s，。；,]*",
    r"(?:^|/)exports/private(?:/|$)",
    r"(?:^|/)\.local-runtime(?:/|$)",
    r"(?:^|/)\.github/workflows(?:/|$)",
    r"(?:^|/)plugins/cache/[^/\s]+/writing-style/[^\s，。；,]*",
    r"\b(?:CURRENT|RESULT|FINAL_REPORT|TEXT_REVIEW)\.json\b",
    r"\b(?:RESULT|FINAL_REPORT)\.md\b",
]
READER_FACING_INTERNAL_LEAK_PATTERNS = [
    ("commit_sha", r"\b[0-9a-f]{40}\b"),
    ("reviewed_handoff_path", r"(?:^|/)automation/reviewed_handoff(?:/|$)"),
    ("task_result_path", r"(?:^|/)results/\d{3}[_/][^\s，。；,]*"),
    ("private_export_path", r"(?:^|/)exports/private(?:/|$)"),
    ("local_runtime_path", r"(?:^|/)\.local-runtime(?:/|$)"),
    ("github_actions", r"\bGitHub Actions\b|actions/runs|\.github/workflows"),
    ("workflow_state", r"\b(?:AWAIT_HUMAN_DECISION|NEEDS_GPT_PLANNER|PLAN_FROZEN|TEXT_REVIEW|READY_FOR_GPT_REVIEW)\b"),
    ("gate_label", r"\bGate\s*\d+\b|\bGate\d+\b"),
    ("dev_command", r"\b(?:git (?:commit|push|diff|status|rev-parse)|python3 -m unittest|pytest)\b"),
    ("process_review_label", r"\b(?:Planner|Reviewer|Executor)\b|规划者审核|外部规划者|本轮满足收口条件|收口条件"),
]
SOURCE_PROCESS_FRAME_PATTERNS = [
    ("source_says", r"原文(?:同时)?(?:指出|提到|说明|认为|强调|写道|给出|使用|采用|在[^。；\n]{0,24}中)"),
    ("given_material", r"根据(?:给定|上述|这些)?材料"),
    ("source_text", r"源文"),
    ("preserve_source", r"这里保留原文|保留原文(?:的)?(?:表述|说法|结构)?"),
]
SOURCE_PROCESS_ALLOWED_CONTEXT_PATTERNS = [
    r"source comparison",
    r"editing commentary",
    r"peer review",
    r"provenance",
    r"\baudit\b",
    r"源文对照",
    r"原文对照",
    r"修改意见",
    r"同行评审",
    r"审稿",
    r"溯源",
    r"审计",
]


class ValidationError(RuntimeError):
    """Raised when a host-authored heavy-rewrite artifact violates the contract."""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _iter_key_values(value: Any, path: str = ""):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            yield child_path, key, child
            yield from _iter_key_values(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _iter_key_values(child, f"{path}[{index}]")


def assert_no_raw_source_fields(payload: Any, *, context: str) -> None:
    for path, key, value in _iter_key_values(payload):
        normalized = str(key).strip().lower()
        if normalized in RAW_SOURCE_KEYS:
            raise ValidationError(f"{context} contains forbidden raw-source drafting field: {path}")
        if normalized in {"template_text", "example_source", "validator_language"}:
            raise ValidationError(f"{context} contains forbidden writer-conditioning field: {path}")
        if normalized in FORBIDDEN_SOURCE_VALUE_KEYS and isinstance(value, str):
            _reject_source_shaped_value(value, context=f"{context}.{path}")


def _reject_source_shaped_value(value: str, *, context: str) -> None:
    stripped = value.strip()
    if not stripped:
        raise ValidationError(f"{context} is missing semantic content")
    if stripped.startswith("SOURCE:") or stripped.startswith("原文"):
        raise ValidationError(f"{context} appears to be source-copy fallback")


def _contains_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def _latin_fraction(text: str) -> float:
    if not text:
        return 0.0
    latin = len(re.findall(r"[A-Za-z]", text))
    non_space = len(re.findall(r"\S", text))
    return latin / non_space if non_space else 0.0


def is_internal_workflow_trace_literal(text: str) -> bool:
    return any(re.search(pattern, text) for pattern in WORKFLOW_TRACE_LITERAL_PATTERNS)


def find_reader_facing_internal_leakage(text: str) -> list[dict[str, str]]:
    findings = []
    for name, pattern in READER_FACING_INTERNAL_LEAK_PATTERNS:
        match = re.search(pattern, text)
        if match:
            findings.append({"kind": name, "literal": match.group(0)})
    return findings


def validate_reader_facing_internal_frame(candidate: str) -> dict[str, Any]:
    findings = find_reader_facing_internal_leakage(candidate)
    if findings:
        kinds = ", ".join(finding["kind"] for finding in findings)
        raise ValidationError("reader-facing internal workflow leakage: " + kinds)
    return {"ok": True, "internal_workflow_leak_count": 0}


def _strip_code_spans(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    return re.sub(r"`[^`\n]*`", "", text)


def find_source_process_framing(text: str, *, task_context: str = "") -> list[dict[str, str]]:
    if any(re.search(pattern, task_context, flags=re.IGNORECASE) for pattern in SOURCE_PROCESS_ALLOWED_CONTEXT_PATTERNS):
        return []
    body = _strip_code_spans(text)
    findings = []
    for name, pattern in SOURCE_PROCESS_FRAME_PATTERNS:
        match = re.search(pattern, body)
        if match:
            findings.append({"kind": name, "literal": match.group(0)})
    return findings


def validate_standalone_reader_frame(candidate: str, *, task_context: str = "") -> dict[str, Any]:
    findings = find_source_process_framing(candidate, task_context=task_context)
    if findings:
        kinds = ", ".join(finding["kind"] for finding in findings)
        raise ValidationError("reader-facing source-process framing: " + kinds)
    return {"ok": True, "source_process_frame_count": 0}


def classify_writing_style_route(prompt: str, source: str) -> dict[str, Any]:
    """Return a deterministic smoke-test route classification for writing-style."""

    prompt_l = prompt.lower()
    source_l = source.lower()
    combined = f"{prompt}\n{source}"
    check_only = any(term in prompt_l for term in ["检查", "核对", "verify", "audit"]) and not any(
        term in prompt_l for term in ["改写", "重写", "rewrite", "polish", "润色"]
    )
    wants_rewrite = any(term in prompt_l for term in ["改写", "重写", "重新组织", "rewrite", "说人话", "自然中文"])
    fidelity_terms = ["数字", "公式", "引用", "比较", "限制", "条件", "caveat", "citation", "formula"]
    has_fidelity = any(term in prompt_l for term in fidelity_terms) or any(
        marker in source for marker in ["$", "[", "`"]
    )
    paragraph_count = len([block for block in re.split(r"\n\s*\n", source) if block.strip()])
    long_enough = len(source) >= 500 or paragraph_count >= 3
    scientific = any(term in source_l for term in ["dice", "method", "model", "dataset"]) or any(
        term in source for term in ["数据集", "实验", "公式", "方法", "指标", "消融", "通信"]
    )

    if check_only:
        route = "writing-fidelity"
    elif _latin_fraction(source) > 0.62 and not _contains_chinese(prompt + source):
        route = "scientific-prose"
    elif wants_rewrite and _contains_chinese(combined) and long_enough and scientific and has_fidelity:
        route = "scientific-rewrite"
    elif _contains_chinese(combined):
        route = "chinese-prose"
    else:
        route = "writing-fidelity"
    return {
        "schema": ROUTE_SELECTION_SCHEMA,
        "selector_owner": "writing-style",
        "selected_route": route,
        "forced_route": False,
        "ordinary_user_prompt": True,
        "prompt_sha256": sha256_text(prompt),
        "source_sha256": sha256_text(source),
        "reason_codes": {
            "check_only": check_only,
            "wants_rewrite": wants_rewrite,
            "has_fidelity_constraints": has_fidelity,
            "long_enough": long_enough,
            "scientific_or_technical": scientific,
            "chinese_dominant": _contains_chinese(combined),
            "english_dominant": _latin_fraction(source) > 0.62,
        },
    }


def validate_route_selection(payload: dict[str, Any], source: str, *, prompt: str | None = None) -> dict[str, Any]:
    if payload.get("schema") != ROUTE_SELECTION_SCHEMA:
        raise ValidationError("route selection schema mismatch")
    assert_no_raw_source_fields(payload, context="route selection")
    if payload.get("selector_owner") != "writing-style":
        raise ValidationError("route selection must be owned by writing-style")
    if payload.get("selected_route") != "scientific-rewrite":
        raise ValidationError("ordinary route did not select scientific-rewrite")
    if payload.get("forced_route"):
        raise ValidationError("forced scientific-rewrite entry cannot satisfy ordinary route gate")
    if payload.get("ordinary_user_prompt") is not True:
        raise ValidationError("route selection requires an ordinary user prompt")
    if payload.get("source_sha256") != sha256_text(source):
        raise ValidationError("route selection source hash mismatch")
    if prompt is not None and payload.get("prompt_sha256") != sha256_text(prompt):
        raise ValidationError("route selection prompt hash mismatch")
    internal_terms = payload.get("prompt_internal_terms") or []
    if internal_terms:
        raise ValidationError("ordinary prompt contains internal route terms: " + ", ".join(map(str, internal_terms)))
    if prompt is not None:
        found = [term for term in sorted(INTERNAL_ROUTE_TERMS) if term.lower() in prompt.lower()]
        if found:
            raise ValidationError("ordinary prompt contains internal route terms: " + ", ".join(found))
    return {
        "ok": True,
        "selector_owner": payload["selector_owner"],
        "selected_route": payload["selected_route"],
        "ordinary_user_prompt": True,
    }


def split_source_anchors(source: str) -> list[dict[str, Any]]:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", source) if block.strip()]
    if not blocks and source.strip():
        blocks = [source.strip()]
    anchors = []
    cursor = 0
    for index, block in enumerate(blocks, start=1):
        start = source.find(block, cursor)
        end = start + len(block)
        cursor = end
        anchors.append(
            {
                "source_anchor_id": f"src-{index:03d}",
                "text_sha256": sha256_text(block),
                "start": start,
                "end": end,
            }
        )
    return anchors


def extract_exact_items(source: str) -> list[dict[str, str]]:
    patterns = [
        ("formula", r"\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)"),
        ("citation", r"\[[0-9,\-\s]+\]"),
        ("path", r"(?<!\w)/(?:[^\s，。；,]+)|[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+"),
        ("config", r"`[^`\n]*[_.:/=][^`\n]*`"),
        ("machine_token", r"\b[A-Z0-9_]{3,}\b"),
        ("formal_identity", r"\b[A-Z][A-Za-z0-9]*(?:[A-Z][A-Za-z0-9]*)+\b|\b[A-Za-z]+[A-Z][A-Za-z0-9-]*\b"),
        ("metric", r"\b[A-Za-z][A-Za-z0-9_]*\s*=\s*\d+(?:\.\d+)?%?\b"),
        ("number", r"\b\d+(?:\.\d+)?%?\b"),
    ]
    seen: set[str] = set()
    items: list[dict[str, str]] = []
    for category, pattern in patterns:
        for match in re.finditer(pattern, source):
            text = match.group(0).strip("`")
            if not text or text in seen:
                continue
            if is_internal_workflow_trace_literal(text):
                continue
            seen.add(text)
            role = "relocatable-trace" if category in {"path", "config"} else "inline-critical"
            items.append(
                {
                    "exact_item_id": f"exact-{len(items) + 1:03d}",
                    "literal": text,
                    "sha256": sha256_text(text),
                    "category": category,
                    "location_role": role,
                }
            )
    return items


def validate_exact_item(item: dict[str, Any]) -> None:
    category = str(item.get("category", ""))
    literal = str(item.get("literal", ""))
    if category in {"ordinary_latin", "latin_span", "useful_recognition", "ordinary_reasoning"}:
        raise ValidationError("ordinary Latin span cannot become required exact item")
    if category not in EXACT_ITEM_CATEGORIES:
        raise ValidationError(f"unsupported exact item category: {category}")
    if category == "formal_identity" and literal and re.fullmatch(r"[a-z]+(?: [a-z]+)+", literal):
        raise ValidationError("ordinary Latin phrase cannot become exact formal identity")
    if item.get("sha256") and item["sha256"] != sha256_text(literal):
        raise ValidationError(f"exact item sha256 mismatch: {item.get('exact_item_id')}")


def validate_meaning_map(payload: dict[str, Any], source: str) -> dict[str, Any]:
    if payload.get("schema") != MEANING_MAP_SCHEMA:
        raise ValidationError("Meaning Map schema mismatch")
    if payload.get("source_sha256") != sha256_text(source):
        raise ValidationError("Meaning Map source hash mismatch")
    anchors = payload.get("source_anchors")
    meanings = payload.get("meanings")
    if not isinstance(anchors, list) or not anchors:
        raise ValidationError("Meaning Map requires source anchors")
    if not isinstance(meanings, list) or not meanings:
        raise ValidationError("Meaning Map requires host-authored meanings")
    anchor_by_id = {str(anchor.get("source_anchor_id")): anchor for anchor in anchors}
    if "" in anchor_by_id or len(anchor_by_id) != len(anchors):
        raise ValidationError("source anchors require unique ids")
    exact_items = payload.get("exact_items") or []
    exact_by_id = {str(item.get("exact_item_id")): item for item in exact_items}
    for item in exact_items:
        validate_exact_item(item)
    covered_anchors: set[str] = set()
    for meaning in meanings:
        meaning_id = str(meaning.get("meaning_id", ""))
        normalized = str(meaning.get("normalized_meaning", "")).strip()
        if not meaning_id:
            raise ValidationError("meaning missing meaning_id")
        _reject_source_shaped_value(normalized, context=f"meaning {meaning_id}.normalized_meaning")
        source_anchor_ids = [str(item) for item in meaning.get("source_anchor_ids") or []]
        if not source_anchor_ids:
            raise ValidationError(f"meaning lacks source authority: {meaning_id}")
        for anchor_id in source_anchor_ids:
            if anchor_id not in anchor_by_id:
                raise ValidationError(f"meaning references unknown source anchor: {anchor_id}")
            covered_anchors.add(anchor_id)
            anchor = anchor_by_id[anchor_id]
            anchor_text = source[int(anchor["start"]) : int(anchor["end"])].strip()
            if normalized == anchor_text or sha256_text(normalized) == anchor.get("text_sha256"):
                raise ValidationError(f"meaning is direct source-copy fallback: {meaning_id}")
        for exact_id in meaning.get("exact_item_ids") or []:
            if str(exact_id) not in exact_by_id:
                raise ValidationError(f"meaning references unknown exact item: {exact_id}")
    missing = sorted(set(anchor_by_id) - covered_anchors)
    if missing:
        raise ValidationError("source anchors lack meaning ownership: " + ", ".join(missing))
    return {
        "ok": True,
        "source_anchor_count": len(anchors),
        "meaning_count": len(meanings),
        "exact_item_count": len(exact_items),
    }


def validate_reader_plan(payload: dict[str, Any], meaning_map: dict[str, Any]) -> dict[str, Any]:
    if payload.get("schema") != READER_PLAN_SCHEMA:
        raise ValidationError("Reader Plan schema mismatch")
    assert_no_raw_source_fields(payload, context="Reader Plan")
    meaning_ids = {str(item.get("meaning_id")) for item in meaning_map.get("meanings", [])}
    exact_ids = {str(item.get("exact_item_id")) for item in meaning_map.get("exact_items", [])}
    bundles = payload.get("bundles")
    if not isinstance(bundles, list) or not bundles:
        raise ValidationError("Reader Plan requires bundles")
    bundle_ids = [str(bundle.get("bundle_id")) for bundle in bundles]
    if len(set(bundle_ids)) != len(bundle_ids) or "" in bundle_ids:
        raise ValidationError("Reader Plan bundle ids must be unique")
    if sorted(payload.get("bundle_order") or []) != sorted(bundle_ids):
        raise ValidationError("Reader Plan bundle_order must reference all bundles")
    splitter = str(payload.get("splitter", "")).lower()
    if splitter in {"fixed_chars", "fixed_paragraphs", "four_paragraphs", "4_paragraphs"}:
        raise ValidationError("fixed-size splitter cannot be the production Reader Plan")
    if "max_chars" in payload or "max_paragraphs" in payload:
        raise ValidationError("mechanical size limits may only request NEEDS_SEMANTIC_SPLIT")
    owned: set[str] = set()
    for bundle in bundles:
        owned_meaning_ids = [str(item) for item in bundle.get("owned_meaning_ids") or []]
        if not owned_meaning_ids:
            raise ValidationError(f"Reader Plan bundle lacks owned meanings: {bundle.get('bundle_id')}")
        for meaning_id in owned_meaning_ids:
            if meaning_id not in meaning_ids:
                raise ValidationError(f"Reader Plan references unknown meaning: {meaning_id}")
            owned.add(meaning_id)
        for exact_id in bundle.get("required_exact_item_ids") or []:
            if str(exact_id) not in exact_ids:
                raise ValidationError(f"Reader Plan references unknown exact item: {exact_id}")
    missing = sorted(meaning_ids - owned)
    if missing:
        raise ValidationError("Reader Plan omits meanings: " + ", ".join(missing))
    return {"ok": True, "bundle_count": len(bundles), "owned_meaning_count": len(owned)}


def validate_realization_packet(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("schema") != REALIZATION_PACKET_SCHEMA:
        raise ValidationError("realization packet schema mismatch")
    assert_no_raw_source_fields(payload, context="REALIZE_MEANING packet")
    if not payload.get("bundle_id") or not payload.get("meaning_records"):
        raise ValidationError("realization packet requires bundle_id and meaning_records")
    return {"ok": True, "bundle_id": payload["bundle_id"]}


def validate_repair_packet(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("schema") != REPAIR_PACKET_SCHEMA:
        raise ValidationError("repair packet schema mismatch")
    assert_no_raw_source_fields(payload, context="repair packet")
    if not payload.get("affected_meaning_ids") or not payload.get("required_semantic_correction"):
        raise ValidationError("repair packet requires affected meanings and structured correction")
    return {"ok": True, "bundle_id": payload.get("bundle_id")}


def validate_assembly_packet(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("schema") != ASSEMBLY_PACKET_SCHEMA:
        raise ValidationError("assembly packet schema mismatch")
    assert_no_raw_source_fields(payload, context="assembly packet")
    if not payload.get("reader_plan_sha256") or not payload.get("realized_bundle_sha256s"):
        raise ValidationError("assembly packet requires reader plan and realized bundle bindings")
    return {"ok": True, "bundle_count": len(payload.get("realized_bundle_sha256s") or [])}


def validate_semantic_audit(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("schema") != SEMANTIC_AUDIT_SCHEMA:
        raise ValidationError("semantic audit schema mismatch")
    critical = []
    for finding in payload.get("findings") or []:
        status = str(finding.get("status", "")).lower()
        finding_type = str(finding.get("finding_type", "")).lower()
        severity = str(finding.get("severity", "")).lower()
        if severity == "critical" or status in SEMANTIC_DRIFT_STATUSES or finding_type in CRITICAL_FINDING_TYPES:
            critical.append(finding)
    decision = str(payload.get("decision", "")).upper()
    if critical or decision not in {"PASS", "OK"}:
        raise ValidationError("semantic audit has unresolved critical findings")
    return {"ok": True, "finding_count": len(payload.get("findings") or [])}


def validate_structural_fidelity(payload: dict[str, Any]) -> dict[str, Any]:
    if payload.get("mode") != "STRUCTURAL_REWRITE":
        raise ValidationError("structural fidelity report must use STRUCTURAL_REWRITE mode")
    protected = set(payload.get("protected_authority") or [])
    required = {
        "claim",
        "evidence",
        "number",
        "formula",
        "citation",
        "comparator",
        "condition",
        "scope",
        "uncertainty",
        "caveat",
        "attribution",
        "conclusion_strength",
    }
    missing = sorted(required - protected)
    if missing:
        raise ValidationError("STRUCTURAL_REWRITE missing protected authority: " + ", ".join(missing))
    if any(item in protected for item in ["source_heading", "paragraph_boundary", "section_order"]):
        raise ValidationError("STRUCTURAL_REWRITE must not protect source structure by default")
    drifts = payload.get("semantic_drifts") or []
    critical = [
        drift
        for drift in drifts
        if str(drift.get("status", "")).lower() in SEMANTIC_DRIFT_STATUSES
        or str(drift.get("finding_type", "")).lower() in CRITICAL_FINDING_TYPES
    ]
    if critical:
        raise ValidationError("STRUCTURAL_REWRITE semantic authority drift")
    return {
        "ok": True,
        "structure_changed": bool(payload.get("structure_changed")),
        "semantic_drift_count": len(drifts),
    }


def verify_exact_items(candidate: str, exact_items: list[dict[str, Any]]) -> dict[str, Any]:
    missing = [item for item in exact_items if str(item.get("literal", "")) not in candidate]
    if missing:
        raise ValidationError("final candidate missing exact items: " + ", ".join(str(item.get("exact_item_id")) for item in missing))
    return {"ok": True, "exact_item_count": len(exact_items)}


def validate_stage_package(
    source: str,
    stage_dir: Path,
    *,
    receipt_path: Path | None = None,
    prompt: str | None = None,
) -> dict[str, Any]:
    route_selection = load_json(stage_dir / "route_selection.json")
    meaning_map = load_json(stage_dir / "meaning_map.json")
    reader_plan = load_json(stage_dir / "reader_plan.json")
    assembly_packet = load_json(stage_dir / "assembly_packet.json")
    semantic_audit = load_json(stage_dir / "semantic_audit.json")
    final_candidate = (stage_dir / "final_candidate.md").read_text(encoding="utf-8")
    route_result = validate_route_selection(route_selection, source, prompt=prompt)
    meaning_result = validate_meaning_map(meaning_map, source)
    reader_plan_result = validate_reader_plan(reader_plan, meaning_map)
    realization_results = []
    for packet_path in sorted((stage_dir / "realization_packets").glob("*.json")):
        realization_results.append(validate_realization_packet(load_json(packet_path)))
    if not realization_results:
        raise ValidationError("stage package requires realization packets")
    repair_results = []
    repair_dir = stage_dir / "repair_packets"
    if repair_dir.is_dir():
        for packet_path in sorted(repair_dir.glob("*.json")):
            repair_results.append(validate_repair_packet(load_json(packet_path)))
    assembly_result = validate_assembly_packet(assembly_packet)
    semantic_result = validate_semantic_audit(semantic_audit)
    exact_result = verify_exact_items(final_candidate, meaning_map.get("exact_items") or [])
    reader_frame_result = validate_reader_facing_internal_frame(final_candidate)
    standalone_frame_result = validate_standalone_reader_frame(final_candidate, task_context=prompt or "")
    receipt = {
        "schema": RUNTIME_SCHEMA,
        "runtime": RUNTIME_NAME,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_sha256": sha256_text(source),
        "candidate_sha256": sha256_text(final_candidate),
        "host_codex_owned_generation": True,
        "external_api_call_count": 0,
        "requires_openai_api_key": False,
        "paid_generation_used": False,
        "source_copy_fallback_used": False,
        "fixed_size_splitter_used": False,
        "seed_templates_used_for_realization": False,
        "private_plaintext_committed": False,
        "route_selection": route_result,
        "meaning_map": meaning_result,
        "reader_plan": reader_plan_result,
        "realization_packet_count": len(realization_results),
        "repair_packet_count": len(repair_results),
        "assembly": assembly_result,
        "semantic_audit": semantic_result,
        "exact_verification": exact_result,
        "reader_facing_internal_frame": reader_frame_result,
        "standalone_reader_frame": standalone_frame_result,
    }
    if receipt_path is not None:
        write_json(receipt_path, receipt)
    return receipt


def command_validate_stage(args: argparse.Namespace) -> None:
    source = Path(args.source).read_text(encoding="utf-8")
    prompt = Path(args.prompt).read_text(encoding="utf-8").rstrip("\n") if args.prompt else None
    receipt = validate_stage_package(
        source,
        Path(args.stage_dir),
        receipt_path=Path(args.receipt) if args.receipt else None,
        prompt=prompt,
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))


def command_exact_items(args: argparse.Namespace) -> None:
    source = Path(args.source).read_text(encoding="utf-8")
    print(json.dumps(extract_exact_items(source), ensure_ascii=False, indent=2, sort_keys=True))


def command_route_check(args: argparse.Namespace) -> None:
    prompt = Path(args.prompt).read_text(encoding="utf-8")
    source = Path(args.source).read_text(encoding="utf-8")
    print(json.dumps(classify_writing_style_route(prompt, source), ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    exact = sub.add_parser("exact-items")
    exact.add_argument("--source", required=True)
    exact.set_defaults(func=command_exact_items)
    route = sub.add_parser("route-check")
    route.add_argument("--prompt", required=True)
    route.add_argument("--source", required=True)
    route.set_defaults(func=command_route_check)
    validate = sub.add_parser("validate-stage")
    validate.add_argument("--source", required=True)
    validate.add_argument("--stage-dir", required=True)
    validate.add_argument("--prompt")
    validate.add_argument("--receipt")
    validate.set_defaults(func=command_validate_stage)
    validate_host = sub.add_parser("validate-host-stage")
    validate_host.add_argument("--source", required=True)
    validate_host.add_argument("--stage-dir", required=True)
    validate_host.add_argument("--candidate", help="Compatibility alias; candidate must be stage-dir/final_candidate.md")
    validate_host.add_argument("--prompt")
    validate_host.add_argument("--receipt")
    validate_host.set_defaults(func=command_validate_stage)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
