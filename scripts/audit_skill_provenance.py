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
SOURCE_KEYS = ("source_repo_url", "source_path", "source_ref", "source_imported_at", "source_license", "source_note")
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
        if provenance == "user-authored":
            row["provenance_category"] = "user-authored"
        elif provenance == "external-adapted":
            row["provenance_category"] = "external-adapted"
        elif provenance == "external-vendored":
            row["provenance_category"] = "external-vendored"
        elif provenance == "generated":
            row["provenance_category"] = "generated"
        elif provenance == "local":
            row["provenance_category"] = "local"
        else:
            row["provenance_category"] = "unknown"
        rows.append(row)
    return sorted(rows, key=lambda item: item["path"])


def audit(include_archive: bool = False) -> dict[str, Any]:
    rows = skill_rows(include_archive=include_archive)
    provenance_counts = Counter(row["provenance"] for row in rows)
    category_counts = Counter(row["provenance_category"] for row in rows)
    author_counts = Counter(row["metadata_skill_author"] or "(missing)" for row in rows)
    license_counts = Counter(row["license"] or "(missing)" for row in rows)
    rows_with_urls = [row for row in rows if row["url_count"]]
    rows_with_license_files = [row for row in rows if row["license_files"]]
    return {
        "scope": "active_and_non_archived" if not include_archive else "all_non_hidden",
        "skill_count": len(rows),
        "provenance_counts": dict(sorted(provenance_counts.items())),
        "provenance_category_counts": dict(sorted(category_counts.items())),
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
    user_rows = [row for row in skills if row["provenance_category"] == "user-authored"]
    adapted_rows = [row for row in skills if row["provenance_category"] == "external-adapted"]
    vendored_rows = [row for row in skills if row["provenance_category"] == "external-vendored"]
    generated_rows = [row for row in skills if row["provenance_category"] == "generated"]
    local_rows = [row for row in skills if row["provenance_category"] == "local"]
    unknown_rows = [row for row in skills if row["provenance_category"] == "unknown"]
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
        f"- User-authored skills: {len(user_rows)}",
        f"- External adapted skills: {len(adapted_rows)}",
        f"- External vendored skills: {len(vendored_rows)}",
        f"- Generated skills: {len(generated_rows)}",
        f"- Local legacy skills: {len(local_rows)}",
        f"- Unknown-origin historical skills: {len(unknown_rows)}",
        f"- Skills containing URLs in the body: {data['rows_with_urls_count']}",
        f"- Skills containing local license files: {data['rows_with_license_files_count']}",
        "",
        "## Provenance Counts",
        "",
    ]
    lines.extend(markdown_table([["Provenance", "Count"]] + [[key, str(value)] for key, value in data["provenance_counts"].items()]))
    for title, rows in (
        ("User Authored", user_rows),
        ("External Adapted", adapted_rows),
        ("External Vendored", vendored_rows),
        ("Generated", generated_rows),
        ("Local Legacy", local_rows),
        ("Unknown Historical", unknown_rows),
    ):
        lines.extend(["", f"## {title}", ""])
        if rows:
            lines.extend(
                markdown_table(
                    [["Skill", "Path", "Provenance", "Source"]]
                    + [
                        [
                            row["name"],
                            row["path"],
                            row["provenance"],
                            json.dumps(row["source_fields"], ensure_ascii=False, sort_keys=True) if row["source_fields"] else "",
                        ]
                        for row in rows
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
            "provenance: external-adapted",
            "source_repo_url: https://github.com/<owner>/<repo>",
            "source_path: path/to/original/skill",
            "source_ref: <full commit sha or tag>",
            "source_imported_at: YYYY-MM-DD",
            "source_license: <license id or URL>",
            "source_note: <short note on local changes>",
            "metadata:",
            "  skill-author: <upstream author or organization>",
            "```",
            "",
            "Use `provenance: user-authored` for original local work. Historical `unknown` is allowed only when the exact source was not recorded; do not guess URLs, refs, or licenses.",
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
