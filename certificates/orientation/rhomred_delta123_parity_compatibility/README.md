# rhomred_delta123_parity_compatibility

This packet verifies row 332 as a line-level compatibility criterion.
The target data certify `delta123:29|93`, and row 331 computes the local
chart sign `(-1)^93=-1` under a supplied source chart.  Row 332 is
stronger: it asks for the Joyce-Upmeier orientation line itself to be
compatible with the source parity decomposition.

The required line-level square is

```text
o_123^{tensor 2} ~= det K_red,123
                  ~= det K_even,123 tensor det(K_odd,123)^{-1}.
```

The packet records that the current manuscript has no source parity
block, no parity involution, no source-to-target comparison rows, no
orientation square-root row, no quotient orientation, no parity
transition row, and no Picard-groupoid transition row for this degree.

Verifier:

```bash
python3 compute/verify_rhomred_delta123_parity_compatibility.py \
  --fixture certificates/orientation/rhomred_delta123_parity_compatibility \
  --check
```

A positive result is
`RHOMRED_DELTA123_PARITY_COMPATIBILITY_OBSTRUCTION_VERIFIED`.
