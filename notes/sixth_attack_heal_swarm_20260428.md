# Sixth Attack-Heal Swarm -- 2026-04-28

Internal ledger.  The manuscript remains standalone and must not refer to
this file.

## Main-thread integration rule

The main worktree is the integration owner.  Subagents may write only in
their assigned worktrees.  Agent outputs are evidence, not authority.  A
claim enters `main.tex` only if it survives direct semantic review:
proof-grade argument, exact obstruction, explicit counterexample, or a
stronger finite certificate statement.  No worker may infer compact
source constructions from `Delta_5`, the OP scalar square, the target
current envelope, or target-side dimensions.

## Worktrees

| Agent | Worktree | Branch | Primary obligation |
|---|---|---|---|
| S01 | `/tmp/igusa-sixth-d0` | `agent/igusa-sixth-d0-construct-20260428` | construct or falsify the finite-stage `D0` Hall/Dirac object, Pfaffian line, and compact parity pieces |
| S02 | `/tmp/igusa-sixth-orientation` | `agent/igusa-sixth-orientation-construct-20260428` | prove or obstruct `(O1)` and `(O1)+`, including `E[2]`, higher even `E[N]`, and Weyl quotient cocycle |
| S03 | `/tmp/igusa-sixth-o2-hybrid` | `agent/igusa-sixth-o2-hybrid-20260428` | compute or obstruct `(O2)` wall models and construct or falsify the real hybrid source |
| S04 | `/tmp/igusa-sixth-chain-normal` | `agent/igusa-sixth-chain-normal-20260428` | construct chain-level normal ordering and kill or isolate all `Theta` obstruction classes |
| S05 | `/tmp/igusa-sixth-koszul-cobar` | `agent/igusa-sixth-koszul-cobar-20260428` | construct the Koszul source coalgebra, filtration, collision coproduct, and source-to-target cobar comparison |
| S06 | `/tmp/igusa-sixth-recognition` | `agent/igusa-sixth-recognition-presentation-20260428` | prove primitive recognition at presentation level: generators, parities, relations, Hopf pairing, radical quotient, no-extra-relations, completed PBW |

Each worktree was seeded from `master` plus the current uncommitted
tracked patch to `main.tex` and `compute/verify_square_root.py`, then
given the current `notes/` and `refs/` context.

## Required reports

- `notes/sixth_d0_construct_attack_heal_report.md`
- `notes/sixth_orientation_weyl_attack_heal_report.md`
- `notes/sixth_o2_hybrid_attack_heal_report.md`
- `notes/sixth_chain_normal_ordering_attack_heal_report.md`
- `notes/sixth_koszul_cobar_attack_heal_report.md`
- `notes/sixth_recognition_presentation_attack_heal_report.md`

## Acceptance standard

Every worker must return:

- stable core or no stable core;
- valid attacks with file anchors;
- repairs inscribed, if any;
- exact formulas/constants;
- verification commands and results;
- remaining open questions.

For theorem-level claims, a successful worker either proves a stronger
finite construction from stated source data, finds a fatal obstruction
that must be written into the paper, or replaces a vague open obligation
by a sharper finite obstruction package.  Unsupported existence language
is not acceptable.

## Main-thread integration result

All six reports were copied into `notes/` and semantically merged into
the main worktree where the mathematical content survived direct attack.

- S01 entered as the finite Hall--Dirac atlas
  `prop:finite-d0-atlas-parity-obstruction` and the sharpened
  `D0` open obligations.  No compact `D0` construction was claimed.
- S02 entered as the finite-stabilizer obstruction to `(O1)`, the
  semidirect Weyl/orientation transport obstruction, and the explicit
  higher even `E[N]` character residuals.  No scalar character was allowed
  to prove finite quotient linearization.
- S03 entered as `prop:o2-hybrid-compatibility-obstruction`, forcing the
  three type-II Pfaffian wall models to come from the same finite hybrid
  correspondence system, with the `delta_2` wall exposing the positive
  elliptic-degree wrapped obstruction.
- S04 entered as the formal-vs-geometric distinction for
  \(\Theta_{\Pi,R}\) and the finite verification diagrams `(NO1)--(NO7)` for
  topological, Hochschild, triple, Jacobi, Frobenius, cyclic, and radical
  normal-ordering defects.
- S05 entered as the canonical finite source-bar coalgebra conditional on
  the supplied hybrid source, plus the remaining source-to-target cobar
  obstruction.  Target bar--cobar data still cannot define the compact
  source.
- S06 entered in `main.tex` and `compute/verify_square_root.py` as the
  height-four signed residual checks `108|90|18`, doubled isotropic
  checks `10|9|1`, and real-string exponent tests.

## Verification

Commands run in the main worktree after sixth integration:

- `git diff --check`
- `python3 compute/verify_lattice.py`
- `python3 compute/verify_square_root.py`
- `python3 -m py_compile compute/verify_square_root.py`
- `make`
- `rg -n -i "undefined|multiply defined|fatal|error|warning|rerun" out/main.log`

Results:

- Whitespace diff check passed.
- Lattice verification passed.
- Square-root verification produced the new height-four, doubled
  isotropic, and real-string checks.
- `make` built `out/main.pdf`.
- The log scan reported only package/rerun infrastructure and `amsrefs`
  style warnings; no undefined references, TeX errors, or fatal errors
  were reported.
