# rhomred_orientation_direct_sum_multiplicativity

This packet verifies row 299 as a criterion and obstruction ledger:
orientation multiplicativity under direct sum is a Picard-groupoid
datum, not a consequence of the determinant-line formula alone.

For retained objects \(\mathcal C,\mathcal D\), the direct-sum
determinant contains the off-diagonal factors
\[
\det K^{\mathrm{red}}_{\mathcal C,\mathcal D}\otimes
\det K^{\mathrm{red}}_{\mathcal D,\mathcal C}.
\]
Direct-sum multiplicativity requires square-root orientation lines, a
hyperbolic square root of the cross term, and an isomorphism
\[
o_{\mathcal C\oplus\mathcal D}\simeq
o_{\mathcal C}\otimes o_{\mathcal D}\otimes q_{\mathcal C,\mathcal D}
\]
with symmetry, pullback, and pentagon coherence.

The current orientation tables supply no orientation-line rows and no
Thom--Sebastiani multiplicativity rows.  The packet therefore records
the exact missing mathematical data and does not certify row 299 as an
unconditional theorem.

Run:

```sh
python3 compute/verify_rhomred_orientation_direct_sum_multiplicativity.py \
  --fixture certificates/orientation/rhomred_orientation_direct_sum_multiplicativity --check
```
