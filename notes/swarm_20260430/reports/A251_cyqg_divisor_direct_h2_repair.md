# A251 CYQG Divisor and Direct-H2 Repair

Runtime id: `019ddcd8-4572-76d0-b22f-8e59b8fb60f8`.

Changed:
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex`.

Repairs:
- Separated `\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5` from divisor order.
- Restored divisor normalization: `\operatorname{div}(\Delta_5)=H_1+2H_4`, `\operatorname{ord}_{H_1}(\Delta_5)=1`, `\operatorname{ord}_{H_4}(\Delta_5)=2`.
- Restored `\Phi_{10}^{\mathrm{un}}=\Delta_5^2` divisor normalization: `2H_1+4H_4`.
- Removed false `H_4` order-1 / order-1/2 language except as normalized square-root coordinate explanation.
- Replaced direct `[H_3]\in H^2(\mathfrak g_{\Delta_5},\mathbb Z)` with gated Heegner target-characteristic language.

Checks:
- `git diff --check -- /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex` passed.
- Requested and broader `rg` scans returned no matches for the bad divisor/H2 strings.
- `pytest compute/tests/test_k3e_coha_structure.py` passed with `99 passed`.

Residual risk:
- The `H_4` order-16 obstruction still rests on the stated Kuga-Satake banding lift. A255 was launched for a primary-source verification pass.
