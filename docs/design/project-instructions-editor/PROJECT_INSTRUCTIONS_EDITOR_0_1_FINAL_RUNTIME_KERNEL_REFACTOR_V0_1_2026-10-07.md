# Project Instructions Editor 0.1 — Final Runtime Kernel Refactor

Date: 2026-10-07

Status: final bounded simple-core repair; user explicitly declined another Critic round

Branch:

```text
work/project-instructions-editor--0.1-closure
```

Current source before refactor:

```text
b296fe64437f6a0f15a9d91c3881d2cb54db0ec0
```

Standalone Skill version remains `0.1`.

## 1. Decision

One more simple-core repair is technically justified, but only as a **subtractive
runtime-kernel refactor**.

Do not add another layer of reminders to the current Skill.

The two latest real ChatGPT Web Server+VPS failures show that the current source
contains the right concepts but the normal-entry generation path still executes
the wrong editing strategy:

```text
user asks for bounded review
-> model interprets bounded as small textual patch
-> old section scaffold survives
-> only locally named defects are edited
-> global dynamic-set / scope-dominance rules are not applied consistently
-> model may opportunistically add “useful” best-practice detail
```

This is different from C7-C11.

C7-C11 showed that repeated final-language self-checks cannot reliably provide
an advanced cross-turn reader layer.

The current failure is earlier: candidate construction itself is wrong.

Therefore the final repair should change candidate construction, not final
polishing.

## 2. Two real failures to absorb

### Failure A — flat consolidation

The first post-C11 Server+VPS attempt improved semantic preservation but expanded
into a long, repetitive source-shaped setting.

The repair added a durable meaning map and surface-consolidation rules.

### Failure B — semantic spine present in source but not controlling rendering

The second real attempt still reused nearly the same section scaffold.

It did improve one dynamic-coverage clause, but:

- a mutable platform enumeration survived elsewhere in the candidate;
- overlapping normal user-delivery sections remained separate;
- the model treated section reorganization as “surface optimization” and refused
  to perform it;
- the model proposed new authentication-secret examples based on contextual
  usefulness rather than current durable semantic authority;
- a broad historical authorization rule was at risk of being judged against
  history instead of the current live baseline.

The lesson is not “add more semantic-spine checks.”

The lesson is that PIE needs an explicit distinction between **semantic mutation
radius** and **surface reconstruction radius**.

## 3. Core distinction: bounded semantics != bounded text edits

Introduce two independent concepts.

### Semantic mutation radius

Which long-lived meanings may actually change.

For preservation-sensitive editing, this is bounded by:

- current live setting;
- current user request;
- current canonical facts only where the current task legitimately needs them
  to resolve an existing rule, owner, locator, or explicitly requested sync;
- necessary lookup-before-action bridges.

A bounded edit means the semantic mutation radius is small.

### Surface reconstruction radius

How much wording, grouping, heading structure, and ordering may be regenerated
to express the allowed semantics cleanly.

When the user requests a complete replacement, or when duplicated/source-shaped
structure is itself a material defect, the surface reconstruction radius may be
global even while semantic mutation remains bounded.

This is the key correction.

A complete replacement must not use the live setting as a paragraph-by-paragraph
editing scaffold merely because the semantic edit is bounded.

Instead:

```text
live setting
-> extract allowed durable meanings
-> normalize
-> regroup
-> render a fresh complete candidate
-> compare candidate back to live meanings
```

“Bounded edit” protects meaning. It does not protect obsolete section layout.

## 4. Closed-world durable meaning set

For preservation-sensitive review, build an internal **Allowed Durable Meaning
Set** before drafting.

The allowed set contains only:

1. durable meanings already present in the live setting;
2. explicit additions, deletions, or corrections in the current user request;
3. current canonical-source facts needed to resolve an already in-scope owner,
   locator, dynamic fact, or explicitly requested synchronization;
4. the minimum Project-resident bridge needed so future work performs the
   required lookup before action.

Everything else is non-authoritative for adding durable content.

In particular, these cannot independently add a new long-lived rule, exception,
category, example list, or hardening clause:

- old candidates;
- historical generated settings;
- chat memory;
- prior incidents;
- model knowledge;
- “best practice”;
- source examples outside the current synchronization need;
- an adjacent topic that happened to appear in past Project work.

History may:

- protect an explicit deletion/rejection;
- clarify the force/status of a live rule;
- confirm a current user decision;

but historical-only absent content remains absent.

### No opportunistic hardening

