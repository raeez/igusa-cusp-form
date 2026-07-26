# Transition Hall-Product Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve the compact Hall product
\(m_R=q_!\operatorname{TS}^{\mathrm{red}}p^*\).

The compact Hall source packet does not yet supply product matrices or
geometric extension-correspondence rows.  The transition-geometry,
orientation-transition, and vanishing-cycle-transition packets record
that the required transition morphisms and coefficient transports are
also absent.  Hall-product preservation requires a commuting transition
cube for the retained extension correspondences, transport of the
orientation and reduced vanishing-cycle coefficient systems,
Thom-Sebastiani compatibility, proper base change, the projection
formula, compact-support pushforward compatibility, product matrix
intertwining, associativity compatibility, strict composition, and
Mittag-Leffler exactness.

Run:

```sh
python3 compute/verify_transition_hall_product_preservation_obstruction.py \
  --fixture certificates/hall/transition_hall_product_preservation --check
```

Expected status:

```text
TRANSITION_HALL_PRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof of Hall-product preservation.  It only
certifies that the obstruction ledger is complete while the core
transition-Hall-product tables remain empty.
