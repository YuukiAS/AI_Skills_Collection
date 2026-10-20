#!/usr/bin/env python3
"""Stdio MCP Hook: native elicitation and one-shot protected cancellation.

The independent command supervisor always denies the original protected Bash
invocation. This server never asks the model to transport a user's answer.
"""
from __future__ import annotations

import asyncio
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


PROBE_COMMAND = "printf '__SLURM_PROTECTED_CANCEL_CARD_PROBE__\\n'"
DECISION_SCHEMA = {
    "type": "object",
    "properties": {"decision": {
        "type": "string", "title": "取消受保护作业",
        "oneOf": [
            {"const": "confirm", "title": "确认取消"},
            {"const": "retain", "title": "保留 Job"},
        ],
    }},
    "required": ["decision"],
}
TOOL_NAME = "slurm_protected_cancel"
ROOT = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("protected_cancel_guard", ROOT / "slurm_cancel_hook.py")
assert _spec is not None and _spec.loader is not None
guard = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(guard)


def block(status: str, reason: str, **extra: Any) -> dict:
    result = {"protected_cancel": status, "reason": reason, "mutation_count": 0, **extra}
    return {"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny",
        "permissionDecisionReason": json.dumps(result, ensure_ascii=False, sort_keys=True),
        "additionalContext": "Protected cancellation was handled by the trusted MCP Hook. Do not call request_user_input or retry scancel.",
    }}


def audit(private: Path, identity: dict, phase: str, **data: Any) -> None:
    directory = private / "audit"
    directory.mkdir(mode=0o700, exist_ok=True)
    if not guard._private_path_ok(directory, directory=True):
        raise ValueError("audit_permissions_invalid")
    key = hashlib.sha256("\0".join(identity.values()).encode()).hexdigest()
    # One record per immutable event phase; never append interleaved JSON.
    record = {**identity, "phase": phase, "time_ns": time.time_ns(), **data}
    path = directory / (key + "." + phase + ".json")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        json.dump(record, stream, ensure_ascii=False, sort_keys=True)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    directory_fd = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def validate_context(event: Any, metadata: Any) -> dict[str, str]:
    if not isinstance(event, dict) or not isinstance(metadata, dict):
        raise ValueError("invalid_hook_context")
    if event.get("hook_event_name") != "PreToolUse" or event.get("tool_name") != "Bash":
        raise ValueError("wrong_hook_event")
    if event.get("agent_id") is not None or event.get("agent_type") is not None:
        raise ValueError("not_root_interactive_session")
    identity = {}
    for name in ("session_id", "turn_id", "tool_use_id"):
        value = event.get(name)
        if not isinstance(value, str) or not guard.TOKEN_RE.fullmatch(value):
            raise ValueError("invalid_" + name)
        identity[name] = value
    if metadata.get("threadId") != identity["session_id"]:
        raise ValueError("owning_thread_mismatch")
    if not guard._event_cwd_valid(event):
        raise ValueError("invalid_cwd")
    return identity


def possible_invocation(private: Path, event: Any) -> bool:
    """Never report zero mutation after a durable invocation intent exists."""
    if not isinstance(event, dict):
        return False
    values = [event.get(key) for key in ("session_id", "turn_id", "tool_use_id")]
    if not all(isinstance(value, str) and guard.TOKEN_RE.fullmatch(value) for value in values):
        return False
    key = hashlib.sha256("\0".join(values).encode()).hexdigest()
    return (private / "audit" / (key + ".invocation_intent.json")).exists()


def execute_confirmed(private: Path, runtime: dict, identity: dict,
                      before: list[dict[str, str]]) -> dict:
    """Reuse guard resolution/identity and reserve before the last scheduler read."""
    job_ids = [target["job_id"] for target in before]
    current = guard._resolve_targets(runtime, job_ids)
    if current != before:
        return block("denied", "target_changed_before_reservation")
    question_id = guard._question_id_for_targets(before)
    reservation_id = hashlib.sha256("\0".join([
        identity["session_id"], identity["turn_id"], identity["tool_use_id"], question_id,
    ]).encode()).hexdigest()
    directory = private / "consumed"
    directory.mkdir(mode=0o700, exist_ok=True)
    if not guard._private_path_ok(directory, directory=True):
        return block("denied", "consumed_permissions_invalid")
    reservation = {**identity, "question_id": question_id, "targets": current,
                   "operation": guard.OPERATION, "status": "reserved"}
    path = directory / (reservation_id + ".json")
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return block("denied", "replayed_or_duplicate_confirmation")
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        json.dump(reservation, stream, sort_keys=True)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    directory_fd = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)
    audit(private, identity, "reserved", targets=current, reservation=reservation_id)
    rechecked = guard._resolve_targets(runtime, job_ids)
    if rechecked != current:
        reservation.update(status="pre_invocation_failed", reason="target_changed_after_reservation")
        guard._replace_json(path, reservation)
        return block("denied", "target_changed_after_reservation")
    audit(private, identity, "final_resolved", targets=rechecked)
    try:
        # Durable intent is recorded before the only possible invocation. An
        # interruption from this point is consumed and must never be retried.
        audit(private, identity, "invocation_intent", executable=runtime["scancel_path"], job_ids=job_ids)
        completed = subprocess.run(
            [runtime["scancel_path"], *job_ids], check=False, capture_output=True,
            text=True, timeout=10, env=guard._clean_environment(runtime),
        )
    except OSError as error:
        reservation.update(status="pre_invocation_failed", error=type(error).__name__)
        guard._replace_json(path, reservation)
        return block("denied", "scancel_pre_invocation_failed")
    except subprocess.TimeoutExpired:
        reservation.update(status="ambiguous", reconciliation=guard._reconciliation_snapshot(runtime, current))
        guard._replace_json(path, reservation)
        return block("ambiguous", "scancel_timeout_after_possible_invocation", mutation_count=None)
    reservation.update(status="completed" if completed.returncode == 0 else "ambiguous", returncode=completed.returncode)
    guard._replace_json(path, reservation)
    audit(private, identity, "invocation_returned", returncode=completed.returncode, targets=current)
    return block("executed" if completed.returncode == 0 else "ambiguous", "confirmed", mutation_count=1, job_ids=job_ids)


