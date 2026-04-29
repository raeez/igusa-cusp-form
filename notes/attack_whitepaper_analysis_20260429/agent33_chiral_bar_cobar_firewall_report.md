# Agent 33 Chiral Bar-Cobar Firewall Report

Date: 2026-04-29

Scope: source/target firewall for chiral current envelopes, Beilinson--Drinfeld / Francis--Gaitsgory bar-cobar, chiral Koszul source data, holomorphic factorization / local `E_3` language, and compact source coalgebras.

Sources mined: `materials/raw/2026-04-29-attack-whitepaper-analysis.pdf` via extracted text `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`; current `main.tex`; prior reports `agent06_hall_factorization_report.md`, `agent15_formal_current_envelope_report.md`, `agent16_source_objects_hpre_htw_report.md`, `agent23_theorem_status_taxonomy_report.md`, and `agent25_finite_source_data_schema_report.md`.

Verdict: the current draft has the right firewall language in several places, especially `main.tex:5707-5722`, `6404-6504`, `6506-6728`, and `11750-12103`. The remaining attack surface is that the same symbols and words still invite a reader to confuse a target-internal BD/FG bar-cobar counit with a compact source construction. The manuscript must make the target construction curve-universal and source-free, then make the compact source a finite-first external datum. No target bar construction, target counit, target root multiplicity, target current envelope, or homotopy inverse to a target counit is allowed to define `C_X`, `F_X^{hyb}`, `Sp^{ch}_{K3,E}`, the source collision coproduct, or primitive representatives.

## Target-internal constructions

1. **Gritsenko--Nikulin denominator algebra.** Current `main.tex:5560-5635` imports the Borcherds--Kac--Moody superalgebra `A_den = g_{Delta_5}` and its denominator identity. This proves a target Lie superalgebra graded by Gram triples through `alpha(n,l,m)`; it supplies signed root supermultiplicities and the BKM bracket. It does not supply a compact Hall algebra, compact moduli, orientation lines, source primitives, or protected integration.

2. **Formal BD current envelope.** Current `main.tex:5724-5768` defines `Cur_E(A_den)` and `Den_{Delta_5,E}=U_E^ch(Cur_E(A_den))`. This is valid as a Beilinson--Drinfeld current-envelope construction on the curve `E`. Agent 15 and the attack PDF correctly press for the stronger and cleaner statement: the formal target is curve-universal. For any smooth complex curve `C`, one can define `Cur_C(g_{Delta_5})` and `Den^{alg}_{Delta_5,C}`. The use of `E` is physical only after the compact `K3 x E` source, OP quotient, elliptic degree, and wrapped anchors enter.

3. **Normal-ordered algebraic target lift.** The target-side lift `D^{alg}_{Delta_5,C,L}` requested by the attack PDF is constructible as a source-free algebraic package once a homomorphism `L: Gamma_gram -> Gamma_X^{form}` is chosen. The monoidal section is `s_L(gamma)=(L gamma, Pi_X(L gamma)-gamma)` in the normal-ordered extension. This creates a regraded copy of `g_{Delta_5}` and its curve-current envelope. It is only a target regrading/current package. It is not a compact source and not a section of the quadratic raw Gram map.

4. **Target-internal BD/FG bar-cobar counit.** Current `main.tex:6404-6449` is correct: after choosing an augmented filtered model of the target current envelope in the conilpotent chiral setting, Francis--Gaitsgory chiral Koszul duality gives a target counit
   `Omega_E^ch Bbar_E^ch(Den_{Delta_5,E}) -> Den_{Delta_5,E}`.
   This proves only that the already defined target can be reconstructed from its own target bar coalgebra. It uses the target augmentation and target charge filtration. It contains no compact moduli stack, no source filtration, no hybrid wrapped sector, no quotient-after-correspondence functor, and no primitive representatives.

5. **Target finite windows and parity shadows.** The target can supply finite root windows, signed dimensions, target brackets, target PBW templates, and minimal parity models. Agent 25 is right: if a datum can be filled from the existing target arithmetic scripts alone, it is target reference data. It cannot satisfy a compact-source certificate unless it also carries source provenance, source operation matrices, and finite HN transition data.

## Missing source constructions

1. **Primary compact source.** The manuscript still needs an actual finite-first holomorphic factorization source interface in a named model. Current `main.tex:6024-6140` lists the right data, but the source itself remains supplied/open: finite BV complexes, QME/anomaly cochains, descent, compact-support control, chosen operadic formality/framing, finite HN quotients, and transition maps.

