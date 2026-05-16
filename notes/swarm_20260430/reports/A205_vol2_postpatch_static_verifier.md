# A205 Vol II Postpatch Static Verifier

## Claim Attacked

The A201/A203 Vol II patches might have fixed local language while
leaving earlier theorem-level BKM recognition overclaims intact.

## Fatal Findings

- `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex` still put
  the BV obstruction class directly in `H^2(\mathfrak g_{\Delta_5})`
  and claimed a BV-to-BKM Chevalley--Eilenberg identification through a
  Drinfeld-double/small-quantum-group comparison.
- The all-order Heegner theorem still asserted
  `c_n \in H^2(\mathfrak g_{\Delta_5})` and
  `c_n=c_{\phi_{-2,1}}(n)[H_n]` as `\ClaimStatusProvedHere`, promoting
  Humbert/Jacobi scalar data to BKM cohomology.
- The Costello-flow section still took HCS with Lie algebra
  `\mathfrak g_{\Delta_5}` as already available, derived a BKM
  characteristic projection, and resummed to the Igusa product.
- The abelian HCS anomaly series was still stated as the Borcherds
  product `(\Phi_{10}^{un}/\eta^{24})^{...}` as a proved theorem.

## High Findings

- `six_d_hcs_feynman_coefficients.tex` still used BKM boundary labels,
  bilinear form, tree-level equality, and BV master-equation language
  too strongly after warning that the BKM source is not constructed.
- `bv_brst.tex` still identified a Humbert surface with an order-3 root
  vector of `\mathfrak g_{\Delta_5}` without root labels and denominator
  lattice comparison.
- `w-algebras-conditional.tex` still used `\mathbf H_{\Delta_5}` as an
  anchor for KZ/DS class-S data and had a Kummer row without the
  source-recognition caveat.

## Checks

- Targeted `rg` over the three focus files for Igusa/Delta5/BKM/Humbert/
  Schur/Enriques/root/parity/supertrace/chain-map terms.
- Broader repo-wide `.tex` `rg`.
- `git diff --check` passed.

## Status

The fatal `bv_brst.tex` findings were delegated to A208. The remaining
Vol II high findings require a separate worker after the BKM cohomology
theorems are repaired.

