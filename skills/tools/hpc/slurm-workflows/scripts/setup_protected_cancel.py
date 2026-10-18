#!/usr/bin/env python3
"""Render or install the user-level protected-cancel Host Hook contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
from typing import Any


PRIVATE_DIR = "slurm-protected-cancel"
HOOKS_DIR = "hooks"
RUNTIME_NAME = "runtime.json"
POLICY_NAME = "policy.toml"
RULES_REL = Path("rules/slurm-protected-cancel.rules")
DECLARATION_START = "# ai-skills-slurm-protected-cancel:declarations:start"
DECLARATION_END = "# ai-skills-slurm-protected-cancel:declarations:end"
PERMISSIONS_START = "# ai-skills-slurm-protected-cancel:permissions:start"
PERMISSIONS_END = "# ai-skills-slurm-protected-cancel:permissions:end"
LEGACY_PROFILES = {"slurm-chat-guard", "slurm-protected-cancel-global"}
HOOK_EVENT_KEYS = {
    "PermissionRequest": "permission_request",
    "PostToolUse": "post_tool_use",
    "PreToolUse": "pre_tool_use",
}


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _source_dir() -> Path:
    return Path(__file__).resolve().parent


def _executable_identity(path: Path, codex_home: Path) -> tuple[Path, Path]:
    invocation = path.expanduser().absolute()
    resolved = invocation.resolve(strict=True)
    if not resolved.is_file() or not os.access(resolved, os.X_OK):
        raise ValueError(f"not an executable file: {path}")
    for candidate in (invocation, resolved):
        if candidate == codex_home or codex_home in candidate.parents:
            raise ValueError(f"trusted executable must be outside CODEX_HOME: {candidate}")
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


def _hooks_document(hook_path: Path, hook_digest: str) -> dict[str, Any]:
    command = _hash_checked_command(hook_path, hook_digest)
    return {
        "PreToolUse": [{
            "matcher": "^Bash$",
            "hooks": [{
                "type": "command",
                "command": command,
                "timeout": 15,
                "statusMessage": "Checking Slurm cancellation policy",
            }],
        }],
        "PermissionRequest": [{
            "matcher": "^Bash$",
            "hooks": [{
                "type": "command",
                "command": command,
                "timeout": 15,
                "statusMessage": "Enforcing protected Slurm cancellation",
            }],
        }],
        "PostToolUse": [{
            "matcher": "^request_user_input$",
            "hooks": [{
                "type": "command",
                "command": command,
                "timeout": 15,
                "statusMessage": "Verifying protected Slurm cancellation",
            }],
        }],
    }


def _toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _handler_toml(handler: dict[str, Any]) -> str:
    fields = [
        f"type = {_toml_string(handler['type'])}",
        f"command = {_toml_string(handler['command'])}",
        f"timeout = {int(handler['timeout'])}",
        f"statusMessage = {_toml_string(handler['statusMessage'])}",
    ]
    return "{ " + ", ".join(fields) + " }"


def _event_toml(groups: list[dict[str, Any]]) -> str:
    rendered = []
    for group in groups:
        handlers = ", ".join(_handler_toml(handler) for handler in group["hooks"])
        rendered.append(
            "{ matcher = " + _toml_string(group["matcher"]) + ", hooks = [" + handlers + "] }"
        )
    return "[" + ", ".join(rendered) + "]"


def _normalized_hook_hash(event_name: str, group: dict[str, Any], handler: dict[str, Any]) -> str:
    normalized_handler = {
        "type": "command",
        "command": handler["command"],
        "timeout": max(int(handler.get("timeout", 600)), 1),
        "async": bool(handler.get("async", False)),
    }
    if handler.get("statusMessage") is not None:
        normalized_handler["statusMessage"] = handler["statusMessage"]
    identity: dict[str, Any] = {
        "event_name": HOOK_EVENT_KEYS[event_name],
        "hooks": [normalized_handler],
        "matcher": group["matcher"],
    }
    encoded = json.dumps(identity, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()
    return "sha256:" + _sha256_bytes(encoded)


def _rules_text(scancel_paths: list[Path]) -> str:
    patterns = ["scancel", *[str(path) for path in sorted(set(scancel_paths), key=str)]]
    return "\n".join(
        [
            "prefix_rule("
            f"pattern=[{_toml_string(pattern)}], "
            'decision="prompt", '
            'justification="Slurm cancellation must pass the normal approval boundary."'
            ")"
            for pattern in patterns
        ]
        + [""]
    )


def _policy_text(protected_partitions: list[str]) -> bytes:
    values = ", ".join(_toml_string(value) for value in protected_partitions)
    return f"protected_cancel_partitions = [{values}]\n".encode()


def render_global_contract(
    codex_home: Path,
    skill_scripts: Path,
    scontrol: Path,
    scancel: Path,
    protected_partitions: list[str],
) -> dict[str, Any]:
    codex_home = codex_home.expanduser().resolve()
    skill_scripts = skill_scripts.expanduser().resolve()
    scontrol_invocation, scontrol_realpath = _executable_identity(scontrol, codex_home)
    scancel_invocation, scancel_realpath = _executable_identity(scancel, codex_home)
    hook_source = (skill_scripts / "slurm_cancel_hook.py").read_bytes()
    hook_digest = _sha256_bytes(hook_source)
    private_root = codex_home / PRIVATE_DIR
    hook_path = private_root / HOOKS_DIR / f"slurm-protected-cancel-{hook_digest}.py"
    policy_path = private_root / POLICY_NAME
    partitions = sorted({value.strip() for value in protected_partitions if value.strip()})
    if not partitions:
        raise ValueError("at least one protected cancellation partition is required")
    policy = _policy_text(partitions)
    hooks = _hooks_document(hook_path, hook_digest)
    runtime = {
        "schema_version": 4,
        "codex_home": str(codex_home),
        "hook_path": str(hook_path),
        "hook_sha256": hook_digest,
        "policy_path": str(policy_path),
        "policy_sha256": _sha256_bytes(policy),
        "scontrol_path": str(scontrol_realpath),
        "scontrol_path_realpath": str(scontrol_realpath),
        "scontrol_invocation_path": str(scontrol_invocation),
        "scancel_path": str(scancel_realpath),
        "scancel_path_realpath": str(scancel_realpath),
        "scancel_invocation_path": str(scancel_invocation),
        "operation": "ordinary_cancel",
    }
    files = {
        str(Path(PRIVATE_DIR) / HOOKS_DIR / hook_path.name): hook_source,
        f"{PRIVATE_DIR}/{POLICY_NAME}": policy,
        f"{PRIVATE_DIR}/{RUNTIME_NAME}": (json.dumps(runtime, indent=2, sort_keys=True) + "\n").encode(),
        str(RULES_REL): _rules_text([scancel_invocation, scancel_realpath]).encode(),
    }
    source_path = codex_home / "config.toml"
    hook_keys: dict[str, str] = {}
    hook_hashes: dict[str, str] = {}
    for event_name, groups in hooks.items():
        suffix = HOOK_EVENT_KEYS[event_name]
        hook_keys[suffix] = f"{source_path}:{suffix}:0:0"
        hook_hashes[suffix] = _normalized_hook_hash(event_name, groups[0], groups[0]["hooks"][0])
    return {
        "files": files,
        "hooks": hooks,
        "manifest": {
            "schema_version": 4,
            "codex_home": str(codex_home),
            "hook_path": str(hook_path),
            "hook_sha256": hook_digest,
            "policy_path": str(policy_path),
            "protected_cancel_partitions": partitions,
            "scontrol_path": str(scontrol_realpath),
            "scancel_path": str(scancel_realpath),
            "scancel_prompt_paths": [str(path) for path in sorted({scancel_invocation, scancel_realpath}, key=str)],
            "hook_source_path": str(source_path),
            "hook_keys": hook_keys,
            "hook_current_hashes": hook_hashes,
            "file_sha256": {name: _sha256_bytes(content) for name, content in sorted(files.items())},
        },
    }


def _strip_block(text: str, start: str, end: str) -> str:
    pattern = re.compile(rf"(?:^|\n){re.escape(start)}\n.*?\n{re.escape(end)}\n?", re.DOTALL)
    return pattern.sub("\n", text)


def _strip_permission_profile(text: str, profile: str) -> str:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    skipping = False
    header = re.compile(r"^\[permissions\.([^\.\]]+)(?:\.[^\]]+)?\]\s*$")
    for line in lines:
        table = header.match(line.strip())
        if table:
            skipping = table.group(1) == profile
        elif skipping and line.lstrip().startswith("["):
            skipping = False
        if not skipping:
            output.append(line)
    return "".join(output)


def update_user_config_text(original: str, rendered: dict[str, Any]) -> str:
    text = _strip_block(original, DECLARATION_START, DECLARATION_END)
    text = _strip_block(text, PERMISSIONS_START, PERMISSIONS_END)
    for profile in LEGACY_PROFILES:
        text = _strip_permission_profile(text, profile)
    text = re.sub(
        r'(?m)^default_permissions\s*=\s*["\'](?:slurm-chat-guard|slurm-protected-cancel-global)["\']\s*\n?',
        "",
        text,
    )

    hooks = rendered["hooks"]
    declarations = "\n".join([
        DECLARATION_START,
        f"hooks.PreToolUse = {_event_toml(hooks['PreToolUse'])}",
        f"hooks.PermissionRequest = {_event_toml(hooks['PermissionRequest'])}",
        f"hooks.PostToolUse = {_event_toml(hooks['PostToolUse'])}",
        DECLARATION_END,
        "",
    ])
    first_table = re.search(r"(?m)^\[", text)
    offset = first_table.start() if first_table else len(text)
    text = text[:offset].rstrip() + "\n\n" + declarations + text[offset:].lstrip()

    features = re.search(r"(?ms)^\[features\]\n(?P<body>.*?)(?=^\[|\Z)", text)
    if not features:
        raise ValueError("user config has no [features] table")
    body = features.group("body")
    if re.search(r"(?m)^default_mode_request_user_input\s*=", body):
        body = re.sub(
            r"(?m)^default_mode_request_user_input\s*=.*$",
            "default_mode_request_user_input = true",
            body,
        )
    else:
        body = "default_mode_request_user_input = true\n" + body
    if not re.search(r"(?m)^hooks\s*=", body):
        body += "hooks = true\n"
    text = text[: features.start("body")] + body + text[features.end("body") :]

    return text.rstrip() + "\n"


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
        temporary.unlink(missing_ok=True)


def write_rendered(rendered: dict[str, Any], destination: Path, *, install: bool) -> None:
    destination = destination.expanduser().resolve()
    for relative, content in rendered["files"].items():
        mode = 0o700 if Path(relative).name.startswith("slurm-protected-cancel-") else 0o600
        _write(destination / relative, content, mode)
    if install:
        private_root = destination / PRIVATE_DIR
        for directory in (
            private_root,
            private_root / HOOKS_DIR,
            private_root / "consumed",
            private_root / "audit",
        ):
            directory.mkdir(parents=True, exist_ok=True)
            os.chmod(directory, 0o700)
        stale_hooks = list(private_root.glob("slurm-hook-*.py"))
        stale_hooks.extend((private_root / HOOKS_DIR).glob("slurm-protected-cancel-*.py"))
        for stale in stale_hooks:
            if stale != Path(rendered["manifest"]["hook_path"]):
                stale.unlink()
        config_path = destination / "config.toml"
        updated = update_user_config_text(config_path.read_text(encoding="utf-8"), rendered)
        _write(config_path, updated.encode(), 0o600)
    else:
        config = update_user_config_text("[features]\ndefault_mode_request_user_input = false\n", rendered)
        _write(destination / "config.toml", config.encode(), 0o600)
        _write(
            destination / "protected-cancel-render-manifest.json",
            (json.dumps(rendered["manifest"], indent=2, sort_keys=True) + "\n").encode(),
            0o644,
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, required=True)
    parser.add_argument("--skill-scripts", type=Path, default=_source_dir())
    parser.add_argument("--scontrol", type=Path, required=True)
    parser.add_argument("--scancel", type=Path, required=True)
    parser.add_argument("--protected-partition", action="append", required=True, dest="protected_partitions")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--install", action="store_true")
    mode.add_argument("--render-output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    rendered = render_global_contract(
        args.codex_home,
        args.skill_scripts,
        args.scontrol,
        args.scancel,
        args.protected_partitions,
    )
    destination = args.codex_home if args.install else args.render_output
    assert destination is not None
    write_rendered(rendered, destination, install=args.install)
    print(json.dumps(rendered["manifest"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
