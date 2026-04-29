# Agent 23 theorem-status taxonomy report

Date: 2026-04-29

Scope: theorem/proposition/definition/conjecture/open-problem labels in the
live `main.tex`, read against `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`
and the 2026-04-29 swarm reports.  This report changes no manuscript source.

Verdict: the draft is much safer than the attacked PDF, but the label system is
still too generous.  Several objects called "theorem" are really certificate
ledgers; several propositions only name an open target; several real theorems
are buried as lemmas; and row/spin appendices still look like dependencies of
the `N=1` Dirac-Igusa spine.  The final rewrite should make the label itself
carry status locally.

## Result inventory

| Block | Current anchor | Current label | Status read | Problem |
|---|---:|---|---|---|
| Local protected observable schema | `main.tex:570` | Definition | certificate/interface | Correct as a definition. It must stay conditional; it is not an `E_3` source theorem. |
| K3 index and half | `main.tex:667`, `722` | Definitions; localization lemma | constructed/imported index plus arbitrary `K_0` representative | Correct if "half" stays Grothendieck-level. Never read as Hilbert splitting. |
| Fock trace | `main.tex:743` | Lemma | constructed computation | Correct. This is an internal formal computation. |
| Normalized `K_0` determinant | `main.tex:818`, `833` | Definition; proposition | constructed determinant package | Too low-status if this is the first main theorem. It should feed a headline determinant theorem. |
| Virtuality of square root | `main.tex:853` | Proposition | separation proposition | Correct. Keep close to determinant theorem. |
| Dirac/Pfaffian target | `main.tex:882` | Proposition | open target specification | Too strong. It proves no proposition; it names the missing first-order object. |
| Type-II local sign certificate | `main.tex:920`, `966`, `1054` | Definition; proposition; conditional theorem | certificate plus conditional finite computation | Mostly correct, but should live in orientation appendix. |
| Conditional Dirac/Pfaffian normalization | `main.tex:1139` | Theorem | conditional theorem with many supplied data | Honest but overlarge. Split into supplied-data definition, Pfaffian comparison implication, sign-character implication, scalar-shadow corollary. |
| Orientation line | `main.tex:2472` | Definition | open datum | Correct. It constructs no line. |
| BGN determinant identification | `main.tex:2530` | Proposition | imported theorem application | Too low-status for main spine. Combine with determinant into an imported/constructed theorem. |
| Borcherds weight identity | `main.tex:2601` | Proposition | imported/check | Correct as proposition or imported lemma. |
| D6-D2-D0 Mukai-Gram dictionary | `main.tex:2661` | Lemma | constructed theorem | Too weak. This is a main bridge theorem. Promote. |
| Reduced scalar quotient integration | `main.tex:2760` | Proposition | imported scalar integration statement | Correct. It refuses Hall/CoHA content. |
| Protected D-brane index | `main.tex:2801` | Conjecture | physical conjecture | Correct. Do not promote. |
| Protected Hall integration criterion | `main.tex:2817` | Definition | criterion/interface | Correct. Could be titled "criterion", not theorem. |
| Orientation gerbe/descent package | `main.tex:2848-4305` | lemmas/propositions/corollaries/open problem | criteria and obstruction ledger | Correct content, wrong placement. Appendix. |
| Formal Mukai/Gram lattice | `main.tex:4316`, `4489` | Definitions | constructed formal definitions | Correct, but avoid `phys` except as deprecated alias. |
| Primitive formal lift | `main.tex:4523` | Lemma | constructed formal lattice lemma | Correct. Explicitly not support/nonemptiness. |
| Gram defect and `B` cocycle | `main.tex:4590`, `4614` | Lemmas | constructed theorem-level formal algebra | Too low-status. This is core new formal mathematics. Promote or fold into normal-ordering theorem. |
| Normal-ordered extension | `main.tex:4832`, `4863` | Definition; lemma | constructed formal degree group | Correct. Make main-spine. |
| Raw Gram descent no-go | `main.tex:4883` | Theorem | constructed obstruction theorem | Correct status. Rename and define raw pushforward first. |
| Denominator algebra | `main.tex:5590`, `5614` | Definition; theorem | imported GN denominator theorem | Correct as imported theorem. Keep main. |
| Formal current envelope | `main.tex:5724`, `5743` | Definition; proposition | formal target envelope | Correct content, dangerous label alias `thm:factorization-square-root`. Rename as target current envelope. |
| Holomorphic `E_3` source interface | `main.tex:5770`, `6024`, `6192`, `6234`, `6281` | Definitions/propositions/corollary | source certificate and obstruction zero-locus | Mostly correct if all nonemptiness is denied. Move ledger to appendix. |
| Chiral Koszul source certificate | `main.tex:6506`, `6731`, `6866`, `6970` | Definition/proposition/corollary/proposition | source certificate | Appendix or compressed main summary. Target bar-cobar does not construct source. |
| Hybrid wrapped source | `main.tex:7039`, `7121`, `7970`, `8051`, `8083`, `8254` | definitions/propositions/open problem | certificate and open object | Correct status. Main gets only the obstruction statement; full certificate appendix. |
| Normal-ordering cochains | `main.tex:8305`, `8348`, `8460`, `8603`, `9132`, `9654` | open problem, definitions, lemmas, theorem, propositions | conditional source-side finite diagrams | Correct if theorem remains explicitly conditional. Appendix except core lattice theorem. |
| Sectorial Hall truncation | `main.tex:9887`, `9929` | Definition; lemma with `prop:` label | conditional finite quotient criterion | Environment-label mismatch. It is a conditional lemma/criterion. |
| First-order `D_0` certificate | `main.tex:9973`, `11518` | Definition; theorem | certificate theorem/status ledger | Honest but ledger-like. Do not let it read as existence. |
| Dirac-Igusa realization certificate | `main.tex:11750` | Definition | certificate/future construction | Correct. Must not be called constructed compact realization. |
| Primitive recognition | `main.tex:12124` | Theorem with multiple labels | conditional certificate theorem | Correct only because title says no source construction. Dangerous aliases remain. |
| Cofinal primitive certificate | `main.tex:12479`, `12590` | Definition; proposition | finite-window criterion | Correct. Appendix/detail. |
| Determinant forgetfulness | `main.tex:12804`, `13652` | Propositions, one with `thm:` label | separation propositions | Correct content; fix theorem-style labels. |
| OP scalar square | `main.tex:13806` | Theorem | imported scalar theorem | Correct. Main, late. |
| OP branch and square-root consequence | `main.tex:13857`, `13885` | Definition; proposition | normalization plus scalar-shadow consequence | Correct if never used for orientation. |
| Coefficient synthesis | `main.tex:14031` | Theorem | mixed theorem/status ledger | Too broad. Split theorem from ledger; remove row dependency from closure. |
| Physical-host certificate for rows | `main.tex:14289` | Definition | certificate ledger | Correct. Appendix or independent row section. |
| Clery-Gritsenko | `main.tex:14339` | Theorem | imported classification theorem | Correct imported theorem, but independent of main spine. |
| Eight formal current rows | `main.tex:15348` | Proposition with `thm:` label | formal row-current construction | Content OK; `thm:` alias too strong. |
| GN/Govindarajan row theorems | `main.tex:14986`, `15470` | Theorems | imported denominator-row theorems | Correct if source-anchored. Appendix/row ledger. |
| Spin `L`-factor | `main.tex:14575` | Theorem/propositions | independent arithmetic import/computation | Not a dependency. Companion note or appendix with explicit independence. |

