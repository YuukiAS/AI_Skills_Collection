# web-development — Long-Term TODO

Canonical maintenance inbox for the `web-development` plugin.

## Open candidates

### Production icon sourcing and icon-registry discipline
status: NEW
source: Lucerna / Windows tray panel production polish, 2026-09-13
evidence: `YuukiAS/Lucerna` real-shell iterations through commits `e81fa0807d4282b0552fabb0b92ca8287acb4037`, `23a98d33acafb9ffc5fe40ecd3b75abe3df095a2`, plus the user-provided production screenshots in the Lucerna project thread
problem: Frontend work repeatedly allowed ad-hoc inline SVG/placeholders and generic status dots to survive into a production-looking interface. The resulting icons had inconsistent geometry, stroke/fill weight, optical size, and platform feel; controls looked AI-generated even after spacing/typography polish. A mature frontend-design workflow should choose and freeze an icon source/system early instead of letting the model improvise each glyph.
project-specific context: Lucerna is a compact Windows tray utility and will likely use Fluent System Icons for generic Windows UI/actions/status plus a separate approved brand-icon source for vendor marks. That exact library choice is Lucerna-specific and must not become a universal plugin rule.

Candidate refinement for the Frontend Design / visual-system workflow:

- Before drawing any generic UI icon, inspect whether the project already has a canonical icon library or platform-native system.
- If none exists, explicitly choose one coherent UI icon family based on platform/product constraints (for example Fluent System Icons for Fluent/Windows surfaces, Lucide or Phosphor for neutral cross-platform/web surfaces) and record the choice.
- Treat brand/provider marks separately from generic UI icons: prefer official vendor assets or a maintained brand set such as Simple Icons, subject to the provider's trademark/usage guidance.
- Do not hand-author generic inline SVG icons when an appropriate maintained icon exists. Custom SVG should be reserved for product identity, genuinely domain-specific symbols, or a documented gap.
- Avoid mixing multiple generic icon families in the same visual layer. If multiple sources are necessary, separate them by role (e.g. generic controls vs brand marks) and normalize optical size, box size, alignment, and semantic color treatment.
- Introduce a central icon registry/component instead of scattering raw SVG strings through render code. The registry should own icon source, size, regular/filled state, accessibility labeling, and theme/currentColor behavior.
- Add a production review check for placeholder icons: before calling a UI production-ready, scan for ad-hoc SVGs, emoji, arbitrary circles/dots standing in for semantic icons, or temporary glyphs that should be replaced by the canonical system.
- Record source/license/provenance for vendored or third-party icon assets so later packaging does not depend on undocumented downloads.

Planner note: first verify whether existing `visual-direction`, `design-system-tokens`, or related Frontend Design references already imply this discipline. If they do, the fix may belong in execution/review gates rather than adding another overlapping skill.

### Desktop-native acceptance must not be inferred from browser fixtures
status: NEW
source: research desktop reader native acceptance feedback, 2026-09-13
target layer: frontend QA / acceptance / desktop-shell review
problem: A browser-fixture review can close obvious layout/copy defects while still missing desktop-only failures: executable/taskbar/sidebar icon mismatch, native WebView jank, slow panel switching, scrollbar hitching, hover/focus feel, titlebar/layout differences, and empty-state flows that depend on native integrations. Declaring a desktop app review-ready from static browser screenshots creates false confidence.
candidate_action:
- When the target is Tauri/Electron/native-WebView desktop, require a native release build evidence class before final product review.
- Distinguish `BROWSER_FIXTURE_VISUAL` from `NATIVE_DESKTOP_VISUAL`; browser evidence may supplement but must not substitute for native desktop proof.
- Require at least one native full-window capture showing titlebar/taskbar/app-shell branding and one native interaction recording/trace for motion-sensitive flows.
- Require the reviewer to return `INSUFFICIENT_NATIVE_EVIDENCE` / not-ready when a desktop-only concern is represented only by browser fixtures.
- Prepare a simple launch path/shortcut before user acceptance so the user tests the exact release candidate rather than localhost/dev mode.
- For desktop products, acceptance should include real empty-state/startup/navigation behavior, not only pre-populated fixture states.
promotion_gate: validate this rule on at least two desktop/WebView projects before promoting it from TODO into generic Frontend Design production review gates.

