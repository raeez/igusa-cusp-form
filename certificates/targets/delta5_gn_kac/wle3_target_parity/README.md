# wle3_target_parity

This fixture records the imported GN/Kac target parity table on the
first arithmetic window \(W_{\le 3}\):

- \(\delta_i:1|0\);
- \(a_{ij}:10|0\);
- \(2\delta_i+\delta_j:1|0\);
- \(\delta_{123}:29|93\).

The verifier recomputes the signed coefficients from
`compute/verify_square_root.py`, checks the real-string exponent, and
checks the decomposition \(29=2+27\), \(93=[qrs]D_5/(qrs)^{1/2}\).
This is a target-reference table only.

Run:

```sh
python3 compute/verify_wle3_target_fixture.py \
  --fixture certificates/targets/delta5_gn_kac/wle3_target_parity \
  --check
```

A positive result is `WLE3_TARGET_PARITY_VERIFIED`.
