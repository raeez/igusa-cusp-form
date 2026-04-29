# Agent 20 bibliography and primary-source audit

Date: 2026-04-29
Scope: audit imported theorem and citation dependencies for the current rewrite.
Write constraint: this report only. No edits to `main.tex`, `proj.bib`, or manuscript source.

## Imported theorem ledger

| Dependency | Manuscript anchor | Current source anchor | Imported content | Status |
|---|---:|---|---|---|
| Gritsenko-Nikulin Borcherds product for the Igusa cusp form | `main.tex:1946-1956`, `2530-2558`, `5560-5685` | `proj.bib:100-134` (`GN`, `GNII`) | Product expansion for `D_5=64^{-1}\Delta_5`, root multiplicities from `f(nm,l)`, denominator identity after the `Z -> 2Z` convention | Essential. Agent03 checked arXiv theorem/equation anchors, but published page/theorem anchors still need exact verification before final claims. |
| Gritsenko-Nikulin Lorentzian lattice/Weyl chamber data | `main.tex:2024-2043`, `5185-5206`, `5246-5285`, `5460-5550`, `14768-15096` | `GN`, `GNII`, `NIKULIN` | Real simple roots, Weyl vector, imaginary simple roots, type-II chambers for `t=1,2,3,4`, reflection-subgroup/chamber facts | Imported. Must cite exact GN/GNII theorem/equation numbers at every denominator/chamber claim. `NIKULIN` bib metadata is weak. |
| Maass multiplier and character restriction | `main.tex:1887-2008`, `5287-5338` | `proj.bib:38-45` (`MAASS:1`), `GN` | Multiplier/character check for the automorphic product | Source-dependent. Main text should not let this read as a geometric Hall orientation proof. Verify Maass source directly if the independent Maass citation is retained. |
| Borcherds automorphic product theorem | `main.tex:2530-2558` | `proj.bib:228-247` (`B`, `Borcherds95`) | General automorphic-product existence/input theorem | Imported. `Borcherds95` metadata lacks DOI/eprint/URL and exact theorem/page citation. |
| Clery-Gritsenko dd-modular products | `main.tex:14339-14459`, `15098-15321` | `proj.bib:158-168` (`GC`) | Eight dd-modular product rows, weights, congruence data, product theorem | Imported product theorem only. It does not supply a BKM chamber, compact Hall source, or orientation package. Exact CG theorem/page anchors still required in the final citation layer. |
| Govindarajan / CHL BKM denominator sources | `main.tex:14505-14532`, `15470-15839` | `proj.bib:170-227` (`GK09CHL`, `GK10Composite`, `CD09BKM`, `Gov11BKM`, `GovSam19`) | CHL/CHL-like BKM denominator/WKB data, row mapping, cover data, scalar-square context | Imported and fragile. Current table-level claims must be checked against `Gov11BKM` Table 3, Section 4.2, Section 4.3, Appendices C-D. F7 cover/half-integral exponent assertions need exact source confirmation. |
| Eichler-Zagier weak Jacobi-form facts | `main.tex:1991`, `2601-2630` | `proj.bib:87-92` (`EZ:1`) | Support/coefficients of `\phi_{0,1}`, `f(0,0)=10`, Jacobi-form normalization | Mostly safe but imported. Cite exact theorem/equation/table for coefficient normalization if used in a theorem proof. |
| OP/Oberdieck reduced K3xE scalar identities | `main.tex:2760-2799`, `13740-13955` | `proj.bib:249-288` (`OB`, `OPand`, `OberdieckReducedPT`) | `\chi_{10}^{OP}=D_5^2=4096^{-1}\Delta_5^2`, reduced quotient DT/PT branch, `Z_{OP}=-4096\Delta_5^{-2}` branch after conventions | Imported scalar branch only. It cannot be cited for Pfaffian orientation, Hall source, Weyl lift, or square-root signs. Exact theorem/proposition labels still require verification. |
| Bryan/Behrend/Thomas ordinary vs reduced DT context | `main.tex:2760-2799`, `13806-13855` | `proj.bib:290-309` (`DT`, `BEHREND`) and `B`/`Bryan` keys as cited locally | Ordinary DT vanishing/reduced quotient framing and Behrend-weighted interpretation | Contextual import. `BEHREND` metadata lacks DOI/eprint. Do not promote to orientation theorem. |
| Mukai lattice and stability technology | `main.tex:4309-4382` plus stability appendix anchors | `proj.bib:808-915` | Mukai lattice pairing, moduli/stability background | Standard but imported. The local arithmetic is internal; the signature/pairing and moduli statements need exact Mukai/Yoshioka/Toda/Bridgeland anchors if theorem-level. |
| PTVV/BBDJS orientation and shifted-symplectic technology | `main.tex:570-638`, `1160-1476`, `3070-3128`, `9536-9652` | `proj.bib:617-636` (`PTVV2013`, `BBDJS2015`) | Shifted symplectic forms, perverse sheaves/vanishing-cycle technology, orientation-line background | Technology only. These sources do not construct the reduced `K3 x E` quotient orientation, finite-stabilizer linearizations, or type-II Weyl lift. Wording must preserve this boundary. |
| Joyce-Upmeier / Borisov-Joyce / Oh-Thomas CY4 orientation analogues | `main.tex:1160-1476`, `1632-1674`, `4130-4250` | `proj.bib:512-604` | Orientation-data existence and CY4 virtual-cycle analogues | Analogy/technology only. Exact theorem/page refs needed if specific orientation existence is invoked. Must not be used as proof of the manuscript's `O1/O1+/O2` package. |
| Factorization/chiral algebra foundations | `main.tex:5730-6140`, `6317-6381`, `6404-6450`, `9468-9652` | `proj.bib:61-78`, `323-449`, `356-397`, `645-672` | BD current envelope, Costello-Gwilliam factorization algebras, Francis-Gaitsgory bar/cobar, formality/cyclic-homology background | Target-side formalism only. It does not produce the compact K3-to-E source or a theorem-level source Hall algebra. |
| Group cohomology of finite stabilizers/orientation gerbes | `main.tex:1239-1352`, `3197-4018` | No adequate current bib anchor. `Evd80` exists at `proj.bib:733-740` but is not the cited group-cohomology source and is unused. | Cohomology of `E[2]`, `(Z/2^a)^2`, Borel group cohomology, residual finite stabilizer classes | Missing source. Either prove entirely in text and remove folklore/source claims, or add/cite a primary/standard group cohomology source. |
| Normal-ordering cocycle and charge-lattice arithmetic | `main.tex:4309-4968` | Internal computations plus Mukai/BGN imports | Quadratic primitive, cocycle formulas, Gram descent obstruction, root-string incompatibility | Mostly internal once Mukai lattice and BGN target root-string data are imported. Current `H^2_sym` wording is unsafe and should be downgraded. |
| Cyclotomic/negative-cyclic orientation cocycle | `main.tex:9738-9878` | `proj.bib:645-672` (`NikolausScholze`, `Goodwillie1985`, `ToenRRRoot`) plus Joyce-Upmeier | Multiplicative orientation cocycle via cyclotomic spectra/negative cyclic classes | Weakly sourced and over-strong. Needs exact theorem/page verification and likely downgrade to conditional framework. |
| Maass/Saito-Kurokawa/spin `L`-factor appendix | `main.tex:14560-14686` | `proj.bib:742-788` (`Del79`, `Andr74`, `ZagierSK`, `Manin72`, `KZ`) | SK lift attached to `\Delta`, spin factorization, completion convention, period/nonzero residue claims | Optional and high-risk. Retain only with exact theorem/page/convention citations, or demote to a non-load-bearing appendix note. |

