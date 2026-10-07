"""Production detector functions for rendered presentation pages."""

from __future__ import annotations

import re
from typing import Any

from .features import rect_distance
from .schemas import CheckResult, DetectorSpec, check_na, check_pass, check_revise


DETECTOR_REGISTRY = [
    DetectorSpec("D-TEXT-COLLISION", "IMPLEMENTED", ["pdf_text_spans"], "TEXT_COLLISION", "non-overlapping text boxes", "overlapping text boxes", "detect_text_collision", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-TYPOGRAPHY", "IMPLEMENTED", ["pdf_text_spans", "rendered_png"], "TYPOGRAPHY_BELOW_FLOOR", "median body text at or above floor", "tiny dense body text", "detect_typography", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-OBJECT-SCALE-WHITESPACE", "IMPLEMENTED", ["rendered_png_components"], "PRIMARY_OBJECT_TOO_SMALL_WITH_LARGE_VOID", "large content region with intentional void", "small object plus large void", "detect_object_scale_whitespace", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-PEER-LAYOUT", "IMPLEMENTED", ["pdf_text_spans", "rendered_png_columns"], "PEER_COLUMN_IMBALANCE", "balanced peer regions", "one dense column with peer imbalance", "detect_peer_layout", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-READING-PATH", "IMPLEMENTED", ["pdf_text_spans", "guard_requirements"], "BROKEN_READING_PATH_OR_ORPHANED_PROSE", "vertical sequential path", "sequential job split into columns", "detect_reading_path", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-QA-GEOMETRY", "IMPLEMENTED", ["pdf_text_spans"], "QUESTION_ANSWER_GEOMETRY_BREAK", "Q/A in close vertical order", "answer detached from question", "detect_qa_geometry", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-SCIENTIFIC-OBJECT-READABILITY", "IMPLEMENTED", ["rendered_png_components", "pdf_text_spans"], "SCIENTIFIC_OBJECT_INTERNAL_UNREADABLE", "object text readable", "tiny internal object text", "detect_scientific_object_readability", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-CODE-OUTPUT-PROXIMITY", "IMPLEMENTED", ["pdf_text_spans"], "CODE_OUTPUT_DETACHED", "output near code", "output far from code", "detect_code_output_proximity", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-EVIDENCE-INTERPRETATION-PROXIMITY", "IMPLEMENTED", ["pdf_text_spans", "rendered_png_components"], "EVIDENCE_INTERPRETATION_SEPARATION", "interpretation near evidence", "interpretation stranded away from evidence", "detect_evidence_interpretation_proximity", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-SHELL-INTEGRITY", "IMPLEMENTED", ["rendered_png", "page_role"], "SHELL_REGRESSION", "shell regions present when applicable", "missing title/header/footer/closing shell", "detect_shell_integrity", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-INTERNAL-IDENTIFIER", "IMPLEMENTED", ["pdf_text_spans"], "INTERNAL_IDENTIFIER_OR_RAW_MARKUP_LEAK", "no internal identifiers", "production ids/raw markup visible", "detect_internal_identifier_leak", "REUSABLE_CANDIDATE"),
    DetectorSpec("D-PROTECTED-OBJECT-PACKET", "IMPLEMENTED", ["guard_requirements", "protected_objects"], "PROTECTED_OBJECT_REVIEW_REQUIRED", "protected object packet created", "protected object missing packet", "build_protected_object_check", "REUSABLE_CANDIDATE"),
]


def _packet_text(packet: dict[str, Any]) -> str:
    return packet.get("features", {}).get("text", {}).get("text_excerpt", "")


def detect_text_collision(packet: dict[str, Any]) -> CheckResult:
    spans = packet.get("features", {}).get("text", {}).get("spans", [])
    collisions = []
    for i, a in enumerate(spans[:500]):
        if len(a.get("text", "")) <= 1:
            continue
        for b in spans[i + 1 : min(len(spans), i + 40)]:
            if len(b.get("text", "")) <= 1:
                continue
            x_overlap = min(a["x1"], b["x1"]) - max(a["x0"], b["x0"])
            y_overlap = min(a["y1"], b["y1"]) - max(a["y0"], b["y0"])
            if x_overlap > min(a["x1"] - a["x0"], b["x1"] - b["x0"]) * 0.45 and y_overlap > 2:
                collisions.append({"a": a["text"], "b": b["text"], "bbox": [a["x0"], a["y0"], b["x1"], b["y1"]]})
    if collisions:
        return check_revise("text_collision", "TEXT_COLLISION", f"{len(collisions)} overlapping text candidates", locations=collisions[:5])
    return check_pass("text_collision", "No overlapping text boxes above collision threshold.")


