# PDF Capability Scenario

Deliverable requested by the user:

- output type: PDF;
- content: Chinese prose with one inline math expression;
- artifact identity must remain PDF;
- HTML/PNG screenshots are not equivalent deliverables.

Project facts:

- repository PDF guidance path:
  `/overflow/htzhu/mingcheng_new/AI_Skills_Collection/skills/tools/documents-media/pdf/SKILL.md`
- safe project probe command:
  `python3 /overflow/htzhu/mingcheng_new/AI_Skills_Collection/results/workflow-core--normal-entry-reliability/g4_probe_project/tools/pdf_capability_probe.py outputs/g4_probe`

The ordinary shell PATH check for `xelatex` may be missing even when another
project-supported PDF route exists. The final answer must distinguish that case
from a truly unavailable capability using actual probe output.
