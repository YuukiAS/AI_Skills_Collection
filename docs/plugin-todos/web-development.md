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

## Watch boundaries

- One product's visual taste is project-local unless repeated or explicitly adopted as a long-term cross-project preference.
- Runtime bugs belong to the app/repo or build capability, not automatically to this plugin.
