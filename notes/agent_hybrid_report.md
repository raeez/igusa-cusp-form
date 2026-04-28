# Agent 2 Hybrid Local/Wrapped Report

Date: 2026-04-28.

## Claim Attacked

Naive slogan: an ordinary support-local factorization object on
`Ran(E)`, possibly with a detached global Fock/Hecke factor, realizes the
full compact `K3 x E` Igusa source.

Status: false as stated.  Ordinary `Ran(E)` locality is finite-support
locality.  Positive elliptic degree has support dominating `E`, so the
wrapped sector must be global over `E` and coupled to projection-finite
insertions by mixed Hall correspondences before the reduced `E` quotient.

## Files Changed

- `main.tex`
- `notes/agent_hybrid_report.md`

## Theorem / Proof Status

Inserted a compact holomorphic `E_3` source interface as finite-first
data, not as an existence theorem.

Inserted a hybrid local/wrapped factorization certificate
`F_X^{hyb}`: hybrid `Ran(E)` strata by elliptic degree, projection-finite
local sector, wrapped prequotient sector, local-local / mixed /
wrapped-wrapped extension correspondences, two-step flag associativity,
reduced `E`-quotient order, and finite HN completion.

Inserted a scope proposition: if the finite-stage certificates and
transition maps are supplied, the object is type-correct for the
`H_X` slot and a decoupled global mode is only determinant-level unless
the mixed correspondences exist.

Updated the `H_X` clause of the Dirac-Igusa certificate to require this
source interface and hybrid certificate explicitly.

## Remaining Obstruction

The full construction remains open.  The exact obstruction is the
simultaneous construction of:

1. compact extension-closed category and stability/HN sector with finite
   type local and wrapped moduli in bounded height;
2. rigidified wrapped prequotient retaining relative `E`-position;
3. local-local, local-wrapped, and wrapped-wrapped extension stacks with
   admissible vanishing-cycle pull-push functors;
4. Thom-Sebastiani-compatible strong orientations on correspondences and
   two-step flags;
5. descent through the reduced `E` quotient, including finite-stabilizer
   gerbe checks;
6. protected integration whose scalar trace recovers the Igusa
   `s`-direction and whose primitive bracket passes the BKM presentation
   test.

## Commands Run

- `sed` reads of `CLAUDE.md`, `AGENTS.md`, required notes, skill file,
  and assigned `main.tex` regions.
- `rg` searches for `Holomorphic E_3`, `Compact holomorphic E_3`,
  `projection-finite`, `wrapped`, `Hybrid wrapped`, `H_X`,
  `mathcal F_X`, `HN`, and related labels.
- `git status --short`
- `git diff --check -- main.tex`
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp main.tex`

The LaTeX syntax pass succeeded.  It was a single pass to `/tmp`, so it
reported expected unresolved citation/reference warnings and did not
touch `out/main.pdf`.
