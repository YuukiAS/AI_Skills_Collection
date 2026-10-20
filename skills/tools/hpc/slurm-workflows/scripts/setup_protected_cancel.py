#!/usr/bin/env python3
"""Render or atomically install the portable protected-cancel Hook runtime."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import pwd
import re
import shlex
import shutil
import subprocess
import sys
import time
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple


PRIVATE_DIR = "slurm-protected-cancel"
HOOK_NAME = "slurm_cancel_hook.py"
SUPERVISOR_NAME = "slurm_cancel_supervisor.sh"
RUNTIME_NAME = "runtime.json"
POLICY_NAME = "policy.json"
MCP_NAME = "slurm_protected_cancel_mcp.py"
MCP_SERVER = "slurm-protected-cancel"
MCP_START = "# ai-skills-slurm-protected-cancel:mcp:start"
MCP_END = "# ai-skills-slurm-protected-cancel:mcp:end"
RULES_REL = Path("rules/slurm-protected-cancel.rules")
DECLARATION_START = "# ai-skills-slurm-protected-cancel:declarations:start"
DECLARATION_END = "# ai-skills-slurm-protected-cancel:declarations:end"
PERMISSIONS_START = "# ai-skills-slurm-protected-cancel:permissions:start"
PERMISSIONS_END = "# ai-skills-slurm-protected-cancel:permissions:end"
LEGACY_PROFILES = {"slurm-chat-guard", "slurm-protected-cancel-global"}
HOOK_EVENT_KEYS = {"PermissionRequest": "permission_request", "PostToolUse": "post_tool_use", "PreToolUse": "pre_tool_use"}
LOADER_ENV_KEYS = {"LD_LIBRARY_PATH", "LIBPATH", "DYLD_LIBRARY_PATH"}


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _source_dir() -> Path:
    return Path(__file__).resolve().parent


def _executable_identity(path: Path, codex_home: Path) -> Tuple[Path, Path]:
    invocation = path.expanduser().absolute()
    resolved = invocation.resolve(strict=True)
    if not resolved.is_file() or not os.access(str(resolved), os.X_OK):
        raise ValueError("not an executable file: {}".format(path))
    for candidate in (invocation, resolved):
        if candidate == codex_home or codex_home in candidate.parents:
            raise ValueError("trusted executable must be outside CODEX_HOME: {}".format(candidate))
    return invocation, resolved


def _system_executable(name: str, codex_home: Path) -> Path:
    for directory in (Path("/usr/bin"), Path("/bin"), Path("/usr/local/bin")):
        candidate = directory / name
        try:
            _, resolved = _executable_identity(candidate, codex_home)
        except (OSError, ValueError):
            continue
        return resolved
    raise ValueError("required system executable unavailable: {}".format(name))


def _runtime_environment(loader_env: Mapping[str, str]) -> Dict[str, str]:
    user = pwd.getpwuid(os.geteuid()).pw_name
    environment = {
        "HOME": str(Path.home()), "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
        "LOGNAME": user, "PATH": "/usr/bin:/bin", "USER": user,
    }
    for key, value in loader_env.items():
        if key not in LOADER_ENV_KEYS:
            raise ValueError("unsupported runtime environment key: {}".format(key))
        if not value or "\x00" in value or "\n" in value:
            raise ValueError("invalid runtime environment value: {}".format(key))
        environment[key] = value
    return environment


def _parse_runtime_env(values: Iterable[str]) -> Dict[str, str]:
    parsed = {}
    for value in values:
        key, separator, setting = value.partition("=")
        if not separator:
            raise ValueError("--runtime-env must use KEY=VALUE")
        if key in parsed:
            raise ValueError("duplicate runtime environment key: {}".format(key))
        parsed[key] = setting
    return parsed


def _python_candidates(explicit: Optional[Path]) -> List[Path]:
    if explicit is not None:
        return [explicit]
    candidates = [Path("/usr/bin/python3"), Path("/usr/local/bin/python3")]
    for directory in os.environ.get("PATH", "").split(os.pathsep):
        if directory:
            candidates.append(Path(directory) / "python3")
    candidates.append(Path(sys.executable))
    unique = []
    seen = set()
    for candidate in candidates:
        identity = str(candidate.expanduser().absolute())
        if identity not in seen:
            seen.add(identity)
            unique.append(candidate)
    return unique


def _qualify_python(codex_home: Path, explicit: Optional[Path], environment: Mapping[str, str]) -> Path:
    diagnostics = []
    probe = (
        "import hashlib,json,os,pathlib,pwd,re,shlex,stat,subprocess,sys;"
        "assert sys.version_info[:2]>=(3,9);print('%d.%d'%sys.version_info[:2])"
    )
    for candidate in _python_candidates(explicit):
        try:
            _, resolved = _executable_identity(candidate, codex_home)
            completed = subprocess.run(
                [str(resolved), "-I", "-c", probe], check=False, capture_output=True,
                text=True, timeout=5, env=dict(environment),
            )
        except (OSError, subprocess.TimeoutExpired, ValueError) as error:
            diagnostics.append("{}:{}".format(candidate, type(error).__name__))
            continue
        if completed.returncode == 0 and completed.stdout.strip():
            return resolved
        diagnostics.append("{}:rc{}".format(candidate, completed.returncode))
    raise ValueError("no qualified Python 3.9+ runtime in sanitized environment ({})".format(", ".join(diagnostics)))


def _fallback_json(event_name: str, reason: str = "hook_runtime_failure") -> str:
    if event_name == "PreToolUse":
        value = {"hookSpecificOutput": {"hookEventName": event_name, "permissionDecision": "deny", "permissionDecisionReason": "SLURM_CANCEL_DENIED reason={}".format(reason)}}
    elif event_name == "PermissionRequest":
        value = {"hookSpecificOutput": {"hookEventName": event_name, "decision": {"behavior": "deny", "message": "SLURM_CANCEL_DENIED reason={}".format(reason)}}}
    else:
        value = {"protected_cancel": "denied", "reason": reason}
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def _supervisor_text(
    python_path: Path,
    hook_digest: str,
    runtime_digest: str,
    policy_digest: str,
    environment: Mapping[str, str],
    tools: Mapping[str, Path],
) -> bytes:
    env_words = " ".join(shlex.quote("{}={}".format(key, value)) for key, value in sorted(environment.items()))
    validator = r'''import json,sys
event=sys.argv[1]
try: value=json.load(open(sys.argv[2],encoding="utf-8"))
except Exception: raise SystemExit(2)
if not isinstance(value,dict): raise SystemExit(3)
if event in ("PreToolUse","PermissionRequest"):
    if value == {}: raise SystemExit(0)
    output=value.get("hookSpecificOutput")
    if not isinstance(output,dict) or output.get("hookEventName") != event: raise SystemExit(4)
    if event == "PreToolUse":
        if output.get("permissionDecision") != "deny" or not isinstance(output.get("permissionDecisionReason"),str): raise SystemExit(5)
    else:
        decision=output.get("decision")
        if not isinstance(decision,dict) or decision.get("behavior") != "deny" or not isinstance(decision.get("message"),str): raise SystemExit(6)
else:
    if value.get("protected_cancel") not in ("ignored","denied","retained","executed","ambiguous"): raise SystemExit(7)
    if value.get("protected_cancel") == "retained" and (type(value.get("mutation_count")) is not int or value["mutation_count"] != 0): raise SystemExit(7)
'''
    lines = [
        "#!/usr/bin/bash", "set -u", "umask 077", "EVENT=${1-}",
        "ROOT=$(CDPATH= cd -- \"$(dirname -- \"$0\")\" && pwd -P) || exit 90",
        "HOOK=$ROOT/{}".format(HOOK_NAME), "RUNTIME=$ROOT/{}".format(RUNTIME_NAME), "POLICY=$ROOT/{}".format(POLICY_NAME),
        "PYTHON={}".format(shlex.quote(str(python_path))), "SHA256={}".format(shlex.quote(str(tools["sha256sum"]))),
        "TIMEOUT={}".format(shlex.quote(str(tools["timeout"]))), "ENV={}".format(shlex.quote(str(tools["env"]))),
        "OUT=$ROOT/.hook-output.$$", "ERR=$ROOT/.hook-error.$$",
        "cleanup() { rm -f -- \"$OUT\" \"$ERR\"; }", "trap cleanup EXIT HUP INT TERM",
        "fallback() {", "  case \"$EVENT\" in",
        "    PreToolUse) printf '%s\\n' {} ;;".format(shlex.quote(_fallback_json("PreToolUse"))),
        "    PermissionRequest) printf '%s\\n' {} ;;".format(shlex.quote(_fallback_json("PermissionRequest"))),
        "    PostToolUse) printf '%s\\n' {} ;;".format(shlex.quote(_fallback_json("PostToolUse"))),
        "    *) printf '%s\\n' {} ;;".format(shlex.quote(_fallback_json("PostToolUse", "unknown_hook_event"))),
        "  esac", "}",
        "case \"$EVENT\" in PreToolUse|PermissionRequest|PostToolUse) ;; *) fallback; exit 0 ;; esac",
        "digest() { \"$SHA256\" -- \"$1\" 2>/dev/null | { read -r value rest; printf '%s' \"$value\"; }; }",
        "[ \"$(digest \"$HOOK\")\" = {} ] || {{ fallback; exit 0; }}".format(shlex.quote(hook_digest)),
        "[ \"$(digest \"$RUNTIME\")\" = {} ] || {{ fallback; exit 0; }}".format(shlex.quote(runtime_digest)),
        "[ \"$(digest \"$POLICY\")\" = {} ] || {{ fallback; exit 0; }}".format(shlex.quote(policy_digest)),
        "\"$TIMEOUT\" --signal=TERM --kill-after=1 8 \"$ENV\" -i {} \"$PYTHON\" -I \"$HOOK\" >\"$OUT\" 2>\"$ERR\"".format(env_words),
        "status=$?", "if [ \"$status\" -ne 0 ]; then fallback; exit 0; fi",
        "\"$TIMEOUT\" --signal=TERM --kill-after=1 2 \"$ENV\" -i {} \"$PYTHON\" -I -c {} \"$EVENT\" \"$OUT\" >/dev/null 2>&1".format(env_words, shlex.quote(validator)),
        "status=$?", "if [ \"$status\" -ne 0 ]; then fallback; exit 0; fi",
        "{} -- \"$OUT\"".format(shlex.quote(str(tools["cat"]))), "exit 0", "",
    ]
    return "\n".join(lines).encode("utf-8")


def _declaration_command(supervisor: Path, digest: str, event_name: str, bash: Path, sha256sum: Path) -> str:
    program = (
        "set -u; supervisor=$1; expected=$2; event=$3; "
        "actual=$($4 -- \"$supervisor\" 2>/dev/null); actual=${actual%% *}; "
        "if [ \"$actual\" = \"$expected\" ] && \"$supervisor\" \"$event\"; then exit 0; fi; "
        "printf '%s\\n' \"$5\"; exit 0"
    )
    values = ["slurm-protected-cancel", str(supervisor), digest, event_name, str(sha256sum), _fallback_json(event_name)]
    return "{} -c {} {}".format(shlex.quote(str(bash)), shlex.quote(program), " ".join(shlex.quote(value) for value in values))


def _hooks_document(supervisor: Path, digest: str, tools: Mapping[str, Path]) -> Dict[str, Any]:
    result = {}
    matchers = {"PreToolUse": "^Bash$", "PermissionRequest": "^Bash$", "PostToolUse": "^request_user_input$"}
    messages = {"PreToolUse": "Checking Slurm cancellation policy", "PermissionRequest": "Enforcing protected Slurm cancellation", "PostToolUse": "Verifying protected Slurm cancellation"}
    for event_name in ("PreToolUse", "PermissionRequest", "PostToolUse"):
        result[event_name] = [{"matcher": matchers[event_name], "hooks": [{
            "type": "command", "command": _declaration_command(supervisor, digest, event_name, tools["bash"], tools["sha256sum"]),
            "timeout": 15, "statusMessage": messages[event_name],
        }]}]
    return result


def _toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _handler_toml(handler: Mapping[str, Any]) -> str:
    if handler["type"] == "mcp_tool":
        def value_toml(value):
            if isinstance(value, dict):
                return "{ " + ", ".join(_toml_string(key) + " = " + value_toml(item) for key, item in value.items()) + " }"
            if isinstance(value, str):
                return _toml_string(value)
            return str(value)
        return value_toml(handler)
    fields = ["type = {}".format(_toml_string(str(handler["type"]))), "command = {}".format(_toml_string(str(handler["command"]))), "timeout = {}".format(int(handler["timeout"])), "statusMessage = {}".format(_toml_string(str(handler["statusMessage"])))]
    return "{ " + ", ".join(fields) + " }"


def _event_toml(groups: List[Dict[str, Any]]) -> str:
    rendered = []
    for group in groups:
        handlers = ", ".join(_handler_toml(handler) for handler in group["hooks"])
        rendered.append("{ matcher = " + _toml_string(group["matcher"]) + ", hooks = [" + handlers + "] }")
    return "[" + ", ".join(rendered) + "]"


def _normalized_hook_hash(event_name: str, group: Mapping[str, Any], handler: Mapping[str, Any]) -> str:
    normalized_handler = {"type": "command", "command": handler["command"], "timeout": max(int(handler.get("timeout", 600)), 1), "async": bool(handler.get("async", False))}
    if handler.get("statusMessage") is not None:
        normalized_handler["statusMessage"] = handler["statusMessage"]
    identity = {"event_name": HOOK_EVENT_KEYS[event_name], "hooks": [normalized_handler], "matcher": group["matcher"]}
    encoded = json.dumps(identity, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return "sha256:" + _sha256_bytes(encoded)


def _rules_text(scancel_paths: List[Path]) -> str:
    patterns = ["scancel"] + [str(path) for path in sorted(set(scancel_paths), key=str)]
    return "\n".join(["prefix_rule(pattern=[{}], decision=\"prompt\", justification=\"Slurm cancellation must pass the normal approval boundary.\")".format(_toml_string(pattern)) for pattern in patterns] + [""])


def render_global_contract(
    codex_home: Path, skill_scripts: Path, scontrol: Path, scancel: Path,
    protected_partitions: List[str], hook_python: Optional[Path] = None,
    runtime_env: Optional[Mapping[str, str]] = None,
    mcp_python: Optional[Path] = None,
    mcp_runtime_env: Optional[Mapping[str, str]] = None,
) -> Dict[str, Any]:
    codex_home = codex_home.expanduser().resolve()
    skill_scripts = skill_scripts.expanduser().resolve()
    scontrol_invocation, scontrol_realpath = _executable_identity(scontrol, codex_home)
    scancel_invocation, scancel_realpath = _executable_identity(scancel, codex_home)
    environment = _runtime_environment(runtime_env or {})
    python_path = _qualify_python(codex_home, hook_python, environment)
    tools = {name: _system_executable(name, codex_home) for name in ("bash", "cat", "env", "sha256sum", "timeout")}
    hook_source = (skill_scripts / HOOK_NAME).read_bytes()
    partitions = sorted({value.strip() for value in protected_partitions if value.strip()})
    if not partitions:
        raise ValueError("at least one protected cancellation partition is required")
    policy = (json.dumps({"protected_cancel_partitions": partitions}, indent=2, sort_keys=True) + "\n").encode("utf-8")
    runtime = {
        "schema_version": 5, "environment": environment, "hook_file": HOOK_NAME,
        "hook_sha256": _sha256_bytes(hook_source), "operation": "ordinary_cancel",
        "policy_file": POLICY_NAME, "policy_sha256": _sha256_bytes(policy), "python_path": str(python_path),
        "scancel_invocation_path": str(scancel_invocation), "scancel_path": str(scancel_realpath), "scancel_path_realpath": str(scancel_realpath),
        "scontrol_invocation_path": str(scontrol_invocation), "scontrol_path": str(scontrol_realpath), "scontrol_path_realpath": str(scontrol_realpath),
    }
    runtime_bytes = (json.dumps(runtime, indent=2, sort_keys=True) + "\n").encode("utf-8")
    supervisor = _supervisor_text(python_path, runtime["hook_sha256"], _sha256_bytes(runtime_bytes), runtime["policy_sha256"], environment, tools)
    supervisor_digest = _sha256_bytes(supervisor)
    private_root = codex_home / PRIVATE_DIR
    supervisor_path = private_root / SUPERVISOR_NAME
    hooks = _hooks_document(supervisor_path, supervisor_digest, tools)
    files = {
        str(Path(PRIVATE_DIR) / HOOK_NAME): hook_source,
        str(Path(PRIVATE_DIR) / SUPERVISOR_NAME): supervisor,
        str(Path(PRIVATE_DIR) / RUNTIME_NAME): runtime_bytes,
        str(Path(PRIVATE_DIR) / POLICY_NAME): policy,
        str(RULES_REL): _rules_text([scancel_invocation, scancel_realpath]).encode("utf-8"),
    }
    mcp_config = None
    if mcp_python is not None:
        invocation, _ = _executable_identity(mcp_python, codex_home)
        mcp_environment = _runtime_environment(mcp_runtime_env or {})
        qualified = subprocess.run(
            [str(invocation), "-I", "-c", "import importlib.metadata;from mcp.server import Server;from mcp.server.session import ServerSession;assert hasattr(ServerSession,'elicit_form');print(importlib.metadata.version('mcp'))"],
            capture_output=True, text=True, check=False, timeout=15, env=mcp_environment,
        )
        if qualified.returncode != 0 or qualified.stdout.strip() != "1.30.0":
            raise ValueError("MCP SDK 1.30.0 runtime qualification failed")
        mcp_source = (skill_scripts / MCP_NAME).read_bytes()
        mcp_digest = _sha256_bytes(mcp_source)
        files[str(Path(PRIVATE_DIR) / MCP_NAME)] = mcp_source
        files[str(Path(PRIVATE_DIR) / "mcp_identity.json")] = (json.dumps({"server_sha256": mcp_digest, "sdk_version": "1.30.0"}, sort_keys=True) + "\n").encode()
        fields = ("session_id", "turn_id", "tool_use_id", "tool_name", "tool_input", "cwd", "hook_event_name", "agent_id", "agent_type")
        hooks["PreToolUse"][0]["hooks"].append({
            "type": "mcp_tool", "server": MCP_SERVER, "tool": "slurm_protected_cancel", "timeout": 900,
            "statusMessage": "Confirm protected Slurm cancellation",
            "input": {"event": {key: "${" + key + "}" for key in fields}, "server_sha256": mcp_digest},
        })
        # Latest user authority (attachment section 4, line 247) explicitly
        # retires THIS product's request_user_input binder. This dictionary
        # contains only handlers rendered by _hooks_document above, never the
        # user's other Hook declarations. Their bytes and trust stay outside
        # the owned declaration markers and are not edited.
        del hooks["PostToolUse"]
        mcp_config = {
            "command": str(tools["env"]),
            "args": ["-i"] + [key + "=" + value for key, value in sorted(mcp_environment.items())]
                    + [str(invocation), "-I", "-B", str(private_root / MCP_NAME)],
            "startup_timeout_sec": 20, "tool_timeout_sec": 900,
        }
    source_path = codex_home / "config.toml"
    hook_keys = {}
    hook_hashes = {}
    for event_name, groups in hooks.items():
        suffix = HOOK_EVENT_KEYS[event_name]
        hook_keys[suffix] = "{}:{}:0:0".format(source_path, suffix)
        hook_hashes[suffix] = _normalized_hook_hash(event_name, groups[0], groups[0]["hooks"][0])
    return {"files": files, "hooks": hooks, "mcp_config": mcp_config, "manifest": {
        "schema_version": 5, "codex_home": str(codex_home), "hook_sha256": runtime["hook_sha256"],
        "fresh_session_required": not bool(mcp_config),
        "client_reload_required": bool(mcp_config),
        "next_action": ("Review only the new MCP Hook in the native Hooks interface, apply the supported client reload, and verify actual current-chat Hook/elicitation events before cancellation." if mcp_config else "After installation and any required Hook trust, start a fresh Codex/Desktop thread and verify its actual Hook events before cancellation. hooks/list alone does not prove an existing session reloaded its Hooks."),
        "policy_sha256": runtime["policy_sha256"], "python_path": str(python_path), "protected_cancel_partitions": partitions,
        "runtime_environment_keys": sorted(environment), "scancel_path": str(scancel_realpath), "scontrol_path": str(scontrol_realpath),
        "supervisor_path": str(supervisor_path), "supervisor_sha256": supervisor_digest, "hook_source_path": str(source_path),
        "hook_keys": hook_keys, "hook_current_hashes": hook_hashes,
        "confirmation_transport": "mcp_elicitation" if mcp_config else "legacy_fixture",
        "mcp_server": MCP_SERVER if mcp_config else None,
        "file_sha256": {name: _sha256_bytes(content) for name, content in sorted(files.items())},
    }}


def _strip_block(text: str, start: str, end: str) -> str:
    pattern = re.compile(
        r"(?ms)^{}\n.*?^{}(?:\n|\Z)".format(re.escape(start), re.escape(end))
    )
    return pattern.sub("", text)


def _take_hook_state(text: str) -> Tuple[str, str]:
    lines = text.splitlines(keepends=True)
    start = next((index for index, line in enumerate(lines) if line.strip() == "[hooks.state]"), None)
    if start is None:
        return text, ""
    end = start + 1
    while end < len(lines):
        stripped = lines[end].strip()
        if stripped == DECLARATION_END or (stripped.startswith("[") and not stripped.startswith("[hooks.state")):
            break
        end += 1
    return "".join(lines[:start] + lines[end:]), "".join(lines[start:end]).strip()


def _strip_permission_profile(text: str, profile: str) -> str:
    lines = text.splitlines(keepends=True)
    output = []
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


def update_user_config_text(original: str, rendered: Mapping[str, Any]) -> str:
    hooks = rendered["hooks"]
    declarations = "\n".join([
        DECLARATION_START, "hooks.PreToolUse = {}".format(_event_toml(hooks["PreToolUse"])),
        "hooks.PermissionRequest = {}".format(_event_toml(hooks["PermissionRequest"])),
        *(["hooks.PostToolUse = {}".format(_event_toml(hooks["PostToolUse"]))] if "PostToolUse" in hooks else []), DECLARATION_END, "",
    ])
    pattern = re.compile(
        r"(?ms)^{}\n.*?^{}(?:\n|\Z)".format(
            re.escape(DECLARATION_START), re.escape(DECLARATION_END)
        )
    )
    existing = pattern.search(original)
    if existing:
        text = original[:existing.start()] + declarations + original[existing.end():]
    else:
        first_table = re.search(r"(?m)^\[", original)
        offset = first_table.start() if first_table else len(original)
        prefix = original[:offset]
        separator = "" if not prefix or prefix.endswith("\n") else "\n"
        text = prefix + separator + declarations + original[offset:]
    features = re.search(r"(?ms)^\[features\]\n(?P<body>.*?)(?=^\[|\Z)", text)
    if not features:
        raise ValueError("user config has no [features] table")
    body = features.group("body")
    if not rendered.get("mcp_config") and not re.search(r"(?m)^default_mode_request_user_input\s*=\s*true\s*$", body):
        raise ValueError("default_mode_request_user_input must already be true")
    if not re.search(r"(?m)^hooks\s*=\s*true\s*$", body):
        raise ValueError("hooks feature must already be true")
    if rendered.get("mcp_config"):
        text = _strip_block(text, MCP_START, MCP_END)
        if re.search(r'(?m)^\[mcp_servers\.(?:"slurm-protected-cancel"|slurm-protected-cancel)\]', text):
            raise ValueError("unowned protected-cancel MCP server declaration")
        mcp = rendered["mcp_config"]
        text += ("" if text.endswith("\n") else "\n") + "\n".join([
            MCP_START, '[mcp_servers."' + MCP_SERVER + '"]',
            "command = " + _toml_string(mcp["command"]),
            "args = [" + ", ".join(_toml_string(item) for item in mcp["args"]) + "]",
            "startup_timeout_sec = 20", "tool_timeout_sec = 900", MCP_END, "",
        ])
    return text


def _write(path: Path, content: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(".{}.{}.tmp".format(path.name, os.getpid()))
    descriptor = os.open(str(temporary), os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(content); stream.flush(); os.fsync(stream.fileno())
        os.replace(str(temporary), str(path)); os.chmod(str(path), mode)
    finally:
        try: temporary.unlink()
        except FileNotFoundError: pass


def _write_private_files(rendered: Mapping[str, Any], destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True, mode=0o700); os.chmod(str(destination), 0o700)
    prefix = PRIVATE_DIR + "/"
    for relative, content in rendered["files"].items():
        if relative.startswith(prefix):
            name = relative[len(prefix):]
            _write(destination / name, content, 0o700 if name == SUPERVISOR_NAME else 0o600)
    for name in ("consumed", "audit", "backups"):
        path = destination / name; path.mkdir(mode=0o700, exist_ok=True); os.chmod(str(path), 0o700)


def _copy_one_time_state(source: Path, destination: Path) -> None:
    for directory in ("consumed", "audit"):
        source_dir = source / directory
        destination_dir = destination / directory
        if not source_dir.is_dir() or source_dir.is_symlink():
            continue
        for item in source_dir.iterdir():
            if item.is_symlink() or not item.is_file() or item.suffix != ".json":
                continue
            target = destination_dir / item.name
            if target.exists():
                raise ValueError("duplicate protected-cancel state: {}".format(item.name))
            _write(target, item.read_bytes(), 0o600)


def _qualify_staged_contract(rendered: Mapping[str, Any], staged_private: Path) -> None:
    event = {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": "printf protected-cancel-runtime-probe"}, "cwd": str(staged_private), "session_id": "install-probe", "turn_id": "install-probe", "tool_use_id": "install-probe"}
    completed = subprocess.run([str(staged_private / SUPERVISOR_NAME), "PreToolUse"], input=json.dumps(event), check=False, capture_output=True, text=True, timeout=12)
    try: payload = json.loads(completed.stdout)
    except json.JSONDecodeError as error: raise ValueError("staged supervisor returned invalid JSON") from error
    if completed.returncode != 0 or payload != {}:
        raise ValueError("staged candidate qualification failed: rc={} payload={!r}".format(completed.returncode, payload))
    if rendered.get("mcp_config"):
        mcp = rendered["mcp_config"]
        args = list(mcp["args"])
        args[-1] = str(staged_private / MCP_NAME)
        completed = subprocess.run([mcp["command"], *args, "--check"], capture_output=True, text=True, check=False, timeout=20)
        if completed.returncode != 0:
            raise ValueError("staged MCP runtime qualification failed")
        identity = json.loads(completed.stdout)
        if identity.get("server_sha256") != _sha256_bytes(rendered["files"][str(Path(PRIVATE_DIR) / MCP_NAME)]):
            raise ValueError("staged MCP server identity mismatch")


def write_rendered(rendered: Mapping[str, Any], destination: Path, install: bool = False) -> None:
    destination = destination.expanduser().resolve()
    if not install:
        for relative, content in rendered["files"].items():
            _write(destination / relative, content, 0o700 if Path(relative).name == SUPERVISOR_NAME else 0o600)
        config = update_user_config_text("[features]\ndefault_mode_request_user_input = true\nhooks = true\n", rendered)
        _write(destination / "config.toml", config.encode("utf-8"), 0o600)
        _write(destination / "protected-cancel-render-manifest.json", (json.dumps(rendered["manifest"], indent=2, sort_keys=True) + "\n").encode("utf-8"), 0o644)
        return
    config_path = destination / "config.toml"
    original_config = config_path.read_bytes()
    updated_config = update_user_config_text(original_config.decode("utf-8"), rendered).encode("utf-8")
    final_private = destination / PRIVATE_DIR
    stage = destination / ".{}-stage-{}".format(PRIVATE_DIR, os.getpid())
    rollback = destination / ".{}-rollback-{}".format(PRIVATE_DIR, os.getpid())
    if stage.exists() or rollback.exists(): raise ValueError("stale protected-cancel activation path exists")
    try:
        _write_private_files(rendered, stage)
        backup = stage / "backups" / "pre-v3-{}".format(time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))
        backup.mkdir(mode=0o700)
        _write(backup / "config.toml", original_config, 0o600)
        if final_private.exists():
            shutil.copytree(str(final_private), str(backup / "private"), symlinks=True)
            _copy_one_time_state(final_private, stage)
        _qualify_staged_contract(rendered, stage)
        if final_private.exists(): os.replace(str(final_private), str(rollback))
        os.replace(str(stage), str(final_private))
        try:
            _write(config_path, updated_config, 0o600)
        except Exception:
            if final_private.exists(): shutil.rmtree(str(final_private))
            if rollback.exists(): os.replace(str(rollback), str(final_private))
            _write(config_path, original_config, 0o600)
            raise
        if rollback.exists(): shutil.rmtree(str(rollback))
    except Exception:
        if rollback.exists() and not final_private.exists():
            os.replace(str(rollback), str(final_private))
        raise
    finally:
        if stage.exists(): shutil.rmtree(str(stage))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, required=True)
    parser.add_argument("--skill-scripts", type=Path, default=_source_dir())
    parser.add_argument("--scontrol", type=Path, required=True)
    parser.add_argument("--scancel", type=Path, required=True)
    parser.add_argument("--protected-partition", action="append", required=True, dest="protected_partitions")
    parser.add_argument("--hook-python", type=Path)
    parser.add_argument("--mcp-python", type=Path)
    parser.add_argument("--mcp-runtime-env", action="append", default=[])
    parser.add_argument("--runtime-env", action="append", default=[])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--install", action="store_true")
    mode.add_argument("--render-output", type=Path)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.install and args.mcp_python is None:
        raise ValueError("production installation requires --mcp-python with qualified MCP SDK 1.30.0")
    rendered = render_global_contract(args.codex_home, args.skill_scripts, args.scontrol, args.scancel, args.protected_partitions, hook_python=args.hook_python, runtime_env=_parse_runtime_env(args.runtime_env), mcp_python=args.mcp_python, mcp_runtime_env=_parse_runtime_env(args.mcp_runtime_env))
    destination = args.codex_home if args.install else args.render_output
    assert destination is not None
    write_rendered(rendered, destination, install=args.install)
    print(json.dumps(rendered["manifest"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