### Motion, hover grammar, and performance budgets belong to the design system
status: NEW
source: research desktop reader interaction/performance feedback, 2026-09-13
target layer: frontend implementation / interaction QA
problem: A visually polished UI can still feel unfinished when tabs switch synchronously with long stalls, buttons have no hover/press feedback, panels remount with flicker, or scrolling janks. Adding animation after the fact can hide rather than solve the underlying state/render bottleneck. Frontend Design currently needs a stronger rule that motion and responsiveness are measurable product qualities, not optional polish.
candidate_action:
- Separate **latency** from **animation duration**: state change should begin immediately; a 160–220 ms transition is acceptable only after input-to-visible-response is already fast.
- Establish project-specific performance budgets for key interactions (e.g. panel/tab switch p95, scroll frame stability, no repeated >50 ms main-thread long tasks).
- Profile before animating. Check polling, whole-tree state replacement, unbounded DOM lists, unnecessary remounts, layout-heavy CSS, and callback/prop churn.
- Prefer event-driven state updates over coarse polling when the platform exposes events.
- Use one motion grammar. For React, evaluate Motion for React (`motion` / `motion/react`) for enter/exit/shared-layout transitions and gestures; use CSS transitions for simple hover when cheaper.
- Keep hover/press effects subtle and compositor-friendly; respect reduced-motion preferences.
- Require representative hover, keyboard-focus, tab transition, scroll, loading and error states in visual QA rather than judging only static screenshots.
- Treat brand/app icons as one canonical asset source across executable shell and in-app brand mark.
promotion_gate: verify these thresholds and motion patterns on real desktop/web apps; avoid freezing exact numeric budgets universally when hardware/product constraints differ.

### Component craftsmanship must be part of the definition of done
status: NEW
source: Bobbio native desktop review after performance repair, 2026-09-13
target layer: frontend design-system execution / visual QA
problem: Individual controls were technically functional and even had hover transitions, yet the native app still looked under-designed because button hierarchy, padding, icon alignment, grouping, repeated CTAs, empty-state composition, and cross-component spacing were not reviewed as one system. “No overflow + clickable + hover exists” is too low a production bar.
candidate_action:
- Define component completion as all applicable states: default, hover, pressed, focus-visible, disabled, loading/busy, selected/current, destructive.
- Review button anatomy explicitly: semantic role, height, horizontal padding, icon optical size/baseline, icon-to-label gap, radius, border/background, hit target, and relationship to adjacent controls.
- Review control clusters for hierarchy: primary action vs secondary/recovery/maintenance actions must not all have equal visual weight.
- Treat spacing as information architecture, not just collision avoidance: group related controls, separate unrelated actions, avoid both cramped utility bars and large unexplained dead zones.
- Add overlay/clipping/layout-shift checks while hovering, focusing, pressing and animating controls; motion must not change container geometry or collide with adjacent components.
- Require native recordings/frame sequences for interactive-state craft; static default-state screenshots cannot prove hover/press/focus quality.
- During final visual review, allow a repeated “functional but visibly placeholder/basic” component pattern to be P2 when it materially lowers product confidence, even if each control works.
- Add an explicit whole-screen composition pass: repeated labels, duplicated CTAs, over-promoted maintenance buttons, unbalanced empty states, panel hierarchy and scrollbar behavior must be reviewed together.
promotion_gate: validate on Bobbio plus at least one additional desktop/web product before turning the exact checklist into a mandatory generic production gate; the principle that all control states/hierarchy are part of done can be promoted earlier if independent evidence repeats.

