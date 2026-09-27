# STAT5060 Assessment and AI Policy V1

- Status: FROZEN_WORKING_DESIGN_FOR_CODEX. Formal instructor adoption is required for the expressly identified institutional/course-policy items, not for ordinary teaching decisions.
- Date: 2026-09-28.
- Source authority: current user's confirmed 2026 assessment weights; old Syllabus/Final Project/HW1/HW2 as historical evidence; CUHK official sources A01–A05 below; SeminarArc oral-defense roadmap.
- Relation: this file owns assessment boundaries, AI policy and the approval register. HW1 question wording and points are owned by the student spec and rubric. No other file may change these policy decisions by implication.

## 1. Assessment functions and weights

Confirmed for 2026: attendance 20%, Assignment 1 20%, Assignment 2 20%, Final Project 40%. Do not retain the old 10/20/20/50 split. This sprint does not redefine how attendance is recorded or penalized.

**Homework assesses guided independent statistical work.** Students receive a bounded question, prepared data, a taught model vocabulary and reproducibility support. They must formulate an appropriate model, implement it correctly, inspect evidence, compare alternatives, explain uncertainty and transfer a workflow to a changed setting. HW1 is not four loops with new parameter values. Nor is it a miniature open-ended project requiring students to find data, invent a research question and build an unfamiliar model from scratch.

The two assignments together remain consequential at 40%. Correct package output alone cannot earn full marks: diagnostic evidence, prediction targets, reference invariance, exposure sensitivity and simulation calibration carry explicit points. The rubric does not award code length, obscure syntax or a model simply being more complicated.

**HW1 boundary:** independent counts, nominal outcomes, a scalar random-intercept binary model, and a focused simulation about misspecified uncertainty. No required ordinal mixed-model coding, full Bayesian programming, latent mixtures, missing-data modeling or HMM implementation.

**HW2 boundary:** later-course structured/latent or incomplete-data analysis and uncertainty propagation, building on rather than repeating HW1. The old HW2's multilevel variation, mixtures and missingness provide useful scope evidence. Do not release a redesigned HW2 from this sprint: its actual questions/rubric are not frozen here. Deeper Bayesian implementation may belong in HW2/Project, but this file does not silently make Bayesian coding mandatory in a future unapproved HW2.

**Final Project assesses integration and autonomy.** Students find legally usable real data, pose a meaningful question, justify a method, produce a complete reproducible analysis and communicate defensible findings. Oral defense verifies understanding and ownership of the submitted work. Homework cannot supply the same verification under unsupervised AI-assisted conditions, and pretending that a clever homework puzzle is AI-proof would weaken assessment validity.

## 2. Working Final Project design

Total remains 40%. Working split: written project 25% of the course plus oral defense 15%. **INSTRUCTOR_APPROVAL_REQUIRED: the internal 25/15 split**. Do not announce it as an already approved grading change. The confirmed total 40% is not pending.

### Written component: proposed 25-point content rubric

- Research question, data source, sampling/measurement context and ethical/legal use: 4.
- Model formulation, assumptions, identification and question–model match: 6.
- Correct reproducible analysis, uncertainty, diagnostics, baseline comparison and sensitivity: 9.
- Interpretation, limitations and quality of scientific conclusions: 4.
- Clear communication, code/data instructions and AI/source disclosure: 2.

This point allocation is the frozen working design if the 25/15 split is adopted. It is not a redesign of the full Project assignment or an assertion of its final deadline/page limit.

Continue the old requirement for a **substantive, justified method from Chapters 4–9**, subject to the instructor adopting the updated brief. 'Substantive' means that the model addresses a real feature of the data/question—multilevel heterogeneity, latent classes, missingness, changing latent states, measurement/mediation or a joint longitudinal-event process—and that its assumptions and diagnostics are actually examined. Merely running one extra function, adding an unnecessary random effect or calling an ordinary GLM 'advanced' does not meet this requirement.

Every project needs a simpler, scientifically relevant baseline. Higher marks come from a defensible question–model match, correct inference, diagnostic reasoning and limitations—not from counting latent variables. Students whose chosen data have no defensible Chapter 4–9 question should revise the question/data at a short proposal checkpoint, rather than bolt on complexity at the end. Finding that a simpler model is adequate can be a strong result **when** the advanced component was genuinely investigated and its limitations understood; it is not permission to omit the course-depth requirement altogether. No automatic cap or grade penalty is invented outside the published rubric.

### Oral component: preserve existing SeminarArc authority

Canonical source: `YuukiAS/SeminarArc/docs/plans/stat5060-oral-defense-pc-roadmap.md`, read from the file with blob SHA `a380e0fdfc84a1acc3c60306629f507ab877bbcc`.

