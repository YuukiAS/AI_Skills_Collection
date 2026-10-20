"""Replay the frozen public-safe known cases through the canonical local entry.

This is development evidence for the wrapper source and unchanged writing
routes. It is not ChatGPT Web exposure, external-file finalization, or G1-G6.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[3]
TASK = "clear-writing--single-entry-artifact-finalization"
HERE = Path(__file__).resolve().parent
ARCHIVE = ROOT / f"private/exports/{TASK}/clear-writing-0.6.0.zip"
DURABLE = Path("/overflow/htzhu/mingcheng_new/AI_Skills_Collection/private/exports") / TASK / "known-regression"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replay(case: str, fixture: str, source_commit: str, archive_sha256: str) -> dict:
    record_path = HERE / "runs" / f"{case}.json"
    if record_path.exists():
        raise RuntimeError(f"attempt already recorded; inspect before any retry: {case}")
    task_path = HERE / "tasks" / f"{case}.md"
    task_path.parent.mkdir(parents=True, exist_ok=True)
    task_path.write_text(
        "# Local implementation replay\n\n"
        "This is a public-safe development replay, not a ChatGPT Web gate. "
        "Unpack the explicitly supplied Clear Writing candidate ZIP into a task-owned "
        "directory inside the replay workspace. Read and apply its single entry at "
        "skills/clear-writing/SKILL.md and the selected packaged routes. "
        "Use the existing installed writing-style capability; do not update any plugin. "
        "Keep package-local paths rooted at the extracted plugin.\n\n"
        f"The original user request is in {fixture}_TASK.md and its complete source "
        f"is in {fixture}_INPUT.md. Follow that request exactly; do not rewrite the task. "
        "Do not access the source repository, other private files, or network. "
        "The final reply must be only the requested answer/artifact, with no replay "
        "report or claim about real Web invocation. If the request asks for a report "
        "or executable prompt/contract, supply the complete artifact.\n",
        encoding="utf-8",
    )
    command = ["ai-bridge", "plugin-replay", "--target", str(ROOT),
               "--plugin", "writing-style@yuukias-ai-skills", "--task", str(task_path),
               "--input", str(ARCHIVE),
               "--input", str(HERE / "fixtures" / f"{fixture}_TASK.md"),
               "--input", str(HERE / "fixtures" / f"{fixture}_INPUT.md")]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    private = DURABLE / case
    private.mkdir(parents=True, exist_ok=True)
    (private / "wrapper.stdout").write_text(completed.stdout)
    (private / "wrapper.stderr").write_text(completed.stderr)
    record = {"case": case, "fixture": fixture, "source_commit": source_commit,
              "wrapper_archive_sha256": archive_sha256,
              "evidence_class": "LOCAL_WRAPPER_SOURCE_REPLAY_NOT_WEB_GATE",
              "attempt": 1, "exit_code": completed.returncode}
    try:
        receipt = json.loads(completed.stdout)
        run_dir = Path(receipt["run_dir"])
        shutil.copytree(run_dir, private / "replay", dirs_exist_ok=True)
        record.update({"run_id": receipt["run_id"], "status": receipt["status"]})
        if completed.returncode == 0 and receipt["status"] == "completed":
            answer = Path(receipt["last_message_path"]).read_bytes()
            out = HERE / "outputs" / f"{case}_OUTPUT.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(answer)
            record["output_sha256"] = digest(answer)
    except (KeyError, ValueError, OSError) as error:
        record["receipt_error"] = str(error)
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    return record


def main() -> None:
    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    receipt = json.loads((HERE.parent / "wrapper/BUILD_RECEIPT.json").read_text())
    archive_sha256 = digest(ARCHIVE.read_bytes())
    if archive_sha256 != receipt["wrapper_archive_sha256"]:
        raise RuntimeError("archive identity mismatch")
    cases = [(f"KR-WEB-{i:02}", f"RW-WEB-{i:02}") for i in range(1, 6)]
    cases += [(f"KR-WEB-{i:02}", f"KR-WEB-{i:02}") for i in range(6, 10)]
    cases += [(f"CW-CONTROL-{i:02}", f"CW-CONTROL-{i:02}") for i in range(1, 5)]
    records = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        pending = {executor.submit(replay, case, fixture, source_commit, archive_sha256): case
                   for case, fixture in cases}
        for future in as_completed(pending):
            result = future.result()
            records.append(result)
            print(json.dumps(result, ensure_ascii=False), flush=True)
    (HERE / "RUNS.json").write_text(json.dumps(sorted(records, key=lambda r: r["case"]), indent=2) + "\n")
    if any(record["exit_code"] or "output_sha256" not in record for record in records):
        raise SystemExit("At least one replay did not complete; inspect evidence before retrying.")


if __name__ == "__main__":
    main()
