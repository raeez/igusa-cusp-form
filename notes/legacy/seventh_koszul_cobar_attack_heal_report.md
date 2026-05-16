# Seventh Koszul/Cobar Attack-Heal Report

Date: 2026-04-28.
Role: S7-K.
Worktree: `/tmp/igusa-seventh-koszul`.
Branch: `agent/igusa-seventh-koszul-cobar-20260428`.

## Claim Attacked

Obligation (7) asks for the source Koszul coalgebra after the hybrid
source, then for the source-to-target cobar comparison where the current
inputs permit it.  The dangerous shortcuts are:
\[
\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E,\le R}),
\qquad
\Omega_E^{\mathrm{ch}}\bar B_E^{\mathrm{ch}}
(\mathsf{Den}_{\Delta_5,E,\le R})\to
\mathsf{Den}_{\Delta_5,E,\le R}
\]
as definitions of compact source coalgebra data, and the weaker shortcut
that the source bar construction alone proves the cobar
quasi-isomorphism to the denominator target.

Status: false.  The stable core is conditional source construction after
the hybrid certificate.  The target-internal counit remains target-only.

## Attacks

- `A7-K-01` finite length/conilpotence attack: valid.  A finite HN
  support does not by itself bound bar length if a non-vacuum zero-height
  colour survives.  The source-bar theorem now requires a supplied
  integer \(N_R\), equivalently positivity of HN height on every
  non-vacuum colour in the reduced bar construction.
- `A7-K-02` collision coproduct coassociativity attack: conditionally
  healed.  The cut coproduct is coassociative only after the hybrid
  eight-word flag coherences and four-input pentagon have been supplied.
