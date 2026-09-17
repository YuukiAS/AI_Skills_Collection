# 057 Repo AGENTS Hygiene — Planner Proposal

- Task key: `057_repo_agents_hygiene`
- Date: 2026-09-17
- Status: `DRAFT_FOR_CRITIC_REVIEW`
- Nature: cross-repo instruction-surface cleanup before starting 056 implementation
- Relationship to 056: **separate task**. Do not modify the already approved 056 execution package or start its Executor until 057 is closed and 056 receives a short source-drift revalidation.

## 1. User goal

This task is **not** about making different repositories carry the same rules. The user specifically wants each repository's own `AGENTS.md` / closely coupled agent-rule surface cleaned up internally:

- find duplicate or near-duplicate rules inside the same repo;
- find internal contradictions, stale authority descriptions, or two sections that can be read as competing instructions;
- preserve every important project-specific invariant, safety boundary, canonical locator and accepted workflow;
- make the files easier to scan and structurally more consistent across repositories;
- avoid the current pattern where rules are appended incident-by-incident until the file becomes a chronological rule pile;
- do not remove a rule merely because it is long; move detailed mechanics to an existing or task-created canonical document only when the rule remains discoverable and semantically preserved.

This task does not redesign Product Delivery Discipline v6. Generic workflow discipline stays with Bridge Kit / Verified Workflow / Frontend Design / AI Skills Maintainer. Repository files keep project-specific facts.

## 2. Why this is worth doing before 056

Current OpenAI Codex source uses a default `project_doc_max_bytes = 32768` total budget for project instruction content, and OpenAI's 2026 harness-engineering guidance explicitly reports that a monolithic `AGENTS.md` failed in practice; they use a short AGENTS file as a map into deeper repository knowledge. This makes internal duplication and stale detail a real consumption risk, not only a style issue.

References checked in this design round:

- OpenAI, *Harness engineering: leveraging Codex in an agent-first world* (2026-02-11): recommends a short `AGENTS.md` as a map rather than a large manual.
- `openai/codex` current source/config: project instruction discovery is subject to a default 32 KiB aggregate project-doc budget.

The target is therefore **progressive disclosure**, not deleting project knowledge.

## 3. Scope

### Primary rewrite candidates

1. `YuukiAS/Bobbio` — `develop`
2. `YuukiAS/Lucerna` — `main`
3. `YuukiAS/Mica-for-ChatGPT` — `main`
4. `YuukiAS/Asteria` — `main`
5. `YuukiAS/SeminarArc` — `main`

### Inspect but do not create new root policy merely for uniformity

6. `YuukiAS/CUHK_Date` — `main`
   - current tracked instruction surface is `docs/design/prototype/AGENTS.md`; no tracked root `AGENTS.md` was found in the current main source.

### Closely coupled instruction surfaces

Where root `AGENTS.md` explicitly delegates to a local `prompts/AGENT_RULES.md`, 057 must inspect both for **within-repo** contradiction or duplicate ownership. It must not blindly merge Bridge Kit managed blocks into project-local rules.

### Out of first-wave implementation scope

CARE/Server/EAT have broader scientific/HPC/control-plane instruction systems and should not be silently swept into the same rewrite without their own source inventory. 057 may list them as future candidates, but this first wave must not mutate them unless the user explicitly expands scope and Critic reviews that expansion.

## 4. Common style target

This is a style/navigation target, not a requirement that every repo contain identical sections.

Each root `AGENTS.md` should, where relevant, read in roughly this order:

1. **Purpose / precedence / default entry** — what this file owns and which generated/managed block must not be hand-edited.
2. **Read first / canonical locators** — short conditional map to deeper authorities.
3. **Project scope and hard invariants** — domain facts that cannot be generalized away.
4. **Environment / source / Git boundaries** — only stable project-specific facts; volatile snapshots move to canonical operational docs.
5. **Safety / data / authority boundaries** — project-specific safety rules.
6. **Testing / acceptance / user-action boundary** — project-specific requirements only; generic Product Delivery Discipline is not duplicated.
7. **Design/UI/domain-specific rules** — only when this repo has such rules.
8. **Version/release/integration rules** — repo-specific release facts.
9. **Deeper docs / ownership** — where detailed mechanics live.

Style rules:

