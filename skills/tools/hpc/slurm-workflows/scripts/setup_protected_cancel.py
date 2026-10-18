#!/usr/bin/env python3
"""Render or install the project-local protected-cancel runtime contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
from typing import Any


PRIVATE_REL = Path(".codex/slurm-protected-cancel-private")
HOOKS_REL = Path(".codex/hooks.json")
CONFIG_REL = Path(".codex/config.toml")
RULES_REL = Path(".codex/rules/slurm-protected-cancel.rules")
SESSION_REL = Path(".codex/hooks/slurm-protected-cancel-session")
SHIM_REL = Path(".codex/automation-bin/scancel")

HOOK_EVENT_KEYS = {
    "PostToolUse": "post_tool_use",
    "SessionEnd": "session_end",
    "SessionStart": "session_start",
}


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _source_dir() -> Path:
    return Path(__file__).resolve().parent


def _read_sources(skill_scripts: Path) -> tuple[bytes, bytes]:
    binder = (skill_scripts / "slurm_cancel_binder.py").read_bytes()
    session = (skill_scripts / "slurm_cancel_session.py").read_bytes()
    return binder, session


def _absolute_executable(path: Path, project_root: Path) -> Path:
    resolved = path.expanduser().resolve(strict=True)
    if not resolved.is_absolute() or not resolved.is_file() or not os.access(resolved, os.X_OK):
        raise ValueError(f"not an executable file: {path}")
    try:
        resolved.relative_to(project_root)
    except ValueError:
        return resolved
    raise ValueError(f"trusted executable must be outside project root: {resolved}")


def _hash_checked_command(executable: str | None, script: Path, digest: str, *arguments: str) -> str:
    invocation = 'exec "$target" "$@"'
    if executable is not None:
        invocation = f"exec {shlex.quote(executable)} \"$target\" \"$@\""
    positional = " ".join(shlex.quote(str(value)) for value in (script, digest, *arguments))
    return (
        "/usr/bin/bash -c 'set -eu; target=$1; expected=$2; "
        "actual=$(/usr/bin/sha256sum -- \"$target\"); actual=${actual%% *}; "
        "[ \"$actual\" = \"$expected\" ] || exit 78; shift 2; "
        f"{invocation}' slurm-protected-cancel {positional}"
    )


def _config_text() -> str:
    return """default_permissions = \"slurm-chat-guard\"
bypass_hook_trust = false

[features]
default_mode_request_user_input = true
hooks = true

[permissions.slurm-chat-guard]
extends = \":workspace\"