Nominal session 10 minutes. Introduction 60–90 seconds: question, method and central result, not a miniature slide presentation. Q1 verifies project/results understanding; Q2 verifies course-method/statistical understanding; Q3 asks integrative reasoning, a perturbation or a limitation. Follow-ups immediately follow their parent question. Students normally do not operate the computer. Evidence is displayed by the examiner. Time windows are flexible; no automatic cutoff or forced question transition.

If oral is 15 course points, Q1/Q2/Q3 each receive 0–5. Anchors: 5 complete independent understanding and sound extension; 4 correct core with a minor gap; 3 basically correct but shallow/limited extension; 2 substantial gaps requiring prompts; 1 superficial repetition without understanding; 0 no substantive answer. Follow-ups calibrate the parent score; they are not an extra fourth scored question. Introduction is not a separate language-performance score.

Ownership checks tie questions to a student's actual figure, modeling choice, code decision or limitation. Ask why an offset is needed, what a parameter conditions on, what would change under another data structure, or what an implausible diagnostic means—not hidden trivia or live package syntax. Human examiners approve questions and compare difficulty across students before the session. Explain a task-specific question in plain language and allow brief thinking time; do not grade speed, accent or presentation polish as a proxy for statistical understanding.

Retain continuous recording plus markers, human grading, no automatic AI scoring and no live AI generation of formal questions. This sprint neither implements SeminarArc nor declares its PC recording workflow production-ready. A tested non-software assessment procedure must exist if the PC app is not ready; the course cannot depend on an unvalidated app.

## 3. What CUHK requires versus what this course chooses

### Institution-level requirements

The public CUHK Academic Honesty guide was marked updated July 2026 when inspected [A01]. It requires appropriate academic honesty declarations, supports course-specific rules concerning AI, addresses disclosure/acknowledgment where applicable and retains institutional review procedures. The public declaration includes compliance with course AI directions; course disclosure does not replace the University's declaration. Relevant text-based submissions still follow the University's/instructor's applicable VeriGuide process. Do not claim that this course can waive these institutional requirements.

Current 2026–27 official registration information refers students to CUHK AI guidance and course instructions [A02]. Official CUHK course/administrative surfaces display selectable approaches, including permitted AI use with acknowledgment [A03–A04]. Permission therefore needs an instructor's clear course-level choice; it is not inferred merely because a tool exists.

Research limitation: the linked full staff/student AI guide redirected to CUHK authentication and could not be read in this session. This policy does **not** claim to quote or have audited that restricted full document. Its institutional claims are limited to the current public official honesty guide, declaration, announcement and selectable-policy evidence. No blog is used as policy authority.

### Instructor-selectable course rule: frozen recommendation

Adopt **permitted AI assistance with meaningful disclosure** for Homework and written Project work. This is closest to CUHK's acknowledged-use approach, not unrestricted use without responsibility and not blanket prohibition. **INSTRUCTOR_APPROVAL_REQUIRED: adoption/publication of this course AI rule**, including the no-AI oral condition. The recommendation itself is decided; Codex is not to choose among policy options.

### Our assessment/enforcement design

Allow assistance with concepts, code, debugging, translation and draft critique, but assess the submitted reasoning and evidence. Require a concise, task-based disclosure. Do not require complete prompt histories, paid AI access, accounts on a named provider or screenshots of every interaction. Complete logs impose burden and do not establish understanding reliably.

Do not use an AI detector as the primary enforcement mechanism or as sole evidence of misconduct. This does not prohibit an institutional review process or replace any University requirement. A concern is investigated using the work, reproducibility, source accuracy and fair human inquiry under normal procedures. The published oral examination is the principal ownership/understanding check, not an ad hoc penalty for students whose writing 'sounds like AI'.

AI assistance can produce a high-quality homework submission end to end. This design is not claimed to prevent that technologically. Its validity rests on meaningful guided work and feedback in homework, coupled with authentic integration and supervised explanation in the Project. Do not market perturbation questions as an AI-proof test.

## 4. Student-facing AI policy — canonical English text

The following block is the exact course/HW1 policy text to publish after instructor adoption. HW1 includes it verbatim or as an exact included source; do not maintain an independently edited copy.

