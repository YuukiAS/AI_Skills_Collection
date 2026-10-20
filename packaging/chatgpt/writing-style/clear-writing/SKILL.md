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

## Bind A GitHub Document To Its Final Candidate

The supported external-finalization surface is a GitHub repository UTF-8 text
file through the host's already connected GitHub tools. Tool names can vary;
use the existing `fetch_file` and `update_file` operations or their host-provided
equivalents with the same source, identity, and expected-blob checks. This Skill
does not provide a connector, authorization, transaction, or unbypassable hook.
Other surfaces may receive a complete candidate, but this version's GitHub
evidence does not establish finalization support for them.

For each authorized GitHub edit:

1. Fetch the complete UTF-8 source and its current blob SHA from the exact
   repository, writable branch, and path. Read every part if the response is
   paginated or truncated; an excerpt, summary, old chat, or cached version
   cannot stand in for the source. If complete source cannot be obtained,
   stop that object as `TARGET_SOURCE_INCOMPLETE`; do not invent replacement
   text and do not write.
2. Bind the target to repository + writable branch + path + blob SHA. Respect
   the user's edit scope and existing tool authorization. Do not write to a
   different repository, branch, or path to get around missing permission.
3. Apply all selected routes to the whole required document. Produce the
   complete final-review candidate before any external write. Compute its
   SHA-256 over the exact UTF-8 bytes that will be written. A proposed diff or
   the chat explanation is not this candidate. If the required full-document
   review or candidate hash cannot be completed, withhold the external write.
4. Immediately before writing, fetch the same branch/path again and compare
   the current blob SHA with the bound SHA. On a difference, stop as
   `TARGET_IDENTITY_DRIFT`; do not overwrite the new content or silently
   rebase the old candidate.
5. Update that exact branch/path with the complete reviewed candidate and the
   bound current blob SHA as the expected source version. Do not fall back to
   an unconditional overwrite. Save the returned commit SHA and content SHA.
   A denied or failed update is `ARTIFACT_NOT_WRITTEN`; the candidate may be
   returned, but the target must not be described as changed.
6. Fetch the same branch/path immediately after the successful update.
   Compare the returned blob SHA with the update's content SHA, and compare
   the complete returned UTF-8 bytes with the reviewed candidate. Confirm the
   repository, branch, and path are unchanged. If readback is unavailable or
   either comparison fails, report `ARTIFACT_FINALIZATION_UNVERIFIED`.
7. Only a successful complete read -> reviewed candidate -> expected-blob
   write -> matching readback permits `ARTIFACT_FINALIZED` for that object.
   Keep the source, candidate identity, update result, and full readback
   accessible for artifact review; hashes alone do not establish prose quality.

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