def detect_typography(packet: dict[str, Any]) -> CheckResult:
    text = packet.get("features", {}).get("text", {})
    median = float(text.get("median_word_height_px") or 0)
    words = int(text.get("word_count") or 0)
    if words > 45 and median and median < 16:
        return check_revise("typography", "TYPOGRAPHY_BELOW_FLOOR", f"Median extracted word height {median:.1f}px across {words} words.")
    if words == 0:
        return check_revise("typography", "MISSING_TEXT_EXTRACTION", "No text spans were extracted from the rendered page/PDF.")
    return check_pass("typography", f"Median extracted word height is {median:.1f}px across {words} words.")


def detect_object_scale_whitespace(packet: dict[str, Any]) -> CheckResult:
    image = packet.get("features", {}).get("image", {})
    bbox_area = float(image.get("body_bbox_area_ratio") or 0)
    top_void = float(image.get("top_void_ratio") or 0)
    bottom_void = float(image.get("bottom_void_ratio") or 0)
    largest = image.get("largest_component") or {}
    largest_area = float(largest.get("area_px") or 0) / max(1, float(image.get("width", 1)) * float(image.get("height", 1)))
    if bbox_area < 0.24 and max(top_void, bottom_void) > 0.28:
        return check_revise("object_scale_whitespace", "PRIMARY_OBJECT_TOO_SMALL_WITH_LARGE_VOID", f"Body bbox area {bbox_area:.2f} with top/bottom void {top_void:.2f}/{bottom_void:.2f}.", locations=[largest] if largest else [])
    if largest_area < 0.025 and max(top_void, bottom_void) > 0.34:
        return check_revise("object_scale_whitespace", "PRIMARY_OBJECT_TOO_SMALL_WITH_LARGE_VOID", f"Largest visible component is only {largest_area:.2%} of slide with large void.")
    return check_pass("object_scale_whitespace", f"Content occupies bbox ratio {bbox_area:.2f}; largest component ratio {largest_area:.2%}.")


def detect_peer_layout(packet: dict[str, Any]) -> CheckResult:
    text = packet.get("features", {}).get("text", {})
    image = packet.get("features", {}).get("image", {})
    left = int(text.get("left_body_words") or 0)
    right = int(text.get("right_body_words") or 0)
    if left > 20 and right > 20:
        ratio = max(left, right) / max(1, min(left, right))
        if ratio > 2.4:
            return check_revise("peer_layout", "PEER_COLUMN_IMBALANCE", f"Peer-column word counts are imbalanced: left={left}, right={right}.")
        return check_pass("peer_layout", f"Peer-column word counts are balanced enough: left={left}, right={right}.")
    if max(left, right) > 40 and min(left, right) <= 25:
        return check_revise("peer_layout", "PEER_COLUMN_IMBALANCE", f"One peer region dominates the page: left={left}, right={right}.")
    if image.get("center_occupancy", 1) < 0.01 and max(left, right) > 30 and min(left, right) < 8:
        return check_revise("peer_layout", "PEER_COLUMN_IMBALANCE", f"Column gap exists but text is concentrated on one side: left={left}, right={right}.")
    return check_na("peer_layout", "No peer-column layout signal.")


def detect_reading_path(packet: dict[str, Any]) -> CheckResult:
    text = packet.get("features", {}).get("text", {})
    job = (packet.get("page_job") or "").lower()
    guard_text = " ".join(g.get("requirement", "") for g in packet.get("guards", [])).lower()
    sequential = any(token in job for token in ["derive", "sequence", "mechanism", "step", "ordered", "workflow", "update", "trace", "offset"])
    if sequential and text.get("two_column_text_signal"):
        return check_revise("reading_path", "BROKEN_READING_PATH_OR_ORPHANED_PROSE", f"Sequential job '{packet.get('page_job', '')[:80]}' conflicts with two-column text signal.")
    return check_pass("reading_path", "Reading path does not conflict with detected text geometry." if sequential else "No sequential-reading-path constraint triggered.")


