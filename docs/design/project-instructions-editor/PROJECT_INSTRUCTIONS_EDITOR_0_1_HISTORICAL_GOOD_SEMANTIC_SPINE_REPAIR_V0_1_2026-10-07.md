# Project Instructions Editor 0.1 — Historical-Good Semantic Spine Repair

Date: 2026-10-07

Status: bounded pre-release repair; no new Critic round

Branch:

```text
work/project-instructions-editor--0.1-closure
```

Current source before this repair:

```text
9cdbe8ed712caf3a3a90592cd09c61ac146d9b02
```

Standalone Skill version remains `0.1`.

## 1. Why this repair exists

The latest real Server+VPS ChatGPT Web acceptance is improved over the prior
13-section failure, but it is still not releasable.

The remaining failure is not “a few English words were not translated.” It is a
structural editor failure:

1. the replacement still follows too much of the source/live-setting section
   scaffolding instead of rebuilding a compact long-lived Project contract;
2. a source-owned mutable platform enumeration was kept as durable Project
   state;
3. a broad production-mutation authorization boundary was lost while a narrower
   client-network authorization rule survived;
4. user-facing answer rules remain split across multiple overlapping sections;
5. ordinary English source labels still influence the vocabulary and headings
   of the durable setting.

This is within PIE 0.1 responsibility because it concerns the quality and
semantic fidelity of the Project setting being edited now. It does not reopen
the unsupported future cross-turn reader-layer guarantee.

## 2. Historical evidence: what actually worked before

Do not guess from recent C11-era source. Read the immutable C6 history directly:

```text
C6 source commit:
6ddab9029bbd96a21d7e5bf0317f7674c66cd909

Historical evidence at that commit:
results/project-instructions-editor--standalone-skill-implementation/SERVER_VPS_R6_UNCOACHED_REGRESSION.md
results/project-instructions-editor--standalone-skill-implementation/C6_IMPLEMENTATION_CRITIC_REVIEW.md
```

C6 is **not** a release candidate to restore wholesale. Its final review was
REVISE because two ordinary English labels still leaked. However, its structural
behavior is a useful development reference.

The C6 uncoached Server+VPS replacement did several things correctly:

- rejected a false no-op;
- removed the copied volatile client/device list;
- replaced that list with a current-source bridge;
- retained exact repository identities;
- retained the broad rule that real accounts, production tunnels, system
  services, remote resources, and cross-device proxy state are not modified
  unless the user explicitly authorizes the concrete object/purpose/scope;
- kept privacy and current-evidence/fail-closed semantics;
- rendered the durable setting as a small number of user-meaningful paragraphs
  rather than mirroring every source heading.

The user-confirmed earlier “good” real setting had the same higher-level shape.
It organized the Project around roughly these semantic families:

1. ownership and routing;
2. user-facing answer behavior;
3. proxy-client delivery integrity and server-first changes;
4. live client-network state plus user action;
5. automated validation;
6. canonical source plus production mutation control;
7. fail-closed and redundancy;
8. completeness and secrets;
9. production closure reporting.

These nine items are a **behavioral reference only**, not a required section
count or template.

The important common property of C6 and the user-confirmed good version is:

> source clauses were digested into a smaller semantic spine before the final
> Project setting was written.

## 3. What changed after the good behavior

The history shows two different failure phases.

### Phase A — C6 was structurally useful but had a narrow language leak

C6 already had:

- live-setting precedence;
- no-op eligibility;
- volatile inventory -> source bridge;
- general production authorization preservation;
- a whole-candidate consistency check.

Its real remaining blocker was narrow: ordinary labels such as
`Project setting` and `secret value` were incorrectly self-exempted as exact
or contextual.

### Phase B — C7 through C11 over-focused on final language realization

Later rounds progressively strengthened exactness/token/final-pass behavior:

- C7 tightened exactness;
- C8 fixed protected-absence residue but still leaked an ordinary meta-label;
- C9 strengthened final replacement review but leaked `tunnel`;
- C10 actually consumed `chinese-prose` in the same turn but still lacked true
  stage separation;
- the C10-B3 probe showed true multi-call stage separation would be required for
  the advanced reader-layer guarantee;
- C11 then proved the simple core could not reliably own that advanced
  cross-turn/whole-reader guarantee.

Those failures remain preserved. Do not reintroduce their implementation class.

### Current regression — the new map is too flat

The current 0.1 repair correctly introduced a durable semantic map, but the map
is one level too shallow:

```text
input clause
-> decide direct / bridge / source-only / task-only / omit
-> draft
```

That still allows ten or twelve clauses with related meanings to survive as ten
or twelve independent Project rules.

It also lacks two explicit semantic protections:

- **scope dominance**: a broad authorization/safety boundary cannot be replaced
  by a narrower special-case boundary;
- **dynamic-set abstraction**: if a mutable set is canonically owned elsewhere,
  Project instructions retain the quantified coverage requirement and locator,
  not the current member list.

## 4. Repair mechanism: build a semantic spine, not only a clause map

Keep the existing durable semantic map, but make it two-level.

### Level 1 — atomic durable meanings

For each relevant live/current/source-supported rule, preserve the existing
semantic fields:

- meaning;
- current support;
- semantic owner;
- enforcement placement;
- volatility;
- authorization/safety/evidence force;
- disposition.

### Level 2 — semantic families

Before drafting, cluster atomic meanings into a smaller set of long-lived
families.

A family is defined by the combination of:

```text
governed actor/surface
+ trigger/phase
+ intended behavior or prohibition
+ authority/owner
+ failure consequence
```

Examples of generic families:

- ownership/routing;
- user delivery;
- mutable facts/current-source lookup;
- production mutation authorization;
- client-state mutation;
- validation/completeness;
- fail-closed/redundancy;
- secrets/privacy;
- closure reporting.

Do not reuse these as a fixed section template. The actual families must come
from the current setting.

### Core rule

```text
many source clauses
-> atomic meanings
-> semantic families
-> one primary durable home per meaning
-> final Project setting
```

Do not draft section-by-section from the source.

## 5. Structure is not a protected semantic invariant

Preserve semantics, not scaffolding.

The following are normally **not** protected merely because they exist in the
live setting or source:

- heading count;
- heading names;
- section order;
- repeated explanatory examples;
- duplicated rationale;
- audit labels;
- source terminology;
- grouping inherited from a repository document.

A preservation-sensitive replacement may therefore merge, reorder, or rename
sections when that is necessary to remove duplication or restore a compact
Project contract, provided all protected semantics remain.

This does not authorize a product redesign or an unrelated full rewrite.

## 6. Scope-dominance rule: broad boundaries cannot be swallowed by narrow ones

This closes the authorization regression in the latest real Server+VPS output.

When two rules overlap, compare their semantic scope.

If rule A governs a **superset** of actions/resources and rule B governs only a
subset, preserving B does not permit dropping A.

Example pattern:

```text
A: any production mutation requires explicit current-task authorization
B: client live-network state changes require explicit current-task authorization
```

B is a useful specialized rule, but it does not replace A.

During consolidation:

- retain the broad boundary once at the broadest correct home;
- retain a narrower rule only when it adds materially useful action-specific
  detail;
- never infer that a specialized allow/prohibit list weakens or replaces the
  general authorization boundary;
- preserve current-task explicit authorization semantics, not merely historical
  or standing authorization.

Apply the same principle to privacy, safety, evidence strength, completion
claims, and fail-closed rules.

## 7. Dynamic-set abstraction

This closes the hard-coded platform-list regression.

If a list/set has all of these properties:

- its membership may change over time;
- a current canonical source owns the membership;
- the Project only needs completeness/coverage, not the current members before
  lookup;

then do not retain the current enumeration as durable Project state.

Replace it semantically with:

```text
all currently supported <items> defined by <canonical source>
```

plus any lookup-before-action bridge needed for enforcement.

Keep a concrete enumeration only when at least one is true:

- the user explicitly declares the member set itself to be a durable constraint;
- the finite names are formal protocol/state/UI values whose exact set defines
  behavior;
- the members are required before source lookup for safety/routing/exact
  identity.

Therefore a current platform/device/client/route inventory is normally source
owned. A formal mode set such as exact protocol state values may remain exact
when the set itself is durable.

Do not special-case Android, Windows, macOS, iPadOS, Server+VPS, Clash, or any
current real inventory in production logic.

## 8. Merge by user consequence, not by nearby wording

The latest real output still split ordinary answer behavior across two adjacent
sections.

During semantic-family clustering, clauses belong together when they have the
same normal trigger and the same user consequence.

For example, rules saying:

- answer with the conclusion first;
- emphasize required action over audit fields;
- do not dump raw status fields;
- keep background/optional/history separate;

all govern the same normal user-delivery phase and should normally have one
primary home.

A production-closure report may remain separate because its trigger is
different: it applies only when formally closing a production task.

Likewise, ownership and production-change procedure may remain separate when
one answers “who owns this?” and the other answers “how may this be mutated?”

The goal is not minimum headings. The goal is no duplicated long-lived meaning.

## 9. Target-language realization happens before drafting family text

Do not return to C7–C11 token chasing.

For a Project whose current setting/user request calls for Chinese:

1. after semantic families are formed, choose natural Chinese names for ordinary
   concepts in each family;
