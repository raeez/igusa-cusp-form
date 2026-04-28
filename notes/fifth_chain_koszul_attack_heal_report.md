# Fifth Chain/Koszul Attack-Heal Report

Date: 2026-04-28.
Role: H05.
Worktree: `/tmp/igusa-fifth-chain-koszul`.
Branch: `agent/igusa-fifth-chain-koszul-20260428`.

## Claim Attacked

The attacked lane was obligations (6) and (7): chain-level
normal-ordering descent and the chiral Koszul source coalgebra.

Status before this pass: mostly guarded, but two survivable weaknesses
remained.

- The full-certificate entry still propagated the normal-ordering package
  as six obstruction classes, omitting the finite-topology class
  `\mathfrak o_\Theta^{top}` even though the theorem and `D0-N` had
  already made finite fibres and completed tensor/coproduct continuity
  load-bearing.
- The Koszul source certificate required a conilpotent coalgebra
  `C_{X,R}`, filtration `F^{co}_{R,\bullet}`, and collision coproduct
  `\Delta_R^{ch}`, but did not type the finite filtration, conilpotence,
  coassociativity/counit, and transition-continuity defects explicitly
  enough to block a false transfer from the target bar-cobar counit.

## Repairs Inscribed

- `main.tex:254`: the introduction now names the finite source filtration
  and collision coproduct as part of the conditional recognition
  certificate.
- `main.tex:4986`: the Koszul source coalgebra clause now requires a
  coaugmented finite-stage chiral coalgebra with counit
  `\varepsilon_R^C`, coaugmentation `\eta_R^C`, bounded exhaustive
  filtration, finite collision pull-push coproduct, coassociativity,
  counit, and transition-compatible coproduct square.
- `main.tex:5083`: the Koszul residual tuple now includes
  `\mathfrak o_R^{fil}`, `\mathfrak o_R^{\Delta,ch}`, and
  `\mathfrak o_{R'R}^{C,tr}` in addition to the previous source,
  conilpotence, bar, cobar, hybrid, normal-ordering, separation, and
  primitive residuals.
- `main.tex:7989`: the full `D_X` entry now requires seven
  normal-ordering obstruction classes, including
  `\mathfrak o_\Theta^{top}`.
- `main.tex:8752`: the open full-certificate obligation now names finite
  coassociativity, counit, and transition-continuity diagrams for the
  source collision coproduct.

## Exact Complexes And Diagrams

The new finite filtration residual is
\[
\mathfrak o^{\mathrm{fil}}_{R}
=
\left(
F^{\mathrm{co}}_{R,-1},\
C_{X,R}/F^{\mathrm{co}}_{R,N_R},\
\{d_C(F^{\mathrm{co}}_{R,p})\to C_{X,R}/F^{\mathrm{co}}_{R,p}\}_p,\
\{\Delta_R^{\mathrm{ch}}(F^{\mathrm{co}}_{R,p})\to
(C_{X,R}\otimes C_{X,R})/
\sum_{i+j\le p}F^{\mathrm{co}}_{R,i}\otimes F^{\mathrm{co}}_{R,j}\}_p
\right).
\]

The reduced coproduct and conilpotence defect are
\[
\overline\Delta_R^{\mathrm{ch}}
=\Delta_R^{\mathrm{ch}}
-((\eta_R^C\varepsilon_R^C)\otimes\mathrm{id}
+\mathrm{id}\otimes(\eta_R^C\varepsilon_R^C)),
\qquad
\mathfrak o^{\mathrm{conil}}_R
=(\overline\Delta_R^{\mathrm{ch}})^{N_R+1}.
\]

The collision-coproduct defect is
\[
\mathfrak o_R^{\Delta,\mathrm{ch}}
=
\left(
(\Delta_R^{\mathrm{ch}}\otimes1)\Delta_R^{\mathrm{ch}}
-(1\otimes\Delta_R^{\mathrm{ch}})\Delta_R^{\mathrm{ch}},
(\varepsilon_R^C\otimes1)\Delta_R^{\mathrm{ch}}-\mathrm{id},
(1\otimes\varepsilon_R^C)\Delta_R^{\mathrm{ch}}-\mathrm{id}
\right).
\]