## Required status label

Use the following taxonomy in the final rewrite.

| Taxonomy label | Meaning | Permitted examples |
|---|---|---|
| Constructed theorem | Proved in the paper from displayed definitions or explicit calculation. | Fock trace; `K_0` determinant after BGN import; D6-D2-D0 Mukai-Gram dictionary; normal-ordered extension; raw no-go. |
| Imported theorem | A cited theorem gives the mathematical result; the paper only fixes normalization and variables. | Borcherds-Gritsenko-Nikulin product/denominator; Oberdieck-Pixton scalar square; Clery-Gritsenko classification; Govindarajan row denominators; Andrianov factorization. |
| Internal computation | Local arithmetic, coefficient, sign, or group-cohomology calculation whose scope is explicit. | Maass reflection values; first timelike counts; `E[2]` and even `E[N]` residuals; coefficient checks. |
| Conditional theorem | A genuine implication from explicitly supplied data. Title must begin `Conditional` or the first sentence must say "Suppose ... is supplied." | Conditional Dirac/Pfaffian normalization; finite type-II local sign; normal-ordered Hall descent; primitive recognition certificate. |
| Certificate | A finite list of data plus residuals. It may be a definition, not an existence theorem. | `D_0` certificate; compact `E_3` source interface; physical-host row certificate; Dirac-Igusa realization certificate. |
| Criterion | Necessary-and-sufficient or one-way test for a certificate entry. | Brauer parity criterion; Klein-four criterion; finite normal-ordering closure criterion; finite Pfaffian window obstruction. |
| Definition | Introduces notation or a data package. No proposition-level conclusion. | Formal current envelope; OP normalization branch; Gram-index notation; normal-ordering coefficient dg category. |
| Open problem | Missing construction, not a hidden hypothesis in a theorem. | Compact source, hybrid wrapped sector, orientation monodromy, normal-ordered bracket descent, state-side `D_0`, row physical hosts. |
| Future program | Construction-first objects not yet in `main.tex`. | `D^{alg}_{\Delta_5,C,L}`, `H_X^{pre}`, `H_X^{tw}`, source coalgebra from compact hybrid source. |
| Appendix ledger | Useful audit material that is not a dependency of the `N=1` theorem. | Full O1/O1+/O2 obstruction algebra, finite source residuals, eight-row row atlas, spin `L`-factor. |

