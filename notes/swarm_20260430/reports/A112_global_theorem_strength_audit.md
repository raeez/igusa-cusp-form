# A112 -- Global Theorem-Strength Audit

## Findings

Critical: Vol III still treats signed coefficients as full parity or
dimension in the BKM dependency theorem. In particular,
`chapters/examples/k3e_bkm_chapter.tex` asserts root/primitive dimension
`|c(D)|`; this fails already at the first timelike Igusa block, where
Igusa has \(29|93\), signed \(-64\), and total dimension \(122\).

High: Vol III still promotes the Stage-2 target comparison to an
equivalence before the finite Hall--Borcherds recognition gate in
`chapters/theory/cy_to_chiral.tex`, and the patched programme chapter
inherits that theorem.

High: a later Vol III motivic lane still identifies source DT/CoHA data
with target root spaces without compact Hall recognition, source
orientation monodromy, pairings, radicals, PBW, or source-to-target
comparison.

Medium: Igusa still has a wording trap in the \(D_0\) Pfaffian lane:
the phrase "target-window parity model" is used for a minimal
\(K_0\)-shadow built by placing signed exponents wholly in one parity.
The surrounding text fences it correctly, but the label can be confused
with true target parity such as \(29|93\).

## No Finding

The current Igusa proof ledger, provenance gate, A071 target rows, and
NO7 firewall are in the right theorem-strength regime. Target labels
remain target/codomain coordinates, \(C_{k,2}\) and \(2\delta_{123}\)
remain signed-only, and NO7 is explicitly only radical descent, not
no-extra/PBW/recognition.

## Files Changed By Agent

None.
