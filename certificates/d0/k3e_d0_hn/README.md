# k3e_d0_hn fixture

This directory is a D0-HN degeneration scaffold. It is not a proof of
\((D0)\).

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until a finite D0-HN
packet supplies row-level mathematical payload and geometric provenance
for:

- flat one-parameter D0-degeneration families;
- retained object, extension, mixed, wrapped, and two-step flag
  substacks over the degeneration;
- proper or closed HN transition morphisms and their composition law;
- quasi-smooth derived enhancements, PTVV shifted symplectic forms,
  d-critical truncations, and perfect obstruction theories;
- additive K3 semiregularity cosections, including extension-stack
  additivity;
- reduced vanishing-cycle specialization;
- Joyce-Upmeier orientation specialization;
- Pfaffian-line, protected-integration, compact-support, Hall product,
  and Hall coproduct specialization;
- strict Mittag-Leffler rows;
- scalar-firewall checks excluding Hilbert-scheme scalar specialization
  as an entry of \(D0_{\mathrm{HN}}\).

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records the missing D0-HN rows: flat D0-degeneration families,
D0-sector containment, retained object/extension/mixed/wrapped/two-step
flag substacks, HN transition maps and their composition law,
quasi-smooth derived and d-critical enhancements, K3 semiregularity
cosection surjectivity/additivity, reduced vanishing-cycle
specializations, Joyce-Upmeier orientation specializations, Pfaffian
and protected-integration specializations, strict Mittag-Leffler rows
for all inverse systems, and scalar firewalls.

Transition preservation of reduced vanishing cycles is isolated in
`certificates/vanishing_cycles/transition_vanishing_cycle_preservation`.
That packet records the missing oriented d-critical chart transitions,
potential compatibility, quadratic stabilization, cosection pullback,
reduced obstruction-complex maps, graph-pullback vanishing-cycle
isomorphisms, BBDJS perverse normalization, Thom-Sebastiani
compatibility, base-change compatibility, strict composition, and
vanishing-cycle Mittag-Leffler rows.  It verifies only
`TRANSITION_VANISHING_CYCLE_PRESERVATION_OBSTRUCTION_VERIFIED`.

The `R^1 lim`-vanishing obligation for retained moduli cohomology is
isolated in `certificates/moduli/moduli_cohomology_lim1_vanishing`.
That packet records the missing coefficient-system rows, cohomology
transition maps, image-stabilization witnesses, and zero `R^1 lim`
rows needed before the D0-HN inverse limit can be evaluated on moduli
cohomology.  It verifies only
`MODULI_COHOMOLOGY_LIM1_VANISHING_OBSTRUCTION_VERIFIED`.

Transition preservation of Hall products is isolated in
`certificates/hall/transition_hall_product_preservation`.  That packet
records the missing extension-correspondence transition cube,
coefficient-system transport, Thom-Sebastiani product transport, proper
base change, projection formula, compact-support pushforward,
product-matrix intertwining, associativity-transition, and
Hall-product Mittag-Leffler rows.  It verifies only
`TRANSITION_HALL_PRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED`.

Transition preservation of Hall coproducts is isolated in
`certificates/hall/transition_hall_coproduct_preservation`.  That packet
records the missing splitting-correspondence transition cube,
coefficient-system transport, inverse Thom-Sebastiani coproduct
transport, proper base change, projection formula, compact-support
pushforward, coproduct-matrix intertwining, coassociativity-transition,
counit-transition, and Hall-coproduct Mittag-Leffler rows.  It verifies
only `TRANSITION_HALL_COPRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED`.

Transition preservation of primitive subspaces is isolated in
`certificates/hall/transition_primitive_subspace_preservation`.  That
packet records the missing primitive-kernel and restricted-transition
rows required after Hall-coproduct and counit transition compatibility.
It verifies only
`TRANSITION_PRIMITIVE_SUBSPACE_PRESERVATION_OBSTRUCTION_VERIFIED`.

The D0-HN obstruction ledger is verified by

```sh
python3 compute/verify_d0_obstruction_ledger.py \
  --fixture certificates/d0/k3e_d0_hn --check
```

A positive result is `D0_OBSTRUCTION_LEDGER_VERIFIED` with
`d0_certification: false` and `mathematical_certification: false`.
The verifier also checks that this packet is still the empty blocked
scaffold; if D0-HN rows are supplied later, this ledger must be retired
or narrowed.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, scalar-only, Hilbert-scheme-only,
status-only, todo, or unsupplied provenance is rejected.

All defect ranks, obstruction ranks, specialization-cone ranks,
composition-defect ranks, cosection-cokernel ranks, additivity-defect
ranks, transition-defect ranks, and `R^1 lim` ranks must be zero.
