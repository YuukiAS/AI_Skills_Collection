# Presentation Pre-Execution Cumulative Acceptance and Review Ownership Contract

Status: **CANONICAL / MUST READ BEFORE EXECUTION**  
Applies to: every non-trivial presentation creation, revision, recovery, or release-review task  
Primary evidence: repeated real-world failures and repairs across STAT5060 Tutorial 01 and other presentation workflows

This file is the mandatory first-read contract before presentation execution begins.

Its purpose is not to add another layer of bureaucracy. It exists to prevent the exact failure mode that repeatedly caused wasted rounds:

> one problem is fixed, another previously fixed problem silently returns, and the user becomes the first person to notice.

Every presentation task must therefore begin by reading this contract, classifying the task, identifying the current freeze state, and determining which historical guards and review layers apply.

---

## 1. Non-negotiable cumulative principle

Presentation acceptance is cumulative.

A later version inherits every still-active requirement from all earlier accepted and rejected rounds. New feedback strengthens the acceptance standard; it does not replace the previous one.

Let:

- \(G_t\) = active acceptance guards in round \(t\);
- \(N_t\) = new guards created by new feedback or a newly discovered failure class;
- \(R_t\) = guards explicitly retired or superseded by a named human/Planner decision.

Then:

\[
G_t = (G_{t-1} \setminus R_t) \cup N_t.
\]

A round may PASS only if **every guard in \(G_t\)** passes.

The default lifecycle is:

- `ACTIVE` — unresolved requirement;
- `RESOLVED_BUT_GUARDED` — the current artifact fixed it, but every later artifact must still prove it did not recur;
- `SUPERSEDED` — a later explicit human/Planner decision replaces it;
- `RETIRED` — explicitly no longer applicable;
- `INSTRUCTOR_ONLY` / `SPEAKER_ONLY` — relevant to preparation but not automatically visible to the audience.

`RESOLVED_BUT_GUARDED` is not equivalent to retired.

A later candidate that reintroduces one closed guard is a regression and cannot PASS merely because the current round's new feedback was fixed.

---

## 2. Mandatory pre-execution acknowledgment

Before any non-trivial presentation execution starts, the Planner/Controller must be able to state:

```text
PREEXECUTION_CONTRACT_READ = YES
TASK_CLASSIFICATION = NEW_SMALL | NEW_MAJOR | MINOR_REVISION | MAJOR_REVISION | FAILED_VERSION_RECOVERY
CRITIC_REQUIRED = YES | NO
BASELINE_IDENTITY =
HISTORY_SCOPE =
CURRENT_FREEZE_LEVEL =
ACTIVE_GLOBAL_GUARDS =
IN_SCOPE_PAGEIDS =
IN_SCOPE_COMPONENTS =
LOCKED_PAGEIDS =
LOCKED_COMPONENTS =
ROUND_ALLOWLIST =
USER_IS_FIRST_QA = NO
```

If these cannot be determined, implementation does not start.

For a major revision or recovery, `HISTORY_SCOPE` means the complete raw feedback history plus the actual rendered lineage and direct human decisions.

For a minor revision, `HISTORY_SCOPE` means current feedback + exact reviewer-seen baseline + active global guards + complete affected-page/component history + current locks/dependencies.

---

## 3. Task routing and Critic policy

### 3.1 New small / low-risk deck

A small deck may proceed directly from Planner authority to production when:

- source and audience are clear;
- the visual system is already established;
- no high-risk teaching/scientific meaning is being introduced;
- no complex historical feedback exists.

A separate prebuild Critic is optional.

### 3.2 New major / high-risk deck

A prebuild Critic is required when the deck is substantial, high-stakes, teaching-heavy, scientific, template-defining, or likely to require non-trivial content/layout judgments.

### 3.3 Minor revision

A separate Critic may be skipped only when **all** are true:

