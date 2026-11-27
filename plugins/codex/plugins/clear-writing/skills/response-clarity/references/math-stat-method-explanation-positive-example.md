# Positive example: explaining a mathematical/statistical method clearly

Date: 2026-10-28  
Route: Clear Writing / `response-clarity`  
Status: user-confirmed positive example

## Why this example is kept

The user explicitly identified the underlying answer as the desired style for
explaining mathematical and statistical ideas: concrete first, formal second,
with enough technical precision to remain useful.

The transferable pattern is:

1. Start from the exact object in the user's problem.
2. Turn the abstraction into a concrete mental picture.
3. Explain the key operation in ordinary language.
4. Work through a much smaller example.
5. Put formulas next to the interpretation they support.
6. Explain the actual computational/statistical gain, not a superficial slogan.
7. Connect the idea to established literature only after the mechanism is clear.
8. Separate established machinery from the project's own research question.
9. State important corrections or boundaries directly.

The example below is preserved as a writing reference, not as a source of
scientific truth. Any future answer must still use the domain owner's current
facts, notation, and evidence.

---

## Example: a synthetic dice calculation

This is an invented classroom example, unrelated to any private research model.
Let $U$ and $V$ be independent fair six-sided dice. We want the probability that
their sum exceeds 8.

### Concrete picture before notation

A direct simulation rolls both dice and records either 0 or 1. A conditional
calculation rolls only the first die, then averages over all six possibilities
for the second die. It replaces one random outcome with its exact conditional
average.

If the first roll is 4, the second die must be 5 or 6. The conditional probability
is therefore $2/6$. For first rolls 1 through 6, the probabilities are
$0, 0, 1/6, 2/6, 3/6, 4/6$. Their average is $5/18$.

### Formal statement after the mechanism

Writing $h(u)=P(V>8-u)$, the same calculation is

$$P(U+V>8)=E_U[h(U)].$$

This is conditional expectation. Averaging out the second die removes the
variation due to that die. In this tiny example all outcomes can be enumerated;
simulation only illustrates why conditioning can help in larger calculations.
The example establishes no claim about the performance of a research algorithm.

---

## What not to copy mechanically

Do not turn every technical answer into a long tutorial. The example works
because the user's question was conceptual and the method had a natural nested
structure. Preserve the same principles at shorter length when the question is
narrower.

Do not invent toy values that could be mistaken for actual project results.
Label them as illustrative when necessary.

Do not use analogy as a substitute for mathematics. The analogy should make
the formal operation easier to understand; the exact object and its boundary
must still appear.
