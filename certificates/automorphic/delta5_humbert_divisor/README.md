# delta5_humbert_divisor

This fixture records the automorphic Humbert-divisor data for
\(\Delta_5\).  It verifies the finite divisor facts used by the
manuscript:

- \(\operatorname{div}(\Delta_5)=H_{\mathrm{Hum}}\);
- the three type-II wall representatives lie in the same Humbert support;
- each representative has \(\Delta_5\)-zero order \(1\);
- the polar divisor of \(\Delta_5^{-2}\) has order \(2\) on the same
  support;
- support equality and multiplicity are separate rows.

The packet is automorphic only.  It is not a Pfaffian wall chart, an O2
wall atlas, a mirror-period discriminant, compact source data, or a
protected trace construction.

Run:

```sh
python3 compute/verify_humbert_divisor_fixture.py \
  --fixture certificates/automorphic/delta5_humbert_divisor \
  --check
```

A positive result is `HUMBERT_DIVISOR_VERIFIED`.
