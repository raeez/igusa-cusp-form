# Agent64 Final Residual Ledger Report

Date: 2026-04-29

Scope: proposal-only residual review of current `main.tex` against
`notes/attack_whitepaper_analysis_20260429/INTEGRATED_DECISION_LEDGER.md`.
No source edits were made.  Build was not run, because the control
instruction allowed writing only this report.

## Critique Integration Complete

1. Source/target firewall is now spine-level.
   `main.tex:94-104`, `main.tex:175-180`, `main.tex:226-229`,
   `main.tex:5826-5835`, and `main.tex:5961-5998` repeatedly state that
   the Borcherds/Gritsenko-Nikulin algebra and finite tower are target
   data, not a compact `K3 x E` Hall source.

2. The latest PDF's universal-object proposal has been demoted safely.
   The inserted section after the formal current envelope defines
   `\mathsf{DI}^{alg}_{\Delta_5,E,L;R}` as a finite algebraic
   Dirac-Igusa target reference tower (`main.tex:5889-5965`) and gives
   only a target-reference normalization (`main.tex:5967-5999`).
   The forbidden `UDI` / universal finite source language is absent by
   grep.

3. Formal Dirac blocks are separated from geometry.
   `D_gamma^2=(1-x^gamma) id` and the formal super-Pfaffian product are
   stated as finite algebraic target constructions (`main.tex:5925-5948`),
   with an explicit denial of compact Pfaffian-line, monodromy, source
   coalgebra, or primitive-recognition consequences (`main.tex:5996-5998`).

4. OP/DT scalar square is quarantined.
   The scalar theorem and normalization are imported as the
   orientation-forgetful branch (`main.tex:13977-14175`) and the synthesis
   states that `-4096 Delta_5^{-2}` does not determine the orientation
   character (`main.tex:14387-14410`, `main.tex:14446-14457`).

5. Compact realization is stated as a certificate/open problem.
   The realization functor target is now `\mathsf{Real}_{X,R}` rather than
   an `R_X` functor (`main.tex:6001-6019`).  The full compact source,
   D0-stage, Pfaffian, orientation, source coalgebra, radical/PBW, and
   primitive recognition obligations are collected as open construction
   tasks (`main.tex:11794-11936`, `main.tex:13552-13690`).

6. Static reference hygiene currently passes at the text level.
   Read-only checks found no duplicate `\label{...}` keys, no missing
   static `\ref`/`\eqref`/`\autoref`/`\pageref` targets, and no missing
   `proj.bib` keys for the simple `\cite{...}`/`\cites{...}` forms.

## Mathematically Open

1. Compact `K3 x E` Hall/Dirac source construction remains open:
   finite Hall kernels, finite Hall-Dirac atlases, quotient/orientation
   data, protected integration, and transition-compatible inverse systems
   are not constructed (`main.tex:11922-11935`, `main.tex:13561-13577`).

2. Orientation is still a gerbe/monodromy problem, not a scalar consequence:
   reduced orientation gerbes, quotient descent, Weyl transport, type-II
   Pfaffian wall signs, and the equality
   `epsilon_o = nu_Delta5` remain to be proved from compact data
   (`main.tex:2961-3242`, `main.tex:12231-12248`,
   `main.tex:13613-13629`).

3. Hybrid local/wrapped realization remains open:
   positive elliptic degree must be represented by rigidified wrapped
   prequotients, mixed local/wrapped correspondences, quotient-after-
   correspondence descent, and protected integration before the reduced
   `E` quotient (`main.tex:6570-6608`, `main.tex:7374-7428`,
   `main.tex:8515-8564`).

4. Source coalgebra and chiral Koszul comparison remain open source-side
   data.  The manuscript correctly forbids defining `C_{X,R}` from the
   target bar-cobar counit (`main.tex:6775-6789`), but the compact
   source coalgebra, bar comparison, cobar quasi-isomorphism, and
   `R^1 lim = 0` conditions remain to be built (`main.tex:13639-13670`).

