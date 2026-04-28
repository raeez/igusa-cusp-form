# Fifth D0/Pfaffian Attack-Heal Report

Date: 2026-04-28.
Role: H01.
Worktree: `/tmp/igusa-fifth-d0`.
Branch: `agent/igusa-fifth-d0-pf-20260428`.
Owned paths: `main.tex`, `notes/fifth_d0_pf_attack_heal_report.md`.

## Stable Core

The stable core remains conditional.  The manuscript proves finite
normal-ordered supports, finite cofinal target windows, and additivity of
`\overline\Pi_X`.  It imports the Borcherds--Gritsenko--Nikulin product
with leading coefficient `64`.  It does not construct a compact Hall
state object, a reduced quotient orientation, a Pfaffian line, a
first-order Dirac operator, or compact parity pieces from the determinant
or from the OP scalar square.

## Valid Attacks

1. Severity 1: the transition system was not genuinely finite-stage.
   The previous `D0` residual tuple carried independent defects
   `\{\mathfrak o^{tr}_{R'R}\}_{R'\ge R}` and
   `\{\mathfrak o^{top}_{\Theta,R'R}\}_{R'\ge R}` at a fixed height.
   This made a finite stage depend on infinitely many larger stages.

2. Severity 1: `\mathfrak D_{X,R}` occurred in the package and the
   Pfaffian clause, but the finite first-order object was not typed in
   `(D0-D)`.  The text jumped from finite complexes `K_R^\Pi` to the
   inverse-limit operator `\mathfrak D_X`.

3. Severity 1: the finite Pfaffian line was named but its finite square
   was not explicitly part of the stage.  The square-root datum must live
   before the inverse limit, not only at `X`.

4. Severity 2: the Pfaffian residuals forced signed multiplicities, but
   the exact finite consequence was not isolated.  In particular, if a
   nonzero Borcherds target degree lies in the target window but not in
   `\Gamma_R^\Pi`, the parity residual is automatically nonzero.  This is
   a stronger finite obstruction than a status label.

5. Severity 2: compact parity pieces cannot be reconstructed from the
   finite product.  Adding the same finite vector space in both parities
   over any active target degree preserves the product, the support test,
   the signed parity test, and the leading coefficient.

6. Severity 3: the orientation obstruction tuple was indexed by stable
   objects.  For finite-stage bookkeeping it must be indexed by the finite
   stable-stratum atlas chosen at the stage.

## Repairs Inscribed

- `main.tex:7060`: fixed a cofinal discrete subsystem
  `\mathcal R=\{R_0<R_1<\cdots\}` and successor notation
  `R^+=R_{\nu+1}`.  Non-successor transitions are composites.

- `main.tex:7100`: made `D_{0,R}` a package for `R\in\mathcal R`.

- `main.tex:7134`: replaced independent all-larger transition residuals by
  the successor residual `\mathfrak o^{tr}_{R^+R}`.

- `main.tex:7157`: added `\mathfrak D` to the transition compatibility
  list, with explicit defect
  `\rho^K_{R^+R}\mathfrak D_{X,R^+}-\mathfrak D_{X,R}\rho^K_{R^+R}`.

- `main.tex:7207`: reindexed the quotient obstruction over the finite
  stable-stratum index set `\mathsf{St}_R`.

- `main.tex:7359`: made the finite-topology descent obstruction the
  successor defect `\mathfrak o^{top}_{\Theta,R^+R}`.

- `main.tex:7407`: typed the finite first-order operator/algebra
  `\mathfrak D_{X,R}:K_R^\Pi\to K_R^\Pi` and its transition
  compatibility.

- `main.tex:7439`: added the finite Pfaffian square
  `\mathscr L_{\mathrm{Pf},R}^{\otimes2}\simeq\mathscr L_{\det,R}` and
  transition compatibility for the square.

- `main.tex:7527`: added Proposition
  `prop:finite-pfaffian-window-obstruction`.  It proves
  `A_R\subset\Gamma_R^\Pi` for active finite target degrees and isolates
  the finite `K_0`-Pfaffian shadow as the strongest object constructible
  from the automorphic input alone.

- `main.tex:7648`: replaced the theorem-level residual tuple by the finite
  successor-stage tuple.

- `main.tex:8724`: updated the open `D0` obligations to ask for stages over
  `\mathcal R`, successor transitions, finite `\mathfrak D_{X,R}`, finite
  Pfaffian squares, and compact parity pieces on the test windows.

## Exact Formulas

- Cofinal finite stages:
  `\mathcal R=\{R_0<R_1<R_2<\cdots\}`, `R_\nu\to\infty`,
  `R^+=R_{\nu+1}`.

- Test windows:
  `\Gamma_R^{test}=(\Gamma_R^\Pi\setminus\{0\})\cup\Gamma_{\Delta,R}`,
  with `\Gamma_{\Delta,R}` exhausting
  `\Gamma_{\mathrm{eff}}\setminus\{0\}`.

- Active and zero finite target pieces:
  `A_R=\{\gamma\in\Gamma_R^{test}\mid a_\Delta(\gamma)\ne0\}`,
  `Z_R=\{\gamma\in\Gamma_R^{test}\mid a_\Delta(\gamma)=0\}`.

- Finite Pfaffian obstruction:
  `P^\Pi_{R,\gamma}=0` for `\gamma\in Z_R`, and
  `\gamma\in\Gamma_R^\Pi`,
  `p^{\bar0}_{R,\gamma}-p^{\bar1}_{R,\gamma}=a_\Delta(\gamma)` for
  `\gamma\in A_R`.

- Target `K_0` shadow:
  `[\mathsf P_{\Delta,R}^{K_0}]=\sum_{\gamma\in\Gamma_R^{test}}
  a_\Delta(\gamma)[\mathbb C_\gamma]`.

- Finite formal section:
  `\operatorname{pf}^{K_0}_{\Delta,R}
  =64q^{1/2}r^{1/2}s^{1/2}
  \prod_{\gamma\in\Gamma_R^{test}}(1-x^\gamma)^{a_\Delta(\gamma)}`.

## Commands Run

- `sed` and `rg` reads of `CLAUDE.md`, `AGENTS.md`,
  `notes/worktree_semantic_merge_audit_20260428.md`,
  `notes/architecture_realization_status_20260428.md`,
  `notes/critique_resolution_table.md`, prior D0/Pfaffian reports, and
  the D0/Pfaffian regions of `main.tex`.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fifth-d0-texcheck main.tex` passed as a one-pass TeX check.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-fifth-d0-texcheck/main.log` found no fatal TeX errors.
- `git diff --check -- main.tex notes/fifth_d0_pf_attack_heal_report.md`
  passed.

## Remaining Open Questions

The actual compact object is still open.  One must construct the
finite-type Hall/factorization stages, the source observable shadow, the
hybrid wrapped sector, the quotient orientation trivializations, the
normal-ordered chain-level descent, the finite first-order operators
`\mathfrak D_{X,R}`, the finite Pfaffian lines and their square roots,
and actual compact parity pieces on every cofinal target window.  The
new proposition proves that the automorphic input supplies only the
finite `K_0` shadow and the active-window coverage obstruction.