async def handle(event: dict, metadata: dict, private: Path, runtime: dict, elicit) -> dict:
    tool_input = event.get("tool_input") if isinstance(event, dict) else None
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    probe = command == PROBE_COMMAND
    targets = None
    if not probe:
        job_ids, error = guard._parse_cancel_command(command, runtime)
        if error:
            return block("denied", error)
        if job_ids is None:
            return {}
    identity = validate_context(event, metadata)
    if not probe:
        targets = guard._resolve_targets(runtime, job_ids)
        if targets is None:
            return block("denied", "target_resolution_failed")
        if not any(item["partition"] in runtime["protected_cancel_partitions"] for item in targets):
            return {}
    audit(private, identity, "elicitation_requested", probe=probe, targets=targets, schema=DECISION_SCHEMA,
          command=command, metadata_thread_id=metadata["threadId"])
    message = ("确认组件无害验证；任何选择均不会取消 Job 或执行命令。" if probe else
               "取消受保护作业：" + ", ".join(item["job_id"] + " [" + item["partition"] + "]" for item in targets))
    try:
        response = await asyncio.wait_for(elicit(message, DECISION_SCHEMA), timeout=600)
    except Exception as error:
        audit(private, identity, "elicitation_failed", error=type(error).__name__, probe=probe)
        return block("denied", "elicitation_failed")
    if hasattr(response, "model_dump"):
        response = response.model_dump(by_alias=True, exclude_none=True)
    audit(private, identity, "elicitation_answered", response=response, probe=probe)
    if (not isinstance(response, dict) or response.get("action") != "accept"
            or not isinstance(response.get("content"), dict)
            or set(response["content"]) != {"decision"}
            or response["content"]["decision"] not in ("confirm", "retain")):
        return block("denied", "not_explicit_confirmation")
    if probe:
        return block("probe_completed", "no_scheduler_or_shell_operation")
    if response["content"]["decision"] == "retain":
        audit(private, identity, "retained", targets=targets, mutation_count=0)
        return block("retained", "user_retained")
    result = execute_confirmed(private, runtime, identity, targets)
    audit(private, identity, "result", result=result)
    return result


async def main() -> None:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp import types

    private, runtime = guard._load_runtime(ROOT / "slurm_cancel_hook.py")
    identity_path = ROOT / "mcp_identity.json"
    if not guard._private_path_ok(identity_path):
        raise ValueError("mcp_identity_permissions_invalid")
    identity = json.loads(identity_path.read_text(encoding="utf-8"))
    if guard._sha256(Path(__file__).resolve()) != identity["server_sha256"]:
        raise ValueError("mcp_server_identity_mismatch")
    if importlib.metadata.version("mcp") != identity["sdk_version"]:
        raise ValueError("mcp_sdk_version_mismatch")
    if sys.argv[1:] == ["--check"]:
        print(json.dumps({"sdk_version": identity["sdk_version"], "server_sha256": identity["server_sha256"]}))
        return
    server = Server("slurm-protected-cancel")

    @server.list_tools()
    async def list_tools():
        return [types.Tool(name=TOOL_NAME,
            description="Trusted PreToolUse Hook: confirm exact protected Slurm cancellation in the owning chat; retain/close never cancels.",
            inputSchema={"type": "object", "properties": {
                "event": {"type": "object"}, "server_sha256": {"type": "string"},
            }, "required": ["event", "server_sha256"], "additionalProperties": False},
            annotations=types.ToolAnnotations(readOnlyHint=False, destructiveHint=True, idempotentHint=False, openWorldHint=False))]

    @server.call_tool()
    async def call_tool(name, arguments):
        try:
            if name != TOOL_NAME or set(arguments) != {"event", "server_sha256"}:
                raise ValueError("invalid_tool_input")
            if arguments["server_sha256"] != identity["server_sha256"]:
                raise ValueError("trusted_hook_identity_mismatch")
            ctx = server.request_context
            meta = ctx.meta.model_dump(by_alias=True) if hasattr(ctx.meta, "model_dump") else ctx.meta
            async def elicit(message, schema):
                return await ctx.session.elicit_form(message, schema, related_request_id=ctx.request_id)
            result = await handle(arguments["event"], meta, private, runtime, elicit)
        except Exception as error:
            ambiguous = possible_invocation(private, arguments.get("event") if isinstance(arguments, dict) else None)
            result = block("ambiguous" if ambiguous else "denied", type(error).__name__ + ":" + str(error),
                           mutation_count=None if ambiguous else 0)
        return [types.TextContent(type="text", text=json.dumps(result, ensure_ascii=False, sort_keys=True))]

    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
