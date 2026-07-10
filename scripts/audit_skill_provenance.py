#!/usr/bin/env python3
"""Audit locally recorded skill provenance without guessing upstream sources."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from skill_utils import ROOT, iter_skill_files, read_frontmatter


DOC_PATH = ROOT / "docs" / "SKILL_PROVENANCE.md"
JSON_PATH = ROOT / "docs" / "skill_provenance_audit.json"
URL_RE = re.compile(r"https?://[^\s)>\]\"'`,]+")
SOURCE_KEYS = ("source_url", "source_repo", "source_commit", "origin_url", "upstream_url", "upstream_repo")
LICENSE_FILES = ("LICENSE", "LICENSE.txt", "license.txt", "COPYING", "NOTICE")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def skill_rows(include_archive: bool = False) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for skill_file in iter_skill_files(include_archive=include_archive):
        meta, body = read_frontmatter(skill_file)
        metadata = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
        urls = sorted({url.rstrip(".,;:") for url in URL_RE.findall(body)})
        source_fields = {key: meta[key] for key in SOURCE_KEYS if meta.get(key)}
        source_fields.update({key: metadata[key] for key in SOURCE_KEYS if metadata.get(key)})
        license_files = [name for name in LICENSE_FILES if (skill_file.parent / name).exists()]
        provenance = str(meta.get("provenance") or "unknown")
        status = str(meta.get("status") or ("archived" if "archive" in skill_file.parts else "active"))
        author = str(metadata.get("skill-author") or "")
        row = {
            "name": str(meta.get("name") or skill_file.parent.name),
            "path": rel(skill_file.parent),
            "status": status,
            "provenance": provenance,
            "metadata_skill_author": author,
            "license": str(meta.get("license") or ""),
            "license_files": license_files,
            "source_fields": source_fields,
            "url_count": len(urls),
            "urls": urls,
        }
        if source_fields:
            row["provenance_confidence"] = "recorded_source_field"
        elif provenance in {"user-authored", "local"}:
            row["provenance_confidence"] = "recorded_local"
        elif author:
            row["provenance_confidence"] = "recorded_author_only"
        else:
            row["provenance_confidence"] = "unknown"
        rows.append(row)
    return sorted(rows, key=lambda item: item["path"])


def audit(include_archive: bool = False) -> dict[str, Any]:
    rows = skill_rows(include_archive=include_archive)
    provenance_counts = Counter(row["provenance"] for row in rows)
    confidence_counts = Counter(row["provenance_confidence"] for row in rows)
    author_counts = Counter(row["metadata_skill_author"] or "(missing)" for row in rows)
    license_counts = Counter(row["license"] or "(missing)" for row in rows)
    rows_with_urls = [row for row in rows if row["url_count"]]
    rows_with_license_files = [row for row in rows if row["license_files"]]
    return {
        "scope": "active_and_non_archived" if not include_archive else "all_non_hidden",
        "skill_count": len(rows),
        "provenance_counts": dict(sorted(provenance_counts.items())),
        "provenance_confidence_counts": dict(sorted(confidence_counts.items())),
        "metadata_skill_author_counts": dict(sorted(author_counts.items())),
        "license_counts": dict(sorted(license_counts.items())),
        "rows_with_urls_count": len(rows_with_urls),
        "rows_with_license_files_count": len(rows_with_license_files),
        "source_field_count": sum(1 for row in rows if row["source_fields"]),
        "skills": rows,
    }


def markdown_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    for row in rows[1:]:
        escaped = [cell.replace("|", "\\|").replace("\n", " ") for cell in row]
        lines.append("| " + " | ".join(escaped) + " |")
    return lines


def render_markdown(data: dict[str, Any]) -> str:
    skills = data["skills"]
    source_field_rows = [row for row in skills if row["source_fields"]]
    local_rows = [row for row in skills if row["provenance_confidence"] == "recorded_local"]
    author_rows = [row for row in skills if row["provenance_confidence"] == "recorded_author_only"]
    unknown_rows = [row for row in skills if row["provenance_confidence"] == "unknown"]
    url_rows = [row for row in skills if row["url_count"]]

    lines = [
        "# Skill Provenance Audit",
        "",
        "This report records what can be proven from files currently in this repository. It does not infer an upstream skill origin from package documentation links, license URLs, or library names.",
        "",
        "## Summary",
        "",
        f"- Scope: `{data['scope']}`",
        f"- Skills audited: {data['skill_count']}",
        f"- Skills with explicit source fields: {data['source_field_count']}",
        f"- Skills marked `user-authored` or `local`: {len(local_rows)}",
        f"- Skills with only `metadata.skill-author`: {len(author_rows)}",
        f"- Skills with unknown origin and no author field: {len(unknown_rows)}",
        f"- Skills containing URLs in the body: {data['rows_with_urls_count']}",
        f"- Skills containing local license files: {data['rows_with_license_files_count']}",
        "",
        "## Provenance Counts",
        "",
    ]
    lines.extend(markdown_table([["Provenance", "Count"]] + [[key, str(value)] for key, value in data["provenance_counts"].items()]))
    lines.extend(["", "## Recorded Authors", ""])
    lines.extend(
        markdown_table(
            [["metadata.skill-author", "Count"]]
            + [[key, str(value)] for key, value in data["metadata_skill_author_counts"].items()]
        )
    )
    lines.extend(["", "## Explicit Source Fields", ""])
    if source_field_rows:
        lines.extend(
            markdown_table(
                [["Skill", "Path", "Source fields"]]
                + [
                    [row["name"], row["path"], json.dumps(row["source_fields"], ensure_ascii=False, sort_keys=True)]
                    for row in source_field_rows
                ]
            )
        )
    else:
        lines.append("No active skill currently records `source_url`, `source_repo`, `source_commit`, `origin_url`, `upstream_url`, or `upstream_repo`.")

    lines.extend(["", "## Local Or User-Authored Records", ""])
    lines.extend(
        markdown_table(
            [["Skill", "Path", "Provenance", "Author"]]
            + [[row["name"], row["path"], row["provenance"], row["metadata_skill_author"] or ""] for row in local_rows]
        )
    )

    lines.extend(["", "## Author-Only External Evidence", ""])
    if author_rows:
        lines.append("These rows identify an author or organization, but not the exact upstream repository or commit.")
        lines.append("")
        lines.extend(
            markdown_table(
                [["Skill", "Path", "Author", "License"]]
                + [
                    [row["name"], row["path"], row["metadata_skill_author"], row["license"] or ""]
                    for row in author_rows
                ]
            )
        )
    else:
        lines.append("None.")

    lines.extend(["", "## URL Evidence", ""])
    if url_rows:
        lines.append("URLs below are evidence of related projects or references found in skill bodies. They are not treated as confirmed skill origins unless also recorded in an explicit source field.")
        lines.append("")
        lines.extend(
            markdown_table(
                [["Skill", "Path", "URL count", "First URLs"]]
                + [
                    [row["name"], row["path"], str(row["url_count"]), ", ".join(row["urls"][:3])]
                    for row in url_rows
                ]
            )
        )
    else:
        lines.append("No URLs found.")

    lines.extend(["", "## Unknown-Origin Inventory", ""])
    lines.extend(
        markdown_table(
            [["Skill", "Path", "License", "License files"]]
            + [
                [row["name"], row["path"], row["license"] or "", ", ".join(row["license_files"])]
                for row in unknown_rows
            ]
        )
    )

    lines.extend(
        [
            "",
            "## Going Forward",
            "",
            "For every newly cloned or adapted skill, add provenance metadata before committing it:",
            "",
            "```yaml",
            "provenance: external",
            "source_url: https://github.com/<owner>/<repo>",
            "source_commit: <full commit sha or tag>",
            "source_license: <license id or URL>",
            "adaptation_notes: <short note on local changes>",
            "metadata:",
            "  skill-author: <upstream author or organization>",
            "```",
            "",
            "Use `provenance: user-authored` for original local work and `provenance: local` for local synthesis where no upstream skill was copied. If the source is not known, leave `provenance: unknown` and add the skill to the unknown-origin inventory instead of guessing.",
            "",
            f"Machine-readable audit: `{JSON_PATH.relative_to(ROOT).as_posix()}`",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--include-archive", action="store_true", help="include archived skills")
    parser.add_argument("--write", action="store_true", help="write docs/SKILL_PROVENANCE.md and JSON audit")
    parser.add_argument("--json", action="store_true", help="print machine-readable audit JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    data = audit(include_archive=args.include_archive)
    if args.write:
        DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
        JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        DOC_PATH.write_text(render_markdown(data), encoding="utf-8")
        print(f"wrote {DOC_PATH.relative_to(ROOT)}")
        print(f"wrote {JSON_PATH.relative_to(ROOT)}")
    if args.json or not args.write:
        print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
