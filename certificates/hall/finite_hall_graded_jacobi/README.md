This packet records row 355: the Hall bracket satisfies graded Jacobi
for supplied finite associative graded Hall data.

The theorem is relative.  The supercommutator in an associative
\(\mathbb Z/2\)-graded algebra satisfies graded Jacobi; after row 354
closure, the identity restricts to the primitive Hall subspace.  The
present compact source has no populated product, bracket, parity,
primitive-closure, or Jacobi rows, so this packet verifies the
criterion and obstruction ledger only.

Run:

```sh
python3 compute/verify_finite_hall_graded_jacobi.py \
  --fixture certificates/hall/finite_hall_graded_jacobi --check
```

The expected status is
`FINITE_HALL_GRADED_JACOBI_OBSTRUCTION_VERIFIED`.