### External review should confirm quality, not discover obvious local P2 defects
status: NEW
source: Bobbio repeated native GPT Work repair cycles, 2026-09-14
target layer: frontend implementation workflow / pre-review QA
problem: External review was repeatedly asked to identify defects that the implementation agent could have found itself by inspecting the same native evidence: nearly indistinguishable pressed/focus states, destructive controls that still looked neutral, contradictory healthy-flow screenshots containing PDF errors, and missing shell/state proof. This wastes review cycles and trains the development loop to outsource first-line quality control.
candidate_action:
- Add an explicit adversarial producer self-review before external review. The implementation agent should use the same P1/P2 rubric as the reviewer and try to reject its own build.
- External review should only be requested after the producer records `P1=0`, `P2=0`, required evidence complete, and no contradictory main-path states.
- Treat evidence integrity as part of implementation quality: a healthy-flow screenshot that contains an unrelated error banner should fail capture/validation before it reaches a reviewer.
- Require side-by-side state discrimination checks for default/hover/pressed/focus/disabled/busy/active/destructive, judging native rendered results rather than CSS rule existence.
- Require a claim-to-evidence matrix so each review claim has the correct evidence class; missing native proof should be detected locally.
- Prefer deterministic assertions and fail-closed capture helpers for known state prerequisites; do not generate nominally “healthy” evidence when the required native state was not reached.
- Use external reviewers for independent product judgment and blind spots after local QA, not for routine defect discovery that can be settled by local screenshots, recordings, performance traces, or state assertions.
promotion_gate: replay this workflow on Bobbio 0.3 and at least one additional UI-heavy project; if it reduces external review loops without lowering quality, promote it into the Frontend Design production review workflow.

### Freeze whole-screen visual direction before implementation polish
status: NEW
source: Bobbio 0.3 repeated native UI rejection after locally green functional/performance gates, 2026-09-14
target layer: Frontend Design planning / full-screen composition / implementation handoff
problem: Repeated local repairs optimized individual defects without first freezing the whole-screen composition and component grammar. This produced obviously arbitrary visual decisions in an otherwise functional app: a large decorative `Choose a paper` circle with no semantic role, sibling controls such as `Change paper` and `Retry PDF` rendered in visibly unrelated styles despite adjacent placement, duplicated `Choose a paper` messaging, mismatched control weights, and locally polished components that still did not form a coherent product. The user was repeatedly forced into the role of art director, pointing out visual incoherence one screenshot at a time. The failure is not one bad button; it is the absence of a mandatory design-before-code gate for the entire screen.
candidate_action:
- Before implementation polish, freeze a **screen-level visual brief** for every primary state: shell, empty Reader/paper picker, loaded Reader, current selection, Explanation, Candidate/history, annotation mode, loading/error/recovery. The brief must define visual hierarchy, dominant task, control grouping, spacing rhythm, density, and what is intentionally absent.
- Require one canonical component grammar before coding: button families, size scale, icon family, border/radius system, surfaces, pills, tabs, inputs, destructive treatment, and motion. Adjacent controls of the same semantic level must use the same family unless a documented hierarchy difference justifies otherwise.
- Ban arbitrary decorative geometry in production UI. A circle/blob/card/accent shape must have a clear semantic, navigational, status, branding, or interaction role. “It fills empty space” is not a valid reason. Decorative shapes that call attention without meaning are a production defect.
- Add a **sibling-control consistency** check: controls that are spatially grouped must be compared side-by-side for height, padding, icon treatment, radius, border, typography, and interaction states. `Change paper` beside `Retry PDF` cannot accidentally look like two unrelated design systems.
- Treat repeated labels/CTAs as a whole-screen defect. One action should not appear as header copy, pill, title, and button unless each occurrence serves a distinct user need.
- Require a full-window native screenshot review at normal scale before accepting component-level evidence. The reviewer must answer: does this look intentionally designed as one product, or like individually repaired widgets accumulated over time?
- Use the canonical design artifact (Figma/reference frame/design board) as the implementation target when one exists. Implementation should compare native screenshots against the approved reference, not improvise during coding.
- Introduce a **visual freeze → implementation → native comparison** loop. Do not ask the user to review until the producer has compared every primary native screen to the frozen visual direction and found zero obvious composition/component inconsistencies.
- External review should happen only after the producer can defend every visible shape/control: why it exists, why it has that visual weight, and why neighboring controls differ. If the answer is “because that was the easiest CSS/markup,” the screen is not review-ready.
- Add an explicit ban on using the user as iterative visual QA. The product team/agent must perform the full-screen design pass first; user review is for final taste/product judgment, not discovering arbitrary circles, inconsistent siblings, repeated CTAs, or basic spacing mistakes.
promotion_gate: treat this as immediately applicable to Bobbio; validate on at least one additional UI-heavy project before promoting the exact checklist into the generic Frontend Design production contract. The underlying principle—freeze whole-screen visual direction before code polish and never use the user as first-line art direction—should be considered high-priority for promotion.

