# Presentations Validator V2

Validate the Git evidence and rendered layout of a presentation candidate. The
program reports objective violations, missing proof, and items for visual
review. Final acceptance belongs to the independent review process.

Use Python 3.10 or newer, Git, PyMuPDF and PyYAML. From this package directory,
install with `python -m pip install .` or run in an environment that already
has the dependencies.

```sh
python -m presentations_validator_v2 validate \
  --repo REPO --authority-bundle AUTHORITY --candidate-bundle CANDIDATE \
  --out integrity.json

python -m presentations_validator_v2 layout \
  --contract CONTRACT.yaml --pdf CANDIDATE.pdf \
  --source-manifest SOURCE.json --source-root SOURCE_ROOT \
  --object-map OBJECTS.json --baseline-pdf BASELINE.pdf --out layout.json

python -m presentations_validator_v2 replay --repo REPO --config REPLAY.json
python -m presentations_validator_v2 inspect
```

Omit `--baseline-pdf` when the map has no protection policy. Supply the five
layout arguments to `validate` for a combined report. The PDF must match a
verified artifact SHA-256 in the Git bundle. The CLI writes JSON to stdout
unless `--out` is supplied. Exit status 1 means deterministic failure, 2 means
insufficient mandatory evidence, and 0 means no deterministic failure or
incomplete gate. Inspect the JSON state for pending `REVIEW` rows even on exit 0.

## Git authority and candidate evidence

Give the validator an authority bundle frozen independently of the candidate.
The CLI reports a canonical SHA-256 of the authority manifest so the caller can
verify it against the freeze receipt. It uses full SHA-1 Git commit, tree and
blob IDs, disables replacement objects and lazy fetching, and reads object
contents from the exact configured commit. GitHub HTTPS and SSH origin URLs
are supported. A historical candidate can be checked while another commit is
checked out. Set `require_head` in authority when the current checkout must
match the candidate, or set `candidate_commit` to freeze a particular replay
target.

| Authority manifest field | Meaning |
| --- | --- |
| `repository`, `baseline_commit` | Frozen repository name and baseline commit |
| `mandatory_source_identities` | Array of `id`, `role`, `path`, `git_blob_sha`, `commit`, `immutable`. Commit is exact or `candidate`; immutable sources must also match at the candidate commit |
| `pages`, `components`, `feedback`, `requirements` | Ordered complete records keyed by `id`. Page `components` and component `consumers` must be inverses |
| `round_scope` | Allowed `pages` and `components` arrays plus a `paths` object mapping Git paths to the affected ID arrays |
| `locks` | Required proof rows, each with `id`, `path`, and frozen `git_blob_sha` |
| `required_objects`, `visible_copy` | Blob proofs with `id`, `path`, and `sha256` |
| `object_decisions` | Explicit relocations or retirements with `id`, `object_id`, `action`, `destination`. A retirement has a null destination |
| `artifacts` | Nonempty array of `id`, `path`, optional exact `sha256`, optional exact `commit` (default `candidate`). Optional `rendered_copy` lists exact extracted PDF text lines page by page |

The authority directory contains `authority_manifest.json`. Supply empty arrays
explicitly for record groups with no applicable rows. The candidate directory
contains:

- `candidate_manifest.json` with `repository`, `baseline_commit`,
  `candidate_commit`, and `candidate_tree`.
- `source_identity_manifest.json` with the exact source tuples and resolved
  commit IDs.
- `derived_feedback_registry.jsonl`, `derived_page_registry.json`,
  `derived_component_registry.json`, and `derived_gate_registry.json` with
  the corresponding complete records in authority order.
- `patch_manifest.json` with `changed_paths`, `modified_pages`,
  `modified_components`, `regression_pages`, `lock_evidence`, and
  `required_object_relocations`. Each change decision includes its
  `authority_record_id`.
- `render_identity_manifest.json` with `id`, `path`, `commit`, and `sha256`
  for each rendered artifact.
- `review_scope.json` with `verdict`, `candidate_commit`, `pages`,
  `components`, `requirements`, `unreviewed_requirements`, and
  `artifact_hashes`. A global PASS claim must cover all four namespaces
  exactly. The caller is responsible for establishing reviewer independence.

Replay config contains `repository` and `locators` with `id`, `commit`,
`path`, and expected `sha256`. A missing object or unfrozen expected digest
returns `NOT_VERIFIED`. A distinct nearby file cannot fulfill a locator.

## Layout evidence

Use the frozen Shared Beamer Core V1 YAML or a separately authorized compatible
contract. Treat the semantic map, any exceptions, the source core hash
allowlist, and mask rectangles as independently supplied evidence. This adapter
does not infer semantic roles from document text. It reads the PDF's actual
span sizes, boxes, baselines, drawing paths, images, and internal link
rectangles. Measurements use top-left PDF coordinates. Pixel tolerances scale
from 1920 pixels across the slide.

The source manifest carries `pdf_sha256`, `entry_source` and a `sources`
array of `id`, relative `path`, `sha256`, and `role` (`authored` or
`pinned_core`). Independently frozen core digests are supplied in the object
map's `pinned_core_sha256` dictionary. The authored inputs are checked for
recognized TeX compression and shrink commands.

The object map carries `pdf_sha256`, the canonical JSON
`source_manifest_sha256`, and one entry per page in `pages`. Each page
has `id`, zero-based `index`, `section`, `objects`, and `spacing`.
An object has `id`, `role`, and indexes into one or more extracted `lines`,
`drawings`, or `images`. Rendered text must have one semantic owner.
Unbound primitives prevent complete validation.

Declare the relevant role relationships on the page or object. The public
tests include concrete examples for each shape.

| Feature | Map data |
| --- | --- |
| Flow and columns | `spacing` edges with `id`, `from`, `to`, `relation`. `columns` entries with `id`, ordered `groups`, `preset`, and `anchor` |
| Captions and tables | Caption and cell `owner`; cell `region` and `atoms`; approved headers may specify `approved_header_lines` |
| Question and answer | Page `qa` entries with `id`, `kind`, `label`, `body`, `rule`, and `accent_rgb` |
| Footer and sections | `footer` with `band`, `credit_role`, `page_label`, and `inset_pdf_pt`; each `section_label` carries its `section` |
| Diagram | Node `style` and `label`; connector `from` and `to`, with `peer_group` if applicable |
| Closing | `closing` archetype, `body_region`, and role-bound cue and upper content |
| Protection | `protection.baseline_pdf_sha256` and per-page `id`, `baseline_index`, `masks` entries. Each mask has `rect` and `kind` (`brand` or `change`) |

The `inspect` command lists the runtime detector hooks and the result of a
limited AST scan for forbidden control selectors. Public regression from the
repository checkout uses `python -m unittest discover -s tests -v` in this
directory. The Beamer fixture test also needs XeLaTeX, Beamer and TeX Gyre
Termes. The archived geometry fixture contains numerical measurements and
font metadata only. It exercises two known historical layout defects without
reproducing course text.
