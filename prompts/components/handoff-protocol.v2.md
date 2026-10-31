# Research Handoff Protocol

At the conclusion of the investigation, provide a structured research report containing:

**1. Executive findings**

State the strongest discoveries, their significance, and their present level of certainty.

**2. Exact mathematical results**

Provide precise statements of theorems, constructions, invariants, and other established properties. Include proofs or reproducible verification procedures.

**3. Failed hypotheses and negative results**

State exactly which hypotheses failed, how they failed, and the scope of the conclusion. Distinguish counterexamples, formal impossibility results, unsuccessful bounded searches, and inconclusive evidence.

**4. Unresolved conjectures**

Include exact formulations, supporting observations, known limitations, and tests that could distinguish competing explanations.

**5. Dependencies**

Identify which results rely on other findings, external mathematical facts, historical assumptions, particular encodings, or supplied data.

**6. Alternative explanations**

Describe simpler explanations, broader mathematical generalizations, and plausible reasons a result might be less distinctive than it appears.

**7. Reproducibility**

Provide code, pseudocode, data definitions, and explicit computational parameters sufficient for independent replication.

**8. Opportunities for further research**

Identify especially promising unanswered questions, useful generalizations, and directions not explored.

**9. Recommended next assignments**

Propose concrete follow-up investigations for independent researchers. Explain what each assignment might establish or eliminate.

**10. Machine-readable research registry**

Conclude with a compact table containing a unique local claim ID, exact claim, evidence type, status, dependencies, and recommended next action for every significant result.

Do not classify a result as independently verified merely because you checked your own reasoning or computation.

The report is intended to become part of a cumulative, multi-investigator mathematical research program. Optimize for precision, reproducibility, and usefulness to future investigators, rather than rhetorical persuasiveness.

## Additional reporting requirements

**Report header.** Begin your report with:

- the investigation ID and assignment title, if you were given them;
- your role in this investigation;
- your model name or identifier as you know it, or "unknown";
- the materials you were given, and any external sources or tools you used (for example, code execution or literature you consulted).

**Data and computation.** For every computation, state whether it was actually executed or only described. Include the complete code or exact pseudocode and all input data, including your full transcription of any traditional sequence, table, or procedure you relied on, with its source if known.

**Registry columns.** In the machine-readable registry (item 10), also give for each claim:

- *domain*: formal (about defined mathematical objects only), source-dependent (about a particular attested arrangement, text, or procedure as you encoded it), historical, or interpretive;
- *contingency*: definition-driven (follows from your definitions alone) or contingent (depends on features of the sources that could have been otherwise);
- *scope*: for negative or inconclusive results, exactly what was ruled out and what was not;
- *prior claims*: the identifiers of any supplied prior claims it restates, depends on, or bears on.
