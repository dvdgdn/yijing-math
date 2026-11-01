# Adjudication of the manuscript-assisted expansion

**Full-context coordinator material.** Written 2026-10-31 by Claude Opus 5.5 at the human coordinator's request, as an outside review of the expansion committed in `de8d17b` ("research init").

The reviewer is not outside the programme. It set up this repository and extracted INV-0001's claims, and is the same model family as INV-0001's author. It is a different family from INV-0003 and from the external manuscripts. The research done in the same session is INV-0004, which is reported, not verified.

**Coordinator update, 2026-11-01.** The original assessment below is retained as the selection record. Its corpus-wide exclusions are provisional screening decisions, not impossibility results. Family 119 is the strongest demonstrated substantial transfer so far; useful exact finite obstructions also exist, including C-0030. Its broad "generation is worst possible" summaries must be read as claims about the displayed endpoint coefficients only. The completed full-context INV-0007 reports a balanced parity label retaining strictly less information than generation at every nontrivial symmetric noise level; its report and exact code are frozen, with registration pending. This does not refute the precise coefficient inequalities in C-0036. Two isolated verifications, INV-0005 and INV-0006, are now running; see the current roadmap and investigation records.

## 1. Verdict in brief

- **The discipline is excellent.** The scaffolding added in `de8d17b` makes overstatement hard:
  - a pinned source with hashes;
  - review levels that never pretend keyword screening is proof review;
  - an import contract;
  - scoped negative results;
  - explicit independence metadata.
- **The yield is thin, and that is a property of the corpus, not a failure of the search.** Of 373 result families, one supplies an exact, non-vacuous statement at the Yijing's scale. About thirty touch it formally at all. 721 manuscripts are not 721 opportunities.
- **INV-0003 is correct but under-connected.** Every finite claim reproduces exactly (INV-0004 R8; C-0027–C-0031). It missed the bridge that matters most: its "artificial" channel at p = 1/4 *is* the three-coin oracle (C-0032). Its priority-1 open question needed no corpus result at all; classical tools settle it (C-0035).
- **The programme's bottleneck has not moved.** Still missing:
  - any external investigation launched since setup;
  - any verification;
  - any cited dataset;
  - INV-0002, which is still absent.

  The expansion added about 35,000 lines, mostly frozen library material and generated catalogue, plus about 2,000 lines of tooling and tests. Recommendation: **freeze infrastructure** until at least three external investigations are registered.

## 2. What the expansion got right

- **Provenance of external material.** The snapshot at `4eaee875`, the source hashes, and the frozen theorem sources with their Lean scope documents are exactly what a later reader needs to trace a correction.
- **Calibrated demotions.** INV-0003 used finite pilots to show that family 113's entropy bounds are vacuous here (−22.5 ≤ H ≤ 24 against an exact 12), that family 131's mixing bound is useless at n = 64, and that family 076's ultraflat transfer fails. These are the most valuable sentences in the transfer review. They model the right habit: test applicability on the actual instance before allocating work.
- **Real bugs fixed in coordination code.**
  - Model family was inferred from display names.
  - Package boundaries could be bypassed by symlinks.
  - Frozen outputs could be overwritten.
- **Assisted and unassisted lanes.** Keeping ASN-0004 and ASN-0006 blind while assisted work proceeds is the right design. INV-0004 now gives ASN-0004 a concrete comparison partner.

## 3. Where it overreaches or risks drift

1. **Volume against evidence.**
   - Thirteen assignments, seven of them drafts, with a board, a dashboard and an impact tool, yet zero launches.
   - Each new draft adds overlap bookkeeping.
   - The marginal value of further process is now negative.
2. **Expectation set by the request.** "Given there's a there there" invites motivated transfer.
   - The Yijing's formal core is a 64-element set with small symmetry groups; nearly every question about it is settled by enumeration.
   - A deep theorem helps only when the question quantifies over a space too large to enumerate: all 2⁶⁴ yes/no questions, all balanced labels, all 64! orders, or all n-line generalizations.
   - That filter, applied honestly, leaves little in this corpus (§4).
3. **Missed elementary routes.** Priority 1 in `transfers.md` asked whether the palace/difference comparison holds for all noise levels and why.
   - The answer uses edge isoperimetry, level-1 Fourier weight, Fano's inequality and monotonicity (C-0035, C-0036).
   - Lesson: before ranking a corpus transfer, ask whether a classical argument already closes the question at n = 6.
4. **Prior work inside the imported source was not surfaced.** Family 119's own prior-work section says that balanced functions were already covered for |ρ| ≤ 0.914 by a computer-assisted argument. Its genuinely new content at coin noise (ρ = 0.5) is therefore the *biased* case.

   Two external facts were also absent from the review:
   - An independent preprint (arXiv:2609.26444, abstract only read) claims a separate proof of the same theorem. That strengthens the premise.
   - The same preprint reports that the multi-bit analogue *fails* for k ≥ 8 and is conjectured for 2 ≤ k ≤ 7, which frames the trigram question (Q-009).
5. **Lineage concentration.**
   - The manuscripts come from an unnamed OpenAI model.
   - INV-0003 is GPT-family.
   - Most recommended verifiers are GPT-family.

   For corpus-derived claims, a Claude or human auditor is the cross-family check. For Claude-derived claims, GPT is. Record lineage, not just family.
6. **Self-registration.** INV-0003's registration was drafted by its originator. I registered INV-0003 (cross-family) and INV-0004 (my own). Both extractions need human review before anyone counts them.

## 4. Independent screen of the corpus

I read all 373 family descriptions in full and swept all 721 abstracts for cube, Boolean, sequence, permutation, coding, tiling, symplectic, entropy and channel vocabulary. My dispositions agree with INV-0003's for every family it reviewed. The additions are marked ★.

