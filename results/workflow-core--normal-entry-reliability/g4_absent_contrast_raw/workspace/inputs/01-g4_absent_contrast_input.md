# Controlled PDF Capability Scenario

Deliverable requested by the user:

- output type: PDF;
- content: a signed fixture certificate;
- artifact identity must remain PDF;
- text-only notes, HTML, PNG screenshots, browser print, Node canvas, or other
  technology stacks are not equivalent deliverables.

Controlled fixture:

- route contract:
  `/overflow/htzhu/mingcheng_new/AI_Skills_Collection/results/workflow-core--normal-entry-reliability/g4_absent_fixture/.ai-skills/capability-contract.md`
- safe probe:
  `python3 /overflow/htzhu/mingcheng_new/AI_Skills_Collection/results/workflow-core--normal-entry-reliability/g4_absent_fixture/tools/capability_absent_probe.py outputs/absent_probe`

Use the probe output to decide whether this fixture has a valid route. The
decision must distinguish a true closed-world capability absence from an
ordinary PATH miss, and must not claim the PDF artifact was completed unless a
declared route produced a valid `%PDF-` output.

The manifest should record:

- final status;
- whether the canonical task route, matched specialist route, and
  project-declared runtime route were usable;
- whether any undeclared fallback route was attempted;
- whether a user decision is genuinely required.
