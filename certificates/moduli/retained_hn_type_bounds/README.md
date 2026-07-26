# Retained HN Type Bounds Certificate

This packet records the bounded HN-type row for a retained active
window.  The finite retained-window HN filtration packet supplies the
semistable factors and exact filtrations.  Here the verifier checks
that the semistable factor type set is finite, that every HN type word
has length bounded by the retained length rank, and that all object HN
types in the active window lie in the displayed finite set.

Run:

```
python3 compute/verify_retained_hn_type_bounds_fixture.py --fixture certificates/moduli/retained_hn_type_bounds --check
```

Expected status:

```
RETAINED_HN_TYPE_BOUNDS_VERIFIED
```

The packet mirrors its `hn_type_bounds.csv` rows into
`certificates/moduli/k3e_finite_moduli/hn_type_bounds.csv`.  It does
not construct finite-type semistable substacks, quasi-smooth derived
enhancements, universal complexes, compact Hall stages, Pfaffian
orientations, or protected traces.
