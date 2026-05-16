# A185 -- E1 / EK Recognition-Gate Patch

## Result

Patched the chiral-bar-cobar \(E_1\) modular Koszul and algebraic
foundations lanes so \(\mathbf H_{\Delta_5}\) inversion and EK
quantization are conditional targets, not unconditional chain-level
theorems from scalar data.

## Changed Paths

- `/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex`

## Anchors

- `e1_modular_koszul.tex:3794`: replaced asserted
  \(\mathbf H_{\Delta_5}\) inversion equivalence with a conditional target
  requiring finite Hall--Borcherds recognition, source datum,
  parity/root fixtures, PBW/no-extra, and comparison maps. The ordered
  averaging warning was kept as a separate valid remark.
- `algebraic_foundations.tex:2880`: fenced EK “unique quantisation”; it now
  states expected/conditional Hall/EK quantization, with gauge uniqueness
  dependent on an exact EK theorem source for the completed
  super-BKM/Hall category.

## Checks

- Targeted `rg` over both files for old unconditional phrases and new
  conditional gates.
- `git diff --check -- chapters/theory/e1_modular_koszul.tex chapters/theory/algebraic_foundations.tex`
  passed.

## Residual Obligation

Prove or cite the finite Hall--Borcherds recognition theorem; fix the K3
Hall source, root/parity/Weyl-vector data, PBW/no-extra theorem, and
comparison maps; and supply a precise EK theorem covering the completed
super-BKM/Hall Lie bialgebra before claiming uniqueness up to gauge.

