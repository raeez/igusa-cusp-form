# A243 CYQG Post-Repair Verifier

Runtime id: `019ddcd1-a5cd-73c2-8cef-cf0521a263a4`.

Verdict:
- Not green. No edits made.

Findings:
- `quantum_chiral_algebras.tex` conflated Borcherds weight with Humbert vanishing order by using `ord_{H_1}(\Delta_5)=5`. The correct separation is `\kappa_{\mathrm{BKM}}(\Delta_5)=c_1(0)/2=5`, while `ord_{H_1}(\Delta_5)=1` and `ord_{H_4}(\Delta_5)=2`.
- `quantum_groups_foundations.tex` had an internal `\Phi_{10}/\Delta_5` divisor conflict: after stating `\operatorname{div}(\Phi_{10}^{un})=2H_1+4H_4`, it later gave an `H_4` order inconsistent with that normalization and another line omitted `H_4`.
- `cyclic_ainf.tex` retained an intrinsic `H^2(\mathfrak g_{\Delta_5},\mathbb Z)` line for `c_3=-8[H_3]`, instead of Heegner/target-characteristic comparison language.

Green checks:
- Source-recognition gates were explicit in `k3e_cy3_programme.tex`, `k3_chiral_bialgebra_platonic.tex`, `braided_factorization.tex`, `quantum_chiral_algebras.tex`, and `coha_wall_crossing_platonic.tex`.

Executable checks:
- `PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider compute/tests/test_k3e_coha_structure.py` passed with `99 passed`.
- Coefficient cross-check returned `all_match=True`, `n_checks=66`.

Integration:
- A251 was launched with ownership of the three affected CYQG files.
