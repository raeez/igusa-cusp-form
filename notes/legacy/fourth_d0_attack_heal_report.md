# Fourth D0 Attack-Heal Report

Date: 2026-04-28.
Role: H01.
Worktree: `/tmp/igusa-fourth-d0`.
Branch: `agent/igusa-fourth-d0-20260428`.
Owned paths: `main.tex`, `notes/fourth_d0_attack_heal_report.md`.

## Stable Core

Stable core preserved.  The manuscript can state a compact first-order
Dirac-Igusa \(D_0\)-certificate only as finite-stage supplied data with
typed residuals.  The proved core is still: finite normal-ordered support,
finite cofinal target windows, additivity of \(\overline\Pi_X\), and the
imported Borcherds-Gritsenko-Nikulin target determinant.  No compact
state object, source observable algebra, Pfaffian line, or parity split is
constructed.

## Valid Attacks And Heals

1. Target-window leakage.
   - Attack: the previous notation used the same \(R\) for HN height and
     automorphic target height.  This could be read as a hidden calibration
     theorem between compact HN support and the Borcherds cusp window.
   - Heal: `main.tex` now makes the target window a separate nondecreasing
     cofinal schedule \(N_R^\Delta\), with
     \(\Gamma_{\Delta,R}=\{\gamma\mid h_\Delta(\gamma)\le N_R^\Delta\}\).
     The certificate includes the schedule; it is finite-window
     bookkeeping, not a physical existence theorem.
   - Anchors: `main.tex:6554`, `main.tex:6589`,
     `main.tex:6973`, `main.tex:7076`.

2. Finite-stage transition coherence.
   - Attack: vanishing of \(\mathfrak o^{\mathrm{tr}}_{R'R}\) and
     \(\mathfrak O_{D_0,R}\) could be read as numerical zero after passing
     to the inverse limit, rather than as compatible finite data.
   - Heal: the transition residual now requires a chosen finite equality or
     null-homotopy in the indicated Hom complex, compatible under
     \(R''\ge R'\ge R\).  The theorem-level residual tuple now says
     vanishing means chosen null-trivializations in the finite obstruction
     groups or complexes, compatible with every transition.
   - Anchors: `main.tex:6668`, `main.tex:6995`.

3. Source/observable ambiguity.
   - Attack: a finite comparison
     \(\iota_R^{obs}:\mathcal F_R^{D_0}\to\mathsf{Den}_{\Delta_5,E}\)
     could still be misread as allowing the imported target, a target
     truncation, or a homotopy inverse to define the source observable.
   - Heal: the \(D_0\)-observable clause now states that no target
     truncation, target bar-cobar counit, or homotopy inverse to
     \(\iota_R^{obs}\) may define \(\mathcal F_R^{D_0}\); the source is
     supplied first, and the arrow is source-to-target.
   - Anchor: `main.tex:6801`.

## Attacks Checked Without Further Change

- Support/parity residual weakness: already guarded.  The support residual
  is an actual super-vector-space residual in target-zero degrees, while
  the parity residual records only signed superdimension in nonzero target
  degrees.  The Borcherds product fixes the signed integer, not a compact
  even/odd split.  Anchor: `main.tex:6940`.
- False implication from imported target determinant to compact state
  object: still blocked.  The target determinant is imported; the compact
  state-side construction and all residual trivializations remain open.
  Anchors: `main.tex:6961`, `main.tex:6993`, `main.tex:7058`.

## D0 Claim Status

- Strengthened: the \(D_0\)-certificate now explicitly includes a cofinal
  target-window schedule and compatible finite null-trivializations.
- Weakened in the correct place: no relation is asserted between HN height
  and automorphic target height.
- Rejected: any inference from \(\Delta_5\), the denominator algebra, or
  the OP scalar square to a compact source object.
- Preserved: conditional use of \(D_0\) in the Dirac-Pfaffian theorem.

## Commands Run

- `git status --short --branch`: confirmed
  `agent/igusa-fourth-d0-20260428`; observed pre-existing uncommitted
  changes in `compute/verify_square_root.py`, `main.tex`, and older
  untracked notes.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.texcheck-fourth-d0 main.tex`:
  passed as a one-pass TeX syntax check.  Expected undefined references
  and citations remain because BibTeX and reruns were not invoked.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" .texcheck-fourth-d0/main.log`:
  no fatal TeX hits.
- `rm -r .texcheck-fourth-d0`: removed generated check artifacts.
- `git diff --check`: passed.
- `git diff --cached --check`: passed after staging.

## Files Changed

- `main.tex`
- `notes/fourth_d0_attack_heal_report.md`

Staged paths:

- `main.tex`
- `notes/fourth_d0_attack_heal_report.md`

## Residual Obligations

The deciding evidence for \(D_0\) remains construction of the finite
compact stages \(D_{0,R}\), source observable shadows
\(\mathcal F_R^{D_0}\), transition maps and null-trivializations,
orientation quotient trivializations, normal-ordered cyclic descent,
Pfaffian line, first-order operator/algebra, compact parity pieces, and
support/parity/leading residual vanishing on the cofinal test windows.
Until those data are supplied, \(D_0\) is a conditional certificate, not a
theorem of compact existence.