5. Primitive recognition remains conditional.
   The compact source must still supply primitive representatives,
   parity dimensions, bracket constants, Jacobi/Serre checks, Hopf
   pairings, closed radicals, no-extra-relations, PBW compatibility, and
   transition exactness.  The first hard finite test is the
   `delta_1+delta_2+delta_3` channel, where `-64` must refine to compact
   `29|93` data (`main.tex:13671-13684`).

6. Eight-row boundary material remains certificate-level.
   Rows beyond the known automorphic/denominator statements do not have
   compact Hall/chiral hosts or reduced CY/DT scalar hosts unless their
   row certificates are supplied (`main.tex:14652-14781`).

## Manuscript Cleanup Remaining

1. Degree notation is mostly repaired but not clean.
   The ledger requires two separate functions: geometric elliptic degree
   `b_R^{geom}` and Borcherds trace exponent
   `m_R=pr_3 \overline\Pi_X`.  Current text still has plain `b_R` or
   "s-degree is elliptic degree" residues at `main.tex:552-559`,
   `main.tex:6794-6795`, `main.tex:7384`, `main.tex:8082`, and
   especially `main.tex:12121-12123`.  These should be normalized before
   final.  Trace degree should be `s^{m_R}`; local/wrapped splitting
   should use `b_R^{geom}`.

2. Output PDF is stale relative to `main.tex`.
   `main.tex` is timestamped 2026-04-29 19:58:54, while `out/main.pdf`
   and `out/main.log` are timestamped 2026-04-29 19:21:58.  The current
   manuscript has not been typeset after the latest patch.

3. The compact-realization section is mathematically honest but still
   reads as a long certificate/residual ledger.  This is acceptable for
   attack-heal convergence; for final manuscript form, consider moving
   some finite obstruction ledgers to appendices after the theorem spine
   is typeset and inspected.

4. The symbol `R_X` remains as the recognition component of
   `\mathfrak K_X=(L_X,H_X,O_X,D_X,R_X)` (`main.tex:12026-12040`).
   This is not the ledger's forbidden geometric functor collision, because
   the functor is now `\mathsf{Real}_{X,R}`.  Still, keep this distinction
   explicit if any prose later calls `R_X` a realization functor.

## Must Verify Before Final

1. Run `make fast`; then run full `make` if cross-references or citations
   change.  Inspect `.build_logs/main-fast.log` or pass logs for fatal
   TeX errors, undefined references, undefined citations, overfull boxes
   in the first theorem-spine pages, and stale rerun warnings.

2. Re-run grep gates after the degree cleanup:
   forbidden source claims (`universal finite Hall-Dirac source`,
   `constructed compact finite source object`, `UDI`), plain `b_R`
   residues where `b_R^{geom}` is meant, and any phrase deriving compact
   Hall/Pfaffian/orientation/source-coalgebra data from the determinant,
   denominator algebra, OP scalar square, or target bar-cobar counit.

3. Re-check the load-bearing constants and conversions:
   `[q^{1/2}r^{1/2}s^{1/2}] Delta_5=64`,
   `D_5=64^{-1} Delta_5`,
   `chi_{10}^{OP}=D_5^2`,
   `Z_OP=Z_DT=-4096 Delta_5^{-2}`,
   and `m_R=d-1` under the rank-one D6-D2-D0/OP variable convention.

4. Re-check the first wrapped wall:
   `delta_2 <-> (0,1,1)` has `m_R(delta_2)=1`; the corresponding
   geometric elliptic degree is positive and is `d=m_R+1=2` in the
   rank-one dictionary.  No projection-finite Ran-sector statement should
   claim to realize it.

5. Re-check that primitive recognition is never used before the full
   finite source certificate, Hopf radical quotient, PBW compatibility,
   source coalgebra, and Koszul completion hypotheses are invoked.

Final residual status: the integration is substantially converged on
claim strength and source/target separation.  The remaining blockers are
not new mathematical contradictions; they are the still-open compact
source theorem and a small but important degree-notation cleanup before
build/PDF verification.
