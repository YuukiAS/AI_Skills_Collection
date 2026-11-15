"""Checks that need input source rather than PDF geometry."""

from pathlib import Path
import re

from ..io import DIGEST, EvidenceMissing, InputError, child_path, read, records, sha256, tagged
from .model import check, route


OVERRIDES = {
    "tiny": r"\\tiny\b",
    "page_local_font_shrink": r"\\(?:scriptsize|footnotesize|small)\b|\bshrink\s*(?:=|[,\]])",
    "arbitrary_fontsize": r"\\(?:fontsize|mag)\b",
    "resizebox_text": r"\\resizebox\*?\s*\{",
    "scalebox_text": r"\\scalebox\s*\{",
    "reduced_body_baselineskip": r"\\(?:setlength\s*\{\\baselineskip\}|baselineskip\s*=|linespread\b|setstretch\b)",
    "negative_vspace_for_fit": r"\\(?:vspace\*?\s*\{\s*|vskip\s*)-\s*(?:\d|\.)",
    "itemsep_zero_for_teaching_list": r"(?:itemsep\s*=|\\setlength\s*\{\\itemsep\}\s*\{)\s*0(?:\.0+)?\s*(?:pt|mm|cm|ex|em|bp)\b",
}
INCLUDE = re.compile(r"\\(?:input|include|subfile)\s*\{([^{}]+)\}")


def scan(source_manifest, root, contract, pinned_core):
    if root is None:
        raise EvidenceMissing("No source root was supplied")
    sources = records(source_manifest["sources"])
    if not sources:
        raise EvidenceMissing("No candidate source inputs")
    expected = source_manifest["entry_source"]
    if expected not in sources or sources[expected]["role"] != "authored":
        raise InputError("No authored source entry is bound")
    paths = set()
    relative_paths = {row["path"] for row in sources.values()}
    if len(relative_paths) != len(sources):
        raise InputError("Duplicate paths in source manifest")
    results = []
    for name, entry in sources.items():
        path = child_path(Path(root), entry["path"])
        data = read(path)
        if tagged(entry["sha256"], DIGEST, "source sha256") != sha256(data):
            results.append(check("SOURCE", False, name, "Source SHA-256 differs from manifest"))
            continue
        if entry["role"] == "pinned_core":
            if pinned_core.get(entry["path"]) != sha256(data):
                raise InputError("Core source has no authorized digest")
            continue
        if entry["role"] != "authored" or path.suffix.lower() != ".tex":
            raise InputError("Unsupported manifested authored source")
        paths.add(name)
        text = re.sub(r"(?<!\\)%[^\n]*", "", data.decode("utf-8"))
        matches = [item for item in contract["forbidden_local_fallbacks"]
                   if re.search(OVERRIDES[item], text)]
        results.append(check("TYPE_SOURCE", not matches, name,
                             "TeX source has no recognized local compression syntax",
                             fallback_classes=matches))
        for included in INCLUDE.findall(text):
            possible = {included, f"{included}.tex"}
            if not relative_paths.intersection(possible):
                results.append(route("SOURCE", "NOT_VERIFIED", name,
                                     "Included source is absent from the manifest", path=included))
    if expected not in paths:
        results.append(check("SOURCE", False, expected, "Source entry is unavailable or differs"))
    return results
