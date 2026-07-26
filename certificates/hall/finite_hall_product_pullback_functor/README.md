This packet records row 343: the criterion for the pullback leg
\(p^*\) in the finite Hall product.

For a supplied finite-type retained extension morphism
\[
p_{c,c'}:\overline{\mathfrak E}^{\mathrm{ret}}_{R,c,c'}\to
\mathfrak M^{\mathrm{red}}_{R,c}\times
\mathfrak M^{\mathrm{red}}_{R,c'}
\]
inside the chosen constructible six-functor formalism, and for a
supplied bounded constructible coefficient on the input product stack,
the pullback \(p_{c,c'}^*\) exists.

The present repository state does not supply the actual retained
extension-stack row, \(p\)-map finite-type row, coefficient row, or
populated pullback row.  This packet therefore verifies the criterion
and obstruction ledger, not a populated Hall product.

Run:

```sh
python3 compute/verify_finite_hall_product_pullback_functor.py \
  --fixture certificates/hall/finite_hall_product_pullback_functor --check
```

The expected status is
`FINITE_HALL_PRODUCT_PULLBACK_FUNCTOR_OBSTRUCTION_VERIFIED`.
