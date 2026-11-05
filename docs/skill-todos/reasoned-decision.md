# reasoned-decision — Historical Seed

status: SUPERSEDED_BY_REASONED_DECISION_PLUGIN_ARCHITECTURE

This file preserves the original positive-use evidence and early capability seed. It is **not** an active standalone-skill proposal anymore. The current architecture direction is a dedicated **Reasoned Decision plugin** with a small number of internal skills; do not turn `reasoned-decision` itself into a standalone skill or fold the whole capability into `workflow-core`.

Current frozen architecture:
- responsibilities: `Task State Integrity → Judgment Integrity → Solution Design`;
- runtime spine: clarify goal/current reality → discover existing solution space → judge mature routes → Adopt/Compose/Extend → Build only for proven residual gap → real validation → freeze unless a valid Decision Delta appears;
- governing relation: human problem-solving flow is the spine; prior-art/reuse/Gap Proof/Decision Delta/regressions are guardrails;
- do not create a standalone `search-first` skill.

Current design:
- [Reasoned Decision v0.1 architecture](../design/reasoned-decision/REASONED_DECISION_V0_1_ARCHITECTURE_2026-11-05.md)
- [Windows Edge real negative example](../design/reasoned-decision/evidence/EDGE_WINDOWS_DECISION_FAILURE_2026-11-05.md)


## Open candidates

### Evidence-backed decision with explicit recommendation and stop condition
status: NEW
source: Claude Pro / Persona KYC three-way decision, 2026-11-04
evidence: real user decision among (1) China passport, (2) Hong Kong identity card, (3) abandon Pro and use an API relay; the accepted answer combined official Anthropic/Persona requirements with recent Reddit, V2EX and LINUX DO reports and gave a single preferred option plus a one-attempt stop rule.
problem: High-stakes practical decisions are often answered too conservatively or with symmetric pros/cons, forcing the user to synthesize conflicting evidence themselves. The missing capability should collect authoritative rules and real-world failure/success evidence, distinguish what is known from what is merely reported, then make one recommendation with an explicit reason, confidence boundary and stop condition.
scope examples: product/account/platform choices, software/service selection, migration choices, infrastructure strategy, purchasing, workflow/tool choice, and other reversible or semi-reversible decisions where current external evidence materially changes the answer.
boundary: This capability does not replace domain experts, legal/medical/financial specialists, or research methods. It owns decision synthesis: evidence weighting, uncertainty handling, option elimination, recommendation, and stop/go criteria. Domain plugins remain responsible for domain facts.
project-specific context: The Claude/Persona case below is evidence only. Do not encode Anthropic-specific KYC rules, supported regions, Chinese passport behavior, HKID behavior, or any single forum's claims as generic decision rules.
next research step: refine the dedicated Reasoned Decision plugin architecture, keeping the internal skill set minimal and reviewing overlap with workflow-core, domain plugins, writing-style, prior-art/search-first methods, cross-turn Decision Delta behavior, and the real regression set. Do not create a standalone `reasoned-decision` skill or proliferate helper skills.

## Accepted real-use evidence: Claude Pro / Persona KYC three-way decision

The user explicitly rejected a citation-light answer and required a three-way choice:

1. use a Chinese passport;
2. use a Hong Kong identity card;
3. abandon the subscription attempt and use an API relay.

The successful answer did not simply list pros and cons. It first chose one option, separated official requirements from community reports, clarified the role of a US visa versus a passport, used recent Chinese and English community evidence, rejected an expired document, explained why HKID evidence was weaker for the exact non-permanent case, distinguished KYC success from later account survival, and set a bounded stop condition.

### Full accepted answer

I would choose **1: use your own valid Chinese passport and follow Persona's default passport + live selfie flow; do not use the expired US visa.** But I would bound it to one normal attempt: if the page explicitly enters a 2-of-3-documents mode, or after the passport passes it still forces a second document that the Chinese flow cannot satisfy, stop immediately and switch to the API relay rather than burning more attempts.

I would not choose 3 immediately, because the available evidence does not support the claim that options 1 and 2 are already hopeless. As recently as September–October 2026, multiple Chinese-community users still reported passing Claude/Persona KYC directly with a Chinese passport, including passport + face success and multiple accounts using Chinese passports. At the same time, another group clearly did fall into the 2-of-3 dead end. The right conclusion is therefore not that Chinese passports no longer work, but that the default passport flow is still worth one attempt while the alternate multi-document flow has a real failure mode.

**A US visa is not a required attachment to a Chinese passport for Claude KYC, and Anthropic does not say a foreign passport must be accompanied by a US visa.** Anthropic's current official requirement is a valid, unexpired, government-issued physical photo ID, with examples including passport, driver's/state ID, and national identity card. It does not list foreign-passport-plus-US-visa as a requirement.

Forum users mention US visas because there are community reports where a user photographed the US visa page in the passport rather than the passport biographical page and Persona accepted it. That is evidence that some Persona flows may accept a visa page as a strong government document, but it is not Anthropic's documented standard path.

For this user that route should be discarded anyway: **the US visa is expired.** Anthropic explicitly requires the submitted identity document to be unexpired, so an expired visa should be eliminated from the decision set rather than treated as a symmetric option.

### Why Chinese passport was preferred over HKID

The Chinese-passport situation is strange but relatively well evidenced: there appear to be at least two Persona paths. The normal passport path can succeed with passport + selfie; the alternate government-ID / alternative-verification path can push users into a complete-2-of-3 requirement.

