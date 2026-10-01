#!/usr/bin/env python3
"""Read-only audit for AI Skills Maintenance Board Issue metadata."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence

KIND_PREFIX = "kind:"
SCOPE_PREFIX = "scope:"
AREA_PREFIX = "area:"
TRIAGE_LABELS = {"triage:needed", "triage:needs-info"}
MAINTENANCE_LABEL = "maintenance-track"
PROJECT_FIELDS = ("Status", "Area", "Resolution commit")

Issue = MutableMapping[str, Any]
Violation = Dict[str, Any]


def _run_gh_graphql(query: str, variables: Mapping[str, Any]) -> Dict[str, Any]:
    args = ["gh", "api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        flag = "-F" if isinstance(value, int) else "-f"
        args.extend([flag, f"{key}={value}"])
    completed = subprocess.run(args, text=True, capture_output=True, check=True)
    return json.loads(completed.stdout)


def collect_tracking_map(root: Path) -> Dict[int, List[Dict[str, str]]]:
    """Return canonical TODO entries that already contain tracking issue locators."""
    mapping: Dict[int, List[Dict[str, str]]] = {}
    for dirname in ("docs/plugin-todos", "docs/skill-todos"):
        base = root / dirname
        if not base.exists():
            continue
        for path in sorted(base.glob("*.md")):
            entry = None
            status = ""
            for raw_line in path.read_text(encoding="utf-8").splitlines():
                line = raw_line.strip()
                if raw_line.startswith("### "):
                    entry = raw_line[4:].strip()
                    status = ""
                    continue
                if entry and line.startswith("status:"):
                    status = line.split(":", 1)[1].strip()
                    continue
                if entry and line.startswith("tracking:"):
                    match = re.search(r"#(\d+)", line)
                    if match:
                        mapping.setdefault(int(match.group(1)), []).append(
                            {
                                "source": str(path.relative_to(root)),
                                "entry": entry,
                                "status": status,
                            }
                        )
    return mapping


def fetch_project(project_owner: str, project_number: int) -> Dict[str, Any]:
    query = """
    query($owner:String!, $number:Int!) {
      user(login:$owner) { projectV2(number:$number) { id title number url } }
    }
    """
    return _run_gh_graphql(query, {"owner": project_owner, "number": project_number})[
        "data"
    ]["user"]["projectV2"]


def fetch_maintenance_issues(repo: str, project_id: str) -> List[Issue]:
    owner, name = repo.split("/", 1)
    query = """
    query($owner:String!, $name:String!, $after:String) {
      repository(owner:$owner, name:$name) {
        issues(first:100, after:$after, labels:["maintenance-track"], states:[OPEN, CLOSED], orderBy:{field:CREATED_AT, direction:ASC}) {
          pageInfo { hasNextPage endCursor }
          nodes {
            id number title url state stateReason createdAt updatedAt closedAt
            labels(first:100) { nodes { name color description } }
            projectItems(first:20) { nodes {
              id
              project { id title number url }
              fieldValues(first:100) { nodes {
                ... on ProjectV2ItemFieldSingleSelectValue { name optionId field { ... on ProjectV2SingleSelectField { id name } } }
                ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { id name } } }
              } }
            } }
          }
        }
      }
    }
    """
    issues: List[Issue] = []
    after = ""
    while True:
        payload = _run_gh_graphql(
            query, {"owner": owner, "name": name, "after": after}
        )
        conn = payload["data"]["repository"]["issues"]
        for raw in conn["nodes"]:
            issues.append(normalize_graphql_issue(raw, project_id))
        if not conn["pageInfo"]["hasNextPage"]:
            break
        after = conn["pageInfo"]["endCursor"]
    return issues


def normalize_graphql_issue(raw: Mapping[str, Any], project_id: str) -> Issue:
    project_item = None
    for item in raw.get("projectItems", {}).get("nodes", []):
        if item.get("project", {}).get("id") == project_id:
            project_item = item
            break
    fields: Dict[str, str] = {}
    if project_item:
        for value in project_item.get("fieldValues", {}).get("nodes", []):
            field = value.get("field") or {}
            field_name = field.get("name")
            if not field_name:
                continue
            if "name" in value and "optionId" in value:
                fields[field_name] = value["name"]
            elif "text" in value:
                fields[field_name] = value["text"]
    return {
        "number": raw["number"],
        "title": raw["title"],
        "url": raw["url"],
        "state": raw["state"],
        "stateReason": raw.get("stateReason"),
        "labels": [node["name"] for node in raw.get("labels", {}).get("nodes", [])],
        "project": fields,
        "projectItemId": project_item.get("id") if project_item else None,
    }


def label_names(issue: Mapping[str, Any]) -> List[str]:
    labels = issue.get("labels", [])
    names: List[str] = []
    for label in labels:
        if isinstance(label, str):
            names.append(label)
        elif isinstance(label, Mapping):
            names.append(str(label.get("name", "")))
    return [name for name in names if name]


def _project_value(issue: Mapping[str, Any], key: str) -> str:
    project = issue.get("project") or {}
    value = project.get(key, "")
    if isinstance(value, Mapping):
        return str(value.get("name") or value.get("text") or "")
    return str(value or "")


def add_violation(violations: List[Violation], issue: Mapping[str, Any], code: str, message: str) -> None:
    violations.append(
        {
            "issue": issue.get("number"),
            "title": issue.get("title", ""),
            "code": code,
            "message": message,
        }
    )


def audit_issues(
    issues: Sequence[Issue], tracking_map: Mapping[int, Sequence[Mapping[str, str]]]
) -> Dict[str, Any]:
    violations: List[Violation] = []
    checked: List[Dict[str, Any]] = []

    for issue in issues:
        labels = label_names(issue)
        label_set = set(labels)
        number = int(issue["number"])
        kind_labels = sorted(name for name in labels if name.startswith(KIND_PREFIX))
        scope_labels = sorted(name for name in labels if name.startswith(SCOPE_PREFIX))
        area_labels = sorted(name for name in labels if name.startswith(AREA_PREFIX))
        project_status = _project_value(issue, "Status")
        project_area = _project_value(issue, "Area")
        resolution_commit = _project_value(issue, "Resolution commit")

        if MAINTENANCE_LABEL not in label_set:
            add_violation(violations, issue, "missing-maintenance-track", "Issue is in audit input without maintenance-track label.")
        if len(kind_labels) != 1:
            add_violation(violations, issue, "kind-count", f"Expected exactly one kind:* label, found {kind_labels}.")
        if len(scope_labels) != 1:
            add_violation(violations, issue, "scope-count", f"Expected exactly one scope:* label, found {scope_labels}.")
        if len(area_labels) != 1:
            add_violation(violations, issue, "area-count", f"Expected exactly one area:* label, found {area_labels}.")
        if TRIAGE_LABELS & label_set:
            add_violation(violations, issue, "triage-leak", "maintenance-track Issue still has pre-admission triage label.")
        status_labels = sorted(name for name in labels if name.startswith("status:"))
        if status_labels:
            add_violation(violations, issue, "lifecycle-label", f"Lifecycle status labels are forbidden: {status_labels}.")
        if len(area_labels) == 1 and project_area and area_labels[0] != f"area:{project_area}":
            add_violation(violations, issue, "area-mismatch", f"{area_labels[0]} does not match Project Area {project_area}.")

        scope = scope_labels[0] if len(scope_labels) == 1 else ""
        if scope in {"scope:plugin", "scope:standalone-skill"} and not tracking_map.get(number):
            add_violation(violations, issue, "missing-source-backlink", "TODO-backed plugin/standalone Issue has no canonical tracking:#N source backlink.")

        state = issue.get("state")
        state_reason = issue.get("stateReason") or ""
        if state == "OPEN" and project_status == "DONE":
            add_violation(violations, issue, "open-done", "Open Issue must not have Project Status DONE.")
        if state == "CLOSED":
            if state_reason == "COMPLETED":
                if project_status != "DONE":
                    add_violation(violations, issue, "completed-not-done", "Completed closed Issue must have Project Status DONE.")
                if not resolution_commit.strip():
                    add_violation(violations, issue, "completed-missing-resolution", "Completed closed Issue must have non-empty Resolution commit.")
            elif project_status == "DONE":
                add_violation(violations, issue, "not-planned-false-done", "Non-completion closed Issue must not be false-DONE.")

        checked.append(
            {
                "issue": number,
                "kind": kind_labels,
                "scope": scope_labels,
                "area": area_labels,
                "project_status": project_status,
                "project_area": project_area,
                "state": state,
                "state_reason": state_reason,
                "tracking_sources": list(tracking_map.get(number, [])),
            }
        )

    return {
        "ok": not violations,
        "issue_count": len(issues),
        "violation_count": len(violations),
        "violations": violations,
        "checked": checked,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="owner/name repository")
    parser.add_argument("--project-owner", required=True)
    parser.add_argument("--project-number", required=True, type=int)
    parser.add_argument("--json-output", required=True)
    args = parser.parse_args(argv)

    root = Path.cwd()
    project = fetch_project(args.project_owner, args.project_number)
    tracking_map = collect_tracking_map(root)
    issues = fetch_maintenance_issues(args.repo, project["id"])
    result = audit_issues(issues, tracking_map)
    result.update(
        {
            "repo": args.repo,
            "project_owner": args.project_owner,
            "project_number": args.project_number,
            "project": project,
        }
    )
    output = Path(args.json_output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if result["ok"]:
        print(f"metadata audit passed for {result['issue_count']} maintenance-track Issues")
        return 0
    print(f"metadata audit failed with {result['violation_count']} violation(s); wrote {output}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
