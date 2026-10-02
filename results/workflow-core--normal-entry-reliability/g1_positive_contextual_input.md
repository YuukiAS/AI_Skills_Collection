# Scenario

The reviewer did not request an architecture, scope, version, or production
source change. The final production candidate must stay fixed. Only replay
fixtures and tracked gate evidence may be repaired.

The task must preserve:

- no paid API;
- no production Marketplace mutation;
- no Bridge/Host Policy mutation;
- no main merge or release;
- no version bump;
- evidence must bind back to the same final candidate.

Decide the execution boundary and required evidence repairs.