### Canonical design artifacts must gate production implementation
status: NEW
source: Bobbio 0.3 Figma rebase after whole-screen UI rejection, 2026-09-14
target layer: Frontend Design source-of-truth governance / Figma-to-code / visual regression
problem: A project can already have an approved Figma/component system and still drift badly if implementation treats it as inspirational rather than normative. Bobbio had a canonical Figma Reading Focus direction, yet production code invented missing states directly in React/CSS. The result was local functional success but system-level visual drift: arbitrary decorative geometry, inconsistent sibling controls, random spacing values, repeated CTAs, and different component grammars across states. The missing workflow rule is that canonical design artifacts must block implementation until the required states and components actually exist in the design source of truth.
candidate_action:
- When a canonical Figma/design file exists, classify it explicitly as **production visual source of truth**, not a moodboard. Production UI changes that materially alter hierarchy, component grammar, spacing, or primary states must be represented there first.
- Before coding a UI milestone, build a **primary-state coverage matrix**. Every user-visible state that will be shipped (empty, loaded, selection, explanation, candidate/history, active tools, loading, error/recovery, responsive variants, important transitions) must have a design target. Missing states are a design gap, not permission for implementation improvisation.
- Require a **Figma/design freeze gate** before production implementation: whole-screen hierarchy, component families, spacing scale, typography, surfaces, colors, motion intent, and responsive behavior must be internally coherent and self-reviewed at normal window scale.
- Freeze shared design tokens before coding. Avoid selector-by-selector arbitrary values for spacing, radius, control height, borders, typography, and motion. New values outside the token system require an explicit reason rather than convenience.
- Require full-screen Figma-to-native comparison after implementation. Compare complete screens, not only component crops, and record layout, typography, spacing, hierarchy, component family, responsive behavior, and intentional deviations.
- Treat unrecorded visual deviation from canonical design as a defect. “Roughly similar” is not sufficient when the project has a deliberate source-of-truth artifact.
- Add a **design debt fail-fast** rule: if the implementation needs a production state absent from Figma, stop and extend the canonical design first. Do not encode the missing state directly in CSS and promise to reconcile it later.
- Require final design convergence to cover at least one compact/laptop viewport and the canonical desktop viewport before external review; a design that only works at one screenshot size is incomplete.
- Preserve functional and accessibility contracts during Figma rebase, but do not let legacy DOM/CSS structure dictate the visual solution. Existing implementation is a behavior substrate, not a design constraint.
- The goal should be end-to-end: **design update → internal design self-review → production implementation → native full-screen comparison → adversarial self-review → external confirmation**. Do not terminate a UI goal after only Figma or only code is complete.
promotion_gate: immediately use this workflow for Bobbio 0.3. Validate the exact gate on at least one other project with a canonical design artifact before making every clause mandatory across Frontend Design.

### Visual acceptance must include a whole-product taste gate, not only defect checklists
status: NEW
source: Bobbio 0.3 weekend UI convergence failure, 2026-09-14
target layer: Frontend Design final visual QA / product taste / user handoff
problem: Even increasingly strict defect checklists can still produce an interface that technically passes local gates while obviously looking incoherent or unfinished at first glance. The missing layer is a deliberate whole-product taste review: does the screen feel intentional, calm, balanced, and like one product? Users should not be forced to identify elementary visual problems one screenshot at a time after the producer has already declared readiness.
candidate_action:
- Add a final **whole-product taste gate** after functional, component-state, and evidence-integrity checks. Review complete native screens at normal scale and ask whether the interface looks intentionally designed without reading implementation rationale.
- Require the producer to explicitly search for arbitrary visual gestures: circles/blobs used only to fill space, over-large empty regions, repeated CTA language, mismatched sibling controls, over-promoted maintenance actions, excessive pills/cards/borders, accidental typography mixing, and inconsistent density.
- A whole-screen UI with zero overflow and correct hover states can still fail P2 if its composition visibly looks ad hoc, placeholder-like, or AI-generated.
- Require a **visual hierarchy explanation** for each primary screen: dominant task, primary action, secondary actions, quiet content, historical content, and intentionally absent controls. If hierarchy cannot be explained simply, the screen is not frozen.
- Add an explicit “first-glance rejection” pass: inspect each screen for 2–5 seconds at normal scale. If an experienced reviewer immediately notices something obviously arbitrary or inconsistent, do not proceed to user review even if detailed checklists are green.
- User review should be reserved for final product/taste judgment and preference decisions, not elementary design-system cleanup. The producer must reach zero obvious P2 visual defects before asking the user to look again.
- When a user has explicitly rejected iterative visual QA, treat further user-facing screenshots as blocked until the producer completes the full design → implementation → native comparison loop.
promotion_gate: high-priority candidate for Frontend Design. Validate whether this reduces repeated UI repair loops on Bobbio and at least one other design-heavy product, then promote into the generic final visual-review contract.

