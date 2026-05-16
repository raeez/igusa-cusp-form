# Next Hybrid Attack-Heal Report

Date: 2026-04-28.
Worktree: `/tmp/igusa-next-hybrid`.
Branch: `agent/igusa-next-hybrid-20260428`.

## Claim Attacked

The attacked shortcut was that the finite hybrid object
\(\mathcal F_X^{\mathrm{hyb}}\) could still be read as slogan-level
local/global factorization: ordinary \(\operatorname{Ran}(E)\) locality
plus a detached Fock/Hecke determinant factor, followed by quotienting by
the elliptic translation action.

Status: false.  Positive elliptic degree dominates \(E\), so the
wrapped sector must keep relative \(E\)-position before the reduced
quotient.  The finite object is a certificate only if local-local,
local-wrapped, and wrapped-wrapped correspondences are formed in the
finite HN quotient before \(Q_{E,R}\), are associative over two-step
flags, and feed protected integration with trace degree \(s^{b_R}\).

## Manuscript Inscription

- `main.tex:224-235` now states the positive Igusa \(s\)-direction as
  finite HN data: \(b_R\), rigidified wrapped prequotients, mixed
  correspondences before the reduced \(E\)-quotient, \(Q_{E,R}\), and
  protected integration with homogeneous trace degree \(s^{b_R}\).
- `main.tex:4609-4901` strengthens
  `def:hybrid-wrapped-factorization-certificate` into a finite-stage
  tuple
  \[
  (\mathcal C_{\sigma,S,\le R}, b_R,\mathcal F_R^{loc},
  \mathcal G_R^{wr}, \mathfrak E_R^{loc},\mathfrak E_R^{hyb},
  \mathfrak E_R^{wr},\mathfrak{Flag}_R^{hyb},\lambda_R,Q_{E,R},
  \theta_R^Q,o_R,I_R^{prot}).
  \]
- `main.tex:4651-4659` records the finite additivity law
  \[
  b_R(0)=0,\qquad b_R(\gamma+\gamma')=b_R(\gamma)+b_R(\gamma')
  \]
  inside \(\Gamma_{\sigma,S}^{HN}(R)\), with height \(>R\) killed.
- `main.tex:4684-4716` requires rigidified wrapped prequotients with
  \(E\)-equivariant anchors
  \[
  \lambda_{\eta,R}:\mathcal M_{\eta,R}^{wr,rig}\to E,\qquad
  \lambda_{\eta,R}(tW)=t+\lambda_{\eta,R}(W).
  \]
- `main.tex:4718-4786` makes the finite operation maps actual pull-push
  maps
  \[
  \mu_R^\bullet=q_!\circ\operatorname{TS}_R^\bullet\circ p^*
  \]
  on local, mixed, and wrapped extension correspondences.
- `main.tex:4788-4812` requires two-step flag associativity before
  completion, after vanishing cycles, Thom-Sebastiani transport,
  orientation signs, and quotient by height \(>R\).
- `main.tex:4814-4839` makes \(Q_{E,R}\) a quotient-after-correspondence
  functor
  \[
  Q_{E,R}:\mathsf{BM}^{E,hyb}_R\to
  \mathsf{BM}^{red,hyb}_R
  \]
  with comparison isomorphisms
  \[
  \theta^Q_{\mu,R}:Q_{E,R}q_!\operatorname{TS}p^*
  \xrightarrow{\sim}
  \overline q_!\overline{\operatorname{TS}}\,
  \overline p^*(Q_{E,R}^{\boxtimes k}).
  \]
- `main.tex:4841-4868` records the protected integration law
  \[
  I_R^{prot}(Q_{E,R}x)\in
  s^{b_R(\gamma)}\mathbb C[q^{\pm1},r^{\pm1}]
  \]
  for a homogeneous class of charge \(\gamma\).
- `main.tex:4914-4951` records the finite consequences and states that
  the proposition constructs no compact source object, quotient functor,
  orientation system, or protected integration map.
- `main.tex:6507-6516` and `main.tex:7845-7855` propagate the same
  finite certificate into the Dirac-Igusa \((H_X)\) entry and the final
  synthesis.

## Status

Conditional certificate only.  The manuscript proves the locality
obstruction and states the exact finite data required.  It does not
construct the compact Hall category, the wrapped rigidification, the
mixed extension stacks, the quotient functor \(Q_{E,R}\), protected
integration, or the primitive BKM recognition.

## Checks

- `rg -F` confirmed no remaining `hybrid local/global`, `structural
  certificate`, or `construction target` phrase in `main.tex`.
- `git diff --check` passed.
- `pdflatex -halt-on-error -interaction=nonstopmode
  -output-directory=/tmp/igusa-next-hybrid-texcheck main.tex` passed.
  It was a one-pass syntax check, so unresolved references/citations and
  rerun warnings remain expected.

## Remaining Obligations

1. Construct the compact extension-closed Hall category and the finite
   HN quotients with finite-type local and wrapped moduli.
2. Construct the rigidified wrapped prequotients and anchors
   \(\lambda_{\eta,R}\) without forcing wrapped support into a finite
   Ran point.
3. Construct admissible local-local, local-wrapped, and wrapped-wrapped
   extension stacks with proper-support pull-push functors.
4. Prove Thom-Sebastiani-compatible orientations and two-step flag
   associativity in every finite quotient.
5. Construct \(Q_{E,R}\) after correspondences, including
   finite-stabilizer gerbe trivializations and the isomorphisms
   \(\theta^Q_{\mu,R}\).
6. Construct protected integration recovering the \(s^{b_R}\) degree
   coefficientwise and prove the primitive bracket satisfies the
   Borcherds-Kac-Moody presentation.