## Missing/weak citations

1. Missing group cohomology source. The manuscript currently relies on explicit `H^2`/Borel cohomology calculations for finite stabilizers and orientation gerbes (`main.tex:1239-1352`, `3197-4018`). `proj.bib` has no Cartan-Eilenberg, Brown, Adem-Milgram, or comparable standard source. `Evd80` is an Evens Chern-class paper, currently unused, and does not by itself cover the finite-stabilizer computations being cited as folklore.

2. `NIKULIN` is bibliographically weak. It is entered as `@BOOK` although the title and venue indicate a paper in Proceedings of the Steklov Institute (`proj.bib:80-86`). If chamber/reflection claims depend on it, the entry needs correct type, pages, translated venue details if used, and exact theorem/page anchors.

3. `Borcherds95` is too thin for theorem-level dependence (`proj.bib:240-247`). Add stable metadata and cite the exact automorphic-product theorem used at `main.tex:2530-2558`.

4. `BEHREND` lacks DOI/eprint metadata (`proj.bib:302-309`). This is not fatal, but it weakens a source chain already being used near reduced DT/PT sign conventions.

5. `MAASS:1` has no stable retrieval metadata (`proj.bib:38-45`). If the Maass multiplier is cited independently of GN, source-check Maass directly and add page/theorem data.