## Rename/demotion/promotion actions

1. Promote `main.tex:818-853` plus `main.tex:2530` to one main theorem:
   `Normalized K_0-determinant form of the Gritsenko-Nikulin product`.
   The theorem should say exactly:
   \[
   \mathcal D_X=64q^{1/2}r^{1/2}s^{1/2}
   \prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}
   =\Delta_5.
   \]
   Status: constructed determinant package plus imported BGN product.

2. Demote `main.tex:882` from proposition to definition/open problem.
   Suggested label:
   `Definition/Open Problem. Dirac-Pfaffian first-order target; no operator constructed.`
   It names \(\mathfrak D_X\); it does not prove that \(\mathfrak D_X\) exists.

3. Split `main.tex:1139` into smaller labels.
   - Definition: supplied data `(D0)`, `(O1)`, `(O1+)`, `(O2)`.
   - Conditional theorem: if all supplied data and \(\iota_{\mathrm{aut}}\) exist, the Pfaffian equals \(\Delta_5\).
   - Conditional corollary: the orientation character restricts to the Maass character.
   - Proposition: scalar trace is the OP scalar branch only after the supplied first-order object exists.

4. Move `main.tex:920-2381` and `main.tex:2848-4305` to an orientation appendix.
   Main text keeps the data names, the six automorphic reflection values, and the statement that O1/O1+/O2 are open compact Hall data.

5. Promote `main.tex:2661` from lemma to theorem.
   Title:
   `D6-D2-D0 Mukai-Gram dictionary`.
   This is the local bridge
   \[
   v_X(I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
   \quad
   \Pi_X(Q_Y,P_Y)=(\beta^2/2,n,d-1).
   \]
   It is theorem-level because it fixes the OP/DT variables against the Gram variables.

6. Promote/fold `main.tex:4590-4881` into the main normal-ordering theorem.
   Suggested title:
   `Normal-ordered Gram descent`.
   Include \(\widehat\Gamma_X\), \(\star\), \(\overline\Pi_X\), the split section \(s(c)=(c,\Pi_X(c))\), and the flag formula
   \[
   (c_1,0)\star\cdots\star(c_k,0)
   =
   \left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right).
   \]

