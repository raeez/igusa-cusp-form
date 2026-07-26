# Mixed Correspondence Projection Formula

This packet records correction row 226.  For the one-sided mixed
correspondence orders \(LW\) and \(WL\), it records the compact-support
projection formula for a chosen model
\[
q^{\mathrm{cs}}_!K=\overline q_*j_!K.
\]
For a retained finite-Tor target coefficient \(L\), the formula is
\[
q^{\mathrm{cs}}_!\bigl(K\otimes^{\mathbf L}q^*L\bigr)
\simeq q^{\mathrm{cs}}_!K\otimes^{\mathbf L}L.
\]
The proof factors through the projection formula for the open immersion
\(j\), then the proper projection formula for \(\overline q\).

This packet proves only that projection-formula row.  It does not prove
Thom--Sebastiani transport, quotient descent, transition compatibility,
compactification-choice independence, or associativity.

Run:

```sh
python3 compute/verify_mixed_correspondence_projection_formula_obstruction.py \
  --fixture certificates/hybrid/mixed_correspondence_projection_formula --check
```

Expected status:

```text
MIXED_CORRESPONDENCE_PROJECTION_FORMULA_VERIFIED
```
