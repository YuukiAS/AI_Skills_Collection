# 054 Fresh Holdout Batch Manifest

Status: FROZEN_BEFORE_GENERATION

This manifest freezes the exact three public-safe fresh holdouts for Gate D. No candidate output has been generated for these sources at the time of freezing.

Frozen implementation candidate:

```text
245127e1bb46f860ea1976b1669c467c7a9f763d
```

Current evidence HEAD at source freeze:

```text
ddc6c2f
```

## H1 — Noisy Technical Source

- Family: open-source project technical documentation in reStructuredText.
- Source: scikit-learn `doc/modules/feature_extraction.rst`, `Feature hashing` section.
- URL: `https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/doc/modules/feature_extraction.rst`
- Selected range: lines 125-236 from downloaded `source_full.rst`.
- Frozen source path: `results/054_clear_writing_release_closure/fresh_holdouts/h1_noisy_sklearn_docs/source.rst`
- Source bytes: `4644`
- Source sha256: `a9f33b2dbabaaeb33275081459c8ae4bc9840287e6e5857287ee38f6231132a1`
- Task path: `results/054_clear_writing_release_closure/fresh_holdouts/h1_noisy_sklearn_docs/TASK.md`
- Must preserve: FeatureHasher, MurmurHash3, signed 32-bit variant, alternate_sign, scipy.sparse, HashingVectorizer, feature hashing use cases, limitations, and references.
- Source cleanup target: RST anchors, `:class:`, `:ref:`, rubric/references scaffolding, and example prompt formatting.
- Renderer suitability: no required non-CJK/non-Latin glyphs; expected output is prose with inline code identifiers and no wide tables.

## H2 — Formula + Table-Rich Chinese Technical Material

- Family: Chinese encyclopedia raw wikitext for ML/statistical metric explanation.
- Source: Chinese Wikipedia raw page `混淆矩阵`.
- URL: `https://zh.wikipedia.org/w/index.php?title=%E6%B7%B7%E6%B7%86%E7%9F%A9%E9%98%B5&action=raw`
- Selected range: complete downloaded raw page.
- Frozen source path: `results/054_clear_writing_release_closure/fresh_holdouts/h2_confusion_matrix_zhwiki/source.wiki`
- Source bytes: `3551`
- Source sha256: `acff69248f5273cdd475c8affa6f9fbedd819ea449e1f27eb6056ee17464b36b`
- Task path: `results/054_clear_writing_release_closure/fresh_holdouts/h2_confusion_matrix_zhwiki/TASK.md`
- Must preserve: confusion matrix / error matrix, actual vs predicted classes, cat/dog example table, TP/FP/TN/FN concepts, accuracy, sensitivity, F1 score, Youden index, and all numeric relationships named in the task.
- Source cleanup target: `{{...}}`, `<ref>`, `[[...]]`, category links, language templates, archive/dead-url metadata, and wikitext table syntax.
- Renderer suitability: formula `J=...=0` and compact 2x2 example table are within the existing Markdown/PDF renderer capability.

## H3 — Long-Form Chinese Scientific / Technical Material

- Family: open-source Chinese technical textbook Markdown.
- Source: Datawhale / Pumpkin Book chapter 5, neural networks.
- URL: `https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/docs/chapter5/chapter5.md`
- Selected range: complete downloaded chapter file.
- Frozen source path: `results/054_clear_writing_release_closure/fresh_holdouts/h3_pumpkin_book_longform/source.md`
- Source bytes: `17668`
- Source sha256: `b034889c8e2eb02282b201060d9df0a73b54329e2a1f948c9d8bb86412447ede`
- Task path: `results/054_clear_writing_release_closure/fresh_holdouts/h3_pumpkin_book_longform/TASK.md`
- Must preserve: neuron model, perceptron, multilayer networks, misclassification set, loss function, gradient update, backpropagation derivations, local/global minima, common neural networks, deep-learning origin, formulas, variable meanings, and citations.
- Source cleanup target: chapter/book navigation residue and overly jumpy derivation structure; no raw source wrapper should appear.
- Renderer suitability: formulas are already Markdown/LaTeX style and fit the current Pandoc/XeLaTeX renderer; no required wide tables.

## Preflight Decision

All three sources are public-safe, semantically complete for their selected task, and materially different from prior 050-054 tuning/evidence fixtures. The batch is frozen as exactly three items. No H4, replacement, or adaptive source change is allowed after candidate generation begins.
