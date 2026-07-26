# Retained Universal Perfect Complexes Certificate

This packet proves optimization row 174 at finite HN height.  For each
retained finite substack it records a universal perfect complex on the
rigidified retained moduli row, a base-change datum, a finite Tor
amplitude, and zero descent and perfection defects.

It certifies only the retained universal-complex row.  It does not
construct finite closed inertia stratifications, extension/flag stacks,
cosection atlases, transitions, Pfaffian orientations, or protected
traces.

Run:

```sh
python3 compute/verify_retained_universal_complexes_fixture.py \
  --fixture certificates/moduli/retained_universal_complexes --check
```
