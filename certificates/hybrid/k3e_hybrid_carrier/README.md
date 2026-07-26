# k3e_hybrid_carrier fixture

This directory is a finite hybrid local/wrapped carrier scaffold. It is
not a construction of the hybrid source.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until finite HN-window
rows supply mathematical payload and geometric provenance for:

- the hybrid Ran prestack definition, local \(b=0\) subprestack,
  wrapped \(b>0\) subprestack, hybrid-base table rows,
  local/wrapped windows, and additive
  elliptic-degree map, with the degree-map definition separated in
  `certificates/hybrid/geometric_elliptic_degree_map` and the additivity
  criterion separated in
  `certificates/hybrid/geometric_elliptic_degree_additivity`;
- the separation of the geometric support degree from the Borcherds
  trace coordinate, recorded in
  `certificates/hybrid/geometric_borcherds_degree_separation`;
- the positive elliptic-degree projection theorem and its object-level
  support-realization obligations, recorded in
  `certificates/hybrid/positive_elliptic_degree_projection`;
- projection-finite closed configuration incidence stacks with diagonal
  compatibility and support-locality rows; fixed-chart symmetric descent
  is recorded in
  `certificates/hybrid/local_configuration_symmetric_descent`, while
  populated aggregate local-configuration rows remain absent here;
- E-equivariant wrapped prequotient definitions, recorded in
  `certificates/hybrid/equivariant_wrapped_prequotient_definition`,
- finite type for the wrapped prequotients, recorded in
  `certificates/hybrid/wrapped_prequotient_finite_type`,
  while populated aggregate wrapped prequotient rows, final anchors,
  properness, quotient descent, and anchor-loss checks remain absent
  here;
- local/local correspondence definitions, recorded in
  `certificates/hybrid/local_local_correspondence_definition`;
- target properness for local/local extension stacks, recorded in
  `certificates/hybrid/local_local_extension_properness`, while source
  properness is not claimed and aggregate correspondence rows remain
  absent here;
- one-sided mixed local/wrapped correspondence definitions, recorded in
  `certificates/hybrid/mixed_local_wrapped_correspondence_definition`;
- target admissibility for one-sided mixed local/wrapped extension
  stacks, recorded in
  `certificates/hybrid/mixed_local_wrapped_extension_admissibility`,
  while source properness is not claimed and compact-support,
  base-change, projection-formula, Thom-Sebastiani, quotient-descent,
  transition, and aggregate correspondence rows remain absent here;
- wrapped/wrapped correspondence definitions, recorded in
  `certificates/hybrid/wrapped_wrapped_correspondence_definition`;
- target admissibility for wrapped/wrapped extension stacks, recorded
  in `certificates/hybrid/wrapped_wrapped_extension_admissibility`,
  while source properness is not claimed and compact-support,
  symmetric-descent, Thom-Sebastiani, quotient-descent, transition, and
  aggregate correspondence rows remain absent here;
- the compact-support exceptional pushforward model, recorded in
  `certificates/hybrid/compact_support_exceptional_pushforward_model`,
  while map population, choice independence, base-change,
  projection-formula, Thom-Sebastiani, symmetric-descent,
  quotient-descent, transition, associativity, and aggregate rows remain
  absent here;
- base change for one-sided mixed correspondences, recorded in
  `certificates/hybrid/mixed_correspondence_base_change`, while
  Thom-Sebastiani, quotient-descent, transition,
  associativity, and aggregate rows remain absent here;
- projection formula for one-sided mixed correspondences, recorded in
  `certificates/hybrid/mixed_correspondence_projection_formula`, while
  Thom-Sebastiani, quotient-descent, transition,
  associativity, and aggregate rows remain absent here;
- Thom-Sebastiani transport for one-sided mixed correspondences,
  recorded in `certificates/hybrid/mixed_correspondence_thom_sebastiani`,
  while quotient-descent, transition, two-step flag associativity, and
  aggregate rows remain absent here;
- the eight-word binary vocabulary, recorded in
  `certificates/hybrid/eight_word_binary_vocabulary`, while the
  actual two-step flag stacks, associativity, pentagon, transition, and
  aggregate rows remain absent here;
- the eight-word two-step flag-stack construction, recorded in
  `certificates/hybrid/eight_word_two_step_flag_stacks`, while
  associativity, pentagon, quotient-descent, transition, and aggregate
  rows remain absent here;