- one concept per bullet;
- short headings and natural prose;
- code identifiers, enum names, paths and commands stay exact;
- no bulk translation merely for uniformity; preserve the repo's established human-language style unless wording is being touched anyway;
- do not preserve historical incident narrative in root AGENTS when a durable invariant plus a canonical evidence/doc locator is enough;
- avoid duplicating the same rule in both root AGENTS and a canonical detailed contract. Root should keep a concise invariant + locator when the detail lives elsewhere;
- do not manually edit content inside Bridge Kit generated/managed markers unless the task explicitly regenerates that block from its canonical source;
- target root AGENTS to fit comfortably below Codex's aggregate project-doc budget when practical. This is not a blind line-count gate: safety-critical facts may justify a larger file, but such detail should be moved to canonical docs when an equivalent discoverable structure exists.

## 5. Preservation contract

Every rewrite must produce a **semantic preservation table** before editing:

| Current rule/invariant | Current owner/location | Keep in root / move / merge | New canonical location | Reason |
|---|---|---|---|---|

Rules may be removed from root only when one of these is true:

1. exact/near-exact duplicate inside the same repo and one canonical statement remains;
2. detailed mechanism is moved to an existing or newly created canonical project doc and root retains a clear locator/invariant;
3. directly contradictory stale wording is replaced by the current authoritative rule, with evidence for which rule is current;
4. purely historical incident narrative is reduced to the durable invariant plus evidence locator.

Forbidden:

- deleting project safety or data boundaries for brevity;
- replacing exact project rules with vague central-plugin prose;
- deleting a rule because 056 *plans* to provide a generic capability but that production capability has not yet been implemented and verified;
- converting a project-specific source locator into generic workflow text;
- inventing a new project workflow/state machine while editing prose.

## 6. Per-repo findings and proposed action

### 6.1 Bobbio — substantial internal cleanup + one known locator fix

Current evidence:

- root AGENTS has 20+ sections and repeats related human/GUI/acceptance semantics across `Computer Use 与 GUI gate`, `Anti-blocking / Goal continuation`, `Desktop acceptance`, and the separate `docs/DEVELOPMENT_WORKFLOW.md` pre-user policy;
- frontend/Product Design read-list currently names `PRODUCT_DESIGN_BRIEF.md` and four `images/Bobbio_Design_*.png`, while `docs/design/FIGMA_HANDOFF.md` explicitly says Figma is the **canonical visual design source** for subsequent implementation and the old images are references/baselines;
- this creates a real authority ambiguity even before 056: the root file can be read as telling an implementer to derive the design system from the four images rather than follow current Figma.

Proposed rewrite:

1. Add `docs/design/FIGMA_HANDOFF.md` to frontend/Product Design conditional reads.
2. Clarify authority:
   - Figma handoff = current canonical visual source;
   - `PRODUCT_DESIGN_BRIEF.md` = durable product/interaction constraints;
   - `images/Bobbio_Design_*.png` = historical/supporting visual references, not a parallel production authority.
3. Consolidate general “when may we ask the user?” semantics into one `Execution / human gate` section. Keep Zotero-specific warnings (e.g. never click updater, isolation constraints) next to Zotero safety.
4. Collapse repeated pre-user QA wording into a concise root invariant + locator to `docs/DEVELOPMENT_WORKFLOW.md` and `docs/quality/NATIVE_DESKTOP_ACCEPTANCE.md`; keep Bobbio-specific native Windows/Tauri and isolated Zotero requirements in root.
5. Keep all knowledge/annotation/Zotero authority rules, but organize them under a smaller set of canonical domain headings rather than incident-era accumulation.
6. Do not delete iPad/Pencil requirements; use locators to its dedicated architecture/QA contracts.

Expected result: shorter, more navigable root AGENTS with **no loss of Zotero safety, knowledge authority, native acceptance, versioning, or milestone constraints**.

### 6.2 Lucerna — light normalization only

Current AGENTS is comparatively coherent. Its long sections are mostly genuinely Lucerna-specific:

- Windows release behavior;
- tray/close lifecycle;
- live provider truth and no mock release evidence;
- canonical screenshot helper;
- Longleaf source/permission boundary.

Proposed action:

- keep the Bridge Kit managed block untouched;
- normalize headings/order and remove only exact/near-exact repetition;
- keep `UI Acceptance`, `Windows Screenshot`, and `Longleaf Integration` as distinct owners because they protect different failures;
- do not replace concrete Lucerna behavior with generic W1/W3/W5 prose;
- if screenshot mechanics are moved, only move them to a canonical Lucerna doc in the same change and retain the helper locator in root.

