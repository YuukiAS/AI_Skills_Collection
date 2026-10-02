#!/usr/bin/env python3
"""Stage B v0.4 live Project recovery evidence helpers."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


REPO = "YuukiAS/AI_Skills_Collection"
PROJECT_OWNER = "YuukiAS"
PROJECT_NUMBER = 5
PROJECT_TITLE = "AI Skills Maintenance"
PROJECT_ID = "PVT_kwHOA0Lgf84BkjCU"
DUPLICATES = [52, 60, 61, 62, 66, 67, 68, 69, 70, 71, 72]
SENTINEL = 52
SENTINEL_LABEL = "kind:enhancement"
COMPLETED_REASON = "COMPLETED"


def run_gh_graphql(query: str, variables: Mapping[str, Any]) -> dict[str, Any]:
    args = ["gh", "api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        flag = "-F" if isinstance(value, int) else "-f"
        args.extend([flag, f"{key}={value}"])
    completed = subprocess.run(args, text=True, capture_output=True, check=True)
    return json.loads(completed.stdout)


def run_gh(args: Sequence[str]) -> str:
    completed = subprocess.run(["gh", *args], text=True, capture_output=True, check=True)
    return completed.stdout


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def project_workflows() -> dict[str, Any]:
    query = """
    query($owner:String!, $number:Int!) {
      user(login:$owner) {
        projectV2(number:$number) {
          id number title url
          workflows(first:20) {
            nodes { id name number enabled createdAt updatedAt }
          }
        }
      }
    }
    """
    return run_gh_graphql(query, {"owner": PROJECT_OWNER, "number": PROJECT_NUMBER})[
        "data"
    ]["user"]["projectV2"]


def all_maintenance_issues() -> list[dict[str, Any]]:
    owner, name = REPO.split("/", 1)
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
                ... on ProjectV2ItemFieldSingleSelectValue {
                  name optionId
                  field { ... on ProjectV2SingleSelectField { id name } }
                }
                ... on ProjectV2ItemFieldTextValue {
                  text
                  field { ... on ProjectV2FieldCommon { id name } }
                }
              } }
            } }
          }
        }
      }
    }
    """
    issues: list[dict[str, Any]] = []
    after = ""
    while True:
        payload = run_gh_graphql(query, {"owner": owner, "name": name, "after": after})
        conn = payload["data"]["repository"]["issues"]
        issues.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            return issues
        after = conn["pageInfo"]["endCursor"]


def project_item(issue: Mapping[str, Any]) -> dict[str, Any] | None:
    for item in issue.get("projectItems", {}).get("nodes", []):
        if item.get("project", {}).get("id") == PROJECT_ID:
            return item
    return None


def project_fields(item: Mapping[str, Any] | None) -> dict[str, dict[str, str]]:
    fields: dict[str, dict[str, str]] = {}
    if not item:
        return fields
    for value in item.get("fieldValues", {}).get("nodes", []):
        field = value.get("field") or {}
        name = field.get("name")
        if not name:
            continue
        entry: dict[str, str] = {"fieldId": field.get("id", "")}
        if "optionId" in value:
            entry.update({"kind": "single_select", "name": value.get("name", ""), "optionId": value.get("optionId", "")})
        elif "text" in value:
            entry.update({"kind": "text", "text": value.get("text", "")})
        fields[name] = entry
    return fields


def normalize_issue(issue: Mapping[str, Any]) -> dict[str, Any]:
    item = project_item(issue)
    return {
        "id": issue["id"],
        "number": issue["number"],
        "title": issue["title"],
        "url": issue["url"],
        "state": issue["state"],
        "stateReason": issue.get("stateReason"),
        "labels": sorted(node["name"] for node in issue.get("labels", {}).get("nodes", [])),
        "projectItemId": item.get("id") if item else None,
        "project": item.get("project") if item else None,
        "projectFields": project_fields(item),
    }


