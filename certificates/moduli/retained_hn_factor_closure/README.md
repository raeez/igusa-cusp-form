# retained_hn_factor_closure fixture

This packet records optimization row 179: every HN factor of a retained
finite HN word is again represented by a retained finite substack.

It imports:

- `certificates/moduli/retained_hn_type_bounds`;
- `certificates/moduli/retained_class_bounds`;
- `certificates/moduli/retained_semistable_substacks`;
- `certificates/moduli/retained_closed_substacks`;
- `certificates/moduli/retained_extension_closure`.

The packet supplies ten factor-occurrence rows: one factor for each
semistable word, two factors for each two-step word, and three factors
for the three-step word.  Each factor occurrence is checked against the
retained class set, the finite-type semistable substack, and the
retained closed substack.

This packet does not prove compactified extension or two-step flag
stacks, subquotient closure in flag stacks, cosection atlases,
transitions, compact Hall stages, Pfaffian orientations, or protected
traces.  Dual closure is supplied by
`certificates/moduli/retained_dual_closure`.

Run:

```sh
python3 compute/verify_retained_hn_factor_closure_fixture.py \
  --fixture certificates/moduli/retained_hn_factor_closure --check
```

The expected status is `RETAINED_HN_FACTOR_CLOSURE_VERIFIED`.
