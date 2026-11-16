"""Read geometry from a PDF snapshot using PyMuPDF."""

from contextlib import contextmanager
from dataclasses import dataclass
from math import isfinite

from ..io import EvidenceMissing, InputError


@dataclass(frozen=True)
class Rect:
    x0: float
    y0: float
    x1: float
    y1: float

    @classmethod
    def from_value(cls, value):
        values = tuple(value)
        if (len(values) != 4
                or not all(type(item) in (int, float) and isfinite(item) for item in values)
                or values[0] > values[2] or values[1] > values[3]):
            raise InputError("Invalid PDF rectangle")
        return cls(*values)

    @property
    def width(self):
        return self.x1 - self.x0

    @property
    def height(self):
        return self.y1 - self.y0

    @property
    def cy(self):
        return (self.y0 + self.y1) / 2

    @property
    def cx(self):
        return (self.x0 + self.x1) / 2

    def contains(self, other, tolerance=0):
        return (other.x0 >= self.x0 - tolerance and other.x1 <= self.x1 + tolerance
                and other.y0 >= self.y0 - tolerance and other.y1 <= self.y1 + tolerance)

    def intersects(self, other):
        return (min(self.x1, other.x1) > max(self.x0, other.x0)
                and min(self.y1, other.y1) > max(self.y0, other.y0))

    def distance_to_boundary(self, x, y):
        if self.x0 <= x <= self.x1 and self.y0 <= y <= self.y1:
            return min(x - self.x0, self.x1 - x, y - self.y0, self.y1 - y)
        return min(
            ((px - x) ** 2 + (py - y) ** 2) ** 0.5
            for px, py in ((self.x0, min(max(y, self.y0), self.y1)),
                           (self.x1, min(max(y, self.y0), self.y1)),
                           (min(max(x, self.x0), self.x1), self.y0),
                           (min(max(x, self.x0), self.x1), self.y1))
        )


def union(boxes):
    boxes = list(boxes)
    if not boxes:
        raise EvidenceMissing("No rendered primitives bind the semantic object")
    return Rect(min(b.x0 for b in boxes), min(b.y0 for b in boxes),
                max(b.x1 for b in boxes), max(b.y1 for b in boxes))


@dataclass(frozen=True)
class Text:
    box: Rect
    spans: tuple
    baseline: float


@dataclass(frozen=True)
class Drawing:
    box: Rect
    segments: tuple
    width: float | None
    color: tuple | None
    fill: tuple | None


@dataclass
class Render:
    bounds: Rect
    lines: list[Text]
    drawings: list[Drawing]
    images: list[Rect]
    links: list[Rect]

    @classmethod
    def extract(cls, page):
        if page.rotation:
            raise EvidenceMissing("Rotated PDF pages require a geometry adapter")
        lines = []
        # Infinite clipping exposes off-page text instead of silently dropping it.
        import pymupdf

        blocks = page.get_text("dict", flags=pymupdf.TEXTFLAGS_TEXT,
                               clip=pymupdf.INFINITE_RECT())["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                spans = tuple(span for span in line["spans"] if span["text"].strip())
                if spans:
                    lines.append(Text(union(Rect.from_value(span["bbox"]) for span in spans),
                                      spans, spans[0]["origin"][1]))
        drawings = [
            Drawing(Rect.from_value(path["rect"]),
                    tuple((tuple(item[1]), tuple(item[2])) for item in path["items"] if item[0] == "l"),
                    path["width"], path["color"], path["fill"])
            for path in page.get_drawings()
        ]
        return cls(Rect.from_value(page.rect), lines, drawings,
                   [Rect.from_value(item["bbox"]) for item in page.get_image_info()],
                   [Rect.from_value(item["from"]) for item in page.get_links()
                    if item.get("kind") == pymupdf.LINK_GOTO and item.get("page", -1) >= 0])


@contextmanager
def document(data):
    try:
        import pymupdf
    except ImportError as exc:
        raise EvidenceMissing("PyMuPDF is required for rendered geometry") from exc
    try:
        doc = pymupdf.open(stream=data, filetype="pdf")
    except (RuntimeError, ValueError) as exc:
        raise InputError("Could not open PDF snapshot") from exc
    with doc:
        if doc.needs_pass or doc.page_count < 1:
            raise EvidenceMissing("PDF is encrypted or has no pages")
        yield doc