| Tier | Families | Judgment |
|---|---|---|
| A. Exact and non-vacuous at six lines | 119 (Courtade–Kumar; Hellinger with output bias) | Quantifies over all 2⁶⁴ Boolean questions. Applied in C-0034; motivates Q-009 and Q-010. |
| B. Valid method or obstruction; exact enumeration or classical results suffice here | 113, ★114, 115, 131, 238 (finite support bound only), 179 (classical at length 64) | Reopen only for a genuinely larger instance: n-line families, the textual corpus, or a real contingency table from cited data. |
| C. Interpretive guardrails | 134, 161, 206, 076 (negative, C-0031), ★097 | 097 (Steinitz): low prefix imbalance is cheap. Any order that places each x next to its complement keeps every partial sum within one ±1 vector, so a "balanced" ordering is not evidence of design. The new Θ(√d) constant is unspecified, so the theorem is vacuous at d = 6. |
| D. Formal contact, asymptotic or vacuous at n = 6 | 127, 132, 192, 171, 186, 099, 121, 122, 129, 133, 177, 178, 229 | Each needs a family of growing objects or a justified channel/tree model. None is available. |
| E. Coincidences of a number or a word, rejected | 266 (six-dimensional bases), 225 (six-vertex model), ★187 (six-cell shape), ★067 (Fano sixfolds), ★015 (sextic fields), ★210 (sixth powers), ★165 (crossing number of K₈,₈, whose 64 edges match the 64 hexagrams only numerically) | No structure-preserving map; do not pursue. |
| No formal contact | the remaining ~340 families (arithmetic geometry, analytic number theory, harmonic analysis, topology, operator algebras, PDE, mathematical physics, complexity separations) | Not reviewed further; reopen only with a concrete new object. |

Individual manuscripts were read beyond their abstracts only for family 119. Unreviewed is not refuted.

## 5. What was done with the one strong transfer (INV-0004)

The natural target of family 119 is the divination layer, because it is the part of the tradition that actually *is* a noisy channel. Full report: `investigations/INV-0004-divination-information-bounds/output.md`.

- **Channels (C-0032).**
  - The coins model is exactly the symmetric line-change channel at 1/4. The set of moving lines says nothing about the primary hexagram.
  - The standard yarrow model is asymmetric: yang→yin 3/8, yin→yang 1/8. Its changed hexagram leans yin, and its moving-line set carries 0.374 bits about the primary.
  - Both move each line with probability 1/4.
- **Sensitivity (C-0033).** The textbook yarrow probabilities hold under binomial splitting. Uniform splitting gives old yang 4.65 times as likely as old yin.
- **One-bit questions (C-0034, conditional).** Under coins, no yes/no question about one hexagram carries more than 0.1887 bits about the other, and a single line achieves it.
- **Three-bit descriptions (C-0035, C-0036).**
  - For every line-change probability: trigram > palace > generation.
  - The trigram is optimal, and the generation label (which line pairs differ) is worst possible, at both noise extremes.
  - Mechanism: edge isoperimetry at low noise, level-1 Fourier weight at high noise.
- **Open (C-0037, C-0038).**
  - Is the trigram optimal at every noise level? This is an instance of a published conjecture.
  - Do single lines stay optimal under the yarrow asymmetry? The evidence so far is exhaustive at n ≤ 4.

Only C-0034 uses the corpus. The strongest formal result, C-0035, does not.

## 6. Dispositions and the proposed slate

| Assignment | Disposition | Reason |
|---|---|---|
| ASN-0001 | **First**, unchanged | Palace/source verification remains foundational; C-0035 uses only the formal D, but every historical reading needs C-0017. |
| ASN-0014 (new) | **Second**, alongside ASN-0001 in a separate fresh session | GPT-family isolated verification of C-0032–C-0036; makes the divination results usable. |
| ASN-0004 | Third | Blind divination exploration; the best test of whether the assisted framing found something an unassisted investigator would not. Keep it free of INV-0004 material. |
| ASN-0007 | Capacity permitting | Gates every historical reading, including which procedure model is attested (Q-011). |
| ASN-0013 | Optional | INV-0004's recomputation found no error; run only to promote C-0027–C-0031. |
| ASN-0010 | Withdrawn | Its main question is answered (C-0035); the remainder is Q-009/Q-010. |
| ASN-0011 | Defer | No cited table exists to condition on; the measure lesson (L4) is retained as a fixture. |
| ASN-0012 | Defer until an attested local generation rule exists | The marginal-versus-joint gap (C-0030) is generic; fitting a local grammar now invites forking paths. |
| Cycle-2 option | Specialist on Q-009 or Q-010 | Genuine open problems with clear Yijing motivation. A solution would teach more information theory than Yijing history. |

**Single best next action:** run ASN-0001 with GPT-6.1 Sol Max in a fresh session. Run ASN-0014 in a second fresh session when convenient.

## 7. Is there a there there?

- **Not in the received order, as far as this corpus can reach.** The corpus contains no hidden key to the order of the hexagrams. Questions about the received order are limited by sources and by the multiplicity of patterns already examined, not by missing theorems.
- **What it does contain:** one sharp instrument, and it points to a frontier the programme had not touched — information flow through the oracle. There, exact and checkable results that bear on practice are now in hand:
  - how much a reading's two hexagrams share;
  - which traditional descriptions survive change;
  - how the two classic procedures differ in what their moving lines reveal.

  That is a real, modest gain.
- **Further gains** will come from:
  - verified foundations (ASN-0001, ASN-0014);
  - cited sources (ASN-0007);
  - blind comparison (ASN-0004).

  They will not come from screening the corpus again.
