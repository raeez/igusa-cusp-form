# Worktree Chain Normal Ordering Report

Date: 2026-04-28.

## Claim Attacked

The attacked gap was the passage from the lattice identity
\[
\overline\Pi_X(c,T)=\Pi_X(c)-T
\]
to an actual chain-level descent of the protected Hall bracket.  The
lattice calculation proves additivity of \(\overline\Pi_X\), but it does
not by itself construct the dg category, central translations, cyclic
cochains, Hall flag coherences, orientation transport, Frobenius
compatibility, Hopf radical stability, or reduced \(E\)-quotient descent.

## Files Changed

- `main.tex`
- `notes/worktree_chain_normal_ordering_report.md`

## Cochains And Obstructions Inscribed

The manuscript now defines the normal-ordering coefficient dg category
\[
\mathsf{Ch}_{k,\widehat{\mathrm{HN}},E}^{\Gamma_{\mathrm{gram}}}
=\varprojlim_R\mathsf{Ch}_{k,R,E}^{\Gamma_{\mathrm{gram}}},
\]
central translation autoequivalences
\[
(\mathsf T_\eta V)_\gamma=V_{\gamma+\eta},
\]
and the Picard dg groupoid
\(\mathsf{Pic}^{\mathrm{dg}}_{\Gamma_{\mathrm{gram}}}\).

The chain representative of the Gram defect is
\[
B_{\mathrm{ch}}(c,c')=\mathsf T_{B(c,c')}.
\]
The normal-ordering cochain is
\[
\Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)},
\qquad
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}.
\]
The cyclic lift is required to satisfy
\[
(b+uB_{\mathrm C})\Theta_\Pi^{-}=B_{\mathrm{ch}}^{-}.
\]

The minimal computable obstruction package is now:
\[
\mathfrak o_{\Theta}^{\mathrm{Hoch}},
\quad
\mathfrak o_{\Theta}^{\mathrm{tri}},
\quad
\mathfrak o_{\Theta}^{\mathrm{Jac}},
\quad
\mathfrak o_{\Theta}^{\mathrm{cyc}}.
\]
The Hochschild component is computed from the explicit formula for
\(B(c,c')\).  The triple component is the difference of the two composites
over the Hall flag stack \(\mathfrak{Flag}_{a,b,c}\); its degree shadow is
\[
B(a,b)+B(a+b,c)-B(b,c)-B(a,b+c)=0.
\]
The Jacobi component is the signed Jacobiator of the transported bracket.
The cyclic component is computed by applying the Connes operator to the
chosen cyclic orientation representative.

## Theorem Status

Proved: the lattice-level central extension \(\widehat\Gamma_X\) and
normal-ordered homomorphism \(\overline\Pi_X\).

Conditional: Theorem `thm:ptvv-joyce-pi-descent` now gives the chain-level
descent once the PTVV host, Hall correspondences, reduced \(E\)-quotient,
\(S^1\)-equivariant orientation cocycle, \(\Theta_\Pi\), negative-cyclic
lift, Frobenius identity, and Hopf pairing are supplied.

Open: construction of those data on the compact/wrapped reduced
\(K3\times E\) Hall sector.

## Commands Run

- `pwd`
- `git branch --show-current`
- `git status --short`
- `sed -n` reads of the local skill, `CLAUDE.md`, `AGENTS.md`, ecosystem
  voice/rubric excerpts, notes, `proj.bib`, and the assigned `main.tex`
  regions.
- `rg` scans for `op:pi-descent-of-bracket`,
  `thm:ptvv-joyce-pi-descent`, `Frobenius`, `Theta`, `D_X`, `B_ch`,
  `overline\Pi_X`, and `overline\Pi_{X,*}^{\Theta}`.
- `git diff --check`
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-chain-texcheck main.tex`
- `make`
- targeted stale-notation scans for raw `\Pi_{X,*}^{\Theta}`,
  stale Picard notation, and missing `\Theta` braces.
- `git add main.tex out/main.pdf notes/worktree_chain_normal_ordering_report.md`

## Remaining Obstruction

The full construction is still open.  One must build the compact
finite-HN Hall/factorization object with local-local, wrapped-wrapped, and
mixed local/wrapped correspondences before the reduced \(E\)-quotient;
construct the Joyce--Upmeier orientation cocycle and its \(S^1\)-equivariant
cyclic lift; compute the four obstruction classes above at finite HN
height; prove compatibility in the inverse limit; and then pass through
the completed Hopf radical quotient.
