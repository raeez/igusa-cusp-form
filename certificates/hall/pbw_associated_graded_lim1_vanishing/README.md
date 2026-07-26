# PBW Associated-Graded lim1 Vanishing Obstruction

This packet records the missing data required to prove that
\(R^1\varprojlim\) vanishes on the PBW associated-graded towers used in
primitive recognition.

For each cofinal finite root window, each retained PBW degree, each
retained Gram degree, and each parity, one must construct the finite
filtered PBW pieces, the associated-graded quotients, bases for those
graded quotients, the associated-graded transition maps, identity and
composition rows, and an explicit Mittag-Leffler image-stabilization
witness.  Filteredness of the transition, a PBW rank equality, a Hilbert
series, a target PBW table, or a formal pushforward statement does not
prove that the associated-graded tower has \(R^1\varprojlim=0\).

Run:

```sh
python3 compute/verify_pbw_associated_graded_lim1_vanishing_obstruction.py \
  --fixture certificates/hall/pbw_associated_graded_lim1_vanishing --check
```

Expected status:

```text
PBW_ASSOCIATED_GRADED_LIM1_VANISHING_OBSTRUCTION_VERIFIED
```

This status is not a proof that \(R^1\varprojlim\) vanishes on PBW
associated gradeds.  It only certifies that the obstruction ledger is
complete while the core PBW associated-graded and Mittag-Leffler tables
remain empty.
