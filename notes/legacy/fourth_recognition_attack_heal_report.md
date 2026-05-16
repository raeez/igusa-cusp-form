# Fourth primitive recognition attack-heal report

Date: 2026-04-28.

## Stable core

The primitive-recognition lane is stable only as a conditional
presentation-level recognition theorem.  The target algebra
\(\mathfrak g_{\Delta_5}\) is the imported
Gritsenko--Nikulin/Kac Borcherds--Cartan superdatum with real generators,
imaginary simple-root parity fibres, Borcherds--Kac relations, invariant
pairing, standard radical quotient, and completed PBW.  A compact
\(K3\times E\) source enters the stable core only after it supplies the
same data: primitive representatives, parities, real and isotropic
relations, complementary real-string relations, Hopf pairing, closed
radical ideal/coideal, no-extra-relations, generation, completed PBW, and
full parity dimensions.

The first timelike target channel is now checked as
\[
\delta_{123}=\delta_1+\delta_2+\delta_3,\qquad
\rootmult_{\overline0}(\delta_{123})=29,\qquad
\rootmult_{\overline1}(\delta_{123})=93.
\]
This is a target presentation count, not a compact Hall computation and
not an inference from the signed exponent alone.

## Attacks

- `A4-H06-01`: signed multiplicity shortcut.  The shortcut
  \(\smult(\delta_{123})=-64\Rightarrow 29|93\) is false.  The signed
  exponent gives only a difference.  The repair keeps the split tied to
  the GN/Kac presentation and the finite coefficient \(m(\delta_{123})\).
- `A4-H06-02`: compact-source overclaim.  The target words
  \(T_a\) and \([e_k,u_{ij,r}]\) were easy to misread as compact Hall
  words.  The manuscript now calls them Borcherds--Kac presentation
  words at the target level.
- `A4-H06-03`: coefficient opacity.  The script previously asserted the
  \(93\) coefficient but did not expose the finite Laurent calculation
  used by the proof.  The repair prints and asserts the Laurent
  polynomial \(A(B^2+C)\).
- `A4-H06-04`: PBW/no-extra-relations residual.  No compact proof of
  no-extra-relations or completed PBW exists.  This remains a stated
  hypothesis/residual in Theorem `thm:primitive-recognition`, not a
  consequence of the determinant.

## Repairs

- `main.tex`: in Proposition `prop:delta123-presentation-count`, replaced
  "Hall words" by "Borcherds--Kac presentation words" for the two
  real-real-real target directions.
- `main.tex`: inserted the finite Laurent calculation
  \[
  A(r)=1-r^{-1},\quad B(r)=-(r^{-1}+10+r),
  \]
  \[
  C(r)=-10r^{-2}+64r^{-1}-108+64r-10r^2,
  \]
  with
  \[
  A(B^2+C)=9r^{-3}-93r^{-2}+90r^{-1}-90+93r-9r^2,
  \]
  so \([r]A(B^2+C)=93\).
- `compute/verify_square_root.py`: added exact Laurent-polynomial
  helpers, a first-timelike coefficient check, a Witt multidegree
  dimension check for the \(2\) real-real-real words, and an asserted
  target presentation split \(29|93\).

## Computed constants

Command output from `python3 compute/verify_square_root.py`:

```text
phi_{0,1} coefficients through q^2:
q^0: [(-1, Fraction(1, 1)), (0, Fraction(10, 1)), (1, Fraction(1, 1))]
q^1: [(-2, Fraction(10, 1)), (-1, Fraction(-64, 1)), (0, Fraction(108, 1)), (1, Fraction(-64, 1)), (2, Fraction(10, 1))]
q^2: [(-3, Fraction(1, 1)), (-2, Fraction(108, 1)), (-1, Fraction(-513, 1)), (0, Fraction(808, 1)), (1, Fraction(-513, 1)), (2, Fraction(108, 1)), (3, Fraction(1, 1))]
prod_{k>=1}(1-q^k)^9 through q^9:
[1, -9, 27, -12, -90, 135, 54, -99, -189, -85]
[q*r*s] 64^{-1} Delta_5 / (q*r*s)^{1/2}:
93
first timelike Laurent check A*(B^2+C):
[(-3, 9), (-2, -93), (-1, 90), (0, -90), (1, 93), (2, -9)]
first timelike target presentation split even|odd:
29|93
m(delta_1+delta_2+delta_3):
-93
```

Thus
\[
f(1,1)=-64,\qquad [qrs]D_5/(qrs)^{1/2}=93,\qquad
m(\delta_{123})=-93,
\]
and the presentation split checks as
\[
2+3\cdot9=29,\qquad 93,\qquad 29-93=-64.
\]

## Commands

- `sed -n` reads of `AGENTS.md`, `CLAUDE.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`,
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`, the attack-heal skill, and
  the shared protocol.
- `rg` and `nl -ba` reads of the denominator algebra, primitive
  recognition theorem, low-degree tests, first timelike proposition, and
  coefficient script.
- `python3 compute/verify_square_root.py`: passed with the constants
  displayed above.
- `python3 -m py_compile compute/verify_square_root.py`: passed.
- `git diff --check -- main.tex compute/verify_square_root.py`: passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fourth-recognition-texcheck main.tex`:
  passed.  The single pass produced expected unresolved reference and
  citation warnings because it was not a full `make` build.
- `git diff --check`: passed.
- `git add main.tex compute/verify_square_root.py notes/fourth_recognition_attack_heal_report.md`.
- `git diff --cached --check`: passed.
- `git diff --cached --name-only`: staged exactly the three owned paths.

## Residual obligations

- Construct compact parity-homogeneous bases in degree \((1,1,1)\) with
  \(29\) even and \(93\) odd vectors after the closed Hopf-radical
  quotient.
- Compute compact Hall constants for \([e_k^X,u^X_{ij,r}]\), verify
  \(T_1^X+T_2^X+T_3^X=0\), the complementary real-string relations, and
  the positive-negative Hopf pairing matrices.
- Prove compact no-extra-relations, generation, completed PBW, and
  equality of the source Hopf radical with the standard GN/Kac radical.

## Files changed and staged

- `main.tex`
- `compute/verify_square_root.py`
- `notes/fourth_recognition_attack_heal_report.md`

No other paths are owned by H06.
