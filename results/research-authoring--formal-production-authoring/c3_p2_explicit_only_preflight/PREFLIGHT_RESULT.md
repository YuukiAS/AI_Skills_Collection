# C3 P2 explicit-only profile preflight result

Status: FAIL / STOP_BEFORE_P2
Date: 2026-10-07
Runtime: codex-cli 0.153.4 from `.local-runtime/codex/0.153.4/bin/codex`
Task: research-authoring--formal-production-authoring

## Static installer evidence

The task-local `research-main` install used the production installer path:

```bash
python scripts/skills.py install --target repo --project results/research-authoring--formal-production-authoring/c3_p2_explicit_only_preflight/project --profile research-main --mode symlink --write-agents-md --json
```

Evidence:

- `evidence/install.json`
- `project/AGENTS.md`
- explicit delegate installed copies:
  - `project/.agents/skills/writing-research-latex-paper-authoring/agents/openai.yaml`
  - `project/.agents/skills/tools-documents-media-pdf/agents/openai.yaml`
  - `project/.agents/skills/tools-documents-media-render-chinese-math-pdf/agents/openai.yaml`

Static installer behavior was correct:

```text
PROFILE_EXPLICIT_ONLY_COPIES=YES
DESTINATION_POLICY_ALLOW_IMPLICIT_INVOCATION_FALSE=YES
NORMAL_SKILL_ROUTING_EXCLUDES_EXPLICIT_DELEGATES=YES
PROFILE_EXPLICIT_DELEGATE_LOCATORS_PRESENT=YES
```

## Runtime probes

Implicit owner probe:

- prompt: `inputs/implicit_owner_probe.md`
- JSONL: `evidence/implicit_owner_probe.jsonl`
- final message: `evidence/implicit_owner_probe.last.txt`

Admitted renderer probe:

- prompt: `inputs/explicit_renderer_probe.md`
- JSONL: `evidence/explicit_renderer_probe.jsonl`
- final message: `evidence/explicit_renderer_probe.last.txt`

The admitted renderer probe did read the project-local explicit-only copy later:

```text
.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md
```

But before that, the same run read the same-name user/global renderer Skill:

```text
/users/a/e/aereinh/.agents/skills/tools-documents-media-render-chinese-math-pdf/SKILL.md
```

This means the current pinned runtime did not prove that a profile-installed explicit-only project-local copy contains a same-name global/user Skill. Under Plan v0.3 / Kickoff v0.3, this is a pre-P2 blocker.

## Global/user mutation evidence

No global/user Skill mutation was performed by this preflight. The user/global renderer Skill hash is the same through the checked `.codex` path, and the `.agents` path has the same hash as `.codex` after the run:

- `evidence/global_same_name_before.sha256`
- `evidence/global_same_name_after.sha256`

## Decision

```text
PROFILE_SCOPED_EXPLICIT_DELEGATE_UNSUPPORTED=YES
P2_NOT_CREATED=YES
C3_CANDIDATE_READY=NO
FINAL_GATES_NOT_STARTED=YES
NEXT_HANDOFF=PLANNER
```

No P2 product commit was formed. The focused source/test implementation attempt remains uncommitted for inspection, but it is not a candidate identity.
