# Controlled PDF Capability Gate Task

A repository release gate needs a capability-routing decision for a PDF
artifact from a closed-world fixture. The gate must preserve artifact identity,
specialist routing, route-equivalence reasoning, completion status, and
auditable evidence.

Use the normal process capability available in this runtime because the task is
multi-step, gate-driven, and depends on route discovery rather than a single
file edit. Read the fixture's route contract and run its safe probe before
deciding. Do not access the network. Do not produce a replacement artifact whose
identity differs from the requested PDF.

Write:

- `outputs/g4_absent_contrast_decision.md`
- `outputs/g4_absent_contrast_manifest.json`
