# rhomred_weyl_orientation_cocycle

This packet verifies row 309 as a formula and obstruction ledger.  Given
a populated finite partial action groupoid \(\mathcal G_R\) and chosen
orientation-line lifts \(\tau_g\), the projective cocycle is defined by

\[
g^*\tau_h\circ\tau_g=(-1)^{c_{o,R}(h,g;S)}\tau_{hg}.
\]

The current tree does not supply the groupoid, lift, composable-pair,
normalization, or cocycle-defect rows.  Row 310, the vanishing of
\([c_{o,R}]\), is not certified here.

Run:

```sh
python3 compute/verify_rhomred_weyl_orientation_cocycle.py \
  --fixture certificates/orientation/rhomred_weyl_orientation_cocycle --check
```
