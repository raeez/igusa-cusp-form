# A165 -- Topological-Strings Tate-P5 Gate Patch

## Result

Patched `topological-strings/tate-P5-cross-volume.tex` so scalar
DT/PT/GW/OP, Igusa, Borcherds, and BF/Moyal data remain target-side unless
an explicit finite-stage recognition gate supplies source data.

## Changed Path

- `/Users/raeez/topological-strings/tate-P5-cross-volume.tex`

## Claims Attacked

- Scalar DT/PT/GW/OP, \(\Delta_5\), \(\Phi_{10}\), Borcherds, and
  anomaly normalizations as source recognition: fenced at `38` and `235`.
- BF/Moyal formal-stalk transfer as compact/global/Igusa theorem: routed
  through \(C_{\mathrm{tar}}\), \(\Gamma_{\mathrm{src}}\), and
  \(\operatorname{Ob}_{\mathrm{UKD}}(C_{\mathrm{tar}})\) at `68`, `189`,
  and `469`.
- Mixed recognition as Borcherds/compact-source recognition: narrowed to
  product-disk recognition at `691`.

## Proof Status

Proved scalar identities were preserved at `971`. Hall/CoHA,
compact-source, parity, PBW, \(E_2\)-centre, factorization, and Borcherds
recognition lifts remain conditional on explicit finite-stage gate data and
\(\operatorname{ob}_{\mathrm{src/rec}}=0\).

## Checks

- Targeted `rg` over the attacked vocabulary.
- `git diff --check -- tate-P5-cross-volume.tex` passed.

## Open Question

No local obstruction remains beyond supplying actual finite-stage source
data for any future compact Hall/CoHA or BKM recognition theorem.

