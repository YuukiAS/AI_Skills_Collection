#!/usr/bin/env python3
"""Trusted Host Hook for exact Slurm cancellation requests."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import pwd
import re
import shlex
import stat
import subprocess
import sys
from typing import Any, Optional, Tuple, List, Dict


OPERATION = "ordinary_cancel"
CONFIRM_LABEL = "确认取消"
RETAIN_LABEL = "保留 Job"
QUESTION_HEADER = "取消受保护作业"
EXACT_JOB_ID_RE = re.compile(r"^[0-9]+(?:_[0-9]+)?$")
TOKEN_RE = re.compile(r"^[A-Za-z0-9._:-]{1,256}$")
CANCELABLE_STATES = {"PENDING", "RUNNING"}
SINGLE_QUESTION_RE = re.compile(
    r"^Job (?P<job_id>[0-9]+(?:_[0-9]+)?) 当前位于受保护分区 "
    r"(?P<partition>[A-Za-z0-9_.-]+)。确认取消这个 Job 吗？$"
)
GROUP_QUESTION_PREFIX = "Jobs "
GROUP_QUESTION_SUFFIX = " 将作为同一组取消；其中至少一个 Job 位于受保护分区。确认取消这些 Jobs 吗？"
GROUP_TARGET_RE = re.compile(r"^(?P<job_id>[0-9]+(?:_[0-9]+)?) \[(?P<partition>[A-Za-z0-9_.-]+)\]$")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _emit(value: dict[str, Any]) -> int:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True))
    return 0


def _deny(reason: str) -> int:
    return _emit(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }
    )


def _permission_deny(reason: str) -> int:
    return _emit(
        {
            "hookSpecificOutput": {
                "hookEventName": "PermissionRequest",
                "decision": {"behavior": "deny", "message": reason},
            }
        }
    )


def _post_result(status: str, reason: str, **extra: Any) -> int:
    return _emit({"protected_cancel": status, "reason": reason, **extra})


def _private_path_ok(path: Path, *, directory: bool = False) -> bool:
    try:
        metadata = path.stat()
    except OSError:
        return False
    expected_type = stat.S_ISDIR if directory else stat.S_ISREG
    return metadata.st_uid == os.geteuid() and expected_type(metadata.st_mode) and metadata.st_mode & 0o077 == 0


def _load_runtime(hook_path: Path) -> Tuple[Path, Dict[str, Any]]:
    private_root = hook_path.parent
    runtime_path = private_root / "runtime.json"
    policy_path = private_root / "policy.json"
    if not (
        _private_path_ok(private_root, directory=True)
        and _private_path_ok(hook_path)
        and _private_path_ok(runtime_path)
        and _private_path_ok(policy_path)
    ):
        raise ValueError("private_runtime_permissions_invalid")
    runtime = json.loads(runtime_path.read_text(encoding="utf-8"))
    if not isinstance(runtime, dict):
        raise ValueError("runtime_not_object")
    if runtime.get("schema_version") != 5:
        raise ValueError("runtime_identity_mismatch")
    hook_digest = _sha256(hook_path)
    if (
        runtime.get("hook_file") != hook_path.name
        or runtime.get("hook_sha256") != hook_digest
    ):
        raise ValueError("runtime_hook_mismatch")
    if runtime.get("operation") != OPERATION:
        raise ValueError("runtime_operation_mismatch")
    if runtime.get("policy_file") != policy_path.name or runtime.get("policy_sha256") != _sha256(policy_path):
        raise ValueError("runtime_policy_identity_mismatch")
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    protected = policy.get("protected_cancel_partitions")
    if not isinstance(protected, list) or not protected or not all(isinstance(value, str) and value for value in protected):
        raise ValueError("runtime_policy_invalid")
    runtime["protected_cancel_partitions"] = protected
    environment = runtime.get("environment")
    if not isinstance(environment, dict) or not all(
        isinstance(key, str) and isinstance(value, str) and "\x00" not in value
        for key, value in environment.items()
    ):
        raise ValueError("runtime_environment_invalid")
    for name in ("scontrol_path", "scancel_path", "python_path"):
        path = Path(str(runtime.get(name) or ""))
        if not path.is_absolute() or private_root.parent in path.parents or not path.is_file() or not os.access(path, os.X_OK):
            raise ValueError(f"runtime_{name}_invalid")
        if name != "python_path" and str(path.resolve(strict=True)) != str(runtime.get(f"{name}_realpath")):
            raise ValueError(f"runtime_{name}_identity_mismatch")
    return private_root, runtime


def _parse_scontrol(output: str, expected_job_id: str) -> Optional[Dict[str, str]]:
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
    array_job_id = record.get("ArrayJobId")
    if "_" in expected_job_id:
        if array_job_id != expected_job_id.split("_", 1)[0]:
            return None
    elif array_job_id not in (None, "", "(null)"):
        return None
    partition = record.get("Partition")
    state = record.get("JobState")
    user = record.get("UserId", "").split("(", 1)[0]
    if not partition or state not in CANCELABLE_STATES or user != pwd.getpwuid(os.geteuid()).pw_name:
        return None
    return {"job_id": expected_job_id, "partition": partition, "state": state}


def _clean_environment(runtime: Dict[str, Any]) -> Dict[str, str]:
    return dict(runtime["environment"])


def _resolve_targets(runtime: Dict[str, Any], job_ids: List[str]) -> Optional[List[Dict[str, str]]]:
    resolved = []
    for job_id in job_ids:
        try:
            result = subprocess.run(
                [runtime["scontrol_path"], "show", "job", "-o", job_id],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
                env=_clean_environment(runtime),
            )
        except (OSError, subprocess.TimeoutExpired):
            return None
        target = _parse_scontrol(result.stdout, job_id) if result.returncode == 0 else None
        if target is None:
            return None
        resolved.append(target)
    return resolved


def _question_id_for_targets(targets: list[dict[str, str]]) -> str:
    identity = [{"job_id": target["job_id"], "partition": target["partition"]} for target in targets]
    if len(identity) == 1:
        return f"slurm-protected-cancel:{identity[0]['job_id']}"
    payload = {"operation": OPERATION, "targets": identity}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "slurm-protected-cancel:" + hashlib.sha256(encoded).hexdigest()


def _expected_options(target_count: int = 1) -> list[dict[str, str]]:
    target = "这个 exact Job" if target_count == 1 else "这组 exact Jobs"
    retained = "Job" if target_count == 1 else "Jobs"
    return [
        {"label": CONFIRM_LABEL, "description": f"取消{target}；确认后由受信 Host Hook 重新核验并执行一次。"},
        {"label": RETAIN_LABEL, "description": f"保留 {retained}，不执行取消。"},
    ]


def _question_for_targets(targets: list[dict[str, str]]) -> dict[str, Any]:
    if len(targets) == 1:
        target = targets[0]
        question = f"Job {target['job_id']} 当前位于受保护分区 {target['partition']}。确认取消这个 Job 吗？"
    else:
        rendered = ", ".join(f"{target['job_id']} [{target['partition']}]" for target in targets)
        question = f"{GROUP_QUESTION_PREFIX}{rendered}{GROUP_QUESTION_SUFFIX}"
    return {
        "id": _question_id_for_targets(targets),
        "header": QUESTION_HEADER,
        "question": question,
        "options": _expected_options(len(targets)),
    }


def _targets_from_question(question: Dict[str, Any]) -> Optional[List[Dict[str, str]]]:
    canonical_keys = {"id", "header", "question", "options"}
    keys = set(question)
    if keys == canonical_keys | {"isOther", "isSecret"}:
        if question["isOther"] is not True or question["isSecret"] is not False:
            return None
    elif keys != canonical_keys:
        return None
    text = question.get("question")
    if not isinstance(text, str):
        return None
    single = SINGLE_QUESTION_RE.fullmatch(text)
    if single:
        targets = [{"job_id": single.group("job_id"), "partition": single.group("partition")}]
    elif text.startswith(GROUP_QUESTION_PREFIX) and text.endswith(GROUP_QUESTION_SUFFIX):
        body = text[len(GROUP_QUESTION_PREFIX) : -len(GROUP_QUESTION_SUFFIX)]
        targets = []
        for item in body.split(", "):
            parsed = GROUP_TARGET_RE.fullmatch(item)
            if parsed is None:
                return None
            targets.append({"job_id": parsed.group("job_id"), "partition": parsed.group("partition")})
        if len(targets) < 2:
            return None
    else:
        return None
    expected = _question_for_targets(targets)
    canonical = {key: question[key] for key in canonical_keys}
    return targets if canonical == expected else None


def _parse_cancel_command(command: Any, runtime: Dict[str, Any]) -> Tuple[Optional[List[str]], Optional[str]]:
    if not isinstance(command, str):
        return None, None
    try:
        arguments = shlex.split(command, posix=True)
    except ValueError:
        return None, "unsupported_scancel_syntax" if "scancel" in command else None
    if not arguments:
        return None, None
    executable = arguments[0]
    accepted = {"scancel", runtime["scancel_path"], runtime["scancel_path_realpath"]}
    looks_like_cancel = executable == "scancel" or Path(executable).name == "scancel"
    contains_cancel = any(token == "scancel" or Path(token).name == "scancel" for token in arguments)
    if not looks_like_cancel:
        if contains_cancel or re.search(r"(^|[^A-Za-z0-9_.-])scancel([^A-Za-z0-9_.-]|$)", command):
            return None, "unsupported_compound_scancel_command"
        return None, None
    if executable not in accepted:
        return None, "untrusted_scancel_executable"
    job_ids = arguments[1:]
    if not job_ids or len(job_ids) != len(set(job_ids)) or any(not EXACT_JOB_ID_RE.fullmatch(value) for value in job_ids):
        return None, "unsupported_scancel_target_or_option"
    return job_ids, None


def _replace_json(path: Path, value: Dict[str, Any]) -> None:
    temporary = path.with_name(".{}.{}.tmp".format(path.name, os.getpid()))
    descriptor = os.open(str(temporary), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(str(temporary), str(path))
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def _reconciliation_snapshot(runtime: Dict[str, Any], targets: List[Dict[str, str]]) -> List[Dict[str, str]]:
    snapshots = []
    for target in targets:
        resolved = _resolve_targets(runtime, [target["job_id"]])
        if resolved is None:
            snapshots.append({"job_id": target["job_id"], "state": "NOT_VISIBLE"})
        else:
            snapshots.append(resolved[0])
    return snapshots


def _event_cwd_valid(event: dict[str, Any]) -> bool:
    cwd = Path(str(event.get("cwd") or ""))
    return cwd.is_absolute() and cwd.is_dir()


def _protected_reason(targets: list[dict[str, str]]) -> str:
    question = _question_for_targets(targets)
    payload = {
        "status": "NEEDS_INTERACTIVE_CHAT_CONFIRMATION",
        "operation": OPERATION,
        "targets": targets,
        "request_user_input": {"questions": [question]},
        "mutation_count": 0,
    }
    if len(targets) == 1:
        target = targets[0]
        prefix = (
            "NEEDS_INTERACTIVE_CHAT_CONFIRMATION "
            f"job_id={target['job_id']} partition={target['partition']} "
        )
    else:
        prefix = f"NEEDS_INTERACTIVE_CHAT_CONFIRMATION target_count={len(targets)} "
    return prefix + json.dumps(payload, ensure_ascii=False, sort_keys=True)


def _pre_tool_use(event: dict[str, Any], runtime: dict[str, Any]) -> int:
    if event.get("tool_name") != "Bash":
        return _emit({})
    tool_input = event.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    job_ids, error = _parse_cancel_command(command, runtime)
    if error:
        return _deny(f"SLURM_CANCEL_DENIED reason={error}")
    if job_ids is None:
        return _emit({})
    if not _event_cwd_valid(event):
        return _deny("SLURM_CANCEL_DENIED reason=invalid_cwd")
    targets = _resolve_targets(runtime, job_ids)
    if targets is None:
        return _deny("SLURM_CANCEL_DENIED reason=target_resolution_failed")
    protected = set(runtime["protected_cancel_partitions"])
    if any(target["partition"] in protected for target in targets):
        return _deny(_protected_reason(targets))
    return _emit({})


def _permission_request(event: dict[str, Any], runtime: dict[str, Any]) -> int:
    if event.get("tool_name") != "Bash":
        return _emit({})
    tool_input = event.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    job_ids, error = _parse_cancel_command(command, runtime)
    if error:
        return _permission_deny(f"SLURM_CANCEL_DENIED reason={error}")
    if job_ids is None:
        return _emit({})
    if not _event_cwd_valid(event):
        return _permission_deny("SLURM_CANCEL_DENIED reason=invalid_cwd")
    targets = _resolve_targets(runtime, job_ids)
    if targets is None:
        return _permission_deny("SLURM_CANCEL_DENIED reason=target_resolution_failed")
    protected = set(runtime["protected_cancel_partitions"])
    if any(target["partition"] in protected for target in targets):
        return _permission_deny(_protected_reason(targets))
    return _emit({})


def _response_object(value: Any) -> dict[str, Any]:
    if isinstance(value, str):
        value = json.loads(value)
    if not isinstance(value, dict):
        raise ValueError("response_not_object")
    return value


def _post_tool_use(event: dict[str, Any], private_root: Path, runtime: dict[str, Any]) -> int:
    if event.get("tool_name") != "request_user_input":
        return _post_result("ignored", "wrong_tool")
    if event.get("agent_id") is not None or event.get("agent_type") is not None:
        return _post_result("denied", "not_root_interactive_session")
    if not _event_cwd_valid(event):
        return _post_result("denied", "invalid_cwd")
    identifiers: dict[str, str] = {}
    for name in ("session_id", "turn_id", "tool_use_id"):
        value = event.get(name)
        if not isinstance(value, str) or not TOKEN_RE.fullmatch(value):
            return _post_result("denied", f"invalid_{name}")
        identifiers[name] = value
    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict) or set(tool_input) != {"questions"}:
        return _post_result("denied", "invalid_tool_input")
    questions = tool_input.get("questions")
    if not isinstance(questions, list) or len(questions) != 1 or not isinstance(questions[0], dict):
        return _post_result("denied", "wrong_question_count")
    question = questions[0]
    targets = _targets_from_question(question)
    if targets is None:
        return _post_result("denied", "question_contract_mismatch")
    question_id = question["id"]
    try:
        response = _response_object(event.get("tool_response"))
    except (json.JSONDecodeError, TypeError, ValueError):
        return _post_result("denied", "invalid_tool_response")
    answers = response.get("answers")
    answer = answers.get(question_id) if isinstance(answers, dict) else None
    if isinstance(answer, dict) and answer.get("answers") == [RETAIN_LABEL]:
        return _post_result("retained", "user_retained", mutation_count=0)
    if not isinstance(answer, dict) or answer.get("answers") != [CONFIRM_LABEL]:
        return _post_result("denied", "not_explicit_confirmation", mutation_count=0)
    current = _resolve_targets(runtime, [target["job_id"] for target in targets])
    if current is None:
        return _post_result("denied", "target_resolution_failed")
    declared = [{"job_id": target["job_id"], "partition": target["partition"]} for target in targets]
    actual = [{"job_id": target["job_id"], "partition": target["partition"]} for target in current]
    protected = set(runtime["protected_cancel_partitions"])
    if actual != declared or not any(target["partition"] in protected for target in current):
        return _post_result("denied", "target_or_partition_changed")
    reservation_id = hashlib.sha256(
        "\0".join([identifiers["session_id"], identifiers["turn_id"], identifiers["tool_use_id"], question_id]).encode("utf-8")
    ).hexdigest()
    consumed_dir = private_root / "consumed"
    consumed_dir.mkdir(mode=0o700, exist_ok=True)
    if not _private_path_ok(consumed_dir, directory=True):
        return _post_result("denied", "consumed_permissions_invalid")
    reservation_path = consumed_dir / f"{reservation_id}.json"
    reservation = {
        **identifiers,
        "question_id": question_id,
        "targets": current,
        "operation": OPERATION,
        "status": "reserved",
    }
    try:
        descriptor = os.open(reservation_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        return _post_result("denied", "replayed_or_duplicate_confirmation")
    except OSError:
        return _post_result("denied", "reservation_failed")
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(reservation, stream, sort_keys=True)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    # The durable one-shot reservation precedes the final scheduler read.
    # Drift consumes this identity without ever invoking scancel.
    rechecked = _resolve_targets(runtime, [target["job_id"] for target in current])
    if rechecked != current:
        reservation["status"] = "pre_invocation_failed"
        reservation["reason"] = "target_changed_after_reservation"
        _replace_json(reservation_path, reservation)
        return _post_result("denied", "target_changed_after_reservation", mutation_count=0)
    try:
        cancelled = subprocess.run(
            [runtime["scancel_path"], *[target["job_id"] for target in current]],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
            env=_clean_environment(runtime),
        )
    except OSError as error:
        reservation["status"] = "pre_invocation_failed"
        reservation["error"] = type(error).__name__
        _replace_json(reservation_path, reservation)
        return _post_result("denied", "scancel_pre_invocation_failed")
    except subprocess.TimeoutExpired:
        reservation["status"] = "ambiguous"
        reservation["reconciliation"] = _reconciliation_snapshot(runtime, current)
        _replace_json(reservation_path, reservation)
        return _post_result("ambiguous", "scancel_timeout_after_possible_invocation", reconciliation=reservation["reconciliation"])
    if cancelled.returncode != 0:
        reservation["status"] = "ambiguous"
        reservation["returncode"] = cancelled.returncode
        reservation["reconciliation"] = _reconciliation_snapshot(runtime, current)
        _replace_json(reservation_path, reservation)
        return _post_result("ambiguous", "scancel_nonzero_after_possible_invocation", returncode=cancelled.returncode, reconciliation=reservation["reconciliation"])
    reservation["status"] = "completed"
    reservation["returncode"] = 0
    _replace_json(reservation_path, reservation)
    return _post_result("executed", "confirmed", job_ids=[target["job_id"] for target in current])


def main() -> int:
    hook_path = Path(__file__).resolve()
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        print("SLURM_CANCEL_DENIED reason=invalid_hook_json", file=sys.stderr)
        return 2
    try:
        private_root, runtime = _load_runtime(hook_path)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        if event.get("hook_event_name") == "PreToolUse":
            return _deny(f"SLURM_CANCEL_DENIED reason={error}")
        if event.get("hook_event_name") == "PermissionRequest":
            return _permission_deny(f"SLURM_CANCEL_DENIED reason={error}")
        return _post_result("denied", str(error))
    if event.get("hook_event_name") == "PreToolUse":
        return _pre_tool_use(event, runtime)
    if event.get("hook_event_name") == "PermissionRequest":
        return _permission_request(event, runtime)
    if event.get("hook_event_name") == "PostToolUse":
        return _post_tool_use(event, private_root, runtime)
    return _post_result("ignored", "wrong_hook_event")


if __name__ == "__main__":
    raise SystemExit(main())
