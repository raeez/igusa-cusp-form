# A233 -- Vol II introduction direct-H2 repair

## Claim attacked

`chapters/theory/introduction.tex` used direct
\(H^2(\mathfrak g_{\Delta_5})\), AGT, Schur, Bethe, MO, and module
category language too strongly.

## Repairs

- Recast \(\mathbf H_{\Delta_5}\) as a Hall--Borcherds
  source-recognition problem with a denominator-character map.
- Recast the \(H^2(\mathfrak g_{\Delta_5})\) statement as a
  Heegner-characteristic/classifying-line target.
- Made AGT, Schur, Bethe-subalgebra, MO, and module-category statements
  conditional on source recognition plus comparison theorems.
- Preserved constants and targets:
  \(c_{\Lambda^{3,2}}(0)/2=5\), \(\mathrm{wt}(\Delta_5)\),
  \(\Phi_{10}^{\mathrm{un}}=\Delta_5^2\), \(\hbar^2=-1/8\), and
  Humbert walls \(H_1,H_4\).

## Verification

`git diff --check -- chapters/theory/introduction.tex` passed. Targeted
`rg` shows the repaired hits are gated or target statements.
