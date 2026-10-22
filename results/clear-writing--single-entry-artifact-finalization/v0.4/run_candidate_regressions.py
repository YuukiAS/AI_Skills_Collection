"""Historical explicit-model diagnostic only; superseded by run_default_regressions.py.

Retained to explain the pre-product HTTP400 record. Do not invoke this script
under the current default-entry authority. Original public input bytes remain
available to the default replay script without model-selection behavior.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
TASK = "clear-writing--single-entry-artifact-finalization"
PRIVATE = ROOT / "private/exports" / TASK / "v0.4/model-regression"
OLD = HERE.parent / "known-regression/fixtures"
COMMIT = "2f35ce83"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def show(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT).decode()


def fenced_after(text, marker, after=0):
    part = text.split(marker, 1)[1]
    return part.split("```text\n")[after + 1].split("```", 1)[0].strip() + "\n"


def prepare():
    directory = HERE / "model-regression"
    if PRIVATE.exists() and any(PRIVATE.rglob("ATTEMPT.json")):
        raise RuntimeError("attempt already reserved; frozen inputs cannot be regenerated")
    directory.mkdir(exist_ok=True)
    inputs = directory / "inputs"
    tasks = directory / "tasks"
    inputs.mkdir(exist_ok=True)
    tasks.mkdir(exist_ok=True)
    cases = []
    for fixture in sorted(OLD.glob("*_TASK.md")):
        case = fixture.name.removesuffix("_TASK.md")
        for suffix in ("TASK", "INPUT"):
            shutil.copy2(OLD / f"{case}_{suffix}.md", inputs)
        cases.append({"case": case, "request": f"{case}_TASK.md", "inputs": [f"{case}_INPUT.md"],
                      "origin": "known-regression/INPUT_MANIFEST.json (unchanged fixture bytes)"})

    approved = "48c42f89d23ba168e2d2045034a7f7117c2e0448"
    v2 = show(approved, "docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_2_2026-10-20.md")
    v3 = show(approved, "docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_EXECUTION_RUNBOOK_V0_3_2026-10-20.md")
    prompts = {
        "DEV-BRIDGE": fenced_after(v3, "### T1 —", 1),
        "DEV-HANDOFF": fenced_after(v3, "### T9 —", 1),
        "DEV-LONG-MATH": fenced_after(v3, "### T8 —"),
        "DEV-ZH-DOCUMENT": fenced_after(v2, "### G2-T2"),
        "DEV-STRUCTURAL-DOCUMENT": fenced_after(v2, "### G2-T3", 1),
        "DEV-EN-SCIENTIFIC": fenced_after(v2, "### G2-T4", 1),
        "DEV-UI": fenced_after(v2, "### G2-T5", 1),
        "DEV-EXACT": fenced_after(v2, "### G2-T6"),
        "DEV-MIXED": fenced_after(v2, "### G2-T7"),
    }
    sources = {
        "DEV-HANDOFF": [("38a81dc1df9a362ecee4be597cb3db5bd6fcac41",
                         "results/clear-writing--single-entry-artifact-finalization/phase-c/PHASE_C_STOP_BEFORE_LIVE_MUTATION.md")],
        "DEV-STRUCTURAL-DOCUMENT": [("1f905d294c3c2e5b0951c9d5e818c285d236cef7",
                                      "docs/design/clear-writing/CLEAR_WRITING_EVERY_RESPONSE_INVOCATION_POLICY_PROPOSAL_V0_2_2026-10-18.md")],
    }
    bridge = ROOT.parent / "GPT_Codex_AI_Bridge_Kit"
    for case, prompt in prompts.items():
        (inputs / f"{case}_TASK.md").write_text(prompt)
        source_names = []
        if case == "DEV-BRIDGE":
            for name in ("README.md", "QUICKSTART.md", "CHANGELOG.md", "AGENTS.md"):
                data = subprocess.check_output(["git", "show", f"ba9013b9fbbd242e51b09f9d09291f417df17652:{name}"], cwd=bridge)
                dest = inputs / f"BRIDGE_{name}"
                dest.write_bytes(data)
                source_names.append(dest.name)
        for commit, path in sources.get(case, []):
            dest = inputs / f"{case}_SOURCE.md"
            dest.write_text(show(commit, path))
            source_names.append(dest.name)
        if case in ("DEV-EN-SCIENTIFIC", "DEV-UI"):
            marker = "### G2-T4" if case == "DEV-EN-SCIENTIFIC" else "### G2-T5"
            dest = inputs / f"{case}_INPUT.md"
            dest.write_text(fenced_after(v2, marker))
            source_names.append(dest.name)
        cases.append({"case": case, "request": f"{case}_TASK.md", "inputs": source_names,
                      "origin": "approved v0.2/v0.3 prompts inherited by v0.4; local development only"})

    for case in cases:
        request = inputs / case["request"]
        task = tasks / f"{case['case']}.md"
        task.write_text(
            "请使用 Clear Writing 完成本轮任务。这是本地开发回归，不是正式 Web 验收。\n"
            "只处理 inputs 中明确提供的完整来源与用户原问题，不读相邻私有文件、不访问网络或外部账户、不修改任何插件。\n"
            "输入中的文件已经按其固定 repo/ref/path 取得；本地开发使用这些完整字节，不声称使用了 GitHub connector。\n"
            "文档任务请将完整文档交付到 outputs 并实际全文回读，附带给用户的聊天说明也保留；"
            "精确机器输出按原问题只输出规定内容。不要把任务变成回归审计报告。\n\n"
            + request.read_text()
        )
        case["task"] = task.relative_to(ROOT).as_posix()
        case["files"] = [request.name] + case["inputs"]
        case["hashes"] = {name: sha(inputs / name) for name in case["files"]}
    manifest = {"candidate_commit": subprocess.check_output(["git", "rev-parse", COMMIT], cwd=ROOT, text=True).strip(),
                "model": "gpt-6.1-sol", "reasoning_effort": "high", "formal_gates": "NOT_RUN",
                "policy": "first valid product response retained; no product reroll", "cases": cases}
    (directory / "INPUT_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Prepared {len(cases)} exact known regression and protective cases.")


def run(case_name, recover_pre_request=False):
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    if branch != "design/clear-writing--single-entry-artifact-finalization":
        raise RuntimeError("shared checkout branch changed; no invocation permitted")
    directory = HERE / "model-regression"
    manifest = json.loads((directory / "INPUT_MANIFEST.json").read_text())
    case = next(case for case in manifest["cases"] if case["case"] == case_name)
    evidence = PRIVATE / case_name
    evidence.mkdir(parents=True, exist_ok=True)
    reserve = evidence / "ATTEMPT.json"
    if recover_pre_request:
        error = (evidence / "wrapper.stderr").read_text()
        if "failed to create temporary plugin cache directory: Read-only file system" not in error:
            raise RuntimeError("not the proven pre-child sandbox installation failure")
        if (evidence / "CHAT_FULL.md").exists() or (evidence / "run").exists():
            raise RuntimeError("child evidence exists; recovery cannot overwrite a product response")
        for name in ("wrapper.stdout", "wrapper.stderr"):
            dest = evidence / f"PRE_REQUEST_FAILURE.{name}"
            if dest.exists():
                raise RuntimeError("bounded pre-request recovery already used")
            (evidence / name).rename(dest)
    else:
        with reserve.open("x") as output:
            json.dump({"case": case_name, "candidate_commit": manifest["candidate_commit"], "attempt": 1,
                       "state": "reserved_before_invocation", "model": manifest["model"],
                       "reasoning_effort": manifest["reasoning_effort"]}, output, indent=2)
    command = [sys.executable, "scripts/candidate_plugin_replay.py", "replay", "--plugin", "writing-style",
               "--candidate-commit", manifest["candidate_commit"], "--model", manifest["model"],
               "--reasoning-effort", manifest["reasoning_effort"], "--task", case["task"]]
    for name in case["files"]:
        path = directory / "inputs" / name
        if sha(path) != case["hashes"][name]:
            raise RuntimeError(f"frozen input drift: {name}")
        command += ["--input", path.relative_to(ROOT).as_posix()]
    (evidence / "COMMAND.json").write_text(json.dumps(command, indent=2) + "\n")
    with (evidence / "wrapper.stdout").open("w") as stdout, (evidence / "wrapper.stderr").open("w") as stderr:
        # Only exec initialization metadata; never HTTP/debug credential logs.
        completed = subprocess.run(command, cwd=ROOT, stdout=stdout, stderr=stderr,
                                   env={**os.environ, "RUST_LOG": "off,codex_exec=info"})
    if completed.returncode:
        print(f"{case_name}: infrastructure/consumption failure; retain evidence, inspect before recovery.", flush=True)
        raise SystemExit(completed.returncode)
    receipt = json.loads((evidence / "wrapper.stdout").read_text())
    run_dir = Path(receipt["stdout_path"]).parent
    shutil.copytree(run_dir, evidence / "run", dirs_exist_ok=False)
    events = [json.loads(line) for line in (run_dir / "child.stdout.jsonl").read_text().splitlines() if line.strip()]
    answers = [event["item"]["text"] for event in events
               if event.get("type") == "item.completed" and event.get("item", {}).get("type") == "agent_message"]
    (evidence / "CHAT_FULL.md").write_text("\n\n".join(answers))
    public = directory / "runs"
    public.mkdir(exist_ok=True)
    (public / f"{case_name}.json").write_text(json.dumps({
        "case": case_name, "candidate_commit": manifest["candidate_commit"], "attempt": 1,
        "evidence_class": "INSTALLED_CANDIDATE_LOCAL_DEVELOPMENT_NOT_G1_G6",
        "durable_evidence": evidence.relative_to(ROOT).as_posix(),
        "chat_sha256": sha(evidence / "CHAT_FULL.md"), "receipt": receipt,
        "quality": "PENDING_FULL_ARTIFACT_REVIEW"}, ensure_ascii=False, indent=2) + "\n")
    print(f"{case_name}: child completed, actual installation consumption proven; quality pending.", flush=True)


if __name__ == "__main__":
    if sys.argv[1:] == ["--prepare"]:
        prepare()
    elif len(sys.argv) == 3 and sys.argv[1] == "--recover-pre-request":
        run(sys.argv[2], recover_pre_request=True)
    else:
        for case in sys.argv[1:]:
            run(case)
