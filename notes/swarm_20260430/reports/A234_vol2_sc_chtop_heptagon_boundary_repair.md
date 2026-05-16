# A234 -- Vol II SC chiral-topological heptagon boundary repair

## Claim attacked

`sc_chtop_heptagon.tex` packaged K3 BKM/heptagon claims as
theorem-grade without the external Hall--Borcherds gates.

## Repairs

- Direct \(H^2(\mathfrak g_{\Delta_5})\) classification is now a scalar
  automorphic target, not a direct cohomology computation without gates.
- The K3 seven-vertex theorem and class-M face statements are
  `\ClaimStatusConditional`.
- Added compact Hall promotion, PBW/no-extra primitive theorem, parity,
  completion, and source-recognition hypotheses.
- Gated the BKM-to-Hall cross-vertex identification and BPS Lie
  intermediate object.

## Verification

`git diff --check -- chapters/theory/sc_chtop_heptagon.tex` passed.
Targeted `rg` shows K3 BKM claims are conditional/gated.

## Residual obligation

The compact Hall promotion, PBW/no-extra primitive theorem, parity
match, common completion, source-recognition, and direct \(K(1)\)-local
\(H^2\) computation remain external gates.