def snapshot() -> dict[str, Any]:
    issues = [normalize_issue(issue) for issue in all_maintenance_issues()]
    duplicate_issues = [issue for issue in issues if issue["number"] in DUPLICATES]
    completed_history = [
        issue
        for issue in issues
        if issue["state"] == "CLOSED"
        and issue.get("stateReason") == COMPLETED_REASON
        and issue.get("projectItemId")
    ]
    workflows = project_workflows()
    return {
        "schema": "ai-skills-maintenance-board-v7-stage-b-recovery-v0.4-live-readback/v1",
        "captured_at": now_iso(),
        "repo": REPO,
        "project_owner": PROJECT_OWNER,
        "project_number": PROJECT_NUMBER,
        "project_id": PROJECT_ID,
        "project_title": PROJECT_TITLE,
        "workflows": workflows,
        "issue_count": len(issues),
        "duplicate_issues": sorted(duplicate_issues, key=lambda issue: issue["number"]),
        "completed_history": sorted(completed_history, key=lambda issue: issue["number"]),
    }


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_duplicate_ready(issue: Mapping[str, Any]) -> None:
    number = issue["number"]
    labels = set(issue.get("labels", []))
    kind = [label for label in labels if label.startswith("kind:")]
    scope = [label for label in labels if label.startswith("scope:")]
    area = [label for label in labels if label.startswith("area:")]
    if issue.get("state") != "CLOSED" or issue.get("stateReason") != "DUPLICATE":
        raise RuntimeError(f"#{number} is not CLOSED / DUPLICATE")
    if "maintenance-track" not in labels:
        raise RuntimeError(f"#{number} is missing maintenance-track")
    if len(kind) != 1 or len(scope) != 1 or len(area) != 1:
        raise RuntimeError(f"#{number} does not have exact reviewed taxonomy labels")
    if not issue.get("projectItemId"):
        raise RuntimeError(f"#{number} is not currently in {PROJECT_TITLE}")
    status = issue.get("projectFields", {}).get("Status", {}).get("name")
    if status != "DONE":
        raise RuntimeError(f"#{number} Project Status is not DONE: {status!r}")


def restore_project_fields(new_item_id: str, old_issue: Mapping[str, Any]) -> list[dict[str, str]]:
    restored: list[dict[str, str]] = []
    for field_name, value in old_issue.get("projectFields", {}).items():
        if field_name == "Title":
            continue
        field_id = value.get("fieldId")
        if not field_id:
            continue
        if value.get("kind") == "single_select" and value.get("optionId"):
            run_gh(
                [
                    "project",
                    "item-edit",
                    "--id",
                    new_item_id,
                    "--project-id",
                    PROJECT_ID,
                    "--field-id",
                    field_id,
                    "--single-select-option-id",
                    value["optionId"],
                ]
            )
            restored.append({"field": field_name, "kind": "single_select", "value": value.get("name", "")})
        elif value.get("kind") == "text":
            run_gh(
                [
                    "project",
                    "item-edit",
                    "--id",
                    new_item_id,
                    "--project-id",
                    PROJECT_ID,
                    "--field-id",
                    field_id,
                    "--text",
                    value.get("text", ""),
                ]
            )
            restored.append({"field": field_name, "kind": "text", "value": value.get("text", "")})
    return restored


