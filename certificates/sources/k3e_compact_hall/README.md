# k3e_compact_hall source fixture

This directory is a compact-source fixture scaffold. It is not a compact
Hall source proof.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until a compact source
stage gives provenance for every source basis vector, parity blocks,
simple primitive representatives, the source matrices `M,D,B,G,K,Q,A`,
the Hall unit and counit maps, Hall bialgebra identity checks, radical
ideal/coideal checks, Hopf pairing adjointness and Frobenius checks,
relation rows, no-extra kernel equality, generation span checks, PBW
associated-graded checks, strict transitions/Mittag-Leffler data, the
`A_beta` comparison identities, and the finite Koszul comparison tables
`koszul_cones.csv`, `koszul_comparison_identities.csv`, and
`koszul_transition_ml.csv`.

The file `blocked_obligations.csv` is the companion obstruction ledger.
It records every missing source artifact required by the finite
recognition datum: source degrees, parity blocks, basis provenance,
simple representatives, \(M,D,\eta,\epsilon,B,G,K,Q,A\), the eight Hall
bialgebra identities, the three Hopf-pairing identities, the
radical ideal/coideal identities, the five Borcherds--Kac relation
families, no-extra equality, generation, PBW, strict transition,
the five \(A_\beta\)-intertwining families, and the Koszul cone,
identity, and Mittag--Leffler rows.

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
packet records the missing source and target coproduct matrices, source
and target counit maps, reduced-coproduct matrices, primitive kernel
rows, ambient Hall transition matrices, Hall-coproduct transition input,
counit-transition compatibility, kernel-intertwining rows, primitive
projection matrices, restricted primitive transition matrices, and
primitive-transition composition rows.  It verifies only
`TRANSITION_PRIMITIVE_SUBSPACE_PRESERVATION_OBSTRUCTION_VERIFIED`.

Primitive-space `R^1 lim` vanishing is isolated in
`certificates/hall/primitive_space_lim1_vanishing`.  That packet records
the missing cofinal root-window sequence, primitive-space rows,
primitive bases, finite-rank rows, parity and sign coverage rows,
restricted transition matrices, functoriality rows, image-stabilization
witnesses, Mittag-Leffler rows, and zero `R^1 lim` rows.  It verifies
only `PRIMITIVE_SPACE_LIM1_VANISHING_OBSTRUCTION_VERIFIED`.

Pairing-kernel `R^1 lim` vanishing is isolated in
`certificates/hall/pairing_kernel_lim1_vanishing`.  That packet records
the missing Hopf-pairing matrices, pairing identity rows, left and right
kernel rows, kernel bases, restricted kernel transitions,
image-stabilization witnesses, Mittag-Leffler rows, and zero `R^1 lim`
rows.  It verifies only
`PAIRING_KERNEL_LIM1_VANISHING_OBSTRUCTION_VERIFIED`.

Transition preservation of Hopf radicals is isolated in
`certificates/hall/transition_radical_preservation`.  That packet
records the missing primitive-transition input, source and target
Hopf-pairing matrices, Hopf-pairing identity rows, radical kernels,
opposite-primitive lift rows, pairing-transition identities, restricted
radical transition matrices, quotient splittings, descended quotient
transition matrices, and radical-transition composition rows.  It
verifies only `TRANSITION_RADICAL_PRESERVATION_OBSTRUCTION_VERIFIED`.

Transition preservation of PBW filtrations is isolated in
`certificates/hall/transition_pbw_filtration_preservation`.  That
packet records the missing radical-quotient transition input, source
and target PBW filtration rows, ordered word bases, relation-rewrite
systems, quotient transition matrices, multiplicative word
transitions, filtered-image identities, associated-graded transition
matrices, PBW-symbol identities, `A_beta` PBW transition squares, and
PBW-transition composition rows.  It verifies only
`TRANSITION_PBW_FILTRATION_PRESERVATION_OBSTRUCTION_VERIFIED`.

PBW associated-graded `R^1 lim` vanishing is isolated in
`certificates/hall/pbw_associated_graded_lim1_vanishing`.  That packet
records the missing associated-graded pieces, graded bases,
associated-graded transitions, PBW-symbol rows, `A_beta` PBW squares,
image-stabilization witnesses, Mittag-Leffler rows, and zero `R^1 lim`
rows.  It verifies only
`PBW_ASSOCIATED_GRADED_LIM1_VANISHING_OBSTRUCTION_VERIFIED`.

