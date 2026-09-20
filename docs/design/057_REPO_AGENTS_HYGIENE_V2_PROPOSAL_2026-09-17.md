# 057 Repo AGENTS Hygiene — Planner Proposal v2

- Task key: `057_repo_agents_hygiene`
- Date: 2026-09-17
- Status: `DRAFT_FOR_CRITIC_REVIEW`
- Supersedes: `docs/design/057_REPO_AGENTS_HYGIENE_PROPOSAL_2026-09-17.md`
- Relationship to 056: **057 first, then narrow 056 source-drift revalidation; do not redesign v6 unless 057 changes a frozen 056 assumption.**

## 1. Bottom line

The user clarified two goals that should be handled together before Task 056 implementation:

1. clean up each target repository's own `AGENTS.md` / closely coupled agent-rule surface internally, removing duplicate/conflicting/stale wording while preserving every important project-specific invariant;
2. stop repeating this cleanup on future repositories by making Bridge Kit provide a **reusable project AGENTS scaffold** for new repos.

This does **not** mean different repositories should have identical rules. The shared artifact is a structural scaffold and ownership model; project-specific content remains project-specific.

The proposed sequence is:

```text
057 design review
-> 057 execution package review
-> user-authorized 057 implementation
-> independent 057 implementation review
-> 057 integration/release as approved
-> return to 056
-> short 056 source-drift revalidation / package amendment if needed
-> no v6 redesign unless new source actually invalidates a frozen assumption
```

Because 057 now proposes a Bridge Kit production behavior change for future `ai-bridge init` workspaces, it must be reviewed as more than a pure Markdown-gardening task.

## 2. Current Bridge Kit reality

Current Bridge Kit already has two distinct instruction surfaces:

- `templates/prompts/AGENT_RULES.md` — Lite/project execution rules copied under `prompts/`;
- `codex/AGENTS_SNIPPET.md` — managed root `AGENTS.md` handoff block.

Current `ai_bridge_kit/cli.py::install_agents_snippet()` behaves as follows:

- if root `AGENTS.md` does not exist, it creates one containing only the managed Bridge handoff block;
- if root `AGENTS.md` exists, it appends or updates only that managed block;
- the repo-specific remainder is entirely ad hoc.

Therefore Bridge Kit already owns creation of the root instruction file for fresh repos, but it does not give maintainers a reusable structure for the **project-owned part**. This is exactly why later repos tend to grow incident-by-incident.

## 3. External reality check

Planner rechecked current official OpenAI guidance and source:

- Codex aggregates project `AGENTS.md` / override instructions subject to a default project-doc budget of about 32 KiB;
- OpenAI's current harness-engineering guidance explicitly treats a short `AGENTS.md` as a table of contents / map into deeper repository knowledge rather than an encyclopedia;
- Codex `AGENTS.md` scope is directory-tree based and more deeply nested instructions can override broader ones, so a root scaffold should focus on stable project-wide authority/locators rather than every subsystem's full manual.

Adopted implication: Bridge Kit should standardize **shape and ownership**, not fill every repo with generic policy text.

## 4. Scope

### 4.1 Existing repo cleanup

Primary first-wave repositories:

1. `YuukiAS/Bobbio` — `develop`
2. `YuukiAS/Lucerna` — `main`
3. `YuukiAS/Mica-for-ChatGPT` — `main`
4. `YuukiAS/Asteria` — `main`
5. `YuukiAS/SeminarArc` — `main`
6. `YuukiAS/CUHK_Date` — inspect current prototype instruction surface; do not create a root `AGENTS.md` merely for symmetry

CARE / Server / EAT remain outside first-wave mutation because their scientific/HPC/control-plane instruction systems need their own source inventory.

### 4.2 Bridge Kit reusable project scaffold

Add a Bridge Kit source template, proposed path:

`templates/repo/AGENTS_TEMPLATE.md`

Purpose:

