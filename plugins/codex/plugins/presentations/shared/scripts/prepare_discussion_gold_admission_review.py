#!/usr/bin/env python3
"""Prepare 026 discussion/next-experiment gold-admission visual inputs."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw


REPO_ROOT = Path(__file__).resolve().parents[6]
TASK_KEY = "026_research_presentation_discussion_next_experiment_gold_recovery"
VISIBLE_TASK_KEY = "026_discussion_gold_admission"
SOURCE_CACHE = REPO_ROOT / ".cache" / "research-presentation-reference-library" / "sources"
RENDER_CACHE = REPO_ROOT / ".cache" / "research-presentation-reference-library" / "inspection" / "rendered_pages"
OUT_DIR = REPO_ROOT / "results" / TASK_KEY / "visual_review" / "gold_admission_1"


CANDIDATES = [
    {
        "reference_id": "RRL-049",
        "source_id": "SRC-059",
        "title": "On the Limitations of Stochastic Pre-processing Defenses",
        "speaker": "Yue Gao, Ilia Shumailov, Kassem Fawaz, Nicolas Papernot",
        "institution": "NeurIPS 2022",
        "source_url": "https://neurips.cc/media/neurips-2022/Slides/54675.pdf",
        "local_cache_file": "neurips2022_stochastic_preprocessing_defenses.pdf",
        "actual_page_number": 24,
        "page_function": "DISCUSSION",
        "scientific_object": "discussion transition from two limitations to lessons learned",
        "evidence_type": "discussion framing",
        "rights_note": "public NeurIPS slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-050",
        "source_id": "SRC-059",
        "title": "On the Limitations of Stochastic Pre-processing Defenses",
        "speaker": "Yue Gao, Ilia Shumailov, Kassem Fawaz, Nicolas Papernot",
        "institution": "NeurIPS 2022",
        "source_url": "https://neurips.cc/media/neurips-2022/Slides/54675.pdf",
        "local_cache_file": "neurips2022_stochastic_preprocessing_defenses.pdf",
        "actual_page_number": 25,
        "page_function": "DISCUSSION",
        "scientific_object": "interpretation of stochastic defense limitations",
        "evidence_type": "discussion synthesis",
        "rights_note": "public NeurIPS slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-051",
        "source_id": "SRC-059",
        "title": "On the Limitations of Stochastic Pre-processing Defenses",
        "speaker": "Yue Gao, Ilia Shumailov, Kassem Fawaz, Nicolas Papernot",
        "institution": "NeurIPS 2022",
        "source_url": "https://neurips.cc/media/neurips-2022/Slides/54675.pdf",
        "local_cache_file": "neurips2022_stochastic_preprocessing_defenses.pdf",
        "actual_page_number": 26,
        "page_function": "NEXT_EXPERIMENT",
        "scientific_object": "future research implications for stochastic defenses",
        "evidence_type": "next research directions",
        "rights_note": "public NeurIPS slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-052",
        "source_id": "SRC-060",
        "title": "Digital Twins: Research Gaps & Future Directions",
        "speaker": "Karen E. Willcox",
        "institution": "Institute for Mathematical and Statistical Innovation",
        "source_url": "https://cdn.imsi.institute/videos/73339/pHUmxZztZj/slides.pdf",
        "landing_page_url": "https://www.imsi.institute/videos/research-gaps-and-future-directions/",
        "local_cache_file": "imsi_research_gaps_future_directions.pdf",
        "actual_page_number": 29,
        "page_function": "NEXT_EXPERIMENT",
        "scientific_object": "recommendation for continual VVUQ methods in digital twins",
        "evidence_type": "future research recommendation",
        "rights_note": "public IMSI slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-053",
        "source_id": "SRC-060",
        "title": "Digital Twins: Research Gaps & Future Directions",
        "speaker": "Karen E. Willcox",
        "institution": "Institute for Mathematical and Statistical Innovation",
        "source_url": "https://cdn.imsi.institute/videos/73339/pHUmxZztZj/slides.pdf",
        "landing_page_url": "https://www.imsi.institute/videos/research-gaps-and-future-directions/",
        "local_cache_file": "imsi_research_gaps_future_directions.pdf",
        "actual_page_number": 40,
        "page_function": "DISCUSSION",
        "scientific_object": "fitness-for-purpose tradeoffs motivating theoretical tools",
        "evidence_type": "research gap discussion",
        "rights_note": "public IMSI slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-054",
        "source_id": "SRC-060",
        "title": "Digital Twins: Research Gaps & Future Directions",
        "speaker": "Karen E. Willcox",
        "institution": "Institute for Mathematical and Statistical Innovation",
        "source_url": "https://cdn.imsi.institute/videos/73339/pHUmxZztZj/slides.pdf",
        "landing_page_url": "https://www.imsi.institute/videos/research-gaps-and-future-directions/",
        "local_cache_file": "imsi_research_gaps_future_directions.pdf",
        "actual_page_number": 43,
        "page_function": "OPEN_QUESTION",
        "scientific_object": "open question about modular digital twin formulations",
        "evidence_type": "open research question",
        "rights_note": "public IMSI slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-055",
        "source_id": "SRC-060",
        "title": "Digital Twins: Research Gaps & Future Directions",
        "speaker": "Karen E. Willcox",
        "institution": "Institute for Mathematical and Statistical Innovation",
        "source_url": "https://cdn.imsi.institute/videos/73339/pHUmxZztZj/slides.pdf",
        "landing_page_url": "https://www.imsi.institute/videos/research-gaps-and-future-directions/",
        "local_cache_file": "imsi_research_gaps_future_directions.pdf",
        "actual_page_number": 47,
        "page_function": "NEXT_EXPERIMENT",
        "scientific_object": "UQ and sensitivity analysis defining coupling/update-rate experiments",
        "evidence_type": "next design experiment",
        "rights_note": "public IMSI slide PDF; composition lessons only",
    },
    {
        "reference_id": "RRL-056",
        "source_id": "SRC-060",
        "title": "Digital Twins: Research Gaps & Future Directions",
        "speaker": "Karen E. Willcox",
        "institution": "Institute for Mathematical and Statistical Innovation",
        "source_url": "https://cdn.imsi.institute/videos/73339/pHUmxZztZj/slides.pdf",
        "landing_page_url": "https://www.imsi.institute/videos/research-gaps-and-future-directions/",
        "local_cache_file": "imsi_research_gaps_future_directions.pdf",
        "actual_page_number": 48,
        "page_function": "DISCUSSION",
        "scientific_object": "digital twins as a scientific grand challenge",
        "evidence_type": "discussion synthesis",
        "rights_note": "public IMSI slide PDF; composition lessons only",
    },
]

FORBIDDEN_VISIBLE_TERMS = [
    "RRL-",
    "SRC-",
    "GSC-",
    "NeurIPS",
    "IMSI",
    "Willcox",
    "Gao",
    "Wisconsin",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def render_page(candidate: dict) -> Path:
    source_pdf = SOURCE_CACHE / candidate["local_cache_file"]
    if not source_pdf.exists():
        raise FileNotFoundError(f"missing source cache file: {source_pdf}")
    RENDER_CACHE.mkdir(parents=True, exist_ok=True)
    prefix = RENDER_CACHE / candidate["local_cache_file"].removesuffix(".pdf")
    page = str(candidate["actual_page_number"])
    rendered = RENDER_CACHE / f"{prefix.name}-{page}.png"
    if not rendered.exists():
        subprocess.run(
            ["pdftoppm", "-f", page, "-l", page, "-r", "140", "-png", str(source_pdf), str(prefix)],
            check=True,
        )
    return rendered


def anonymize(rendered: Path, output: Path) -> None:
    image = Image.open(rendered).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    # Hide common source branding/page-number zones from the model-visible review
    # while leaving the scientific composition itself inspectable.
    draw.rectangle((int(width * 0.90), 0, width, int(height * 0.16)), fill=(255, 255, 255))
    draw.rectangle((0, int(height * 0.90), int(width * 0.20), height), fill=(255, 255, 255))
    draw.rectangle((int(width * 0.88), int(height * 0.90), width, height), fill=(255, 255, 255))
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)


def admission_rubric() -> str:
    return (
        "You are reviewing anonymous public-safe rendered research-slide pages for 026 discussion/next-experiment "
        "production-gold admission. Inspect the actual pixels for every item. Do not infer quality from order, file "
        "names, metadata, SHA values, or presumed provenance.\n"
        "For each item, decide whether the visible composition reaches a mature doctoral research-group meeting or "
        "strong conference-talk bar for reuse as an abstract composition reference for DISCUSSION, NEXT_EXPERIMENT, "
        "OPEN_QUESTION, or LIMITATION_TO_NEXT_TEST pages. PASS means the page has a real scientific object, a clear "
        "relationship between present evidence or limitation and the next research action, mature hierarchy, "
        "projection-readable typography, disciplined whitespace, useful annotation/caption/legend/panel relations, "
        "and no generic future-work/card-dashboard/template feel. REVISE means it remains an ordinary inspected "
        "reference only. BLOCKED means pixels cannot be assessed.\n"
        "For every item, state the primary scientific object, the discussion/next-experiment page-job fit, visual "
        "maturity, projection readability, and the admission or rejection reason. Do not admit a page merely because "
        "it says future work, discussion, or open question; the visible composition must actually support scientific "
        "reasoning or next validation planning. Top-level PASS means the packet is assessable; item-level decisions "
        "carry admission semantics."
    )


def main() -> int:
    if len(CANDIDATES) > 12:
        raise RuntimeError("026 Terra page cap exceeded")
    input_dir = OUT_DIR / "inputs"
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    input_dir.mkdir(parents=True, exist_ok=True)

    inputs = []
    identity_items = []
    item_sha = {}
    for index, candidate in enumerate(CANDIDATES):
        anonymous_id = f"item_{chr(ord('A') + index)}"
        rendered = render_page(candidate)
        anonymous_path = input_dir / f"{anonymous_id}.png"
        anonymize(rendered, anonymous_path)
        digest = sha256(anonymous_path)
        item_sha[anonymous_id] = digest
        source_pdf = SOURCE_CACHE / candidate["local_cache_file"]
        rendered_digest = sha256(rendered)
        inputs.append({
            "logical_id": anonymous_id,
            "path": str(anonymous_path.relative_to(REPO_ROOT)),
            "mime_type": "image/png",
            "sha256": digest,
            "description": "Anonymous discussion/next-experiment research-slide render. Judge only visible pixels and page-job fit.",
        })
        identity_items.append({
            **candidate,
            "anonymous_id": anonymous_id,
            "source_file_sha256": sha256(source_pdf),
            "canonical_rendered_page_sha256": rendered_digest,
            "canonical_rendered_page_path": str(rendered.relative_to(REPO_ROOT)),
            "review_input_path": str(anonymous_path.relative_to(REPO_ROOT)),
            "review_input_sha256": digest,
            "materialization_method": "download/verify public PDF, render selected page with pdftoppm -r 140, and mask source branding/page-number zones before Terra input",
            "semantic_prescreen": "visible page content carries discussion, next-experiment, open-question, or limitation-to-next-test research reasoning",
        })

    visible_manifest = {
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": VISIBLE_TASK_KEY,
        "workflow_type": "generic",
        "review_kind": "research-gold-discussion-next-experiment-admission",
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "external_upload_authorization": "",
        "prompt_version": "ai-bridge.visual-review.v1",
        "identity_bindings": {
            "adapter_identity": "026_gold_admission_1",
            "page_job_contract": "discussion / next experiment production gold composition admission",
            "item_sha256_by_anonymous_id": item_sha,
        },
        "inputs": inputs,
        "rubric": {
            "instructions": admission_rubric(),
            "source_contracts": [],
        },
    }
    visible_text = json.dumps(visible_manifest, sort_keys=True)
    for forbidden in FORBIDDEN_VISIBLE_TERMS:
        if forbidden in visible_text:
            raise RuntimeError(f"Terra-visible manifest leaks forbidden term {forbidden}")
    manifest_sha = hashlib.sha256(visible_text.encode("utf-8")).hexdigest()
    visible_manifest["identity_bindings"]["immutable_review_identity_sha256"] = manifest_sha

    identity_map = {
        "schema": "RESEARCH_PRESENTATION_GOLD_DISCUSSION_ADMISSION_IDENTITY_MAP_V1",
        "task_key": TASK_KEY,
        "review_identity_sha256": manifest_sha,
        "source_url_count": len({item["source_url"] for item in CANDIDATES}),
        "deck_intake_count": len({item["local_cache_file"] for item in CANDIDATES}),
        "terra_page_count": len(CANDIDATES),
        "admission_packet_count": 1,
        "caps": {
            "max_source_urls": 8,
            "max_decks": 4,
            "max_terra_pages": 12,
            "max_admission_packets": 2,
        },
        "items": identity_items,
    }
    review_identity = {
        "schema": "RESEARCH_PRESENTATION_GOLD_DISCUSSION_ADMISSION_IDENTITY_V1",
        "task_key": TASK_KEY,
        "review_identity_sha256": manifest_sha,
        "visual_inputs_sha256": hashlib.sha256(
            json.dumps(visible_manifest, sort_keys=True).encode("utf-8")
        ).hexdigest(),
        "review_input_sha256_by_anonymous_id": item_sha,
        "rubric_sha256": hashlib.sha256(admission_rubric().encode("utf-8")).hexdigest(),
        "anonymous_item_count": len(inputs),
    }
    for path, payload in [
        (OUT_DIR / "visual_inputs.json", visible_manifest),
        (OUT_DIR / "review_identity_map.json", identity_map),
        (OUT_DIR / "review_identity.json", review_identity),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "manifest": str((OUT_DIR / "visual_inputs.json").relative_to(REPO_ROOT)),
        "identity_map": str((OUT_DIR / "review_identity_map.json").relative_to(REPO_ROOT)),
        "terra_page_count": len(CANDIDATES),
        "source_url_count": identity_map["source_url_count"],
        "deck_intake_count": identity_map["deck_intake_count"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
