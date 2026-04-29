# Agent66 latest-PDF consistency report

Date: 2026-04-29.

Scope: proposal-only final consistency review.  No source edits.  Compared
`main.tex` and
`notes/attack_whitepaper_analysis_20260429/INTEGRATED_DECISION_LEDGER.md`
against the latest extracted PDF window
`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:27800-30200`.

Protocol read:

- `AGENTS.md`
- `CLAUDE.md`
- `~/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`
- `~/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md`

## Verdict

Stable core: nonempty.

The current manuscript is consistent with the integrated ledger, not with the
literal strongest claims in the latest PDF window.  That is the correct
adjudication.  The latest PDF proposes a construction-first object called a
universal finite Dirac--Igusa Hall source
(`...revision-1923.txt:27848-27879`, `29517-29732`).  The ledger accepts the
construction-first order but rejects the source claim: if the object is built
from `\mathfrak g_{\Delta_5}`, `U(\mathfrak g_{\Delta_5})`, the BKM bracket,
target PBW, target radical quotient, and the GN product, it is a target
reference tower, not a compact `K3\times E` Hall source
(`INTEGRATED_DECISION_LEDGER.md:20-28`, `40-49`, `56-66`).

`main.tex` follows that decision.  It introduces
`\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L;R}` as a finite algebraic
Dirac--Igusa target reference tower, explicitly says it is not a compact Hall
source, not a geometric orientation gerbe, not a source coalgebra, and not
protected integration (`main.tex:5889-5964`).  The compact theorem is restated
as an open realization problem via `\mathsf{Real}_{X,R}` from independent
geometric source data into this target tower (`main.tex:6001-6018`).

## Integrated critique results

1. Source/target firewall from the latest `UDI` proposal.
   Integrated, with downgrade.  The PDF's `UDI_R` source language at
   `27848-27948` and `29517-29732` is replaced by a target/reference tower in
   the abstract, status tables, body definition, and open problem
   (`main.tex:83-104`, `399-408`, `5889-6018`).  Bare `UDI` terms do not
   appear in `main.tex`.

2. Normal-ordered charge repair.
   Integrated.  The PDF's formal charge algebra and raw/split/lift repair
   (`27950-28171`) appears as the normal-ordered extension, raw placement,
   splitting, additive Gram map, flag formula, and raw fixed-lift no-go
   (`main.tex:4890-5085`).  This is now a spine theorem, not a warning.

3. D6--D2--D0 degree dictionary.
   Integrated.  The manuscript promotes the dictionary to a theorem and
   proves the Gram shadow
   `\Pi_X(Q_Y,P_Y)=(h-1,n,d-1)` (`main.tex:2703-2740`).  The OP table now
   labels the `s` exponent as the Borcherds/Gram exponent `m=d-1`
   (`main.tex:13990-13998`).

4. Geometric realization functor.
   Integrated, conditionally.  The PDF's `R_{X,R}:H^{geom}_{X,R}\to UDI_R`
   proposal (`29738-29800`) is written as
   `\mathsf{Real}_{X,R}:\mathfrak H^{geom}_{X,R}\to
   \mathsf{DI}^{alg}_{\Delta_5,E,L;R}` and made an open problem
   (`main.tex:6001-6018`).  The notation avoids the `R_X` collision flagged
   by the second-wave reports.

5. OP/DT scalar-square quarantine.
   Integrated.  The PDF says the OP scalar square checks
   `-4096\Delta_5^{-2}` but does not construct orientation, Hall product, or
   primitives (`30028-30036`).  The manuscript repeats this firewall in the
   opening, dependency chain, OP normalization branch, square-root consequence,
   and constants remark (`main.tex:123-135`, `226-229`, `13977-14231`).

6. Formal Dirac block and super-Pfaffian product.
   Integrated with status downgrade.  The PDF's block
   `D_\gamma^2=(1-x_\gamma)id` and product (`29390-29515`) becomes a finite
   algebraic target-reference block/product (`main.tex:5925-5964`).  It is not
   asserted as a compact Pfaffian line theorem.

7. Chiral bar/source coalgebra firewall.
   Integrated.  The PDF's useful distinction between source-to-target cobar
   and target-internal bar-cobar (`29254-29381`) is reflected as a source-side
   certificate: `C_{X,R}` cannot be defined from
   `\bar B_E^{ch}(\mathsf{Den}_{\Delta_5,E,\le R})` or a target counit
   (`main.tex:6725-6755`, `6768-6789`, `6843-6865`).

8. Hybrid degree split.
   Mostly integrated.  The latest PDF separates
   `m_{\mathrm{Borch}}(\gamma)=m` from `b_{\mathrm{ell}}(\gamma)=m+1`
   (`29083-29096`, `30081-30084`).  `main.tex` now uses
   `m_R` for the `s` exponent and `b_R^{geom}` for wrapped support in the
   opening and main hybrid proof sites (`main.tex:264-272`, `6423-6428`,
   `7939-7995`, `8258-8277`, `8438-8455`, `14431-14441`).

## Rejected or downgraded claims

1. `UDI_R` as a constructed compact finite source.
   Rejected.  The PDF explicitly says "This is the constructed finite compact
   source object" (`29620`).  The ledger rejects this as circular
   (`INTEGRATED_DECISION_LEDGER.md:40-41`), and `main.tex` uses
   `\mathsf{DI}^{alg}` as target/reference only (`5889-5964`).