- `A7-K-03` transition attack: valid.  The transition maps are now
  explicitly
  \(\rho^{\mathrm{bar}}_{R'R}=
  \bar B_E^{\mathrm{ch}}(\tau^{\mathrm{hyb}}_{R'R})\)
  followed by height-\(R\) truncation.  The residual
  \(\mathfrak o^{C,\mathrm{tr}}_{R'R}\) is preservation of ordered
  collision flags, quotient compatibilities, and bar length.
- `A7-K-04` source-internal bar-cobar attack: valid.  Even after
  constructing \(C^{\mathrm{bar}}_{X,R}\), the source counit
  \(\varepsilon^{\mathrm{src}}_{\mathrm{bar},R}\) is a
  quasi-isomorphism only if the supplied hybrid source is augmented and
  lies in the BD/Francis--Gaitsgory completed or coderived domain.
- `A7-K-05` source-to-target cobar attack: valid.  A map
  \(\vartheta_R:\mathcal F^{\mathrm{hyb}}_{X,\sigma,S,\le R}\to
  \mathsf{Den}_{\Delta_5,E,\le R}\) with chain, product, unit,
  transition, cone, and primitive compatibility is still external source
  data.
- `A7-K-06` target-internal inversion attack: invalid as a repair path.
  A homotopy inverse to the target counit cannot define \(C_{X,R}\),
  \(F^{\mathrm{co}}_{R,\bullet}\), \(\Delta_R^{\mathrm{ch}}\), source
  primitives, or \(\vartheta_R\).

## Repairs Made

- `main.tex`, Proposition
  `prop:canonical-source-bar-coalgebra`: strengthened the source-bar
  theorem by adding the finite bounded-length hypothesis \(N_R\), making
  the conilpotence proof depend on a real finite filtration rather than on
  implicit HN finiteness.
- `main.tex`, same proposition: defined the source transition map
  \(\rho^{\mathrm{bar}}_{R'R}\) by applying the chiral bar construction
  to the hybrid transition and then truncating to height \(R\).
- `main.tex`, Corollary
  `cor:source-bar-remaining-cobar-obstruction`: split the surviving cobar
  residual into
  \[
  \mathfrak o^\Omega_R=
  (\mathfrak o^{\varepsilon,\mathrm{src}}_R,\mathfrak o^\vartheta_R).
  \]
  The first part records source-internal bar-cobar admissibility and the
  cone of the source counit.  The second records the actual
  source-to-target quasi-isomorphism defect.
- `main.tex`, full certificate entry `(D_X)` and the open state-side
  construction problem: propagated the split residual so the final
  certificate does not hide source-internal admissibility inside the
  target comparison.

## Stable Core

Assuming the finite hybrid source is supplied with
\(\mathfrak O_{\mathrm{hyb},R}=0\), proper/admissible pull-push maps,
flag coherences, quotient-after-correspondence descent, protected
integration, and a bounded non-vacuum bar length \(N_R\), the source
coalgebra can be chosen as
\[
C^{\mathrm{bar}}_{X,R}=
\bar B_E^{\mathrm{ch}}
(\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}).
\]
Its finite filtration is bar length, its coaugmentation is the vacuum
summand, its counit is projection to the vacuum, and its collision
coproduct is deconcatenation realized by finite collision/flag pull-push
maps.  Coassociativity and counit are precisely the supplied finite flag
coherences.  Conilpotence follows because every reduced coproduct lowers
the length of each tensor branch and all surviving words have length
\(\le N_R\).

This kills
\[
\mathfrak o^C_R,\quad
\mathfrak o^{\mathrm{fil}}_R,\quad
\mathfrak o^{\mathrm{conil}}_R,\quad
\mathfrak o^{\Delta,\mathrm{ch}}_R
\]
and takes \(b_{X,R}\) to be the identity of the source bar coalgebra.

## Residuals

- Construct the finite hybrid source itself:
  \(\mathfrak O_{\mathrm{hyb},R}=0\).
- Prove the bounded non-vacuum length hypothesis, or make it part of the
  finite HN stage.  Without it the conilpotence residual survives.
- Prove transition compatibility
  \(\mathfrak o^{C,\mathrm{tr}}_{R'R}=0\).
- Prove source-internal bar-cobar admissibility:
  \(\mathfrak o^{\varepsilon,\mathrm{src}}_R=0\).
- Construct the actual source-to-target quasi-isomorphism
  \(\vartheta_R\) and prove \(\mathfrak o^\vartheta_R=0\).
- Prove primitive recognition after the closed Hopf-radical quotient.

## Commands Run

- `sed -n` reads of `AGENTS.md`, `CLAUDE.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`,
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`,
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`,
  and the attack-heal protocol.
- `git status --short --branch`.
- `rg -n` scans of `main.tex`, `proj.bib`, and the local report/material
  files for Koszul, cobar, hybrid, source, target, coalgebra, collision,
  conilpotence, and filtration anchors.
- `nl -ba main.tex | sed -n ...` reads of the compact realization,
  source-target separation, chiral Koszul source certificate, hybrid
  source certificate, full `(D_X)` entry, and open construction list.
- `sed -n` reads of prior Koszul/hybrid attack-heal reports and local
  `agent_material/*Koszul*` dossiers.
- Read-only cross-repo checks in
  `/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md` and local
  bar-cobar directories to confirm that source specialization and
  bar-cobar inversion are separate.
- `git diff --check -- main.tex notes/seventh_koszul_cobar_attack_heal_report.md`:
  passed.
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp/igusa-seventh-koszul-texcheck main.tex`:
  first attempt failed before reading the manuscript because the output
  directory did not exist and TeX could not write `main.log`; after
  `mkdir -p /tmp/igusa-seventh-koszul-texcheck`, the same one-pass syntax
  check passed.  It reported expected first-pass unresolved
  references/citations and layout warnings; no fatal TeX error occurred.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-seventh-koszul-texcheck/main.log`:
  no hits.
- `git diff --check -- main.tex notes/seventh_koszul_cobar_attack_heal_report.md`:
  passed after the report update.
- `git show HEAD:main.tex | rg -n "canonical-source-bar|source-bar-remaining-cobar|chiral-koszul-source-certificate|hybrid-wrapped-factorization-certificate|source-target-koszul-separation"`:
  no hits.  The Koszul source-bar lane is an unstaged manuscript addition
  relative to this branch base, so `main.tex` had to be staged as a file
  path rather than as an isolated hunk.
- `git add main.tex notes/seventh_koszul_cobar_attack_heal_report.md`.
- `git diff --cached --check -- main.tex notes/seventh_koszul_cobar_attack_heal_report.md`:
  passed.
- `git status --short --branch`.
- `git diff --cached --stat -- main.tex notes/seventh_koszul_cobar_attack_heal_report.md`.

## Files Changed

- `main.tex`
- `notes/seventh_koszul_cobar_attack_heal_report.md`

Staged paths:

- `main.tex`
- `notes/seventh_koszul_cobar_attack_heal_report.md`

Pre-existing dirty and untracked files were observed in this worktree and
not reverted.  `compute/verify_square_root.py` remains unstaged.
