# Agent 04: OP/DT Scalar Square And Enumerative Normalization

Scope: Oberdieck--Pixton / Oberdieck--Pandharipande / Oberdieck imports, \(\chi_{10}^{\mathrm{OP}}\), \(D_5^2\), \(-4096\Delta_5^{-2}\), scalar square versus first-order object, Behrend/reduced theory, and forbidden inference from scalar square to orientation/Pfaffian/Hall source.

## Imported Theorems

1. **Oberdieck--Pixton scalar import.** The manuscript imports Oberdieck--Pixton, *Holomorphic anomaly equations and the Igusa cusp form conjecture* (`proj.bib:249-260`), as the primitive \(K3\times E\) reduced Gromov--Witten theorem giving
   \[
   Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}
   \]
   in the OP chamber. The arXiv abstract for `1706.10100` states the broad source claim: reduced Gromov--Witten theory of \(S\times E\) is solved for classes primitive in the K3 factor, and the Igusa cusp form conjecture follows. The manuscript uses this at `main.tex:13762-13804` and `main.tex:13852-13854`.

2. **Oberdieck--Pandharipande comparison import.** The manuscript imports Oberdieck--Pandharipande, *Curve counting on \(K3\times E\), the Igusa cusp form \(\chi_{10}\), and descendent integration* (`proj.bib:262-275`), for the coordinate convention and primitive reduced GW/PT comparison. The live uses are `main.tex:13769-13783` and `main.tex:13843-13849`. This source must stay framed as an OP-variable and primitive-comparison bridge, not as a compact Hall construction.

3. **Oberdieck reduced PT import.** The manuscript imports Oberdieck, *On reduced stable pair invariants* (`proj.bib:277-288`), for two reduced \(S\times E\) statements: quotient Behrend-weighted stable-pair invariants agree with reduced virtual-class/incidence definitions, and reduced DT/PT comparison holds for nonzero K3 class. The arXiv abstract for `1605.04631` supports the broad source claim. The live uses are `main.tex:2760-2799` and `main.tex:13833-13842`.

4. **Behrend/Thomas scalar background.** The manuscript cites Thomas 2000 and Behrend 2009 (`proj.bib:290-309`) only for ordinary DT and Behrend-weighted Euler-characteristic technology. In the \(S\times E\) case, the manuscript correctly routes the scalar count through the reduced quotient-by-\(E\) theory: `main.tex:2785-2795`.

5. **What these imports do not supply.** None of the above imports supplies a compact \(K3\times E\) Hall category, CoHA product, protected primitive bracket, Pfaffian line, orientation monodromy, Weyl lift, \(E_3\)-factorization algebra, or first-order operator. The manuscript says this explicitly at `main.tex:2760-2781`, `main.tex:2817-2844`, `main.tex:10884-10917`, `main.tex:11750-11763`, and `main.tex:14247-14264`.

## Normalization

1. The paper's notation must remain:
   \[
   D_X=\Delta_5,\qquad D_5=64^{-1}\Delta_5.
   \]
   Here \(D_X\) is the theta-normalized automorphic section and \(D_5\) is the monic Borcherds product. Current anchors: `main.tex:80-81`, `main.tex:319-328`, `main.tex:14048-14060`, `main.tex:14116-14124`, `main.tex:14562-14566`.

2. OP's scalar form is:
   \[
   \chi_{10}^{\mathrm{OP}}=D_5^2=(64^{-1}\Delta_5)^2=4096^{-1}\Delta_5^2.
   \]
   Current anchors: `main.tex:13752-13759`, `main.tex:13886-13905`, `main.tex:13924-13955`, `main.tex:14116-14124`.

3. Therefore:
   \[
   Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}
   =-4096\,\Delta_5^{-2}.
   \]
   With Oberdieck reduced DT/PT and the primitive OPand comparison:
   \[
   Z^X_{\mathrm{DT}}(T,Q,P)=Z^X_{\mathrm{OP}}(P,Q,T)
   =-4096\,\Delta_5^{-2}.
   \]
   Current anchors: `main.tex:13806-13855`, `main.tex:13857-13883`, `main.tex:14111-14133`.

4. The constant decomposes as
   \[
   -4096=(-1)_{\mathrm{OP}}\cdot64^2.
   \]
   The \(64^2\) is the squared theta-to-monic conversion. The leading minus is the OP scalar convention. It is not an enumerative degeneracy, anomaly, orientation sign, Maass character, or square-root datum. Current anchors: `main.tex:127-129`, `main.tex:330-337`, `main.tex:13868-13876`, `main.tex:13937-13954`, `main.tex:14123-14124`.