### Design corrections must round-trip through the canonical Figma before code changes
status: NEW
source: Bobbio 0.3 canonical-Figma drift and repeated code-only visual repair, 2026-09-14
target layer: Frontend Design repair workflow / Figma governance / implementation discipline
problem: Having a canonical Figma file is not enough if later visual feedback is repaired directly in React/CSS. That creates two sources of truth: Figma remains nominally approved while production becomes a sequence of undocumented visual patches. Bobbio repeatedly hit exactly this failure mode: a screen was rejected, the code was patched locally, but the canonical design was not updated first, so the next state inherited fresh inconsistencies. A mature workflow needs a mandatory round-trip rule whenever a visual defect is found after implementation begins.
candidate_action:
- Classify every UI defect before editing code: **design defect**, **implementation drift**, **product/interaction semantics defect**, or **runtime-only defect**.
- For a **design defect** (hierarchy, composition, spacing system, component family, typography, visual weight, responsive layout, motion grammar), update and re-review the canonical Figma first. Production code may change only after the corrected design is frozen.
- For **implementation drift** (production differs from an already-correct frozen Figma), keep Figma unchanged and change code only to converge to the canonical design.
- For a **product/interaction semantics defect**, update the product contract and Figma state/flow first, then implement. Do not let code silently redefine the interaction model.
- For a **runtime-only defect** (race, stale state, integration failure, performance bug) that does not change intended visual semantics, fix code directly but re-run native visual regression afterward.
- After any visually material repair, the workflow must loop back through **Figma design state → production implementation → native full-screen comparison**. A code-only patch that materially changes appearance without a corresponding design decision is not review-ready.
- Record intentional deviations in the Figma/native comparison artifact. If a deviation cannot be explained as a platform constraint, accessibility requirement, or explicit product decision, treat it as drift.
- Do not mark a design milestone “done” while production still implements an older visual revision, and do not mark production “done” while Figma still describes a rejected screen. Design and implementation must converge in the same goal.
- Require the final handoff to identify the exact canonical Figma frames/states used to implement each primary production screen so later repair work knows which design artifact must be updated first.
- Prefer Code Connect/component mapping or an equivalent explicit component-to-design mapping where it materially reduces drift; the point is not tool ceremony but preserving one component grammar across design and code.
promotion_gate: treat as immediately mandatory for Bobbio. Validate on another Figma-driven product before promoting the exact defect-classification taxonomy as universal, but preserve the core rule now: material visual repairs must round-trip through the canonical design source rather than bypass it in CSS.

### “Figma complete” needs an explicit definition of done
status: NEW
source: Bobbio 0.3 redesign/implementation mismatch, 2026-09-14
target layer: Frontend Design planning / Figma completion / handoff quality
problem: Teams can say “the Figma is done” when only hero/default screens are polished, while production still needs empty, error, loading, history, transition, compact viewport, focus/pressed, or recovery states that were never designed. The implementation then invents those states ad hoc, and the canonical design becomes incomplete the moment coding starts. The definition of Figma completion must therefore be state- and interaction-complete, not screenshot-complete.
candidate_action:
- Define Figma completion as **coverage + grammar + interaction intent + responsiveness + self-review**, not the existence of a few attractive frames.
- Require a primary-state matrix before implementation: default, empty, loaded, current selection, output/result, history/persistence, loading/busy, error/recovery, important transitions, destructive actions, and any active-tool modes that will ship.
- Require at least the canonical desktop viewport and one compact/laptop viewport for each layout that materially changes with size. Responsive notes alone are insufficient when the compact state changes hierarchy or control density.
- Include component interaction states where they affect perceived behavior: hover, pressed, focus-visible, disabled, busy/loading, selected/active, destructive. They may live in component variants rather than separate whole-screen frames, but they must be frozen before implementation.
- Include motion intent in the design handoff: which transitions animate, approximate duration/easing class, what remains stationary, and reduced-motion behavior. Motion must not be invented after implementation is otherwise complete.
- Include content density/long-content examples for panels, lists, inspectors, history, and error text; a design that only works with short placeholder copy is not complete.
- Include platform-shell constraints for desktop products when titlebar/taskbar/shortcut/native chrome materially affect the final composition.
- Require an internal Figma self-review at normal scale before coding. The producer should attempt to reject the design for repeated CTAs, arbitrary decoration, mismatched sibling controls, dead space, over-carded layout, typography drift, and weak hierarchy.
- Figma completion must produce a durable handoff record: canonical frames, component families, tokens, responsive states, interaction states, intentional omissions, and any states explicitly deferred from the current milestone.
- Implementation may start only when the Figma self-review is P1=0/P2=0 for the current milestone. If a missing state is discovered later, implementation pauses and the design source is extended first.
promotion_gate: high-priority generic candidate. The exact list of mandatory states can vary by product, but the rule that “Figma done” means all shipped primary states and interaction grammar are covered should be promoted broadly.

