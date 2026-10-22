"""Default canonical candidate replay; no model selection or credential changes."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PUBLIC = HERE / "default-regression"
PRIVATE = ROOT / "private/exports/clear-writing--single-entry-artifact-finalization/v0.4/default-regression"
STATE = ROOT / ".local-runtime/candidate-plugin-replay/runs"
COMMIT = "157725b909775e169926c449844301e772e50f08"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def run(case, retry=False):
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    if branch != "design/clear-writing--single-entry-artifact-finalization":
        raise RuntimeError("checkout branch changed; no invocation permitted")
    previous = PRIVATE / case["case"] / "attempt-1"
    if retry:
        verdict = json.loads((previous / "RESULT.json").read_text())
        if verdict["product_messages"] or verdict["helper_exit"] == 0:
            raise RuntimeError("cannot retry a product response or successful run")
    evidence = PRIVATE / case["case"] / ("attempt-2" if retry else "attempt-1")
    evidence.mkdir(parents=True, exist_ok=False)
    command = [sys.executable, "scripts/candidate_plugin_replay.py", "replay", "--plugin", "writing-style",
               "--candidate-commit", COMMIT, "--task", case["task"]]
    for name in case["files"]:
        path = HERE / "model-regression/inputs" / name
        if sha(path) != case["hashes"][name]:
            raise RuntimeError("frozen input drift: " + name)
        command += ["--input", path.relative_to(ROOT).as_posix()]
    assert "--model" not in command and "--reasoning-effort" not in command
    write(evidence / "COMMAND.json", command)
    before = set(STATE.iterdir())
    with (evidence / "wrapper.stdout").open("w") as out, (evidence / "wrapper.stderr").open("w") as err:
        completed = subprocess.run(command, cwd=ROOT, stdout=out, stderr=err,
                                   env={**os.environ, "RUST_LOG": "off,codex_exec=info"})
    new = set(STATE.iterdir()) - before
    if len(new) != 1:
        raise RuntimeError("cannot identify exact child run directory: " + str(new))
    source = new.pop()
    shutil.copytree(source, evidence / "run")
    stdout = source / "child.stdout.jsonl"
    events = [json.loads(line) for line in stdout.read_text().splitlines() if line.strip()] if stdout.exists() else []
    messages = [e["item"]["text"] for e in events
                if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
    (evidence / "CHAT_FULL.md").write_text("\n\n".join(messages))
    log = (source / "child.stderr").read_text() if (source / "child.stderr").exists() else ""
    model = re.search(r'model: "([^"\n]+)"', log)
    effort = re.search(r'reasoning_effort: ([^,\n]+)', log)
    result = {"case": case["case"], "candidate_commit": COMMIT, "attempt": 2 if retry else 1,
              "helper_exit": completed.returncode, "product_messages": len(messages),
              "actual_model": model.group(1) if model else None,
              "actual_reasoning_effort": effort.group(1) if effort else None,
              "runtime_cli": "0.153.4", "explicit_model_arguments": False,
              "raw_evidence": evidence.relative_to(ROOT).as_posix(),
              "quality": "PENDING_FULL_ARTIFACT_REVIEW" if messages else "NO_PRODUCT_RESPONSE"}
    if completed.returncode == 0:
        result["receipt"] = json.loads((evidence / "wrapper.stdout").read_text())
    write(evidence / "RESULT.json", result)
    write(PUBLIC / "runs" / f"{case['case']}-attempt-{result['attempt']}.json", result)
    print(json.dumps({k: v for k, v in result.items() if k != "receipt"}), flush=True)
    if completed.returncode:
        raise SystemExit("Inspect retained infrastructure/consumption evidence before any one-time recovery.")


manifest = json.loads((HERE / "model-regression/INPUT_MANIFEST.json").read_text())
cases = manifest["cases"]
if sys.argv[1:] == ["--prepare"]:
    PUBLIC.mkdir(exist_ok=False)
    write(PUBLIC / "INPUT_MANIFEST.json", {
        "candidate_commit": COMMIT, "authority": "current user default-entry decision; v0.4 and 157725b9",
        "model_selection": "DEFAULT_NO_MODEL_OR_REASONING_ARGUMENTS",
        "runtime_cli": "0.153.4", "inputs": "../model-regression/inputs", "cases": cases,
        "policy": "first valid product answer; at most one same-default same-input infrastructure recovery"})
elif len(sys.argv) == 3 and sys.argv[1] == "--retry-infra":
    run(next(c for c in cases if c["case"] == sys.argv[2]), retry=True)
else:
    selected = cases if sys.argv[1:] == ["--remaining"] else [c for c in cases if c["case"] in sys.argv[1:]]
    for case in selected:
        if sys.argv[1:] == ["--remaining"] and (PRIVATE / case["case"]).exists():
            continue
        run(case)
