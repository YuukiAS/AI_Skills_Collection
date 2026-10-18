#!/usr/bin/env python3
"""Host-side session capability lifecycle for protected cancellation."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import secrets
import sys
from typing import Any


def _atomic_json(path: Path, value: dict[str, Any], mode: int = 0o600) -> None:
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        os.chmod(path, mode)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def main() -> int:
    session_script = Path(__file__).resolve()
    project_root = session_script.parents[2]
    private_root = project_root / ".codex/slurm-protected-cancel-private"
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 2
    if event.get("agent_id") is not None or event.get("agent_type") is not None:
        return 3
    try:
        if Path(str(event.get("cwd") or "")).resolve() != project_root:
            return 4
        runtime_path = private_root / "runtime.json"
        runtime = json.loads(runtime_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 5
    if runtime.get("project_root") != str(project_root):
        return 6
    if runtime.get("session_hook_path") != str(session_script):
        return 7
    if runtime.get("session_hook_sha256") != hashlib.sha256(session_script.read_bytes()).hexdigest():
        return 8
    session_id = event.get("session_id")
    if not isinstance(session_id, str) or not session_id:
        return 9

    private_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(private_root, 0o700)
    for name in ("bin", "consumed", "audit"):
        directory = private_root / name
        directory.mkdir(mode=0o700, exist_ok=True)
        os.chmod(directory, 0o700)

    if event.get("hook_event_name") == "SessionEnd":
        capability_path = private_root / "capability.key"
        try:
            capability = json.loads(capability_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            capability = {}
        if capability.get("session_id") == session_id:
            try:
                capability_path.unlink()
            except FileNotFoundError:
                pass
        if runtime.get("active_session_id") == session_id:
            runtime["active_session_id"] = None
            runtime["active_session_started_at"] = None
            _atomic_json(runtime_path, runtime)
        return 0
    if event.get("hook_event_name") != "SessionStart":
        return 10

    now = datetime.now(timezone.utc).isoformat()
    capability = {
        "schema_version": 1,
        "capability": secrets.token_hex(32),
        "session_id": session_id,
        "project_root": str(project_root),
        "hook_version": runtime.get("session_hook_sha256"),
        "created_at": now,
    }
    runtime["active_session_id"] = session_id
    runtime["active_session_started_at"] = now
    _atomic_json(private_root / "capability.key", capability)
    _atomic_json(runtime_path, runtime)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
