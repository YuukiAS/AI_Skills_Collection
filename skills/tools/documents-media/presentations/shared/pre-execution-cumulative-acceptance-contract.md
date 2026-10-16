# Presentation Pre-Execution Cumulative Acceptance and Review Ownership Contract

Status: **CANONICAL / MUST READ BEFORE EXECUTION**  
Applies to: every non-trivial presentation creation, revision, recovery, and release-review task

This contract prevents the recurring failure in which one newly reported issue is fixed while earlier accepted requirements silently regress.

Presentation acceptance is cumulative.

---

## 1. Cumulative guard rule

Let:

- `G_t` = active acceptance guards in round `t`;
- `N_t` = new guards created by new feedback or a newly discovered failure class;
- `R_t` = guards explicitly retired or superseded by a named human/Planner decision.

Then:

\[
G_t = (G_{t-1} \setminus R_t) \cup N_t.
\]

A round may PASS only if every guard in `G_t` passes.

New feedback strengthens the standard. It does not replace the previous one.

---

## 2. Lifecycle

Allowed lifecycle states:

- `ACTIVE` — unresolved requirement;
- `RESOLVED_BUT_GUARDED` — fixed in the current artifact but permanently checked in later artifacts;
- `RENDER_PENDING` — Planner specification exists, but exact render evidence is still required;
- `RESOLVED_IN_RENDER` — exact candidate render was inspected and passed;
- `SUPERSEDED` — a later explicit decision replaces the requirement;
- `RETIRED_BY_PAGE_CHANGE` — explicit authority proves the historical object/page no longer exists and its teaching role is replaced;
- `RETIRED` — explicitly no longer applicable;
- `INSTRUCTOR_ONLY` / `SPEAKER_ONLY` — routed out of the audience artifact;
- `SOURCE_GAP_UNVERIFIABLE` — a counted historical item exists but cannot be individually recovered.

`RESOLVED_BUT_GUARDED` and `RESOLVED_IN_RENDER` are not equivalent to retired.

A later candidate that reintroduces one guarded defect fails even if it fixes all new feedback.

---

## 3. Mandatory pre-execution state

Before work starts, record:

```text
PREEXECUTION_CONTRACT_READ = YES
TASK_CLASSIFICATION = NEW_SMALL | NEW_MAJOR | MINOR_REVISION | MAJOR_REVISION | FAILED_VERSION_RECOVERY
CRITIC_REQUIRED = YES | NO
BASELINE_IDENTITY =
HISTORY_SCOPE =
CURRENT_FREEZE_LEVEL =
ACTIVE_GLOBAL_GUARDS =
RENDER_PENDING_GUARDS =
POSITIVE_VISUAL_ANCESTRY_READY = YES | NO
IN_SCOPE_PAGEIDS =
IN_SCOPE_COMPONENTS =
LOCKED_PAGEIDS =
LOCKED_COMPONENTS =
ROUND_ALLOWLIST =
USER_IS_FIRST_QA = NO
```

Implementation does not begin if this state is incomplete.

---

## 4. Review ownership

### Planner / ChatGPT Web

Owns meaning and specification:

- audience, purpose, storyline, page count;
- page jobs and required/forbidden objects;
- exact visible copy;
- audience boundary;
- semantic layout and archetypes;
- feedback lifecycle;
- positive/negative visual ancestry;
- locks and unlocks.

### Prebuild Critic

Owns independent specification review:

- source/history consumption;
- page count/sequence;
- content correctness and sufficiency;
- audience boundary;
- archetype suitability;
- ancestry completeness;
- Controller design.

A prebuild Critic cannot certify a future render.

### Codex Producer

Owns implementation and self-QA only.

### Fresh deterministic Auditor

Owns exact conformance, code/numerical fidelity, locks, history coverage, object preservation, artifact identity, and machine-checkable regression.

### Fresh rendered-artifact Auditor

Owns whole-page and whole-deck visual implementation review against the exact candidate.

### GPT Work

Owns final aesthetic, reader-effort, pedagogical, natural-language, and deck-rhythm review.

### User

Owns subjective preference, new human decisions, explicit locks, and final acceptance. The user is never routine QA.

---

## 5. Permanent failure-class ownership map

The following classes are cumulative. New classes may be appended; existing classes may not be silently dropped.