def detect_qa_geometry(packet: dict[str, Any]) -> CheckResult:
    text = packet.get("features", {}).get("text", {})
    q = text.get("question_spans", [])
    a = text.get("answer_spans", [])
    job = (packet.get("page_job") or "").lower()
    targets = " ".join(packet.get("stable_targets", []) + packet.get("component_targets", [])).lower()
    qa_required = "qa" in targets or "q-a" in targets or "question" in job or "answer" in job or any(
        token in job for token in ["question/answer", "q/a", "question-answer", "answer block"]
    )
    if not q and not a:
        return check_na("q_a_geometry", "No Q/A labels detected.")
    if not q or not a:
        if qa_required:
            return check_revise("q_a_geometry", "QUESTION_ANSWER_GEOMETRY_BREAK", "Q/A structure is required but only one of Question/Answer labels is visible.")
        return check_na("q_a_geometry", "Only one of Question/Answer labels is visible, but no Q/A layout requirement applies.")
    qy = min(s["y0"] for s in q)
    ay = min(s["y0"] for s in a)
    h = float(packet.get("features", {}).get("image", {}).get("height") or 1)
    gap = (ay - qy) / h
    if gap < 0 or gap > 0.62:
        return check_revise("q_a_geometry", "QUESTION_ANSWER_GEOMETRY_BREAK", f"Question/Answer vertical gap ratio is {gap:.2f}.")
    return check_pass("q_a_geometry", f"Question/Answer labels are in plausible vertical order, gap ratio {gap:.2f}.")


def detect_scientific_object_readability(packet: dict[str, Any]) -> CheckResult:
    text = packet.get("features", {}).get("text", {})
    image = packet.get("features", {}).get("image", {})
    object_words = [s for s in text.get("spans", []) if s["y0"] > image.get("height", 0) * 0.22 and s["y1"] < image.get("height", 0) * 0.86]
    tiny = [s for s in object_words if s.get("height", 99) < 13.5]
    if len(tiny) >= 12:
        return check_revise("scientific_object_internal_readability", "SCIENTIFIC_OBJECT_INTERNAL_UNREADABLE", f"{len(tiny)} object/body text spans are below 13.5px.")
    return check_pass("scientific_object_internal_readability", f"Object/body text has {len(tiny)} tiny spans below the internal-readability warning floor.")


def detect_code_output_proximity(packet: dict[str, Any]) -> CheckResult:
    spans = packet.get("features", {}).get("text", {}).get("spans", [])
    job = (packet.get("page_job") or "").lower()
    guard_text = " ".join(g.get("requirement", "") for g in packet.get("guards", [])).lower()
    requires_output = any(token in f"{job} {guard_text}" for token in ["output", "result", "estimate", "summary", "fitted", "coefficient", "posterior"])
    code = [s for s in spans if re.search(r"\b(import|library|glm|stan|pymc|fit|summary|for|def)\b|[{}<>~=]", s.get("text", ""), re.I)]
    output = [s for s in spans if re.search(r"\b(estimate|std|error|mean|sd|rhat|ess|coef|ratio|interval)\b|\d+\.\d+", s.get("text", ""), re.I)]
    if len(code) < 4:
        return check_na("code_output_proximity", "No code-heavy page signal.")
    if not output:
        if requires_output:
            return check_revise("code_output_proximity", "CODE_OUTPUT_DETACHED", "Code/result page has no visible result/output tokens.")
        return check_na("code_output_proximity", "Code-like tokens are visible, but no result/output proximity requirement applies.")
    min_dist = min(rect_distance(c, o) for c in code[:30] for o in output[:30])
    if min_dist > 360:
        return check_revise("code_output_proximity", "CODE_OUTPUT_DETACHED", f"Nearest code/output distance is {min_dist:.0f}px.")
    return check_pass("code_output_proximity", f"Nearest code/output distance is {min_dist:.0f}px.")


