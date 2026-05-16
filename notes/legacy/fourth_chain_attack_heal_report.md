# Fourth Chain Attack-Heal Report

Date: 2026-04-28.

## Stable Core

The lattice normal-ordering theorem remains intact.  The quadratic Gram
map \(\Pi_X\) has defect \(B\), the corrected charge extension
\(\widehat\Gamma_X\) has additive homomorphism \(\overline\Pi_X\), and
raw \(\Pi_X\)-descent still cannot realize the full BKM real-root
strings.  No lattice formula was changed.

The chain-level Hall lane remains conditional.  A compact source must
supply finite HN stages, reduced quotient and orientation descent,
normal-ordering cochains, finite-fibre compatibility, Frobenius
cyclicity, negative-cyclic lift, closed Hopf radical ideal/coideal
stability, no-extra-relations, and completed PBW compatibility.

## Valid Attacks

- H05-A1, finite fibres/topology: the notation
  \(\overline\Pi_{X,*}^{\Theta}\) still allowed an uncontrolled product
  over fibres of \(\overline\Pi_X\).  This could smuggle in an infinite
  product or completion not present at finite HN height.
- H05-A2, completed tensor/coproduct: the completed Hopf coproduct and
  pairing needed explicit HN inverse-limit compatibility, not only
  notation \(\widehat{\otimes}\).
- H05-A3, cyclic route: the negative-cyclic cochain could still be read
  as supplying more than Hochschild normal ordering and cyclic lift.
  It does not supply finite-fibre topology, Frobenius, or radical
  coideal stability.
- H05-A4, Frobenius: the CY-Serre/Frobenius route needed the finite Hall
  product, trace, pairing, and primitive projection to commute with
  transitions.  A cyclic trace on an auxiliary model is not enough.
- H05-A5, radical quotient: equality of radical ranks is insufficient.
  The quotient requires finite-stage kernels, Lie ideal condition,
  coideal condition, closedness, and transition compatibility.
- H05-A6, PBW/no-extra-relations: target PBW and signed dimensions do not
  transfer to the compact source.  The source needs finite saturated
  window kernel checks and PBW associated-graded isomorphisms.

## Repairs Inscribed

- `main.tex:5471`: the normal-ordering coefficient dg category now fixes
  complete separated HN topology and defines completed tensor products as
  inverse limits of finite-stage tensor products.
- `main.tex:5537`: the old \(\Gamma_X^{\mathrm{phys}}\)-pushforward
  formula is only an uncompleted finite-support shorthand.
- `main.tex:5550`: the actual finite-stage formula is
  \[
  (\overline\Pi_{R,*}^{\Theta}V_R)_\gamma
  =
  \prod_{\overline\Pi_X(c,T)=\gamma}(V_R)_{(c,T)},
  \]
  with finite fibre inside \(\widehat\Gamma_R\), and
  \(\overline\Pi_{X,*}^{\Theta}\) is its inverse limit.
- `main.tex:5682`: hypothesis (E) now requires finite-stage products,
  brackets, coproducts, pairings, and \(\overline\Pi_{R,*}^{\Theta}\) to
  commute with transitions.
- `main.tex:5850`: new obstruction
  \[
  \mathfrak o_\Theta^{\mathrm{top}}
  =
  \{\mathfrak o^{\mathrm{fib}},
    \mathfrak o^m,
    \mathfrak o^\Delta,
    \mathfrak o^{\langle,\rangle}\}_{R'\ge R}
  \]
  records finite-fibre descent, product, coproduct, and pairing
  transition defects.
- `main.tex:6205`: the negative-cyclic route now explicitly supplies none
  of finite-HN topology, Frobenius, or Hopf-radical ideal/coideal data.
- `main.tex:6277`: the Frobenius-from-Serre lemma now requires
  finite-stage Hall product/traces/pairings/primitive projections to
  commute with transitions, and its following remark states that this
  proves only \(\mathfrak o_F=0\).
- `main.tex:6905`: \(D0\)-normal-ordering now carries finite-topology
  trivializations and finite fibre product formulae.
- `main.tex:7117`: the \(D_0\) residual tuple now has seven chain-level
  obstruction groups: topological/fibre, Hochschild, triple, Jacobi,
  Frobenius, negative-cyclic, and Hopf-radical ideal/coideal.
- `main.tex:7730`: the radical quotient certificate now requires
  finite-stage kernels, transition-compatible radicals, Lie ideal and
  coideal inclusions, and closure.
- `main.tex:7763` and `main.tex:7792`: no-extra-relations and PBW are now
  finite saturated window assertions before completion.
- `main.tex:8162`: the open \(D_0\)-descent obligation includes
  \(\mathfrak o^{\mathrm{top}}_{\Theta,R'R}=0\) for every \(R'\ge R\).

## Exact Obstruction Classes

The chain-level normal-ordering closure now requires:
\[
\mathfrak o_{\Theta}^{\mathrm{top}},\quad
\mathfrak o_{\Theta}^{\mathrm{Hoch}},\quad
\mathfrak o_{\Theta}^{\mathrm{tri}},\quad
\mathfrak o_{\Theta}^{\mathrm{Jac}},\quad
\mathfrak o_F,\quad
\mathfrak o_{\Theta}^{\mathrm{cyc}},\quad
\mathfrak o_{\Theta}^{\mathrm{rad}}.
\]
The radical class is the ordered pair
\[
\mathfrak o_{\Theta}^{\mathrm{rad}}
=
(\mathfrak o_{\Theta}^{\mathrm{rad,Lie}},
 \mathfrak o_{\Theta}^{\mathrm{rad,coid}}),
\]
and coideal vanishing means
\[
(\bar q_\Pi\widehat{\otimes}\bar q_\Pi)\Delta_\Theta(r)=0
\qquad(r\in\operatorname{Rad}_X^\Pi).
\]

## Verification

- `git diff --check -- main.tex` passed.
- One-pass TeX check passed:
  `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fourth-chain-texcheck-20260428-H05 main.tex`.
  It reported expected undefined references/citations because BibTeX and
  reruns were not invoked.
- `compute/verify_lattice.py` was not run because no lattice formula was
  changed.

## Files Changed

- `main.tex`
- `notes/fourth_chain_attack_heal_report.md`

## Residual Obligations

Construct the compact finite-HN Hall/factorization stages, the reduced
\(E\)-quotient descent, the Joyce--Upmeier \(S^1\)-equivariant
orientation cocycle, \(\Theta_\Pi\) and \(\Theta_\Pi^{-}\) with all seven
obstruction classes zero, the CY/Serre or equivalent Hall cyclic trace
source for \(\mathfrak o_F=0\), the closed Hopf radical ideal/coideal
quotient, the finite-window no-extra-relations theorem, and completed
PBW compatibility.