### Design-to-code goals must not stop at either Figma or implementation
status: NEW
source: Bobbio 0.3 weekend redesign failure and repeated review loops, 2026-09-14
target layer: Frontend Design goal construction / delivery workflow / visual QA
problem: Splitting UI work into “design first, implementation later, QA later” allows each phase to declare success while the product remains visibly inconsistent. Conversely, jumping directly to implementation produces design drift. For design-heavy milestones, the useful unit of completion is the entire closed loop, not one artifact.
candidate_action:
- Construct UI goals as one closed loop: **Figma update → Figma self-review → production implementation → release/native capture → Figma/native full-screen comparison → adversarial producer review → external confirmation**.
- Do not allow the goal to return success after only Figma is polished, after only code compiles, or after only browser screenshots look correct.
- If native comparison reveals a **design problem**, return to Figma, update the canonical design, re-freeze it, then re-implement. If it reveals **implementation drift**, keep Figma fixed and repair code. Do not patch both arbitrarily until screenshots “look better.”
- Require whole-screen comparison for every primary state, not only representative component crops. Components can pass individually while the screen still fails composition, hierarchy, density, or spacing.
- Require functional/performance regression in the same goal: visual redesign cannot be accepted if it reintroduces jank, flicker, overflow, stale state, or broken integration flows.
- The producer should not ask the user to review until this closed loop is locally green. User review is a final product judgment, not a phase transition between Figma and implementation.
- External reviewers should confirm the converged result, not discover that the design and code describe different products.
promotion_gate: immediately mandatory for Bobbio; strong candidate for generic Frontend Design workflows where a canonical design artifact exists.

### Normal UI must have a human-readable presentation boundary
status: NEW
source: Lucerna production acceptance review, 2026-09-17
evidence: `YuukiAS/Lucerna@461dcea4015434f90d50922d9b7ae054286c98bc` plus user-provided release screenshots showing raw Longleaf/Slurm/recovery text such as `status=online`, `controller=available; partition=mixed`, `canonical-longleaf-bridge`, raw exit-code details, and internal recovery IDs in the normal UI
problem: The frontend rendered backend/runtime diagnostic strings directly into production copy. Technically truthful provider fields became unreadable user-facing prose, forcing the user to understand implementation contracts instead of product state.
project-specific context: Longleaf, Slurm, Bridge A/B and their exact contract fields are Lucerna-specific. The reusable frontend issue is the missing presentation layer between structured runtime state and normal product copy.

### Primary surfaces should optimize for actionability, not implementation completeness
status: NEW
source: Lucerna production acceptance review, 2026-09-17
evidence: user-provided release screenshots where healthy/usable Longleaf status was followed by expanded recovery, scheduler, Bridge internals and other low-actionability operational detail in the main information flow
problem: The interface promoted diagnostic and maintenance information merely because it existed. Routine status, actionable exceptions, recovery tools, scheduler diagnostics and extensions were not separated by user need, so the compact utility became an operations dashboard that increased cognitive load during normal use.
project-specific context: Lucerna specifically wants recovery, diagnostics and optional extensions under a collapsed bottom area. Other products may choose different placement, but the generic issue is that low-frequency maintenance tooling should not compete with the primary task unless it is currently actionable.