Transition preservation of parity decompositions is isolated in
`certificates/hall/transition_parity_decomposition_preservation`.
That packet records the missing primitive-transition input, source and
target-stage parity blocks, parity-homogeneous bases, fermion-parity
involutions, ambient transition matrices, parity-commutator identities,
off-diagonal zero identities, restricted even and odd transition
matrices, negative-root parity transport rows, `A_beta` parity
transition squares, and parity-transition composition rows.  It
verifies only
`TRANSITION_PARITY_DECOMPOSITION_PRESERVATION_OBSTRUCTION_VERIFIED`.

The compact Hall obstruction ledger is verified by

```sh
python3 compute/verify_compact_hall_obstruction_ledger.py \
  --source certificates/sources/k3e_compact_hall --check
```

A positive result is `COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED` with
`compact_source_recognition: false` and `mathematical_certification:
false`.  The verifier also checks that the source fixture is still the
empty blocked scaffold; if source rows are later supplied, the
obstruction ledger must be retired or narrowed.

Target labels such as `e_i,E_ij,u_ij_r,T_i,M_ij_r,w_s` are forbidden in
source rows. They may occur only in target reference fixtures or in the
codomain coordinates of `A_entries.csv` and target-matrix references used
by `a_beta_comparison_maps.csv`.

The source verifier may consume a target fixture path. It must not
generate target truth, target parity tables, target PBW ranks, or target
basis templates. The verifier is check-only; `--check` is an explicit
spelling of its default mode and does not permit writes or generated truth.
The target path must be a separate existing target reference directory,
not the source packet itself and not any path inside this source packet.

Future populated packets must supply mathematical payload fields in every
CSV row. Status/comment-only rows do not supply a gate, and `degrees.csv`
passes only rows whose `source_block_status` is `source_verified` or
`source_admissible`.

Every populated row must also carry `geometric_source_id` and
`proof_reference`.  The geometric source is the compact-source
correspondence, stratum, orientation datum, pairing construction,
radical computation, or transition map from which the row is obtained.
The proof reference is the theorem, lemma, equation, computation, or
source certificate that verifies that construction.  Placeholder,
mock, target-only, signed-only, status-only, todo, or unsupplied
provenance is rejected.

Rank rows are checked as identities, not comments. Defect-rank tables
must have `defect_rank=0`; rank-comparison tables such as parity blocks,
radical ideal/coideal, no-extra, generation, and PBW must have the
corresponding source/target/combined ranks equal.

Identity coverage is also checked. Required canonical row types are:
`unit_left,unit_right,counit_left,counit_right,associativity,coassociativity,bialgebra_compatibility,primitive_closure`
in `hall_bialgebra_identities.csv`;
`hopf_adjointness,frobenius_cyclic,quotient_nondegenerate` in
`hopf_pairing_identities.csv`; `lie_ideal,coproduct_coideal` in
`radical_ideal_coideal.csv`;
`cartan,chevalley,real_serre,borcherds_orthogonality,super_sign` in
`relation_rows.csv`; and
`bracket,coproduct,pairing,radical_quotient,pbw` in
`a_beta_comparison_maps.csv`.  The finite Koszul comparison must also
supply `source_bar_cobar_counit,source_to_target_quasi_isomorphism` in
`koszul_cones.csv`;
`weyl_action,pfaffian_orientation,hall_product,hall_coproduct,hopf_pairing,radical_quotient,pbw`
in `koszul_comparison_identities.csv`; and
`source_cone,target_cone,weyl_action,pfaffian_orientation,hall_pairing,radical_quotient,pbw`
in `koszul_transition_ml.csv`.  The cone cohomology ranks, finite
comparison defect ranks, and `R^1 lim` ranks must all be zero.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, target-reference separation, target-label firewall, and
source-degree firewall checks passed. It is not compact-source
certification. The manifest `certified` field is not proof status for this
checker; `compact_source_recognition` and `mathematical_certification`
remain `false`. Schema-only completeness exits fail-closed unless the
caller explicitly passes `--schema-only-ok`; certification and external
verification belong to proof-mode artifacts.