- page count unchanged;
- section order unchanged;
- no page job changes;
- no scientific/statistical/pedagogical claim changes;
- no shell/header/footer/navigation/template redesign;
- no new archetype, page split, or page merge;
- copy changes are local and source-supported;
- scope is normally at most three pages and one already-defined shared component;
- no closed historical guard has recurred;
- no shared-root failure is suspected.

ChatGPT Planner may then freeze the bounded allowlist directly.

### 3.4 Major revision

A fresh prebuild Critic is mandatory when any of these occurs:

- page count, section order, narrative, or page jobs change;
- broad visible-copy/content changes affect multiple pages;
- title/header/footer/navigation/template/shared shell changes;
- new layout archetypes, major figure systems, page split or merge;
- scientific/statistical/pedagogical/assessment meaning changes;
- repeated regression suggests the current authority may be wrong;
- the user asks to rethink, rebuild, overhaul, or reread all history.

If uncertain, classify as major.

### 3.5 Failed-version recovery

Recovery is always major.

It requires:

- full raw history reread;
- exact counts;
- direct human decisions;
- actual rendered lineage;
- lifecycle/supersession resolution;
- positive and rejected visual/content baselines;
- new Planner authority;
- prebuild Critic before implementation.

### 3.6 Critic consequence

For major/recovery work:

```text
Planner freezes specification
-> fresh read-only Critic
-> PASS or bounded REVISE
```

If `REVISE`, only Planner authority is amended. No slide implementation begins.

A major Planner amendment after Critic review requires another fresh Critic pass.

---

## 4. Freeze ladder

Every substantial presentation proceeds through explicit freezes. Later stages cannot silently reopen earlier ones.

### F0 — source / baseline / history freeze

Freeze:

- source/evidence set;
- exact reviewer-seen baseline;
- artifact family/version identity;
- historical feedback corpus;
- positive/negative baselines;
- current page/component locks.

### F1 — narrative / page-job freeze

Freeze:

- section sequence;
- page count or bounded range;
- stable PageIDs;
- one job per PageID;
- primary scientific/teaching/decision object;
- required and forbidden objects;
- source anchors;
- transitions;
- audience vs speaker/instructor/internal boundary.

### F2 — visible-copy freeze

Freeze every audience-visible string:

- title/subtitle;
- prose/bullets;
- equations and labels;
- Question/Answer;
- table cells;
- figure labels;
- code shown;
- captions and sources;
- administrative instructions.

### F3 — layout-semantics freeze

Freeze:

- semantic relationship;
- reading path;
- approved archetype;
- primary-object priority;
- allowed fallback;
- forbidden fallback;
- shared-component bindings.

### F4 — shared-component freeze

After real-content proof and internal review, lock:

- title shell;
- header/navigation;
- footer/source/buttons/page number;
- typography;
- Question/Answer grammar;
- table/code/caption/figure grammar;
- closing shell.

### F5 — golden-page composition freeze

Lock representative density, scale, composition, and archetype behavior on high-risk real pages.

### F6 — full-candidate freeze

Freeze exact source, commit, PDF/PPTX, page renders, hashes, page map, and review bundle.

### F7 — human locks

Explicit user acceptance creates a page/component lock until an explicit named unlock states reason and scope.

---

## 5. Role ownership: who decides, who verifies

The same issue may have different owners at different stages.

### 5.1 ChatGPT Web / Planner

Owns **meaning and specification**:

- audience, purpose, storyline, page count;
- page jobs and required objects;
- content sufficiency;
- exact visible copy;
- student/audience vs instructor/speaker boundary;
- layout semantic relationship;
- page archetype selection;
- feedback interpretation/lifecycle;
- locks/unlocks;
- Critic routing.

Planner does not implement slide source.

### 5.2 Prebuild Critic

Owns **independent specification review before major production**:

- prove source/history was actually consumed;
- independently judge page count and sequence;
- review every planned page;
- verify content sufficiency;
- verify audience boundary;
- verify layout/archetype suitability;
- verify historical guard coverage;
- audit the Codex Controller/review route.

Critic does not implement fixes.

### 5.3 Codex Producer

Owns **implementation**:

- typesetting;
- geometry within approved archetype;
- line breaks, widths, spacing, alignment;
- approved figure/asset generation;
- build/render/export;
- deterministic smoke checks;
- proof-carrying patch manifest;
- ordinary repair inside frozen scope.

Producer does not decide what to teach, claim, omit, merge, split, or rewrite.

### 5.4 Fresh Codex deterministic Auditor

Owns **objective candidate conformance**:

- exact copy;
- page count/order/PageIDs;
- history/guard coverage;
- locks and allowlist;
- component bindings/consumers;
- shell presence and consistency;
- code execution/copyability;
- math glyphs;
- figure labels;
- PDF structure;
- versioning/artifact identity;
- forbidden strings/roles;
- recurrence of closed deterministic guards.

It is read-only and independent from Producer.

### 5.5 Fresh rendered-artifact Reviewer

Owns **rendered whole-page implementation review** before GPT Work:

- hierarchy;
- reading path;
- object scale;
- whitespace;
- semantic proximity;
- shared-component optical consistency;
- rendered Q/A geometry;
- table/code/figure readability;
- page/deck rhythm;
- obvious audience-language problems.

It is still part of the Codex-controlled internal QA loop and should eliminate routine defects before GPT Work.

### 5.6 GPT Work

Owns the **final aesthetic / reader-effort / communication gate**:

- all-page or scoped-delta visual quality according to task class;
- whole-deck rhythm;
- whether the audience can actually follow the page;
- whether whitespace feels deliberate;
- whether evidence and interpretation are visually connected;
- whether student/audience language feels natural;
- whether a page is visually/pedagogically convincing rather than merely mechanically compliant;
- recurrence of historical visual failure classes.

GPT Work does not implement fixes and does not override deterministic or statistical failures.

### 5.7 User

Owns only:

- truly subjective preference between already acceptable alternatives;
- explicit page/component lock;
- final subjective acceptance;
- new semantic/course/research decisions not supported by frozen authority.

The user is never routine QA.

---

## 6. Historical failure classes and permanent review ownership

The following failure classes were repeatedly exposed by real human annotations. They are cumulative acceptance classes, not one-off project notes.

