#!/usr/bin/env python3
"""Deterministic Slurm routing helpers for the installed slurm-workflows skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    tomllib = None
from datetime import datetime, time, timedelta, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Any


UNKNOWN = "UNKNOWN"
LIVE_KNOWN = "LIVE_KNOWN"
LOCAL_EXPLICIT = "LOCAL_EXPLICIT"
PROFILE_POLICY = "PROFILE_POLICY"


SINFO_FIELDS = "%P|%a|%l|%D|%c|%m|%G|%f|%T|%Q"
SINFO_COLUMNS = (
    "partition",
    "availability",
    "time_limit",
    "nodes",
    "cpus",
    "memory_mb",
    "gres",
    "features",
    "state",
    "priority_tier",
)
SCONTROL_CONFIG_FIELDS = {
    "ClusterName",
    "SelectType",
    "SelectTypeParameters",
    "SchedulerType",
    "SchedulerParameters",
    "PriorityType",
    "PriorityFlags",
    "PrivateData",
    "AccountingStorageType",
}
DEFAULT_STATE_PATH = Path.home() / ".config" / "ai-skills" / "slurm-workflows.toml"
STATE_JSON_TABLES = ("accepted_workload_contracts", "capacity_families", "enrollments")


def _run(argv: list[str], timeout: float = 5.0) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(argv, text=True, capture_output=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 127, "", str(exc)
    return proc.returncode, proc.stdout, proc.stderr


def _safe_id(value: str | None) -> str | None:
    if not value:
        return None
    raw = re.sub(r"[^a-zA-Z0-9_-]+", "-", value.strip().lower()).strip("-")
    if not raw:
        return None
    if len(raw) > 48:
        digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
        raw = f"local-slurm-{digest}"
    return raw


def parse_sinfo(text: str) -> list[dict[str, Any]]:
    partitions: list[dict[str, Any]] = []
    for raw in text.splitlines():
        if not raw.strip():
            continue
        parts = raw.rstrip("\n").split("|")
        parts += [""] * (len(SINFO_COLUMNS) - len(parts))
        row = dict(zip(SINFO_COLUMNS, parts[: len(SINFO_COLUMNS)]))
        name = row["partition"].strip()
        default = name.endswith("*")
        name = name.rstrip("*")
        if not name:
            continue
        row["partition"] = name
        row["default"] = default
        row["provenance"] = LIVE_KNOWN
        partitions.append(row)
    return partitions


def parse_scontrol_kv(text: str, allowed: set[str] | None = None) -> dict[str, str]:
    data: dict[str, str] = {}
    for key, value in re.findall(r"([A-Za-z][A-Za-z0-9_]+)=([^ \n]+)", text):
        if allowed is None or key in allowed:
            data[key] = value
    return data


def _empty_workflow_state() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "accepted_workload_contracts": {},
        "capacity_families": {},
        "enrollments": {},
        "evidence_locators": {},
    }


def load_workflow_state(path: Path | str | None = None) -> dict[str, Any]:
    """Load durable local Slurm workflow state without keeping scheduler history."""

    state_path = Path(path).expanduser() if path else DEFAULT_STATE_PATH
    state = _empty_workflow_state()
    if not state_path.exists():
        return state
    if tomllib is None:
        raise RuntimeError("TOML state loading requires Python 3.11+ tomllib")
    parsed = tomllib.loads(state_path.read_text(encoding="utf-8"))
    state["schema_version"] = int(parsed.get("schema_version", 1) or 1)
    for table in STATE_JSON_TABLES:
        values: dict[str, Any] = {}
        for key, raw in dict(parsed.get(table) or {}).items():
            if isinstance(raw, str) and raw.strip():
                values[str(key)] = json.loads(raw)
            elif isinstance(raw, dict):
                values[str(key)] = raw
        state[table] = values
    state["evidence_locators"] = {str(key): str(value) for key, value in dict(parsed.get("evidence_locators") or {}).items()}
    return state


def _toml_quote(value: str) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def save_workflow_state(state: dict[str, Any], path: Path | str | None = None) -> Path:
    """Persist declarative workload/capacity state to the local config file."""

    state_path = Path(path).expanduser() if path else DEFAULT_STATE_PATH
    state_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["schema_version = 1", ""]
    for table in STATE_JSON_TABLES:
        lines.append(f"[{table}]")
        for key in sorted(dict(state.get(table) or {})):
            payload = json.dumps(state[table][key], sort_keys=True, separators=(",", ":"))
            lines.append(f"{_toml_quote(key)} = {_toml_quote(payload)}")
        lines.append("")
    lines.append("[evidence_locators]")
    for key, value in sorted(dict(state.get("evidence_locators") or {}).items()):
        lines.append(f"{_toml_quote(key)} = {_toml_quote(str(value))}")
    state_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return state_path


def persist_accepted_workload_contract(
    state: dict[str, Any],
    intent: dict[str, Any],
    resources: dict[str, Any],
    evidence_locator: str | None = None,
) -> dict[str, Any]:
    family = comparable_family_id(intent)
    if not family:
        raise ValueError("accepted workload contract requires a comparable family id")
    state.setdefault("accepted_workload_contracts", {})[family] = {
        "resources": dict(resources),
        "accepted_at": datetime.now(timezone.utc).isoformat(),
    }
    if evidence_locator:
        state.setdefault("evidence_locators", {})[family] = evidence_locator
    return state


def persist_capacity_family(state: dict[str, Any], family: dict[str, Any], evidence_locator: str | None = None) -> dict[str, Any]:
    family_id = family.get("capacity_family_id")
    if not family_id:
        raise ValueError("capacity family requires capacity_family_id")
    state.setdefault("capacity_families", {})[str(family_id)] = dict(family)
    enrollment = family.get("enrollment")
    if isinstance(enrollment, dict):
        state.setdefault("enrollments", {})[str(family_id)] = dict(enrollment)
    if evidence_locator:
        state.setdefault("evidence_locators", {})[str(family_id)] = evidence_locator
    return state


def discover_live_site_context(local_site_id: str | None = None, policy_overlay_id: str | None = None) -> dict[str, Any]:
    """Discover a bounded, public-safe SiteContext from Slurm user commands."""

    commands = {name: shutil.which(name) for name in ("sinfo", "scontrol", "sacctmgr")}
    discovery = {
        "sinfo": {"argv": ["sinfo", "-h", "-o", SINFO_FIELDS], "status": "missing", "stderr": ""},
        "scontrol_config": {"argv": ["scontrol", "show", "config"], "status": "missing", "stderr": ""},
        "scontrol_partition": {"argv": ["scontrol", "show", "partition"], "status": "missing", "stderr": ""},
        "sacctmgr_assoc": {
            "argv": ["sacctmgr", "-n", "-P", "show", "assoc", f"user={os.environ.get('USER', '')}", "format=Cluster,Account,Partition,QOS,DefaultQOS"],
            "status": "missing",
            "stderr": "",
        },
    }
    partitions: list[dict[str, Any]] = []
    config: dict[str, str] = {}
    partition_detail_status = UNKNOWN
    assoc_status = UNKNOWN

    if commands["sinfo"]:
        rc, out, err = _run(["sinfo", "-h", "-o", SINFO_FIELDS])
        discovery["sinfo"].update({"status": "ok" if rc == 0 else "failed", "stderr": err.strip()})
        if rc == 0:
            partitions = parse_sinfo(out)

    if commands["scontrol"]:
        rc, out, err = _run(["scontrol", "show", "config"])
        discovery["scontrol_config"].update({"status": "ok" if rc == 0 else "failed", "stderr": err.strip()})
        if rc == 0:
            config = parse_scontrol_kv(out, SCONTROL_CONFIG_FIELDS)
        rc, _out, err = _run(["scontrol", "show", "partition"])
        partition_detail_status = LIVE_KNOWN if rc == 0 else UNKNOWN
        discovery["scontrol_partition"].update({"status": "ok" if rc == 0 else "failed", "stderr": err.strip()})

    if commands["sacctmgr"]:
        rc, _out, err = _run(discovery["sacctmgr_assoc"]["argv"])
        assoc_status = LIVE_KNOWN if rc == 0 else UNKNOWN
        discovery["sacctmgr_assoc"].update({"status": "ok" if rc == 0 else "failed", "stderr": err.strip()})

    cluster_name = config.get("ClusterName")
    resolved_site_id = local_site_id or _safe_id(cluster_name)
    return {
        "schema_version": 1,
        "kind": "slurm-workflows-site-context",
        "local_site_id": resolved_site_id,
        "policy_overlay_id": policy_overlay_id,
        "runtime_available": bool(partitions),
        "fact_provenance": {
            "partitions": LIVE_KNOWN if partitions else UNKNOWN,
            "partition_detail": partition_detail_status,
            "associations": assoc_status,
            "cluster_name": LIVE_KNOWN if cluster_name else UNKNOWN,
        },
        "partitions": partitions,
        "scheduler": {
            key: config.get(key, UNKNOWN)
            for key in sorted(SCONTROL_CONFIG_FIELDS)
            if key != "ClusterName"
        },
        "discovery": discovery,
    }


def merge_site_context(
    live: dict[str, Any] | None,
    policy_overlay: dict[str, Any] | None = None,
    local: dict[str, Any] | None = None,
) -> dict[str, Any]:
    live = live or {}
    policy_overlay = policy_overlay or {}
    local = local or {}
    overlay_id = policy_overlay.get("id") or policy_overlay.get("site_id")
    local_site_id = local.get("local_site_id") or live.get("local_site_id") or _safe_id(local.get("site_id"))
    context = {
        "local_site_id": local_site_id,
        "policy_overlay_id": overlay_id,
        "runtime_available": bool(live.get("runtime_available")),
        "fact_provenance": dict(live.get("fact_provenance") or {}),
        "partitions": list(live.get("partitions") or []),
        "constraints": dict(policy_overlay.get("constraints") or {}),
        "policy": dict(policy_overlay.get("policy") or {}),
        "preferences": dict(local.get("preferences") or {}),
        "local_facts": {key: value for key, value in local.items() if key not in {"preferences"}},
    }
    if not context["partitions"] and policy_overlay.get("partitions"):
        context["partitions"] = [
            {**item, "provenance": PROFILE_POLICY}
            for item in policy_overlay.get("partitions", [])
            if isinstance(item, dict)
        ]
    return context


def classify_workload_mode(intent: dict[str, Any]) -> str:
    requested = str(intent.get("mode") or "").strip().lower()
    if requested in {"batch", "persistent", "debug"}:
        return requested
    if intent.get("persistent") or intent.get("reuse_capacity") or intent.get("recurrence"):
        return "persistent"
    if intent.get("debug") or intent.get("interactive") or intent.get("shell"):
        return "debug"
    return "batch"


def comparable_family_id(intent: dict[str, Any]) -> str | None:
    explicit = intent.get("family_id")
    if explicit:
        return str(explicit)
    required = [
        intent.get("project"),
        intent.get("entrypoint"),
        intent.get("workload_class"),
        intent.get("scale_signature"),
        intent.get("accelerator_requirement", "cpu"),
    ]
    if any(not value for value in required[:4]):
        return None
    return "|".join(str(value) for value in required)


def resolve_resource_contract(
    intent: dict[str, Any],
    project_contracts: dict[str, Any] | None,
    user_contracts: dict[str, Any] | None,
    estimate: dict[str, Any] | None,
) -> dict[str, Any]:
    family = comparable_family_id(intent)
    if intent.get("resources"):
        source = "explicit"
        contract = dict(intent["resources"])
    elif family and project_contracts and family in project_contracts:
        source = "project_contract"
        contract = dict(project_contracts[family])
    elif family and user_contracts and family in user_contracts:
        source = "user_local_contract"
        stored = user_contracts[family]
        contract = dict(stored.get("resources") if isinstance(stored, dict) and "resources" in stored else stored)
    else:
        source = "initial_estimate"
        contract = dict(estimate or {})
    return {"family_id": family, "source": source, "resources": contract}


def _memory_mb(value: Any) -> int | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return int(value)
    text = str(value).strip().lower()
    match = re.fullmatch(r"(\d+(?:\.\d+)?)([kmgt]?)b?", text)
    if not match:
        return None
    amount = float(match.group(1))
    unit = match.group(2)
    factor = {"": 1, "k": 1 / 1024, "m": 1, "g": 1024, "t": 1024 * 1024}[unit]
    return int(amount * factor)


def _round_memory_mb(value: float) -> int:
    quantum = 1024
    rounded = int(((value + quantum - 1) // quantum) * quantum)
    return max(quantum, rounded)


def memory_hysteresis(current_mb: int, evidence: list[dict[str, Any]]) -> dict[str, Any]:
    comparable = [item for item in evidence if item.get("comparable") is True]
    if any(item.get("oom") for item in comparable):
        high = max([_memory_mb(item.get("max_rss_mb")) or current_mb for item in comparable] + [current_mb])
        candidate = _round_memory_mb(max(current_mb + 1, high * 1.25))
        if candidate <= current_mb:
            candidate = current_mb + 1024
        return {"decision": "increase", "memory_mb": candidate, "reason": "OOM"}
    highs = [_memory_mb(item.get("max_rss_mb")) for item in comparable if _memory_mb(item.get("max_rss_mb"))]
    if highs and max(highs) >= current_mb * 0.85:
        return {"decision": "increase", "memory_mb": _round_memory_mb(max(highs) * 1.25), "reason": "high_water"}
    lows = [value for value in highs if value < current_mb * 0.5]
    successes = [item for item in comparable if item.get("state") == "COMPLETED"]
    if len(successes) >= 3 and len(lows) >= 3:
        return {"decision": "decrease_candidate", "memory_mb": _round_memory_mb(max(lows) * 1.5), "reason": "three_low_runs"}
    if any(item.get("ambiguous") for item in evidence) or any(item.get("comment_available") is False for item in evidence):
        return {"decision": "keep", "memory_mb": current_mb, "reason": "ambiguous_history"}
    return {"decision": "keep", "memory_mb": current_mb, "reason": "no_new_evidence"}


def right_size_contract(contract: dict[str, Any], evidence: list[dict[str, Any]]) -> dict[str, Any]:
    resources = dict(contract)
    current_mb = _memory_mb(resources.get("memory_mb", resources.get("memory"))) or 0
    decision = memory_hysteresis(current_mb, evidence) if current_mb else {"decision": "keep", "reason": "no_memory_contract"}
    if decision["decision"] in {"increase", "decrease_candidate"}:
        resources["memory_mb"] = decision["memory_mb"]
    if any(item.get("state") == "TIMEOUT" and item.get("comparable") is True for item in evidence):
        resources["walltime_action"] = "increase_candidate"
    resources["cpu_action"] = "stable_first"
    resources["gpu_action"] = "preserve_count_and_type"
    return {"resources": resources, "memory_decision": decision}


def route_candidates(
    site_context: dict[str, Any],
    contract: dict[str, Any],
    local_preferences: dict[str, Any] | None = None,
    fixed_partition: str | None = None,
) -> dict[str, Any]:
    local_preferences = local_preferences or {}
    required_accelerator = contract.get("accelerator_requirement") or contract.get("gpu_type")
    candidates = []
    for partition in site_context.get("partitions", []):
        name = partition.get("partition")
        if fixed_partition and name != fixed_partition:
            continue
        if str(partition.get("availability", "")).lower() not in {"up", "yes", "avail", "available"}:
            continue
        gres = str(partition.get("gres") or "")
        features = str(partition.get("features") or "")
        haystack = f"{gres} {features}".lower()
        if contract.get("gpus", 0) and "gpu" not in haystack:
            continue
        if required_accelerator and str(required_accelerator).lower() not in haystack:
            if contract.get("accelerator_hard", True):
                continue
        candidates.append(dict(partition))

    preferred_partitions = list(local_preferences.get("partition_priority") or [])
    accelerator_priority = [str(item).lower() for item in local_preferences.get("accelerator_priority", [])]

    def score(item: dict[str, Any]) -> tuple[int, int, str]:
        name = str(item.get("partition") or "")
        partition_score = preferred_partitions.index(name) if name in preferred_partitions else len(preferred_partitions)
        text = f"{item.get('gres', '')} {item.get('features', '')}".lower()
        accel_score = len(accelerator_priority)
        for index, accel in enumerate(accelerator_priority):
            if accel and accel in text:
                accel_score = index
                break
        return partition_score, accel_score, name

    ordered = sorted(candidates, key=score)
    return {
        "decision": "route" if ordered else "fail_closed",
        "candidates": ordered,
        "resource_contract": contract,
        "fixed_partition": fixed_partition,
    }


def widening_plan(job: dict[str, Any], candidates: list[str], capabilities: dict[str, Any]) -> dict[str, Any]:
    if job.get("state") == "RUNNING":
        return {"action": "fail_closed", "reason": "running_transition"}
    if job.get("array") or job.get("dependency") or job.get("external_jobid_reference"):
        if not capabilities.get("in_place_partition_update_verified"):
            return {"action": "fail_closed", "reason": "identity_sensitive"}
    if capabilities.get("native_multi_partition"):
        return {"action": "native_widen", "partitions": candidates}
    if job.get("replaceable_pending") and capabilities.get("state_safe_cancel_confirmed"):
        return {"action": "replace_pending", "partitions": candidates}
    return {"action": "fail_closed", "reason": "unverified_widening"}


def duplicate_race_decision(site_policy: dict[str, Any], user_opt_in: bool) -> dict[str, Any]:
    allowed = site_policy.get("duplicate_race") == "allowed" or site_policy.get("race_execution") == "allowed"
    return {"allowed": bool(allowed and user_opt_in), "reason": "explicit_allow_and_opt_in" if allowed and user_opt_in else "disabled_or_missing_authority"}


def bounded_replacement_decision(monitor: dict[str, Any], old_job: dict[str, Any]) -> dict[str, Any]:
    interval = int(monitor.get("poll_interval_seconds") or 0)
    if interval and interval < 60:
        return {"action": "fail_closed", "reason": "tight_polling"}
    if not monitor.get("replacement_reason"):
        return {"action": "observe", "reason": "no_blind_resubmit"}
    if old_job.get("state") != "PENDING" or old_job.get("inactive_confirmed") is not True:
        return {"action": "fail_closed", "reason": "old_job_uncertain"}
    if old_job.get("array") or old_job.get("dependency") or old_job.get("external_jobid_reference"):
        return {"action": "fail_closed", "reason": "identity_sensitive"}
    return {"action": "replace_pending", "reason": monitor["replacement_reason"]}


def _parse_datetime(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        return value
    if not value:
        return None
    text = str(value).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def _parse_duration(value: Any) -> timedelta:
    if isinstance(value, timedelta):
        return value
    if isinstance(value, (int, float)):
        return timedelta(hours=float(value))
    if not value:
        return timedelta(0)
    text = str(value).strip().lower()
    match = re.fullmatch(r"(\d+(?:\.\d+)?)([smhd]?)", text)
    if not match:
        return timedelta(0)
    amount = float(match.group(1))
    unit = match.group(2) or "h"
    return {
        "s": timedelta(seconds=amount),
        "m": timedelta(minutes=amount),
        "h": timedelta(hours=amount),
        "d": timedelta(days=amount),
    }[unit]


def _weekday_index(value: Any) -> int | None:
    if value is None:
        return None
    text = str(value).strip().lower()
    names = {"mon": 0, "monday": 0, "tue": 1, "tuesday": 1, "wed": 2, "wednesday": 2, "thu": 3, "thursday": 3, "fri": 4, "friday": 4, "sat": 5, "saturday": 5, "sun": 6, "sunday": 6}
    if text in names:
        return names[text]
    try:
        value_int = int(text)
    except ValueError:
        return None
    return value_int if 0 <= value_int <= 6 else None


def _parse_time_of_day(value: Any) -> time:
    if not value:
        return time(0, 0)
    text = str(value).strip()
    try:
        parts = [int(part) for part in text.split(":")]
    except ValueError:
        return time(0, 0)
    parts += [0, 0]
    return time(parts[0] % 24, parts[1] % 60, parts[2] % 60)


def next_capacity_window(family: dict[str, Any], invocation: dict[str, Any]) -> dict[str, Any] | None:
    target = dict(invocation.get("target_occurrence") or family.get("target_occurrence") or {})
    recurrence = dict(family.get("recurrence") or {})
    now = _parse_datetime(invocation.get("now") or family.get("now")) or datetime.now(timezone.utc)
    start = _parse_datetime(target.get("start") or target.get("target_start"))
    if start is None and recurrence:
        weekday = _weekday_index(recurrence.get("weekday"))
        if weekday is not None:
            days = (weekday - now.weekday()) % 7
            candidate = datetime.combine((now + timedelta(days=days)).date(), _parse_time_of_day(recurrence.get("start_time") or recurrence.get("start")), tzinfo=now.tzinfo)
            if candidate <= now:
                candidate += timedelta(days=7)
            start = candidate
    if start is None:
        return None
    duration = _parse_duration(target.get("duration") or recurrence.get("duration") or recurrence.get("duration_hours") or family.get("target_duration") or 0)
    if isinstance(recurrence.get("duration_hours"), (int, float)):
        duration = timedelta(hours=float(recurrence["duration_hours"]))
    end = _parse_datetime(target.get("end") or target.get("target_end")) or (start + duration if duration else None)
    minimum_useful_duration = _parse_duration(
        target.get("minimum_useful_duration")
        or family.get("minimum_useful_duration")
        or recurrence.get("minimum_useful_duration")
        or duration
    )
    latest_useful_end = _parse_datetime(target.get("latest_useful_end") or family.get("latest_useful_end") or family.get("cutoff")) or end
    lead_time = _parse_duration(target.get("successor_lead_time") or family.get("successor_lead_time"))
    ready_by = _parse_datetime(target.get("target_ready_by") or family.get("target_ready_by")) or (start - lead_time if lead_time else start)
    return {
        "start": start,
        "end": end,
        "target_ready_by": ready_by,
        "minimum_useful_duration": minimum_useful_duration,
        "latest_useful_end": latest_useful_end,
    }


def _covers_capacity_window(item: dict[str, Any], window: dict[str, Any] | None) -> bool:
    if window is None:
        return True
    start = window["start"]
    minimum_useful_duration = window["minimum_useful_duration"]
    latest_useful_end = window["latest_useful_end"]
    item_start = _parse_datetime(item.get("start_time") or item.get("requested_start") or item.get("eligible_time"))
    item_end = _parse_datetime(item.get("end_time") or item.get("expected_end") or item.get("time_limit_end"))
    if item_start and item_start > start:
        return False
    required_end = latest_useful_end or (start + minimum_useful_duration)
    if item_end is None or required_end is None:
        return False
    if item_end < required_end:
        return False
    return item_end >= start + minimum_useful_duration


def calendar_submit_options_decision(capabilities: dict[str, Any] | None) -> dict[str, Any]:
    capabilities = capabilities or {}
    if capabilities.get("calendar_submit_verified") is True:
        return {"allowed": True, "reason": "calendar_submit_verified"}
    return {"allowed": False, "reason": "calendar_submit_unverified"}


def capacity_reconcile(
    family: dict[str, Any],
    active_allocations: list[dict[str, Any]],
    successors: list[dict[str, Any]],
    invocation: dict[str, Any],
) -> dict[str, Any]:
    if not _activation_matches(family, invocation):
        return {"action": "read_only", "reason": "activation_scope_mismatch"}
    window = next_capacity_window(family, invocation)
    compatible_active = [
        item
        for item in active_allocations
        if _resource_compatible(family, item) and item.get("state") == "RUNNING" and _covers_capacity_window(item, window)
    ]
    if compatible_active:
        return {"action": "reuse_active", "allocation": compatible_active[0], "target_window": _json_safe_window(window), "successor_mutation": False}
    lifecycle_successors = [
        item
        for item in successors
        if item.get("lifecycle_owned") and _resource_compatible(family, item) and _covers_capacity_window(item, window)
    ]
    if len(lifecycle_successors) > 1:
        return {"action": "fail_closed", "reason": "multiple_lifecycle_successors", "successor_mutation": False}
    if lifecycle_successors:
        return {"action": "keep_successor", "successor": lifecycle_successors[0], "target_window": _json_safe_window(window), "successor_mutation": False}
    enrollment = family.get("enrollment") or {}
    if not family.get("auto_maintain_successor") or not _valid_enrollment(family, enrollment):
        return {"action": "read_only_proposal", "reason": "missing_valid_enrollment", "successor_mutation": False}
    if window and family.get("calendar_bound_submission", True):
        calendar_decision = calendar_submit_options_decision(invocation.get("site_capabilities") or family.get("site_capabilities"))
        if not calendar_decision["allowed"]:
            return {"action": "read_only_proposal", "reason": calendar_decision["reason"], "target_window": _json_safe_window(window), "successor_mutation": False}
    return {"action": "plan_one_successor", "max_successors": 1, "target_window": _json_safe_window(window), "successor_mutation": True}


def _json_safe_window(window: dict[str, Any] | None) -> dict[str, Any] | None:
    if not window:
        return None
    safe: dict[str, Any] = {}
    for key, value in window.items():
        if isinstance(value, datetime):
            safe[key] = value.isoformat()
        elif isinstance(value, timedelta):
            safe[key] = int(value.total_seconds())
        else:
            safe[key] = value
    return safe


def _activation_matches(family: dict[str, Any], invocation: dict[str, Any]) -> bool:
    scope = family.get("activation_scope") or {}
    if scope.get("family_id") and scope.get("family_id") != invocation.get("family_id"):
        return False
    if scope.get("accelerator_requirement") and scope.get("accelerator_requirement") != invocation.get("accelerator_requirement"):
        return False
    return invocation.get("mode") == "persistent"


def _resource_compatible(family: dict[str, Any], item: dict[str, Any]) -> bool:
    envelope = family.get("allowed_resource_envelope") or family.get("accepted_resource_contract") or {}
    for key in ("gpus", "gpu_type", "cpus_per_task"):
        if key in envelope and key in item and envelope[key] != item[key]:
            return False
    return True


def _scope_digest(family: dict[str, Any]) -> str:
    scoped = {
        "local_site_id": family.get("local_site_id"),
        "capacity_family_id": family.get("capacity_family_id"),
        "activation_scope": family.get("activation_scope"),
        "accepted_resource_contract": family.get("accepted_resource_contract"),
        "allowed_resource_envelope": family.get("allowed_resource_envelope"),
        "recurrence": family.get("recurrence"),
        "max_successor": 1,
    }
    return hashlib.sha256(json.dumps(scoped, sort_keys=True).encode("utf-8")).hexdigest()


def _valid_enrollment(family: dict[str, Any], enrollment: dict[str, Any]) -> bool:
    if not enrollment.get("submit_successor"):
        return False
    if enrollment.get("max_successor", 1) != 1:
        return False
    digest = enrollment.get("scope_digest")
    return isinstance(digest, str) and digest == _scope_digest(family)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Slurm Workflows routing helper")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("discover", help="Run bounded live Slurm discovery")
    p.add_argument("--local-site-id")
    p.add_argument("--policy-overlay-id")
    p = sub.add_parser("scope-digest", help="Compute a capacity-family enrollment scope digest")
    p.add_argument("family_json", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    if args.command == "discover":
        print(json.dumps(discover_live_site_context(args.local_site_id, args.policy_overlay_id), indent=2, sort_keys=True))
        return 0
    if args.command == "scope-digest":
        family = json.loads(args.family_json.read_text(encoding="utf-8"))
        print(_scope_digest(family))
        return 0
    raise SystemExit(f"unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
