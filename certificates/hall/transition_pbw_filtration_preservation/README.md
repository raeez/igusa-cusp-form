# Transition PBW Filtration Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve the PBW filtrations on the primitive
recognition towers.

After radical quotients are formed, PBW preservation is a filtered
statement about the induced maps on universal enveloping algebras.  It
requires source and target PBW filtration rows, ordered word bases,
relation-rewrite data, quotient transition matrices, multiplicative
word transitions, filtered-image identities, associated-graded
transition matrices, the \(A_\beta\)-PBW square, and composition rows.
Primitive or radical transition preservation alone does not supply
these rows.

Run:

```sh
python3 compute/verify_transition_pbw_filtration_preservation_obstruction.py \
  --fixture certificates/hall/transition_pbw_filtration_preservation --check
```

Expected status:

```text
TRANSITION_PBW_FILTRATION_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof that transition maps preserve PBW
filtrations.  It only certifies that the obstruction ledger is complete
while the core transition-PBW tables remain empty.

The separate packet
`certificates/hall/pbw_associated_graded_lim1_vanishing` records the
missing Mittag-Leffler image-stabilization and zero `R^1 lim` rows for
the PBW associated-graded towers.  Filtered transition preservation
supplies the associated-graded maps only after its own rows exist; it
does not prove PBW associated-graded Mittag-Leffler exactness.
