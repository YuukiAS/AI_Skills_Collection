#!/usr/bin/env python3
"""Render or install the project-local protected-cancel Host Hook contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
from typing import Any


PRIVATE_REL = Path(".codex/slurm-protected-cancel-private")
HOOK_REL = PRIVATE_REL / "slurm-cancel-hook"
HOOKS_REL = Path(".codex/hooks.json")
CONFIG_REL = Path(".codex/config.toml")
RULES_REL = Path(".codex/rules/slurm-protected-cancel.rules")
OBSOLETE_RELS = (
    Path(".codex/automation-bin/scancel"),
    Path(".codex/hooks/slurm-protected-cancel-session"),
    Path(".codex/hooks/session_start_probe.py"),
    PRIVATE_REL / "bin/slurm-protected-cancel-binder",
    PRIVATE_REL / "capability.key",
)

HOOK_EVENT_KEYS = {
    "PostToolUse": "post_tool_use",
    "PreToolUse": "pre_tool_use",
}


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _source_dir() -> Path:
    return Path(__file__).resolve().parent


def _executable_identity(path: Path, project_root: Path) -> tuple[Path, Path]:
    invocation = path.expanduser().absolute()
    resolved = invocation.resolve(strict=True)
    if not invocation.is_absolute() or not resolved.is_file() or not os.access(resolved, os.X_OK):
        raise ValueError(f"not an executable file: {path}")
    for candidate in (invocation, resolved):
        try:
            candidate.relative_to(project_root)
        except ValueError:
            continue
        raise ValueError(f"trusted executable must be outside project root: {candidate}")
    return invocation, resolved


def _hash_checked_command(script: Path, digest: str) -> str:
    positional = " ".join(shlex.quote(str(value)) for value in (script, digest))
    return (
        "/usr/bin/bash -c 'set -eu; target=$1; expected=$2; "
        "actual=$(/usr/bin/sha256sum -- \"$target\"); actual=${actual%% *}; "
        "[ \"$actual\" = \"$expected\" ] || exit 78; "
        "exec /usr/bin/python3 \"$target\"' slurm-protected-cancel "
        f"{positional}"
    )


def _config_text(scancel_paths: list[Path]) -> str:
    absolute_denies = "\n".join(
        f'{json.dumps(str(path))} = "deny"' for path in sorted(set(scancel_paths), key=str)
    )
    return f"""default_permissions = \"slurm-chat-guard\"
bypass_hook_trust = false

[features]
default_mode_request_user_input = true
hooks = true

[permissions.slurm-chat-guard]
extends = \":workspace\"

[permissions.slurm-chat-guard.filesystem]
{absolute_denies}