2. **Rectified `K3 -> E` specialization.** `Sp^{ch}_{K3,E}`, `kappa_E`, and `pi_*^{ch}` must be constructed as finite-chain maps between specified categories with product/unit/HN transition squares. Current `main.tex:5770-6012` makes them supplied comparison data. BD/CG language does not produce them automatically.

3. **Hybrid local/wrapped source.** The projection-finite `Ran(E)` sector sees only `b=0`. Current `main.tex:7039-7119` proves the obstruction, and `7121-7850` gives the right certificate shape. Missing source data include rigidified wrapped prequotients, unit-weight/lossless anchors, LL/LW/WL/WW correspondences, all eight two-step flag stacks, quotient-after-correspondence, and protected integration.

4. **Source chiral coalgebra.** The compact source coalgebra must be built from the supplied hybrid source, not from `Den`. Current `main.tex:6506-6728` states the correct certificate. At finite `R`, one must supply `F^{hyb}_{X,R}`, `C_{X,R}`, finite filtration, collision coproduct, bar comparison `b_{X,R}: C_{X,R} -> Bbar_E^ch(F^{hyb}_{X,R})`, and source-to-target cobar map `Theta_{Kos,R}: Omega_E^ch C_{X,R} -> Den_{Delta_5,E,<=R}`.

5. **Finite Hall source kernel.** Current `main.tex:10994-11174` is conditional on a supplied finite source kernel. Missing: finite residual inertia, BBDJS coefficients, orientations, admissible pull-push maps, product/coproduct, two-step flags, source provenance, normal-ordering cochains on correspondence targets, and transition-compatible kernels.

6. **Primitive recognition source data.** Current `main.tex:12124-12308` correctly says primitive recognition is a certificate, not a source construction. Missing: source representatives, parity split, Hall bracket constants, real Serre and isotropic relation checks, completed Hopf pairing, closed radical quotient, PBW compatibility, and no-extra-relations theorem.

## Bar-cobar firewall rules

1. **Never define `C_{X,R}` by target bar construction.** The forbidden equation is `C_{X,R} := Bbar_E^ch(Den_{Delta_5,E,<=R})`. It erases all compact geometry. The target bar coalgebra has target augmentation data, not source collision data.

2. **Never use a homotopy inverse to the target counit as source construction.** A homotopy inverse to `Omega Bbar(Den) -> Den`, if chosen, lives in the target bar-cobar domain. It does not construct `F^{hyb}_{X,R}`, `C_{X,R}`, `Delta_R^ch`, `b_{X,R}`, source primitives, or `Sp^{ch}_{K3,E}`.

3. **Keep the direction of the source comparison fixed.** The compact Koszul map is source-to-target:
   `Theta_{Kos,R}: Omega_E^ch C_{X,R} -> Den_{Delta_5,E,<=R}`.
   It is not the target counit. It is not `kappa_E`. It is not a pushforward along `p_E`.

4. **Different filtrations, different objects.** Target charge filtration on `Den` is not the finite HN/source bar/collision/wrapped filtration on `C_{X,R}`. A conilpotent target truncation cannot stand in for source conilpotence.

5. **Source-bar is legal only after the source exists.** Current `main.tex:6731-6970` is acceptable because it assumes `O_hyb,R=0`, bounded bar length, augmentation of the supplied hybrid source, and transition compatibility. Its output is `Bbar(F^{hyb}_{X,R})`, not `Bbar(Den)`.

6. **Target-internal bar-cobar is a sanity check only.** It can check that the formal current envelope lies in the expected chiral homotopy-theoretic domain. It cannot reduce any compact source residual: not `O_hyb`, not `O_Kos`, not `O_Pi`, not primitive recognition, not orientation/Pfaffian.

7. **Do not say "Koszul duality" generically.** The manuscript must distinguish: target chiral bar-cobar, source chiral Koszul comparison, operadic `E_3` formality/Koszul language, and Lie coalgebra/Hopf primitive Koszul signs. The attack PDF lines around `21455-21710` demand exactly this forbidden-conflations table.

8. **Algebraic universal target is not compact source.** If `D^{alg}_{Delta_5,C,L}` is added, its own bar-cobar counit is valid inside the algebraic target. That still does not define the compact `C_X` attached to `K3 x E`.

## E3/factorization terminology constraints

1. **Define the primary category before `E_3`.** The manuscript should choose a primary holomorphic factorization model, e.g. a Costello--Gwilliam-style cosheaf/factorization category or an explicit chain-operadic holomorphic-polydisc model. Only after that may it define the local `E_3` shadow.