- define the recommended **project-owned** structure for a root `AGENTS.md`;
- coexist with the current Bridge-managed `<!-- ai-bridge-kit:start --> ... <!-- ai-bridge-kit:end -->` block;
- provide future repos a clean starting shape so maintainers append rules into the right owner instead of building a chronological incident pile.

This template is not a new Lite rules file and does not replace `prompts/AGENT_RULES.md`.

## 5. Proposed common root-AGENTS structure

The template should be concise and optional-by-section. Suggested shape:

1. **Purpose / authority / precedence**
   - what the repo is;
   - what this root file owns;
   - which managed/generated blocks must not be hand-edited.
2. **Read first / canonical locators**
   - README/roadmap/current plan;
   - conditional domain/design/safety docs.
3. **Project scope and hard invariants**
   - only durable project-specific facts.
4. **Environment / source / Git boundaries**
   - stable host/source rules only;
   - volatile snapshots move to canonical environment docs.
5. **Safety / data / authority boundaries**
   - repo-specific secrets, production, device, user-data constraints.
6. **Testing / acceptance / human boundary**
   - project-specific acceptance only;
   - generic Product Delivery Discipline is not duplicated here.
7. **Design / UI / domain rules**
   - only when applicable.
8. **Version / release / integration**
   - repo-specific release facts.
9. **Deeper docs / ownership**
   - where long mechanics and historical evidence live.

Not every repo needs every section. Empty/irrelevant sections should be omitted rather than retained as boilerplate.

## 6. Bridge Kit installation behavior

The scaffold should make fresh repos better without rewriting existing repos behind the user's back.

### Fresh repo / no root `AGENTS.md`

`ai-bridge init` should create a root `AGENTS.md` from the canonical scaffold and insert the current managed Bridge block in the designated location.

The created file should be useful but short:

- managed handoff block;
- project-owned structural headings / concise guidance;
- no duplicated Lite checklist;
- no fake project facts;
- no required placeholder text that looks like an invariant.

Implementation may use comments or minimal prompts for sections, but the final rendered file must remain context-efficient.

### Existing root `AGENTS.md`

Keep the current fail-safe behavior:

- do not auto-restructure the user's project-owned content;
- only append/update the managed Bridge block;
- expose the scaffold as the recommended maintenance template/reference;
- migration of an existing repo to the scaffold is an explicit task such as 057, not an automatic `init --force` side effect.

### `--force`

`--force` must not mean "replace the user's whole AGENTS with the canonical template". It may refresh managed Bridge content according to existing semantics, but project-specific prose remains user/repo-owned.

## 7. Why the template must not duplicate Lite Handoff

The current Bridge architecture already separates:

- root `AGENTS.md` / managed Bridge snippet = repository entry map + protocol locator;
- `prompts/AGENT_RULES.md` = long-lived execution rules / Lite handoff surface;
- deeper repo docs = project-specific detailed contracts.

The new scaffold should preserve that split.

Specifically, do **not** copy the six 056 Lite rules verbatim into the new root template. A fresh root should point to `prompts/AGENT_RULES.md` and keep only project-owned invariants/locators. Otherwise the same rule would exist in two long-lived sources and drift.

## 8. Existing repo hygiene contract

Every target repo rewrite still requires a semantic preservation table before editing:

| Current rule/invariant | Current owner/location | Keep in root / move / merge | New canonical location | Reason |
|---|---|---|---|---|

A rule may leave root only if:

1. it is exact/near-exact duplication and one canonical statement remains;
2. detailed mechanics move to an explicit canonical doc while root keeps the hard invariant/locator;
3. stale wording conflicts with a newer accepted authority and the supersession is evidenced;
4. historical incident narrative is reduced to the durable invariant while evidence remains discoverable.

Never remove project safety/data/authority rules merely because the new template is shorter.

## 9. Per-repo intended disposition

### Bobbio — substantial reorganization

