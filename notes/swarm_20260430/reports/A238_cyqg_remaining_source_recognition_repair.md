# A238 CYQG Remaining Source-Recognition Repair

Runtime id: `019ddcc7-5541-7010-8b6d-62252990bd2c`.

Changed:
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/coha_wall_crossing_platonic.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex`.
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex`.

Repairs:
- Chamber Hall-Drinfeld comparison now requires finite Hall-Borcherds source-recognition gates.
- Cyclic uniqueness is fibrewise after source recognition; `H^2` is only the target characteristic line.
- Kazhdan limit applies to the `\Delta_5` target; compact `\mathbf H_{\Delta_5}` enters only after gates.
- Direct `\Phi`-producer language was repaired in the owned files.

Checks:
- `git diff --check -- chapters/examples/coha_wall_crossing_platonic.tex chapters/theory/cyclic_ainf.tex chapters/theory/quantum_groups_foundations.tex` passed.
- Targeted `rg -n -F` for `H^2(\mathfrak g_{\Delta_5})`, `\mathbf H_{\Delta_5}`, `\mathfrak g_{\Delta_5}`, `constructed by \Phi`, and `EK uniqueness`.
- Supplementary direct-construction `rg` found no remaining matches for `constructed by \Phi`, `constructed by the CY-to-chiral functor \Phi`, `produced by the CY-to-chiral functor`, or direct `\mathbf H_{\Delta_5}=\Phi` forms.