| Failure class | Planner / Critic | Codex Producer / Auditors | GPT Work |
|---|---|---|---|
| Title page overloaded with topic inventory | Keep title job narrow; separate overview | Exact-copy/object check | Grouping, restraint, hierarchy |
| Title page loses shell/navigation/footer/page number | Freeze shell and binding | Render every required shell element | Optical integration |
| Wrong course/tutorial identity | Freeze exact text | Exact-copy check | Secondary check |
| Presenter/date too small | Set hierarchy expectation | Rendered scale check | Final optical judgment |
| Title/subtitle visually detached | Freeze title-block relationship | Preserve geometry | Final composition |
| Section names abbreviated | Freeze full labels | Exact header/miniframe check | Legibility/rhythm |
| Header/miniframe/bookmark/navigation missing | Freeze shell | Every-page shell regression | Whole-deck shell quality |
| Footer/buttons/page number misaligned | Freeze component role | Shared-component geometry regression | Subtle optical alignment |
| Closing page loses shell | Freeze dedicated close + same shell | Explicit closing binding and consumer regression | Final closure quality |
| Question rule wrong/missing | Freeze paired Q/A grammar | Geometry regression on every consumer | Flow/emphasis |
| Answer rule missing or incomplete | Freeze one continuous answer where required | Ensure all answer text remains inside component | Readability |
| Answer fragmented merely to fit | Decide semantic block count | Component-role check | Natural flow |
| Large meaningless whitespace | Reject weak spec/missing content | Whole-slide scale/occupancy review | Semantic whitespace judgment |
| Result pushed far from evidence | Freeze proximity | Rendered proximity check | Page balance |
| Primary figure/table/formula tiny while space is empty | Set primary-object priority and scale expectation | Scale-floor and whole-slide review | Reader-effort judgment |
| Text shrunk below token floor | Freeze typography tokens | Hard fail page-local shrinking | Readability |
| Two columns used merely because space exists | Choose semantic relation | Enforce approved archetype | Reading-path judgment |
| Sequential derivation/Q-evidence-A split into columns | Require vertical sequence | Archetype check | Visual order |
| Peer columns misaligned | Define peer relationship | Anchor/baseline regression | Optical alignment |
| Context photo narrow/tall/distorted | Specify role/aspect | Crop/no-distortion check | Composition |
| Caption carries body explanation | Assign semantic roles | Role/adjacency check | Accessibility |
| Math variables written as words in figures | Freeze labels | Glyph/text scan | Secondary check |
| Residual plot lacks how-to-read explanation | Write interpretation | Required-object check | Evidence proximity |
| Dispersion value lacks meaning | Content responsibility | Copy/object check | Communication |
| NB2 lacks “2”, kappa, uncertainty, AIC context | Content responsibility | Required-object check | Density/sufficiency |
| Count/rate/offset compressed or unclear | Own teaching sequence and estimand | Protect page jobs/copy/order | Sequence readability |
| Multinomial log-ratio confused with probability | Statistical explanation | Equation/table/copy check | Derivation clarity |
| Random intercept reduced to “add u_i” | Explain mechanism/dependence | Required mechanism check | Student clarity |
| Wrong grouping variable | Semantic correctness | Exact model/object check | Secondary check |
| Conditional/marginal/heterogeneity disconnected | Content sufficiency | Required table/interpretation check | Visual grouping |
| Simulation lacks purpose/truth/rationale/repeated-fit logic | Content sufficiency | Preserve sequence/code/results | Sequence comprehension |
| Bayesian section becomes package workflow | Sequence/boundary | Forbid API inventory | Section coherence |
| Prior predictive lacks statistic/judgment/follow-through | Content | Required Q/A/evidence | Figure-answer proximity |
| MCMC motivation or chain/state/draw missing | Content | Sequence check | Section clarity |
| MH/Gibbs/augmentation/blocks/HMC/NUTS collapsed into labels | Decide mechanism depth | Protect required objects/pages | Reader effort |
| Why-not-NUTS not answered | Content | Decision-table/clarification check | Visibility/understanding |
| Diagnostics confuse MCSE/posterior SD/geometry/model fit | Statistical meaning | Exact diagnostic-role check | Proximity/layout |
| Posterior transform lacks draw-by-draw meaning | Statistical meaning | Exact content | Visual clarity |
| PPC lacks model-fit judgment | Interpretation | Required interpretation | Evidence adjacency |
| Code page has code but no result | Specify result role | Execute and show result | Code/result balance |
| Code/API inventory becomes teaching content | Audience boundary | Forbid plumbing | Engineering-looking page |
| Code blocks unequal/tiny/large lower void | Layout authority | Peer geometry/scale review | Readability |
| Output detached from producing code | Freeze pairing | Output-to-code adjacency | Visual relation |
| Curly quotes/broken/non-copyable code | Source fidelity | Deterministic PDF/code gate | Not primary |
| AI-like slogans/defensive “not X”/internal language | Natural copy | Forbidden-pattern/role check | Final naturalness |
| Visible prerequisite/object/file dependency narration | Forbid | Hard fail | Secondary catch |
| Assessment/HW/project exposes hidden rubric/scaffold | Audience boundary | Exact allowed-copy gate | Naturalness |
| Previously fixed defect returns | Retain guard lifecycle | Cumulative regression check | Final independent catch |
| Latest-version-only history reading | Full-history rule | Bundle coverage check | Not primary |
| Local repair rewrites unrelated pages | Allowlist/locks | Source/render diff | Affected rhythm only |
| Shared component repair breaks consumers | Dependency tracking | Revalidate all consumers | Optical consistency |
| Representative-page review claims global PASS | Forbid scope inflation | Review-scope gate | Full-deck/contact-sheet gate |
| New version silently drops old standard | Maintain cumulative set | Evaluate inherited guards | Same cumulative visual set |
| Producer self-review treated as final acceptance | Prohibit | Fresh Auditor required | Independent final gate |
| Good visual ancestor discarded while content survives | Freeze positive visual ancestry | Mandatory-object/ancestor diff | Judge preserved teaching value |
| Diagram deleted instead of repaired | Explicit retirement required | Missing protected-object hard fail | Final catch |
| Internal proof skipped because user does not want to see it | Planner/Controller must keep proof internal | Proof artifact/evidence gate | Not primary |
| Prebuild Critic PASS misrepresented as render PASS | Clarify stage scope | Release gate requires render evidence | Independent catch |
| Source/text checks replace image inspection | Require exact-render review | Page PNG/hash review rows | Whole-slide judgment |
| RENDER_PENDING rows never checked on final artifact | Maintain closure matrix | Exact-candidate row per item | Final guard replay |
| Widespread tiny-object plus large-void layout | Set scale/whitespace expectations | Whole-slide/contact-sheet fail | Global quality judgment |
| Suspicious numerical chart/trace not validated | Specify quantity/source | Underlying-variable/numerical validation | Secondary plausibility check |
| Render review not bound to exact candidate bytes | Require immutable candidate | Hash-bound evidence | Refuse stale review |
| All-page PASS without one row per page | Require full scope | Page-row count hard gate | Full-deck scope check |
| GPT Work review absent or not bound to final candidate | Require final gate | Evidence binding | No PASS |
| User is first to identify obvious full-deck defects | Workflow failure classification | Candidate rejected; strengthen upstream gate | Record missed classes |