The transition defect is
\[
\mathfrak o^{C,\mathrm{tr}}_{R'R}
=
\left(
(\rho^C_{R'R}\otimes\rho^C_{R'R})\Delta_{R'}^{\mathrm{ch}}
-\Delta_R^{\mathrm{ch}}\rho^C_{R'R},\
\{\rho^C_{R'R}(F^{\mathrm{co}}_{R',p})\to
C_{X,R}/F^{\mathrm{co}}_{R,p}\}_{p}
\right).
\]

Thus the completed coproduct on `C_X` is an inverse limit of finite maps,
not a transported target coproduct:
\[
\begin{tikzcd}
C_{X,R'} \arrow[r,"\Delta_{R'}^{\mathrm{ch}}"]
\arrow[d,"\rho^C_{R'R}"']
& C_{X,R'}\otimes C_{X,R'}
\arrow[d,"\rho^C_{R'R}\otimes\rho^C_{R'R}"]\\
C_{X,R} \arrow[r,"\Delta_R^{\mathrm{ch}}"']
& C_{X,R}\otimes C_{X,R}.
\end{tikzcd}
\]

## Attacks Rejected Without Further Manuscript Change

- The negative-cyclic route remains correctly scoped: it can supply the
  Hochschild normal-ordering shadow and cyclic lift only after the cyclic
  model and triple homotopies are supplied.  It does not prove
  `\mathfrak o_\Theta^{top}=0`, `\mathfrak o_F=0`, or radical coideal
  stability.
- The Frobenius lemma remains correctly conditional on finite-stage Hall
  product, trace, pairing, primitive projection, reduced quotient, and HN
  transition compatibility.  It proves only `\mathfrak o_F=0`.
- The source-target separation lemma already blocks defining `C_{X,R}`,
  `F^{co}`, `\Delta_R^{ch}`, `b_{X,R}`, or primitive representatives from
  the target counit or a homotopy inverse to it.

## Claim Status

- Proved: lattice normal ordering
  `\overline\Pi_X(c,T)=\Pi_X(c)-T` and raw Gram descent no-go.
- Conditional: chain normal ordering, finite topology, Frobenius,
  negative-cyclic lift, radical ideal/coideal stability, and chiral
  Koszul source certificate.
- Open: actual construction of the compact finite-HN Hall/factorization
  source, the hybrid local/wrapped correspondence atlas, finite collision
  coproduct, source filtration, bar comparison, cobar comparison, and
  primitive recognition.

## Commands Run

- `git -C /tmp/igusa-fifth-chain-koszul status --short --branch`
- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`, inherited ecosystem
  sections, and the `chriss-ginzburg-rectify` skill.
- `rg` scans for normal-ordering, `D0-N`, chiral Koszul source
  certificate, `\overline\Pi_{X,*}^{\Theta}`, `C_{X,R}`,
  `F^{\mathrm{co}}`, `\Delta_R^{\mathrm{ch}}`, target counit, and stale
  six-class wording.
- `sed -n` and `nl -ba` reads of the normal-ordering theorem,
  `def:normal-ordering-coefficient-dg-category`, `D0-N`, the chiral
  Koszul source certificate, the full `D_X` entry, and the open
  construction list.
- Reads of previous chain/Koszul/D0/hybrid attack-heal reports in
  `notes/`.
- `git diff --check -- main.tex` -- passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fifth-chain-koszul-texcheck-H05 main.tex`
  -- passed as a one-pass syntax check.  It reported expected first-pass
  undefined references/citations because BibTeX and reruns were not
  invoked.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-fifth-chain-koszul-texcheck-H05/main.log`
  -- no hits.
- `git diff --check -- main.tex notes/fifth_chain_koszul_attack_heal_report.md`
  -- passed.
- `git add main.tex notes/fifth_chain_koszul_attack_heal_report.md`
  -- staged only owned paths.
- `git diff --cached --check -- main.tex notes/fifth_chain_koszul_attack_heal_report.md`
  -- passed.

## Files Changed

- `main.tex`
- `notes/fifth_chain_koszul_attack_heal_report.md`

Pre-existing dirty/untracked files in the worktree were observed and not
touched.