> **Generative AI and responsibility for your work**
>
> You may use generative AI to help you understand concepts, plan an analysis, write or debug code, improve language, or critique a draft for this homework and for the written Final Project. You remain fully responsible for every model, calculation, figure, interpretation, quotation and reference in your submission. Run and check code yourself; verify statistical claims and references against appropriate sources. AI output is not evidence that a method or conclusion is correct.
>
> Include an **AI-use statement** at the end of your report. For each material type of assistance, state the tool and model/version as displayed (or 'not displayed'), approximate date(s), the affected question/section/script or function, what assistance you used, and how you checked or changed it. Group repeated interactions that served the same task. A short table or a few sentences is sufficient; a full prompt history is not required. If you used no generative AI, write: 'I did not use generative AI in preparing this submission.' Ordinary package documentation, spell-checking and a non-generative calculator need not be listed as AI use, but external sources and reused code must still be acknowledged normally.
>
> Do not fabricate data, analyses, citations or checks. Do not submit claims you cannot explain. Do not upload identifiable personal data, another student's work, confidential material or restricted teaching materials to an external AI service without the required permission. No paid AI tool is required, and marks do not depend on whether you used AI.
>
> **Generative AI assistance is not permitted during the oral defense.** You must answer yourself. The examiner will display any approved report/code evidence needed for a question.
>
> This AI-use statement is additional to, and does not replace, the applicable CUHK academic honesty declaration and submission procedures. Follow any more specific published instructions from the course instructor. Suspected academic misconduct is handled under the University's procedures, not inferred from an AI-detector score alone.

A material disclosure example may name 'debugging the NB2 offset in Q1, then checking units and fitted means against a manual calculation'. Do not require students to claim they rejected an AI suggestion when they did not; fabricated process narratives are not a learning outcome. A statistical decision record can instead document a genuine model revision or a check that confirmed the original choice.

## 5. Marking safeguards

Homework feedback should identify a conceptual error separately from a local coding/transcription mistake. Follow-through credit applies when subsequent reasoning is internally correct given an earlier local mistake. Do not deduct repeatedly for one root error unless distinct required skills are independently missing. Legitimate software differences, readable base R versus tidyverse, or a disclosed AI-assisted code style are not penalties.

An omitted AI-use statement initially costs at most its explicit one-point process item under the HW1 rubric; seek clarification/correction rather than automatically declaring misconduct. False disclosure or other dishonesty is a separate institutional matter and must not be settled through an invented detector-based grade deduction. No full-report zero or grade cap is silently introduced here.

## 6. Open instructor approvals and administrative placeholders

Only these matters remain outside the design freeze:

1. Formal adoption of the Project's 25 written / 15 oral split within the confirmed 40% total, and publication of the updated Project brief/course-depth requirement.
2. Formal adoption/publication of the allowed-with-disclosure AI rule and no-AI oral condition.
3. Recording governance: advance notice/consent where required, authorized access, storage, retention through the applicable assessment/appeal period, deletion and any transcription/export policy. No invented retention date and no automatic cloud upload.
4. HW1 due date/time/timezone and official LMS/declaration submission details. Student text keeps explicit placeholders; old 2025 dates are prohibited.

These do not prevent Codex building the complete materials. Until the applicable approvals/date fields are resolved, outputs must be labeled **prepared for instructor release**, not falsely announced as published course policy. Do not stop ordinary coding, rendering or testing because the administrative release gate remains open.

## 7. Official source register

All accessed 2026-09-28.

- A01 CUHK Academic Honesty guide, updated July 2026, including declaration/submission and AI-related provisions: https://www.aqs.cuhk.edu.hk/policies-guidelines-and-procedures/teaching-and-learning/academic-honesty/honesty-in-academic-work-a-guide-for-students-and-teachers/details/
- A02 CUHK Registration and Examinations Section, information for 2026–27 new undergraduates, referring to University AI guidance/course instructions: https://www.res.cuhk.edu.hk/announcement/important-information-regarding-the-start-of-new-academic-year-2026-27-for-new-undergraduate-students/
- A03 CUHK official selectable-policy forms: https://cloud.itsc.cuhk.edu.hk/webform/view.php?id=13691165 and https://cloud.itsc.cuhk.edu.hk/webform/view.php?id=13714399
- A04 CUHK official 2026–27 course example displaying acknowledged AI use: https://www.history.cuhk.edu.hk/en/course/2026272_hist1701/ . This is evidence that a course-selectable acknowledged-use approach exists, not authority to impose that other course's diary requirements on STAT5060.
- A05 CUHK Library learning workshops, current AI/citation support: https://www.lib.cuhk.edu.hk/en/learning/ug-workshops/ . Educational support, not an institutional assessment rule.

The original Syllabus and Final Project PDFs provide historical structure only where current user instructions do not override them. SeminarArc governs the already-designed oral format; this document governs the course assessment rationale and pending approvals.
