# Transition Primitive-Subspace Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve the primitive Hall subspaces
\[
P_R=\ker\widetilde\Delta_R\cap\ker\epsilon_R,\qquad
\widetilde\Delta_R=\Delta_R-\eta_R\epsilon_R\otimes \mathrm{id}
-\mathrm{id}\otimes\eta_R\epsilon_R .
\]

The compact Hall source packet does not yet supply coproduct matrices,
counit maps, primitive kernel rows, primitive projections, or ambient
transition matrices.  The Hall-coproduct transition packet records that
the required coproduct and counit transition identities are also absent.
Primitive-subspace preservation requires the reduced-coproduct and
counit intertwining identity, explicit source and target primitive
kernel rows, a restricted transition matrix on primitives, projection
compatibility, and strict composition.

Run:

```sh
python3 compute/verify_transition_primitive_subspace_preservation_obstruction.py \
  --fixture certificates/hall/transition_primitive_subspace_preservation --check
```

Expected status:

```text
TRANSITION_PRIMITIVE_SUBSPACE_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof that transition maps preserve primitive
subspaces.  It only certifies that the obstruction ledger is complete
while the core transition-primitive tables remain empty.

The separate packet
`certificates/hall/primitive_space_lim1_vanishing` records the missing
Mittag-Leffler image-stabilization and zero `R^1 lim` rows for the
primitive-space inverse systems after such transition maps exist.
