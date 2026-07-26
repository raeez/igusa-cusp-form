# delta123_presentation_split

This fixture records the target presentation split at the first timelike
degree

```text
delta123 = delta_1 + delta_2 + delta_3.
```

It checks `norm=-6`, `smult=-64`, the monic `qrs` coefficient `93`,
the additive correction `m(delta123)=-93`, the even count
`29=2+27`, and the odd imaginary-simple fibre of rank `93`.

The table `real_real_real_words.csv` records the three Jacobi words
`T_1,T_2,T_3` modulo one relation.  The table
`mixed_real_isotropic_words.csv` records the `27=3*9` words
`[e_k,u_{ij,r}]`.  The table `odd_imaginary_generators.csv` records
the 93 target odd generators `xi_delta123_001` through
`xi_delta123_093`.

This is target data only.  It does not construct compact source
representatives, source Hall brackets, source parity, pairing radicals,
PBW data, Pfaffian orientations, O2 wall atlases, mirror discriminants,
or protected traces.

Run:

```sh
python3 compute/verify_delta123_presentation_split_fixture.py \
  --fixture certificates/targets/delta5_gn_kac/delta123_presentation_split \
  --check
```

A positive result is `DELTA123_PRESENTATION_SPLIT_VERIFIED`.
