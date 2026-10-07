# 059 Research Authoring C3 Capability Gate 影响说明 v0.3

日期：2026-10-07  
状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Task：`research-authoring--formal-production-authoring`

## 1. Taxonomy

No new Gate.

~~~text
G1 = normal entry / owner boundary
G2 = research-document semantics + incremental update
G3 = real manuscript/package
G4 = ChatGPT + Codex production
ADD_G5=NO
~~~

## 2. Development failure disposition

`04a17a904ce522cb4a517cb33f22e062f2bcbc09` remains a failed provisional development attempt.

Its DEV-04/DEV-05 failures are permanent development regression evidence.

No PASS from `04a17...` contributes to P2/C3 admission.

## 3. P2 recovery evidence is still development evidence

The new profile-scoped explicit-only preflight and full eleven-case matrix are pre-final risk-matched regression/admission checks.

They do not prove final G1-G4.

~~~text
P2_PREFLIGHT_PASS != G1_PASS
P2_MATRIX_PASS != RESEARCH_AUTHORING_0_3_COMPLETE
~~~

## 4. Why broad development rerun is required

P2 changes shared profile-install behavior and the integrated `research-main` owner chain.

Therefore all eleven development case families rerun on the same P2, including standalone, integrated, render-only, authoring-only, neighboring owner and counterexample surfaces.

This is not a hidden fifth Gate; it is same-candidate development regression after a failed provisional candidate.

## 5. Should-not-change additions inside existing cases

No new case family is created.

Existing case families gain risk-matched subruns：

- DEV-06/07: research-main finalized-source render-only still reaches the explicit-only renderer;
- DEV-08: research-main existing-PDF support still reaches the explicit-only generic pdf;
- DEV-04/05: record exact Skill read order and profile policy identity.

## 6. Final Gate policy after C3

Only after：

~~~text
P2 full matrix PASS
-> C3 freeze
-> independent C3 development Critic PASS
-> new C3 pre-final packet
-> pre-final Critic PASS
~~~

may final G1-G4 start.

All final evidence must bind to exact C3.

C2 final evidence and 04a17 development evidence remain regression only.

## 7. G4 wrapper

The offline wrapper built from `04a17...` is not final evidence.

Exact-C3 wrapper must be rebuilt after P2 matrix PASS/C3 freeze.

Live update remains separately user-authorized.

## 8. Conclusion

~~~text
ADD_G5=NO
G1_G4_TAXONOMY_CHANGED=NO
P2_PROFILE_POLICY_PREFLIGHT=DEVELOPMENT_ONLY
P2_FULL_11_CASE_MATRIX=DEVELOPMENT_ONLY
C2_FINAL_EVIDENCE=REGRESSION_ONLY
04A17_DEVELOPMENT_EVIDENCE=REGRESSION_ONLY
FINAL_GATES_NOT_STARTED=YES
~~~
