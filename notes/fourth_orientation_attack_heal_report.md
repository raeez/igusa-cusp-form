# Fourth Orientation Attack-Heal Report

Date: 2026-04-28.

Role: H02.  Worktree: `/tmp/igusa-fourth-orientation`.  Branch:
`agent/igusa-fourth-orientation-20260428`.

## Stable Core

Connected free quotient.  The connected translation quotient is governed
by
```tex
BE\simeq BT^2\simeq K(\mathbb Z^2,2),\qquad
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2.
```
Thus
```tex
H^1(BE;\mathbb F_2)=0,\qquad
H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2,
```
and the connected class is exactly
```tex
\alpha^{E,\mathrm{free}}_{\mathcal C}
=a_1(\mathcal C)u_1+a_2(\mathcal C)u_2.
```
There is no connected \(E_2^{1,1}\) lane.  Translation-fixedness of an
ordinary line is not a finite equivariant linearization.

Finite stabilizers.  For \(E[N]\simeq(\mathbb Z/N)^2\), odd \(N\) has
no positive-degree mod-\(2\) obstruction by transfer.  Even \(N\) is
detected on its two-primary part.  At \(N=2\),
```tex
H^2(BE[2];\mathbb F_2)
=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle,
```
and
```tex
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2).
```
The \(r_i\) are degree-two coefficients.  After
\(\beta^{E,E[2]}_{\mathcal C}=0\), trivial \(E[2]\)-linearization is a
separate degree-one condition
```tex
\lambda_{\mathcal C}^{E[2]}
=\lambda_1x_1+\lambda_2x_2\in H^1(BE[2];\mathbb F_2),
```
with \(\rho_1=\lambda_1,\rho_2=\lambda_2,\rho_3=\lambda_1+\lambda_2\).

For \(2^a\parallel N\), \(a\ge2\),
```tex
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
```
```tex
H^2=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle.
```
The class
```tex
A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2
```
has mixed coefficient \(A_{12}^{(N)}\) invisible to every cyclic
restriction; it is detected by the rank-two quotient
\((\mathbb Z/2^a)^2\twoheadrightarrow(\mathbb Z/2)^2\).

Weyl transport.  A choice of wall transports is first projective:
```tex
w'^*\tau_w\circ\tau_{w'}=(-1)^{c_o(w,w')}\tau_{ww'},
\qquad
c_o\in Z^2(W^{(2)}(\Lambda^{2,1}_{II});\mathbb F_2).
```
The strong Weyl package requires \([c_o]=0\), a killing \(1\)-cochain,
\(\tau_i^2=1\), zero quotient-trivialization torsor defects
\(\omega_{i,\mathcal C}\), and Coxeter coherence.  Only then do the
three type-II Pfaffian signs define a Hall orientation character.

## Valid Attacks And Repairs

`A4-H02-01` valid, healed.  The manuscript still allowed the reader to
identify \(H^2\) gerbe residuals \(r_i\) with \(H^1\) sign characters.
Repaired in `main.tex` around (O1), (P1),
Lemma `bmu2-klein-four-vanishing`, Proposition
`rank-one-e2-linearization-obstruction`, and the certificate clauses:
\(r_i\) are degree-two; \(\rho_i\) are degree-one.

`A4-H02-02` valid, healed.  Cyclic restriction was too weak for even
\(N\ge4\).  Repaired in Lemma `even-finite-stabilizer-residuals`: the
mixed class \(x_1x_2\) restricts to zero on every cyclic subgroup and is
rank-two quotient data.

`A4-H02-03` valid, healed.  (O1)\(^+\) said "coherent lifts" without
naming the projective Weyl cocycle.  Repaired by naming
\([c_o]\in H^2(W^{(2)}(\Lambda^{2,1}_{II});\mathbb F_2)\), the killing
cochain, \(\tau_i^2=1\), and the \(H^1\)-torsor defects.

`A4-H02-04` attacked, stable after repair.  Connected \(BE\)-descent
remains separated from finite stabilizers.  The manuscript now states
that \(H^1(BE)=0\) gives no finite-character information.

`A4-H02-05` attacked, stable.  Automorphic Maass signs remain target
data only.  Hall signs still require (O1), (O1)\(^+\), and (O2).

## Formulas And Constants

No Fourier coefficient, Borcherds exponent, Weyl vector, or scalar
normalization was changed.  Constants \(64\) and \(-4096\) remain outside
the orientation proof.

Group cohomology formulas used:
```tex
H^*(B(\mathbb Z/2)^2;\mathbb F_2)=\mathbb F_2[x_1,x_2],
```
```tex
H^*(B\mathbb Z/2^a;\mathbb F_2)
=\Lambda(x)\otimes\mathbb F_2[y]\quad(a\ge2),
```
```tex
H^1(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\mathbb F_2\langle x_1,x_2\rangle,\qquad
H^2=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle.
```

## Files Changed

- `main.tex`
- `notes/fourth_orientation_attack_heal_report.md`

## Commands

- `rg` over O1, O1\(^+\), \(E[2]\), even \(N\), Pfaffian, Weyl, and
  orientation anchors.
- `git diff --check` passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fourth-orientation-texcheck main.tex`
  passed as a one-pass TeX syntax check.  The run wrote only outside the
  worktree.  Undefined citation/reference warnings are the expected
  one-pass/BibTeX warnings.

## Residual Obligations

Compute
```tex
\alpha^{\mathrm{red}}_{\mathcal C},\quad
a_1(\mathcal C),a_2(\mathcal C),\quad
\beta^{E,N}_{\mathcal C},\quad
\lambda^{E,N}_{\mathcal C}
```
on every Hall stratum used by the quotient.

Construct quotient-compatible null-trivializations and prove
```tex
[c_o]=0,\qquad \tau_i^2=1,\qquad
\omega_{i,\mathcal C}=0
```
with Coxeter coherence.

Supply the three finite type-II Pfaffian wall charts and verify
\(N_{\delta_i}=1\).  Until these data are constructed, the orientation
package remains a certificate target, not an existence theorem.

## Staged Paths

The owned paths staged for integration are:

- `main.tex`
- `notes/fourth_orientation_attack_heal_report.md`