2. treat source English labels as evidence, not as preferred vocabulary;
3. preserve formal/machine identities that require exact spelling;
4. then draft the family once in Chinese.

This is **pre-draft concept realization**, not a final Latin-token scan.

Do not:

- count English;
- use a blacklist;
- maintain a translation dictionary;
- demand a reason for every Latin token;
- add a Server+VPS term list.

A few isolated ordinary English terms remain a Clear Writing concern and do not
alone fail PIE 0.1. But systematic source-label vocabulary that shapes headings
and durable clauses means the family was not actually digested and remains a
PIE current-artifact failure.

## 10. Final structural reconciliation

Before delivery, reconcile the final candidate against the two-level semantic
spine.

Check:

1. every protected atomic meaning is still represented;
2. broader authorization/safety/evidence boundaries have not been narrowed by
   consolidation;
3. dynamic source-owned sets are abstracted rather than copied;
4. no meaning appears in multiple families without a real different trigger or
   consequence;
5. source headings/order did not become candidate structure merely by inertia;
6. unsupported/new durable rules are absent;
7. protected absence remains absent without tombstones;
8. exact identifiers remain exact;
9. current-language family wording is natural enough to show the source labels
   were digested;
10. candidate growth corresponds to real long-lived semantics.

This is a semantic/structural reconciliation, not an advanced reader-layer
finalizer.

## 11. Regression strategy

### Historical development replay A — C6

Use immutable C6 as a development reference:

```text
6ddab9029bbd96a21d7e5bf0317f7674c66cd909
results/project-instructions-editor--standalone-skill-implementation/SERVER_VPS_R6_UNCOACHED_REGRESSION.md
```

A successor does not have to copy C6 wording. It should preserve the successful
behavior:

- no false no-op;
- volatile inventory removed;
- source bridges retained;
- broad production authorization retained;
- compact durable output.

Do not reintroduce C6's internal mode label or its known ordinary-English leak.

### Structural development replay B — generic complex setting

Add a public-safe fixture/runtime case with:

- two canonical owners;
- a broad production authorization rule;
- a narrower client-network authorization rule;
- a mutable current platform/client list owned by a canonical source;
- two overlapping normal user-delivery sections;
- a separate formal closure-report trigger;
- one protected deleted rule;
- privacy/evidence/fail-closed rules;
- several ordinary English source labels;
- exact machine/repository/protocol identities.

The expected qualitative behavior is:

- broad authorization survives;
- narrow special case survives only if it adds detail;
- mutable list becomes quantified canonical-source coverage;
- overlapping user-delivery rules merge;
- formal closure trigger remains distinct if needed;
- protected absence stays absent;
- source-label structure is not mirrored;
- exact identities remain;
- no unsupported durable rules;
- target-language ordinary concepts are drafted naturally.

Do not assert exact section count, exact final wording, English ratio, or banned
tokens.

### Final evidence

The next real Server+VPS fresh-thread Web acceptance remains the only final
normal-entry behavior test for this repair.

## 12. Implementation boundaries

Allowed:

```text
skills/core/codex-system/project-instructions-editor/SKILL.md
skills/core/codex-system/project-instructions-editor/references/editor-contract.md
tests/test_project_instructions_editor_contract.py
tests/fixtures/project_instructions_editor/*
results/project-instructions-editor--standalone-skill-implementation/*
docs/skill-todos/project-instructions-editor.md
generated registry/catalog surfaces required by the normal generator
wrapper handoff/candidate metadata
```

Not allowed:

- Clear Writing production changes;
- writing-style version change;
- C12;
- sibling `chinese-prose` chain;
- external finalizer;
- MCP/API/hosting;
- Server+VPS-specific production branch;
- fixed 9-section template;
- restoration/cherry-pick of C6 source wholesale;
- unrelated Research Authoring / Presentations / workflow-core changes.

Standalone PIE remains `0.1`.

The live ChatGPT wrapper is currently `0.2.3`; if source changes, the next
wrapper candidate must be `0.2.4`.

## 13. Release decision

Do not release from static tests alone.

After implementation:

1. focused/static tests pass;
2. historical C6 development replay is not structurally worse;
3. generic complex structural replay passes qualitatively if a real runtime
   replay surface is available;
4. wrapper 0.2.4 candidate is built from the exact final source;
5. stop for one real Server+VPS fresh-thread acceptance.

Release only if that real output:

- no longer mirrors the 12/13-section bad structure;
- preserves the broad production authorization boundary;
- does not hard-code a mutable canonical-source-owned platform/client set;
- consolidates overlapping user-delivery rules;
- preserves all safety/privacy/evidence/exact-identity semantics;
- is structurally at least as mature as the user-confirmed earlier good version.

C11 reader-layer failure remains preserved and is not reclassified as PASS.