7. Rename `main.tex:4883`.
   Current title is acceptable but less precise. Preferred:
   `Raw homogeneous Pi_X-pushforward cannot realize the type-II real-root strings`.
   Define the raw homogeneous fixed-lift pushforward before the theorem.

8. Rename `main.tex:5743`.
   Current proposition is safe, but `\label{thm:factorization-square-root}` is unsafe.
   Use:
   `Proposition. Formal denominator current envelope`.
   If expanded, define `Den^{alg}_{\Delta_5,C}` and `Den^{alg}_{\Delta_5,C,L}` for a smooth curve \(C\).  Keep this target-side.

9. Keep `main.tex:6024`, `6192`, `6234`, `6281` as definitions/propositions/corollaries only after adding a nonemptiness warning at each use.
   Any title containing `construction protocol` must say "protocol from supplied data", not "construction".

10. Reclassify `main.tex:11518`.
    Keep the content as a `D_0 certificate theorem` or `status theorem`, preferably in an appendix.  It should not be the main theorem of the paper.

11. Keep `main.tex:12124` conditional, but delete dangerous aliases.
    The safe title is:
    `Primitive recognition certificate theorem; no source construction`.
    Drop or rename aliases like `thm:microscopic-hall-drinfeld-criterion` unless an actual microscopic Hall object has been constructed.

12. Demote `main.tex:14031` from theorem to final theorem-status ledger, or split it.
    The determinant, normal-ordering theorem, denominator theorem, and OP square are separate results.  The coefficient synthesis is a dependency table and claim-strength summary.  It should not silently package open compact realization and row extensions into one theorem.

13. Rename the row part at `main.tex:14267`.
    Use:
    `Independent diagonal-divisor denominator row ledger`
    or
    `Diagonal-divisor rows and required certificates`.
    Do not use `CHL boundary physics` in a title unless a physical host is constructed.

14. Move the spin `L`-factor block `main.tex:14558-14686` to a companion arithmetic note unless a main theorem cites it.
    If retained, its section title must include `independent arithmetic normalization`.

## Main-spine labels

The main paper should have only the following theorem spine.

1. `Theorem. Normalized K_0 determinant and Igusa square-root product.`
   Status: constructed `K_0` determinant plus imported BGN product.

2. `Theorem. D6-D2-D0 Mukai-Gram dictionary.`
   Status: constructed local calculation.

3. `Theorem. Normal-ordered Gram descent.`
   Status: constructed formal lattice theorem.

4. `Theorem. Raw homogeneous Pi_X-pushforward obstruction.`
   Status: constructed no-go theorem.

5. `Theorem. Gritsenko-Nikulin denominator algebra identity.`
   Status: imported denominator theorem with the paper's normalization.

6. `Proposition/Theorem. Formal denominator current envelope.`
   Status: target-internal formal construction.  It is not the compact source.

7. `Open Problem. Compact Dirac-Igusa source and Pfaffian realization.`
   Status: open compact Hall/factorization construction, with short certificate list.

8. `Theorem. Reduced DT/PT/OP scalar square.`
   Status: imported scalar theorem.  It sees \(D_5^2\), not the first-order object.

9. `Theorem-status ledger.`
   Status: summary table, not a theorem proving new claims.

The row and spin material must not appear in this dependency chain.

## Appendix labels

Use appendices as ledgers, not as hidden proof dependencies.

