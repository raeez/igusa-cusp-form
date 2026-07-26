# rhomred_delta123_chart_orientation

This packet verifies row 331 as a chart-orientation criterion for the
first timelike degree

```text
delta123 = delta_1 + delta_2 + delta_3.
```

The imported target packets certify the presentation split
`delta123:29|93`, with `29=2+27` and `29-93=-64`.  If a retained
compact Hall source chart realizes this decomposition as the reduced
coefficient block and supplies the quotient orientation,
determinant-square row, and transition row, the local orientation sign is

```text
(-1)^93 = -1.
```

This packet does not construct that source chart.  It records the exact
missing source rows and excludes the target presentation, scalar
supermultiplicity, Pfaffian obstruction ledger, and protected trace as
substitutes for compact source orientation data.

Verifier:

```bash
python3 compute/verify_rhomred_delta123_chart_orientation.py \
  --fixture certificates/orientation/rhomred_delta123_chart_orientation \
  --check
```

A positive result is
`RHOMRED_DELTA123_CHART_ORIENTATION_OBSTRUCTION_VERIFIED`.
