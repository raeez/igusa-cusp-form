# Seventh D0 Source Attack-Heal Report

Date: 2026-04-28.
Role: S7-D0.
Worktree: `/tmp/igusa-seventh-d0`.
Branch: `agent/igusa-seventh-d0-source-20260428`.
Owned lane: compact finite-stage D0 Hall/Dirac source, Pfaffian line,
compact parity pieces, cofinal target windows, and direct cross-references.

## Stable Core

The strongest true finite construction is not an unconditional compact
`K3 x E` D0 object.  It is the following finite theorem:

1. A supplied finite Hall source kernel `mathfrak S_R` constructs the
   finite oriented Hall state object, pull-push product, coproduct,
   primitive bracket, normal-ordered primitive algebra, successor maps,
   and the Chevalley-Eilenberg first-order differential justified by the
   finite bracket.
2. The target exponents construct a canonical minimal finite target-window
   parity model `P^{min}_{Delta,R}`.
3. The comparison from that target-window model to actual compact source
   primitives is exactly the support/parity residual plus the
   no-hidden-cancellation condition.
4. The protected Dirac operator, Pfaffian line, source observable shadow,
   quotient orientation, and compact parity lifts remain additional finite
   Hall-Dirac atlas data.  The finite Pfaffian object constructed without
   choice is still the square-root torsor; a line is a section of it.

## Attacks

1. Valid, severity 1: the prior finite `D0` lane still began too late.
   It named a Hall-Dirac atlas, but the actual finite Hall source object
   was not constructed by formula from source geometry.  Repair:
   `main.tex:8615` defines the finite Hall source kernel and
   `main.tex:8665` constructs the finite Hall state object and operations
   by compactly supported vanishing-cycle cohomology and pull-push.

2. Valid, severity 1: "first-order" could still be read as a protected
   Dirac operator smuggled into the source.  Repair: `main.tex:8717`
   constructs only the Chevalley-Eilenberg first-order differential whose
   square is the finite Jacobi diagram; `mathfrak D_{X,R}` remains extra
   Dirac/Pfaffian atlas data.

3. Valid, severity 1: the compact parity lane had an obstruction monoid
   but no explicit finite target-window model.  Repair: `main.tex:8771`
   constructs `mathsf P^{min}_{Delta,R}` degree by degree and proves its
   exact `K_0` relation to the finite Pfaffian shadow.

4. Valid, severity 2: equality in `K_0` could still be mistaken for an
   isomorphism of compact parity pieces.  Repair: `main.tex:8792` states
   that the upgrade to an actual isomorphism with the minimal model holds
   exactly under no-hidden-cancellation.

5. Valid, severity 2: target-window cofinality could still be read as a
   source coverage theorem.  Repair: the new parity comparison restates
   active-window source coverage as a condition, not a consequence, and
   the open problem now asks first for `mathfrak S_R`.

6. Invalid as a proof route: the Borcherds product, OP scalar square, or
   denominator target still do not construct the compact Hall source,
   Pfaffian square root, protected Dirac operator, or compact parity lift.
   The manuscript keeps these outside the stable core.

## Repairs Made

- `main.tex:8615`: added `def:finite-hall-source-kernel`, isolating the
  finite source-side geometric input before target comparison.
- `main.tex:8665`: added
  `prop:finite-d0-hall-source-construction`, with explicit formulas for
  `mathcal H_R^{or}`, `m_R`, `Delta_R`, the primitive bracket, the
  normal-ordered primitive algebra, and `d_{CE,R}`.
- `main.tex:8771`: added
  `prop:cofinal-target-window-parity-model`, constructing the minimal
  finite target-window parity model and its comparison criterion.
- `main.tex:8852`: rewrote the Hall-Dirac atlas proposition so the source
  core is constructed first from `mathfrak S_R`; the full finite `D0`
  stage still requires Dirac/Pfaffian data.
- `main.tex:9113`: added the finite source construction item to the
  finite `D0` certificate theorem.
- `main.tex:10455`: updated the open `D0` state obligation to demand
  `mathfrak S_R` before the full finite Hall-Dirac atlas.
- `main.tex:10519`: clarified that the minimal target-window parity model
  is constructed, while identifying it with compact source primitives
  remains open.

## Residual Obligations

Construct the actual finite kernels `mathfrak S_R`: finite-type
d-critical stacks, compactly supported vanishing-cycle complexes,
extension correspondences, orientation transport, protected integration,
normal-ordering cochains acting on correspondence targets, and successor
truncation morphisms.  Then construct the finite Hall-Dirac enhancements:
source observable shadows, reduced quotient orientation trivializations,
the protected Dirac complexes `K_R^Pi`, operators `mathfrak D_{X,R}`,
Pfaffian square-root torsor trivializations, compact parity lifts, and
transition null-homotopies.  The deciding evidence is vanishing of
`mathfrak O_{D_0,R}` and `mathfrak o^{atlas}_{R^+R}` for every finite
successor stage, plus the no-hidden-cancellation theorem if the minimal
target-window parity lift is used.

## Commands Run

- Required `sed -n` reads of `AGENTS.md`, `CLAUDE.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`,
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`,
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`,
  and `references/protocol.md`.
- `wc -l` on the required control documents.
- `rg -n` searches in `main.tex`, `notes`, `agent_material`, and
  `/Users/raeez/calabi-yau-quantum-groups/FRONTIER.md` for D0, Hall,
  Dirac, Pfaffian, parity, cofinal, source, and target-window anchors.
- `nl -ba main.tex | sed -n ...` reads around the compact realization,
  finite normal-ordering, D0 definition, Hall-Dirac atlas, theorem, and
  open problem.
- `sed -n` reads of prior D0/Pfaffian attack-heal reports and architecture
  ledgers.
- One malformed `rg` regex for a CE-differential pattern failed; reran a
  fixed-string `rg -n -F "finite Hall source kernel" main.tex` successfully.

## Files Changed

- `main.tex`
- `notes/seventh_d0_source_attack_heal_report.md`

## Verification

- `git diff --check -- main.tex notes/seventh_d0_source_attack_heal_report.md`:
  passed.
- `python3 compute/verify_square_root.py`: passed; it reproduced the
  `phi_{0,1}` coefficients through `q^2`, the `93` first timelike
  coefficient, the `29|93` target presentation split, the `90/108/18`
  height-four residuals, doubled-isotropic `10|9|1` residuals, and
  real-string pairing/exponent checks.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-seventh-d0-texcheck main.tex`:
  passed as a one-pass TeX syntax check.  Undefined references/citations
  are expected because BibTeX and reruns were not invoked.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-seventh-d0-texcheck/main.log`:
  no fatal hits.