[permissions.slurm-chat-guard.filesystem.\":workspace_roots\"]
\".codex\" = \"deny\"
"""


def _rules_text(private_binder: Path) -> str:
    return "\n".join(
        [
            'prefix_rule(pattern=["scancel"], decision="forbidden")',
            'prefix_rule(pattern=["/usr/bin/scancel"], decision="forbidden")',
            f'prefix_rule(pattern=["{private_binder}"], decision="forbidden")',
            "",
        ]
    )


def _hooks_document(
    session_path: Path,
    session_digest: str,
    binder_path: Path,
    binder_digest: str,
) -> dict[str, Any]:
    session_command = _hash_checked_command("/usr/bin/python3", session_path, session_digest)
    binder_command = _hash_checked_command(None, binder_path, binder_digest)
    return {
        "hooks": {
            "SessionStart": [
                {
                    "matcher": "startup|resume|clear",
                    "hooks": [
                        {
                            "type": "command",
                            "command": session_command,
                            "timeout": 10,
                            "statusMessage": "Preparing protected-cancel session authority",
                        }
                    ],
                }
            ],
            "SessionEnd": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": session_command,
                            "timeout": 10,
                            "statusMessage": "Closing protected-cancel session authority",
                        }
                    ]
                }
            ],
            "PostToolUse": [
                {
                    "matcher": "^request_user_input$",
                    "hooks": [
                        {
                            "type": "command",
                            "command": binder_command,
                            "timeout": 15,
                            "statusMessage": "Verifying protected Slurm cancellation",
                        }
                    ],
                }
            ],
        }
    }


def _normalized_hook_hash(event_name: str, group: dict[str, Any], handler: dict[str, Any]) -> str:
    """Match Codex's normalized project-Hook currentHash identity."""

    timeout = int(handler.get("timeout", 600))
    if event_name == "SessionEnd":
        timeout = min(max(timeout, 1), 3)
    else:
        timeout = max(timeout, 1)
    normalized_handler: dict[str, Any] = {
        "type": "command",
        "command": handler["command"],
        "timeout": timeout,
        "async": bool(handler.get("async", False)),
    }
    if handler.get("statusMessage") is not None:
        normalized_handler["statusMessage"] = handler["statusMessage"]
    if handler.get("additionalContextLimit") not in (None, 2500):
        normalized_handler["additionalContextLimit"] = int(handler["additionalContextLimit"])
    identity: dict[str, Any] = {
        "event_name": HOOK_EVENT_KEYS[event_name],
        "hooks": [normalized_handler],
    }
    if group.get("matcher") is not None:
        identity["matcher"] = group["matcher"]
    serialized = json.dumps(identity, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return "sha256:" + _sha256_bytes(serialized)


def _hook_current_hashes(hooks_document: dict[str, Any]) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for event_name, groups in hooks_document["hooks"].items():
        event_key = HOOK_EVENT_KEYS[event_name]
        for group_index, group in enumerate(groups):
            for handler_index, handler in enumerate(group["hooks"]):
                hashes[f"{event_key}:{group_index}:{handler_index}"] = _normalized_hook_hash(
                    event_name,
                    group,
                    handler,
                )
    return hashes


def _shim_text(
    routing_helper: Path,
    site_id: str,
    local_override: Path,
    scontrol_path: Path,
    scancel_path: Path,
) -> str:
    values = [routing_helper, local_override, scontrol_path, scancel_path]
    if any("\n" in str(value) or "'" in str(value) for value in values) or "'" in site_id:
        raise ValueError("unsupported quote or newline in generated shim path")
    return f"""#!/usr/bin/bash
set -eu
exec /usr/bin/python3 '{routing_helper}' guard-cancel \\
  --site-id '{site_id}' \\
  --local-override '{local_override}' \\
  --scontrol '{scontrol_path}' \\
  --scancel '{scancel_path}' \\
  -- "$@"
"""


def render_contract(
    project_root: Path,
    skill_scripts: Path,
    scontrol: Path,
    scancel: Path,
    site_id: str,
    local_override: Path,
    protected_partitions: list[str],
) -> dict[str, Any]:
    project_root = project_root.expanduser().resolve()
    skill_scripts = skill_scripts.expanduser().resolve()
    scontrol = _absolute_executable(scontrol, project_root)
    scancel = _absolute_executable(scancel, project_root)
    binder_source, session_source = _read_sources(skill_scripts)
    binder_digest = _sha256_bytes(binder_source)
    session_digest = _sha256_bytes(session_source)
    private_binder = project_root / PRIVATE_REL / "bin/slurm-protected-cancel-binder"
    session_path = project_root / SESSION_REL
    routing_helper = skill_scripts / "slurm_routing.py"
    if not routing_helper.is_file():
        raise ValueError(f"missing routing helper: {routing_helper}")
    partitions = sorted({value.strip() for value in protected_partitions if value.strip()})
    if not partitions:
        raise ValueError("at least one protected cancellation partition is required")
    hooks = _hooks_document(session_path, session_digest, private_binder, binder_digest)
    runtime = {
        "schema_version": 1,
        "project_root": str(project_root),
        "binder_path": str(private_binder),
        "binder_sha256": binder_digest,
        "session_hook_path": str(session_path),
        "session_hook_sha256": session_digest,
        "scontrol_path": str(scontrol),
        "scancel_path": str(scancel),
        "site_id": site_id,
        "local_override": str(local_override.expanduser().resolve()),
        "protected_cancel_partitions": partitions,
        "operation": "ordinary_cancel",
        "active_session_id": None,
        "active_session_started_at": None,
    }
    files: dict[str, bytes] = {
        str(CONFIG_REL): _config_text().encode("utf-8"),
        str(HOOKS_REL): (json.dumps(hooks, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8"),
        str(RULES_REL): _rules_text(private_binder).encode("utf-8"),
        str(SESSION_REL): session_source,
        str(SHIM_REL): _shim_text(routing_helper, site_id, local_override, scontrol, scancel).encode("utf-8"),
        str(PRIVATE_REL / "bin/slurm-protected-cancel-binder"): binder_source,
        str(PRIVATE_REL / "runtime.json"): (json.dumps(runtime, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    }
    hooks_path = project_root / HOOKS_REL
    hook_keys = {
        "post_tool_use": f"{hooks_path}:post_tool_use:0:0",
        "session_end": f"{hooks_path}:session_end:0:0",
        "session_start": f"{hooks_path}:session_start:0:0",
    }
    hook_hashes_by_suffix = _hook_current_hashes(hooks)
    hook_current_hashes = {
        name: hook_hashes_by_suffix[f"{name}:0:0"]
        for name in hook_keys
    }
    manifest = {
        "schema_version": 1,
        "project_root": str(project_root),
        "binder_path": str(private_binder),
        "binder_sha256": binder_digest,
        "session_hook_path": str(session_path),
        "session_hook_sha256": session_digest,
        "scontrol_path": str(scontrol),
        "scancel_path": str(scancel),
        "protected_cancel_partitions": partitions,
        "hook_source_path": str(hooks_path),
        "hook_keys": hook_keys,
        "hook_current_hashes": hook_current_hashes,
        "file_sha256": {name: _sha256_bytes(content) for name, content in sorted(files.items())},
    }
    return {"files": files, "manifest": manifest}


def _write(path: Path, content: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        os.chmod(path, mode)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def write_rendered(rendered: dict[str, Any], destination: Path, *, install: bool) -> None:
    destination = destination.expanduser().resolve()
    executable = {str(SESSION_REL), str(SHIM_REL), str(PRIVATE_REL / "bin/slurm-protected-cancel-binder")}
    private_prefix = str(PRIVATE_REL) + "/"
    for relative, content in rendered["files"].items():
        target = destination / relative
        mode = 0o700 if relative in executable else 0o600 if relative.startswith(private_prefix) else 0o644
        _write(target, content, mode)
    if install:
        private_root = destination / PRIVATE_REL
        for directory in (private_root, private_root / "bin", private_root / "consumed", private_root / "audit"):
            directory.mkdir(parents=True, exist_ok=True)
            os.chmod(directory, 0o700)
    if not install:
        _write(
            destination / "protected-cancel-render-manifest.json",
            (json.dumps(rendered["manifest"], indent=2, sort_keys=True) + "\n").encode("utf-8"),
            0o644,
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--skill-scripts", type=Path, default=_source_dir())
    parser.add_argument("--scontrol", type=Path, required=True)
    parser.add_argument("--scancel", type=Path, required=True)
    parser.add_argument("--site-id", required=True)
    parser.add_argument("--local-override", type=Path, required=True)
    parser.add_argument("--protected-partition", action="append", required=True, dest="protected_partitions")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--install", action="store_true")
    mode.add_argument("--render-output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rendered = render_contract(
        args.project_root,
        args.skill_scripts,
        args.scontrol,
        args.scancel,
        args.site_id,
        args.local_override,
        args.protected_partitions,
    )
    destination = args.project_root if args.install else args.render_output
    assert destination is not None
    write_rendered(rendered, destination, install=args.install)
    print(json.dumps(rendered["manifest"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
