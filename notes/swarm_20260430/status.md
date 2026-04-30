# 2026-04-30 swarm status

Concurrency rule: six live agents maximum. The main thread is
integration owner. Agents are read-only/proposal-only unless later
assigned an isolated worktree.

## Live Agents

| Agent | Runtime id | Nickname | Scope | Status |
|---|---|---|---|---|
| A115 | `019ddc40-2cbc-7b53-9383-5655fddc7995` | Gauss the 2nd | Post-proof Igusa build verifier | live |
| A116 | `019ddc42-abc2-7ba0-9929-07babd443587` | Kuhn the 2nd | CYQG BKM signed-coefficient dimension patch | live |
| A117 | `019ddc42-b4e8-79f3-9a0b-772908683eeb` | Hubble the 2nd | CYQG `cy_to_chiral` recognition-gate patch | live |
| A118 | `019ddc42-bdcb-7c20-8e89-d2a3076e4036` | Laplace the 2nd | CYQG lattice automorphic coefficient firewall patch | live |
| A119 | `019ddc42-c6bd-7a90-acbf-2812d826a9f5` | Pauli the 2nd | CYQG BPS Hall--Borcherds criterion patch | live |
| A120 | `019ddc42-d054-79c2-8cd7-bff6d3e14c77` | McClintock the 2nd | CYQG unifying Borcherds positive-half gate patch | live |

## Completed Agents

Reports A001-A083 are archived under `notes/swarm_20260430/reports/`.
The latest completed files are:

| Agent | Report |
|---|---|
| A071 | `notes/swarm_20260430/reports/A071_wle7_relation_closed_window_design.md` |
| A072 | `notes/swarm_20260430/reports/A072_source_fixture_verifier_spec.md` |
| A073 | `notes/swarm_20260430/reports/A073_main_tex_recognition_patch_plan.md` |
| A074 | `notes/swarm_20260430/reports/A074_vol3_primitive_recognition_consistency.md` |
| A075 | `notes/swarm_20260430/reports/A075_source_fixture_theorem_proof_skeleton.md` |
| A076 | `notes/swarm_20260430/reports/A076_certificate_repo_integration_plan.md` |
| A081 | `notes/swarm_20260430/reports/A081_schema_to_manuscript_integration.md` |
| A077 | `notes/swarm_20260430/reports/A077_citation_patch_verification.md` |
| A078 | `notes/swarm_20260430/reports/A078_recognition_theorem_latex_drafts.md` |
| A079 | `notes/swarm_20260430/reports/A079_vol3_coefficient_projection_patch_plan.md` |
| A080 | `notes/swarm_20260430/reports/A080_a071_target_fixture_arithmetic_design.md` |
| A084 | `notes/swarm_20260430/reports/A084_vol3_coefficient_projection_patch_text.md` |
| A085 | `notes/swarm_20260430/reports/A085_relation_closed_window_status_table.md` |
| A082 | `notes/swarm_20260430/reports/A082_primitive_recognition_proof_ledger_text.md` |
| A083 | `notes/swarm_20260430/reports/A083_citation_patch_followup_verification.md` |
| A086 | `notes/swarm_20260430/reports/A086_source_fixture_verifier_pseudocode.md` |
| A087 | `notes/swarm_20260430/reports/A087_compact_source_provenance_gate.md` |
| A088 | `notes/swarm_20260430/reports/A088_recognition_section_build_risk_audit.md` |
| A089 | `notes/swarm_20260430/reports/A089_primitive_recognition_proof_ledger.md` |
| A090 | `notes/swarm_20260430/reports/A090_vol3_patch_ranges_and_text.md` |
| A091 | `notes/swarm_20260430/reports/A091_relation_window_parity_target_audit.md` |
| A092 | `notes/swarm_20260430/reports/A092_certificate_verifier_integration_design.md` |
| A093 | `notes/swarm_20260430/reports/A093_compact_source_provenance_integration_audit.md` |
| A094 | `notes/swarm_20260430/reports/A094_recognition_post_edit_verifier_checklist.md` |
| A095 | `notes/swarm_20260430/reports/A095_session_end_build_bibliography_audit.md` |
| A096 | `notes/swarm_20260430/reports/A096_vol3_patch_verifier_checklist.md` |
| A097 | `notes/swarm_20260430/reports/A097_target_presentation_computation_spec.md` |
| A098 | `notes/swarm_20260430/reports/A098_weyl_root_string_affine_citations.md` |
| A099 | `notes/swarm_20260430/reports/A099_recognition_patch_verifier.md` |
| A100 | `notes/swarm_20260430/reports/A100_certificate_verifier_worker_scope.md` |
| A101 | `notes/swarm_20260430/reports/A101_vol3_patch_safety_report.md` |
| A102 | `notes/swarm_20260430/reports/A102_recognition_patch_static_verifier.md` |
| A103 | `notes/swarm_20260430/reports/A103_vol3_coefficient_recognition_patch.md` |
| A104 | `notes/swarm_20260430/reports/A104_recognition_criterion_a_map_audit.md` |
| A105 | `notes/swarm_20260430/reports/A105_a071_target_presentation_theorem_draft.md` |
| A106 | `notes/swarm_20260430/reports/A106_post_patch_static_build_verifier.md` |
| A107 | `notes/swarm_20260430/reports/A107_vol3_modular_trace_dependency_patch.md` |
| A108 | `notes/swarm_20260430/reports/A108_a_map_criterion_post_patch_verifier.md` |
| A109 | `notes/swarm_20260430/reports/A109_cyqg_cache_propagation_audit.md` |
| A110 | `notes/swarm_20260430/reports/A110_vol3_modular_trace_verifier.md` |
| A111 | `notes/swarm_20260430/reports/A111_target_presentation_reducer_scope.md` |
| A112 | `notes/swarm_20260430/reports/A112_global_theorem_strength_audit.md` |
| A113 | `notes/swarm_20260430/reports/A113_provenance_gate_proof_verifier.md` |
| A114 | `notes/swarm_20260430/reports/A114_cyqg_cross_file_recognition_audit.md` |

## Queued Next

| Agent | Scope |
|---|---|
| A095 | Session-end build and bibliography audit |
| A096 | Vol III patch verifier after master-thread edit |
| A097 | Target parity computation lane after A091 |
| A104 | Certificate verifier implementation worker |
| A121 | Igusa Pfaffian-lane wording patch |
| A122 | CYQG programme chapter Stage-2 / motivic recognition patch |
| A123 | Target presentation reducer implementation worker |
| A124 | Source verifier schema implementation worker |
| A125 | Cross-repo post-patch recognition audit |

## Master-Thread Rule

When one live agent returns, mark it complete, archive the report under
`notes/swarm_20260430/reports/`, and launch the next queued agent before
doing broad synthesis. Reports are evidence, not authority.

## Supremum Discipline

The integration target is not demotion. When an attacked statement is too
strong for the current proof, first reconstruct the strongest true
version: add the missing mathematical objects, hypotheses, source
fixtures, computations, or citations needed to make the theorem honest.
Only mark a statement conditional as a temporary proof-status ledger
until the stronger theorem is actually supplied or the precise obstruction
is proved.