- `LLL` associativity, recorded in
  `certificates/hybrid/lll_associativity`, while `LLW`, `LWL`, `WLL`,
  `LWW`, `WLW`, `WWL`, `WWW`, pentagon, quotient-descent, transition,
  and aggregate rows remain absent here;
- `LLW` associativity, recorded in
  `certificates/hybrid/llw_associativity`, while `LWL`, `WLL`, `LWW`,
  `WLW`, `WWL`, `WWW`, pentagon, quotient-descent, transition, and
  aggregate rows remain absent here;
- `LWL` associativity, recorded in
  `certificates/hybrid/lwl_associativity`, while `WLL`, `LWW`, `WLW`,
  `WWL`, `WWW`, pentagon, quotient-descent, transition, and aggregate
  rows remain absent here;
- `WLL` associativity, recorded in
  `certificates/hybrid/wll_associativity`, while `LWW`, `WLW`, `WWL`,
  `WWW`, pentagon, quotient-descent, transition, and aggregate rows
  remain absent here;
- `LWW` associativity, recorded in
  `certificates/hybrid/lww_associativity`, while `WLW`, `WWL`, `WWW`,
  pentagon, quotient-descent, transition, and aggregate rows remain
  absent here;
- `WLW` associativity, recorded in
  `certificates/hybrid/wlw_associativity`, while `WWL`, `WWW`,
  pentagon, quotient-descent, transition, and aggregate rows remain
  absent here;
- `WWL` associativity, recorded in
  `certificates/hybrid/wwl_associativity`, while `WWW`, pentagon,
  quotient-descent, transition, and aggregate rows remain absent here;
- `WWW` associativity, recorded in
  `certificates/hybrid/www_associativity`, while pentagon,
  quotient-descent, transition, and aggregate rows remain absent here;
- four-input pentagon coherence, recorded in
  `certificates/hybrid/four_input_pentagon_coherence`, while
  higher-coloured tree data, units, quotient-descent, transition, and
  aggregate rows remain absent here;
- the higher-coloured tree category definition, recorded in
  `certificates/hybrid/higher_coloured_tree_category_definition`,
  while residual vanishing, units, quotient-descent, transition, and
  aggregate rows remain absent here;
- the higher-coloured residual vanishing criterion, recorded in
  `certificates/hybrid/higher_coloured_residual_vanishing_criterion`,
  while unit, symmetric, refinement, descent, overlap,
  quotient-descent, transition, and aggregate rows remain absent here;
- the hybrid unit object and split vacuum correspondences, recorded in
  `certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences`,
  while unit identity laws, quotient-descent, transition, and
  aggregate rows are not populated in this aggregate packet;
- local unit compatibility, recorded in
  `certificates/hybrid/local_unit_compatibility`, while
  quotient-descent, transition, and aggregate rows remain absent here;
- wrapped unit compatibility, recorded in
  `certificates/hybrid/wrapped_unit_compatibility`, while
  quotient-descent, transition, and aggregate rows remain absent here;
- local configuration symmetric descent, recorded in
  `certificates/hybrid/local_configuration_symmetric_descent`, while
  collision compatibility, closed-chart refinement, ordered-chart
  descent, quotient-descent, transition, and aggregate rows remain
  absent here;
- wrapped insertion order conventions, recorded in
  `certificates/hybrid/wrapped_insertion_order_conventions`, while
  unordered wrapped-pair symmetric descent, ordered-chart descent,
  overlap compatibility, quotient-descent, transition, and aggregate
  rows remain absent here;
- ordered two-sided mixed correspondence definitions, recorded in
  `certificates/hybrid/two_sided_mixed_correspondence_definition`;
- source/target anchor-memory definitions before quotient, recorded in
  `certificates/hybrid/source_target_anchor_memory_definition`;
- determinant-anchor construction, recorded in
  `certificates/hybrid/determinant_anchor_construction`;
- determinant-anchor translation weight, recorded in
  `certificates/hybrid/determinant_anchor_translation_weight`;
- determinant-anchor chi-zero degeneracy, recorded in
  `certificates/hybrid/determinant_anchor_chi_zero_degeneracy`;
- determinant-anchor extra-anchor data, recorded in
  `certificates/hybrid/determinant_anchor_extra_anchor_data`;
- anchor-residual definition, recorded in
  `certificates/hybrid/anchor_residual_definition`;