| Failure class | Planner / Critic responsibility | Codex Producer/Auditor responsibility | GPT Work responsibility |
|---|---|---|---|
| Title page overloaded with topic inventory | Planner keeps title job narrow; Critic verifies title vs overview split | Auditor verifies only approved title objects appear | Judge grouping, restraint, title hierarchy |
| Title page loses established shell/navigation/footer/page number | Planner freezes shell requirement; Critic catches contradictory spec | Producer implements shared shell; Auditor checks required elements on rendered page | Judge optical integration and professional quality |
| Wrong identity text such as duplicated/numbered tutorial labels | Planner freezes exact identity | Auditor exact-copy check | Secondary visual check only |
| Presenter/date too small or visually detached | Critic flags hierarchy risk | Rendered Reviewer checks readable scale | Final optical judgment |
| Section names abbreviated to save space | Planner freezes full labels | Auditor verifies exact section labels/miniframes | Judge legibility/rhythm |
| Header/miniframe/bookmark/navigation missing or inconsistent | Critic checks shell specification | Auditor checks every section/page shell | Final whole-deck shell quality |
| Footer rule/buttons/page number misaligned | Planner freezes component role | Producer centralizes footer; Auditor checks geometry across consumers | Judge subtle optical alignment |
| Question accent rule wrong/missing; Answer lacks matching rule | Planner freezes paired Q/A grammar | Producer uses one shared component; Auditor checks both states and geometry | Judge visual flow and emphasis |
| Multiple fragmented Answer blocks when one continuous answer is required | Planner/Critic decide semantic block structure | Auditor exact role/component usage | Judge readability |
| Large meaningless whitespace | Critic rejects weak layout plan or missing content | Rendered Reviewer flags tiny object + void / pushed result / unfinished composition | Final semantic whitespace judgment |
| Result pushed to bottom leaving a hole | Critic protects evidence-interpretation relationship | Rendered Reviewer detects composition regression | Final page balance |
| Tiny primary figure/table/formula despite available space | Critic sets primary-object priority | Reviewer checks scale and archetype use | Final reader-effort judgment |
| Two-column layout used merely because space exists | Planner chooses semantic relation; Critic rejects wrong archetype | Auditor verifies only approved archetype is used | Judge actual reading path |
| Sequential derivation/question/evidence/answer split into columns | Planner/Critic require vertical sequence | Auditor enforces archetype | Judge whether visual order is obvious |
| Peer columns misaligned | Planner defines peer relationship | Producer aligns headings/formulas; Reviewer checks common anchors | Final optical alignment |
| Narrow/tall or badly cropped context photo | Planner specifies role/aspect need | Producer uses approved crop; Reviewer checks no distortion and useful scale | Final composition |
| Figure/caption mis-role: body explanation hidden as caption | Planner/Critic assign semantic roles | Auditor checks role mapping and adjacency | Judge whether interpretation is visually accessible |
| Math variables written as words inside figures | Planner freezes mathematical labels | Auditor checks glyphs/figure text | Secondary visual check |
| Residual plot shown without how-to-read explanation | Planner writes interpretation; Critic checks student sufficiency | Auditor ensures required explanation/caption exists | Judge readability and evidence proximity |
| Dispersion value shown without explaining what 1 or 3.182 means | Planner/Critic content responsibility | Auditor exact required-object check | Judge whether page communicates clearly |
| NB2 shown without explaining “2”, κ, uncertainty, AIC context | Planner/Critic content responsibility | Auditor exact copy/object presence | Judge whether page feels overloaded/under-explained |
| Count/rate/offset compressed or unclear | Planner/Critic own three-job teaching sequence and estimand meaning | Auditor protects page jobs/copy/order | GPT Work checks sequence readability and visual continuity |
| Multinomial relative log-ratios confused with probabilities | Planner/Critic statistical explanation | Auditor protects equations/tables/copy | Judge whether derivation/result is visually understandable |
| Random intercept presented as “just add \(u_i\)” | Planner/Critic explain sharing, conditional independence, marginal association | Auditor protects required mechanisms | Judge student-facing clarity |
| Wrong grouping variable or no explanation of grouping | Planner/Critic semantic correctness | Auditor exact model/object check | Secondary communication check |
| Conditional OR, coefficient/SE change, heterogeneity not linked | Planner/Critic content sufficiency | Auditor protects table/interpretation | Judge whether visual grouping supports comparison |
| Simulation lacks purpose, known truth, κ rationale, or repeated-fit logic | Planner/Critic content sufficiency | Auditor protects required sequence/code/results | Judge whether sequence is comprehensible |
| Bayesian section starts with package workflow instead of why/what | Planner/Critic sequence responsibility | Auditor protects twelve-page job sequence | GPT Work checks section coherence |
| Prior predictive shown without what statistic to inspect or what conclusion means | Planner/Critic content | Auditor required object/text check | Judge figure-question-answer proximity |
| MCMC motivation or chain/state/draw mechanism missing | Planner/Critic content | Auditor protects sequence | Judge section clarity |
| MH/Gibbs/augmentation/blocks/HMC/NUTS collapsed into labels | Planner/Critic decide mechanism depth | Auditor protects required pages/objects | Judge reading effort and density |
| “Why not NUTS?” not actually answered | Planner/Critic content | Auditor protects decision table/clarification | Judge whether answer is visible and understandable |
| MCMC diagnostics confuse MCSE, posterior SD, sampler geometry, model fit | Planner/Critic statistical meaning | Auditor exact content | Judge layout and interpretation proximity |
| Posterior transform shown without draw-by-draw meaning | Planner/Critic statistical meaning | Auditor exact content | Judge visual clarity |
| PPC figure shown without a model-fit judgment | Planner/Critic interpretation | Auditor exact required interpretation | Judge evidence/interpretation adjacency |
| Code page contains code but no actual result | Planner specifies result role | Auditor runs code and checks result | Judge code/result visual balance |
| Code/API/package inventory becomes the teaching content | Planner/Critic student boundary | Auditor forbids unauthorized visible plumbing | GPT Work flags engineering-looking page |
| Code blocks unequal, tiny, or have useless lower void | Layout spec sets peer role | Rendered Reviewer checks scale/balance | Final readability |
| Curly quotes / broken text / non-copyable code | None beyond source fidelity | Auditor deterministic PDF/code-copyability gate | Not a GPT Work primary gate |
| AI-like slogans, “not X” defensive prose, noun-colon fragments, internal engineering language | Planner writes natural copy; Critic reviews boundary | Auditor role/forbidden-pattern checks | GPT Work final naturalness judgment |
| Visible `Prerequisite:` or page/object dependency narration | Planner forbids; Critic checks | Auditor hard-fails | GPT Work secondary catch |
| Assessment/HW/project slide exposes answer scaffold, hidden rubric, internal rationale | Planner/Critic owns student boundary | Auditor exact allowed-copy gate | GPT Work checks presentation naturalness |
| Closing page loses course shell or becomes generic blank “Questions?” | Planner freezes closing job + shell; Critic checks history | Producer uses shared shell; Auditor checks Summary/header/footer/page number | GPT Work final closure quality |
| Previously fixed defect returns in later version | Planner retains guard lifecycle | Auditor compares cumulative guards/locks; Controller rejects recurrence | GPT Work acts as final independent catch, never the first expected detector |
| Latest-version-only history reading | Planner/Critic full-history rule for major/recovery | Auditor verifies compiled bundle coverage | Not primarily GPT Work |
| Local repair rewrites unrelated pages | Planner freezes allowlist/locks | Auditor source/render diff + patch-manifest gate | GPT Work checks affected deck rhythm only after scope passes |
| Fixing a shared component breaks all its consumers | Planner tracks dependencies | Auditor automatically revalidates all consumers | GPT Work reviews optical consistency on affected consumers |
| Candidate reviewed only on representative pages but declared global PASS | Critic/Planner forbid scope inflation | Auditor review-scope gate | GPT Work full-deck/contact-sheet gate for major release |
| One version’s acceptance standard silently replaces prior standards | Planner maintains cumulative guard set | Auditor proves all inherited guards evaluated | GPT Work uses same cumulative visual guard set |
| Producer self-review treated as final acceptance | Controller architecture prohibits it | Fresh Auditor required | GPT Work independent final gate |

