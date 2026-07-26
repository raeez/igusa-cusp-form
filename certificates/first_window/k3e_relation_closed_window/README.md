# k3e_relation_closed_window fixture

This directory is a scaffold for the first relation-closed compact
source recognition window. It is not a computation of primitive
recognition.

The target-side height-window convention and target-root exhaustion are
supplied separately by `certificates/lattice/downward_root_windows` and
`certificates/lattice/active_root_window_exhaustion`.  The source-window
compact-support obstruction ledger is
`certificates/sources/source_window_compact_support`.  The target/source
compatibility obstruction ledger is
`certificates/sources/target_source_window_compatibility`.  This packet
still lacks the compact-source `window_closure.csv` rows.

The packet is intentionally `first_window_scalar_firewall_blocked`.
Only the scalar-exclusion rows are populated.  The verifier must return
`BLOCKED` until finite rows supply mathematical payload and
compact-source provenance for:

- a compact-source `window_closure.csv` row using the target
  height-window convention, relation closure, and active exhaustion;
- target-source representatives with compact cycle provenance and full
  even/odd parity ranks;
- Cartan, Chevalley, real Serre, Borcherds orthogonality, and super
  sign matrices;
- the Hall-Chevalley boundary complex with `d1^2 = 0`;
- the finite-window spectral sequence with vanishing higher
  differentials and strong convergence;
- computed kernel bases, GN/Kac kernel agreement, radical ranks, and
  no-extra kernel equality;
- PBW associated-graded rank comparisons and strict filtrations;
- first-window theorem rows for O1, O1+, O2, Pfin, Hall product, Hall
  coproduct, Hopf pairing, Koszul comparison, PBW comparison, primitive
  recognition, and Pfaffian equality;
- strict transition and Mittag-Leffler rows;
- scalar-firewall checks excluding target labels, signed dimensions,
  scalar traces, Pfaffian products, denominator products, target PBW
  rows, arbitrary matrices, and status-only rows as first-window proof.

The populated `scalar_firewall.csv` rows cite
Lemma `lem:first-window-scalar-exclusions` of the manuscript.  They
verify only that the listed scalar or target-side substitutes are not
first-window primitive-recognition proof.  They do not supply compact
source representatives, Hall operations, pairings, kernels, PBW rows,
or transition maps.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, target-only, target-label-only,
signed-only, denominator-only, Pfaffian-only, scalar-only,
arbitrary-matrix, status-only, todo, or unsupplied provenance is
rejected.

The file `blocked_obligations.csv` is the first-window obstruction
ledger.  It records the missing rows for the window closure,
target-source representatives, Chevalley and Serre matrices,
Hall-Chevalley boundary complex, spectral sequence, kernel equality,
PBW comparison, theorem packet, and strict transitions.  Run:

```bash
python3 compute/verify_first_window_obstruction_ledger.py \
  --fixture certificates/first_window/k3e_relation_closed_window --check
```

A positive result is `FIRST_WINDOW_OBSTRUCTION_LEDGER_VERIFIED` with
`first_window_certification: false` and
`mathematical_certification: false`.  It verifies that the missing
finite theorem rows are recorded while the packet remains
`first_window_scalar_firewall_blocked`.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, relation coverage, theorem coverage, rank equalities,
defect ranks, spectral sequence, PBW, transition, and scalar-firewall
checks passed. It is not a proof of the first-window theorem.
