This packet records row 344: the compact-support criterion for the
exceptional pushforward leg \(q_!\) in the finite Hall product.

For a supplied retained target morphism
\[
q_{c,c'}:\overline{\mathfrak E}^{\mathrm{ret}}_{R,c,c'}\to
\mathfrak M^{\mathrm{red}}_{R,c+c'}
\]
and a supplied bounded constructible coefficient on the extension
correspondence after pullback and reduced Thom--Sebastiani transport,
the functor \(q_!^{cs}\) exists if \(q\) is proper or if a
compact-support model \(q=\overline q\circ j_q\) is supplied in the
chosen constructible six-functor formalism.

The present repository state does not supply the actual retained
extension-stack row, retained \(q\)-map row, properness or
compactification row, coefficient row, or populated pushforward row.
This packet therefore verifies the criterion and obstruction ledger,
not a populated Hall product and not compactification independence.

Run:

```sh
python3 compute/verify_finite_hall_product_pushforward_functor.py \
  --fixture certificates/hall/finite_hall_product_pushforward_functor --check
```

The expected status is
`FINITE_HALL_PRODUCT_PUSHFORWARD_FUNCTOR_OBSTRUCTION_VERIFIED`.
