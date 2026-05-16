# A149 -- CYQG Residual Signed-Multiplicity Verifier

## Findings

Fatal:

- `chapters/examples/k3_chiral_algebra.tex` still treated signed K3
  elliptic-genus coefficients as Hilbert-space and root-space dimensions.
  This fails already at \(D=3\), where the coefficient is negative.
- `chapters/examples/k3e_bkm_chapter.tex` used
  \(\dim \mathfrak g_{v_i+v_j}=c(D(v_i+v_j))\) inside a load-bearing CE
  differential proof.

Serious:

- CoHA/Hall compute code still promoted absolute coefficients to
  dimensions in `elliptic_hall_hocolim.py`, `k3e_coha_structure.py`, and
  their tests.
- `k3_chiral_bialgebra_platonic.tex` had generator ranges
  \(r=1,\ldots,c_{K3}(N)\), ill-formed for negative coefficients.
- `k3_yangian_chapter.tex` used \(|c(D)|\) as a generator count and BPS
  vector-space dimension.
- `k3_chiral_algebra.tex` still said imaginary roots produce BPS walls
  with multiplicity \(|f(D)|\).

Minor/serious drift:

- `k3e_bkm_chapter.tex` still had local table drift with
  `mult = |c(D)|`.
- duplicate notes retained old positive-root multiplicity language.

## Follow-Up

The first fatal manuscript repair is assigned to A158. The second fatal
`k3e_bkm_chapter.tex` repair is queued as the next available worker.

## Files Changed By Agent

None.