- add `docs/design/FIGMA_HANDOFF.md` to frontend/Product Design conditional reads;
- resolve authority as:
  - Figma handoff = current canonical visual source;
  - `PRODUCT_DESIGN_BRIEF.md` = durable product/interaction constraints;
  - `images/Bobbio_Design_*.png` = historical/supporting references;
- consolidate repeated general GUI/human-gate/anti-blocking/pre-user acceptance prose;
- keep Zotero authority/isolation, native Windows acceptance, knowledge model and iPad/Pencil-specific rules discoverable;
- use deeper canonical docs rather than deleting safety semantics.

### Lucerna — light edit

Keep distinct owners for:

- Windows release/tray lifecycle;
- live provider truth;
- matching regression;
- screenshot helper;
- Longleaf boundaries.

Normalize headings/order and exact duplication only.

### Mica — testing consolidation

Merge the repeated focused-test/full-E2E guidance into one ladder while preserving:

- real-failure reproduction;
- privacy-safe built-in diagnostics;
- authenticated account safety;
- typing hot-path invariant;
- final real long-conversation acceptance as manual, not automated authenticated regression.

### Asteria — substantial map conversion

Root should retain stable hard invariants/locators, while long operational mechanics live in canonical docs:

- fixed public URL must not be silently replaced;
- canonical black-box browser contract locator + essential invariant `可以自动操作页面；不能绕过页面`;
- GPT Work-before-human release gate;
- visual/self-QA/scientific-graph/generic-fix rules located through `prompts/AGENT_RULES.md`;
- tunnel/server/runtime command details moved to a canonical operations doc if no adequate current owner exists.

### SeminarArc — substantial map conversion with safety preservation

Root retains a short non-negotiable physical-device summary:

- Emulator-first;
- protected physical device is not a generic connected-test target;
- no automatic transport recovery/reset;
- explicit serial + pre/postflight for authorized physical writes;
- device-channel failure does not automatically block headless/Emulator work.

Detailed command bans, environment inventory and historical incident evidence stay in `docs/DEVICE_TESTING.md` / an environment doc after uniqueness is verified.

### CUHK Date — no root creation for symmetry

Current prototype `AGENTS.md` is short/coherent. Do not create root policy solely to match the scaffold.

## 10. AGENTS style target

This is a common editing style, not a common rule set:

- root = map + hard project invariants;
- deeper docs = long procedures, volatile environment details, historical evidence;
- one concept per bullet;
- explicit canonical locators;
- preserve exact path/enum/command identifiers;
- no bulk language translation solely for uniformity;
- no Bridge-managed block manual forks;
- no deletion purely to hit line/byte targets;
- project-specific safety outranks cosmetic consistency.

## 11. Conflict-resolution order during cleanup

If two statements inside the same repo conflict, do not choose by prose preference:

1. current user instruction / frozen task;
2. current branch source and explicitly current/canonical docs;
3. newer accepted milestone/ADR/policy that explicitly supersedes the older wording;
4. runtime/test evidence;
5. unresolved ambiguity => preserve both and report `EVIDENCE_NEEDED` rather than silently deleting one.

## 12. Capability / acceptance gates for 057

Because 057 now changes Bridge Kit's future repo-initialization behavior, success cannot be judged only by "the files look cleaner".

### H1 — Semantic preservation

Every pre-edit hard rule/invariant in each modified repo is accounted for. Deleted/moved text has a canonical surviving owner.

### H2 — No internal contradiction

Final root + delegated instruction surfaces no longer contain known competing authorities or user-action/test semantics.

### H3 — Discoverability

A new agent starting from root can find current design/safety/testing authorities without reading historical incident logs.

### H4 — Managed-block integrity

Bridge-managed content is updated only from canonical Bridge source; project-specific cleanup never forks generated blocks.

### H5 — Context quality

Bobbio/Asteria/SeminarArc/Mica report before/after root bytes/lines and show meaningful reduction/reorganization where duplication/volatile detail existed. No numeric target can override safety preservation.

