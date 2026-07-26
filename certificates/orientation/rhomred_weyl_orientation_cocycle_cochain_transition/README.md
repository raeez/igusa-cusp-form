# rhomred_weyl_orientation_cocycle_cochain_transition

This packet verifies row 312 as a finite transition-compatibility
criterion for the Coxeter cochains.  For each successor \(R'\le R\),
row 312 requires transition cochain maps
\[
\rho^i_{RR'}:C^i_{R'}\to C^i_R,\qquad i=1,2,
\]
with
\[
d^1_R\rho^1_{RR'}=\rho^2_{RR'}d^1_{R'},\qquad
\rho^2_{RR'}v(c_{o,R'})=v(c_{o,R}),\qquad
\rho^1_{RR'}(b_{R'})=b_R.
\]

The current tree does not supply the row-311 cochain vectors,
transition cochain maps, cocycle-pullback rows, \(b_R\)-defect rows,
or two-step coherence rows.  Rows 313--314, the torsor defects
\(\omega_{i,\mathcal C}\), are not certified here.

Run:

```sh
python3 compute/verify_rhomred_weyl_orientation_cocycle_cochain_transition.py \
  --fixture certificates/orientation/rhomred_weyl_orientation_cocycle_cochain_transition --check
```