def rollback_removed(removed: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rollback: list[dict[str, Any]] = []
    for issue in removed:
        add_payload = json.loads(
            run_gh(
                [
                    "project",
                    "item-add",
                    str(PROJECT_NUMBER),
                    "--owner",
                    PROJECT_OWNER,
                    "--url",
                    issue["url"],
                    "--format",
                    "json",
                ]
            )
        )
        new_item_id = add_payload["id"]
        restored = restore_project_fields(new_item_id, issue)
        rollback.append(
            {
                "issue": issue["number"],
                "url": issue["url"],
                "oldProjectItemId": issue["projectItemId"],
                "newProjectItemId": new_item_id,
                "restoredFields": restored,
            }
        )
    return rollback


def remove_duplicates(pre_snapshot_path: Path, output_path: Path) -> int:
    pre_snapshot = json.loads(pre_snapshot_path.read_text(encoding="utf-8"))
    duplicates = pre_snapshot["duplicate_issues"]
    duplicate_numbers = sorted(issue["number"] for issue in duplicates)
    if duplicate_numbers != DUPLICATES:
        raise RuntimeError(f"unexpected duplicate cohort: {duplicate_numbers}")
    for issue in duplicates:
        require_duplicate_ready(issue)

    removed: list[dict[str, Any]] = []
    operations: list[dict[str, Any]] = []
    rollback: list[dict[str, Any]] = []
    error = None
    try:
        for issue in duplicates:
            run_gh(
                [
                    "project",
                    "item-delete",
                    str(PROJECT_NUMBER),
                    "--owner",
                    PROJECT_OWNER,
                    "--id",
                    issue["projectItemId"],
                    "--format",
                    "json",
                ]
            )
            removed.append(issue)
            operations.append(
                {
                    "issue": issue["number"],
                    "action": "project-item-delete",
                    "projectItemId": issue["projectItemId"],
                }
            )
    except Exception as exc:  # noqa: BLE001 - evidence script must rollback and report exact failure.
        error = repr(exc)
        rollback = rollback_removed(removed)

    post = snapshot()
    payload = {
        "schema": "ai-skills-maintenance-board-v7-stage-b-duplicate-repair-v0.4/v1",
        "captured_at": now_iso(),
        "repo": REPO,
        "project_owner": PROJECT_OWNER,
        "project_number": PROJECT_NUMBER,
        "cohort": DUPLICATES,
        "before": duplicates,
        "operations": operations,
        "rollback": rollback,
        "error": error,
        "after": post["duplicate_issues"],
    }
    write_json(output_path, payload)
    if error:
        raise RuntimeError(error)
    return 0


def issue_by_number(payload: Mapping[str, Any], number: int) -> dict[str, Any]:
    for issue in payload["duplicate_issues"]:
        if issue["number"] == number:
            return issue
    raise RuntimeError(f"issue #{number} was not found in duplicate cohort")


def duplicate_absence_ok(payload: Mapping[str, Any]) -> bool:
    for issue in payload["duplicate_issues"]:
        if issue["number"] not in DUPLICATES:
            continue
        if issue.get("state") != "CLOSED" or issue.get("stateReason") != "DUPLICATE":
            return False
        if "maintenance-track" not in issue.get("labels", []):
            return False
        if issue.get("projectItemId") is not None:
            return False
    return True


def sentinel_probe(output_path: Path, settling_seconds: int) -> int:
    before = snapshot()
    before_issue = issue_by_number(before, SENTINEL)
    before_labels = before_issue["labels"]
    if SENTINEL_LABEL not in before_labels:
        raise RuntimeError(f"#{SENTINEL} is missing {SENTINEL_LABEL}")
    if before_issue.get("projectItemId") is not None:
        raise RuntimeError(f"#{SENTINEL} is still in Project before sentinel probe")

    mid = None
    after_restore = None
    final = None
    error = None
    try:
        run_gh(["issue", "edit", str(SENTINEL), "--repo", REPO, "--remove-label", SENTINEL_LABEL])
        mid = snapshot()
        run_gh(["issue", "edit", str(SENTINEL), "--repo", REPO, "--add-label", SENTINEL_LABEL])
        after_restore = snapshot()
        time.sleep(settling_seconds)
        final = snapshot()
    except Exception as exc:  # noqa: BLE001 - evidence script must restore before surfacing.
        error = repr(exc)
        try:
            latest = snapshot()
            latest_issue = issue_by_number(latest, SENTINEL)
            if SENTINEL_LABEL not in latest_issue.get("labels", []):
                run_gh(["issue", "edit", str(SENTINEL), "--repo", REPO, "--add-label", SENTINEL_LABEL])
                after_restore = snapshot()
        except Exception as restore_exc:  # noqa: BLE001
            error = f"{error}; restore_error={restore_exc!r}"
        final = snapshot()

    final_issue = issue_by_number(final, SENTINEL) if final else None
    ok = (
        error is None
        and final_issue is not None
        and final_issue.get("labels") == before_labels
        and final_issue.get("state") == "CLOSED"
        and final_issue.get("stateReason") == "DUPLICATE"
        and "maintenance-track" in final_issue.get("labels", [])
        and final_issue.get("projectItemId") is None
        and duplicate_absence_ok(final)
    )
    payload = {
        "schema": "ai-skills-maintenance-board-v7-stage-b-sentinel-probe-v0.4/v1",
        "captured_at": now_iso(),
        "repo": REPO,
        "sentinel_issue": SENTINEL,
        "sentinel_label": SENTINEL_LABEL,
        "settling_seconds": settling_seconds,
        "ok": ok,
        "error": error,
        "before": before,
        "after_remove": mid,
        "after_restore": after_restore,
        "final": final,
    }
    write_json(output_path, payload)
    if not ok:
        raise RuntimeError("sentinel probe failed; see output evidence")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["snapshot", "remove-duplicates", "sentinel-probe"])
    parser.add_argument("--pre-snapshot")
    parser.add_argument("--output", required=True)
    parser.add_argument("--settling-seconds", type=int, default=60)
    args = parser.parse_args(argv)
    if args.command == "snapshot":
        write_json(Path(args.output), snapshot())
        return 0
    if args.command == "sentinel-probe":
        return sentinel_probe(Path(args.output), args.settling_seconds)
    if not args.pre_snapshot:
        parser.error("--pre-snapshot is required for remove-duplicates")
    return remove_duplicates(Path(args.pre_snapshot), Path(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