### Metric labels and rankings must be backed by the data semantics they imply
status: NEW
source: Lucerna GitHub Actions resource review, 2026-09-17
evidence: `YuukiAS/Lucerna` GitHub Actions implementation used a deduplicated alphabetically sorted repository list and displayed the first item as `Top`, while the user expected actual usage ranking and separate overall/private views
problem: The frontend presented a strong analytical label (`Top`) without a matching aggregation/ranking contract. A visually plausible label hid a semantic data error. Frontend/product work needs to treat ranking, filtering, scope and denominator as part of the visible UI contract, not as incidental backend details.
project-specific context: Lucerna's public-vs-private GitHub Actions quota semantics are product-specific. The generic issue is that labels such as `top`, `highest`, `remaining`, `share`, or `risk` must correspond to explicit computed semantics and must not be inferred from array order or convenience fields.

### Comparable resource cards need one coherent progress and reset grammar
status: NEW
source: Lucerna resource-card polish, 2026-09-17
evidence: user-provided release screenshots showing Codex, GitHub Actions, VPS bandwidth and Longleaf lease information using inconsistent combinations of bucket labels, percentages, reset text, remaining values and progress bars
problem: Comparable quota/lease resources were each rendered with different copy and visual conventions. Some exposed provider bucket names, some duplicated usage text, and reset/expiry meaning was not visually standardized. The user had to relearn the same concept for every card.
project-specific context: Lucerna prefers a compact used-versus-remaining status bar plus a consistent reset/expiry line. The exact colors and card density are project-local; the generic issue is that semantically comparable resources should share a stable visual/copy grammar.

### Opaque identifiers and formatting artifacts must not leak into glanceable UI
status: NEW
source: Lucerna OpenAI/resource acceptance review, 2026-09-17
evidence: user-provided release screenshots showing raw `proj_...` project identifiers, mixed time formats/timezones, and negative-zero currency such as `-$0.00` in glanceable production UI
problem: Machine-oriented identifiers and low-level formatting artifacts were technically valid but visually noisy and confusing. The normal UI did not distinguish human labels from diagnostic identifiers, and formatting normalization was treated as optional polish rather than part of production quality.
project-specific context: OpenAI project IDs and Lucerna's exact time/currency fields are project-specific. The reusable issue is that primary UI should prefer human-readable aliases/names, normalized zero values, and one deliberate date/time convention, while raw IDs remain available only in details/diagnostics when needed.

### Severity colors must encode one stable semantic meaning
status: NEW
source: Lucerna Usage card visual acceptance review, 2026-09-17
evidence: user-provided release screenshots where an OpenAI Usage card labeled `NORMAL` used an amber/yellow warning treatment while other healthy states used green
problem: Status text and status color communicated different meanings. Reusing an attention/warning palette for a normal state weakens the entire severity system because users can no longer infer whether color reflects health, category branding, or decoration.
project-specific context: Lucerna specifically prefers green for normal, amber for attention and red for critical. Exact hues are project-local; the generic issue is that semantic status colors must be globally consistent and should not be repurposed decoratively on the same surface.

### Native interaction acceptance must prove the intended control path, not only the final window state
status: NEW
source: Lucerna titlebar-close false-positive acceptance, 2026-09-17
evidence: `YuukiAS/Lucerna@461dcea4015434f90d50922d9b7ae054286c98bc` reported physical close PASS from a coordinate-based smoke because the window became hidden, while the user still could not close the release by clicking the visible X; the app also had focus-loss/outside-click hide routes that could satisfy the same final-state assertion
problem: The black-box test verified an outcome (`window hidden`) but not its cause (`the visible X received real pointer input and triggered the canonical close path`). Multiple valid hide routes allowed a false positive to pass and prematurely moved the product to user acceptance.
project-specific context: Lucerna's hide-to-tray titlebar control and exact coordinates are project-specific. The reusable frontend QA issue is that interaction acceptance should identify the actual rendered hit target and, when competing routes can produce the same final state, prove the intended control/event path rather than infer causality from the outcome alone.

## Watch boundaries

- One product's visual taste is project-local unless repeated or explicitly adopted as a long-term cross-project preference.
- Runtime bugs belong to the app/repo or build capability, not automatically to this plugin.