# Pre-final output-contract development failure

Candidate commit: `07f6587128d5c3db70b3fea1ae892ffe589291ca`

Runtime tree Git identity: `5f93c1d2f11e6a2f0333f4893cfe8db1687bf8ec`

Observed sessions:

- small bounded edit: `01a14e00-2ae3-7b50-ab58-eda7c2826341`
- explicit-empty greenfield: `01a14e00-7b4e-7d01-a41a-3ed68f7c8f44`
- explicit reset: `01a14e00-dc56-7021-a27c-cb906f29b35e`
- genuine no-op: `01a14e02-f259-7fe0-9b38-c40e550a78a1`
- G3 fidelity: `01a14e03-431f-7570-9d3e-714739d252e0`
- G4 representative task: `01a14e04-207a-7b30-9e0f-f2df18e604dd`

Findings:

- `explicit reset`, `no-op`, and the G3 fidelity case preserved their semantic contracts.
- The small bounded edit omitted the frozen baseline receipt and described the insertion instead of rendering the actual Markdown preview.
- The greenfield case included the receipt but described the new section instead of rendering the actual Markdown preview.
- The representative G4 case returned a clean replacement and a change summary, but no actual strikethrough/bold Markdown preview and no frozen baseline receipt.

Disposition: `FAIL`. Summary prose is not preview `R`; the receipt, actual `R`, and clean `C` order must be made explicit before a new final candidate is frozen. This commit is not reused for final Gate evidence.
