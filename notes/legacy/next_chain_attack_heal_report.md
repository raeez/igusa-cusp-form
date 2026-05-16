# Next Chain Attack-Heal Report

Date: 2026-04-28.

## Claim Attacked

The attacked claim was the chain-level lift
\[
\overline\Pi_X(c,T)=\Pi_X(c)-T
\quad\Longrightarrow\quad
\overline\Pi_{X,*}^{\Theta}
\]
as if the lattice normal-ordering identity already supplied Hall descent.
That implication is false without coefficient categories, central
translation quasi-isomorphisms, Hall flag coherences, cyclic lift,
Frobenius/Hopf invariance, and radical quotient control.

## Heal Inscribed

`main.tex` now separates the proved lattice statement from the exact
chain-level certificate:

- coefficient dg category and central translations:
  \[
  (\mathsf T_\eta V)_\gamma=V_{\gamma+\eta},
  \qquad
  B_{\mathrm{ch}}(c,c')=\mathsf T_{B(c,c')};
  \]
- Hochschild normal-ordering equation:
  \[
  \Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)},\qquad
  d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}};
  \]
- triple pentagon obstruction over \(\mathfrak{Flag}_{a,b,c}\):
  \[
  \operatorname{Pent}_{\Theta}(a,b,c)
  =
  [(\vartheta_{a,b}\otimes1)\vartheta_{a+b,c}]
  -[(1\otimes\vartheta_{b,c})\vartheta_{a,b+c}];
  \]
- negative-cyclic lift:
  \[
  (b+uB_{\mathrm C})\Theta_\Pi^{-}=B_{\mathrm{ch}}^{-};
  \]
- Frobenius/Hopf obstruction:
  \[
  \mathfrak o_F(x,y,z)=
  \langle[x,y]_{\Theta},z\rangle
  +(-1)^{|x||y|}\langle y,[x,z]_{\Theta}\rangle;
  \]
- radical-stability obstruction:
  \[
  \mathfrak o_{\Theta}^{\mathrm{rad}}(x,r,z)=
  \langle[x,r]_{\Theta},z\rangle,
  \qquad r\in\operatorname{Rad}_X^\Pi .
  \]

The obstruction package is now six classes:
\[
\mathfrak o_{\Theta}^{\mathrm{Hoch}},\quad
\mathfrak o_{\Theta}^{\mathrm{tri}},\quad
\mathfrak o_{\Theta}^{\mathrm{Jac}},\quad
\mathfrak o_F,\quad
\mathfrak o_{\Theta}^{\mathrm{cyc}},\quad
\mathfrak o_{\Theta}^{\mathrm{rad}}.
\]

## File Anchors

- `main.tex:4967`: normal-ordering coefficient dg category.
- `main.tex:5210`: triple pentagon obstruction formula.
- `main.tex:5293`: six-class obstruction package.
- `main.tex:5404`: proof separating lattice degree shadows from chain
  Jacobi/Frobenius/radical obligations.
- `main.tex:5478`: Hopf--Frobenius lemma weakened to exact obstruction;
  non-degeneracy detects but does not construct (F).
- `main.tex:6548`: Dirac-Igusa certificate now requires all six descent
  obstructions to vanish on finite HN quotients.

## Commands Run

- `sed -n` and `nl -ba` reads of `.agents/skills/chriss-ginzburg-rectify/SKILL.md`,
  `CLAUDE.md`, `AGENTS.md`, ecosystem excerpts, `proj.bib`, relevant
  `notes/` reports, and the assigned `main.tex` regions.
- `rg` scans for chain normal-ordering, Hall, Hochschild, pentagon,
  Jacobiator, negative-cyclic, Frobenius, Hopf, radical, descent, and
  `\overline\Pi_{X,*}^{\Theta}`.
- Targeted stale-notation scans: a PCRE scan for unbarred Pi-star
  descent notation, a scan for obsolete four-class obstruction wording,
  and raw-pushforward recognition scans in `main.tex`.
- `git diff --check -- main.tex`.
- `git diff --check`.
- `git diff --cached --check`.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-next-chain-texcheck main.tex`.
- `git add main.tex notes/next_chain_attack_heal_report.md`.

## Verification

- No unbarred Pi-star descent notation remains in `main.tex`.
- No `main.tex` hit remains for the stale four-class obstruction wording
  or for obsolete raw-pushforward recognition language.
- `git diff --check`, `git diff --check -- main.tex`, and
  `git diff --cached --check` passed.
- The one-pass TeX check passed.  It reported expected undefined
  references/citations because BibTeX and reruns were not invoked.

## Remaining Open Obligations

Construct the finite-HN compact Hall/factorization stages, the reduced
\(E\)-quotient descent, the Joyce--Upmeier \(S^1\)-equivariant
orientation cocycle, the \(\Theta_\Pi\) quasi-isomorphisms with
\(\operatorname{Pent}_{\Theta}=0\), the negative-cyclic representative,
the Frobenius/Hopf identity \(\mathfrak o_F=0\), and closed coideal
stability of \(\operatorname{Rad}_X^\Pi\) before taking the completed
radical quotient.
