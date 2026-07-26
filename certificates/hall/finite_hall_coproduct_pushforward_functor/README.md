This packet records row 348: the compact-support criterion for the
exceptional pushforward leg \(p_!\) in the finite Hall coproduct.

For a supplied retained splitting morphism
\[
p_{c,c'}:\overline{\mathfrak E}^{\mathrm{ret}}_{R,c,c'}\to
\mathfrak M^{\mathrm{red}}_{R,c}\times
\mathfrak M^{\mathrm{red}}_{R,c'}
\]
and a supplied bounded constructible coefficient on the splitting
correspondence after pullback and inverse reduced Thom--Sebastiani
transport, the functor \(p_!^{cs}\) exists if \(p\) is proper or if a
compact-support model \(p=\overline p\circ j_p\) is supplied in the
chosen constructible six-functor formalism.

The present repository state does not supply the actual retained
splitting-stack row, retained \(p\)-map row, properness or
compactification row, coefficient row, inverse Thom--Sebastiani row, or
populated pushforward row.  This packet therefore verifies the
criterion and obstruction ledger, not a populated Hall coproduct and
not coassociativity.

Run:

```sh
python3 compute/verify_finite_hall_coproduct_pushforward_functor.py \
  --fixture certificates/hall/finite_hall_coproduct_pushforward_functor --check
```

The expected status is
`FINITE_HALL_COPRODUCT_PUSHFORWARD_FUNCTOR_OBSTRUCTION_VERIFIED`.
