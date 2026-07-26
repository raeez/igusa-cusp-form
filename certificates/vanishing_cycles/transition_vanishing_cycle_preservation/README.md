# Transition Vanishing-Cycle Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve reduced perverse sheaves of vanishing cycles.

The D0-HN packet does not yet supply reduced vanishing-cycle transition
rows.  The finite-moduli transition-geometry packet does not yet supply
the underlying stack transition morphisms.  The orientation-transition
packet does not yet supply the Picard-groupoid orientation transport
needed by the BBDJS gluing of vanishing-cycle sheaves.

Vanishing-cycle preservation requires chart-level data: transition
maps of oriented d-critical charts, potential compatibility up to the
allowed quadratic stabilization, pullback compatibility of the K3
semiregularity cosection, maps of reduced obstruction complexes, graph
pullback isomorphisms of the reduced vanishing-cycle complexes,
perverse normalization, Thom-Sebastiani compatibility, proper
base-change compatibility, strict composition, and Mittag-Leffler
exactness.

Run:

```sh
python3 compute/verify_transition_vanishing_cycle_preservation_obstruction.py \
  --fixture certificates/vanishing_cycles/transition_vanishing_cycle_preservation --check
```

Expected status:

```text
TRANSITION_VANISHING_CYCLE_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof of vanishing-cycle preservation.  It only
certifies that the obstruction ledger is complete while the core
transition-vanishing-cycle tables remain empty.
