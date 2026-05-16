# A177 -- Chiral-Bar-Cobar Residual Overclaim Verifier

## Result

Read-only verifier found several remaining scalar-to-chain recognition
overclaims outside the already patched `higher_genus_foundations.tex` and
`w-algebras.tex` lanes.

## Fatal

- `chiral-bar-cobar-vol2/chapters/theory/six_d_hcs_feynman_coefficients.tex:195`
  claimed the Borcherds lift of \(\phi_{-2,1}\) is \(\Phi_{10}\) and read a
  one-variable \(1/\Delta_5\) coefficient as a BV-loop coefficient.
- `chiral-bar-cobar/chapters/connections/feynman_diagrams.tex:1672`
  identified the Beem--Rastelli chiral algebra with
  \(\mathbf H_{\Delta_5}\) and its character with
  \(1/\Phi_{10}^{\mathrm{un}}\).

## High

- `feynman_diagrams.tex:1497`: displayed equality
  \(\mathbf H_{\Delta_5}=D_\hbar(\mathrm{CoHA}\cdots)\) too strong even
  under conjectural status.
- `e1_modular_koszul.tex:3794`: asserted an actual \(E_1\) bar-cobar
  inversion equivalence for \(\mathbf H_{\Delta_5}\) without the finite
  Hall--Borcherds gate.
- `algebraic_foundations.tex:2947`: “unique quantisation” of
  \(\mathfrak g_{\Delta_5}\) via EK too strong without a theorem source.
- `arithmetic_shadows.tex:13738`: overstated scalar automorphic reciprocity
  as chain/Lie-bialgebra recognition.
- `ht_physical_origins.tex:1713`, `1874`: promoted physical 11D SUGRA /
  loop QME statements to \(\mathbf H_{\Delta_5}\), \(\Delta_5\), and
  \(\log\Phi_{10}\) chain theorems.
- `w-algebras-conditional.tex:1707`, `1902`: Enriques orbifold and
  multiplicity-halving statements stronger than scalar elliptic-genus
  halving supports.

## Medium

- `feynman_diagrams.tex:1171`: untagged 1-loop \(\Delta_5\) trivializer
  statement too strong.
- `compute/lib/cy_bkm_algebra_engine.py:1226`: docstring blurred BKM
  denominator, K3 elliptic genus, and higher-genus scalar projection lanes.
- `compute/tests/test_cy_bkm_algebra_engine.py:1007`: comment
  misidentified \(\phi_{0,1}\) with the theta/eta \(\phi_{-2,1}\) lane.

## Main-Thread Follow-Up

The main thread patched the unassigned arithmetic/compute/comment items
locally. A182, A184, A185, and the next available Vol II worker cover the
remaining fatal/high manuscript lanes.

