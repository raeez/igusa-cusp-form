This packet records row 342: the finite Hall product operator
\[
m_R^{\mathrm{red}}=q_!\operatorname{TS}^{\mathrm{red}}p^*.
\]

The packet verifies only the definition of the formal pull--TS--push
operator on the retained compactified extension correspondence.  It
does not prove the existence of \(p^*\), the existence of \(q_!\), or
compactification independence.  It also does not populate product
matrices, associativity witnesses, product-transition rows, primitive
closure, or Hopf data.

Run:

```sh
python3 compute/verify_finite_hall_product_operator_definition.py \
  --fixture certificates/hall/finite_hall_product_operator --check
```

The expected status is
`FINITE_HALL_PRODUCT_OPERATOR_DEFINITION_VERIFIED`.
