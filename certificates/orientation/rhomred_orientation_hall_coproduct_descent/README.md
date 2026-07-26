# rhomred_orientation_hall_coproduct_descent

This packet verifies row 304 as a criterion and obstruction ledger:
orientation descent through the \(E\)-quotient commutes with the Hall
coproduct only after the quotient-orientation cocycle on the splitting
correspondence, the inverse oriented Thom--Sebastiani row, the
external-product descent row, and the \(p_!\) compact-support comparison
are supplied.

The quotient-after-correspondence `theta_mu_coproduct` packet supplies
compatibility for already supplied coproduct and bialgebra rows.  It is
not itself a Joyce--Upmeier orientation row and does not populate the
compact Hall source coproduct or counit tables.

Run:

```sh
python3 compute/verify_rhomred_orientation_hall_coproduct_descent.py \
  --fixture certificates/orientation/rhomred_orientation_hall_coproduct_descent --check
```
