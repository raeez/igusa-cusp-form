# k3e_finite_moduli fixture

This directory is a retained finite-moduli and d-critical/cosection
atlas scaffold.  Its HN type-bound rows are populated from
`certificates/moduli/retained_hn_type_bounds`, its finite-type
semistable-substack rows are populated from
`certificates/moduli/retained_semistable_substacks`, and its
quasi-smooth derived-enhancement rows are populated from
`certificates/moduli/retained_derived_enhancements`.  Its scalar
rigidification / finite residual inertia rows are populated from
`certificates/moduli/retained_rigidification_inertia`.  Its finite
class set, Hilbert-polynomial, cohomological-amplitude, and regularity
bound rows are populated from
`certificates/moduli/retained_class_bounds`.  Its universal perfect
complex rows are populated from
`certificates/moduli/retained_universal_complexes`.  Its
E-translation rigidification rows are populated from
`certificates/moduli/retained_e_translation_rigidifications`.  Its
retained closed-substack and finite closed-cover rows are populated
from `certificates/moduli/retained_closed_substacks`.  Its retained
extension-closure rows are populated from
`certificates/moduli/retained_extension_closure`.  Its retained
HN-factor-closure rows are populated from
`certificates/moduli/retained_hn_factor_closure`.  Its retained
dual-closure rows are populated from
`certificates/moduli/retained_dual_closure`; the remaining
Hall-correspondence and atlas rows are not yet supplied.

The packet is intentionally `retained_dual_closure_partial_blocked`.
The full finite-moduli verifier must return `BLOCKED` until finite
HN-window rows supply
mathematical payload and geometric provenance for:

- compactified extension and two-step flag stacks, finite type,
  quasi-smooth, proper or closed, and closed under subquotients;
- d-critical charts, cosections, vanishing-cycle complexes, and
  orientation lines with zero compatibility defects;
- strict transition and Mittag-Leffler rows with `R^1 lim` rank zero;
- scalar-firewall checks excluding formal charge windows, Liu
  stability alone, Hilbert-scheme scalar tests, target windows, and
  Pfaffian products as finite-moduli data.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the remaining missing finite-moduli rows: extension and
two-step flag stacks, d-critical cosection charts, transitions,
Mittag-Leffler exactness, and scalar firewalls.

The proper-or-closed transition-geometry obligation is isolated in
`certificates/moduli/finite_moduli_transition_geometry`.  That packet
records the missing object-stack, extension-stack, and two-step
flag-stack transition morphisms, component proper/closed statuses, and
zero transition-defect rows.  It verifies only
`FINITE_MODULI_TRANSITION_GEOMETRY_OBSTRUCTION_VERIFIED`.

The `R^1 lim`-vanishing obligation for retained moduli cohomology is
isolated in `certificates/moduli/moduli_cohomology_lim1_vanishing`.
That packet records the missing coefficient-system rows, cohomology
tower rows, cohomology transition maps, functoriality rows,
image-stabilization witnesses, strict Mittag-Leffler status rows, zero
`R^1 lim` rows, and degreewise coverage rows.  It verifies only
`MODULI_COHOMOLOGY_LIM1_VANISHING_OBSTRUCTION_VERIFIED`.

The HN type-bound obligations are discharged by

```sh
python3 compute/verify_retained_hn_type_bounds_fixture.py \
  --fixture certificates/moduli/retained_hn_type_bounds --check
```

The finite-type semistable-substack obligations are discharged by

```sh
python3 compute/verify_retained_semistable_substacks_fixture.py \
  --fixture certificates/moduli/retained_semistable_substacks --check
```

The quasi-smooth derived-enhancement obligations are discharged by

```sh
python3 compute/verify_retained_derived_enhancements_fixture.py \
  --fixture certificates/moduli/retained_derived_enhancements --check
```

The scalar rigidification and finite residual inertia obligations are
discharged by

```sh
python3 compute/verify_retained_rigidification_inertia_fixture.py \
  --fixture certificates/moduli/retained_rigidification_inertia --check
```

The finite class-bound obligations are discharged by

```sh
python3 compute/verify_retained_class_bounds_fixture.py \
  --fixture certificates/moduli/retained_class_bounds --check
```

The universal perfect-complex obligations are discharged by

```sh
python3 compute/verify_retained_universal_complexes_fixture.py \
  --fixture certificates/moduli/retained_universal_complexes --check
```

The E-translation rigidification obligations are discharged by

```sh
python3 compute/verify_retained_e_translation_rigidifications_fixture.py \
  --fixture certificates/moduli/retained_e_translation_rigidifications --check
```

The retained closed-substack and finite closed-cover obligations are
discharged by

```sh
python3 compute/verify_retained_closed_substacks_fixture.py \
  --fixture certificates/moduli/retained_closed_substacks --check
```

The retained extension-closure obligations are discharged by

```sh
python3 compute/verify_retained_extension_closure_fixture.py \
  --fixture certificates/moduli/retained_extension_closure --check
```

The retained HN-factor-closure obligations are discharged by

```sh
python3 compute/verify_retained_hn_factor_closure_fixture.py \
  --fixture certificates/moduli/retained_hn_factor_closure --check
```

The retained dual-closure obligations are discharged by

```sh
python3 compute/verify_retained_dual_closure_fixture.py \
  --fixture certificates/moduli/retained_dual_closure --check
```

The remaining obstruction ledger is verified by

```sh
python3 compute/verify_moduli_obstruction_ledger.py \
  --fixture certificates/moduli/k3e_finite_moduli --check
```

A positive result is `MODULI_OBSTRUCTION_LEDGER_VERIFIED` with
`moduli_certification: false` and `mathematical_certification: false`.
The verifier also checks that this packet is still blocked after the
bounded HN type, finite-type semistable-substack, and quasi-smooth
derived-enhancement rows, and after scalar rigidification with finite
residual inertia, finite class-bound rows, and universal
perfect-complex rows, after E-translation rigidification rows, after
retained closed-substack rows, and after retained extension-closure and
HN-factor-closure rows, and after retained dual-closure rows; if more
finite-moduli stack rows are supplied later, this ledger must be
retired or narrowed.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, scalar-only, target-only,
charge-window-only, Liu-stability-only, Hilbert-scheme-only,
Pfaffian-only, status-only, todo, or unsupplied provenance is rejected.

The full finite-moduli fixture remains blocked until those rows are
supplied. A schema-complete result is not a proof of finite moduli.