Expected result: modest style cleanup, not a rewrite.

### 6.3 Mica — merge repeated testing prose, preserve browser-specific invariants

Current evidence:

- `Development testing budget`, `Test tiers`, and `Focused iteration before full E2E` repeat much of the same focused-first/full-E2E-last policy;
- `P0 acceptance` says to test a real long conversation, while `Browser-test boundary` correctly forbids automated authenticated ChatGPT loops and makes the user's real-site pass manual. These are compatible, but the current separation can look contradictory.

Proposed rewrite:

1. Merge the repeated test-loop guidance into one testing ladder:
   - focused risk test during iteration;
   - same focused failure twice -> inspect source/fixture/validator before another rerun;
   - Tier 1/2/3 definitions;
   - at most one stable full E2E attempt per candidate unless substantive runtime changes follow a real failure.
2. Clarify that “real long conversation” is the final/manual authenticated acceptance path, **not** an automated real-account regression loop.
3. Keep separate, prominent sections for:
   - fail-open ChatGPT DOM/private-endpoint behavior;
   - privacy-safe built-in diagnostics;
   - typing hot-path performance invariant;
   - stable `dist/mica-dev` path and runtime version identity.
4. Do not add 056 generic human-time or repeat-failure text if the Mica-specific version already expresses the behavior more precisely.

Expected result: materially shorter testing section without weakening the real-site/account/performance boundaries.

### 6.4 Asteria — convert root AGENTS from operational manual to map + hard invariants

Current evidence:

- root AGENTS contains a Bridge managed block plus detailed local rules;
- the root repeats a large amount of the already-canonical `UI_BLACKBOX_BROWSER_CONTRACT.md` instead of primarily pointing to it;
- fixed public URL/tunnel/start commands, dev-server mechanics and other volatile operational details live directly in root;
- `prompts/AGENT_RULES.md` already owns developer visual self-QA, canonical scientific graph visual system, generic-fix/no-fixture-hardcode, and related execution rules.

Proposed rewrite:

1. Keep the managed Bridge block untouched.
2. Keep in root only stable project invariants:
   - fixed public entry point must not be silently replaced;
   - black-box audit must use the canonical browser contract;
   - GPT Work-before-human release gate;
   - version/Git standing authorization boundaries;
   - current normal dev-server locator.
3. Move exact tunnel/server/runtime commands and dated operational facts into a canonical Asteria operations doc (create one only if no adequate current doc exists), then link it from root.
4. Replace duplicated browser-contract details with a short locator + the essential invariant `可以自动操作页面；不能绕过页面`; the canonical contract remains the detailed authority.
5. Root must point to `prompts/AGENT_RULES.md` for developer visual self-QA / scientific graph / generic-fix rules rather than re-copying them.
6. Preserve the acceptance campaign and regression requirements; do not weaken the GPT Work-before-human gate.

Expected result: large reduction in root operational clutter while all runtime, browser, visual and release rules remain reachable and authoritative.

### 6.5 SeminarArc — largest map-vs-manual cleanup, with safety preservation

Current evidence:

- root AGENTS contains long dated environment snapshots (SDK/JDK/AVD versions, cache paths, WSL interop state) and a very long physical-device safety block;
- `docs/DEVICE_TESTING.md` already exists as the canonical emulator/physical-device testing policy and duplicates many of those facts;
- root AGENTS also contains project skills, 0.1.x scope, dogfood recovery, Compose architecture and a managed Bridge block.

Proposed rewrite:

1. Keep a short **non-negotiable physical-device safety summary** in root:
   - Emulator-first;
   - protected physical serial is never a generic connected-test target;
   - no automatic transport recovery/reset;
   - explicit serial + pre/postflight for authorized physical writes;
   - device-channel failure does not automatically block headless/Emulator work.
2. Make `docs/DEVICE_TESTING.md` the detailed canonical source for command bans, historical incident evidence, environment inventory and mixed-inventory procedure. Before trimming root, ensure every unique safety detail currently in root is preserved there or another canonical environment doc.
3. Move volatile JDK/SDK/AVD/cache/path snapshots into an environment/testing doc; root keeps canonical repo/host roles and locator.
4. Keep project skills, 0.1.x product invariants, internal-dogfood authorization boundary and Compose architectural constraints in root because they are project-specific and frequently needed.
5. Keep the Bridge managed block untouched; audit root + `prompts/AGENT_RULES.md` for internal mapping consistency, but do not hand-copy 056's future Lite rules before 056 is implemented.