- first-window anchor-residual obstruction, recorded in
  `certificates/hybrid/anchor_residual_first_window_obstruction`;
- quotient-after-correspondence pseudofunctor definition, recorded in
  `certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition`,
  and quotient-after-correspondence composition preservation, recorded
  in `certificates/hybrid/quotient_after_correspondence_composition`,
  and quotient-after-correspondence base-change square preservation,
  recorded in
  `certificates/hybrid/quotient_after_correspondence_base_change`,
  and quotient-after-correspondence Thom-Sebastiani descent, recorded
  in
  `certificates/hybrid/quotient_after_correspondence_thom_sebastiani`,
  and quotient-first exclusion, recorded in
  `certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion`,
  and the Borel-Moore chain functor, recorded in
  `certificates/hybrid/quotient_after_correspondence_bm_chain_functor`,
  and the theta comparison maps, recorded in
  `certificates/hybrid/quotient_after_correspondence_theta_mu_comparison`,
  and the theta associativity compatibility, recorded in
  `certificates/hybrid/quotient_after_correspondence_theta_mu_associativity`,
  and the theta coproduct compatibility, recorded in
  `certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct`,
  and the theta primitive-projection compatibility, recorded in
  `certificates/hybrid/quotient_after_correspondence_theta_mu_primitives`,
  and the HN transition compatibility of \(Q_{E,R}\), recorded in
  `certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`,
  and the definition of protected integration, recorded in
  `certificates/hybrid/protected_integration_definition`,
  and protected-integration product compatibility, recorded in
  `certificates/hybrid/protected_integration_product_compatibility`,
  and protected-integration coproduct compatibility, recorded in
  `certificates/hybrid/protected_integration_coproduct_compatibility`,
  and protected-integration primitive-projection compatibility, recorded
  in `certificates/hybrid/protected_integration_primitive_compatibility`,
  and protected-integration Gram degree, recorded in
  `certificates/hybrid/protected_integration_gram_degree`,
  and protected-integration Pi_X separation, recorded in
  `certificates/hybrid/protected_integration_pi_x_separation`, while
  compact-support pushforward base-change, protected-integration
  transition compatibility,
  product/coproduct/primitive transition preservation, and aggregate
  quotient rows remain absent here;
- aggregate local-local, one-sided mixed, wrapped-wrapped, and
  two-sided mixed correspondence rows with the remaining properness,
  Thom-Sebastiani, and pull-push admissibility data;
- populated source/target anchor-memory rows on those finite
  correspondence stacks;
- populated determinant-anchor rows on finite wrapped prequotients;
- populated determinant-anchor translation-weight rows on finite wrapped
  prequotients;
- populated determinant-anchor chi-zero degeneracy rows on finite wrapped
  prequotients;
- populated determinant-anchor extra-anchor-data rows on finite wrapped
  prequotients;
- populated anchor-residual vanishing rows on finite wrapped
  prequotients;
- first-window anchor-residual vanishing theorem rows;
- populated aggregate rows for the eight-word two-step flag-stack
  atlas for `LLL`, `LLW`, `LWL`, `WLL`, `LWW`, `WLW`, `WWL`, `WWW`,
  with associativity, pentagon, and anchor retention defects zero;
- higher-coloured coherences for units, symmetries, refinements, and
  overlaps;
- quotient-after-correspondence pseudofunctor rows, not quotient-first
  Hall products;
- protected integration Gram degree in
  `certificates/hybrid/protected_integration_gram_degree`;
- protected integration Pi_X separation in
  `certificates/hybrid/protected_integration_pi_x_separation`;
- protected integration compatibility rows for transitions;
- strict transition and Mittag-Leffler rows with `R^1 lim` rank zero;
- scalar-firewall checks excluding ordinary Ran locality, Fock traces,
  determinant anchors alone, quotient-first products, Borcherds
  `s`-degree alone, and scalar Pfaffian products as hybrid-carrier data.

Every populated row must carry `geometric_source_id` and
`proof_reference`. Placeholder, mock, ordinary-Ran-only,
quotient-first, determinant-only, Fock-only, trace-only, scalar-only,
status-only, todo, or unsupplied provenance is rejected.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, correspondence coverage, flag-word coverage, defect,
ML, and scalar-firewall checks passed. It is not a proof of the hybrid
carrier.
