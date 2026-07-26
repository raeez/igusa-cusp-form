# k3e_protected_trace fixture

This directory is a finite protected trace scaffold. It is not a
construction of the trace functor and it is not a gravity-line
operator algebra.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until finite rows
supply mathematical payload and provenance for:

- the level-Z trace category and closed `K3 x E -> pt` cobordism;
- the protected trace functor, including functoriality, cyclicity, and
  excision checks;
- the operator being traced and the determinant/inverse-square datum;
- OP and unscaled scalar normalizations, including `64`, `4096`, and
  the OP sign `-1`;
- the trace identity `Delta_5^{-2} = (Phi_10^un)^{-1}`;
- forgetful maps proving that orientation, primitive bracket, Hopf
  pairing, PBW, and parity data are killed by the scalar trace;
- gravity residual rows recording the level-A Hall-Borcherds residual
  as conjectural, not constructed, and not used in the trace proof;
- strict transition and Mittag-Leffler rows;
- scalar-firewall checks excluding orientation characters, Pfaffian
  lines, primitive brackets, Hopf pairings, PBW bases, parity splits,
  source Koszul maps, and gravity path integrals as data recovered from
  the scalar trace.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the missing trace rows: level-Z trace category, closed
`K3 x E -> pt` cobordism, protected trace functor, operator being
traced, OP and unscaled normalizations, inverse-square identities,
forgetful maps, level-A gravity residual separation, strict
transitions, Mittag-Leffler exactness, and scalar firewalls. It is
verified by

```sh
python3 compute/verify_trace_obstruction_ledger.py \
  --fixture certificates/trace/k3e_protected_trace --check
```

A positive result is `TRACE_OBSTRUCTION_LEDGER_VERIFIED` with
`protected_trace_certification: false` and `mathematical_certification:
false`. The verifier also checks that this packet is still the empty
blocked scaffold; if trace rows are supplied later, this ledger must be
retired or narrowed.

Every populated row must carry `geometric_source_id` or
`source_formula_id` where appropriate, together with `proof_reference`.
Placeholder, mock, automorphic-only, OP-only, Pfaffian-only,
determinant-only, target-only, scalar-only, trace-only, gravity-only,
path-integral-only, status-only, todo, or unsupplied provenance is
rejected.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, normalization, trace identity, forgetful-map,
gravity-residual, transition, and scalar-firewall checks passed. It is
not a proof of the global trace theorem and it is not a gravity-line
construction.