### H6 — Repo-specific regression

Each repo retains its unique critical protections: Zotero/native/Bobbio design authority; Lucerna Windows/live provider/Longleaf; Mica account/typing/test ladder; Asteria fixed public URL/browser/visual acceptance; SeminarArc physical-device safety; CUHK prototype semantics.

### H7 — Fresh Bridge scaffold normal entry

On a clean temporary repo with no `AGENTS.md`, the real Bridge init path creates:

- a root AGENTS from the canonical scaffold;
- exactly one managed Bridge block;
- a locator to `prompts/AGENT_RULES.md`;
- no fabricated project invariants;
- a concise project-owned structure suitable for later additions.

This must be tested through the normal CLI/init path, not only by rendering the template helper.

### H8 — Existing-repo should-not-change

On a fixture with a custom existing root `AGENTS.md`, normal/force init must preserve project-owned prose and only install/update the managed Bridge block. It must not silently migrate/reformat to the new scaffold.

### H9 — No Lite duplication

The generated fresh root does not copy the Lite baseline or create a second execution-policy authority. `prompts/AGENT_RULES.md` remains its owner.

These gates prove different behaviors; do not add further gate numbers unless Critic finds a distinct unprotected failure.

## 13. Alternatives considered

### A. Only clean existing repos; no reusable template

Simplest immediate fix but guarantees future projects can drift back into the same accumulation pattern. Rejected as incomplete after the user's explicit request.

### B. Put all project rules into `prompts/AGENT_RULES.md`

Would blur generic handoff rules with project-specific product/environment/safety facts and make root discovery weaker. Rejected.

### C. Auto-rewrite every existing AGENTS whenever Bridge Kit updates

Would be dangerous, destroy project-specific ownership, and make Bridge Kit a repo-policy migration engine. Rejected.

### D. Reusable structural scaffold only for fresh repos + explicit migration tasks for existing repos

Chosen. It solves future maintainability while keeping existing repos fail-safe and user-owned.

## 14. Red Team

### Too weak

- template exists but real `ai-bridge init` never consumes it;
- fresh root duplicates Lite rules;
- existing repos still retain internal conflicts after cosmetic edits;
- moved safety rules become undiscoverable;
- Bobbio still has Figma/images dual authority;
- Mica/Asteria/SeminarArc remain manuals with new headings only.

### Too heavy

- scaffold becomes another giant universal AGENTS;
- Bridge Kit starts auto-migrating user-owned root files;
- every repo gets empty sections and generic checklists;
- 057 creates a second workflow/control system;
- existing project docs are rewritten merely to match section names;
- the cleanup triggers product/runtime changes unrelated to instructions.

## 15. Relationship back to 056

057 should finish before 056 implementation because the user explicitly wants instruction surfaces cleaned first.

However **056 is not redesigned** by default.

After 057 implementation/integration, Planner performs a bounded 056 source-drift revalidation:

1. reread current Bridge Kit main, Bobbio `develop`, and 056 v0.2 package;
2. confirm v6 responsibilities, W1–W5/F-A–F-C/G1–G8 are unchanged;
3. reconcile any mechanical overlap:
   - Bridge version/source ref if 057 consumed the previously planned `0.8.3` slot;
   - Bobbio Figma locator if 057 already implemented it;
   - new Bridge root scaffold ownership vs 056 Lite distribution;
4. remove duplicate 056 work already completed by 057 rather than performing it twice;
5. update Plan/Goal/Kickoff version/locators if needed and send that narrow amendment to Critic.

Only if 057 changes a frozen 056 assumption or owner does Planner reopen architecture. Ordinary version/ref/"already completed by 057" adjustments are not a new v6 design round.

## 16. Current boundary

This v2 proposal authorizes nothing by itself.

No product repo AGENTS is modified here. No Bridge Kit production source is modified here. No branch/worktree is created. No 056 Executor starts.

`NEXT_HANDOFF = CRITIC`
