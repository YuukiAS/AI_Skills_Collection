---
name: clear-writing
description: Improve ordinary explanations, Chinese documents and source-faithful long rewrites, English scientific prose, and product-interface wording. For an authorized GitHub UTF-8 text-file edit, review the complete document before writing and verify the written file afterward. Preserve exact machine output and domain meaning.
---
# Clear Writing

Use this entry when the user selects Clear Writing. Identify every deliverable
in the request, apply the appropriate packaged writing route to each, and
finish each object independently. The user does not need to select an internal
route. A clear chat reply does not establish that an external document has
been reviewed or changed.

This entry coordinates delivery; the six route references own professional
writing behavior. Read the selected ROUTE.md and its required support files
before applying it. Do not replace that work with a declaration that a route
was used. Do not create another model, service, MCP, App, or persistent ledger.
Domain owners retain scientific, statistical, visual, medical, research-plan,
evidence-selection, and product-semantic decisions.

## Identify The Deliverables

Privately distinguish the objects actually requested in this turn:

- `CHAT_RESPONSE`: an explanation, diagnostic, conclusion, or progress summary.
- `INLINE_DOCUMENT`: a complete document returned in the conversation.
- `EXTERNAL_DOCUMENT`: an identified document to read or edit outside chat.
- `PRODUCT_UI_COPY`: interface wording under frozen product meaning.
- `MACHINE_PAYLOAD`: JSON, YAML, code, commands, logs, or verbatim output.

These are temporary working distinctions, not a schema to save or a checklist
to print. One request can contain several objects. Identify each object's
source, requested operation, audience, protected meaning, and required output.
Do not invent an external target for a chat-only request or write during a
read-only review. For an external document, identify the exact repository,
writable branch, path, and current blob SHA. An immutable commit is a read
source, not authorization to select a writable destination.

## Select And Complete The Existing Routes

Paths below are relative to this Skill directory. Each route's references,
scripts, assets, and evals remain beside its ROUTE.md.

| Deliverable | Required route references, in order |
| --- | --- |
| Ordinary explanation or result summary | `references/routes/response-clarity/ROUTE.md`, with `references/routes/writing-fidelity/ROUTE.md` when protected meaning is involved |
| Chinese document editing or final review | `references/routes/writing-fidelity/ROUTE.md` then `references/routes/chinese-prose/ROUTE.md` |
| Existing Chinese or Chinese-dominant long technical/scientific material requiring structural rewrite | `references/routes/writing-fidelity/ROUTE.md` then `references/routes/scientific-rewrite/ROUTE.md`, with `references/routes/chinese-prose/ROUTE.md` for realization and the final candidate pass |
| English scientific writing | `references/routes/writing-fidelity/ROUTE.md` then `references/routes/scientific-prose/ROUTE.md` |
| Product-interface wording | `references/routes/writing-fidelity/ROUTE.md` then `references/routes/product-ui-copy/ROUTE.md` |
| Exact-only machine output | Preserve its bytes; do not apply natural-language rewriting |

For mixed output, finalize the natural-language objects while preserving the
machine payload exactly. Do not require the user to name a route, a planning
packet, or a validation stage. A request for a complete document still requires
the complete document; rewriting is not permission to substitute a summary.

The heavy rewrite route includes its existing semantic planning, realization,
assembly, mechanical helper, and fidelity checks. Use the packaged helper at
`skills/clear-writing/references/routes/scientific-rewrite/scripts/rewrite_support.py`
according to that route. Resolve this command path against the plugin root. If
the host cannot execute the required helper or finish a required route stage,
report the incomplete route; do not silently skip it and claim completion.

## Use The Shared Final Delivery Contract

For document delivery, actually read and apply
`references/routes/writing-fidelity/references/final-delivery.md` alongside
the selected routes. It owns complete-source coverage, full reviewed
candidate identity, authorized existing-file update or non-overwriting
creation, and full readback plus actual saved-document review. This entry
does not maintain a second version of those rules or of ordinary-answer
content selection; the latter lives in Response Clarity's Workflow.

Apply the shared contract separately to each document. A local file does not
prove GitHub delivery. Missing full source, route/helper access, write access,
or readback cannot be hidden by a polished chat explanation. This plugin
provides no connector, permission, transaction service, or unbypassable hook.

## Finish Each Object Truthfully

Return the requested complete inline artifact or exact payload. For external
edits, briefly explain what changed and whether it was actually written and
verified. Report a chat result separately from each external document's state;
one object's success cannot clear another object's incomplete state. When an
external write cannot be completed, provide an already available complete
candidate and the precise remaining action, without claiming that the target
was modified. Missing full source is not permission to fabricate a candidate.

Use natural reader-facing language for the explanation and retain technical
identifiers where needed for exact location or action. Do not expose internal
route selection as the user's next job. Preserve the established boundary:
this is a writing and delivery contract for the host, not a guarantee of
automatic loading on every turn.
