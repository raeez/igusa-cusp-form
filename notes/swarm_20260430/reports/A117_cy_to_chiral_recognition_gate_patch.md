# A117 -- `cy_to_chiral` Recognition-Gate Patch

## Claim Attacked

`chapters/theory/cy_to_chiral.tex` stated the K3 x E chiral algebra
equivalence with \(U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})\) before the
finite Hall--Borcherds recognition gate.

## Patch

The stale theorem was rewritten as a Hall--Borcherds recognition
criterion. The equivalence is now asserted only after the finite gate
supplies:

- compact source provenance;
- full parity blocks;
- \(M,D,B,G,K,Q,A\) matrices;
- radical quotient;
- no-extra-relations;
- PBW comparison;
- Mittag--Leffler transition compatibility.

The Oberdieck--Pixton and Borcherds data are now stated as target
arithmetic tests, not source recognition.

## Verification

```text
git diff --check -- chapters/theory/cy_to_chiral.tex
```

passed. Targeted search found the rewritten criterion anchors and the
remaining downstream references.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`
