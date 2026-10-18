#!/usr/bin/env python3
"""Private Host Hook binder for one exact protected Slurm cancellation."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import pwd
import re
import stat
import subprocess
import sys
from typing import Any


OPERATION = "ordinary_cancel"
CONFIRM_LABEL = "确认取消"
RETAIN_LABEL = "保留 Job"
QUESTION_HEADER = "确认取消"
EXACT_JOB_ID_RE = re.compile(r"^[0-9]+(?:_[0-9]+)?$")
TOKEN_RE = re.compile(r"^[A-Za-z0-9._:-]{1,256}$")
QUESTION_RE = re.compile(
    r"^Job (?P<job_id>[0-9]+(?:_[0-9]+)?) 当前位于受保护分区 "
    r"(?P<partition>[A-Za-z0-9_.-]+)。确认取消这个 Job 吗？$"
)
CANCELABLE_STATES = {"PENDING", "RUNNING"}


def _fail(reason: str, code: int) -> int:
    print(json.dumps({"protected_cancel": "denied", "reason": reason}, sort_keys=True))
    return code


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected object")
    return value


def _private_path_ok(path: Path, *, directory: bool = False) -> bool:
    try:
        metadata = path.stat()
    except OSError:
        return False
    expected_type = stat.S_ISDIR if directory else stat.S_ISREG
    return metadata.st_uid == os.geteuid() and expected_type(metadata.st_mode) and metadata.st_mode & 0o077 == 0


def _response_object(value: Any) -> dict[str, Any]:
    if isinstance(value, str):
        value = json.loads(value)
    if not isinstance(value, dict):
        raise ValueError("response is not an object")
    return value


def _parse_scontrol(output: str, expected_job_id: str) -> tuple[str, str] | None:
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if len(lines) != 1:
        return None
    record: dict[str, str] = {}
    for token in lines[0].split():
        if "=" in token:
            key, value = token.split("=", 1)
            record[key] = value
    if record.get("JobId") != expected_job_id:
        return None
    if record.get("HetJobId") not in (None, "", "(null)"):
        return None
    array_parent = record.get("ArrayJobId")
    if array_parent not in (None, "", "(null)") and "_" not in expected_job_id:
        return None
    scheduler_user = str(record.get("UserId") or "").split("(", 1)[0]
    if scheduler_user != pwd.getpwuid(os.geteuid()).pw_name:
        return None
    partition = str(record.get("Partition") or "").strip()
    state = str(record.get("JobState") or "").split("+", 1)[0].upper()
    if not partition or state not in CANCELABLE_STATES:
        return None
    return partition, state


def _question_id(job_id: str, partition: str) -> str:
    payload = {"job_id": job_id, "operation": OPERATION, "partition": partition}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "slurm_protected_cancel_" + hashlib.sha256(encoded).hexdigest()


def _expected_options() -> list[dict[str, str]]:
    return [
        {
            "label": CONFIRM_LABEL,
            "description": "取消这个 exact Job；确认后由受信 Host Hook 重新核验并执行一次。",
        },
        {"label": RETAIN_LABEL, "description": "保留 Job，不执行取消。"},
    ]


def main() -> int:
    binder_path = Path(__file__).resolve()
    project_root = binder_path.parents[3]
    private_root = project_root / ".codex/slurm-protected-cancel-private"
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return _fail("invalid_json", 2)

    if event.get("hook_event_name") != "PostToolUse" or event.get("tool_name") != "request_user_input":
        return _fail("wrong_hook_event", 3)
    if event.get("agent_id") is not None or event.get("agent_type") is not None:
        return _fail("not_root_interactive_session", 4)
    try:
        if Path(str(event.get("cwd") or "")).resolve() != project_root:
            return _fail("wrong_project", 5)
    except OSError:
        return _fail("wrong_project", 5)

    identifiers: dict[str, str] = {}
    for name in ("session_id", "turn_id", "tool_use_id"):
        value = event.get(name)
        if not isinstance(value, str) or not TOKEN_RE.fullmatch(value):
            return _fail(f"invalid_{name}", 6)
        identifiers[name] = value

    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict) or set(tool_input) != {"questions"}:
        return _fail("invalid_tool_input", 7)
    questions = tool_input.get("questions")
    if not isinstance(questions, list) or len(questions) != 1 or not isinstance(questions[0], dict):
        return _fail("wrong_question_count", 8)
    question = questions[0]
    if set(question) != {"id", "header", "question", "options"}:
        return _fail("question_contract_mismatch", 9)
    parsed = QUESTION_RE.fullmatch(str(question.get("question") or ""))
    if not parsed:
        return _fail("question_contract_mismatch", 9)
    job_id = parsed.group("job_id")
    declared_partition = parsed.group("partition")
    expected_question_id = _question_id(job_id, declared_partition)
    if (
        question.get("id") != expected_question_id
        or question.get("header") != QUESTION_HEADER
        or question.get("options") != _expected_options()
    ):
        return _fail("question_contract_mismatch", 9)

    try:
        response = _response_object(event.get("tool_response"))
    except (json.JSONDecodeError, TypeError, ValueError):
        return _fail("invalid_tool_response", 10)
    answers = response.get("answers")
    if not isinstance(answers, dict):
        return _fail("not_explicit_confirmation", 11)
    answer = answers.get(expected_question_id)
    if not isinstance(answer, dict) or answer.get("answers") != [CONFIRM_LABEL]:
        return _fail("not_explicit_confirmation", 11)

    runtime_path = private_root / "runtime.json"
    capability_path = private_root / "capability.key"
    if not (
        _private_path_ok(binder_path)
        and _private_path_ok(private_root, directory=True)
        and _private_path_ok(runtime_path)
        and _private_path_ok(capability_path)
    ):
        return _fail("private_authority_permissions_invalid", 12)
    try:
        runtime = _load_json(runtime_path)
        capability = _load_json(capability_path)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return _fail("private_authority_unavailable", 12)
    if runtime.get("schema_version") != 1 or runtime.get("project_root") != str(project_root):
        return _fail("runtime_identity_mismatch", 13)
    if runtime.get("binder_path") != str(binder_path) or runtime.get("binder_sha256") != _sha256(binder_path):
        return _fail("runtime_binder_mismatch", 14)
    if runtime.get("operation") != OPERATION:
        return _fail("runtime_operation_mismatch", 15)
    protected = runtime.get("protected_cancel_partitions")
    if not isinstance(protected, list) or declared_partition not in protected:
        return _fail("partition_not_protected", 16)

    if (
        capability.get("schema_version") != 1
        or capability.get("project_root") != str(project_root)
        or capability.get("session_id") != identifiers["session_id"]
        or capability.get("session_id") != runtime.get("active_session_id")
        or capability.get("hook_version") != runtime.get("session_hook_sha256")
        or not isinstance(capability.get("capability"), str)
        or not re.fullmatch(r"[0-9a-f]{64}", capability["capability"])
    ):
        return _fail("capability_mismatch", 17)

    scontrol_path = Path(str(runtime.get("scontrol_path") or ""))
    scancel_path = Path(str(runtime.get("scancel_path") or ""))
    if not scontrol_path.is_absolute() or not scancel_path.is_absolute():
        return _fail("runtime_executable_not_absolute", 18)
    if project_root in scontrol_path.parents or project_root in scancel_path.parents:
        return _fail("runtime_executable_inside_project", 19)
    if not os.access(scontrol_path, os.X_OK) or not os.access(scancel_path, os.X_OK):
        return _fail("runtime_executable_unavailable", 20)

    try:
        resolved = subprocess.run(
            [str(scontrol_path), "show", "job", "-o", job_id],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return _fail("job_reresolution_failed", 21)
    current = _parse_scontrol(resolved.stdout, job_id) if resolved.returncode == 0 else None
    if current is None:
        return _fail("job_reresolution_failed", 21)
    current_partition, current_state = current
    if current_partition != declared_partition or current_partition not in protected:
        return _fail("target_or_partition_changed", 22)

    reservation_id = hashlib.sha256(
        "\0".join(
            [
                identifiers["session_id"],
                identifiers["turn_id"],
                identifiers["tool_use_id"],
                expected_question_id,
            ]
        ).encode("utf-8")
    ).hexdigest()
    consumed_dir = private_root / "consumed"
    consumed_dir.mkdir(mode=0o700, exist_ok=True)
    if not _private_path_ok(consumed_dir, directory=True):
        return _fail("consumed_permissions_invalid", 24)
    reservation_path = consumed_dir / f"{reservation_id}.json"
    reservation = {
        **identifiers,
        "question_id": expected_question_id,
        "job_id": job_id,
        "partition": current_partition,
        "state_before": current_state,
        "operation": OPERATION,
        "status": "reserved",
    }
    try:
        descriptor = os.open(reservation_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return _fail("replayed_or_duplicate_confirmation", 23)
    except OSError:
        return _fail("reservation_failed", 24)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(reservation, stream, sort_keys=True)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())

    clean_env = {key: value for key, value in os.environ.items() if not key.startswith("SCANCEL_")}
    try:
        cancelled = subprocess.run(
            [str(scancel_path), job_id],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
            env=clean_env,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        reservation.update({"status": "scancel_error", "error_type": type(error).__name__})
        _atomic_json(reservation_path, reservation)
        return _fail("scancel_failed_after_reservation", 25)
    reservation.update({"status": "executed" if cancelled.returncode == 0 else "scancel_failed", "returncode": cancelled.returncode})
    _atomic_json(reservation_path, reservation)
    if cancelled.returncode != 0:
        return _fail("scancel_failed_after_reservation", 25)
    print(json.dumps({"protected_cancel": "executed", "job_id": job_id}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