2. **`E_3` is not shorthand for complex dimension three.** The safe phrase is: "holomorphic factorization source with a local `E_3` shadow after the chosen operadic formality/framing datum." The local shadow requires a chain operad, holomorphic-polydisc comparison, formality torsor point, framing/homotopy witness, compact-support convention, and field of definition.

3. **Remove unqualified equivalences.** Current `main.tex:5778-5785` and `5824-5847` are improved but still dangerous. "Chiral algebra on `E`, equivalently factorization algebra on `Ran(E)`" is allowed only after a named BD/CG/formality comparison `kappa_E` in specified model categories and with support hypotheses.

4. **Ginzburg is absent.** `proj.bib` has BD, Francis--Gaitsgory, and Costello--Gwilliam entries, but no Ginzburg reference. Do not mention a Ginzburg convention unless the exact citation and comparison theorem are added.

5. **Projection-finite and wrapped sectors must stay separate.** Ordinary `Fact(Ran(E))` applies only to the `b=0` projection-finite sector. Positive elliptic degree must be routed through `Ran^{hyb}(E)`, rigidified wrapped modules, mixed Hall correspondences, and quotient-after-correspondence.

6. **`Sp^{ch}_{K3,E}` is supplied data.** It is not ordinary proper pushforward, not BD/CG equivalence, not source bar-cobar inversion, and not a consequence of the determinant.

7. **QME/anomaly language must be typed.** Current `main.tex:6092-6099` still has an "or" in the quantum equation. Choose one convention, define the degrees/signs of `d_R`, bracket, and `Delta_R^{BV}`, and make `omega_QME,R` and `omega_anom,R` explicit finite cochains.

## main.tex anchors

1. `main.tex:95-168`: abstract target/source split is good but still says "holomorphic E_3-factorization algebra" before model conventions are fixed.

2. `main.tex:280-294`: abstract mentions `C_X`, bar comparison, cobar map, Koszul ML, and primitive recognition. This needs an immediate firewall footnote/table that these are supplied source data, not outputs of target BD/FG machinery.

3. `main.tex:5560-5635`: denominator algebra identity. Stable imported target.

4. `main.tex:5707-5722`: strong firewall paragraph. Keep and reuse this as the local standard for every later compact-source claim.

5. `main.tex:5724-5768`: formal current envelope. Correct target construction, but label `thm:factorization-square-root` is unsafe. Expand to curve-universal `C`, and reserve `E` for physical specialization.

6. `main.tex:5770-6012`: holomorphic `E_3` upgrade and finite `K3 -> E` specialization. Split into model convention, local `E_3` shadow, and rectified finite specialization. Remove any residual unqualified equivalence.

7. `main.tex:6024-6140`: compact `E_3` source interface. Good certificate list, but QME equation must be fixed and the primary model category must be named earlier.

8. `main.tex:6404-6504`: target-internal bar-cobar and source-target separation. This is the core firewall. Promote its rule into a boxed table or "Forbidden implications" display.

9. `main.tex:6506-6728`: chiral Koszul source certificate. Strong and mostly correct; keep the ban on defining source data from target bar/cobar.

10. `main.tex:6731-6970`: canonical finite source-bar coalgebra and remaining cobar obstruction. Good, but the title should stress "conditional on supplied hybrid source."

11. `main.tex:7039-7119`: projection-to-`E` support-locality obstruction. This is theorem-level and should be the reason `Fact(Ran(E))` cannot host the `s`-direction.

12. `main.tex:7121-7850`: hybrid local/wrapped certificate. This is the required source shape, not constructed compact geometry until `O_hyb,R=0`.

13. `main.tex:10994-11174`: finite Hall source kernel. Conditional source kernel, not target data.

14. `main.tex:11750-12121`: Dirac--Igusa certificate. Correctly says target current envelope and target bar-cobar counit do not imply compact realization.

15. `main.tex:12124-12308`: primitive recognition certificate. Conditional. Do not let labels or cross-references imply source construction.

16. `main.tex:13276-13414`: state-side construction open problem. This should be cross-referenced from every theorem or proposition that says "suppose a compact Hall/factorization construction supplies..."

## Patch queue

1. Add a compact "BD/FG firewall" table immediately after the formal current envelope: target current envelope, target bar coalgebra, target counit, source hybrid object, source coalgebra, source bar comparison, source-to-target cobar map, and primitive recognition, with "constructed/imported/supplied/open" status.