6. `OPand` citation labels conflict with the local audit material. Current `main.tex:13806-13855` cites `OPand` Proposition 5. `agent_material/08_op_dt_primary_source_comparison.tex` says the relevant statement is the proposition after Conjecture D. This must be resolved against the primary source before final.

7. Nikolaus-Scholze/Goodwillie/Toen citations are not enough for the strong cyclotomic orientation-cocycle theorem as currently worded (`main.tex:9738-9878`). The cited results may supply TC/THH/cyclotomic infrastructure, but not the manuscript-specific lift of orientation lines into `\pi_0 HC^-` as a strict multiplicative cocycle.

8. The bibliography has unused keys that look like abandoned or potential support sources: `ConnesNCG`, `EOT`, `Evd80`, `GNPartI`, `Gritsenko2018Reflective`, `II10`, `Ich05`, `KNAPP:1`, `LurieHA`, `Niemann03`, `Schlichting2010`. Do not add text just to use them. Either remove later, or use only after exact source-role assignment.

9. No missing `\cite` keys were found by extracting citation keys from `main.tex` and comparing them against `proj.bib`. The problem is not broken keys; it is weak source role, missing standard background entries, and exact theorem/page debt.

## Claims requiring exact theorem/page verification

1. `64^{-1}\Delta_5(2Z)` denominator normalization and visible multiplicities `f(nm,l)` (`main.tex:1946-1956`, `2530-2558`, `5560-5685`). Verify GN/GNII theorem/equation numbering in the published versions, not only arXiv numbering.

2. Reflection signs and Maass-character restriction (`main.tex:5185-5206`, `5287-5338`). Agent03 identified GN formulas (1.3)-(1.5) and propositions 2.1/2.2 as likely exact anchors. Current text still contains a brittle citation line near `main.tex:5201` that should be made precise by the integration owner.

3. Type-II row/chamber data for `t=1,2,3,4` (`main.tex:14768-15096`). Verify GNII equations (2.21)/(2.20)/(2.11), Lemma 2.5, Section 5.1.1, and the `t=4` parabolic claim.

4. Clery-Gritsenko eight-row product table (`main.tex:14339-14459`, `15098-15321`). Verify Theorem 1.4, Proposition 1.2, Theorem 3.1, and each row's weight/character/cover status.

5. Govindarajan/CHL denominator rows (`main.tex:15470-15839`). Verify `Gov11BKM` Table 3, Section 4.2, Section 4.3, Appendices C-D, plus the dependence on `GK09CHL`, `GK10Composite`, and `CD09BKM`. The F7 `\mu_4` cover and half-exponent assertions are especially source-sensitive.

6. OP scalar branch constants (`main.tex:13740-13955`). Verify Oberdieck Theorem 1, Oberdieck Theorem 3(i), Oberdieck-Pandharipande Section 2/Proposition label, Bryan Definition 2.1/Conjecture 2.3, and the conversion `\chi_{10}^{OP}=D_5^2=4096^{-1}\Delta_5^2`.

7. Cosection parity flip (`main.tex:3070-3128`). The cited PTVV/BBDJS/Joyce-Upmeier/Oberdieck technology does not automatically prove the claimed parity package. Either add a local proof or demote it to conditional.

8. Joyce-Upmeier/BBDJS/PTVV orientation statements (`main.tex:1160-1476`, `1632-1674`, `4130-4250`). Exact theorem/page references are required for whatever is actually imported. The reduced quotient orientation, `E[2]` linearization, and Weyl cocycle remain manuscript assumptions unless separately proved.

9. Factorization/current-envelope claims (`main.tex:5730-6140`, `6317-6450`, `9468-9652`). Exact BD/Francis-Gaitsgory/Costello-Gwilliam anchors are needed for target-formalism claims. No cited source should be represented as constructing the compact source.

10. Cyclotomic orientation construction (`main.tex:9738-9878`). Verify Nikolaus-Scholze Corollary II.1.7, Theorem II.6.9, Theorem I.1.13, Goodwillie, and Toen references against the exact functorial/monoidal claims. Until checked, call it a conditional construction, not a theorem.

11. Mukai lattice signature/pairing and stability background (`main.tex:4309-4382`). Use exact Mukai/Yoshioka/Toda/Bridgeland anchors for imported geometric facts. The arithmetic after the pairing is internal.

12. Spin `L`-factor appendix (`main.tex:14560-14686`). Verify Andrianov/Zagier source for the SK lift and spin factor, the completed `L`-function convention, central-zero cancellation, nonzero residue at `s=10`, and Manin-Deligne period normalization. This section is not needed for the main denominator argument and should not carry unverified theorem-level claims.

## Claims safe as internal computations

