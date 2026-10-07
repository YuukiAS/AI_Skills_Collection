# Presentation End-to-End Pre-Execution Runbook

Status: **CANONICAL / MUST READ IN FULL BEFORE EVERY NON-TRIVIAL PRESENTATION TASK**  
Applies to: teaching, research, business, product, technical, decision, seminar, group-meeting, defense, and course presentations  
Companion acceptance contract: \`pre-execution-cumulative-acceptance-contract.md\`

This runbook is the complete operating procedure for presentation work.

It exists because repeated failures showed that isolated rules are not enough. A presentation can fail even when individual requirements are correct if the overall production sequence is wrong: the Planner freezes an incomplete specification, Codex improvises layout or copy, a later revision regenerates accepted pages, a reviewer checks only representative pages, or the latest round silently forgets earlier human feedback.

The rule from now on is:

> **Before any non-trivial presentation work begins, read this runbook in full, then read the cumulative acceptance contract. Only then may planning, Critic review, production, revision, or release work start.**

No task-local prompt, domain skill, or later workflow may weaken this runbook. Domain-specific skills may add requirements.

---

# 1. Core objective

The workflow must optimize three things simultaneously:

1. **content quality** — what is taught/claimed/shown is correct, sufficient, audience-appropriate, and source-grounded;
2. **visual quality** — hierarchy, composition, object scale, whitespace, typography, navigation, and rhythm are deliberate;
3. **revision efficiency** — accepted work stays accepted, obvious defects are solved internally, and the user normally sees only two to four shrinking review deltas.

The user is never the first QA pass.

Infrastructure exists to support a good presentation. Once enough authority is frozen, the process must move to visible artifacts. Do not spend open-ended time extending governance while no useful slide artifact appears.

---

# 2. Mandatory first-step output

Before doing substantive work, the Planner/Controller must determine and be able to report:

\`\`\`text
RUNBOOK_READ = YES
CUMULATIVE_ACCEPTANCE_CONTRACT_READ = YES
TASK_CLASSIFICATION =
CRITIC_REQUIRED =
DELIVERABLE_FORMAT =
AUDIENCE =
PURPOSE =
EXACT_BASELINE =
SOURCE_SET =
HISTORY_SCOPE =
CURRENT_FREEZE_LEVEL =
ACTIVE_GLOBAL_GUARDS =
LOCKED_PAGEIDS =
LOCKED_COMPONENTS =
IN_SCOPE_PAGEIDS =
IN_SCOPE_COMPONENTS =
ROUND_ALLOWLIST =
USER_IS_FIRST_QA = NO
\`\`\`

If these fields cannot yet be determined, the next action is source/history recovery or Planner clarification, not slide production.

---

# 3. Task classification

Classify before authoring.

## 3.1 NEW_SMALL

Use only when:

- the deck is small and low-risk;
- source and audience are clear;
- no complex historical feedback exists;
- no new high-risk teaching/scientific meaning is being introduced;
- the visual system is already established or simple.

A separate prebuild Critic is optional.

## 3.2 NEW_MAJOR

Use when a new deck is:

- substantial;
- teaching-heavy;
- scientific/high-stakes;
- template-defining;
- likely to need non-trivial page-count, content-depth, or layout judgments.

A prebuild Critic is required before broad production.

## 3.3 MINOR_REVISION

A revision is minor only if **all** are true:

- page count unchanged;
- section order unchanged;
- no page job changes;
- no scientific/statistical/pedagogical claim changes;
- no title/header/footer/navigation/template redesign;
- no new archetype;
- no page split or merge;
- visible-copy changes are local and source-supported;
- scope is normally no more than about three pages and one already-defined shared component;
- no closed historical guard has recurred;
- no shared-root failure is suspected.

Minor work may skip the prebuild Critic.

## 3.4 MAJOR_REVISION

Major when any of the following holds:

- page count changes;
- section order or narrative changes;
- page jobs change;
- broad copy/content changes span multiple pages;
- shared shell/template/header/footer/navigation changes;
- new layout archetype or major figure system is introduced;
- page split/merge is required;
- scientific/statistical/pedagogical/assessment meaning changes;
- repeated regression suggests the current Planner authority may be wrong;
- user asks to rethink, rebuild, overhaul, or reread all history.

If uncertain, classify as major.

## 3.5 FAILED_VERSION_RECOVERY

Always major.

Required additions:

- authoritative version map;
- exact reviewer-seen historical renders;
- raw annotation recovery;
- feedback lifecycle/supersession;
- positive baselines;
- rejected/negative baselines;
- explicit recovery decision;
- prebuild Critic before implementation.

---

# 4. Role separation

## 4.1 ChatGPT Web / Planner / Presentation Author

ChatGPT Web owns human-level judgment.

It is responsible for:

- source reading and reconciliation;
- audience, purpose, duration, format, and desired audience change;
- task classification and Critic routing;
- narrative and section sequence;
- page count;
- stable PageIDs;
- one page job per PageID;
- primary scientific/teaching/decision object;
- required and forbidden content;
- source anchors;
- audience vs speaker/instructor/internal boundary;
- exact visible copy;
- layout semantic relationship;
- layout archetype selection;
- feedback interpretation, lifecycle, supersession;
- locks and unlocks;
- Planner amendments;
- Critic prompt;
- autonomous Codex Controller Goal;
- deciding whether a finding is a specification defect or an implementation defect.

ChatGPT Web must not be reduced to “write a prompt telling Codex to make it better.”

ChatGPT Web does **not** own:

- TeX/PPTX implementation;
- compilation;
- final rendering;
- low-level figure generation;
- deterministic build QA;
- repository production mechanics.

## 4.2 Prebuild Critic

Fresh, read-only, independent.

Required for major revision, failed-version recovery, and major/high-risk new decks.

The Critic verifies:

- actual source/history consumption;
- exact feedback counts where relevant;
- page count and sequence;
- every page job;
- content correctness;
- content sufficiency;
- audience boundary;
- exact-copy completeness;
- layout/archetype suitability;
- historical regression coverage;
- Controller review/repair plan.

The Critic returns:

- \`PASS\`;
- \`REVISE\` with a bounded Planner-amendment list;
- or \`BLOCKED_HISTORY_NOT_CONSUMED\` / source-equivalent block.

The Critic does not implement slides.

A major Planner amendment after Critic review requires another fresh Critic pass.

## 4.3 Codex Parent Controller

Owns the autonomous engineering/review loop.

It must coordinate:

\`\`\`text
fresh Producer
-> Producer self-QA
-> fresh read-only Auditor/Reviewer
-> fresh Producer repair
-> new immutable candidate if bytes changed
-> new fresh review
-> repeat until independently accepted
\`\`\`

The Parent:

- binds exact candidate/authority/round scope;
- does not make new semantic decisions;
- does not ask the user to relay intermediate completion blocks;
- routes ordinary findings to fresh Producer contexts;
- stops only for a real Planner decision, human-only external action, or proven reviewer-runtime failure.

## 4.4 Codex Producer

Owns implementation only.

Allowed:

- typeset approved copy;
- implement approved archetype;
- choose line breaks, spacing, widths, alignment within the frozen archetype;
- use approved fallback;
- generate approved figures/assets from frozen values/labels;
- crop/scale without changing meaning;
- build/render/export;
- run code and deterministic smoke tests;
- prepare proof-carrying patch manifest;
- repair Auditor findings inside frozen scope.

Forbidden:

- decide what to teach or claim;
- add/delete/paraphrase audience-visible prose;
- change page count;
- merge/split pages without Planner authority;
- invent a new archetype;
- delete difficult content to fix layout;
- change shared components without explicit unlock;
- edit tests/gates/acceptance rules to make candidate pass;
- declare final acceptance.

## 4.5 Fresh Codex deterministic Auditor

Fresh, read-only, independent from Producer.

Checks objective conformance:

- exact copy;
- exact PageID/order/count;
- scope/allowlist;
- locks;
- active historical guards;
- required-object preservation;
- component bindings and consumers;
- shell presence/consistency;
- code execution/copyability;
- mathematical glyphs;
- figure labels;
- PDF/PPTX structure;
- artifact identity/versioning;
- forbidden visible strings/roles;
- recurrence of deterministic historical defects.

## 4.6 Fresh rendered-artifact Reviewer

Reviews actual renders after Producer stops.

Checks:

- page hierarchy;
- reading path;
- primary-object scale;
- whitespace;
- semantic proximity;
- table/code/figure readability;
- shared-component optical consistency;
- Q/A geometry;
- page rhythm;
- deck rhythm;
- obvious audience-language problems.

This is still internal Codex-controlled QA. It should eliminate routine visible defects before GPT Work.

## 4.7 GPT Work

Final independent aesthetic / reader-effort / communication gate.

For major/new/recovery full candidates:

- review all pages;
- review full contact sheet;
- inspect high-risk pages at high resolution;
- apply cumulative visual/pedagogical historical guards;
- judge whole-deck rhythm;
- judge audience reading effort;
- judge naturalness;
- judge evidence-interpretation proximity;
- judge whether pages are convincingly communicative rather than merely mechanically valid.

For minor bounded revisions, GPT Work may review:

- changed pages;
- affected shared-component consumers;
- minimum context pages;
- full contact sheet;

only when global structure, shell, page jobs, and archetypes are locked.

GPT Work does not:

- implement fixes;
- invent content;
- change scientific/statistical meaning;
- override deterministic failures.

## 4.8 User

The user owns only:

- genuine subjective preference between already acceptable options;
- new semantic/course/research decisions not determined by source;
- explicit page/component locking;
- final subjective acceptance.

The user is not routine QA.

---

# 5. Freeze ladder

Later stages cannot silently reopen earlier freezes.

## F0 — source/baseline/history freeze

Freeze:

- source set;
- baseline artifact;
- reviewer-seen version;
- historical feedback;
- positive/negative baselines;
- artifact/version identity;
- current locks.

## F1 — narrative/page-job freeze

Freeze:

- section sequence;
- page count or bounded range;
- stable PageIDs;
- one job per PageID;
- primary object;
- required/forbidden objects;
- source anchors;
- transitions;
- audience vs speaker/instructor boundary.

## F2 — visible-copy freeze

Freeze every audience-visible string:

- titles;
- subtitles;
- prose;
- bullets;
- equations and labels;
- Question/Answer;
- table cells;
- figure labels;
- code;
- captions;
- source lines;
- administrative instructions.

## F3 — layout-semantics freeze

Freeze:

- semantic relationship;
- reading path;
- archetype;
- primary-object priority;
- allowed fallback;
- forbidden fallback;
- shared-component bindings.

## F4 — shared-component freeze

After proof and internal review, lock:

- title;
- header/navigation;
- footer/source/buttons/page number;
- typography;
- Question/Answer grammar;
- table/code/caption/figure grammar;
- closing.

## F5 — golden-page composition freeze

Lock representative:

- density;
- scale;
- composition;
- archetype behavior;
- high-risk page patterns.

## F6 — full-candidate freeze

Freeze exact:

- source;
- commit;
- PDF/PPTX;
- renders;
- hashes;
- page map;
- review bundle.

## F7 — human locks

Explicit acceptance creates a page/component lock until a named unlock gives:

- stable ID;
- reason;
- authorized scope.

---

# 6. Historical feedback policy

Historical acceptance is cumulative.

## 6.1 Major revision / recovery

Planner + Critic reread:

- complete raw feedback;
- direct human decisions;
- rendered lineage;
- lifecycle/supersession;
- positive baselines;
- rejected baselines.

They report:

- exact counts;
- source gaps;
- conflicts;
- affected PageIDs/components.

## 6.2 Every Codex round

Codex receives a read-only compiled authority bundle containing:

- all active global guards;
- all guards for modified PageIDs/components;
- current-round feedback;
- current human locks;
- round-frozen scope;
- ancestry;
- component consumers;
- unresolved conflicts.

The fresh Auditor verifies bundle coverage against the cumulative registry.

Codex does not resolve human-feedback conflicts.

## 6.3 Minor revision

Planner reads:

- current feedback;
- exact reviewer-seen baseline;
- all active global guards;
- complete affected-page/component history;
- locks and dependencies.

Escalate to major if:

- a closed guard recurs;
- history is ambiguous;
- shared shell changes;
- page job changes;
- cross-page root cause appears.

## 6.4 Authority precedence

\`\`\`text
latest explicit human decision
> active raw feedback and named Planner amendment
> lifecycle/supersession decision
> compiled guard registry
> latest candidate
> executor preference
\`\`\`

Derived summaries organize history; they do not outrank active human feedback.

---

# 7. Page-planning rule

Every page must have:

- one primary job;
- one primary audience action;
- one primary object or object group;
- explicit required objects;
- explicit forbidden objects;
- source anchor;
- transition in/out;
- audience boundary;
- layout semantic relation;
- approved archetype.

A page should not be created because “there is room for another slide.”

A page should not be merged because “we can fit both topics.”

Split/merge decisions are semantic decisions, not layout conveniences.

---

# 8. Layout grammar

Layout is selected from semantic relationship.

## 8.1 Columns are appropriate for true peers

Examples:

- R vs Python;
- before vs after;
- model A vs model B;
- written vs oral roles;
- two independent evidence panels;
- stable figure + interpretation pair.

Conditions:

- either side can be understood without finishing the other first;
- both remain readable;
- peer headings/formulas align;
- primary object is not shrunk for symmetry;
- interpretation remains adjacent to evidence.

## 8.2 Columns are inappropriate for sequential logic

Use vertical flow for:

- derivations;
- algorithms;
- mechanism chains;
- Question -> evidence -> Answer;
- count -> exposure -> rate;
- stepwise interpretation;
- any page where the right side depends on the left.

Test:

> If the audience must finish the left region before the right region makes sense, the relationship is sequential and should normally be vertical.

## 8.3 Codex layout freedom

Codex may adjust:

- widths;
- spacing;
- line breaks;
- alignment;
- crop/scale;
- approved responsive fallback.

Codex may not:

- invent a new archetype;
- delete text;
- split/merge pages;
- replace explanation with cards or slogans;
- switch to columns merely because horizontal space exists.

---

# 9. Whitespace and density

Whitespace is judged **after content sufficiency**.

## 9.1 Acceptable whitespace

Accept when:

- page job is complete;
- primary object is already readable and properly scaled;
- reading path is clear;
- space supports grouping/breathing room;
- title/closing restraint is intentional.

## 9.2 Failing whitespace

Fail when large unused space coexists with:

- undersized figure/table/formula/code;
- missing explanation;
- result far from evidence;
- result pushed to bottom;
- tiny text;
- lower void caused by columns;
- deleted/compressed teaching content;
- unfinished composition.

Do not fill space with:

- slogans;
- cards;
- decorative arrows;
- repeated labels;
- filler captions;
- generic takeaway boxes.

Use available space to improve:

- primary-object scale;
- evidence-interpretation proximity;
- grouping;
- needed explanation.

Whitespace must be judged on whole-slide renders and on the contact sheet.

---

# 10. Shared components

Shared components must be centralized and independently reviewable.

At minimum:

- title shell;
- section/header navigation;
- footer;
- page number;
- source line;
- navigation/action buttons;
- typography;
- Question;
- Answer;
- table;
- code;
- caption;
- figure/diagram treatment;
- closing shell.

If one shared component changes:

- unlock only that component;
- automatically place all consumer pages in regression scope;
- do not reopen semantic/copy locks on those pages;
- rerender/review all affected consumers.

---

# 11. Question/Answer grammar

Question and Answer are paired semantic components.

Rules:

- use consistent accent-rule grammar;
- both Question and Answer retain their intended rule;
- rule aligns to the rendered text block;
- sequential Question -> evidence -> Answer stays vertical;
- when one continuous Answer is required, do not fragment it into repeated Answer labels;
- Question/Answer must not become arbitrary cards or decorative blocks.

---

# 12. Figure / caption / evidence rules

A figure is not decoration.

Rules:

- figure must encode data, mechanism, model, uncertainty, or evidence;
- mathematical variables use actual mathematical glyphs;
- captions are captions, not hidden paragraphs;
- interpretation stays adjacent to evidence;
- photo/crop aspect ratio must support the teaching role;
- do not distort images;
- regenerate figures for slide scale when paper/export versions are unreadable;
- do not shrink a primary figure while leaving large empty regions.

---

# 13. Code-page rules

Code pages must be student/audience useful.

Rules:

- code is copyable;
- actual code is run when results are shown;
- visible results stay near the code;
- code syntax is subordinate to the statistical/scientific job;
- avoid package/API inventory as the page's teaching purpose unless package behavior itself is the topic;
- peer code blocks use aligned roles and reasonable balance;
- do not leave one column short with a large lower void while the other is dense;
- no curly quotes or broken PDF text extraction.

---

# 14. Prebuild Critic workflow

Required for major/recovery and major new decks.

Critic must:

1. prove source/history consumption;
2. independently evaluate page count;
3. independently evaluate sequence;
4. review every planned PageID;
5. check content correctness;
6. check student/audience sufficiency;
7. check visible-copy boundary;
8. check layout suitability;
9. list relevant historical guards;
10. audit the autonomous Codex Controller.

If any planned page is REVISE, broad production stays blocked.

The response is:

\`\`\`text
PASS
or
REVISE -> Planner amendment only
or
BLOCKED_HISTORY_NOT_CONSUMED
\`\`\`

Do not say “production can fix it later.”

---

# 15. Component proof and golden pages

## 15.1 Shared-component proof

Before broad production in a materially new visual system, prove real-content shared components.

Use real deck content, not lorem ipsum.

Internal loop:

\`\`\`text
Producer
-> deterministic checks
-> fresh Reviewer
-> repair
-> fresh Reviewer
\`\`\`

## 15.2 Golden-page proof

Normally select six to ten pages covering:

- highest-risk content;
- every major archetype;
- historical failure classes;
- dense and sparse pages;
- figure/table/code/formula/Q&A;
- opening and closing.

Golden pages establish:

- density floor;
- composition grammar;
- component behavior;
- object scale;
- slide-level quality.

## 15.3 Exception

A major Critic may authorize direct full-deck production in an urgent recovery only when:

- shell is frozen;
- copy is frozen;
- archetypes are frozen;
- historical guards are frozen;
- review route is strong enough;
- user explicitly does not want another proof round.

This is an exception, not the default.

---

# 16. Full-candidate production

Full candidate production uses one autonomous Controller Goal.

Sequence:

\`\`\`text
Producer builds full candidate
-> Producer self-QA
-> fresh deterministic Auditor
-> fresh rendered Reviewer
-> repair all P0/P1/P2
-> new immutable candidate if bytes change
-> new fresh full review
-> repeat until internally accepted
-> GPT Work final gate
\`\`\`

The user does not receive intermediate candidate defects.

---

# 17. Producer self-QA

Before launching fresh review, Producer must remove obvious defects.

Minimum checks:

- clean build;
- exact page count/order;
- exact copy;
- required objects;
- forbidden strings/roles;
- code execution;
- correct numerical results;
- correct math labels;
- no clipping/overlap;
- shared shell present;
- component geometry present;
- renders/contact sheet exist;
- obvious whitespace issue fixed;
- tiny-object issue fixed;
- bad column choice fixed only within allowed archetype;
- footer/header issue fixed;
- Q/A geometry fixed;
- caption-role problem fixed;
- patch manifest matches real diff.

Producer self-QA does not create final PASS.

---

# 18. Fresh Codex Auditor

For major/full deck, review every page and contact sheet.

Per page, record:

\`\`\`text
PageID
historical guards checked
page job
primary object
copy fidelity
shell/component fidelity
reading path
object scale
whitespace
semantic proximity
audience boundary
statistical/pedagogical sufficiency
finding or PASS reason
verdict
\`\`\`

A source change after Auditor review requires:

- new candidate identity/version;
- new fresh Auditor.

Representative-page review may guide development but cannot issue global PASS.

---

# 19. GPT Work gate

GPT Work is the final aesthetic/reader-effort/communication gate.

## Major / recovery / substantial new deck

Review:

- all pages;
- full contact sheet;
- key high-resolution pages;
- cumulative visual guards;
- whole-deck rhythm;
- density changes;
- natural language;
- semantic proximity;
- audience effort;
- historical visual recurrence.

## Minor revision

May review:

- changed pages;
- affected shared-component consumers;
- minimum context;
- full contact sheet;

provided global structure remains locked.

## Routing findings

Mechanical/layout defect:

\`\`\`text
fresh Producer repair
-> fresh Auditor
-> GPT Work re-review
\`\`\`

Shared-component defect:

\`\`\`text
unlock named component
-> repair primitive
-> revalidate all consumers
-> fresh Auditor
-> GPT Work
\`\`\`

Planner/content/pedagogy defect:

\`\`\`text
return to Planner
-> amend F1/F2/F3
-> if major, fresh Critic
-> resume production
\`\`\`

New failure class:

\`\`\`text
append cumulative guard
-> assign permanent owner
-> strengthen upstream gate
-> replay rejected example
\`\`\`

---

# 20. User review

The user should receive:

- final internally accepted candidate;
- or a bounded delta;
- before/after for changed pages when useful;
- resolved feedback IDs;
- genuine remaining subjective decisions;
- proof that unrelated locks remain unchanged.

The user should not receive:

- intermediate defect lists;
- routine QA logs;
- completion-block relay tasks;
- requests to find basic whitespace/footer/title/code issues.

---

# 21. Bounded revision

Every revision round freezes:

- exact baseline;
- allowed PageIDs/components;
- current feedback IDs;
- locks;
- round-frozen scope;
- shared-component consumers;
- explicit unlocks;
- change budget.

Producer provides proof-carrying patch manifest:

\`\`\`text
candidate_id
parent_candidate_id
baseline_commit
modified_page_ids
modified_component_ids
addressed_feedback_ids
unchanged_locked_page_ids
unchanged_locked_component_ids
required_object_relocations
visible_copy_changes
dependency_invalidations
open_items_before
open_items_after
\`\`\`

Out-of-allowlist changes fail.

---

# 22. Monotone convergence

Each accepted round must satisfy:

\`\`\`text
open_feedback_next is a strict subset of open_feedback_current
human_locked_pages_next is a superset of human_locked_pages_current
human_locked_components_next is a superset of human_locked_components_current
modified_ids are a subset of the explicit allowlist
unrelated_source_changes = 0
unrelated_render_changes = 0
closed_guard_recurrences = 0
\`\`\`

Normal target: two to four user review rounds.

If open issues do not decrease or accepted work reopens:

- do not create another broad candidate;
- diagnose authority/copy/archetype/component/reviewer root cause first.

---

# 23. Failure escalation

## Planner/specification failure

Examples:

- wrong page count;
- insufficient explanation;
- wrong audience boundary;
- wrong archetype;
- contradictory shell requirement.

Route:

\`\`\`text
Planner amendment
-> fresh Critic if major
-> production resumes only after PASS
\`\`\`

## Producer implementation failure

Examples:

- spacing;
- crop;
- alignment;
- footer;
- Q/A line;
- code copyability;
- clipping.

Route:

\`\`\`text
fresh Producer
-> fresh Auditor
\`\`\`

## Shared-component failure

Route:

\`\`\`text
unlock component only
-> repair root primitive
-> revalidate all consumers
-> fresh rendered review
\`\`\`

## Review-coverage failure

A defect was present but reviewers returned PASS.

Route:

\`\`\`text
add permanent guard
-> strengthen responsible layer
-> replay historical rejected example
\`\`\`

## Self-certification/control-plane failure

Route:

\`\`\`text
stop project-local patch chain
-> repair/version generic validator/reviewer runtime
-> replay historical and unrelated decks
\`\`\`

---

# 24. Cumulative acceptance

Read the companion:

\`pre-execution-cumulative-acceptance-contract.md\`

Its guard lifecycle and failure ownership are mandatory.

New feedback:

- adds guards;
- strengthens guards;
- or explicitly supersedes/retires guards.

New feedback does not silently erase old guards.

A later version cannot PASS while any inherited active or resolved-but-guarded requirement fails.

---

# 25. Final full-deck regression

Before release, review the exact delivery artifact for:

- all pages and ordering;
- all active historical guards;
- semantic/copy/layout/component locks;
- header/footer/navigation;
- outline/bookmarks;
- typography;
- math glyphs;
- figures/tables/code;
- code copyability;
- PDF/PPTX text quality;
- whitespace;
- semantic proximity;
- deck rhythm;
- source fidelity;
- artifact identity;
- reproducibility.

Delta review never replaces final full-deck regression.

---

# 26. Completion rule

A presentation is complete only when all applicable layers agree:

- runbook read;
- cumulative acceptance contract read;
- required Critic PASS;
- Planner freezes intact;
- Producer self-QA complete;
- fresh deterministic Auditor PASS;
- fresh rendered review PASS;
- GPT Work PASS where required;
- all cumulative guards PASS;
- all prior locks preserved;
- final full-deck regression PASS;
- artifact identity/reproducibility PASS;
- user final subjective acceptance where required.

A file existing, compiling, or looking acceptable on representative pages is never sufficient.

---

# 27. Mandatory read order for future work

Before every non-trivial presentation task, read in this order:

1. **this file** — \`presentation-end-to-end-pre-execution-runbook.md\`;
2. **cumulative acceptance contract** — \`pre-execution-cumulative-acceptance-contract.md\`;
3. \`authoring-production-workflow.md\`;
4. \`chatgpt-web-authoring-contract.md\` when ChatGPT Web is planning;
5. \`anti-shortcut-production-contract.md\`;
6. \`independent-review-contract.md\`;
7. domain skill / project-specific authority;
8. task-local source, baseline, history, and locks.

Do not begin execution until steps 1–2 are complete.
