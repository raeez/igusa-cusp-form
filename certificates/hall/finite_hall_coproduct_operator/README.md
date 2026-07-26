This packet records row 347: the finite compact Hall coproduct
operator
\[
\Delta_R^{\mathrm{red}}
=p_!^{cs}(\operatorname{TS}^{\mathrm{red}})^{-1}q^*.
\]

The packet verifies the definition only.  It does not supply the
retained splitting correspondence, the \(q^*\) row, the \(p_!\) row for
the reversed correspondence, inverse Thom--Sebastiani transport,
compactification independence, coproduct matrices, counit rows,
coassociativity, bialgebra compatibility, transition compatibility, or
primitive closure.

Run:

```sh
python3 compute/verify_finite_hall_coproduct_operator_definition.py \
  --fixture certificates/hall/finite_hall_coproduct_operator --check
```

The expected status is
`FINITE_HALL_COPRODUCT_OPERATOR_DEFINITION_VERIFIED`.
