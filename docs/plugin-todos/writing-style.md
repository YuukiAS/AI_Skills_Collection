# writing-style — Long-Term TODO

Canonical maintenance inbox for the `writing-style` plugin.

## Open candidates

### Keep style cleanup downstream of scientific structure
status: CANDIDATE_GENERIC
source: real Presentation and advisor-report revisions
evidence: repeated user feedback on AI-like internal language, rhetorical templates and unnatural Chinese
target layer: writing
problem: style rules can accidentally take ownership of scientific structure or artifact mechanics.
candidate action: preserve the current boundary: `writing-fidelity` protects facts, `scientific-prose` / `chinese-prose` polish reader-facing language after evidence/structure are stable.
promotion gate: only add new style rules when repeated across independent real artifacts; do not duplicate research-reporting/presentation structural rules.

## Do not do

- Do not create detector-evasion or generic humanizer behavior.
- Do not let style rewriting change equations, claims, labels, versions or citation meaning.
