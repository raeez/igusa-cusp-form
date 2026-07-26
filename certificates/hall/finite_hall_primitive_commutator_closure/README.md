This packet records row 354: in a supplied finite counital graded
bialgebra, the supercommutator of primitive elements is primitive.

The theorem is relative.  It uses the bialgebra identities, the
primitive-kernel rows of row 353, and the finite product/coproduct
matrices.  The present compact Hall source does not yet supply those
rows, so this packet verifies the criterion and obstruction ledger, not
a populated compact-source primitive bracket.

Run:

```sh
python3 compute/verify_finite_hall_primitive_commutator_closure.py \
  --fixture certificates/hall/finite_hall_primitive_commutator_closure --check
```

The expected status is
`FINITE_HALL_PRIMITIVE_COMMUTATOR_CLOSURE_OBSTRUCTION_VERIFIED`.
