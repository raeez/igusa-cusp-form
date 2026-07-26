# retained_extension_closure fixture

This packet records optimization row 178: retained finite HN rows are
closed under the supplied extension words.

It imports:

- `certificates/moduli/retained_hn_type_bounds`;
- `certificates/moduli/retained_closed_substacks`.

The nonempty binary extension rows check that the middle HN type of
each retained extension lies inside the retained finite HN word set:

- `hn_s3 * hn_s2 -> hn_e32`;
- `hn_s2 * hn_s1 -> hn_e21`;
- `hn_e32 * hn_s1 -> hn_f321`;
- `hn_s3 * hn_e21 -> hn_f321`.

The packet does not construct extension stacks, two-step flag stacks,
closure under HN factors, closure under duals, cosection atlases,
transitions, compact Hall stages, Pfaffian orientations, or protected
traces.

Run:

```sh
python3 compute/verify_retained_extension_closure_fixture.py \
  --fixture certificates/moduli/retained_extension_closure --check
```

The expected status is `RETAINED_EXTENSION_CLOSURE_VERIFIED`.
