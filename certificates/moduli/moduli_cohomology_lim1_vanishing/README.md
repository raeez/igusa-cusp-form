# Moduli Cohomology lim1 Vanishing Obstruction

This packet records the missing data required to prove that
\(R^1\varprojlim\) vanishes on the cohomology towers of the retained
K3xE moduli stacks.

For each retained object, extension, mixed, wrapped, or two-step flag
stack, each coefficient system, and each cohomological degree, one must
construct the finite cohomology groups, the transition maps, and an
explicit Mittag-Leffler image-stabilization witness.  Proper or closed
transition geometry only makes the maps available; it does not prove
that their images stabilize.  Bounded HN types, finite-type substacks,
Euler characteristics, protected traces, and target windows do not
substitute for \(R^1\varprojlim=0\).

Run:

```sh
python3 compute/verify_moduli_cohomology_lim1_vanishing_obstruction.py \
  --fixture certificates/moduli/moduli_cohomology_lim1_vanishing --check
```

Expected status:

```text
MODULI_COHOMOLOGY_LIM1_VANISHING_OBSTRUCTION_VERIFIED
```

This status is not a proof that \(R^1\varprojlim\) vanishes.  It only
certifies that the obstruction ledger is complete while the core
cohomology and Mittag-Leffler tables remain empty.
