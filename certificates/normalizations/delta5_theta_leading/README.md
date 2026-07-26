# delta5_theta_leading

This fixture records the scalar normalization constants used at the
Igusa type-II cusp:

- \([q^{1/2}r^{1/2}s^{1/2}]\Delta_5=64\);
- \(D_5=64^{-1}\Delta_5\) has monic leading coefficient \(1\);
- \(\Delta_{10}=\Delta_5^2\) has leading coefficient \(4096\);
- \(\chi_{10}^{OP}=D_5^2=4096^{-1}\Delta_{10}\) is monic.
- \(\Delta_{10}\), \(\chi_{10}\), \(\Phi_{10}^{un}\),
  \(\chi_{10}^{OP}\), and their inverse scalar branches are recorded as
  separate conventions in `form_conventions.csv` and `form_relations.csv`.

The table is scalar arithmetic only.  It is not a Pfaffian-line
construction, an O2 wall atlas, an orientation-character computation, or
a compact-source trace.

The sign of the leading constant is convention-dependent: \(+64\) in the
manuscript's phase convention
\(\exp(\pi i(z[l+\tfrac12 a]+{}^tbl))\)
(`03_view1_automorphic.tex`, `sec:view1-theta-normalization`), \(-64\)
in the Mumford convention
\(\exp(\pi i(z[l+\tfrac12 a]+{}^t(l+\tfrac12 a)b))\).  The
`Delta5_theta_leading_mumford` row records the trap;
`compute/verify_theta_product_identity.py` computes the
ten-even-theta-constant product and the Borcherds product from first
principles in both conventions and asserts exact equality (including
the \(+64\)) on the box \(q,s\le 7/2\).

Run:

```sh
python3 compute/verify_theta_normalization_fixture.py \
  --fixture certificates/normalizations/delta5_theta_leading \
  --check
python3 compute/verify_theta_product_identity.py
```

A positive result is `SCALAR_NORMALIZATION_VERIFIED` and
`THETA_PRODUCT_IDENTITY_VERIFIED`.