A model-generated “this would also be safer/more complete” observation does not
enter the replacement automatically.

If it is not supported by the Allowed Durable Meaning Set:

- omit it from the replacement;
- normally do not mention it unless the user explicitly asked for broader
  product-policy recommendations.

This prevents the authentication/2FA example expansion observed in the latest
real attempt.

### Examples are semantic content too

Adding examples can narrow, broaden, or fossilize a rule.

Therefore a new concrete example list requires the same authority as a new
durable rule.

A broad existing rule such as “do not expose credentials or secrets” should not
be expanded with an opportunistic list of credential types unless that list is
itself currently supported and useful as a durable constraint.

## 5. Short mandatory runtime kernel

Refactor `SKILL.md` so the normal complex-edit path is dominated by one short
kernel near the top.

Detailed rationale belongs in `references/editor-contract.md`.

For preservation-sensitive complete replacement, execute this order:

### K1 — Freeze allowed meaning

Build the Allowed Durable Meaning Set.

Do not draft replacement prose yet.

### K2 — Normalize each meaning

For each allowed meaning, determine only what is needed for rendering:

- governed surface/object;
- trigger;
- required behavior/prohibition;
- owner/authority;
- breadth/scope;
- volatility;
- failure consequence;
- exact identifiers;
- direct rule / lookup bridge / source-only / task-only / omit.

### K3 — Form semantic families

Merge meanings that have the same practical trigger and consequence.

Do not inherit section names/order from the live setting.

### K4 — Apply global transforms before prose

Apply to the entire normalized set, not section-by-section:

- duplicate merge;
- scope dominance;
- dynamic-set abstraction;
- volatile-detail relocation;
- protected absence;
- exact-identity preservation.

A transformation is incomplete if an equivalent stale form survives elsewhere
in the candidate.

### K5 — Render fresh candidate

If a complete replacement is requested, render from semantic families from
scratch.

Do not patch the old text section-by-section.

For Chinese-facing settings, choose natural Chinese ordinary concepts at this
stage. Exact machine/formal identifiers remain exact.

### K6 — Bidirectional reconciliation

Perform two independent checks.

#### Coverage direction

Every allowed live/current meaning that should remain Project-effective must be:

- represented once in the candidate; or
- safely represented by a direct bridge/locator; or
- explicitly removed by the current user.

#### Provenance direction

Every durable rule, exception, concrete example, enumeration, or requirement in
the candidate must map back to one item in the Allowed Durable Meaning Set.

If it cannot be mapped, remove it.

Then verify:

- no broad live boundary was narrowed;
- no mutable source-owned member list remains anywhere;
- no duplicate meaning survives under another heading;
- no history-only rule or tombstone was introduced;
- no unsupported “helpful” hardening was introduced.

### K7 — Deliver proportionally

Normal user output:

- short conclusion;
- clean bounded edit or complete replacement;
- only the few important changes.

Do not expose K1-K6, internal mode labels, semantic tables, provenance tables, or
audit machinery unless formal audit evidence is requested.

## 6. Scope dominance must use the live allowed set, not historical nostalgia

The previous acceptance discussion exposed a possible evaluator mistake.

Scope dominance means:

> when both a broader and narrower current valid meaning are in the Allowed
> Durable Meaning Set, the narrower rule cannot silently replace the broader one.

It does **not** mean:

> restore a broader rule merely because an older good candidate or historical
> setting once contained it.

Therefore:

- live broad rule + live narrow rule -> preserve the broad boundary;
- live narrow rule + historical-only broad rule -> protected absence wins;
- current user explicitly re-adopts broad rule -> it becomes allowed;
- current canonical synchronization explicitly supports and authorizes the broad
  rule -> evaluate within that sync scope.

This keeps scope dominance compatible with protected absence.

## 7. Dynamic-set abstraction must be global

Once an atomic meaning is classified as a mutable source-owned set, record that
fact at the normalized meaning level.

During K4/K6, search conceptually across the whole candidate for equivalent
enumerations.

The candidate fails if it says both:

- “use the current canonical supported set”; and
- elsewhere freezes the current members of that same set.

Do not implement this with literal platform-name matching.

The rule is semantic:

```text
same mutable set identity
+ canonical owner exists
+ members not needed before lookup
=> no current member enumeration anywhere in durable candidate
```

Formal finite state sets and explicit durable user constraints remain allowed.

## 8. Structure reconstruction must be real

When duplicate headings or repeated rules are material defects, the replacement
must be structurally rebuilt.

