# Primitive Space lim1 Vanishing Obstruction

This packet records the missing data required to prove that
\(R^1\varprojlim\) vanishes on the primitive Hall-space towers used in
primitive recognition.

For each cofinal finite root window, each retained Gram degree, and each
parity, one must construct the finite primitive space, a basis, the
restricted primitive transition maps, identity and composition rows, and
an explicit Mittag-Leffler image-stabilization witness.  Transition
preservation of primitive subspaces only makes the inverse system
available; it does not prove that the images stabilize.  Signed
multiplicities, target windows, denominator products, primitive-kernel
headers, radical-transition rows, and PBW-transition rows do not
substitute for \(R^1\varprojlim=0\).

Run:

```sh
python3 compute/verify_primitive_space_lim1_vanishing_obstruction.py \
  --fixture certificates/hall/primitive_space_lim1_vanishing --check
```

Expected status:

```text
PRIMITIVE_SPACE_LIM1_VANISHING_OBSTRUCTION_VERIFIED
```

This status is not a proof that \(R^1\varprojlim\) vanishes on primitive
spaces.  It only certifies that the obstruction ledger is complete while
the core primitive-space and Mittag-Leffler tables remain empty.