Recent LINUX DO discussions included users who voluntarily entered Anthropic verification and completed it with a Chinese passport, and multiple users in the same period reported Chinese passport + face verification succeeding. Other discussions around October 15–16 described the failure mode where one Chinese passport item passed but the flow then demanded a second credential such as a driver's license or national-ID path that the user could not complete.

The 2-of-3 dead end is not unique to Chinese users. Reddit reports include users in other countries whose first government document passed but Persona still demanded another document, leaving them stuck in verification pending. Other users reported that after an incomplete attempt their verification link expired or could not be cleanly restarted. Anthropic officially says users usually have multiple attempts, but real-world Persona state can still get stuck, so conserving attempts is rational.

Therefore, if choosing option 1, the recommended normal behavior is:

**Select the document issuer truthfully as China → choose Passport → capture the valid physical Chinese passport → complete the live selfie.**

Do not select the United States just because the network exit or payment card is American. KYC document country refers to the issuing authority, not the user's current IP.

If the flow is the normal Passport + selfie path, continue. If it shows alternative verification, 2 of 3, or requires additional driver's-license / national-ID evidence that the user does not actually have for that path, stop rather than trying unrelated countries or mismatched document types.

### HKID: legitimate document, but weaker evidence for the exact case

A normal, non-permanent Hong Kong identity card is still a real government-issued identity document. Hong Kong Immigration explicitly issues identity cards to residents who are not permanent residents, so non-permanent does not mean not-an-HKID. Persona in general supports government-issued national identity cards and similar official identity documents.

There are community reports of Claude/Persona verification succeeding with a Hong Kong identity card, including users who described using a Hong Kong resident identity card and later continuing to use paid Claude plans.

The problem is evidence specificity: the available success reports usually say only HKID or Hong Kong resident identity card. They do not consistently establish that the successful credential was specifically a non-permanent HKID. Therefore the exact case is less directly supported than the Chinese-passport case.

There is also a broader distinction that must not be blurred: **passing Persona identity verification is not the same thing as the account being guaranteed safe afterward.** Community reports include users who passed KYC and were later suspended, and other users who passed and continued normally. KYC success only answers the identity-verification step; it does not guarantee every later account-integrity decision.

### Final ranking

| Option | Decision |
| --- | --- |
| **1. Valid Chinese passport** | **Preferred. It is an officially accepted document type and has the strongest volume of recent real-world success evidence. Use only the default Passport + selfie path; stop if it mutates into a 2-of-3 requirement.** |
| **2. Non-permanent HKID** | **Second choice. The document itself is legitimate and there are Claude success reports, but the evidence is weaker for the exact non-permanent-card case.** |
| **3. Abandon Pro and use the API relay** | **Not necessary before one normal passport attempt. It becomes the default fallback after a failed or structurally blocked first attempt.** |

The final recommendation was:

> **Try the valid Chinese passport once.**
>
> Valid physical passport → China → Passport → live selfie.
>
> Do not submit the expired US visa. Do not treat it as a required second document. Do not proactively enter alternate multi-document verification.
>
> If the normal passport flow fails, or if it becomes a 2-of-3 / additional-document requirement that cannot be truthfully satisfied, stop there and use the already-working API relay rather than continuing to burn time and attempts.

## Durable sources used by the accepted answer

Official:
- Anthropic, Identity verification on Claude: https://support.claude.com/en/articles/14328960-identity-verification-on-claude
- Persona, Can I use a photo of my ID?: https://help.withpersona.com/articles/gyFutFQ7Gxc2I46Ein6QAM/
- Hong Kong Immigration Department, Registration / replacement of HKID: https://www.immd.gov.hk/eng/services/hkid/reg_replace.html

Chinese-community evidence:
- LINUX DO, Chinese-passport KYC discussion / reports: https://linux.do/t/topic/2952017
- LINUX DO, 2-of-3 verification discussion: https://linux.do/t/topic/3027072
- LINUX DO, US-visa-page success report: https://linux.do/t/topic/3042090
- LINUX DO, HKID success report: https://linux.do/t/topic/2422179
- LINUX DO, KYC success followed by later account issues: https://linux.do/t/topic/2952235
- V2EX, Chinese-passport KYC / later account outcome discussion: https://s.v2ex.com/t/1250966
- V2EX, recent KYC trigger / account-environment discussion: https://global.v2ex.co/t/1253660

Reddit / international reports:
- Reddit, Persona multi-document verification dead-end report: https://www.reddit.com/r/Claude_reports/comments/1x735h4/anthropic_support_is_garbage_persona_verification/
- Reddit, ID verification discussion: https://www.reddit.com/r/claude/comments/1xej2fv/questions_about_id_verification/
- Reddit, Persona verification failure / access impact: https://www.reddit.com/r/ClaudeCode/comments/1xf7trb/cant_validate_my_identity_with_persona_i_can_no/

## Candidate capability extracted from this example

1. Make a decision first. Do not hide behind a balanced list when evidence supports a preferred option.
2. Separate authoritative policy, current product behavior, community reports, and inference.
3. Resolve semantic confusion before comparing options.
4. Use real-world evidence to stress-test official policy.
5. Do not overgeneralize anecdotes.
6. Eliminate invalid options early.
7. Include a stop condition.
8. Distinguish immediate success from downstream risk.
9. Cite enough evidence for the confidence level the user needs.
10. Prefer a bounded experiment when uncertainty is material but downside is controlled.
