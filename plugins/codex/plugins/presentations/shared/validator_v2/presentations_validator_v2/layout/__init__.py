"""Layout validation over explicit semantic assignments to rendered PDF primitives."""

from collections import Counter
from contextlib import ExitStack

from ..io import DIGEST, EvidenceMissing, InputError, canonical, records, sha256, tagged
from ..render import Render, document
from . import checks, protection, source
from .model import Page, check, route


DETECTORS = {
    "TYPE": checks.typography,
    "RAIL": checks.rail,
    "SPACE": checks.spacing,
    "COLUMN": checks.columns,
    "CAPTION": checks.captions,
    "QA": checks.qa,
    "FOOTER": checks.footer,
    "TABLE": checks.tables,
    "DIAGRAM": checks.diagram,
    "CLOSING": checks.closing,
    "DENSITY_WHITESPACE": checks.density,
    "SECTION_NAV": checks.section_nav,
    "TYPE_SOURCE": source.scan,
    "PROTECTION": protection.compare,
}


def guarded(code, target, detector, *args):
    try:
        result = detector(*args)
    except EvidenceMissing as exc:
        return [route(code, "NOT_VERIFIED", target, str(exc))]
    except (ValueError, KeyError, TypeError, AttributeError, IndexError) as exc:
        return [route(code, "FAIL", target, f"Invalid evidence: {exc}")]
    return result if isinstance(result, list) else [result]


def validate(contract, pdf, source_manifest, semantic_map, source_root=None, old_pdf=None):
    if contract["schema"] != "presentations-shared-beamer-core-v1":
        raise InputError("Unknown layout contract schema")
    digest = sha256(pdf)
    for bundle in (source_manifest, semantic_map):
        if digest != tagged(bundle["pdf_sha256"], DIGEST, "pdf_sha256"):
            raise InputError("Layout evidence does not match candidate PDF SHA-256")
    if sha256(canonical(source_manifest)) != semantic_map["source_manifest_sha256"]:
        raise InputError("Object map does not bind the source manifest")
    page_specs = records(semantic_map["pages"])
    rows = guarded("TYPE_SOURCE", "source", source.scan, source_manifest, source_root,
                   contract, semantic_map.get("pinned_core_sha256", {}))
    with ExitStack() as stack:
        doc = stack.enter_context(document(pdf))
        numbers = [page["index"] for page in page_specs.values()]
        if any(type(n) is not int for n in numbers) or sorted(numbers) != list(range(len(doc))):
            raise InputError("Object map must bind every PDF page once")
        section_counts = Counter(spec["section"] for spec in page_specs.values())
        old = None
        policy = semantic_map.get("protection")
        if policy is not None and old_pdf is not None:
            expected = tagged(policy["baseline_pdf_sha256"], DIGEST, "baseline PDF SHA-256")
            if sha256(old_pdf) != expected:
                raise InputError("Protected baseline PDF differs from contract")
            old = stack.enter_context(document(old_pdf))
        elif policy is None and old_pdf is not None:
            raise InputError("Baseline PDF supplied without protection authority")
        elif policy is not None:
            rows.append(route("PROTECTION", "NOT_VERIFIED", "artifact", "Protected baseline unavailable"))
        protected = records(policy["pages"]) if policy else {}
        if protected.keys() - page_specs.keys() or (policy is not None and not protected):
            raise InputError("Invalid protected page coverage")
        old_indexes = [entry["baseline_index"] for entry in protected.values()]
        if old is not None and (any(type(i) is not int or i < 0 or i >= len(old)
                                    for i in old_indexes)
                                or len(set(old_indexes)) != len(old_indexes)):
            raise InputError("Protected page map has invalid or duplicate baseline indexes")
        for page_id, spec in page_specs.items():
            native_page = doc[spec["index"]]
            try:
                render = Render.extract(native_page)
                page = Page(spec, render)
            except EvidenceMissing as exc:
                rows.append(route("OBJECT_MAP", "NOT_VERIFIED", page_id, str(exc)))
                continue
            missing = page.unbound_lines or page.unbound_images or page.unbound_drawings
            rows.append(route("OBJECT_MAP", "NOT_VERIFIED" if missing else "PASS", page_id,
                              "Coverage of extracted text, images and paths", text=page.unbound_lines,
                              images=page.unbound_images, drawings=page.unbound_drawings))
            for key, detector in DETECTORS.items():
                if key in {"TYPE_SOURCE", "PROTECTION"}:
                    continue
                args = (page, contract, section_counts) if key == "SECTION_NAV" else (page, contract)
                rows.extend(guarded(key, page_id, detector, *args))
            if old is not None and page_id in protected:
                spec = protected[page_id]
                rows.extend(guarded("PROTECTION", page_id, protection.compare,
                                    spec["masks"], page, old[spec["baseline_index"]], native_page))
    return rows, {
        "pdf_sha256": digest, "contract_sha256": sha256(canonical(contract)),
        "object_map_sha256": sha256(canonical(semantic_map)),
        "source_manifest_sha256": sha256(canonical(source_manifest)),
        "baseline_pdf_sha256": sha256(old_pdf) if old_pdf is not None else None,
    }
