# rhomred_orientation_primitive_projection_descent

This packet verifies row 305 as a criterion and obstruction ledger:
orientation descent through the \(E\)-quotient commutes with the
primitive projection only after the quotient-orientation rows, oriented
Hall-coproduct descent, unit-counit descent, compact Hall primitive
kernels, primitive idempotents, and primitive transition rows are
supplied.

The quotient-after-correspondence `theta_mu_primitives` packet supplies
compatibility for already supplied primitive kernel and projection rows.
It is not a Joyce--Upmeier orientation row and does not populate the
compact Hall source coproduct, counit, kernel, or projection tables.

Run:

```sh
python3 compute/verify_rhomred_orientation_primitive_projection_descent.py \
  --fixture certificates/orientation/rhomred_orientation_primitive_projection_descent --check
```
