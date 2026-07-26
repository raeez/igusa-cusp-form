# Active Root-Window Exhaustion Certificate

This packet records the target-side exhaustion statement for the active
height windows:

```text
union_nu W_nu_active = R_plus.
```

Here `W_nu_active = W_nu`, where `W_nu` is the height window supplied by
`certificates/lattice/downward_root_windows`.  The proof is the height
witness:

```text
beta in R_plus -> beta in W_ht(beta).
```

The sample table checks the low active target rows used in the
denominator chapter, including the inverse formula
`gamma_beta=(b1,b1+b2-b3,b2)` and the type-II product-chamber sector.

This packet is not the compact-source support exhaustion of
Optimization row 184.  It does not construct compact support, moduli
transitions, orientation transport, vanishing-cycle transport, Hall
operations, radicals, PBW filtrations, or protected traces.

Run:

```sh
python3 compute/verify_active_root_window_exhaustion_fixture.py \
  --fixture certificates/lattice/active_root_window_exhaustion --check
```

Expected status:

```text
ACTIVE_ROOT_WINDOW_EXHAUSTION_VERIFIED
```
