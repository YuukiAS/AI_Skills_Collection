"""Historical explicit-model diagnostic recorder; not the current closure entry."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PRIVATE = ROOT / "private/exports/clear-writing--single-entry-artifact-finalization/v0.4"
RUN = PRIVATE / "model-regression/DEV-ZH-DOCUMENT/FAILED_CHILD_RUN"
COMMIT = "2f35ce839a42f81f39cff55f577f44a10206e5a7"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


events = [json.loads(line) for line in (RUN / "child.stdout.jsonl").read_text().splitlines()]
stderr = (RUN / "child.stderr").read_text()
thread = next(e["thread_id"] for e in events if e["type"] == "thread.started")
assert thread in stderr
assert 'model: "gpt-6.1-sol"' in stderr
assert "reasoning_effort: Some(High)" in stderr
assert 'model_provider_id: "openai"' in stderr
assert any(e["type"] == "turn.failed" for e in events)
assert not any(e.get("item", {}).get("type") in {"agent_message", "command_execution"} for e in events)
assert not any((RUN / "workspace/outputs").iterdir())
after = json.loads((PRIVATE / "PLUGIN_LIST_AFTER_MODEL_FAILURE.json").read_text())
assert not any(p["pluginId"].endswith("@ai-skills-candidate") for p in after["installed"])
production = next(p for p in after["installed"] if p["pluginId"] == "writing-style@yuukias-ai-skills")
assert production["enabled"] and production["version"] == "0.5"
failure = "The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT account."
assert failure in (RUN / "child.stdout.jsonl").read_text()
preflight_path = HERE / "validation/CODEX_RUNTIME_PREFLIGHT.json"
preflight = json.loads(preflight_path.read_text())
preflight.update({
    "implementation_commit": COMMIT,
    "candidate_replay_helper_sha256": sha(ROOT / "scripts/candidate_plugin_replay.py"),
    "candidate_replay_model_override_supported": True,
    "new_candidate_model_requests_sent": 1,
    "pre_request_install_failures": 1,
    "pre_request_model_binding": "PROVEN_BY_REAL_CHILD_SESSION_CONFIGURED_EVENT",
    "configured_child_thread_id": thread,
    "configured_child_model": "gpt-6.1-sol",
    "configured_child_reasoning_effort": "high",
    "model_provider": "openai",
    "runtime_version": "codex-cli 0.153.4",
    "model_request_result": "HTTP_400_UNSUPPORTED_MODEL_FOR_CHATGPT_ACCOUNT",
    "model_request_error": failure,
    "product_responses": 0,
    "candidate_actual_skill_consumption": False,
    "candidate_removed_after_failure": True,
    "production_identity_after": {"plugin_id": production["pluginId"], "version": production["version"], "enabled": production["enabled"]},
    "full_raw_run": RUN.relative_to(ROOT).as_posix(),
    "raw_evidence": [{"path": (RUN / name).relative_to(ROOT).as_posix(), "sha256": sha(RUN / name)}
                     for name in ("child.stdout.jsonl", "child.stderr", "plugin-add.json")],
    "meaning": "Explicit configuration is proven in the real child; inference was rejected. No candidate product/quality PASS or formal Gate evidence.",
})
write(preflight_path, preflight)
manifest = json.loads((HERE / "model-regression/INPUT_MANIFEST.json").read_text())
write(HERE / "model-regression/RUNS.json", {
    "candidate_commit": COMMIT, "model": "gpt-6.1-sol", "reasoning_effort": "high",
    "formal_gates": "NOT_RUN", "product_responses": 0,
    "cases": [{"case": c["case"],
               "status": "INFRASTRUCTURE_FAILURE_HTTP400_NO_PRODUCT_RESPONSE" if c["case"] == "DEV-ZH-DOCUMENT" else "NOT_RUN",
               "quality": "NOT_ASSESSED_NO_PRODUCT_ARTIFACT" if c["case"] == "DEV-ZH-DOCUMENT" else "NOT_RUN"}
              for c in manifest["cases"]],
})
full = PRIVATE / "FULL_TESTS_MODEL_BINDING_STABLE.log"
assert re.search(r"Ran 392 tests in 208\.168s", full.read_text()) and "\nOK\n" in full.read_text()
write(HERE / "validation/MODEL_BINDING_TESTS.json", {
    "implementation_commit": COMMIT, "targeted_tests": {"passed": 33, "independent_review": True},
    "full_suite": {"passed": 392, "seconds": 208.168, "log": full.relative_to(ROOT).as_posix(), "sha256": sha(full),
                   "branch_stability": "HEAD was 2f35ce83 from 02:26:56 through log completion 02:30:43; next switch 02:35:08 -0400"},
    "source_generated_parity": "PASS: validate/check and skills validate",
    "wrapper_check": {"result": "PASS", "archive_sha256": "978b93115a0f66aab6f7a4cce2f590118ce2f0804d7113b02c3626c3b88cfc00"},
})
ci = json.loads((PRIVATE / "CI_MODEL_BINDING_CURRENT.json").read_text())
assert ci["headSha"] == COMMIT and ci["conclusion"] == "success"
write(HERE / "validation/GITHUB_CI_MODEL_BINDING.json", ci)
print("Recorded real model binding, HTTP400, zero product responses, cleanup, 392 tests and exact-code CI.")
