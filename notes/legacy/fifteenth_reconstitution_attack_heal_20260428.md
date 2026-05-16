# Fifteenth Reconstitution Attack-Heal -- 2026-04-28

## Scope

The swarm attacked the reconstituted manuscript at the compact-source
frontier: compact holomorphic \(E_3\) source, hybrid Hall convolution,
Mittag--Leffler descent, orientations, NO7, K3-to-\(E\) specialization,
primitive recognition closure, boundary assumptions, and cross-repo
consistency.

Agents were capped at six live lanes.  One early HN-side lane was closed
before returning a report; its obligation was rerun as the dedicated
Bridgeland/HN lane.  The main thread integrated by semantic merge only.

## Surviving attacks

- `A15-COMPACT-E3`: no nonempty
  \(\mathbb A^{E_3}_{X,\sigma,S}\) is constructed.  The finite interface
  must explicitly include \(S_R\), the BV bracket/Laplacian convention,
  QME/anomaly cocycles, descent cochains, finite HN quotient law, and
  transition-compatible homotopies.
- `A15-HYBRID-CONV`: finite Hall convolution remains a supplied
  certificate.  Properness/admissibility/TS vanishing, \(p\)-fiber
  finiteness, and d-critical/cosection structure on extension stacks are
  not proved.
- `A15-ML`, `A15-PUSH-KOSZUL`, `A15-RECOG-CLOSURE`: the source-bar
  consequence was too strong without derived-limit exactness.  Completed
  quasi-isomorphisms now require a Koszul Mittag--Leffler hypothesis.
- `A15-ORIENT-MONO`, `A15-O2-WALL`, `A15-BOREL-O1`: O1, O1\(^+\), and
  O2 are correctly open.  The local Pfaffian sign requires an invariant
  unit after quotient orientation trivialization, and O2/hybrid
  integration must test the full \(q^nr^ls^m\) label and transported
  Pfaffian sign.
- `A15-NO7`, `A15-HALL-KERNEL`: NO7 remains finite source data.  The
  first source test is \(W_{\le3}\), not an undefined \(R_{\min}\);
  `verify_square_root.py` verifies target arithmetic only.
- `A15-K3E-SPECIAL`: \(\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\),
  \(\kappa_E\), and \(\pi_*^{\mathrm{ch}}\) remain three distinct
  finite-stage comparison data.
- `A15-BOUNDARY`: the introduction needed an explicit smooth-scope
  sentence for \(S\) and \(E\), with singular/nodal/imprimitive/\(s=0\)
  and multi-component behavior deferred.
- `A15-SOURCE-EXP`: Borcherds exponents, GN additive coefficients, and
  the OP scalar square are not compact source multiplicities.
- `A15-CROSS-REPO`: no load-bearing conflict with the current Vol III or
  topological-strings frontier.  Vol III has separate stale/overstrong
  internal notes, not an Igusa contradiction.

## Manuscript repairs

- Front-loaded the standing smooth assumptions for the compact
  realization problem.
- Demoted the local protected observable algebra from "the compact
  \(E_3\) source" to a pre-interface schema.
- Typed the finite \(E_3\) source interface with finite BV/QME/anomaly
  witnesses, descent cochains, formality torsor choice, sectorial
  quotient law, and source/target data for
  \(\mathrm{Sp}^{\mathrm{ch}}_{K3,E,R}\).
- Softened \(\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\), \(\kappa_E\), and
  \(\pi_*^{\mathrm{ch}}\) into supplied comparison data rather than
  constructed functors.
- Added Koszul \(R^1\varprojlim=0\) exactness for the completed
  source-bar/cobar quasi-isomorphisms.
- Added \(\lim^1\)-vanishing equivalents to primitive recognition S9/R8.
- Hardened finite hybrid wording to "supplied finite charge-support HN
  quotient under [K3\(\times\)E-fin]".
- Strengthened the local Pfaffian sign proof and the O2/hybrid
  integration test.
- Clarified that `compute/verify_square_root.py` is target-only near
  \(W_{\le3}\).
- Repaired two note-level shorthand risks:
  `notes/reconstitution_plan_20260428.md` and
  `notes/attack_whitepaper_analysis_20260428_090346_guide.md`.

## Claim status

The compact source construction, finite hybrid Hall convolution,
Mittag--Leffler descent, strong orientations, NO7, and K3-to-\(E\)
specialization remain supplied/open data.  The manuscript now makes those
load-bearing gaps falsifiable without upgrading any of them to theorems.
