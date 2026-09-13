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

## Watch boundaries

- One product's visual taste is project-local unless repeated or explicitly adopted as a long-term cross-project preference.
- Runtime bugs belong to the app/repo or build capability, not automatically to this plugin.