Expected result: much shorter root AGENTS without losing the high-risk physical-device protections that were learned from a real disconnect incident.

### 6.6 CUHK Date — no root file created for symmetry

Current tracked `docs/design/prototype/AGENTS.md` is short and internally coherent: it tells the prototype agent to run its own server, use Product Design context, follow a selected mock as the design source, and preserve Sites build files.

Proposed action:

- no new root `AGENTS.md` merely to look like other repos;
- only wording/format cleanup if a direct duplicate/conflict is found during implementation preflight;
- Questionnaire V4 delivery discipline remains a central W1/W3/W5/Frontend concern, not copied here.

## 7. Conflict-resolution rules during implementation

If two statements in the same repo conflict, Executor may not choose by style preference. Resolve in this order:

1. current user instruction / frozen task;
2. current repo branch source and explicit current/canonical docs;
3. newer accepted milestone/ADR/policy that explicitly supersedes an older one;
4. runtime/test evidence;
5. if still ambiguous, stop that specific rewrite and report `EVIDENCE_NEEDED` rather than deleting either rule.

Historical text must not silently override a newer canonical authority, but historical safety evidence should remain accessible.

## 8. Validation / acceptance

057 is a documentation-policy hygiene task, but its success is not “Markdown looks cleaner”. Each repo must pass:

### H1 — Semantic preservation

Every pre-edit hard rule/invariant is accounted for in the preservation table. Deleted/moved content has a canonical surviving owner.

### H2 — No internal contradiction

Search/read the final root AGENTS and delegated agent-rule docs for conflicting authority, user-action, branch, acceptance and source-of-truth statements. Known examples (Bobbio Figma/images, Mica real-site manual vs automated testing) must be explicitly resolved.

### H3 — Discoverability

A new agent starting from root AGENTS can locate the correct current product/design/safety/testing authorities without reading historical incident logs.

### H4 — Managed-block integrity

Bridge-managed sections are not manually forked. Any managed-block update must come from the canonical Bridge mechanism, not 057 hand editing.

### H5 — Context-size improvement

For Bobbio/Asteria/SeminarArc/Mica, report before/after bytes and lines for root AGENTS. A reduction is expected where duplicated or volatile detail moves out, but **semantic preservation takes priority over a numeric target**.

### H6 — Repo-specific regression review

- Bobbio: Zotero isolation/authority + Figma authority + native pre-user review still explicit/discoverable.
- Lucerna: Windows release + real providers + tray/Longleaf still explicit.
- Mica: authenticated account safety + typing hot path + focused testing still explicit.
- Asteria: fixed public URL + black-box contract + GPT Work-before-human + visual-rule locator still explicit.
- SeminarArc: physical-device safety + Emulator-first + dogfood boundary still explicit.
- CUHK Date: prototype behavior unchanged unless a direct conflict was fixed.

No paid API, no product runtime execution, no release/maturity change is needed for 057.

## 9. Relationship to 056 after 057

Do **not** send the already-approved 056 Kickoff before 057 is resolved if the user wants this cleanup first.

After 057 implementation/review:

1. re-read the exact 056 v0.2 Plan/Goal/Kickoff;
2. compare the repos it references against post-057 source;
3. perform a short source-drift revalidation only;
4. if 057 was semantics-preserving and Bobbio locator remains compatible, reuse the 056 architecture without redesign;
5. if 057 changes any 056 assumption materially, return to Planner/Critic before execution.

This avoids silently using an execution-ready package against changed repository policies.

## 10. Alternatives considered

### A. Do nothing; rely on 056 central rules

Rejected. 056 cannot resolve internal authority ambiguity or oversized/stale project instruction files, and current Codex context budgeting makes large root instructions a real consumption risk.

### B. Bulk replace every repo AGENTS with one common template

Rejected. It would erase important project-specific safety/product semantics and create a central-policy copy problem.

### C. Delete all generic-looking rules immediately because 056 will own them

Rejected. 056 production behavior is not implemented yet; removing current protections before proving central consumption would create a gap.

### D. Semantics-preserving per-repo gardening with shared structural style

Recommended. It reduces duplication/context cost while preserving all important project rules and cleanly separates central discipline from project facts.

## 11. Planner recommendation

Proceed with a separate 057 after independent Critic review. Do not fold it silently into the already approved 056 execution package.

`NEXT_HANDOFF = CRITIC`
