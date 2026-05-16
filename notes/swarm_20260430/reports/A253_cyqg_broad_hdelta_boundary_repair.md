# A253 CYQG Broad HDelta Boundary Repair

Runtime id: `019ddcdb-25f6-7361-a96a-8f0cb1114203`.

Changed:
- `/Users/raeez/calabi-yau-quantum-groups/AGENTS.md`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_c_six_routes_convergence.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/phi_universal_trace_platonic.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/m3_b2_obstruction.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_waves_11_through_16_healed.tex`.

Repairs:
- Gated `H^2`/`\mathbf H_{\Delta_5}` lines as conditional comparison characteristics.
- Replaced HMS/gauge-class language by conditional Igusa comparison language.
- Added Hall--Borcherds and Heegner gates to six-route convergence claims.
- Corrected `\Phi_{10}` normalization where invoked: `\Phi_{10}^{\mathrm{un}}=\Delta_5^2`, hence `\kappa_{\mathrm{BKM}}(\Phi_{10})=10`.

Checks:
- In `/Users/raeez/calabi-yau-quantum-groups`, `git diff --check -- AGENTS.md chapters/theory/introduction.tex chapters/examples/fukaya_categories.tex chapters/examples/cy_c_six_routes_convergence.tex chapters/theory/phi_universal_trace_platonic.tex chapters/connections/geometric_langlands.tex chapters/theory/m3_b2_obstruction.tex notes/platonic_synthesis_waves_11_through_16_healed.tex` passed in the agent workspace.
- Targeted `rg` found no remaining exact old phrases for classifying invariant, unique gauge class, bare `\mathbf H_{\Delta_5}=\Sp...`, six-route common-image equality, `\kBKM(\Phi_{10})=5`, or `\Phi_{10}\mapsto 5`.

Residual risk:
- Finite Hall--Borcherds recognition and Heegner comparison remain explicit hypotheses.
