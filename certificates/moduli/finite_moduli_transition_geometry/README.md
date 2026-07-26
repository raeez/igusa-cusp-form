# Finite Moduli Transition Geometry Obstruction

This packet records the missing geometric data required to prove that
finite K3xE moduli transitions are closed embeddings or proper maps.

The finite-moduli packet supplies bounded HN types, finite-type
semistable substacks, derived enhancements, universal complexes,
scalar rigidifications, retained closed substacks, extension closure,
HN-factor closure, and dual closure.  It does not yet supply the
transition morphisms between retained stages.  Row 186 of the
optimization list requires actual morphisms on the object, extension,
and two-step flag stacks, with each component proved proper or a closed
embedding and with zero transition defects.

Run:

```sh
python3 compute/verify_finite_moduli_transition_geometry_obstruction.py \
  --fixture certificates/moduli/finite_moduli_transition_geometry --check
```

Expected status:

```text
FINITE_MODULI_TRANSITION_GEOMETRY_OBSTRUCTION_VERIFIED
```

This status is not a proof of transition properness or closedness.  It
only certifies that the obstruction ledger is complete while the core
transition-geometry tables remain empty.