1. Citation-key integrity: the current `main.tex` citation keys all resolve in `proj.bib`. No missing key-level bib entries were detected.

2. The normal-ordering lattice arithmetic, once the Mukai pairing and BGN target root-string data are imported, is internal. This includes the quadratic primitive, cocycle formulas, and raw Gram descent obstruction (`main.tex:4309-4968`).

3. The computational low-degree checks reported by the swarm are internal checks: `\phi_{0,1}` coefficients, Borcherds product low-degree terms, the `93` and `29 | 93` arithmetic, height-four residuals, doubled-isotropic residuals, type-II lattice matrix checks, and finite active-support checks. These support consistency; they do not replace primary GN/CG/Gov source verification.

4. The OP normalization conversion between `D_5`, `\Delta_5`, and the square `D_5^2` is internal algebra after the OP/Oberdieck scalar identity and the manuscript's normalization convention are fixed by source.

5. The statement "OP/Oberdieck supplies a scalar square, not an orientation square root" is safe as a negative-source conclusion from the local primary-source comparison, provided it is phrased as a boundary on what those papers claim.

6. The BD/Francis-Gaitsgory target current-envelope construction can be kept as target-side formal algebra if it is explicitly separated from any compact K3xE source claim.

## Source-dependent rewrite wording

Use source-role wording that prevents accidental theorem inflation:

1. GN/BGN denominator:
   "By the Gritsenko-Nikulin Borcherds product/denominator theorem, with the manuscript's `Z -> 2Z` and `D_5=64^{-1}\Delta_5` normalization, the automorphic product has exponents `f(nm,l)`. We import this automorphic denominator as target data."

2. Maass character:
   "The Maass/Gritsenko-Nikulin multiplier computation checks the automorphic character of the target product. It is not a construction of a Hall orientation character."

3. OP/DT:
   "The OP/Oberdieck branch imported here is the reduced primitive nonzero-K3-class scalar identity. It gives the orientation-forgetful scalar square and the `-4096\Delta_5^{-2}` branch after normalization. It does not construct the Pfaffian orientation, the Hall source, or the denominator square root."

4. Orientation:
   "PTVV, BBDJS, Joyce-Upmeier, Borisov-Joyce, and Oh-Thomas supply shifted-symplectic, vanishing-cycle, and orientation technology. The reduced `K3 x E` quotient orientation package, finite-stabilizer linearization, and type-II Weyl lift are additional hypotheses or open construction tasks here."

5. Clery-Gritsenko/Govindarajan rows:
   "Clery-Gritsenko supplies product identities for the dd-modular rows; Govindarajan/CHL sources supply the physical BKM denominator data for the CHL rows. Neither source supplies a compact Hall/CY source or the orientation package required by this manuscript."

6. Factorization/chiral:
   "BD, Costello-Gwilliam, and Francis-Gaitsgory provide target-side current and factorization formalism. The compact source coalgebra and its comparison to the target remain conditional."

7. Group cohomology:
   "The finite-stabilizer cohomology calculations are elementary group-cohomology computations proved here" if fully proved in text. Otherwise add a standard source and cite it. Do not call them folklore without a source.

8. Cyclotomic construction:
   "Assuming the orientation-line data admits the stated cyclotomic/negative-cyclic lift, the following cocycle is multiplicative." Do not call this unconditional until exact Nikolaus-Scholze/Goodwillie/Toen/Joyce-Upmeier source support is verified.

9. Spin appendix:
   "If retained, the Saito-Kurokawa/spin calculation is independent corroborating arithmetic, not an input to the denominator or orientation theorem."

## main.tex/proj.bib anchors

Primary manuscript anchors:

- Abstract/source-status framing: `main.tex:73-168`, `520-638`.
- GN/Maass/BGN target denominator: `main.tex:1887-2043`, `2530-2630`, `5185-5685`.
- OP/Oberdieck/DT scalar branch: `main.tex:2760-2799`, `13740-13955`.
- Orientation package and finite stabilizers: `main.tex:1160-1476`, `1632-1674`, `3070-3128`, `3197-4250`.
- Mukai/normal-ordering arithmetic: `main.tex:4309-4968`.
- Factorization/chiral/current formalism: `main.tex:5730-6450`, `9468-9878`.
- Eight-row boundary and CHL/Govindarajan material: `main.tex:14339-15839`.
- Spin/Saito-Kurokawa appendix: `main.tex:14560-14686`.

Primary bibliography anchors:

- Maass/GN/Nikulin/Eichler-Zagier: `proj.bib:38-134`.
- Clery-Gritsenko/Govindarajan/CHL/Borcherds: `proj.bib:158-247`.
- OP/Oberdieck/DT/Behrend: `proj.bib:249-309`.
- Hall/factorization/cyclic foundations: `proj.bib:61-78`, `311-449`, `645-672`.
- CY4/orientation/PTVV/BBDJS/Joyce-Upmeier: `proj.bib:512-636`.
- Group cohomology placeholder/weak source: `proj.bib:733-740` (`Evd80`, unused and insufficient for current role).
- Spin/Saito-Kurokawa/period sources: `proj.bib:742-788`.
- Mukai/stability sources: `proj.bib:808-915`.

## Patch queue for citations

1. Add a real group cohomology source entry, or rewrite the finite-stabilizer sections as fully self-contained proofs and remove all "folklore" source language. Candidate type: Cartan-Eilenberg or Brown, depending on the exact claims the integration owner wants to cite.

2. Repair `NIKULIN` bibliographic metadata and add exact theorem/page anchors wherever it supports reflection/chamber claims.

3. Add exact GN/GNII source anchors in the denominator theorem and row sections. Prefer equation-level citations for product normalization, Weyl vector, simple-root lists, and imaginary-root multiplicities.

4. Clean the Maass/GN character citation near `main.tex:5185-5338`. The text should cite exact GN multiplier/reflection-sign statements and avoid any implication that the Maass character is a Hall orientation.

5. Reconcile `OPand` Proposition 5 versus "proposition after Conjecture D" against the primary source. Then cite Oberdieck/OP/Bryan with exact theorem/proposition labels in the OP scalar branch.

6. Add a source-role footnote/table near the orientation section stating that PTVV/BBDJS/Joyce-Upmeier/Borisov-Joyce/Oh-Thomas are technology/analogy sources, not a proof of `O1/O1+/O2`.

7. Downgrade or exactly source-check the cyclotomic/negative-cyclic orientation lemma. If retained as theorem-level text, add exact Nikolaus-Scholze/Goodwillie/Toen theorem/page citations and a proof of the manuscript-specific lift.

8. Replace unsafe `H^2_sym` language in the normal-ordering section with "ordinary class zero by a quadratic primitive" language. This is not a bibliography patch alone, but it is citation-relevant because no source supports the stronger additive-linear trivialization wording.

9. For CG/Govindarajan rows, add exact table/theorem anchors and source-role wording: product identity, CHL denominator data, scalar square, and host/orientation are separate columns.

10. If the spin appendix remains, add exact Andrianov/Zagier/Kohnen-Zagier/Manin-Deligne theorem/page/convention anchors. Otherwise demote it to a non-load-bearing note or remove it from the source-critical path.

11. Add DOI/eprint/stable metadata for thin entries where feasible: `Borcherds95`, `BEHREND`, `MAASS:1`; do not change mathematical claims while doing metadata cleanup.

12. Decide what to do with unused bibliography keys. `GNPartI`, `Gritsenko2018Reflective`, `Ich05`, `II10`, `LurieHA`, and `Schlichting2010` may become useful if source roles are added; otherwise leave cleanup to a later bibliography pass.

## Residual source-audit plan

Priority 0:

1. Verify GN/GNII published theorem/equation/page anchors for the core denominator, multiplier, Weyl-vector, simple-root, and row claims.
2. Verify OP/Oberdieck/Bryan exact theorem/proposition anchors and the `4096`/`64` normalization chain.
3. Add or eliminate the group cohomology source dependency.

Priority 1:

4. Verify CG and Govindarajan/CHL row data from primary sources, especially the F7 cover and denominator-versus-product boundary.
5. Verify orientation-source boundaries: PTVV/BBDJS/Joyce-Upmeier/Borisov-Joyce/Oh-Thomas must stay technology/analogy sources unless the manuscript proves more.
6. Source-check the cyclotomic/negative-cyclic orientation construction or downgrade it to a conditional interface.

Priority 2:

7. Verify Mukai/stability exact anchors for all imported geometric facts.
8. Verify the factorization/chiral exact anchors and keep them target-side.
9. Decide whether the spin `L`-factor appendix is worth the source burden. If retained, audit Andrianov/Zagier/Kohnen-Zagier/Manin-Deligne conventions line by line.
10. Perform metadata cleanup for thin bib entries after theorem/page audit, not before.

Bottom line: the bibliography is key-complete but theorem-role-incomplete. The manuscript can safely rely on internal computations only after the imported automorphic, OP scalar, group-cohomology, orientation-technology, and CHL row boundaries are made explicit and exact.
