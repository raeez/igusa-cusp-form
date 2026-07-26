# rhomred_weyl_orientation_cocycle_class_vanishing

This packet verifies row 310 as a finite cohomology criterion.  Given
the populated row-309 cocycle
\[
c_{o,R}\in Z^2(\mathcal G_R;\underline{\mathbb F}_{2,o}),
\]
row 310 proves \([c_{o,R}]=0\) by the rank identity
\[
\operatorname{rank}_{\mathbb F_2}(d^1_R)
=
\operatorname{rank}_{\mathbb F_2}[d^1_R\mid v(c_{o,R})].
\]

The current tree does not supply cocycle values, normalized
cochain-complex bases, a coboundary matrix, or a rank certificate.
Row 311, the choice of a killing \(1\)-cochain, is not certified here.

Run:

```sh
python3 compute/verify_rhomred_weyl_orientation_cocycle_class_vanishing.py \
  --fixture certificates/orientation/rhomred_weyl_orientation_cocycle_class_vanishing --check
```
