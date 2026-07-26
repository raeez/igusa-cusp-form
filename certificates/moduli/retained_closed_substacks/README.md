# retained_closed_substacks fixture

This packet records optimization row 177: the retained finite substacks
are retained as closed substacks with a finite closed cover and finite
residual inertia after scalar rigidification.

It imports:

- `certificates/moduli/retained_semistable_substacks`;
- `certificates/moduli/retained_rigidification_inertia`;
- `certificates/moduli/retained_e_translation_rigidifications`.

It supplies one closed retained substack and one closed-cover row for
each retained semistable substack.  The mirrored
`stratifications.csv` rows in
`certificates/moduli/k3e_finite_moduli` record positive finite strata
count, finite residual inertia, zero coverage defect, and zero inertia
defect.

This packet does not prove closure under extensions, closure under HN
factors, closure under duals, extension/flag stacks, cosection
atlases, transitions, compact Hall stages, Pfaffian orientations, or
protected traces.

Run:

```sh
python3 compute/verify_retained_closed_substacks_fixture.py \
  --fixture certificates/moduli/retained_closed_substacks --check
```

The expected status is `RETAINED_CLOSED_SUBSTACKS_VERIFIED`.