| Appendix | Contents | Allowed labels |
|---|---|---|
| Maass multiplier and automorphic signs | Generator computations, six reflection values, divisor orders | imported/computed propositions and remarks |
| Orientation gerbes and Pfaffian wall signs | O1/O1+/O2, quotient gerbes, `E[N]`, wall charts, local signs | definitions, criteria, conditional computations, open problem |
| Compact-source residuals | `E_3` interface, hybrid wrapped source, Koszul source certificate, normal-ordering cochain diagrams, `D_0` residuals | definitions, certificate theorems, criteria, open problems |
| Primitive recognition finite windows | PBW, radical, NO7, first timelike counts, finite windows | criterion/proposition/certificate theorem |
| Row ledger | Clery-Gritsenko rows, GN/Govindarajan denominator rows, row physical-host certificate | imported theorems, definitions, open problems |
| Spin `L`-factor | Saito-Kurokawa/Andrianov arithmetic normalization | companion note; if retained, imported theorem plus internal computation |
| Boundary compatibility | `N=1` boundary checks only | appendix ledger; no row-map theorem |

## Dangerous theorem names

Ban or rename the following names/aliases unless the corresponding source object is actually constructed.

1. `Igusa square-root theorem`.
   Safe replacement: `Normalized K_0 determinant and Igusa product`.

2. `BPS determinant theorem`.
   Safe replacement: `Virtual Borcherds determinant`.

3. `Compact realization theorem`.
   Safe replacement: `Compact Dirac-Igusa realization problem` or `Dirac-Igusa realization certificate`.

4. `Recognition theorem` without `certificate` and `no source construction`.
   Safe replacement: `Primitive recognition certificate theorem`.

5. `Dirac/Pfaffian recognition target` as a proposition.
   Safe replacement: `Open Dirac-Pfaffian target specification`.

6. `factorization-square-root` as a theorem label for the formal current envelope.
   Safe replacement: `formal-current-envelope` or `formal-denominator-current-envelope`.

7. `protected-denominator-shadow` as a theorem label on a proposition about forgetfulness.
   Safe replacement: `determinant-forgetfulness` or `denominator-shadow-separation`.

8. `eight-formal-current-rows` as a theorem label when the environment is a proposition.
   Safe replacement: `formal-current-row-ledger`.

9. `microscopic-hall-drinfeld-criterion`.
   Safe replacement: `primitive-recognition-certificate` unless microscopic Hall data are built.

10. `Diagonal-divisor rows and CHL boundary physics`.
    Safe replacement: `Independent diagonal-divisor denominator row ledger`.

11. Any title that says `physical host`, `BPS object`, `operator`, or `compact source` without the words `supplied`, `certificate`, `conditional`, or `open`.

Environment-label mismatches to fix during source edits:

| Current anchor | Mismatch |
|---:|---|
| `main.tex:2024` | Remark carries `lem:imaginary-wall-orientation-extension`. |
| `main.tex:3653` | Remark carries several `lem:bmu2-*` labels. |
| `main.tex:9929` | Lemma carries `prop:sectorial-hall-truncation`. |
| `main.tex:13652` | Proposition carries `thm:protected-denominator-shadow`. |
| `main.tex:15348` | Proposition carries `thm:eight-formal-current-rows`. |
| `main.tex:15841` | Remark carries `prop:no-unbuilt-denominator`. |

These are not cosmetic.  They contaminate `\cref` output and make appendix
ledgers look theorem-level.

## Patch queue

1. Create a front "Status of results" table with four columns:
   `Object`, `Status`, `Source`, `What it does not prove`.

2. Replace the current abstract's row-heavy close with one sentence:
   "The diagonal-divisor row material is independent extension data and is not used in the `N=1` theorem."

3. Convert `main.tex:882-917` to a definition/open problem.  Remove proposition language.

4. Move the full orientation package out of the opening part.  Leave a two-page main statement of O1/O1+/O2 and a pointer to the appendix.

5. Promote `main.tex:2661-2750` to theorem and move it before scalar integration and before normal-ordering if possible.