5. The OP theorem sees \(D_5^2\), not \(D_5\). It confirms the scalar square in the reduced enumerative theory. It does not select the automorphic square root as an oriented Pfaffian object. Attack-analysis anchors: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:390-442`, `:5665-5687`, `:7512-7540`.

## Forbidden Inference

1. **Scalar to orientation.** Forbidden:
   \[
   Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}
   \quad\Longrightarrow\quad
   \epsilon_o=\nu_{\Delta_5}.
   \]
   A scalar prefactor is a number. \(\epsilon_o\) and \(\nu_{\Delta_5}\) are characters. The scalar square forgets the sign character. Current anchors: `main.tex:100-115`, `main.tex:211-213`, `main.tex:14168-14179`; attack anchors: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:5131-5180`, `:8666-8782`, `:12980-13085`.

2. **OP minus to Hall sign.** Forbidden: using the OP leading minus as the Hall/Pfaffian orientation convention. The OP minus may be compatible with a later reduced parity convention, but it is not evidence for it. Current anchors: `main.tex:13937-13954`; attack anchors: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:5131-5180`, `:7512-7540`.

3. **Behrend scalar integration to CoHA.** Forbidden: treating quotient Behrend-weighted Euler characteristic as a Hall product, CoHA integration map, primitive projection, or orientation character. The manuscript correctly says it lands in numbers coefficientwise. Current anchors: `main.tex:2760-2781`, `main.tex:2817-2844`.

4. **Square to Pfaffian.** Forbidden: "choose a branch of \(\Delta_5^2\)" as the construction of the Igusa square root. The Dirac formulation requires a first-order protected algebra/Pfaffian object whose scalar shadow is the OP square. Current anchors: `main.tex:100-115`, `main.tex:11750-11766`; attack anchors: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:1888-1995`, `:2770-2868`.

5. **Signed multiplicity to Hall source.** Forbidden: using the determinant, denominator, or scalar square to infer parity dimensions, primitive representatives, bracket constants, PBW, or Hopf radical. Current anchors: `main.tex:13603-13650`, `main.tex:13652-13699`, `main.tex:12390-12429`, `main.tex:12522-12588`, `main.tex:14180-14192`.

