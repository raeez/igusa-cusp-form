# Fifth recognition/PBW attack-heal report

Date: 2026-04-28.

## Claim attacked

The attacked shortcut was:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)
\quad\Longrightarrow\quad
\text{primitive recognition of the compact source}.
\]

This shortcut remains false.  The denominator fixes the imported
Gritsenko--Nikulin/Kac target.  It does not construct compact
parity-homogeneous generators, Hall brackets, Hopf pairing matrices,
closed radical ideal/coideal data, the no-extra-relations kernel theorem,
or completed PBW.

## Repairs

- Added Proposition `prop:first-saturated-primitive-recognition-window`.
  It names the first downward-saturated finite target window
  \(W_{\le3}\), lists the target parity dimensions there, and states the
  finite certificate required before a compact source is recognized in
  that window.
- Strengthened `compute/verify_square_root.py` from a one-off
  \([qrs]\) check to a finite monic \(D_5/(qrs)^{1/2}\) coefficient
  engine.  The script now checks the first timelike split \(29|93\), the
  height-four additive coefficients, and the next point on the
  \(\delta_{123}\)-ray.
- Kept the PBW/no-extra-relations claim conditional.  The new finite
  proposition says explicitly that dimension equality is not recognition
  without finite kernel equality, Hopf-radical ideal/coideal stability,
  and associated-graded PBW isomorphism.

## Target constants

First window:
\[
W_{\le3}=\{\beta=\sum c_i\delta_i\in\mathcal R_+:
c_i\ge0,\ 1\le\sum c_i\le3\}.
\]

Target parity dimensions in \(W_{\le3}\):
\[
\delta_i:1|0,\qquad
\delta_i+\delta_j:10|0,\qquad
2\delta_i+\delta_j:1|0,\qquad
\delta_{123}:29|93.
\]

The first timelike count remains:
\[
[qrs]D_5/(qrs)^{1/2}=93,\qquad
m(\delta_{123})=-93,\qquad
29-93=-64=f(1,1).
\]

New coefficient checks:
\[
[q^2r^2s]D_5/(qrs)^{1/2}
=[qr^2s^2]D_5/(qrs)^{1/2}
=[qs]D_5/(qrs)^{1/2}
=-90,
\]
\[
[q^2r^2s^2]D_5/(qrs)^{1/2}=540.
\]

Thus
\[
m(2\delta_1+\delta_2+\delta_3)
=m(\delta_1+2\delta_2+\delta_3)
=m(\delta_1+\delta_2+2\delta_3)=90,
\]
\[
m(2\delta_{123})=-540.
\]

These are additive simple-root coefficients, not full root-space parity
dimensions and not compact Hall data.

## Surviving obstruction

The exact obstruction to full primitive recognition is unchanged but now
finite-window sharp.  For every saturated finite window \(W\), beginning
with \(W_{\le3}\), the compact source must provide:

- compact simple-root representatives with the GN parity fibres;
- Borcherds--Kac relation checks in the protected Hall bracket;
- positive-negative Hopf-pairing matrices and transition-compatible
  closed radicals;
- equality of the compact radical with the standard GN/Kac radical;
- finite kernel equality
  \(\ker\pi_W=(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}})_W\);
- generation in the window;
- associated-graded PBW isomorphism and strict transition maps.

The determinant, signed root multiplicities, and the new additive
coefficient checks do not prove these statements.

## Commands

Run from `/tmp/igusa-fifth-recognition`:

- `python3 compute/verify_square_root.py`: passed.  It printed
  \(29|93\), \(m(\delta_{123})=-93\), and the next additive checks
  \((1,1,2):90\), \((1,2,1):90\), \((2,1,1):90\),
  \((2,2,2):-540\).
- `python3 -m py_compile compute/verify_square_root.py`: passed.
- `git diff --check -- main.tex compute/verify_square_root.py notes/fifth_recognition_pbw_attack_heal_report.md`:
  passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fifth-recognition-texcheck main.tex`:
  passed.  The single pass reported expected unresolved references and
  citations because it was not a full `make` build.

## Files changed

- `main.tex`
- `compute/verify_square_root.py`
- `notes/fifth_recognition_pbw_attack_heal_report.md`
