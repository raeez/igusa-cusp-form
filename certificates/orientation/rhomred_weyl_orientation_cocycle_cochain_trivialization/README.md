# rhomred_weyl_orientation_cocycle_cochain_trivialization

This packet verifies row 311 as a finite cochain-trivialization
criterion.  Given row 310, a row 311 datum is a chosen vector
\[
b_R\in C^1(\mathcal G_R;\underline{\mathbb F}_{2,o})
\]
with verified equation
\[
d^1_R b_R=v(c_{o,R}).
\]

The current tree does not supply the row-309 cocycle values, the
row-310 rank certificate, a cochain vector, a gauge convention, or a
coboundary-defect row.  Row 312, compatibility under \(R\to R'\), is
not certified here.

Run:

```sh
python3 compute/verify_rhomred_weyl_orientation_cocycle_cochain_trivialization.py \
  --fixture certificates/orientation/rhomred_weyl_orientation_cocycle_cochain_trivialization --check
```
