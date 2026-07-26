# finite_hall_positive_negative_pairing

This packet records correction row 358.

It defines the finite positive-negative Hall pairing matrix
`G_{gamma,p}` for supplied compact source data:

```text
G_{gamma,p;ab} = tr_0(m_R^Theta(e_{gamma,p,a}, e_{-gamma,p,b})).
```

The packet imports formal degree-zero pairing rows only as evidence for
the shape of the definition.  The current compact source still has no
`G_entries.csv` rows, trace functional row, compact pairing
correspondence rows, orientation transport rows, or Hopf-pairing
identity rows.

Run:

```sh
python3 compute/verify_finite_hall_positive_negative_pairing.py \
  --fixture certificates/hall/finite_hall_positive_negative_pairing --check
```

Expected status:

```text
FINITE_HALL_POSITIVE_NEGATIVE_PAIRING_OBSTRUCTION_VERIFIED
```
