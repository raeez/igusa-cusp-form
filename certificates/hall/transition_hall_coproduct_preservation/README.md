# Transition Hall-Coproduct Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve the compact Hall coproduct
\(\Delta_R=p_!(\operatorname{TS}^{\mathrm{red}})^{-1}q^*\).

The compact Hall source packet does not yet supply coproduct matrices,
counit maps, or geometric splitting-correspondence rows.  The
transition-geometry, orientation-transition, and
vanishing-cycle-transition packets record that the required transition
morphisms and coefficient transports are also absent.  Hall-coproduct
preservation requires a commuting transition cube for the retained
splitting correspondences, transport of the orientation and reduced
vanishing-cycle coefficient systems, inverse Thom-Sebastiani
compatibility, proper base change, the projection formula,
compact-support pushforward compatibility, coproduct matrix
intertwining, coassociativity and counit compatibility, strict
composition, and Mittag-Leffler exactness.

Run:

```sh
python3 compute/verify_transition_hall_coproduct_preservation_obstruction.py \
  --fixture certificates/hall/transition_hall_coproduct_preservation --check
```

Expected status:

```text
TRANSITION_HALL_COPRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof of Hall-coproduct preservation.  It only
certifies that the obstruction ledger is complete while the core
transition-Hall-coproduct tables remain empty.
