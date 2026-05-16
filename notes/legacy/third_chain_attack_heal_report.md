# Third Chain Attack-Heal Report

Date: 2026-04-28.

## Claim Attacked

The attacked lane was the chain normal-ordering descent in `main.tex`:
coefficient dg category, the identity
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}},
\]
the two-step flag pentagon \(\operatorname{Pent}_{\Theta}\), Jacobi
defect, negative-cyclic lift, Frobenius obstruction \(\mathfrak o_F\),
and Hopf radical stability.

The main failure modes were:

- treating the \(\Gamma_X^{\mathrm{phys}}\)-graded pushforward formula
  as sufficient after the \(\widehat\Gamma_X\)-counterterm is introduced;
- recording radical stability only as Lie-ideal stability, while the Hopf
  quotient also needs coideal stability and closedness;
- listing only Hochschild, triple, Jacobi, and cyclic finite-stage
  normal-ordering defects in the \(D_0\)-certificate;
- leaving the negative-cyclic construction as an untyped proof paragraph;
- allowing language that could be read as deriving Frobenius cyclicity
  from non-degeneracy.

## Heal Inscribed

`main.tex` now records the \(\widehat\Gamma_X\)-graded form of
\(\overline\Pi_{X,*}^{\Theta}\):
\[
(\overline\Pi_{X,*}^{\Theta}V)_\gamma
=
\prod_{\overline\Pi_X(c,T)=\gamma}V_{(c,T)}.
\]

The radical obstruction remains one of the six normal-ordering classes,
but is now a two-component obstruction:
\[
\mathfrak o_{\Theta}^{\mathrm{rad}}
=
(\mathfrak o_{\Theta}^{\mathrm{rad,Lie}},
\mathfrak o_{\Theta}^{\mathrm{rad,coid}}).
\]
The Lie component is
\[
\mathfrak o_{\Theta}^{\mathrm{rad,Lie}}(x,r,z)
=\langle[x,r]_{\Theta},z\rangle,
\]
and the coideal component is
\[
\mathfrak o_{\Theta}^{\mathrm{rad,coid}}(r)
=
(\bar q_\Pi\widehat{\otimes}\bar q_\Pi)\Delta_\Theta(r).
\]
Thus radical descent requires
\[
\Delta_\Theta(\operatorname{Rad}_X^\Pi)
\subset
\overline{\operatorname{Rad}_X^\Pi\widehat{\otimes}P_X^\Pi
+P_X^\Pi\widehat{\otimes}\operatorname{Rad}_X^\Pi},
\]
with closedness in the HN topology still a separate topological input.

The finite \(D_0\)-certificate now includes
\[
\mathfrak o_{F,R},\qquad
\mathfrak o_{\Theta,R}^{\mathrm{rad}}
\]
beside the Hochschild, triple, Jacobi, and negative-cyclic classes.
Thus finite normal-ordered descent now carries Frobenius and Hopf
radical ideal/coideal obligations explicitly.

The negative-cyclic route has been promoted to
Proposition `prop:negative-cyclic-normal-ordering-route`.  It gives a
second conditional route to the same normal-ordering cochain:
\[
(b+uB_{\mathrm C})(\iota_{\varpi_X}\Pi_X)=B_{\mathrm{ch}}^{-}
\]
implies the Hochschild shadow
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}
\]
after forgetting to Hochschild cochains, provided the Hall flag
homotopies have \(\operatorname{Pent}_{\Theta}=0\).  The proposition
states that this route supplies neither \(\mathfrak o_F=0\) nor radical
ideal/coideal stability.

The Frobenius lane now says explicitly that non-degeneracy detects a
proved identity after radical quotient; it does not construct
Frobenius cyclicity.  Actual input must be cyclic/Serre, such as
Lemma `lem:F-frobenius-from-cy-serre`, or an equivalent Hall-side cyclic
trace compatible with the coproduct.

## File Anchors

- `main.tex:5256`: normal-ordering coefficient dg category.
- `main.tex:5329`: \(\widehat\Gamma_X\)-graded
  \(\overline\Pi_{X,*}^{\Theta}\) formula.
- `main.tex:5642`: radical obstruction as ideal/coideal pair.
- `main.tex:5779`: proof separates Frobenius-implied ideal stability
  from independent coideal stability.
- `main.tex:5898`: negative-cyclic route proposition.
- `main.tex:6066`: non-degeneracy cannot construct Frobenius cyclicity.
- `main.tex:6552`: finite \(D_0\)-normal-ordering clause includes
  Frobenius and radical obligations.
- `main.tex:6722`: residual tuple includes \(\mathfrak o_{F,R}\) and
  \(\mathfrak o_{\Theta,R}^{\mathrm{rad}}\).
- `main.tex:7009`: Dirac-Igusa certificate requires the six obstruction
  classes, with the radical class read as ideal/coideal data.

## Verification

- `git diff --check` passed.
- `git diff --check -- main.tex` passed.
- One-pass TeX check passed:
  `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-third-chain-texcheck main.tex`.
  It reported expected undefined references/citations because BibTeX and
  reruns were not invoked.

## Remaining Open Obligations

Construct the compact finite-HN Hall/factorization stages, the reduced
\(E\)-quotient descent, the Joyce--Upmeier \(S^1\)-equivariant
orientation cocycle, the \(\Theta_\Pi\) quasi-isomorphisms with
\(\operatorname{Pent}_{\Theta}=0\), a negative-cyclic representative,
the Frobenius identity \(\mathfrak o_F=0\), and the closed Hopf radical
ideal/coideal stability before taking the completed radical quotient.
