# Transition Orientation Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve Joyce--Upmeier orientations.

The reduced-orientation packet is still an empty blocked scaffold.  The
finite-moduli transition-geometry packet records that the stack
transition morphisms are also absent.  Orientation preservation requires
both: actual finite-stage stack transitions and Picard-groupoid
isomorphisms carrying the Joyce--Upmeier orientation line, determinant
square root, quotient Borel null-trivialisations, Thom--Sebastiani
multiplicativity, Weyl lifts, and Coxeter cochains from height `R` to
height `R'`.

Run:

```sh
python3 compute/verify_transition_orientation_preservation_obstruction.py \
  --fixture certificates/orientation/transition_orientation_preservation --check
```

Expected status:

```text
TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof of orientation preservation.  It only
certifies that the obstruction ledger is complete while the core
transport tables remain empty.
