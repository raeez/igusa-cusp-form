# k3e_finite_pfaffian fixture

This directory is a finite geometric Pfaffian datum scaffold. It is not
a proof of the Pfaffian--Dirac theorem.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until a finite
geometric Pfaffian datum supplies row-level mathematical payload and
geometric provenance for:

- cosection-reduced skew perfect self-Ext complexes;
- Pfaffian lines, orientations, and determinant-square isomorphisms;
- finite Pfaffian sections with support, parity, exponent, and skew
  block data;
- rank-one type-II wall charts, local divisor order, and sign rows;
- Pfaffian-to-automorphic line comparisons with leading coefficient,
  weight, character, and squaring compatibility;
- strict transition and Mittag-Leffler rows for the Pfaffian line and
  section systems;
- scalar-firewall checks excluding scalar Borcherds products, squared
  determinants, OP scalar traces, and exponent tables as entries of
  `P_fin`.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the missing finite Pfaffian rows: retained quotient strata,
cosection-reduced skew self-dual perfect complexes, reduced obstruction
theory and quotient compatibility, Pfaffian determinant lines,
determinant-square isomorphisms, orientation input, finite Pfaffian
sections with active support and parity ranks, type-II wall normal-form
rows, Pfaffian-to-automorphic line comparisons, strict transition and
Mittag-Leffler rows, and scalar firewalls.  It is verified by

```sh
python3 compute/verify_pfaffian_obstruction_ledger.py \
  --fixture certificates/pfaffian/k3e_finite_pfaffian --check
```

A positive result is `PFAFFIAN_OBSTRUCTION_LEDGER_VERIFIED` with
`pfaffian_certification: false` and `mathematical_certification:
false`.  The verifier also checks that this packet is still the empty
blocked scaffold; if finite Pfaffian rows are supplied later, this
ledger must be retired or narrowed.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, target-only, signed-only,
scalar-only, status-only, todo, or unsupplied provenance is rejected.

Rank and scalar rows are identities, not comments: all defect ranks,
cohomology ranks, residuals, and `R^1 lim` ranks must be zero; type-II
normal Pfaffian rank and wall divisor order must be one; the local
simple-reflection sign must be `-1`; the automorphic comparison must
have leading coefficient `64`, weight `5`, and character `nu_delta5`.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, scalar firewall, and local identity checks passed. It
is not a proof of the global Pfaffian theorem.
