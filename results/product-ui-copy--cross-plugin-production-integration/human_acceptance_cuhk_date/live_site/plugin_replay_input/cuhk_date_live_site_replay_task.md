# CUHK Date Live Site Product UI Copy First-Pass Review

You are evaluating the current public CUHK Date / Meet at CU website for human acceptance of the exact Product UI Copy production candidate.

Candidate commit:

`a06ff050bc82bb22358dfcb3e4faa885fddd285b`

Use the normal workflow:

Frontend Design -> Product UI Copy -> Frontend rendered acceptance.

Important phase boundary:

- This is Phase 1 blind live-site review.
- Do not use or infer from the 2026-09-26 historical CUHK Date audit.
- Use only the attached live public-site capture inputs.
- Do not log in, register, submit forms, call private APIs, or use CUHK Date repository/source as an input.
- Do not tune plugin behavior, modify source files, or create a new holdout.

Inputs contain public page URLs, locale, rendered DOM text, screenshot locators, and capture time. Review reachable public pages only; register/login routes may be reported as unavailable if the capture says they are 404.

For each page, first make a page-level Frontend Design judgment:

1. What visible text needs to exist.
2. What each block is doing: badge, heading, body, CTA, legal disclosure, support instruction, navigation, footer, or system state.
3. Whether badge / heading / body / CTA repeat the same state.
4. Whether ordinary status is written like a slogan.
5. Whether internal product, engineering, or legal state leaks into public copy.
6. Which issues are KEEP, WORDING/NATURALNESS, LOCALE/REGISTER, CONTENT ARCHITECTURE, PRODUCT SEMANTICS, or LEGAL/TRUST/SAFETY.
7. Which parts should be deleted or merged instead of rewritten.
8. Whether zh-Hans and zh-Hant-HK are independently natural.
9. Which product facts are insufficient and cannot be finalized.

Then let Product UI Copy handle only the safe wording changes under protected meaning. Preserve page context. Do not beautify isolated sentences.

Write these files under `outputs/`:

1. `LIVE_SITE_COPY_REVIEW.md`
   - concise but specific page-level review;
   - representative before -> proposed result examples;
   - at least 20 real examples across KEEP / rewrite / architecture / escalation;
   - at least 3 CONTENT ARCHITECTURE cases;
   - at least 3 PRODUCT / LEGAL / TRUST escalation cases;
   - separate zh-Hans and zh-Hant-HK observations;
   - rendered acceptance notes based on the captured screenshots/DOM evidence limits.

2. `PLUGIN_CONSUMPTION_EVIDENCE.md`
   - candidate commit;
   - state that this is Phase 1 blind live-site input;
   - confirm web-development 0.4 and writing-style 0.4 were used in the same replay session;
   - list input file identities and output file identities;
   - state that historical audit evidence was not used as candidate input.

Keep the answer in natural Chinese, with only necessary technical tokens.
