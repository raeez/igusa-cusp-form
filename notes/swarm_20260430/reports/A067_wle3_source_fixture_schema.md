# A067 - W_{\le3} Source Fixture Schema

Using `chriss-ginzburg-rectify` discipline. Proposal only. No files
edited by the agent.

## Status

The fixture is not a proof of the `W_{\le3}` source theorem. It is the
minimum machine-checkable certificate schema that would make the
conditional criterion in `main.tex` near line 15268 executable.
A056-A062 all force the same firewall: target labels and target
arithmetic are admissible only as codomain/reference data, never as
source bases.

## Proposed Packet

`certificates/wle3/<certificate_id>/`

`manifest.yaml`

Fields: `certificate_id`, `schema_version`, `stage_R`, `window=W_le3`,
`degree_set=W_le3 union -W_le3 union {0}`, `coefficient_domain`,
`exact_scalar_encoding`, `super_sign_convention`,
`ordinary_flip_convention`, `target_fixture_id`,
`source_target_firewall=true`, `all_hashes`, `status`.

`degrees.csv`

Fields: `degree_id`, `sign`, `c1,c2,c3`, `height`, `is_zero`,
`target_even_dim`, `target_odd_dim`, `source_raw_even_dim`,
`source_raw_odd_dim`, `K_even_dim`, `K_odd_dim`, `L_even_dim`,
`L_odd_dim`, `retained_by_R`, `status`.

`basis_provenance.csv`

Fields: `basis_id`, `stage_R`, `degree_id`, `parity`, `raw_index`,
`neutral_source_name`, `charge_lift_id`, `Pi_bar_value`, `stack_id`,
`stratum_or_cycle_id`, `IC_or_vanishing_cycle_id`,
`cohomological_degree`, `orientation_line_id`,
`orientation_trivialization_id`, `TS_transport_id`, `stabilizer_id`,
`quotient_orientation_id`, `protected_integration_id`, `dual_basis_id`,
`K_or_L_status`, `transition_status`, `source_reference`.

Target names `e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s` are forbidden here.
They may appear only in `target_basis.csv` and `A_entries.csv`.

`pairs.csv`, `decompositions.csv`

Fields: `pair_or_dec_id`, `stage_R`, `alpha`, `beta`, `rho`, `mu`,
`nu`, `ordered=true`, `output_degree`, `retained`,
`killed_by_height_R`, `coverage_scope=in_window|deferred_height4|deferred_height7`,
`reason`.

`matrix_index.csv`

Fields: `matrix_id`, `type=M|D|B|G|K|Q|A|T`, `stage_R`,
`domain_degree_ids`, `codomain_degree_id`, `parity_block`,
`domain_basis_order`, `codomain_basis_order`, `shape`, `entry_file`,
`derived_from`, `check_status`.

Sparse entry tables:

`M_entries.csv`: `matrix_id,left_basis_id,right_basis_id,out_basis_id,value,correspondence_id,protected_integration_id`.

`D_entries.csv`: `matrix_id,source_basis_id,left_basis_id,right_basis_id,value,correspondence_id`.

`B_entries.csv`: same tensor fields as `M`, plus `computed_from_M=true`;
must satisfy `B=M-(-1)^{|x||y|}M\tau`.

`G_entries.csv`: `matrix_id,pos_basis_id,neg_basis_id,value,pairing_correspondence_id,trace_id`.

`K_entries.csv`: `matrix_id,kernel_vector_id,raw_basis_id,value`;
inclusion matrix for `K=\ker G\cap\ker G_-^t`.

`Q_entries.csv`: `matrix_id,raw_basis_id,L_basis_id,value`.

`A_entries.csv`: `matrix_id,L_basis_id,target_basis_id,target_label,value`;
target labels allowed only here.

`relation_rows.csv`

Fields: `relation_id`,
`type=Chevalley|real_Serre|orthogonality|super_sign|Jacobi|real_string|mixed_27`,
`stage_R`, `input_basis_ids`, `word_degree`, `output_degree`,
`coverage_scope`, `matrix_expression_id`, `expected_result`,
`residual_vector_file`, `Q_applied`, `A_applied`,
`zero_or_target_status`.

For `W_{\le3}`, terminal real-Serre and complementary real-string rows
whose outputs lie beyond the window must be marked `deferred_*`, not
counted as certified.

`pbw.csv`

Fields: `pbw_gen_id`, `L_basis_id`, `degree_id`, `parity`, `pbw_order`,
`word_id`, `filtration_degree`, `normal_form_vector`, `target_word_id`,
`gr_map_matrix_id`, `source_gr_dim`, `target_gr_dim`, `rank`,
`is_isomorphism`, `transition_strict_check_id`.

`no_extra.csv`

Fields: `window`, `free_lie_word_basis_id`, `pi_matrix_id`,
`BK_relation_span_matrix_id`, `GN_radical_span_matrix_id`,
`kernel_pi_matrix_id`, `rank_kernel`, `rank_relation_radical_span`,
`rank_combined`, `kernel_equality_status`,
`transition_compatibility_status`.

`transitions.csv`, `ml_stable_images.csv`

Fields: `transition_id`,
`tower=P|C|U|radical|PBW|kernel|cokernel|cone`, `from_R`, `to_R`,
`degree_id`, `parity`, `matrix_id`, `preserves_MDB_GKQA`,
`preserves_PBW_strictly`, `preserves_orientation`, `cocycle_check`,
`stable_image_mu0`, `rank_mu`, `rank_mu0`,
`block_rank_strictness_status`.

`orientation_protected.csv`

Fields: `orientation_id`, `stage_R`, `stack_or_correspondence_id`,
`orientation_line`, `square_root_line`, `gerbe_class`, `trivialization`,
`finite_stabilizer_character`, `E_quotient_class`,
`Thom_Sebastiani_transport`, `wall_chart_id`, `pfaffian_unit_id`,
`protected_integration_id`, `proper_or_exceptional_support`,
`six_functor_admissibility`, `trace_degree_m_R`,
`transition_trivialization`, `status`.

## Where main.tex Consumes It

- Source bases, `M,D,G,K,Q`, PBW: `main.tex` near line 13836.
- Comparison maps `A_{\beta,\bar p}`: `main.tex` near line 14012.
- `W_{\le3}`, `29|93`, target templates, source obligations:
  `main.tex` near line 15004.
- Executable finite source criterion: `main.tex` near line 15268.
- NO7 radical/coideal protocol: `main.tex` near line 15373, with
  earlier matrix form near line 9581.
- No-extra/PBW/global recognition: `main.tex` near lines 12488 and
  12848.
- ML transitions: `main.tex` near lines 11114 and 11145.
- Protected integration/orientation package in finite realization datum:
  `main.tex` near line 14445.

## Residual Obligations

Populate the fixture from compact `K3 x E` source data. Verify exact
`QB`, `QD`, Hopf adjointness, quotient tensor nondegeneracy,
`A`-intertwining, no-extra kernel equality, PBW associated-graded
isomorphism, strict transitions, and finite-slice ML ranks.

