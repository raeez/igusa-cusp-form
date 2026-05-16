# Seventh O2/Hybrid Attack-Heal Report

Date: 2026-04-28.
Role: S7-H.
Worktree: `/tmp/igusa-seventh-o2-hybrid`.
Branch: `agent/igusa-seventh-o2-hybrid-20260428`.
Owned lane: O2 type-II wall Pfaffian local model and hybrid local/wrapped factorization object.

## Context Loaded

- `AGENTS.md`, `CLAUDE.md`.
- `/Users/raeez/ecosystem/INVARIANTS.md`.
- `/Users/raeez/ecosystem/AGENTS-HARNESS.md`.
- `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`.
- `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`.
- `main.tex` around O2, type-II walls, hybrid factorization, Dirac-Igusa, and open certificate lists.
- Prior reports: fifth O2, fifth hybrid, third hybrid, sixth O2/hybrid, and semantic merge audit.

## Claims Attacked

1. O2 computes a rank-one Pfaffian local model on the three simple type-II walls.
2. The hybrid object is an actual finite local/wrapped factorization object, not a slogan or detached Fock factor.
3. The O2 wall charts and hybrid wrapped source can be asserted independently.

Status: no full compact construction is present.  The stable core is finite and conditional: once the named local/hybrid residuals vanish, the finite sign and finite correspondence-module operations are computed.  The remaining construction is explicit residual debt.

## Attack Ledger

`S7-H-01` O2 supplied-versus-computed attack.  Valid.  The old text named local O2 data and a local obstruction proposition, but no stable finite theorem separated the computed sign from the supplied chart, splitting, unit, rank, and transition data.

`S7-H-02` rank/parity attack.  Valid.  Odd parity alone is weaker than the O2 certificate.  The rank-one assertion is the equality
`N_{\delta_i}^{\mathrm{Pf}}=1` on each of the three walls, not the automorphic order-one divisor.

`S7-H-03` hybrid-object attack.  Valid.  The certificate had correspondences and operations, but the finite object was still most naturally read as a tuple of data.  The repair makes it the correspondence-module functor
`\mathcal B_R^{E,\mathrm{hyb}}:\mathsf{Corr}^{E,\mathrm{hyb}}_R\to\mathrm{Ch}_{\mathbb C}`.

`S7-H-04` properness/admissibility attack.  Valid.  Pull-push maps are not operations until proper-support, admissibility, and Thom-Sebastiani witnesses vanish.  These are now named finite residuals.

`S7-H-05` quotient-first attack.  Still valid as an obstruction and still healed by the existing no-quotient-first corollary.  The new edits preserve quotient-after-correspondence order.

`S7-H-06` wrapped wall attack.  Valid.  The wall label
`\delta_2\leftrightarrow(0,1,1)` has positive `s`-degree.  It cannot be supplied by projection-finite `Ran(E)` locality.

No invalid attacks were used as repair drivers.

## Repairs Made

- `main.tex:973`: added `thm:stable-finite-type-ii-local-theorem`.  It defines the finite O2 residual
  `\mathfrak O^{\mathrm{O2}}_{\delta_i,R}` with chart, wall, split, unit, rank, and transition entries.  If it vanishes, the local normal Pfaffian is
  `\upsilon_{\delta_i,R}u_{\delta_i,R}`, reflection multiplies it by `-1`, and the squared determinant is fixed.
- `main.tex:6108`: added generator-wise properness/admissibility/Thom-Sebastiani residuals
  `\mathfrak o^{\mathrm{prop}}_{e,R}`,
  `\mathfrak o^{\mathrm{adm}}_{e,R}`,
  `\mathfrak o^{\mathrm{TS}}_{e,R}`, aggregated as LL, mixed, and WW properness residuals.
- `main.tex:6180`: defined the finite unreduced hybrid object as the correspondence-module functor `\mathcal B_R^{E,\mathrm{hyb}}`, and the reduced object as
  `\mathcal B_R^{\mathrm{red},\mathrm{hyb}}:=Q_{E,R}\mathcal B_R^{E,\mathrm{hyb}}`.
- `main.tex:6421`: inserted the properness/admissibility residuals into `\mathfrak O_{\mathrm{hyb},R}` and stated that without their vanishing the hybrid notation names an obstruction problem, not a source object.
- `main.tex:6481`: sharpened the transition residual as the joint defect of object truncation, correspondence base-change, flag/pentagon coherence, anchor compatibility, and the induced chain map.
- `main.tex:6509`: threaded properness/admissibility through the finite consequences proposition and proof.
- `main.tex:6686`: inserted the rank residual into the O2/hybrid compatibility obstruction.
- `main.tex:6738`, `main.tex:9183`, `main.tex:10409`, and `main.tex:11162`: propagated the properness/admissibility requirement into the hybrid open problem, Dirac-Igusa certificate, full-certificate list, and synthesis summary.

## Residuals

For each `i=1,2,3` and finite height `R`, O2 still requires actual construction of:

- wall objects `x_{\delta_i,R}`;
- equivariant reduced real d-critical charts and anti-invariant wall coordinates;
- reduced self-Ext complexes and tangent/normal splittings;
- invariant normal Pfaffian units;
- rank-one normal quasi-isomorphisms;
- transition null-homotopies.

The hybrid source still requires actual construction of:

- finite HN local and wrapped moduli;
- rigidified wrapped prequotients with anchors;
- all ordered local-local, mixed local/wrapped, and wrapped-wrapped extension stacks;
- proper-support, admissibility, and Thom-Sebastiani witnesses;
- eight-word flags and four-input pentagon coherences;
- quotient-after-correspondence functor `Q_{E,R}`;
- protected integration with product, coproduct, primitive, and transition residuals zero.

The combined O2/hybrid residual now also includes the rank residual
`\mathfrak o^{\mathrm{rank}}_{\delta_i,R}`.  The `\delta_2` case remains the immediate wrapped test because its Gram label has `m=1`.

## Commands Run

- `pwd`.
- `git status --short --branch`.
- `cat` reads of the required local and ecosystem instruction files.
- `rg -n` searches for O2, type-II, hybrid, wrapped, Pfaffian, quotient, properness, eight-word flags, and report anchors.
- `nl -ba main.tex | sed -n ...` reads of the O2, hybrid, Dirac-Igusa, and open-certificate regions.
- `cat` reads of prior O2/hybrid reports.
- `python3 compute/verify_lattice.py`: passed.
- `python3 compute/verify_square_root.py`: passed.
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp/igusa-seventh-o2-hybrid-texcheck main.tex`: passed as a one-pass syntax check; undefined references/citations and rerun warnings are expected without BibTeX and later LaTeX passes.
- `git diff --check -- main.tex notes/seventh_o2_hybrid_attack_heal_report.md`: passed.

Two over-escaped exploratory `rg` regexes failed; fixed-string reruns produced the intended anchors.

## Files Changed

- `main.tex`.
- `notes/seventh_o2_hybrid_attack_heal_report.md`.

`compute/verify_square_root.py` was already modified in the worktree before this pass and was not edited in this lane.