This table is a permanent ownership map. New failure classes are appended; existing classes are not deleted merely because one version fixed them.

---

## 7. Codex self-QA versus fresh Auditor

Codex has two distinct internal responsibilities.

### 7.1 Producer self-QA

Before asking for independent review, Producer must remove obvious defects itself.

At minimum:

- build succeeds from clean output;
- exact page count/order;
- exact copy and required objects;
- no forbidden visible strings/roles;
- code actually runs where required;
- math/figure labels are correct;
- no clipping/overlap/overfull output;
- shell and shared components render;
- page images/contact sheet exist;
- obvious whitespace, tiny-object, broken-column, bad-footer, broken-Q/A, bad-caption defects are fixed;
- patch manifest matches actual changes.

Producer self-QA does **not** issue final PASS.

### 7.2 Fresh Auditor

The fresh Auditor independently reviews the exact candidate.

For major/full-deck work it reviews every page plus the contact sheet.

For each page it records:

- PageID;
- active historical guards checked;
- page job;
- primary object;
- copy fidelity;
- component/shell fidelity;
- reading path;
- object scale;
- whitespace use;
- semantic proximity;
- audience-language boundary;
- statistical/pedagogical sufficiency;
- observed issue or PASS reason.

A source change after Auditor review creates a new candidate/version and requires a fresh Auditor.