6. Move `main.tex:4309-4977` before compact-source ledgers.  Define raw placement \(i_0(c)=(c,0)\), split section \(s(c)=(c,\Pi_X(c))\), and raw fixed-lift pushforward before the no-go theorem.

7. Replace any claim that `[B]` is "nontrivial" in ordinary cohomology with the precise statement:
   the ordinary class is zero via the quadratic primitive \(\Pi_X\), but there is no compatible linear homogeneous trivialization for raw fixed-lift descent.

8. Rename the formal current envelope and remove `thm:factorization-square-root`.

9. Compress `main.tex:5704-13700` to a main summary plus appendices.  The main text should not make the reader traverse every finite residual before seeing the theorem spine.

10. Keep OP/DT scalar square late and add a boxed sentence:
    "OP/DT proves the scalar square, not the first-order square root."

11. Convert `main.tex:14031-14265` into a final dependency ledger, not an omnibus theorem.

12. Rename the row section and add the row independence disclaimer at its first paragraph.

13. Move or quarantine the spin `L`-factor appendix.  If kept, add at the start:
    "This arithmetic normalization is independent of the Dirac-Igusa, Hall/Pfaffian, BKM, compact-source, scalar-square, and row-certificate arguments."

14. Run a label hygiene pass:
    theorem labels only on theorem environments; proposition labels only on propositions; lemma labels only on lemmas; remarks get `rem:` labels.

## Residual status checks

Before the final rewrite is called publication-grade, run these checks.

1. Source status check.
   Verify exact theorem/equation anchors for:
   Borcherds 1995, GN/GNII, Clery-Gritsenko, Oberdieck-Pixton, Oberdieck-Pandharipande, Oberdieck reduced PT, Govindarajan, Cheng-Dabholkar, Andrianov/Saito-Kurokawa if spin remains.

2. Label grep checks.
   ```
   rg -n '\\label\{thm:' main.tex
   rg -n '\\label\{prop:' main.tex
   rg -n '\\label\{lem:' main.tex
   ```
   Each hit must match its environment.

3. Dangerous title checks.
   ```
   rg -n 'Compact realization theorem|Recognition theorem|BPS determinant|CHL boundary physics|factorization-square-root|microscopic-hall' main.tex appendices
   ```
   Every hit must be renamed or explicitly quarantined.

4. Open-problem coverage check.
   The following must appear as open problems or certificate entries, not theorem conclusions:
   compact `E_3` source, hybrid wrapped sector, reduced quotient orientation, orientation monodromy, normal-ordered bracket descent, state-side `D_0`, primitive Hall recognition, row physical hosts.

5. Scalar-square separation check.
   ```
   rg -n '4096.*orientation|orientation.*4096|-4096.*Pfaffian|OP minus.*orientation' main.tex appendices
   ```
   Any hit must say the scalar constant is not orientation data.

6. Gram/additivity check.
   Search for direct Hall grading by `\Gamma_{\mathrm{gram}}` or `\Gamma_{\mathrm{ind}}`.  Every use must say this is a Gram/Fourier/root degree after normal-ordered descent, not the additive Hall charge.

7. Row-dependency check.
   The final synthesis must not list rows `F_2`--`F_8`, comparison symbols, or spin `L`-factors as dependencies of the `N=1` determinant, denominator, normal-ordering, compact-source obstruction, or OP scalar square.

8. Compute check.
   Keep `python3 compute/verify_square_root.py` as the local coefficient/regression companion for low-degree Borcherds, root-string, and first-timelike counts.  Do not upgrade its target arithmetic to a compact source computation.

9. Layout check.
   The first ten pages should expose: determinant, imported denominator target, normal-ordered charge repair, OP scalar square as second-order check, and compact realization as open.  They should not begin with residual ledgers.

10. Final build check.
   After actual source edits, run the normal TeX build and inspect `\cref` output for theorem/proposition/lemma mismatches caused by moved labels.