Do not treat these as protected:

- existing heading count;
- heading names;
- source section order;
- duplicated user-response sections;
- repeated rationale;
- historical grouping.

For example, three sections that all govern ordinary answer presentation may
collapse into one family, while a formal task-closure report remains separate
because its trigger differs.

No fixed number of sections is required.

The acceptance question is:

> does each final section correspond to a genuinely distinct long-lived family?

not:

> did the candidate preserve the old table of contents?

## 9. Reduce production prompt entropy

The current `SKILL.md` has accumulated several repair eras.

This final refactor should **replace and consolidate**, not append.

Requirements:

- put K1-K7 before long explanatory material;
- remove duplicated instructions that restate the same candidate-construction
  rule;
- move historical rationale and edge-case exposition to
  `references/editor-contract.md`;
- keep only runtime-critical invariants in `SKILL.md`;
- preserve exact product boundary, modes, no-op, protected absence, authorization,
  privacy, evidence, exact identities, degradation, and runtime-boundary
  semantics;
- do not reintroduce C7-C11 token-by-token language machinery.

A successful implementation should normally make the production `SKILL.md`
shorter or materially denser than `b296fe64...`.

Do not use a hard character target. If the production Skill grows materially,
the Executor must explain why the refactor did not become another additive
patch.

## 10. Tests

Static tests must validate contract structure, not exact output wording.

Add/adjust generic fixtures for:

### Case A — semantic bounded / surface global

Input:

- live setting has several duplicated sections;
- current request asks for only one or two semantic changes but wants a complete
  replacement.

Expected:

- semantic changes remain bounded;
- final surface may be globally regrouped;
- source heading structure is not protected.

### Case B — closed-world / no opportunistic addition

Input:

- live setting has a broad secret/privacy rule;
- history mentions a separate authentication incident or credential type;
- current request is ordinary Project-instruction review.

Expected:

- historical incident does not create a new durable rule or example list;
- existing privacy meaning remains preserved.

### Case C — global dynamic-set abstraction

Input:

- same mutable set appears in two different live sections;
- canonical source owns membership.

Expected:

- both enumerations disappear from the conceptual candidate;
- one current-source coverage/lookup meaning remains.

### Case D — scope dominance compatible with protected absence

Cover both:

1. live broad + live narrow -> broad survives;
2. historical-only broad + live narrow -> broad is not resurrected.

Do not hard-code Server+VPS, platform names, TOTP, or exact final section count.

## 11. Historical regression use

Use C6 only as development behavior evidence:

```text
6ddab9029bbd96a21d7e5bf0317f7674c66cd909
```

Useful C6 behavior:

- false no-op avoided;
- mutable inventory moved to source bridge;
- output compact;
- current authorization/privacy/evidence semantics preserved.

Do not restore:

- C6's internal mode-label output;
- C6's later token-oriented language mechanism;
- any historical-only rule absent from the current live baseline.

C7-C11 remain negative evidence. They must not be converted into runtime token
checks.

## 12. Wrapper and validation

Standalone Skill version remains:

```text
0.1
```

Current live personal wrapper is:

```text
0.2.4
```

If production source changes, build wrapper candidate:

```text
0.2.5
```

Do not mutate the live wrapper until repository-side source/static validation is
complete.

Run focused tests and ordinary repository validation required by current repo
rules.

Static tests are not behavior PASS.

If no authorized standalone runtime replay harness exists, do not fabricate one
for this repair.

## 13. One-more-attempt stop rule

This is the final simple-core candidate-construction repair.

After source validation and wrapper update, run **one** fresh real Server+VPS Web
acceptance.

If that next first complete response still materially does any of the following:

- copies the old section scaffold instead of rebuilding from families;
- leaves a mutable source-owned set enumerated elsewhere after claiming to
  abstract it;
- narrows a current broad boundary to a special case;
- adds unsupported history/best-practice-derived durable rules or example lists;
- fails bidirectional semantic traceability;

then stop prompt-layer refinement.

Do not create another synonym repair, C12-like round, token rule, or larger
checklist.

The truthful product conclusion would then be that PIE 0.1 simple-core is
reliable for smaller bounded Project edits but not reliable enough to promise
complex preservation-sensitive full-setting restructuring in ordinary ChatGPT
Web. Scope/release claims must be narrowed accordingly.

This stop rule prevents infinite goalpost movement.

C11 reader-layer failure remains preserved regardless of the outcome.
