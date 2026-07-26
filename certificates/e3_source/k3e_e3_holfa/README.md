# k3e_e3_holfa fixture

This directory is a finite holomorphic E3-prefactorization and
K3-to-E specialization scaffold. It is not a construction of the
compact K3xE source.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until finite HN-window
rows supply mathematical payload and geometric provenance for:

- formal K3xE target charts and finite retained local models;
- field complexes with differential, shifted symplectic pairing, and
  elliptic degree window;
- holomorphic E3 operations, including unit, binary product,
  little-3-disks action, and higher coherence rows;
- BV quantum master equation rows with classical, quantum, and anomaly
  defects zero;
- anomaly, framing, and formality rows, including the holomorphic
  de Rham obstruction and its trivialization;
- compact retained support rows excluding boundary-only or scalar-only
  replacements;
- prefactorization descent rows with Cech, locality, and descent
  defects zero;
- K3-to-E chain specialization rows compatible with cosection,
  wrapped legs, vanishing cycles, orientations, and Pfaffian lines;
- strict transition and Mittag-Leffler rows with `R^1 lim` rank zero;
- scalar-firewall checks excluding automorphic sections, Borcherds
  denominators, target current envelopes, protected traces, and
  hybrid-carrier-only data as entries of the compact E3 source.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the missing E3-source rows: formal target charts, field
complexes, holomorphic E3 operations, BV quantum master equation,
anomaly and holomorphic de Rham trivializations, compact support,
prefactorization descent, K3-to-E chain specialization, strict
transitions, Mittag-Leffler exactness, and scalar firewalls. It is
verified by

```sh
python3 compute/verify_e3_source_obstruction_ledger.py \
  --fixture certificates/e3_source/k3e_e3_holfa --check
```

A positive result is `E3_SOURCE_OBSTRUCTION_LEDGER_VERIFIED` with
`e3_source_certification: false` and `mathematical_certification:
false`. The verifier also checks that this packet is still the empty
blocked scaffold; if E3-source rows are supplied later, this ledger
must be retired or narrowed.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, scalar-only, target-only,
hybrid-only, Pfaffian-only, denominator-only, trace-only, status-only,
todo, or unsupplied provenance is rejected.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, operation coverage, anomaly coverage, defect, ML, and
scalar-firewall checks passed. It is not a proof of the compact source.
