# Retained Class Bounds Certificate

This packet proves optimization rows 170--173 at finite HN height.  It
defines the retained finite class set `C_R`, assigns each retained
class its Hilbert-polynomial label `P_{c,i}`, records the
cohomological amplitude interval `[a_c,b_c]`, and records a finite
regularity bound `N_c`.

It certifies only finite class-bound data imported from the retained
HN type-bound and semistable-substack packets.  It does not construct
universal complexes, finite closed inertia stratifications,
extension/flag stacks, cosection atlases, transitions, Pfaffian
orientations, or protected traces.

Run:

```sh
python3 compute/verify_retained_class_bounds_fixture.py \
  --fixture certificates/moduli/retained_class_bounds --check
```
