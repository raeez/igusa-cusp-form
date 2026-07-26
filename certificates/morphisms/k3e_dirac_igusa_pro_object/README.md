# k3e_dirac_igusa_pro_object morphism fixture

This directory is a finite-stage Dirac-Igusa morphism scaffold. It is
not a proof that the Dirac-Igusa inverse system exists as a pro-object.

The packet is intentionally `mock_empty_blocked`. Its core pro-object
CSV files contain headers only. The verifier must return `BLOCKED`
until finite HN-window rows supply mathematical payload and geometric
provenance for:

- a directed cofinal HN subsystem with zero identity and composition
  defects;
- finite-stage object rows for all fourteen components
  `A_E3`, `F_hyb`, `Gamma`, `Pi`, `Phi`, `o`, `H`, `P_Pi`, `C`,
  `Theta_Kos`, `L_Pf`, `pf`, `epsilon_o`, and `Rec`;
- strict transition morphisms between finite stages;
- component maps for each clause `M1` through `M8`, with zero
  compatibility, kernel, and cokernel ranks;
- the `M5` Hall bialgebra component map must include product,
  coproduct, counit, and primitive-subspace transition data; the
  primitive part is isolated in
  `certificates/hall/transition_primitive_subspace_preservation`, and
  the radical quotient part is isolated in
  `certificates/hall/transition_radical_preservation`;
- the `M8` primitive-recognition component map must include PBW
  filtered transition data; the PBW part is isolated in
  `certificates/hall/transition_pbw_filtration_preservation`;
- the `M8` primitive-recognition component map must also include
  parity-preserving transition data; the parity part is isolated in
  `certificates/hall/transition_parity_decomposition_preservation`;
- composition laws
  `rho_{R'R''} rho_{RR'} = rho_{RR''}` with zero defect;
- strict Mittag-Leffler rows with `R^1 lim` rank zero for every
  component tower;
- the moduli-cohomology part of the `M2` tower is isolated in
  `certificates/moduli/moduli_cohomology_lim1_vanishing`;
- the primitive-space part of the `M5`/`M8` towers is isolated in
  `certificates/hall/primitive_space_lim1_vanishing`;
- the pairing-kernel part of the `M5`/`M8` towers is isolated in
  `certificates/hall/pairing_kernel_lim1_vanishing`;
- the PBW associated-graded part of the `M8` tower is isolated in
  `certificates/hall/pbw_associated_graded_lim1_vanishing`;
- pro-isomorphism rows over a common cofinal subsystem with commuting
  finite-stage isomorphisms and two-sided inverse defects zero;
- scalar-firewall checks excluding scalar Pfaffian products,
  denominator products, squared determinants, signed exponent tables,
  and protected traces as transition or pro-isomorphism data.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, scalar-only, product-only,
Pfaffian-only, denominator-only, trace-only, signed-only, target-only,
status-only, todo, or unsupplied provenance is rejected.

The file `blocked_obligations.csv` is the morphism/pro-object
obstruction ledger.  It records the missing finite HN cofinal system,
fourteen stage components, strict transition morphisms, component maps
for `M1` through `M8`, transition composition laws,
Mittag-Leffler exactness rows, and pro-isomorphism rows.  Run:

```bash
python3 compute/verify_morphism_obstruction_ledger.py \
  --fixture certificates/morphisms/k3e_dirac_igusa_pro_object --check
```

A positive result is `MORPHISM_OBSTRUCTION_LEDGER_VERIFIED` with
`pro_object_certification: false` and
`mathematical_certification: false`.  It verifies that the missing
finite morphism data are recorded while the packet remains
`mock_empty_blocked`.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, component coverage, clause coverage, defect, ML, and
scalar-firewall checks passed. It is not a proof of the pro-object.
