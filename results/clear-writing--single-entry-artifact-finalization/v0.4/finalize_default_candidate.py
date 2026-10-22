"""Collect public-safe development outputs and freeze only after real review."""
from pathlib import Path
import base64
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PUBLIC = HERE / "default-regression"
PRIVATE = ROOT / "private/exports/clear-writing--single-entry-artifact-finalization/v0.4"
PRODUCT_SOURCE = "157725b909775e169926c449844301e772e50f08"
SOURCE = "cee207d3fa83ad4571f94774f3896798d837a5ca"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def collect():
    manifest = json.loads((PUBLIC / "INPUT_MANIFEST.json").read_text())
    records = []
    for case in manifest["cases"]:
        receipts = sorted((PUBLIC / "runs").glob(f"{case['case']}-attempt-*.json"))
        if not receipts:
            continue
        results = [json.loads(p.read_text()) for p in receipts]
        products = [r for r in results if r["product_messages"]]
        if len(products) > 1:
            raise RuntimeError("multiple product attempts: " + case["case"])
        record = products[0] if products else results[-1]
        exact_bypass = record["case"] == "DEV-EXACT" and record["helper_exit"] == 1
        if record["helper_exit"] and not exact_bypass:
            records.append(record)
            continue
        assert record["candidate_commit"] == PRODUCT_SOURCE
        if not exact_bypass:
            assert record["receipt"]["actual_consumption"]["proven"]
        raw = ROOT / record["raw_evidence"]
        events = [json.loads(line) for line in (raw / "run/child.stdout.jsonl").read_text().splitlines() if line.strip()]
        record["completed_product_turns"] = sum(e.get("type") == "turn.completed" for e in events)
        record["agent_message_count"] = record["product_messages"]
        assert record["completed_product_turns"] == 1
        if exact_bypass:
            expected = (HERE / "model-regression/inputs/DEV-EXACT_TASK.md").read_text().splitlines()[-1]
            assert (raw / "CHAT_FULL.md").read_text() == expected
            assert "actual consumption was not proven" in (raw / "wrapper.stderr").read_text()
            record["exact_only_protection"] = "PASS; installed, no skill consumption, wrapper exit 1 retained"
        record["candidate_skill_reads"] = sorted({
            skill for e in events
            if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "command_execution"
            and e["item"].get("exit_code") == 0
            for skill in re.findall(r"plugins/cache/ai-skills-candidate/writing-style/[^/\s]+/skills/([^/\s]+)/SKILL\.md",
                                    e["item"].get("command", ""))
        })
        dest = PUBLIC / "outputs" / case["case"]
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(raw / "CHAT_FULL.md", dest / "CHAT_FULL.md")
        artifacts = []
        output = raw / "run/workspace/outputs"
        for path in sorted(output.rglob("*")):
            if path.is_symlink():
                raise RuntimeError("symlink output")
            if path.is_file():
                relative = path.relative_to(output)
                # Heavy-route intermediate packets remain complete in durable raw evidence.
                if any(part.startswith(".") for part in relative.parts):
                    continue
                target = dest / "files" / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
                artifacts.append({"path": target.relative_to(ROOT).as_posix(), "sha256": digest(path.read_bytes())})
        record["artifacts"] = artifacts
        record["chat_path"] = (dest / "CHAT_FULL.md").relative_to(ROOT).as_posix()
        record["chat_sha256"] = digest((dest / "CHAT_FULL.md").read_bytes())
        records.append(record)
    write(PUBLIC / "RUNS.json", {"source_commit": PRODUCT_SOURCE, "records": records,
                                 "counting_note": "product_messages is historical field name for agent messages including commentary; each successful case has exactly one completed model turn",
                                 "expected_cases": 22, "quality": "SEE_INDEPENDENT_QUALITY_REVIEW"})
    print(f"Collected {len(records)}/22 actual result records.")
    return records


