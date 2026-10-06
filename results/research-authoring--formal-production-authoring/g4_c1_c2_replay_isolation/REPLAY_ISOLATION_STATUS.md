# G4-C1 C2 Development Replay Isolation Status

Date: 2026-10-06
Branch: `work/research-authoring--formal-production-authoring`
Candidate under test: `research-writing@ai-skills-candidate`
Candidate commit: `ac501d988f00cb6672fec105ae5fd51a0679cae0`
Repo-local runtime: `codex-cli 0.153.4`

## Scope

This diagnostic did not modify Research Authoring production source, Marketplace source config, routing tests, generated plugin payload, frozen G4 task/rubric/baseline, the live Plugin, Bridge Kit, or global user plugin state intentionally. It only tested whether the current Codex runtime supports process-local disabling of the conflicting live wrapper while enabling the candidate.

## Process-local config tested

```text
plugins.research-writing@ai-skills-candidate.enabled=true
plugins.research-authoring@created-by-me-remote.enabled=false
```

The manual replay command is preserved in `manual-replay-command.txt`. CLI help/config evidence is preserved in `codex-help.txt`, `codex-exec-help.txt`, and `codex-plugin-help.txt`. Plugin-list before/after evidence is preserved in `plugin-list-before.json` and `plugin-list-after.json`.

## Result

```text
CANDIDATE_PLUGIN_ENABLED=YES
CONFLICTING_LIVE_WRAPPER_PROCESS_LOCAL_DISABLED=NO
PERSISTENT_LIVE_PLUGIN_MUTATION=NO
CANDIDATE_ACTUAL_CONSUMPTION_PROVEN=NO
```

The child run completed successfully and produced the expected source/handoff files, with no PDF/render mechanics observed:

```text
child_returncode=0
required_output_files_present=true
pdf_output_files=[]
forbidden_command_counts.xelatex=0
forbidden_command_counts.latexmk=0
forbidden_command_counts.pandoc_to_pdf=0
forbidden_command_counts.pdf_open_render_tools=0
forbidden_command_counts.pdf_text_info_fonts=0
```

However, candidate consumption was not proven. Parsed child JSONL command events show:

```text
candidate_read_event_count=0
live_wrapper_read_event_count=6
candidate_installed_path=/users/a/e/aereinh/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3
conflicting_live_path=/users/a/e/aereinh/.codex/plugins/cache/created-by-me-remote/research-authoring/0.3.0
```

The live wrapper read events are preserved in `live-wrapper-read-events.json`; candidate read events are preserved in `candidate-read-events.json` and are empty.

## Persistent-state checks

```text
candidate_absent_after_cleanup=true
plugin_list_unchanged_after_cleanup=true
persistent_live_plugin_mutation=false
```

The live wrapper tree hash before/after is preserved in `live-wrapper-tree-before.json` and `live-wrapper-tree-after.json`.

## Closure

The current Codex runtime did not provide a reliable process-local live-wrapper disable for this replay surface. Because candidate actual consumption remains unproven, this development replay cannot be used as a C2 PASS.

```text
CANDIDATE_REPLAY_ISOLATION_UNAVAILABLE=YES
SHARED_REPLAY_HELPER_CHANGE_MAY_BE_REQUIRED=YES
PRODUCTION_CANDIDATE_CHANGE_REQUIRED=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER_CRITIC
```
