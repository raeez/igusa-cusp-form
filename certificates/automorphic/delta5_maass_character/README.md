# delta5_maass_character

This fixture records the automorphic Maass character of the Igusa cusp
form \(\Delta_5\).  It verifies the finite character consequences used
by the manuscript:

- \(\nu_{\Delta_5}(s_{\delta_i})=-1\) on the three type-II Weyl
  generators;
- \(\nu_{\Delta_5}=1\) on the three type-I chamber-automorphism
  generators;
- \(\nu_{\Delta_5}|_{W^{(2)}}=\det\);
- \(\nu_{\Delta_5}^2=1\), so \(\Delta_5^2\) is scalar;
- \(\Delta_5\) is a section of \(L^5\otimes\nu_{\Delta_5}\), not an
  orientation line.

The packet is automorphic only.  It does not construct a Pfaffian
orientation, Weyl-equivariant determinant-line transport, an O2 wall
atlas, compact source representatives, or an OP scalar trace.

Run:

```sh
python3 compute/verify_maass_character_fixture.py \
  --fixture certificates/automorphic/delta5_maass_character \
  --check
```

A positive result is `MAASS_CHARACTER_VERIFIED`.
