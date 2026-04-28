# Worktree D0 Report

Date: 2026-04-28.

## Claim Attacked

The first-order \(D_0\)-certificate still permitted a black-box reading:
one could cite \(D_0\) without seeing the finite Hall stages, transition
maps, quotient obstruction classes, \(\Theta\)-classes, or Pfaffian parity
defects that must actually be supplied.

## Files Changed

- `main.tex`
- `notes/worktree_d0_report.md`

## Manuscript Change

- Strengthened hypothesis `(D0)` in
  `thm:dirac-pfaffian-recognition-conditional` to require a finite-stage
  \(D_0\)-certificate: stages \(D_{0,R}\), transition maps, reduced
  orientation and finite-stabilizer obstruction trivializations,
  Hochschild/cyclic \(\Theta\)-trivializations, and Pfaffian parity
  defects.
- Rebuilt `def:first-order-d0-certificate` as an inverse system over HN
  height \(R\), with finite normal-ordered support
  \(\widehat\Gamma_R\), maps \(m_R,\Delta_R,[\,\cdot\,,\,\cdot\,]_R\),
  \(I_R^{\mathrm{prot}}\), \(\iota_R^{obs}\), transition maps
  \(\rho^H,\rho^F,\rho^K\), and stage Pfaffian lines.
- Added the exact finite-stage obstruction tuple
  \[
  \mathfrak O_{D_0,R}=
  (\{\mathfrak o^{or}_{R,\mathcal C}\}_{\mathcal C},
  \mathfrak o^{\mathrm{Hoch}}_{\Theta,R},
  \mathfrak o^{\mathrm{cyc}}_{\Theta,R},
  \{\mathfrak o^{\mathrm{par}}_{R,\gamma}\}_{\gamma},
  \mathfrak o^{\mathrm{lead}}_R).
  \]
- Strengthened `thm:first-order-d0-certificate` with a proof that the
  certificate implies every later use of `(D0)` in the conditional
  Dirac--Pfaffian theorem.
- Updated `op:compact-igusa-realization` so the open \(D_0\) obligations
  are finite-stage state, quotient, observable, descent, and Pfaffian
  construction tasks.

## Theorem Status

- Proved: finite support \(\widehat\Gamma_R\) at each HN height \(R\);
  additivity of \(\overline\Pi_X\) on \(\widehat\Gamma_X\).
- Imported: \(\mathsf{Den}_{\Delta_5,E}\), \(\mathfrak g_{\Delta_5}\),
  and the Borcherds--Gritsenko--Nikulin product
  \(\Delta_5\).
- Conditional: a supplied finite-stage \(D_0\)-certificate gives the
  `(D0)` hypothesis and the Pfaffian normalization
  \(\operatorname{pf}_X=\Delta_5\).
- Open: construction of the finite compact Hall/factorization stages,
  quotient trivializations, hybrid wrapped source, \(\Theta\)-cochains,
  Pfaffian line, first-order operator, and compact parity pieces.

## Commands Run

- `sed -n` reads of the local skill, `CLAUDE.md`, `AGENTS.md`, required
  notes, and current `main.tex` regions.
- `rg` scans for `def:first-order-d0-certificate`,
  `thm:first-order-d0-certificate`,
  `thm:dirac-pfaffian-recognition-conditional`, `D0-F`, `D0-Q`,
  `mathfrak O_{D_0,R}`, and D0 obstruction classes.
- `python3 compute/verify_lattice.py` -- passed.
- `python3 compute/verify_square_root.py` -- passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-d0-texcheck main.tex` -- passed.
- `BIBINPUTS=/tmp/igusa-agent-d0: bibtex main` in
  `/tmp/igusa-d0-texcheck` -- passed.
- Three further `pdflatex` passes into `/tmp/igusa-d0-texcheck` -- passed;
  `rg -n "undefined|Rerun|Label\\(s\\)" /tmp/igusa-d0-texcheck/main.log`
  reports no unresolved labels or citations.
- `git diff --check` -- passed.

## Remaining Obstruction

No compact \(K3\times E\) first-order source is constructed.  The exact
remaining obstruction is now finite-stage: build \(D_{0,R}\), prove
transition compatibility, trivialize \(\mathfrak O_{D_0,R}\) for all
heights \(R\), and then pass to the HN-completed reduced compact
quotient.
