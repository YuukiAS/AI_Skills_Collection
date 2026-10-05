# G4 Chat -> Codex Handoff Rubric

G4 reuses the G2 PASS document and evaluates integration/production, not a new scientific task.

## ChatGPT side

PASS requires the PRIVATE / USER-scope / skills-only wrapper to:

1. consume Research Authoring from the exact final candidate identity;
2. use the Clear Writing support snapshot bound to the same canonical commit;
3. preserve the G2-approved scientific content;
4. output stable Markdown/LaTeX or equivalent source;
5. provide a handoff containing:
   - document family;
   - audience;
   - purpose;
   - canonical semantic baseline locator;
   - evidence authority and unresolved evidence;
   - edit scope = content-preserving production handoff;
   - table/figure/formula roles;
   - citation authority;
   - venue/project formatting authority;
   - required production/render route;
   - requested final artifact;
   - final Research Authoring scientific QA requirement.
6. not claim to have rendered the PDF itself;
7. not reroute to Presentations.

Missing any material handoff field => G4 FAIL.

## Codex side

PASS requires exact `C` `research-main` normal entry to:

1. consume Research Authoring before renderer mechanics;
2. preserve all handoff fields and G2-approved semantics;
3. invoke the canonical PDF route appropriate to the frozen document;
4. produce a real, directly accessible final PDF;
5. perform renderer QA;
6. perform final Research Authoring document-level scientific QA after rendering;
7. surface the artifact, not only a repo path.

## Identity / authority

- live Plugin Creator mutation requires the separately approved bounded user authorization already defined by Plan;
- wrapper payload/hash must bind to exact `C`;
- no MCP/connector/database/watcher/state/PDF runtime in wrapper;
- no paid API;
- no private scientific data sent to an unapproved provider.

## Failure

G4 FAIL if:
- Chat wrapper or Codex runtime does not bind to exact C;
- Clear Writing support snapshot is from a different canonical commit;
- handoff loses scientific/document identity;
- Codex bypasses Research Authoring and only renders;
- output science drifts from G2 PASS;
- final PDF is unreadable/undelivered;
- a slide-deck route is substituted;
- live wrapper mutation is performed without required user authorization.
