# Mixed Correspondence Base Change

This packet records correction row 225.  For the one-sided mixed
correspondence orders \(LW\) and \(WL\), it records Cartesian
compact-support squares
\[
\mathfrak E'\to\mathfrak E,\qquad
\overline{\mathfrak E}'\to\overline{\mathfrak E},\qquad
Z'\to Z
\]
and the coefficient identification \(K'\simeq \widetilde g^*K\).
For the compact-support model
\[
q^{\mathrm{cs}}_!K=\overline q_*j_!K,
\]
proper base change for \(\overline q\) and base change for the open
immersion \(j\) give
\[
g^*q^{\mathrm{cs}}_!K\simeq q'{}^{\mathrm{cs}}_!K'.
\]

This packet proves only that base-change row.  It does not prove the
projection formula, Thom--Sebastiani transport, quotient descent,
transition compatibility, compactification-choice independence, or
associativity.

Run:

```sh
python3 compute/verify_mixed_correspondence_base_change_obstruction.py \
  --fixture certificates/hybrid/mixed_correspondence_base_change --check
```

Expected status:

```text
MIXED_CORRESPONDENCE_BASE_CHANGE_VERIFIED
```
