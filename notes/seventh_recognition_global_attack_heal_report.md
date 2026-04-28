# Seventh primitive recognition global attack-heal report

Date: 2026-04-28.

## Claim attacked

The attacked shortcut was:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)
\quad\Longrightarrow\quad
\text{global compact primitive recognition}.
\]

The attack succeeds.  The Borcherds--Gritsenko--Nikulin denominator data
fix the imported target presentation and signed supermultiplicities.  They
do not construct compact source representatives, relation constants,
positive-negative Hopf pairing matrices, closed radical kernels, the
no-extra-relations theorem, or completed PBW.

## Attacks adjudicated

- `S7-A1` valid: signed dimensions and determinant data do not determine
  compact parity dimensions or invisible even-odd cancelling summands.
- `S7-A2` valid: target Borcherds--Kac relations do not prove the compact
  Hall bracket satisfies the same Chevalley, Serre, orthogonality, and
  super sign relations.
- `S7-A3` valid: a closed Hopf radical cannot be read from a denominator
  product; it requires finite pairing matrices, kernel compatibility, Lie
  ideal stability, and coideal stability.
- `S7-A4` valid: no-extra-relations and completed PBW are kernel and
  associated-graded theorems, not coefficient equalities.
- `S7-A5` invalid as an attack on the conditional theorem: once the
  cofinal finite-window certificate is supplied, the presentation
  universal property gives the isomorphism with
  \(\mathfrak g_{\Delta_5}\).

## Repairs inscribed

- `main.tex`: added
  `def:cofinal-primitive-recognition-certificate`, a global finite-window
  certificate consisting of downward-saturated windows and finite checks
  for representatives, parities, relations, full parity dimensions, Hopf
  pairing/radical, no-extra-relations, generation, and completed PBW.
- `main.tex`: added
  `prop:global-recognition-cofinal-certificate`, proving that this
  cofinal certificate supplies the remaining global hypotheses
  `(S5)`--`(S9)` of `thm:primitive-recognition`, hence gives
  \(P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}\).
- `main.tex`: connected the open compact realization problem to the new
  cofinal finite-window certificate, so the residual is exact rather than
  a slogan about "primitive recognition".

## Manuscript anchors

- `main.tex:9364`: presentation-level primitive recognition theorem.
- `main.tex:9545`: completed Hopf pairing and radical quotient
  hypothesis.
- `main.tex:9578`: no-extra-relations hypothesis.
- `main.tex:9607`: completed PBW hypothesis.
- `main.tex:9700`: new cofinal finite-window recognition certificate.
- `main.tex:9794`: new global-recognition proposition.
- `main.tex:10413`: open full certificate now points to the cofinal
  finite-window certificate.

## Verification

- `python3 compute/verify_square_root.py`: passed.  It confirmed
  \([qrs]D_5/(qrs)^{1/2}=93\), the \(29|93\) first timelike target split,
  height-four signed/additive gaps \(108|90|18\), doubled isotropic gaps
  \(10|9|1\), and real-string exponents \(3,5,3\).
- `python3 -m py_compile compute/verify_square_root.py`: passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-seventh-recognition-texcheck main.tex`:
  passed.  The single pass reported expected unresolved references and
  citations because it was not a full `make` build.
- `git diff --check -- main.tex compute/verify_square_root.py notes/seventh_recognition_global_attack_heal_report.md`:
  passed.

## Files changed

- `main.tex`
- `notes/seventh_recognition_global_attack_heal_report.md`

`compute/verify_square_root.py` was read and executed but not edited in
this seventh-recognition pass.

## Residual obstruction

Full compact recognition remains conditional.  A compact source must still
construct the cofinal finite-window certificate: actual compact primitive
representatives, all finite relation checks, full parity dimensions, Hopf
pairing matrices and closed radical kernels, finite kernel equalities,
generation, and PBW associated-graded transition isomorphisms.  The first
finite bracket test remains the \(\delta_1+\delta_2+\delta_3\) channel:
the compact source must refine the signed dimension \(-64\) to compact
\(29|93\) bases, structure constants, Jacobi/Serre checks, pairing
matrices, and the radical quotient.
