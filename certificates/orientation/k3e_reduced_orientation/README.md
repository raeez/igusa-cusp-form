# k3e_reduced_orientation fixture

This directory is a finite reduced-orientation and Weyl-lift scaffold.
It is not a proof of \((O1)\) or \((O1)^+\).

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until a finite
orientation packet supplies row-level mathematical payload and geometric
provenance for:

- reduced orientation lines and determinant square-root isomorphisms;
- Thom-Sebastiani multiplicativity and flag pentagon compatibility;
- quotient Cech-Borel gerbe classes and null-trivialisations;
- finite-stabilizer edge reduction, Klein-four and two-primary mixed
  coefficient calculations, and zero \(H^1\)-linearization characters;
- Weyl lifts, projective cocycle trivialisation, torsor defects, and
  quotient-cocycle transport;
- strict transition and Mittag-Leffler rows;
- scalar-firewall checks excluding scalar trace, squared determinant,
  OP scalar branch, and Maass-character values as orientation data.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the missing cohomological and rank equations: determinant
square roots, orientation-class vanishing, Thom-Sebastiani and pentagon
compatibility, the four quotient Cech-Borel classes, finite-stabilizer
edge reduction, odd-transfer rows, Klein-four and two-primary
coefficients, Weyl lift involutivity, torsor defects,
quotient-cocycle transport, projective-cocycle/cochain/Coxeter rows,
strict transition and Mittag-Leffler rows, and the scalar firewalls.

Transition preservation of orientations is isolated in
`certificates/orientation/transition_orientation_preservation`.  That
packet records the missing Picard-groupoid pullback isomorphisms,
determinant square compatibility, quotient Cech-Borel
null-trivialization transport, finite-stabilizer and zero-linearization
transport, Thom-Sebastiani transition compatibility, Weyl-lift
transition compatibility, Coxeter-cochain transition compatibility,
strict Picard-groupoid transition, and orientation Mittag-Leffler rows.
It verifies only
`TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED`.

It is verified by

```sh
python3 compute/verify_orientation_obstruction_ledger.py \
  --fixture certificates/orientation/k3e_reduced_orientation --check
```

A positive result is `ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED` with
`orientation_certification: false` and `mathematical_certification:
false`.  The verifier also checks that this packet is still the empty
blocked scaffold; if orientation rows are supplied later, this ledger
must be retired or narrowed.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, scalar-only, cyclic-only,
Picard-line-only, status-only, todo, or unsupplied provenance is
rejected.

All defect ranks, Cech-Borel ranks, torsor ranks, square-root ranks,
pentagon ranks, Coxeter ranks, transition ranks, and `R^1 lim` ranks
must be zero. Finite-stabilizer rows must be edge-reduced and must not
be cyclic-only. The rank-two mixed coefficient is an explicit row value,
not an inference from cyclic restrictions.
