# Fifth Attack-Heal Swarm -- 2026-04-28

This ledger records the fifth adversarial swarm topology.  The manuscript
remains standalone and must not refer to this file.

## Main-thread integration rule

The main worktree is the integration owner.  Agent outputs are evidence,
not authority.  A worktree is mergeable only when its strongest true
mathematical content is represented in `main.tex` or its false claim is
explicitly rejected.  No agent may infer compact source constructions
from the determinant, the scalar OP square, or target-side current
envelopes.

## Worktrees

| Agent | Worktree | Branch | Primary obligation |
|---|---|---|---|
| H01 | `/tmp/igusa-fifth-d0` | `agent/igusa-fifth-d0-pf-20260428` | finite-stage `D0`, Pfaffian line, compact parity pieces |
| H02 | `/tmp/igusa-fifth-orientation` | `agent/igusa-fifth-orientation-weyl-20260428` | strong reduced orientation `(O1)` and Weyl cocycle `(O1)+` |
| H03 | `/tmp/igusa-fifth-o2` | `agent/igusa-fifth-o2-walls-20260428` | geometric Pfaffian local model `(O2)` on type-II walls |
| H04 | `/tmp/igusa-fifth-hybrid` | `agent/igusa-fifth-hybrid-real-20260428` | real hybrid local/wrapped factorization object |
| H05 | `/tmp/igusa-fifth-chain-koszul` | `agent/igusa-fifth-chain-koszul-20260428` | chain normal-ordering and Koszul source coalgebra |
| H06 | `/tmp/igusa-fifth-recognition` | `agent/igusa-fifth-recognition-pbw-20260428` | primitive recognition, radical quotient, no-extra-relations, PBW |

Each worktree was seeded from `master` plus the current uncommitted
tracked patch to `main.tex` and `compute/verify_square_root.py`, then
given the current `notes/` and `refs/` context.

## Required reports

- `notes/fifth_d0_pf_attack_heal_report.md`
- `notes/fifth_orientation_weyl_attack_heal_report.md`
- `notes/fifth_o2_walls_attack_heal_report.md`
- `notes/fifth_hybrid_real_attack_heal_report.md`
- `notes/fifth_chain_koszul_attack_heal_report.md`
- `notes/fifth_recognition_pbw_attack_heal_report.md`

## Acceptance standard

Every worker must return:

- stable core or no stable core;
- valid attacks with file anchors;
- repairs inscribed, if any;
- exact formulas/constants;
- verification commands and results;
- remaining open questions.

Severity-1 through severity-3 attacks must be healed, refuted, or kept
outside the stable core before the main thread declares convergence.

## Integration result

All six fifth-swarm reports were copied into `notes/` and their stable
content was semantically merged into `main.tex` and
`compute/verify_square_root.py`.

- H01 `D0/Pfaffian`: merged the cofinal discrete HN subsystem
  `mathcal R`, successor transition defects, finite operator
  `mathfrak D_{X,R}`, finite Pfaffian square data, and the finite
  `K_0` Pfaffian-shadow obstruction.
- H02 `Orientation/Weyl`: merged the separation of (O1) from (O1)+, the
  zero finite-stabilizer `H^1(BE[N];F_2)` character requirement, and the
  Weyl quotient-orientation obstruction lemma.
- H03 `O2 walls`: merged the local obstruction certificate requiring
  three equivariant charts, reduced self-Ext splittings, invariant
  Pfaffian units, and rank-one normal-mode computations.
- H04 `Hybrid`: merged quotient and protected-integration transition
  residuals and the no-quotient-first hybrid repair corollary.
- H05 `Chain/Koszul`: merged the coaugmented finite source coalgebra,
  finite filtration, collision coproduct, coassociativity, counit,
  conilpotence, and transition-continuity defects.
- H06 `Recognition/PBW`: merged the finite \(W_{\le3}\) primitive
  recognition window and the general monic `D_5/(qrs)^{1/2}` coefficient
  engine with the next timelike additive checks
  `90,90,90,-540`.

The fifth swarm did not prove the compact source exists.  Its stable
outcome is stronger: every surviving assertion now says exactly which
finite source data, obstruction classes, pairing/radical/PBW diagrams,
and local wall computations must be supplied before the Dirac-Igusa
certificate can be declared constructed.
