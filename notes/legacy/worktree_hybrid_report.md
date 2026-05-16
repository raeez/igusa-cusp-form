# Worktree Hybrid Report

Date: 2026-04-28.
Worktree: `/tmp/igusa-agent-hybrid`.
Branch: `agent/igusa-hybrid-20260428`.

## Claim Attacked

The attacked shortcut is that ordinary support-local factorization on
`Ran(E)`, possibly with a detached global Fock/Hecke factor, realizes the
positive elliptic-degree direction of the Igusa product and supplies the
compact primitive bracket.

Status: false.  Positive elliptic degree dominates `E`; it is not a
finite-support Ran insertion.  A global factor is determinant-level
unless it acts through mixed local/wrapped Hall correspondences before
the reduced `E` quotient.

## Manuscript Changes

- Replaced `def:hybrid-wrapped-factorization-certificate` with a finite
  hybrid certificate:
  - finite HN stage `C_{sigma,S,<=R}`;
  - elliptic-degree split `b_R`, `Gamma_R^loc`, `Gamma_R^wr`;
  - projection-finite BM/vanishing-cycle local summands;
  - rigidified wrapped prequotient summands;
  - explicit local, mixed, and wrapped operation maps;
  - flag associativity equality in finite HN quotients;
  - quotient-after-correspondences operation `Q_{E,R}`;
  - protected integration `I_R^prot` with trace degree `s^{b_R}`.
- Strengthened `prop:hybrid-certificate-scope` into finite consequences
  of the certificate.
- Sharpened `op:hybrid-wrapped-factorization` to list the exact
  remaining construction gates.
- Updated the `(H_X)` clause of the Dirac-Igusa certificate so it points
  to the finite operation families, `Q_{E,R}`, and the `s`-degree
  protected integration test.

## Theorem Status

- Proved input: the locality obstruction remains
  `lem:projection-e-support-locality-obstruction`; positive elliptic
  degree cannot be a finite Ran support.
- Conditional certificate: if the finite stages and transitions in
  `def:hybrid-wrapped-factorization-certificate` are supplied, then
  `F_X^hyb := lim_R F_{X,sigma,S,<=R}^hyb` is type-correct as the
  hybrid `H_X` source object.
- Not constructed: the compact Hall category, wrapped rigidification,
  mixed extension stacks, orientations, quotient descent, protected
  integration, and primitive BKM recognition remain open.

## Attack-Heal Result

- Finite-HN stages: forced all operations to live first in
  `Gamma_{sigma,S}^{HN}(R)`, with height `>R` killed before completion.
- Wrapped rigidification: made the prequotient memory explicit and
  noncanonical; absence of such memory means the wrapped certificate is
  absent.
- Mixed correspondences: inserted operation maps for local-local,
  local-wrapped, and wrapped-wrapped convolution; a scalar global mode
  without the mixed map is insufficient.
- Quotient order: inserted `Q_{E,R}` only after extension
  correspondences, with finite-stabilizer gerbe checks.
- Flag associativity: required equality of the two parenthesized
  pull-push maps in finite HN quotients after TS transport and
  orientation signs.
- Protected integration: required homogeneous trace degree
  `s^{b_R}`; coefficient equality with `f(nm,l)` and primitive BKM
  relations remain recognition tests, not proven facts.

## Commands Run

- `sed -n` reads of `.agents/skills/chriss-ginzburg-rectify/SKILL.md`,
  `CLAUDE.md`, `AGENTS.md`, and architecture/status notes.
- `nl -ba main.tex | sed -n ...` reads around the compact `E_3` source,
  hybrid strata/certificate, and `(H_X)`.
- `rg` scans for `projection-finite`, `wrapped`, `hybrid`,
  `def:hybrid-wrapped-factorization-certificate`, `H_X`,
  `Q_{E,R}`, `I_R^{\mathrm{prot}}`, mixed correspondences, quotient
  order, and `s^{b_R}`.
- `git status --short`.
- `git diff -- main.tex`.
- `git diff --check`.
- `mkdir -p /tmp/igusa-agent-hybrid-texcheck`.
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp/igusa-agent-hybrid-texcheck main.tex`.
- `git add main.tex notes/worktree_hybrid_report.md`.

## Verification

- `git diff --check` succeeded.
- Targeted `rg -F` scans found the new finite certificate, `Q_{E,R}`,
  `I_R^{\mathrm{prot}}`, `s^{b_R}`, and `(H_X)` anchors.
- The one-pass `pdflatex` syntax check succeeded and wrote only to
  `/tmp/igusa-agent-hybrid-texcheck`.  It reported expected first-pass
  undefined citation/reference warnings because BibTeX and reruns were
  not invoked.

## Remaining Obstruction

The exact remaining obstruction is simultaneous construction of:

1. the compact extension-closed Hall category with finite-type local and
   wrapped moduli in bounded `h_S` height;
2. a rigidified wrapped prequotient retaining relative `E` position;
3. admissible local-local, local-wrapped, and wrapped-wrapped extension
   stacks with proper-support pull-push functors;
4. strong orientations and Thom-Sebastiani transport on correspondences
   and two-step flags;
5. reduced `E`-quotient descent after correspondences, including
   finite-stabilizer gerbe checks;
6. protected integration recovering the Igusa `s`-direction
   coefficientwise and primitive brackets satisfying the
   Borcherds-Kac-Moody presentation.
