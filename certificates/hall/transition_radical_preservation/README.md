# Transition Radical Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve the Hopf-pairing radical
\[
\operatorname{Rad}_{R,\gamma,\bar p}^{\Pi}
=\{x\in P_{R,\gamma,\bar p}^{\Pi}\mid
\langle x,y\rangle_R=0
\text{ for all }y\in P_{R,-\gamma,\bar p}^{\Pi}\}.
\]

Primitive-subspace preservation is not enough.  To prove
\(T_R^{\Prim}(\operatorname{Rad}_R^\Pi)\subset
\operatorname{Rad}_{R'}^\Pi\), one must supply source and target
Hopf-pairing matrices, source and target radical kernels, a lift of
target opposite primitives to the source stage or an equivalent finite
pairing-kernel intertwining identity, restricted radical transition
matrices, and quotient transition matrices.

Run:

```sh
python3 compute/verify_transition_radical_preservation_obstruction.py \
  --fixture certificates/hall/transition_radical_preservation --check
```

Expected status:

```text
TRANSITION_RADICAL_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof that transition maps preserve radicals.  It
only certifies that the obstruction ledger is complete while the core
transition-radical tables remain empty.

The separate packet
`certificates/hall/pairing_kernel_lim1_vanishing` records the missing
Mittag-Leffler image-stabilization and zero `R^1 lim` rows for the
left and right Hopf-pairing kernel towers.  Radical preservation gives
transition maps only after its own rows exist; it does not prove
pairing-kernel Mittag-Leffler exactness.