def freeze():
    records = collect()
    assert len(records) == 22 and all(r["product_messages"] and
        (r["helper_exit"] == 0 or (r["case"] == "DEV-EXACT" and r["helper_exit"] == 1)) for r in records)
    identities = {(r["actual_model"], r["actual_reasoning_effort"], r["runtime_cli"]) for r in records}
    assert len(identities) == 1 and all(not r["explicit_model_arguments"] for r in records)
    six = {"fidelity", "response-clarity", "zh", "scientific-rewrite", "sci", "product-ui-copy"}
    assert six <= {skill for r in records for skill in r["candidate_skill_reads"]}
    review = json.loads((PUBLIC / "QUALITY_REVIEW.json").read_text())
    assert review["source_commit"] == SOURCE and review["implementation_review"] == "PASS"
    assert set(review["cases"]) == {r["case"] for r in records}
    assert all(v == "PASS" for v in review["cases"].values())
    revalidation = json.loads((HERE / "helper-revalidation/RESULT.json").read_text())
    assert revalidation["source_commit"] == SOURCE and revalidation["helper_exit"] == 0
    assert revalidation["validation_exit"] == 0 and revalidation["first_product_bytes_unchanged"]
    assert revalidation["receipt"]["actual_consumption"]["proven"]
    assert revalidation["actual_model"] == records[0]["actual_model"]
    assert revalidation["actual_reasoning_effort"] == records[0]["actual_reasoning_effort"]
    production_paths = ["skills/writing/core", "plugins/codex/plugins/writing-style",
                        "packaging/chatgpt/writing-style", "profiles/codex-writing-style.json",
                        "scripts/candidate_plugin_replay.py", "scripts/build_clear_writing_chatgpt_wrapper.py"]
    delta = subprocess.check_output(["git", "diff", "--name-only", PRODUCT_SOURCE, SOURCE,
                                    "--", *production_paths], cwd=ROOT, text=True).splitlines()
    assert set(delta) == {"skills/writing/core/scientific-rewrite/scripts/rewrite_support.py",
                         "plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py"}
    ci = json.loads((HERE / "validation/GITHUB_CI_FINAL.json").read_text())
    assert ci["headSha"] == SOURCE and ci["conclusion"] == "success"
    assert len(ci["jobs"]) == 4 and all(j["conclusion"] == "success" for j in ci["jobs"])
    test_log = PRIVATE / "FULL_TESTS_FINAL_CANDIDATE.log"
    text = test_log.read_text()
    assert "Ran 397 tests" in text and "\nOK\n" in text
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_clear_writing_chatgpt_wrapper as builder
    files, receipt = builder.build_payload(ROOT, "0.6")
    raw_zip = builder.deterministic_zip(files)
    assert raw_zip == builder.deterministic_zip(files)
    expected = PRIVATE / "final-clear-writing-0.6.0.zip"
    assert raw_zip == expected.read_bytes()
    receipt["source_commit"] = SOURCE
    receipt["candidate_replay_entry_sha256"] = digest((ROOT / "scripts/candidate_plugin_replay.py").read_bytes())
    write(HERE / "wrapper/BUILD_RECEIPT_FINAL.json", receipt)
    transport = HERE / "transport"
    transport.mkdir(exist_ok=True)
    encoded = base64.b64encode(raw_zip)
    parts = []
    for index, offset in enumerate(range(0, len(encoded), 6000)):
        data = encoded[offset:offset + 6000]
        name = f"part-{index:03d}.b64"
        (transport / name).write_bytes(data)
        parts.append({"filename": name, "sha256": digest(data), "size_bytes": len(data)})
    reconstructed = base64.b64decode(b"".join((transport / p["filename"]).read_bytes() for p in parts), validate=True)
    assert reconstructed == raw_zip
    write(transport / "MANIFEST.json", {"schema": "CLEAR_WRITING_PRIVATE_WRAPPER_TRANSPORT_V1",
          "source_commit": SOURCE, "zip_sha256": digest(raw_zip), "zip_size_bytes": len(raw_zip),
          "base64_sha256": digest(encoded), "part_count": len(parts), "part_size_limit": 6000,
          "parts": parts, "classification": "PUBLIC_SAFE_REPOSITORY_PAYLOAD_ONLY"})
    paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", SOURCE, "skills/writing/core",
                                    "plugins/codex/plugins/writing-style", "packaging/chatgpt/writing-style",
                                    "profiles/codex-writing-style.json", "scripts/candidate_plugin_replay.py",
                                    "scripts/build_clear_writing_chatgpt_wrapper.py", "scripts/codex_marketplace_config.json",
                                    ".agents/plugins/marketplace.json", "tests",
                                    "docs/design/clear-writing/CLEAR_WRITING_0_6_GATE_RUNBOOK_V0_4_2026-10-22.md",
                                    "docs/design/clear-writing/CLEAR_WRITING_0_6_PRODUCT_AND_EXECUTION_PLAN_V0_4_2026-10-22.md",
                                    "docs/goals/CLEAR_WRITING_0_6_UNIFIED_DELIVERY_GOAL_V0_4_2026-10-22.md",
                                    "docs/operations/prompts/CLEAR_WRITING_0_6_KICKOFF_DRAFT_V0_4_2026-10-22.md"], cwd=ROOT, text=True).splitlines()
    identities = []
    for path in paths:
        data = subprocess.check_output(["git", "show", f"{SOURCE}:{path}"], cwd=ROOT)
        assert data == (ROOT / path).read_bytes()
        identities.append({"path": path, "sha256": digest(data)})
    candidate = {
        "schema": "CLEAR_WRITING_06_FINAL_CANDIDATE_V2", "source_commit": SOURCE,
        "approved_product_package": "48c42f89d23ba168e2d2045034a7f7117c2e0448",
        "model_contract_amendment": PRODUCT_SOURCE, "model_contract_authority": "v0.4/DEFAULT_ENTRY_AUTHORITY.md",
        "default_entry_authority_sha256": digest((HERE / "DEFAULT_ENTRY_AUTHORITY.md").read_bytes()),
        "writing_style_version": "0.6", "personal_wrapper_version": "0.6.0",
        "wrapper_archive_sha256": digest(raw_zip), "wrapper_archive_size_bytes": len(raw_zip),
        "build_receipt": "v0.4/wrapper/BUILD_RECEIPT_FINAL.json",
        "build_receipt_sha256": digest((HERE / "wrapper/BUILD_RECEIPT_FINAL.json").read_bytes()),
        "transport_manifest": "v0.4/transport/MANIFEST.json", "files": identities,
        "transform_rule_version": builder.PROJECTION, "zip_spec_version": builder.ZIP_SPEC,
        "reader_value_contract": "CHAT_RESPONSE_READER_VALUE_SELECTION_V1", "gate_rule_version": "CW06-v0.4",
        "archive_reader_sha256": digest((ROOT / "scripts/build_clear_writing_chatgpt_wrapper.py").read_bytes()),
        "runtime": {"cli": "0.153.4", "actual_model": records[0]["actual_model"],
                    "actual_reasoning_effort": records[0]["actual_reasoning_effort"],
                    "explicit_model_arguments": False, "ignore_user_config": True},
        "codex_candidate_replay": "PASS", "known_regressions": "18/18 PASS", "should_not_change": "4/4 PASS",
        "replay_lineage": {"first_product_source": PRODUCT_SOURCE, "first_product_cases": 22,
            "generic_replay_successes": 21, "exact_only_protection": "PASS; wrapper exit 1 and no skill consumption retained",
            "unaffected_product_evidence_carried_forward": 21, "production_delta": delta,
            "affected_fixed_product_revalidation_source": SOURCE,
            "affected_revalidation": "v0.4/helper-revalidation/RESULT.json",
            "first_product_redrafted": False},
        "implementation_review": "PASS", "code_implementation": "COMPLETE", "current_final_candidate_frozen": True,
        "release_status": "NOT_RELEASED", "live_gates": "NOT_RUN", "web_gates_run": False,
        "historical_only": False,
        "live_personal_plugin_mutated": False, "next_handoff": "PHASE_C", "release_eligible": False,
        "meaning": "Code and Codex candidate accepted; account backup/restore, Web gates and formal release remain separate."
    }
    historical = HERE.parent / "candidate/FINAL_CANDIDATE.json"
    backup = historical.with_name("HISTORICAL_FINAL_CANDIDATE_079bd798.json")
    if not backup.exists():
        shutil.copy2(historical, backup)
    write(historical, candidate)
    runtime_path = HERE / "validation/CODEX_RUNTIME_PREFLIGHT.json"
    previous = HERE / "validation/HISTORICAL_EXPLICIT_MODEL_RUNTIME.json"
    if not previous.exists():
        shutil.copy2(runtime_path, previous)
    write(runtime_path, {
        "source_commit": SOURCE, "runtime_cli": "codex-cli 0.153.4",
        "actual_model": records[0]["actual_model"], "actual_reasoning_effort": records[0]["actual_reasoning_effort"],
        "resolution": "fixed CLI normal default; no model or reasoning arguments",
        "ignore_user_config": True, "same_batch_identity": True, "product_cases": 22,
        "generic_helper_successes": 21, "fixed_helper_revalidation_successes": 1,
        "actual_installed_candidate_consumption": True, "cleanup_succeeded": True,
        "first_product_source": PRODUCT_SOURCE, "final_installed_helper_source": SOURCE,
        "exact_only_no_consumption_case": "DEV-EXACT; wrapper exit 1 retained",
        "candidate_replay_helper_sha256": digest((ROOT / "scripts/candidate_plugin_replay.py").read_bytes()),
        "historical_explicit_model_diagnostic": previous.relative_to(ROOT).as_posix(),
        "web_model": "GPT-5.6 Sol", "web_gates_run": False,
    })
    write(HERE / "validation/DEFAULT_CANDIDATE_VALIDATION.json", {
        "source_commit": SOURCE, "full_tests": "397/397 PASS", "test_log_sha256": digest(test_log.read_bytes()),
        "full_test_log": test_log.relative_to(ROOT).as_posix(), "ci_run": ci["databaseId"],
        "source_generated_support_parity": "PASS", "deterministic_zip": "PASS",
        "all_distribution_files_bound": True, "final_candidate_frozen": True,
        "implementation_review": "PASS", "product_review": "22/22 PASS (known local development only)",
    })
    print(f"Frozen {SOURCE}; ZIP {digest(raw_zip)}, {len(raw_zip)} bytes, {len(parts)} transport parts.")


if sys.argv[1:] == ["--freeze"]:
    freeze()
else:
    collect()
