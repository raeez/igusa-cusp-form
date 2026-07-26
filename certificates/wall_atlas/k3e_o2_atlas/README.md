# k3e_o2_atlas fixture

This directory is a retained type-II wall-atlas scaffold for the
`(O2_atlas)` datum. It is not a proof of the O2 wall-normal-form
theorem.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until finite HN-window
rows supply mathematical payload and geometric provenance for:

- retained type-II wall objects with full charge match, wall
  semistability, reduced self-Ext splitting, rank-one normal Pfaffian
  block, invariant unit, and quotient orientation;
- rank-one wall charts with normal rank `1`, divisor order `1`, unit
  invariance, coordinate flip under reflection, and local sign `-1`;
- overlap transition isomorphisms, Cech two-cocycles, and cochains with
  zero coboundary, unit, and orientation defects;
- Weyl orbit transport rows preserving Pfaffian charts, normal rank, and
  sign;
- half-Hilbert orbit rows with twelve binary wall coordinates,
  cardinality `2^12=4096`, and zero coverage defect;
- Thom-Sebastiani, HN-transition, Weyl-lift, quotient-orientation,
  protected-integration, boundary, and component compatibility rows;
- scalar-separation checks recording `4096=2^12=64^2` only after passing
  to the scalar shadow, while excluding OP scalar normalization, Maass
  character values, and squared theta-leading constants as wall-atlas
  data.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the missing O2 rows: simple wall coverage, charge match,
wall semistability, reduced self-Ext splitting, rank-one normal blocks,
invariant units, quotient orientations, middle-wall wrapped object,
normal coordinates, tangent Pfaffian lines, rank-one chart identities,
overlaps, Weyl transport, half-Hilbert orbit data, compatibility rows,
type-I exclusion, D0-limit extension, and scalar firewalls. It is
verified by

```sh
python3 compute/verify_o2_obstruction_ledger.py \
  --fixture certificates/wall_atlas/k3e_o2_atlas --check
```

A positive result is `O2_OBSTRUCTION_LEDGER_VERIFIED` with
`o2_certification: false` and `mathematical_certification: false`. The
verifier also checks that this packet is still the empty blocked
scaffold; if wall-atlas rows are supplied later, this ledger must be
retired or narrowed.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, local-only, generic-chart-only,
signed-only, scalar-only, OP-scalar-only, Maass-character-only,
status-only, todo, or unsupplied provenance is rejected.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, compatibility, half-Hilbert count, and scalar
separation checks passed. It is not a proof of the global O2 theorem.