2. PBW and radical as source theorems.
   Downgraded to target structure.  The PDF's PBW/radical theorem
   (`29655-29662`) is valid only for the imported GN/Kac target.  Source PBW,
   radical kernels, and transition compatibility remain realization data
   (`main.tex:6011-6018`, `11833-11851`, `13553-13617`).

3. `Hyb_R` as an actual geometric hybrid source.
   Rejected as stated.  The PDF's finite colored PROP (`29110-29245`) is a
   useful algebraic interface, but not wrapped stacks, anchors, mixed Hall
   correspondences, quotient-after-correspondence, or protected integration.
   `main.tex` keeps the geometric hybrid object as a supplied certificate
   (`main.tex:7374-8100`).

4. `C_R=B_E^{ch}(F_R)` as source coalgebra when `F_R` is target-built.
   Rejected.  Safe only after an independent hybrid source exists.  The
   manuscript states exactly this source/target separation (`main.tex:6725-6755`,
   `6768-6789`).

5. Orientation gerbe triviality in the universal finite base.
   Downgraded.  The PDF's claim that quotient orientation is trivial in the
   universal algebraic source (`29969-29972`) is harmless only for a formal
   target convention.  Compact geometry still must supply determinant lines,
   gerbes, lifted correspondences, quotient descent, and transition coherence.

6. Minimal parity lift forced by the determinant.
   Not integrated as a theorem.  `main.tex` chooses finite super vector spaces
   with the correct signed superdimension (`main.tex:5925-5927`) but does not
   claim the determinant fixes a canonical parity split.  This matches the
   ledger's optional-convention status.

7. Machine-checkable finite data as already present.
   Rejected for current checkout.  The PDF lists degree tables, bracket
   tensors, pairing matrices, products, coproducts, PBW bases, radical
   kernels, normal-ordering tables, hybrid operation tables, and transition
   matrices (`29802-29943`).  The repository has target arithmetic scripts and
   manuscript certificates, not the claimed source data layer.

## Residual consistency defects

1. Stale `b_R` language remains.
   The hard old patterns `s^{b_R}`, `b_R(\eta)=1`, and
   `b_R(\eta_2)=1` are gone, but semantic remnants remain:
   `main.tex:6794-6795` says `b_R=0` / `b_R>0`,
   `main.tex:7384` still names the tuple entry `b_R`,
   `main.tex:8082` preserves `b_R(\gamma)=b_{R'}(\gamma')`,
   `main.tex:11262` says projection-finite source has `b_R=0`, and
   `main.tex:12122-12123` still says homogeneous `s`-degree is elliptic
   degree `b_R`.  These should be normalized to `b_R^{geom}` for support
   degree and `m_R` for the `s` exponent.

2. `A_R` is under-specified in the new target tower.
   `main.tex:5891-5915` fixes a finite cusp-positive active window, but does
   not tie it to the older target-window schedule, exclude zero, or state the
   formal-product topology.  Agent61's attack remains valid.

3. PBW finite-window wording is still slightly too strong.
   `main.tex:5911-5923` defines a PBW span by total Gram degree in `A_R`.
   That is safe as target filtration language only if the positive-half,
   letter set, and successor-window convention are made explicit.

4. First tower mention lacks local source anchors.
   The abstract's target tower paragraph (`main.tex:99-103`) and the body
   target tower (`main.tex:5889-5999`) rely on GN/Kac/BD source roles.  Agent63
   found no missing bibliography keys, but the local theorem/equation anchors
   should be inserted before final release.

## Safe high-value unintegrated ideas

1. Replace the current `A_R` sentence by a reference to the established
   cofinal finite target-window schedule, with `A_R\subset\Gamma_{act}`,
   `0\notin A_R`, positive-half PBW letters, and coefficientwise limit in the
   Borcherds cusp formal-product topology.

2. Tie `V_\gamma` either to the target root superspace
   `\mathfrak g_{\Delta_5,\alpha(\gamma)}` or label it explicitly as a
   chosen signed-dimension model.  Do not let the formal block imply a
   canonical compact parity lift.

3. Add a compact internal data-layer appendix for target/reference checks:
   degree table, bracket tensor, pairing matrix, product/coproduct tensor,
   PBW words, radical kernel, normal-ordering table, hybrid operation table,
   and transition matrices.  Label it target/mock/reference until source
   provenance exists.

4. Reuse the latest PDF's finite colored PROP idea only as a comparison
   interface.  The manuscript should continue to require geometric wrapped
   prequotients, anchors, mixed correspondences, quotient descent, and
   protected integration before calling anything a hybrid source.

5. Add a gerbe-first compact-source definition once the geometric finite
   stacks are specified.  The ordering is correct: determinant-line gerbe,
   twisted correspondences, then global orientation/trivialization as an
   additional condition.

## Static checks run

- Bare `UDI` gate over `main.tex appendices standalone`: zero hits.
- Exact old degree-conflation gate for `s^{b_R}`, `b_R(\eta)=1`,
  `b_R(\delta_2)=1`, `b_R(\eta_2)=1`: zero hits.
- Full `b_R` / `m_R` grep: residual stale semantic sites listed above.

No LaTeX build was run.  A build would update generated artifacts; this task
was proposal-only and source-edit forbidden.