---

## 8. GPT Work final gate

GPT Work is not a substitute for the fresh Codex Auditor.

It is used **after** deterministic/internal review has closed routine defects.

### Major / new high-risk / recovery

GPT Work reviews:

- all pages at whole-slide scale;
- full contact sheet;
- key high-resolution pages;
- cumulative visual/pedagogical guards;
- full-deck rhythm and density;
- audience reader effort;
- natural language;
- semantic proximity;
- historical visual recurrence.

### Minor bounded revision

GPT Work may review:

- changed pages;
- affected shared-component consumers;
- minimum context pages;
- full contact sheet;

only when page count, section order, page jobs, shell, and archetypes remain locked.

Final release still requires one whole-deck regression.

### GPT Work finding routing

If GPT Work finds:

- **mechanical/layout implementation defect** -> fresh Producer repair -> fresh Auditor -> GPT Work re-review;
- **shared-component defect** -> unlock component scope -> repair -> revalidate all consumers -> fresh Auditor -> GPT Work;
- **Planner/content/pedagogy defect** -> return to ChatGPT Planner; if major, fresh Critic before production resumes;
- **new historical failure class** -> append a cumulative guard and assign permanent ownership before next candidate.

A GPT Work finding that should have been caught earlier is evidence that an upstream gate needs strengthening. It must not remain a one-off note.

---

## 9. Layout decision contract

### 9.1 Use columns only for true peers

Columns are appropriate for:

- R vs Python;
- before vs after;
- model A vs model B;
- written vs oral roles;
- two independent evidence panels;
- stable figure + interpretation pairs.

Conditions:

- either side can be understood without first finishing the other;
- both remain readable at slide scale;
- peer headings/formulas align;
- primary object is not shrunk for symmetry;
- interpretation remains adjacent to its evidence.

### 9.2 Use vertical flow for sequential logic

Vertical is default for:

- derivations;
- algorithms;
- causal/mechanism chains;
- Question -> evidence -> Answer;
- count -> exposure -> rate;
- stepwise interpretation;
- any page where the right region depends on the left.

Test:

> If the audience must finish the left region before the right region makes sense, it is sequential and should normally be vertical.

Codex may not switch archetypes merely to solve fit.

---

## 10. Whitespace contract

Whitespace is judged after content sufficiency.

### Acceptable

Whitespace is acceptable when:

- page job is complete;
- primary object is already large/readable;
- reading path is clear;
- space provides deliberate breathing room;
- title/closing restraint is intentional.

### Failing

A page fails when large unused space coexists with:

- undersized figure/table/formula/code;
- missing explanation;
- result pushed far from evidence;
- tiny text;
- column-created lower void;
- deleted/compressed content;
- unfinished-looking composition.

Do not fill space with:

- slogans;
- decorative cards;
- generic arrows;
- repeated labels;
- filler captions;
- generic takeaway boxes.

Use space first to improve:

- primary-object scale;
- evidence-interpretation proximity;
- grouping;
- needed explanation.

Whitespace must be judged at whole-slide scale and in sequence on the contact sheet.

---

## 11. Historical-feedback consumption by round

### Major revision / recovery

Planner + Critic reread:

- complete raw feedback;
- direct human decisions;
- actual rendered lineage;
- lifecycle/supersession;
- positive and rejected baselines.

They report exact counts and unresolved conflicts.

### Every Codex round

Codex receives a read-only compiled bundle containing:

- all active global guards;
- all guards for modified PageIDs/components;
- current round feedback;
- human locks;
- round-frozen scope;
- ancestry;
- shared-component consumers;
- unresolved conflicts.

Fresh Auditor verifies bundle coverage against the cumulative registry.

Codex never interprets or resolves human-feedback conflicts.

### Minor revision

Planner reads:

- current feedback;
- exact reviewer-seen baseline;
- active global guards;
- complete history for affected pages/components;
- locks and dependencies.

Any recurrence, ambiguity, shared-shell change, page-job change, or cross-page root cause escalates to major.

---

## 12. One-Goal autonomous production

Non-trivial production and revision milestones use:

```text
Parent Controller
├─ fresh Producer
├─ Producer self-QA
├─ fresh read-only deterministic/rendered Auditor
├─ fresh Producer repair
├─ new immutable candidate if bytes change
├─ fresh complete re-review
└─ independently accepted candidate/delta
```

Ordinary engineering/review defects are internal work.

Do not ask the user to:

- relay completion blocks;
- manually start routine reviewers;
- inspect intermediate candidate defects;
- choose already-frozen implementation details.

---

## 13. Bounded revision and non-regression

Every revision round freezes:

- exact baseline;
- allowlist PageIDs/components;
- addressed feedback IDs;
- human locks;
- round-frozen scope;
- shared-component consumers;
- explicit unlocks;
- change budget.

Every candidate supplies a proof-carrying patch manifest.

A round cannot PASS unless:

```text
open_feedback_next ⊂ open_feedback_current
human_locked_pages_next ⊇ human_locked_pages_current
human_locked_components_next ⊇ human_locked_components_current
modified_ids ⊆ explicit_allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
```

A shared-component change automatically revalidates every consumer page, but does not reopen their semantic/copy locks.

If the same closed guard recurs twice after claimed repair, stop page-local patching and repair the shared primitive/authority/reviewer coverage.

---

## 14. Failure-to-owner escalation

When a new failure is discovered, do not just patch it.

Classify it:

### Planner/specification failure

Examples:

- wrong page count;
- insufficient explanation;
- wrong audience boundary;
- wrong archetype;
- contradictory shell requirement.

Action:

```text
return to Planner
-> amend F1/F2/F3
-> if major, fresh Critic
-> resume production only after PASS
```

### Producer implementation failure

Examples:

- wrong spacing;
- bad crop;
- misaligned table;
- broken footer;
- Q/A line geometry;
- code copyability;
- clipping.

Action:

```text
fresh Producer repair
-> fresh Auditor
```

### Shared-component failure

Action:

```text
unlock named component only
-> repair root primitive
-> deterministic regression over every consumer
-> fresh rendered review over affected consumers
```

### Review-coverage failure

Example: a defect was present but every reviewer claimed PASS.

Action:

```text
add permanent guard
-> strengthen the responsible review layer
-> replay historical rejected example
```

### New self-certification/control-plane failure

Action:

```text
stop project-local patch chain
-> repair/version generic validator/reviewer runtime
-> replay historical + unrelated decks
```

---

## 15. Completion and release

A presentation is complete only when all applicable layers agree:

- required prebuild Critic PASS;
- Planner freezes are intact;
- Codex deterministic Auditor PASS;
- rendered Auditor PASS;
- GPT Work PASS where required;
- cumulative historical guards PASS;
- prior locks preserved;
- final full-deck regression PASS;
- artifact identity/reproducibility PASS;
- user final subjective acceptance when required.

A file existing, compiling, or looking acceptable on a few representative pages is never sufficient.

---

## 16. Read-before-work rule

This file must be read before every non-trivial presentation task.

Other workflow files may add domain-specific detail, but they may not weaken or replace the cumulative principles here.

If a later document appears to conflict with this contract, stop and resolve the conflict before production rather than silently following the newer file.
