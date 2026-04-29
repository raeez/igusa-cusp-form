# Agent 21 Appendix Quarantine / Compression Report

Source set: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`, live `main.tex`, `appendices/boundary_compatibility_conditions.tex`, and prior attack reports in `notes/attack_whitepaper_analysis_20260429/`.

Verdict: the manuscript is substantially more honest than earlier attacks, but the current layout is still not a theorem paper. It is a theorem spine wrapped in orientation obstruction algebra, source-construction ledgers, diagonal-divisor atlases, and an unrelated arithmetic appendix. The paper must quarantine anything not needed for the `N=1` Dirac--Igusa square-root theorem. Rows and spin data may be valuable, but they are not dependencies.

## Main-spine-only content

Keep in the main theorem spine only material that is used to state, prove, or correctly delimit the `N=1` Dirac--Igusa result.

1. Determinant and normalized automorphic target.
   - Current anchors: `main.tex:640-2381`, with the actual determinant spine at `main.tex:640-918` and the normalized cusp form beginning at `main.tex:2383`.
   - Main text should keep the virtual determinant statement, the normalized automorphic line, and only the reflection values needed downstream.
   - Do not keep the full local sign/O1/O2 proof package in the main spine. It is a certificate dependency, not the theorem narrative.

2. D6--D2--D0 Mukai--Gram dictionary.
   - Current anchors: `main.tex:2634-2845`, especially `main.tex:2661-2750`.
   - This should be promoted from supporting dictionary to main theorem/proposition status. It is the bridge from physical charge variables to the Borcherds coefficient variables.
   - Keep the formula
     `v_X(I_Y)=(1,0,1-d)\otimes 1_E+(0,-\beta,-n)\otimes\omega_E`
     and the Gram triple `(beta^2/2,n,d-1)` in the main text.
   - Clarify the later shift conflict: when hybrid/source sections use a geometric elliptic degree `b_R`, state whether `b_R=d` or the Borcherds exponent is `m=d-1`.

3. Normal-ordered Gram descent.
   - Current anchors: `main.tex:4309-4977`.
   - This is core theorem-spine material and should appear before the compact-source ledgers.
   - Keep the cocycle, the normal-ordered extension, and the raw fixed-lift no-go.
   - Fix before promotion: distinguish the raw placement `i_0(c)=(c,0)` from the split section `s(c)=(c,\Pi(c))`; define the raw homogeneous pushforward before the no-go theorem; replace any misleading `H^2_{\mathrm{sym}}` language with the actual statement that the ordinary class is zero but there is no linear homogeneous trivialization compatible with the raw lift.

4. Denominator algebra and scalar square.
   - Current anchors: denominator algebra `main.tex:5560-5702`; scalar square `main.tex:13701-13955`.
   - Keep the denominator identity and OP scalar square as main consistency theorems.
   - The scalar square should stay late as an independent second-order check, not as orientation evidence.

5. Compact Dirac--Igusa realization problem.
   - Current anchor: `main.tex:5704-13700`.
   - Main text should contain a short target/current-envelope statement, a precise list of missing source-comparison certificates, and the theorem-status ledger.
   - It should not contain the full D0, hybrid, Koszul, primitive-recognition, and residual ledgers. Those belong in appendices.

6. One status ledger at the front and one synthesis ledger at the end.
   - Current anchors: front status `main.tex:357-453`; final synthesis `main.tex:13957-14264`.
   - Keep one front claim-strength table and one final constructed/imported/open dependency table.
   - Remove row and spin dependencies from the closure diagram unless a theorem actually uses them.

## Appendix content to retain

Appendices should preserve checkability without letting side material masquerade as a proof dependency.

1. Boundary compatibility appendix.
   - Current anchor: `appendices/boundary_compatibility_conditions.tex:1-121`, included at `main.tex:16081`.
   - Retain. It is scoped, useful, and already contains the right disclaimers at `appendices/boundary_compatibility_conditions.tex:84-88` and `appendices/boundary_compatibility_conditions.tex:114-121`.
   - Title should remain explicitly `N=1` or boundary-compatibility scoped. It must not imply a row map for the eight diagonal divisors.

2. Orientation obstruction algebra.
   - Current anchors: `main.tex:920-2381`, `main.tex:2848-4305`.
   - Retain in an appendix titled along the lines of `Orientation gerbes, quotient characters, and Pfaffian wall signs`.
   - Main text keeps a two-page theorem statement: what O1/O1+/O2 are, what they certify, and what remains open.
   - Appendix keeps the local obstruction certificates, rank-one quotient checks, Klein-four criterion, finite-stabilizer residuals, and HN reducible Pin^c criterion.

3. Maass multiplier and reflection table.
   - Current anchors: `main.tex:2400-2413`, `main.tex:2452-2470`, `main.tex:5287-5338`.
   - Retain as an appendix if the generator computations remain in the paper.
   - Main text should state only the six reflection values and the resulting target character. Generator-level verification is check material, not theorem flow.

4. Sign and polarization conventions.
   - Current anchor: Bott/sign remark `main.tex:2509-2528`.
   - Move to a sign-conventions appendix or delete.
   - Rename the content so it cannot read as a Bott-theoretic explanation of the square root. The useful statement is only that polarization/sign conventions are separate from Hall orientation data.

5. Fourier-variable and coefficient dictionary.
   - Current anchors: `main.tex:2560-2599`, `main.tex:13714-13721`, `main.tex:13724-13855`, `main.tex:13960-14012`.
   - Retain one compact appendix table if it prevents notation drift.
   - Do not repeat the same dictionary in the introduction, scalar square section, and final synthesis.

6. Finite source and compact-realization residual ledgers.
   - Current anchors: formal current envelope `main.tex:5724-5768`; E3 source material `main.tex:5770-6140`; finite compact obstruction around `main.tex:6192`; chiral Koszul source around `main.tex:6506`; hybrid/local wrapped material `main.tex:7039-8303`; normal-ordering cochains `main.tex:8348-9511`; D0 certificate around `main.tex:9973`; compact realization certificate around `main.tex:11750`; primitive-recognition material around `main.tex:12124`.
   - Retain as appendices because these are necessary to audit the open compact-source claim.
   - Compress the main section to target, obstruction, and missing certificates.

7. Optional row ledger appendix.
   - Current anchors: main row section `main.tex:14267-14552`; detailed row appendix `main.tex:14689-16081`.
   - If row material stays inside this paper, keep a compressed independent row section plus one appendix ledger.
   - Do not keep both the current main row section and the full row appendix in their present duplicated form.

## Companion-note/removal candidates

1. Spin L-factor appendix.
   - Current anchor: `main.tex:14558-14686`.
   - Quarantine level: companion note, not main paper appendix, unless a theorem in the main spine starts citing it.
   - It is an arithmetic normalization note. It is independent of the virtual determinant, Hall/Pfaffian orientation problem, compact source problem, BKM denominator, scalar OP square, and diagonal-row certificates.
   - If retained in the PDF, reduce to one paragraph plus a pointer. Otherwise move to `notes/` or a separate arithmetic appendix note.

2. Eight diagonal-divisor row atlas.
   - Current anchors: `main.tex:14267-14552` and `main.tex:14689-16081`.
   - Quarantine level: companion row atlas unless the paper is explicitly widened beyond the `N=1` theorem.
   - The rows are independent extension data. They are not part of the theorem spine.
   - The current title `Diagonal-divisor rows and CHL boundary physics` overclaims. Replace with `Independent diagonal-divisor row ledger` or `Diagonal-divisor denominator rows and required certificates`.

3. Comparison-symbol and fractional-root material.
   - Current anchors: `main.tex:15893-16055`.
   - Quarantine level: companion modular-root note or a short forbidden-identifications box.
   - The present length invites the reader to think the comparison symbols are already the Clery--Gritsenko rows or physical CHL hosts. They are not.

4. Repeated ledgers and status tables.
   - Current anchors: front tables `main.tex:357-453`; compact ledgers throughout `main.tex:5704-13700`; row status table `main.tex:14374-14444`; final synthesis `main.tex:13957-14264`; row appendix status material `main.tex:14689-16081`.
   - Remove repetition. One theorem-status table at the front, one final dependency table, and one row table only if rows stay.

5. Bott/sign digression.
   - Current anchor: `main.tex:2509-2528`.
   - Quarantine level: delete from main. If retained, it belongs in sign conventions and should be framed negatively: it is not orientation data and not a proof source.

## Compression map with exact current anchors

| Current anchor | Current role | Required action | Destination |
|---|---|---|---|
| `main.tex:57-172` | Abstract with determinant, denominator, charge, compact realization, rows | Compress. Remove row detail and any phrase implying physical row realization. | Short abstract for `N=1` theorem plus independent extensions sentence |
| `main.tex:177-462` | Introduction and claim tables | Keep one claim-strength ledger. Remove duplicate later-row closure language. | Main |
| `main.tex:640-918` | Determinant core | Keep. | Main |
| `main.tex:920-2381` | Local sign/O1/O2/Pfaffian/Weyl obstruction package | Move almost all. Main keeps short conditional orientation theorem. | Orientation appendix |
| `main.tex:2383-2630` | Normalized cusp form, Maass character, Bott/sign remark, BGN identification | Split. Keep normalized target and BGN identity; move generator computations and sign remarks. | Main plus Maass/sign appendices |
| `main.tex:2509-2528` | Bott/sign/Gram polarization remark | Delete or quarantine. Fix grammar if kept: `Orientation data enter`. | Sign appendix |
| `main.tex:2634-2845` | D6--D2--D0 dictionary and reduced scalar quotient | Promote and keep. | Main, earlier than normal-ordering theorem |
| `main.tex:2848-4305` | Orientation monodromy, quotient cohomology, Klein-four, finite stabilizers, rank-one rigidification | Move. | Orientation appendix |
| `main.tex:4309-4977` | Normal-ordered Gram descent and raw fixed-lift no-go | Keep and move earlier. Fix raw/split definitions and cohomology language. | Main |
| `main.tex:5024-5702` | Exterior-square model, Weyl chamber, denominator algebra | Keep the denominator theorem. Move detailed generator checks if duplicated. | Main plus Maass appendix |
| `main.tex:5704-13700` | Compact realization problem plus long source/residual ledgers | Compress main to target plus missing certificates. | Main summary plus source appendices |
| `main.tex:13701-13955` | Scalar square and OP normalization | Keep late. Add disclaimer that constants/signs are not orientation inputs. | Main |
| `main.tex:13957-14264` | Coefficient dictionary and main synthesis | Compress to final dependency table. Remove row/spin from theorem closure. | Main |
| `main.tex:14267-14552` | Diagonal-divisor rows and CHL boundary physics | Rename and quarantine. Keep only if explicitly independent. | Independent section or companion |
| `main.tex:14558-14686` | Spin L-factor appendix | Move out unless cited by a theorem. | Companion arithmetic note |
| `main.tex:14689-16081` | Full eight-row appendix | Compress or move out. Eliminate duplicate status/ledger material. | Row appendix or companion row atlas |
| `appendices/boundary_compatibility_conditions.tex:1-121` | N=1 boundary compatibility checks | Retain. | Boundary appendix |

## Required independence disclaimers

Add these disclaimers verbatim or in equivalent mathematical language where the corresponding material remains.

1. Rows.
   - `The diagonal-divisor row material is independent extension data. It is not used in the N=1 Dirac--Igusa theorem, the virtual determinant calculation, the compact-source obstruction analysis, or the OP scalar square.`
   - If the section remains in the PDF, add this at the start of the row section, current anchor `main.tex:14267`.

2. Spin L-factor.
   - `The spin L-factor normalization is an arithmetic side note. None of the Dirac--Igusa, Hall/Pfaffian orientation, BKM denominator, compact-source, scalar-square, or row-certificate arguments depends on it.`
   - If the appendix remains, add this before current `main.tex:14558`.

3. Maass character versus Hall orientation.
   - `The Maass multiplier fixes the automorphic target character. It does not construct the Hall/Pfaffian orientation line and does not discharge O1, O1+, or O2.`
   - Add near `main.tex:2400-2470` and again before any main-body use of reflection signs.

4. Scalar-square constants.
   - `The constants 64 and 4096, and the OP minus sign, are scalar normalizations. They are not orientation data and do not prove Pfaffian descent.`
   - Add near `main.tex:13701-13955` if not already stated sharply enough.

5. Boundary compatibility.
   - `The boundary compatibility checks are N=1 checks only. They do not supply row maps for F5--F8 and do not construct a CHL/CY/DT/chiral boundary host.`
   - The existing appendix already gestures at this at `appendices/boundary_compatibility_conditions.tex:84-88` and `appendices/boundary_compatibility_conditions.tex:114-121`; keep it after any rewrite.

6. Coefficient dictionary.
   - `The coefficient dictionary identifies Borcherds exponents and scalar normalizations; it is not an equality of Hilbert schemes, brackets, or Hall state spaces unless the separate comparison package is supplied.`
   - Add near `main.tex:13960-14012`.

7. Compact source.
   - `The formal current envelope is a target algebraic envelope. It is not by itself a compact Dirac--Igusa source object.`
   - Add near `main.tex:5724-5768`.

8. Comparison rows.
   - `The comparison symbols and fractional-power products are formal comparison data. They are not identified with the Clery--Gritsenko rows or with physical CHL boundary sectors without the listed certificates.`
   - Add if `main.tex:15893-16055` remains.

## Rewrite section order

Recommended order after compression:

1. Abstract.
   - State the `N=1` theorem, target object, and open compact-source status. Mention rows only as independent extension data if retained.

2. Introduction and claim strength.
   - One table: constructed, imported, conditional, open.
   - No spin L-factor. No row atlas.

3. Virtual determinant and automorphic square root.
   - Current determinant core from `main.tex:640-918`.
   - Normalized automorphic target from `main.tex:2383-2508`, compressed.

4. D6--D2--D0 Mukai--Gram theorem.
   - Current `main.tex:2634-2845`, promoted.
   - Resolve the `d-1` / `b_R` notation before the reader enters normal ordering.

5. Normal-ordered Gram descent.
   - Current `main.tex:4309-4977`.
   - This should become one of the central formal sections.

6. Denominator algebra.
   - Current `main.tex:5024-5702`, with generator computations compressed to appendix.

7. Compact Dirac--Igusa realization problem.
   - Current `main.tex:5704-13700`, collapsed to target, obstruction classes, and missing certificates.

8. Scalar square and OP check.
   - Current `main.tex:13701-13955`.
   - Keep as independent consistency check.

9. Coefficient dictionary and main synthesis.
   - Current `main.tex:13957-14264`, compressed to the final theorem-status ledger.

10. Independent diagonal-divisor row ledger.
   - Current `main.tex:14267-14552`, only if retained.
   - Otherwise move this entire part plus `main.tex:14689-16081` to a companion row atlas.

Appendices after rewrite:

1. Fourier variables and normalization constants.
2. Maass multiplier and reflection values.
3. Orientation gerbes, Pfaffian wall signs, and quotient obstructions.
4. Compact-source residual certificates.
5. `N=1` boundary compatibility.
6. Optional compressed row ledger, if not moved to a companion note.

Do not include the spin L-factor as a default appendix. It belongs in a companion arithmetic note unless integrated by a real dependency.

## Patch queue

1. Rename `main.tex:14267` from `Diagonal-divisor rows and CHL boundary physics` to `Independent diagonal-divisor row ledger` or `Diagonal-divisor denominator rows and required certificates`.

2. Move `main.tex:14558-14686` out of the manuscript or reduce it to one independence-marked pointer.

3. Move `main.tex:920-2381` and `main.tex:2848-4305` into an orientation appendix. Leave a compact main theorem stating the obstruction classes and remaining certificate obligations.

4. Promote `main.tex:2661-2750` from dictionary lemma posture to a main theorem/proposition, and move it before the normal-ordering section.

5. Move `main.tex:4309-4977` before the compact-source ledgers. Repair raw/split notation, define raw homogeneous pushforward, and add the missing flag formula.

6. Replace `H^2_{\mathrm{sym}}` or equivalent language in the normal-ordering section with a statement about zero ordinary class plus no compatible linear homogeneous trivialization.

7. Move full Maass generator computations from `main.tex:2400-2413` and `main.tex:5287-5338` to an appendix. Main text keeps only the reflection values and their consequence.

8. Delete or quarantine the Bott/sign paragraph at `main.tex:2509-2528`. If kept, fix `Orientation data enters` to `Orientation data enter`.

9. Replace the synthesis arrow around `main.tex:14014-14028` so it does not include row extension data as a theorem dependency.

10. Deduplicate row tables: keep either the compact table at `main.tex:14339-14444` or a detailed appendix table in `main.tex:14689-16081`, not both in full.

11. Compress `main.tex:15893-16055` to a forbidden-identifications box or move it to a companion note.

12. Rename the formal current envelope around `main.tex:5724-5768` so the notation cannot be read as an already-constructed compact source. Use a target-current name rather than a source-realization name.

13. Add all independence disclaimers listed above before moving text. This prevents accidental theorem-strengthening during mechanical reordering.

## Residual layout/build checks

Run these checks after the actual rewrite, not as part of this report-only task.

1. Search checks.
   - `rg -n "Diagonal-divisor rows and CHL boundary physics" main.tex appendices`
     should return no hits.
   - `rg -n "spin L|L_\\{\\\\mathrm\\{spin\\}\\}|Andrianov" main.tex appendices`
     should return only a companion pointer or an explicitly independent appendix.
   - `rg -n "Bott|Grothendieck--Witt" main.tex`
     should return no main-body explanatory digression.
   - `rg -n "4096.*orientation|orientation.*4096|-4096.*orientation" main.tex appendices`
     should return only negative disclaimers, not evidence claims.
   - `rg -n "H\\^2_\\{\\\\mathrm\\{sym\\}\\}|H\\^2_\\{sym\\}" main.tex appendices`
     should return no misleading cohomology class language.
   - `rg -n "well defined modulo.*B|modulo B" main.tex appendices`
     should be checked against the corrected normal-ordering quotient statements.
   - `rg -n "physical charge lattice" main.tex`
     should not hit the abstract unless the phrase is precisely qualified.

2. Table and ToC checks.
   - Compile after the rewrite and inspect the first ten pages. The reader should see theorem spine before residual ledgers.
   - The table of contents should not put spin L-factors or eight-row atlases before the main synthesis.
   - Long row/status tables should be appendix-only or companion-only.

3. Cross-reference checks.
   - Moving orientation and source ledgers will break labels unless done carefully. Check every `\ref`, `\cref`, and theorem label touching O1/O1+/O2, D0, compact realization, and row certificates.
   - Boundary appendix numbering must remain stable after `\appendix`.

4. Claim-strength checks.
   - Every occurrence of `physical`, `realization`, `boundary`, `CHL`, `compact`, and `orientation` should be audited for whether it is constructed, imported, conditional, or open.
   - Row material must never be listed as a dependency of the `N=1` theorem.
   - Spin material must never be listed as a dependency unless a new theorem actually uses it.

5. Build checks.
   - After integration, run the repo's normal LaTeX build command and inspect warnings for overfull boxes in the moved row tables and appendices.
   - No build is required for this Agent 21 report itself.
