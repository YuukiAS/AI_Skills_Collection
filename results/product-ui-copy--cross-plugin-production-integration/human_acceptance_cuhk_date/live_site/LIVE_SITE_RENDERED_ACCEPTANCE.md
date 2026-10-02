# CUHK Date Live Site Rendered Acceptance Notes

This file is part of Phase 1 blind live-site acceptance. It uses only the
current public CUHK Date screenshots captured during this run, plus the DOM/text
capture already saved in this directory. It does not use the 2026-09-26
historical audit.

Candidate commit:

`a06ff050bc82bb22358dfcb3e4faa885fddd285b`

Capture time:

`2026-09-29T13:47:43+08:00`

## Screenshot Coverage

Ten public pages were captured at 1440 x 1800:

- `zh-Hant-HK_home.png`
- `zh-Hant-HK_how-it-works.png`
- `zh-Hant-HK_privacy.png`
- `zh-Hant-HK_terms.png`
- `zh-Hant-HK_support.png`
- `zh-Hans_home.png`
- `zh-Hans_how-it-works.png`
- `zh-Hans_privacy.png`
- `zh-Hans_terms.png`
- `zh-Hans_support.png`

The requested register and login routes were probed separately and returned
404 for both `zh-Hans` and `zh-Hant-HK`; no register/login page screenshots are
claimed beyond that route result.

## Rendered Findings

- Home: hero heading, CTA buttons, flow blocks, boundary list, and non-official
  disclosure are readable. The page visually confirms the Product UI Copy
  finding that the current-open state and "prepare profile first" message appear
  close together and should be consolidated before further wording polish.
- How it works: the four-step structure is readable and matches the DOM text.
  The screenshot confirms this page is a genuine process explanation, not a
  marketing-only page; step titles can be reviewed as UI roles rather than
  isolated sentences.
- Privacy: cards are readable. The screenshot confirms the internal phase
  phrase "第一批真实用户前 / 第一批真實用戶前" appears as a visible page eyebrow,
  so it is not merely metadata from the DOM extraction.
- Terms: cards are readable. The screenshot confirms the same internal phase
  wording appears visibly and that legal/status uncertainty sits in the main
  page body, so Product UI Copy should escalate rather than hide it.
- Support: support paths, reporting, deletion, and emergency-situation text are
  readable. The emergency boundary is visible on the captured page, but any
  desired prominence change should be judged in the real responsive viewport
  before shipping.

## Evidence Boundary

These screenshots prove the current public browser-rendered pages are reachable
and readable at the captured desktop viewport. They do not prove login,
registration, account flows, mobile breakpoints, live form behavior, or any
backend/project-level binding. They also do not apply the proposed copy to the
site; they only support the first-pass review of current visible copy and page
structure.
