# retained_dual_closure fixture

This packet records optimization row 180: when duals are needed, the
retained finite HN window is closed under the supplied duality
involution.

It imports:

- `certificates/moduli/retained_hn_type_bounds`;
- `certificates/moduli/retained_class_bounds`;
- `certificates/moduli/retained_closed_substacks`;
- `certificates/moduli/retained_hn_factor_closure`.

The factor duality is

- `type_s3 <-> type_s1`;
- `type_s2 -> type_s2`.

The induced HN-word duality reverses the HN word and dualizes each
factor.  Thus `hn_e32 <-> hn_e21`, `hn_f321 -> hn_f321`, and
`hn_zero -> hn_zero`.

This packet does not construct compactified extension or two-step flag
stacks, subquotient closure in flag stacks, cosection atlases,
transitions, compact Hall stages, Pfaffian orientations, or protected
traces.

Run:

```sh
python3 compute/verify_retained_dual_closure_fixture.py \
  --fixture certificates/moduli/retained_dual_closure --check
```

The expected status is `RETAINED_DUAL_CLOSURE_VERIFIED`.