def detect_evidence_interpretation_proximity(packet: dict[str, Any]) -> CheckResult:
    spans = packet.get("features", {}).get("text", {}).get("spans", [])
    evidence = [s for s in spans if re.search(r"\b(plot|figure|table|observed|estimate|interval|ratio|rhat|ess|mcse|bias|rmse)\b", s.get("text", ""), re.I)]
    interp = [s for s in spans if re.search(r"\b(therefore|suggest|means|interpret|because|shows|answer|conclusion)\b", s.get("text", ""), re.I)]
    if not evidence or not interp:
        return check_na("evidence_interpretation_proximity", "No evidence/interpretation pair signal.")
    min_dist = min(rect_distance(e, i) for e in evidence[:35] for i in interp[:35])
    if min_dist > 430:
        return check_revise("evidence_interpretation_proximity", "EVIDENCE_INTERPRETATION_SEPARATION", f"Nearest evidence/interpretation distance is {min_dist:.0f}px.")
    return check_pass("evidence_interpretation_proximity", f"Nearest evidence/interpretation distance is {min_dist:.0f}px.")


def detect_shell_integrity(packet: dict[str, Any]) -> CheckResult:
    role = packet.get("page_role") or "ordinary"
    image = packet.get("features", {}).get("image", {})
    top = float(image.get("top_void_ratio") or 0)
    bottom = float(image.get("bottom_void_ratio") or 0)
    text = _packet_text(packet).lower()
    if role == "title":
        if any(t in text for t in ["overview", "workflow", "roadmap"]):
            return check_revise("shell", "SHELL_REGRESSION", "Title page includes roadmap/workflow text.")
        return check_pass("shell", "Title shell has no ordinary roadmap/workflow leakage.")
    if role == "closing":
        if not any(t in text for t in ["question", "questions", "contact", "summary"]):
            return check_revise("shell", "SHELL_REGRESSION", "Closing page lacks visible close/contact/question signal.")
        return check_pass("shell", "Closing page has visible close/contact/question signal.")
    if top > 0.20 or bottom > 0.42:
        return check_revise("shell", "SHELL_REGRESSION", f"Ordinary page has suspicious top/bottom shell void {top:.2f}/{bottom:.2f}.")
    return check_pass("shell", f"Ordinary shell regions have plausible top/bottom void {top:.2f}/{bottom:.2f}.")


def detect_internal_identifier_leak(packet: dict[str, Any]) -> CheckResult:
    text = _packet_text(packet)
    patterns = [
        r"\bT\d{2}-[A-Z0-9-]+\b",
        r"\bPageID\b",
        r"\bfeedback[_ -]?id\b",
        r"\bTODO\b|\bFIXME\b",
        r"\\begin\{|\\end\{|<[^>]+>",
        r"\bV\d{2}\b.*\bproof\b",
        r"\bcheckpoint\b|\binternal\b|\bproduction\b",
    ]
    hits = [pat for pat in patterns if re.search(pat, text, re.I)]
    if hits:
        return check_revise("internal_identifier_or_markup_leak", "INTERNAL_IDENTIFIER_OR_RAW_MARKUP_LEAK", f"Visible text matched forbidden internal/raw patterns: {hits[:3]}.")
    return check_pass("internal_identifier_or_markup_leak", "No internal identifiers or raw markup patterns detected.")


def build_protected_object_check(packet: dict[str, Any]) -> CheckResult:
    protected = packet.get("protected_objects") or []
    if not protected:
        return check_na("protected_object", "No protected visual object in packet.")
    image = packet.get("features", {}).get("image", {})
    components = image.get("content_components", [])
    if not components:
        return check_revise("protected_object", "PROTECTED_OBJECT_PACKET_MISSING_VISIBLE_REGION", "Protected object required but no rendered components were detected.")
    return check_pass("protected_object", f"Protected-object review packet contains {len(protected)} object requirement(s) and {len(components)} visible region candidates.")


DETECTOR_FUNCTIONS = [
    detect_text_collision,
    detect_typography,
    detect_object_scale_whitespace,
    detect_peer_layout,
    detect_reading_path,
    detect_qa_geometry,
    detect_scientific_object_readability,
    detect_code_output_proximity,
    detect_evidence_interpretation_proximity,
    detect_shell_integrity,
    detect_internal_identifier_leak,
    build_protected_object_check,
]


def run_detectors(packet: dict[str, Any]) -> list[dict[str, Any]]:
    return [result.to_dict() for result in (fn(packet) for fn in DETECTOR_FUNCTIONS)]
