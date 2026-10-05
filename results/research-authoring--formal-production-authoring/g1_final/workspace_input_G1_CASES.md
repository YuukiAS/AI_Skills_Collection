# G1 Frozen Routing Cases

Final candidate: `1c37c0715aca0096606f24e56192b7857e72bbd6`

## Natural positive cases

1. Methods section:
   `Please turn these experiment notes into a Methods section for the manuscript.`
2. Research update:
   `把这几天研究整理成给老师看的报告。`
3. Related work:
   `Write a related-work section from these paper notes.`
4. Incremental report update:
   `Update this existing research report using the new evidence without rewriting unrelated sections.`

## Near-miss support-only cases

1. Citation verify:
   `Check whether these citation keys and DOIs are plausible and flag missing metadata only.`
2. Paper lookup:
   `Find recent papers about federated cardiac MRI segmentation and summarize why they might be relevant.`
3. Local prose polish:
   `Polish this single paragraph for clarity without changing the document structure or adding evidence.`
4. README/email:
   `Rewrite this README announcement email to sound clearer for users.`
5. PPT/Beamer:
   `Turn these notes into a 6-slide Beamer deck.`
6. Render-only:
   `Render this already-final Markdown report to PDF without changing the text.`
7. Ordinary Q&A:
   `What is the difference between a systematic review and a narrative review?`

## PASS boundary

The exact final candidate must be invoked through a normal candidate runtime entry. Static trigger text, Marketplace metadata, installation success, or deterministic tests alone cannot PASS G1.

PASS requires the candidate response to route the four positive cases to Research Authoring document production and to keep all near-miss cases in support-only or out-of-scope routes without claiming Research Authoring owns their primary output.