6. **Gram triple to additive Hall grading.** Forbidden: grading the compact Hall category directly by \(\Gamma_{\mathrm{gram}}\) or \(\Gamma_{\mathrm{ind}}\). The Hall source must be graded upstairs by an additive physical/formal charge lattice; the Gram map is quadratic and needs the normal-ordered extension. Current anchors: `main.tex:131-155`, `main.tex:14062-14085`, `main.tex:11768-11783`; attack anchors: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:1160-1315`, `:1594-1665`, `:1765-1825`.

7. **OP chamber to chamber independence.** Forbidden: assuming a future compact Hall source in an arbitrary stability chamber has the OP scalar branch without wall-crossing compatibility. Current anchor: `main.tex:10836-10857`.

## Replacement Language

Use this language where the paper risks over-inference:

1. "The OP theorem sees \(D_5^2\), not \(D_5\). It proves the reduced scalar square, not the first-order square root."

2. "The reduced OP/DT branch is an orientation-forgetful scalar check on a supplied first-order object. It is not an input constructing the Hall source, Pfaffian line, or primitive recognition data."

3. "The leading minus is a scalar convention of the OP/DT branch. It may be compatible with a later reduced parity convention, but it is not evidence for the reflection character \(\epsilon_o\). The reflection character must be computed from orientation-line monodromy."

4. "A scalar square is not square-rooted by choosing an analytic branch. It is square-rooted, in the Dirac sense, by constructing a first-order protected algebra whose Pfaffian/determinant is \(\Delta_5\)."

5. "The compact Hall category, if constructed, is graded by the supplied additive algebraic/effective charge support. The Borcherds variables are its Gram shadow after normal-ordered descent."

6. "Oberdieck's reduced quotient theory produces coefficientwise Behrend-weighted numbers. A protected Hall/CoHA refinement would require extension-closed compact sectors, oriented critical correspondences, vanishing-cycle coefficients, HN-finite completion, primitive projection, wall-crossing compatibility, and Weyl orientation lift."

## Current Anchors

1. **Abstract and introduction already carry the right separation.** The abstract says the OP/DT branch is orientation-forgetful and that the compact first-order object is open: `main.tex:100-129`. The introduction says the OP/DT equality is a check on the square of a supplied first-order Pfaffian object, not a Hall/Pfaffian input: `main.tex:194-213`.

2. **Claim-strength ledger is correct.** It marks the scalar OP/DT square as imported/check and excludes \(\mathfrak D_X\) and \(\epsilon_o\): `main.tex:390-445`.

3. **Reduced scalar quotient integration is correctly typed.** It is coefficientwise Behrend-weighted quotient integration and not Hall/CoHA/orientation: `main.tex:2760-2799`. The Hall refinement criterion lists the missing data: `main.tex:2817-2844`.

4. **The Pfaffian window obstruction blocks over-inference.** Automorphic input alone gives a finite \(K_0\)-Pfaffian shadow, not a compact Hall object, Pfaffian line, or first-order operator: `main.tex:10860-10917`.

5. **The Dirac--Igusa certificate blocks source reconstruction.** The certificate is not a consequence of the Borcherds product, scalar OP square, target current envelope, target bar--cobar counit, or orientation-line existence alone: `main.tex:11750-11763`.

6. **The determinant and denominator forget structure.** The manuscript explicitly says the denominator determines signed integers only, not parity dimensions or brackets: `main.tex:13603-13650`. It says the determinant only remembers a \(K_0\)-class: `main.tex:13652-13699`.

7. **The OP normalization section is mostly healed.** It fixes variables, chamber, \(\chi_{10}^{\mathrm{OP}}=D_5^2\), and \(-4096\Delta_5^{-2}\): `main.tex:13724-13855`. It also defines the OP normalization branch and excludes external scalar-square status without a source: `main.tex:13857-13883`.

8. **The square-root consequence now has the necessary caveat.** It states that a supplied Pfaffian square root may differ by a sign character and that the OP scalar does not determine it: `main.tex:13885-13922`.

9. **Constants are not orientation data.** The remark states that \(64\), \(4096\), and the OP minus sign are not Hall orientation characters: `main.tex:13924-13955`.

10. **The synthesis preserves the hierarchy.** It separates determinant, formal lattice, GN denominator, OP scalar branch, and open compact realization: `main.tex:14031-14265`.

11. **The spin \(L\)-appendix is separated.** It says OP normalization is scalar normalization of a Hecke eigenline and not a Hall/Pfaffian construction: `main.tex:14558-14686`.

12. **The boundary-row close repeats the correct rule.** The \(N=1\) row has the reduced OP scalar branch; the compact observable algebra remains the open recognition target: `main.tex:16064-16079`.

## Residual Primary-Source Checks

1. **OB exact formula check.** Verify in Oberdieck--Pixton `arXiv:1706.10100` the exact Theorem 1 statement, equation `(3)` product, equation `(56)` Laurent expansion if retained, product index chamber, and the sign in \(Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}\). Broad abstract checked; exact formula still needs paper-level audit.

2. **OPand exact comparison check.** Verify Oberdieck--Pandharipande `arXiv:1411.1514`, Section 2 and Proposition 5, for \(y=-p_{\mathrm{OP}}\), \(p_{\mathrm{OP}}=e^{iu}\), primitive \(\beta_h\), elliptically fibered \(S\) assumptions if any, and the precise GW/PT comparison used at `main.tex:13843-13849`.

3. **Oberdieck reduced PT exact theorem check.** Verify Oberdieck `arXiv:1605.04631`, Theorem 1 and Theorem 3(i), for the nonzero K3-class hypothesis, quotient-by-\(E\) Behrend-weighted Euler characteristic, reduced virtual-class/incidence equality, and reduced DT/PT comparison. Broad abstract checked; theorem hypotheses still need exact audit.

4. **Bryan convention check.** Verify Bryan `arXiv:1504.02920` for the ordinary DT vanishing due to \(E\)-action, the Hilbert-scheme normalization, the \(q/\widetilde q\) interchange, and the monic \(\chi_{10}\) convention if Bryan remains cited in the proof. Current local anchor: `proj.bib:451-462`; manuscript anchor: `main.tex:13779-13783`, `main.tex:2789-2791`.

5. **Negative-source check.** Confirm by direct source audit that none of OB, OPand, Oberdieck reduced PT, Bryan, Behrend, or Thomas constructs the compact Hall/CoHA source, Pfaffian orientation line, Weyl reflection character, or first-order Dirac--Igusa operator. The manuscript currently treats these as open; this must remain stable.

6. **Notation check.** Verify that the paper never conflates classical \(\chi_{10}\), \(\Delta_5^2\), \(\Delta_{10}^{\theta}\), and \(\chi_{10}^{\mathrm{OP}}\). The safe internal convention is:
   \[
   \Delta_{10}^{\theta}=\Delta_5^2,\qquad
   \chi_{10}^{\mathrm{OP}}=2^{-12}\Delta_{10}^{\theta}=D_5^2.
   \]

7. **Chamber check.** If a future compact Hall source is asserted, verify that its stability/HN chamber is the OP/DT chamber or that wall-crossing transport is compatible with \(\overline\Pi_X\). The current manuscript correctly marks this as separate conjectural input at `main.tex:10836-10857`.

Bottom line: the current paper mostly survives Agent 04's OP/DT attack. The surviving rule is rigid: OP/Oberdieck proves the reduced scalar square \(-4096\Delta_5^{-2}\). It does not prove the square-root orientation, Pfaffian line, or compact Hall source.