2. Rename the formal current envelope theorem alias. Replace `thm:factorization-square-root` with a target-only label such as `prop:formal-denominator-current-envelope`. This is not cosmetic: theorem-style aliases contaminate later `cref` output.

3. Generalize the formal target from `E` to a smooth curve `C`; then add an "elliptic specialization" paragraph explaining why compact geometry forces `C=E` only for `K3 x E`, OP/DT quotient, elliptic degree, and wrapped anchors.

4. Add the source-free algebraic target package `D^{alg}_{Delta_5,C,L}` only as a formal target tuple. Include the rule that its target bar-cobar counit is not `C_X`.

5. Split the "Holomorphic E_3 quantum upgrade" section into three definitions: primary holomorphic factorization source model; local `E_3` shadow after formality/framing; rectified finite `K3 -> E` specialization. This follows Agent 06 and the attack PDF items `127-145`.

6. Replace generic `F_X` shorthand in firewall-sensitive statements with `F_X^{(0)}`, `F_X^{(1)}`, or `F_X^{hyb}`. Make it impossible to read the projection-finite shadow as the full source.

7. Fix the finite BV/QME paragraph by choosing one quantum master equation convention and typing `Delta_R^{BV}`, `d_R`, the bracket, anomaly cocycle, and null-homotopies.

8. Insert a "Koszul layers and forbidden conflations" table near `main.tex:6404`: target chiral bar-cobar, source chiral bar/cobar, source-to-target cobar comparison, operadic `E_3` formality, and primitive Lie/Hopf Koszul signs.

9. Retitle `Canonical finite source-bar coalgebra` as conditional: "Canonical source-bar coalgebra after a supplied hybrid source." Add a first sentence: "This proposition does not construct `F^{hyb}_{X,R}`."

10. Add cross-references from compact realization, primitive recognition, and final theorem-status ledger back to `op:compact-igusa-realization` and `def:chiral-koszul-source-certificate`.

11. Add a source-data schema pointer, following Agent 25, saying a compact-source certificate requires machine-checkable finite data: source provenance, matrices for products/brackets/coproducts, pairings, radicals, PBW, normal-ordering cochains, orientation, and transitions. Target-only fixtures must be rejected as compact-source certificates.

12. Audit every occurrence of "equivalently factorization algebra on Ran(E)", "E_3-factorization algebra", "Koszul duality", "recognition target", and "current envelope" for source/target status in the local sentence.

## Residual proof/source obligations

1. Fix the primary holomorphic factorization model and the exact chain operad. Without this, `E_3` remains suggestive language.

2. Specify the formality torsor point, framing/homotopy witness, field of definition, holomorphic-polydisc comparison, and transition compatibility.

3. Construct finite BV/QME/anomaly cochains, not just the typed obstruction tuple.

4. Prove finite-type compact Hall stages `[K3 x E-fin]`, finite d-critical Hall atlas `[K3 x E-atlas]`, residual inertia control, BBDJS coefficient systems, orientations, and admissible six-functor pull-push maps.

5. Prove finite HN transition compatibility and the relevant Mittag--Leffler exactness, including `R^1 lim = 0` for source coalgebras, completed bar/cobar systems, target truncations, and comparison cones.

6. Construct the hybrid local/wrapped source: rigidified wrapped prequotients, anchors, ordered mixed correspondences, wrapped-wrapped correspondences, eight two-step flags, higher colored configuration atlas, quotient-after-correspondence, and protected integration.

7. Construct `C_{X,R}` from the supplied hybrid source, with finite filtration, collision coproduct, conilpotence, source bar comparison, transition maps, and source-internal bar-cobar admissibility.

8. Construct the source-to-target cobar quasi-isomorphism `Theta_{Kos,R}` and prove compatibility with transitions and primitives. Target FG counit does not reduce this obligation.

9. Construct finite Hall source kernels and normal-ordering cochains on actual correspondence targets. The lattice homomorphism and target exponent table are insufficient.

10. Construct primitive representatives, full parity dimensions, Hopf pairings, closed radical quotient, relation checks, PBW, and no-extra-relations theorem. Signed superdimension equality is not enough.

11. Construct orientation/Pfaffian quotient data and Weyl monodromy before identifying Hall orientation character with the Maass character. The constants `64`, `4096`, and the OP minus sign are target/scalar normalizations only.

12. If any Ginzburg convention is invoked, add the exact citation and comparison theorem. Otherwise keep the comparison language strictly BD / Costello--Gwilliam / Francis--Gaitsgory as currently cited.