---

## 6. Historical-feedback assimilation

Every raw item must map through:

```text
raw feedback
-> exact historical artifact/page
-> stable PageID/component
-> normalized requirement
-> requirement class
-> lifecycle/supersession
-> positive ancestor and negative example
-> Planner authority locator
-> verification owner
-> required evidence
-> current state
```

A count-only ledger is insufficient.

For major/recovery work, the Critic must verify the item-level matrix. For every production candidate, the rendered Auditor must verify every `RENDER_PENDING` item against the exact page image.

---

## 7. Non-regression conditions

A round cannot PASS unless:

```text
open_feedback_next is a strict subset of open_feedback_current
human_locked_pages_next is a superset of human_locked_pages_current
human_locked_components_next is a superset of human_locked_components_current
modified_ids are a subset of explicit_allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
positive_visual_object_losses = 0
```

A shared-component change revalidates every consumer without reopening semantic/copy locks.

---

## 8. Review evidence requirements

### Prebuild Critic

- exact authority commit;
- source/history counts;
- page-by-page specification rows;
- ancestry completeness;
- bounded amendments.

### Deterministic Auditor

- exact candidate identity;
- conformance matrix;
- numerical/code validation;
- lock/allowlist/history coverage;
- positive-object preservation.

### Rendered Auditor

- one row per page;
- one row per render-dependent historical item;
- per-page PNG hashes;
- contact-sheet review;
- whole-slide findings;
- exact candidate hash.

### GPT Work

- exact final artifact identity;
- all pages/contact sheet for major decks;
- cumulative visual guard set;
- final aesthetic/reader-effort verdict.

---

## 9. Severe workflow failure

Classify a candidate as a severe workflow failure when several of these occur:

- correct content but widespread unfinished composition;
- positive visual ancestors lost;
- diagrams/tables/figures deleted instead of repaired;
- multiple historical visual guards visibly recur;
- numerical figure plausibility is unverified;
- all-page review is claimed without image-bound evidence;
- the user is the first person to identify obvious full-deck defects.

Consequence:

```text
CANDIDATE = HUMAN_REJECTED
MINOR_PATCH = FORBIDDEN
RETURN_TO = POSITIVE_ANCESTRY + RENDER_ACCEPTANCE + UPSTREAM_GATE_REPAIR
```

---

## 10. Completion rule

A presentation is ready for user review only when:

- required Critic PASS exists;
- Planner freezes are intact;
- internal proofs passed;
- deterministic Auditor passed;
- rendered Auditor reviewed every required page/item;
- all mandatory render-dependent guards are resolved on the exact candidate;
- positive visual ancestry is preserved or explicitly retired;
- GPT Work passed where required;
- all inherited guards pass;
- all prior locks remain intact;
- artifact identity and reproducibility pass.

A file existing, compiling, or containing the right words is never sufficient.