[permissions.slurm-chat-guard.filesystem.\":workspace_roots\"]
\".codex\" = \"deny\"
"""


def _rules_text(scancel_paths: list[Path], private_hook: Path) -> str:
    patterns = ["scancel", *[str(path) for path in sorted(set(scancel_paths), key=str)], str(private_hook)]
    return "\n".join(
        [f"prefix_rule(pattern=[{json.dumps(pattern)}], decision=\"forbidden\")" for pattern in patterns]
        + [""]
    )


def _hooks_document(
    hook_path: Path,
    hook_digest: str,
) -> dict[str, Any]:
    hook_command = _hash_checked_command(hook_path, hook_digest)
    return {
        "hooks": {
            "PreToolUse": [
                {
                    "matcher": "^(Bash|shell_command|exec_command)$",
                    "hooks": [
                        {
                            "type": "command",
                            "command": hook_command,
                            "timeout": 15,
                            "statusMessage": "Checking Slurm cancellation policy",
                        }
                    ],
                }
            ],
            "PostToolUse": [
                {
                    "matcher": "^request_user_input$",
                    "hooks": [
                        {
                            "type": "command",
                            "command": hook_command,
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

    timeout = max(int(handler.get("timeout", 600)), 1)
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


def render_contract(
    project_root: Path,
    skill_scripts: Path,
    scontrol: Path,
    scancel: Path,
    site_id: str,
    local_override: Path,
    protected_partitions: list[str],
    runtime_skill_scripts: Path | None = None,
) -> dict[str, Any]:
    project_root = project_root.expanduser().resolve()
    skill_scripts = skill_scripts.expanduser().resolve()
    del runtime_skill_scripts
    scontrol_invocation, scontrol_realpath = _executable_identity(scontrol, project_root)
    scancel_invocation, scancel_realpath = _executable_identity(scancel, project_root)
    hook_source = (skill_scripts / "slurm_cancel_hook.py").read_bytes()
    hook_digest = _sha256_bytes(hook_source)
    private_hook = project_root / HOOK_REL
    partitions = sorted({value.strip() for value in protected_partitions if value.strip()})
    if not partitions:
        raise ValueError("at least one protected cancellation partition is required")
    hooks = _hooks_document(private_hook, hook_digest)
    runtime = {
        "schema_version": 2,
        "project_root": str(project_root),
        "hook_path": str(private_hook),
        "hook_sha256": hook_digest,
        "scontrol_path": str(scontrol_realpath),
        "scontrol_path_realpath": str(scontrol_realpath),
        "scontrol_invocation_path": str(scontrol_invocation),
        "scancel_path": str(scancel_realpath),
        "scancel_path_realpath": str(scancel_realpath),
        "scancel_invocation_path": str(scancel_invocation),
        "site_id": site_id,
        "local_override": str(local_override.expanduser().resolve()),
        "protected_cancel_partitions": partitions,
        "operation": "ordinary_cancel",
    }
    scancel_paths = [scancel_invocation, scancel_realpath]
    files: dict[str, bytes] = {
        str(CONFIG_REL): _config_text(scancel_paths).encode("utf-8"),
        str(HOOKS_REL): (json.dumps(hooks, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8"),
        str(RULES_REL): _rules_text(scancel_paths, private_hook).encode("utf-8"),
        str(HOOK_REL): hook_source,
        str(PRIVATE_REL / "runtime.json"): (json.dumps(runtime, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    }
    hooks_path = project_root / HOOKS_REL
    hook_keys = {
        "post_tool_use": f"{hooks_path}:post_tool_use:0:0",
        "pre_tool_use": f"{hooks_path}:pre_tool_use:0:0",
    }
    hook_hashes_by_suffix = _hook_current_hashes(hooks)
    hook_current_hashes = {
        name: hook_hashes_by_suffix[f"{name}:0:0"]
        for name in hook_keys
    }
    manifest = {
        "schema_version": 2,
        "project_root": str(project_root),
        "hook_path": str(private_hook),
        "hook_sha256": hook_digest,
        "scontrol_path": str(scontrol_realpath),
        "scontrol_invocation_path": str(scontrol_invocation),
        "scancel_path": str(scancel_realpath),
        "scancel_invocation_path": str(scancel_invocation),
        "scancel_denied_paths": [str(path) for path in sorted(set(scancel_paths), key=str)],
        "protected_cancel_partitions": partitions,
        "hook_source_path": str(hooks_path),
        "hook_keys": hook_keys,
        "hook_current_hashes": hook_current_hashes,
        "file_sha256": {name: _sha256_bytes(content) for name, content in sorted(files.items())},
        "obsolete_paths_removed": [str(path) for path in OBSOLETE_RELS],
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


def _remove_obsolete(destination: Path) -> None:
    for relative in OBSOLETE_RELS:
        try:
            (destination / relative).unlink()
        except FileNotFoundError:
            pass
    for relative in (Path(".codex/automation-bin"), PRIVATE_REL / "bin"):
        shutil.rmtree(destination / relative, ignore_errors=True)
    hook_cache = destination / ".codex/hooks/__pycache__"
    for stale in hook_cache.glob("session_start_probe.*.pyc"):
        stale.unlink(missing_ok=True)
    try:
        hook_cache.rmdir()
    except OSError:
        pass


def write_rendered(rendered: dict[str, Any], destination: Path, *, install: bool) -> None:
    destination = destination.expanduser().resolve()
    _remove_obsolete(destination)
    private_prefix = str(PRIVATE_REL) + "/"
    for relative, content in rendered["files"].items():
        target = destination / relative
        mode = 0o700 if relative == str(HOOK_REL) else 0o600 if relative.startswith(private_prefix) else 0o644
        _write(target, content, mode)
    if install:
        private_root = destination / PRIVATE_REL
        for directory in (private_root, private_root / "consumed", private_root / "audit"):
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
    parser.add_argument(
        "--runtime-skill-scripts",
        type=Path,
        help=argparse.SUPPRESS,
    )
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
        args.runtime_skill_scripts,
    )
    destination = args.project_root if args.install else args.render_output
    assert destination is not None
    write_rendered(rendered, destination, install=args.install)
    print(json.dumps(rendered["manifest"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
