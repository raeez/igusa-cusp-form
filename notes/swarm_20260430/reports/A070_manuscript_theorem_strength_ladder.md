# A070 - Manuscript Theorem-Strength Ladder

Using `chriss-ginzburg-rectify` and supremum discipline. No edits made
by the agent.

## Controlling Ladder

| Rung | Label After Reconstruction | Hypotheses | Conclusion | Anchors / Upgrade Data |
|---|---|---|---|---|
| 0 | **Proposition: target reference tower** | finite active window `A_R`, imported GN/Kac denominator algebra, formal `V_\gamma` with `\sdim V_\gamma=f(nm,l)` | formal target Pfaffian product normalizes to `\Delta_5`; no compact source | `main.tex` near lines 5944 and 6032 |
| 1 | **Open Problem: compact realization of target tower** | none supplied | construct `\mathfrak H^{geom}_{X,R}` and `\mathsf{Real}_{X,R}` preserving Hall product/coproduct, orientation, source coalgebra, Pfaffian, primitives, PBW, transitions | `main.tex` near line 6066 |
| 2 | **Theorem from supplied retained sector datum** | retained Liu-Hilbert schedule, compactified extension/flag stacks, finite inertia, d-critical/BBDJS data, reduced orientations, six-functor admissibility | finite Hall source kernel, bialgebra, primitive bracket, normal-ordered descent | `main.tex` near line 13002. Upgrade by replacing full Liu-class `C_R` with `\Xi=(\gamma,[a,b],(P_i),N)`, closed under retained sums/subobjects/quotients/flags; A025. |
| 3 | **Criterion: finite `D_0` Hall source package** | finite Hall source kernel `\mathfrak S_R`, protected integration, `\Theta_{\Pi,R}`, bialgebra compatibility | `\mathcal H_R^{or}`, primitive bracket, CE first-order differential; not yet Dirac/Pfaffian | `main.tex` near lines 11353 and 11452 |
| 4 | **Criterion/Theorem: Dirac-Pfaffian from supplied atlas** | `D_{0,R}` atlas with `\mathfrak D_{X,R}`, Pfaffian line, support/parity lifts, leading cusp normalization | finite first-order object and Pfaffian shadow | `main.tex` near lines 11641 and 11880. Upgrade by constructing actual parity spaces, Pfaffian square-root torsor trivialization, and no-hidden-cancellation. |
| 5 | **Theorem from O1/O1+/O2 data** | `D0`, quotient orientation gerbe trivializations, Weyl cocycle killed, type-II rank-one Pfaffian wall charts, `\iota_{\mathrm{aut}}` | `\operatorname{Pf}(\mathfrak D_X)=\Delta_5`, scalar trace `-4096\Delta_5^{-2}`, `\epsilon_o=\nu_{\Delta_5}` on type-II Weyl group | `main.tex` near line 1128. Upgrade by supplying wall objects, reduced self-Ext splittings, invariant Pfaffian units, `N^{Pf}_{\delta_i}=1`, quotient linearizations; A047-A048. |
| 6 | **Theorem: source bar coalgebra from supplied hybrid source** | `\mathfrak O_{\mathrm{hyb},R}=0`, augmented finite hybrid source, bounded non-vacuum word length `N_R` | `C^{bar}_{X,R}`, filtration, conilpotent collision coproduct, bar comparison | `main.tex` near lines 6824 and 7049 |
| 7 | **Criterion: source-to-target Koszul comparison** | source bar-cobar counit is admissible quasi-isomorphism; source-to-target `\vartheta_R:\mathcal F^{hyb}_{X,R}\to\mathsf{Den}_{\Delta_5,E,\le R}` | `\Theta_{\mathrm{Kos},R}=\vartheta_R\circ\varepsilon^{src}_{bar,R}` | `main.tex` near line 7184. Upgrade via primitive matrices and `A_{\beta,\bar p}`. |
| 8 | **Theorem: primitive recognition criterion** | S1-S10: chain-level `\overline\Pi^\Theta`, Cartan, source simple representatives, BK relations, Hopf radical, no-extra-relations, generation, PBW, exact completion, full parity dimensions | `P_X^{\Pi,red}\cong\mathfrak g_{\Delta_5}`; denominator `64^{-1}\Delta_5(2Z)` | `main.tex` near line 12488. Keep as criterion until source data exist; A049-A064. |
| 9 | **Criterion: cofinal finite-window recognition** | cofinal downward-saturated windows with R1-R8 data | global recognition iff finite representatives, relations, pairing/radical, kernel equality, PBW, exact triangular completion are supplied compatibly | `main.tex` near lines 12848 and 12959 |
| 10 | **Target Proposition, not source theorem: `W_{\le3}`** | GN/Kac target arithmetic | target table `1|0,10|0,1|0,29|93`, `29-93=-64`, height-four gaps | `main.tex` near line 15004. Upgrade to source theorem only with neutral source bases and `M,D,B,G,K,Q,A_\beta`; A055-A067. |
| 11 | **Finite Matrix Recognition Criterion** | compact source bases with provenance, `M,D,B,G,K,Q,A`, kernel equality, PBW associated-graded iso, strict transitions/ML | radical descent, no-extra-relations, PBW, exact inverse limits on `W` | `main.tex` near lines 15268 and 15373 |
| 12 | **Open Problems: larger terminal windows** | `W_{\le3}` source packet plus enlarged retained windows | height-four terminal Serre/doubled-isotropic rows; height-six/seven complementary strings | A065-A066. `W_{\le3}` is not relation-closed. |

## Patch Plan

1. Rename reader-facing "construction" phrasing for the full compact
   source to **Open Problem** unless all retained finite data are
   supplied; keep the final assembly as a **conditional theorem** from
   supplied stages.
2. Strengthen `main.tex` near line 13002: replace finite full Liu classes
   by retained Liu-Hilbert schedules `\Xi`, compactified
   closed-filtration/flag-Quot correspondences, and explicit exceptional
   `q_!` alternatives.
3. Keep `main.tex` near lines 14137 and 14345 target-only. They are
   algebraic normal forms, not compact `K3 x E` source geometry.
4. Insert the A067 source fixture schema as the manuscript's finite
   certificate standard: neutral source IDs, provenance,
   `M,D,B,G,K,Q,A`, relation rows, PBW, no-extra, transitions, ML ranks.
5. After `W_{\le3}`, add explicit open problems for `W_{\le4}` and the
   height-seven complementary strings. Do not let the `W_{\le3}`
   criterion certify terminal Serre rows.

No build run; no files changed by the agent.

