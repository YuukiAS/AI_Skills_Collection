"""Narrow historical rendered-page validator pilot core.

This package is intentionally small. It provides reusable candidate machinery for
rendered presentation-page validation without encoding any course, artifact,
page-id, or historical verdict knowledge.
"""

from .aggregation import aggregate_page_result
from .anti_fitting import scan_paths_for_answer_fitting
from .detectors import DETECTOR_REGISTRY, run_detectors
from .features import extract_pdf_text_pages, inspect_rendered_png
from .review import blocked_rendered_review_row, build_review_packet, normalize_reviewer_row, review_rendered_page

__all__ = [
    "DETECTOR_REGISTRY",
    "aggregate_page_result",
    "build_review_packet",
    "blocked_rendered_review_row",
    "extract_pdf_text_pages",
    "inspect_rendered_png",
    "normalize_reviewer_row",
    "review_rendered_page",
    "run_detectors",
    "scan_paths_for_answer_fitting",
]
