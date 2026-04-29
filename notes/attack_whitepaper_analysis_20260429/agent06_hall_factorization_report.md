# Agent 06 Hall / Factorization Attack Report

Scope: compact Hall source, holomorphic `E_3` language, Costello--Gwilliam / Beilinson--Drinfeld / Ginzburg ambiguity, `Ran(E)` projection-finite locality obstruction, wrapped/global sector, mixed Hall action, finite-first HN completion, formality point, QME/anomaly control.

Status: the manuscript has largely healed the first-order lattice and normal-ordering defect. The remaining attack surface is not the Borcherds product. It is the source category. Every theorem-level use of compact Hall/factorization language must be read as conditional until the finite source, rectification, hybrid wrapped, QME/anomaly, and HN transition certificates are supplied.

## Required Definitions

1. **Primary holomorphic source category.** Define first a model category or stable infinity-category
   `Fact^hol_X(Ch_C)` or `Fact^hol(X; Ch_C)` for holomorphic factorization algebras on `X = K3 x E`. The current phrase "factorization algebra on X in the sense of Costello--Gwilliam ... equivalently a factorization algebra in the holomorphic E_3-operadic sense" at `main.tex:5778-5785` still compresses two structures. It must state the chosen model: Costello--Gwilliam cosheaf/factorization algebra, a holomorphic disk/polydisk operad, or a rectified chain-operadic model.

2. **Local `E_3` shadow.** Define the local object only after the primary holomorphic source:
   `A^{loc}_{X,x} in Alg_{E_3}(Ch_C)`.
   Required inputs: a holomorphic polydisc at `x`, compact-support convention, the chosen chain operad, a formality quasi-isomorphism, a homotopy/framing datum, and the field of definition. Attack source lines `5375-5422`, `6776-6840`, and `20819-20839` all make this point. The current manuscript lists the ingredients at `main.tex:6024-6140`, but it does not yet name the actual operad/model category before using the `E_3` symbol.

3. **Formality point.** The phrase "fixed `E_3`-formality point" must be a definition, not a noun. It should specify whether `\varphi_R^{E_3}` is a torsor point of quasi-isomorphisms
   `C_*(E_3) -> H_*(E_3)`, a framed-little-disks datum, a holomorphic-polydisc-to-little-disks comparison, or a model-dependent rectification. Current anchors: `main.tex:6037-6057`, `6117-6119`, `6328-6350`. Attack source lines `21463-21470` ask exactly this.

4. **BD / CG / Ginzburg convention.** The manuscript currently cites Beilinson--Drinfeld at `proj.bib:61-66` and Costello--Gwilliam at `proj.bib:431-449`, and uses the comparison language at `main.tex:5821-5847`, `6000-6005`, `6375-6381`. It has no `Ginzburg` entry or reference in `main.tex` / `proj.bib` / the attack file (`rg Ginzburg` returned no hits). Either:
   - do not mention Ginzburg at all; or
   - add the exact Ginzburg convention and comparison theorem needed.
   In either case, "`chiral algebra on E`, equivalently factorization algebra on `Ran(E)`" is forbidden without a named BD/CG/formality comparison map.

5. **Rectified `K3 -> E` specialization.** Define `Sp^{ch}_{K3,E}` as a finite-chain functor/correspondence with source category, target category, support condition, charge grading, model-category or infinity-categorical rectification, product/unit squares, and HN transition squares. Current anchors: `main.tex:5804-5853`, `5854-6012`, and Definition `main.tex:5981-6022`. Attack source lines `559-599`, `6820-6840` say the same: the specialization is the missing construction, not part of the product proof.

6. **Projection-finite sector.** Keep `projection-to-E support-locality obstruction` as the theorem-level phrase. The current lemma at `main.tex:7082-7101` is correct: positive elliptic degree implies `p_E(C)=E`. The corollary at `main.tex:7103-7119` correctly says ordinary support-local factorization on `Ran(E)` sees only the projection-finite sector. Do not broaden this into a general spacetime-locality obstruction.

7. **Hybrid local/wrapped source.** Define the hybrid object as a finite colored correspondence-module system, not as `Ran(E) x {b}` with a scalar label. The current Definition `main.tex:7121-7850` is the right shape: local closed-configuration stacks, rigidified wrapped prequotients, anchors, ordered local/wrapped and wrapped/wrapped correspondences, eight two-step flag stacks, quotient-after-correspondence, protected integration, and HN transitions. The degree shadow at `main.tex:7071-7079` must never be used as the actual category.

8. **Mixed Hall action.** Define both ordered actions `local-wrapped` and `wrapped-local`, plus wrapped-wrapped operations, before using the phrase "mixed Hall action." Current anchors: `main.tex:7333-7382`, `7468-7508`, `7970-8027`, `8051-8080`. The action is not a scalar Fock mode and not a detached Hecke factor.

9. **Finite Hall source kernel.** A compact Hall source must be a finite source kernel at each HN height before normal-ordering or comparison with `g_{\Delta_5}`. Current definition: `main.tex:10994-11091`; construction from supplied kernel: `main.tex:11093-11174`. The kernel must include finite residual inertia, BBDJS coefficients, orientation lines, admissible pull-push maps, coproduct, two-step flags, and normal-ordering cochains acting on actual correspondence targets.

10. **Finite-first HN completion.** The inverse limit is legal only after finite HN stages and transition maps are defined. The manuscript has the correct finite-first skeleton at `main.tex:9930-9970`, `9973-10450`, and the [ML] condition at `main.tex:10090-10120`. The reportable gap is existence: [K3 x E-fin], [K3 x E-atlas], and [ML] are supplied hypotheses, not proved theorems.

11. **QME/anomaly data.** The QME and anomaly controls must be explicit cochains in a finite BV complex. Current text makes a serious start at `main.tex:6063-6116` and typed obstruction tuple `main.tex:6192-6231`. Remaining ambiguity: `main.tex:6094-6097` presents the quantum equation with an "or"; choose one convention and type the degree/sign of `\Delta_R^{BV}` and the differential. Attack source lines `21471-21478` explicitly require cochains, not words.

12. **Source chiral Koszul coalgebra.** `C_X` must be source-side data attached to the hybrid source, not a construction from the target current envelope. Current anchors: `main.tex:12049-12103`, `13263-13414`. Attack source lines `24483-24578` contain the same prohibition.

13. **Primitive recognition certificate.** The compact primitive algebra is not produced by the determinant. It requires source primitive representatives, parities, BKM relations in the Hall bracket, completed Hopf pairing, radical quotient, PBW compatibility, and no-extra-relations theorem. Current anchors: `main.tex:12124-12308`, `13295-13408`.

## Forbidden Theorem-Level Terms

Use these only inside a definition of supplied data or an open problem, never as constructed theorem output:

1. "`holomorphic E_3-factorization algebra on K3 x E`" without the chosen holomorphic factorization category, operad, formality point, and framing datum.

2. "`E_3`" as a synonym for complex dimension three. Replacement: "holomorphic factorization source with a local `E_3` shadow after the chosen formality/framing datum."

3. "`chiral algebra on E, equivalently factorization algebra on Ran(E)`" without naming the BD/CG/formality comparison and its support hypotheses.

4. "`Sp^{ch}_{K3,E}`" or "`K3 -> E specialization`" as if it were a known functor. Replacement: "supplied rectified finite `K3 -> E` specialization datum."

5. "`Fact(Ran(E))`" for the full compact object. Replacement: "projection-finite `Ran(E)` sector plus hybrid wrapped correspondence-module object."

6. "`locality obstruction`" unqualified. Replacement: "projection-to-`E` support-locality obstruction."

7. "`global Fock/Hecke sector`" as a repair. Replacement: "rigidified wrapped prequotients with anchors, acted on by ordered mixed Hall correspondences before reduced `E` quotient."

8. "`compact Hall source`" for the formal BD current envelope. Replacement: "formal target current envelope." Current target envelope anchors: `main.tex:5724-5768`.

9. "`finite HN completion`" without finite stages and [ML]. Replacement: "finite-first HN inverse system satisfying [K3 x E-fin], [K3 x E-atlas], and [ML]."

10. "`QME/anomaly control`" without finite BV complex, anomaly cocycle, and null-homotopy. Replacement: "finite QME/anomaly cochains `\omega_{QME,R}`, `\omega_{anom,R}` with specified null-trivializations."

11. "`orientation line` implies `Pfaffian square root` or `Maass character`." Replacement: "orientation line plus quotient descent, Weyl transport, finite-stabilizer character vanishing, and reflection-sign computation."

12. "`g_{\Delta_5}` implies compact Hall source." This is explicitly forbidden by attack source `20890-20913` and by current manuscript `main.tex:11761-11763`, `12191-12193`, `13210-13413`.

## Replacement Language

1. Replace theorem-level "`A_X^{E_3}` is a holomorphic `E_3`-factorization algebra" with:
   "A compact realization must supply a finite-first holomorphic factorization source interface `\mathbb A_{X,\sigma,S}^{E_3}` in a named model, together with a chosen local `E_3` formality/framing datum."

2. Replace "`\mathcal F_X in Fact(Ran(E))`" with:
   "The projection-finite output is `\mathcal F_X^{(0)}` on `Ran(E)` after the rectified `K3 -> E` specialization. The full positive elliptic-degree object is the hybrid source `\mathcal F_X^{hyb}` over `Ran^{hyb}(E)`."

3. Replace "`BD/CG equivalence`" with:
   "A supplied comparison `\kappa_{E,R}` between the Beilinson--Drinfeld chiral presentation and the Costello--Gwilliam factorization presentation, inside named finite model categories, with product/unit/HN transition squares null-trivialized."

4. Replace "`formality point`" with:
   "A specified torsor point `\varphi_R^{E_3}` of operadic quasi-isomorphisms for the chosen chain `E_3` model, compatible with the holomorphic-polydisc local model and the finite HN transitions."

5. Replace "`QME and anomaly cancellation`" with:
   "A finite BV complex `C_R^{BV}`, action `S_R`, anomaly cocycle `\mathfrak a_R`, obstruction class `[\mathfrak a_R]`, and cochains killing the QME and anomaly classes compatibly with `\rho_{R'R}`."

6. Replace "`wrapped sector`" with:
   "Rigidified wrapped prequotient stacks `\mathcal M_{\eta,R}^{wr,rig}` with anchors `\lambda_{\eta,R}`, ordered mixed extension stacks, wrapped-wrapped stacks, eight-word flag stacks, quotient-after-correspondence functor `Q_{E,R}`, and protected trace with `s`-degree `b_R`."

7. Replace "`normal-ordered pushforward`" with:
   "A chain-level normal-ordering package `\Theta_{\Pi,R}`, `\Theta_{\Pi,R}^-` acting on finite Hall correspondence targets and satisfying the NO1--NO7 diagrams; the lattice homomorphism alone is not this package."

8. Replace "`compact recognition theorem`" with:
   "Primitive recognition certificate from a supplied source: representatives, parities, BKM relations, pairing radical quotient, PBW compatibility, and no-extra-relations theorem."

## Exact Certificate Checklist

A compact Hall/factorization claim in this scope must provide all entries below.

1. **Source model.** Named category for holomorphic factorization on `X`, chosen chain `E_3` operad, local holomorphic-polydisc model, compact-support convention, and model-category/infinity-categorical rectification calculus.

2. **Finite BV/QME package.** For every finite HN height `R`: cyclic finite `L_\infty` algebra or equivalent local BV presentation, `C_R^{BV}`, action `S_R`, bracket, BV Laplacian, anomaly cocycle, QME cocycle, and null-homotopies compatible with `R' -> R`.

3. **Formality/framing.** Torsor point `\varphi_R^{E_3}`, framing/homotopy witness `\tau_R^{fr}`, field of definition, and transition compatibility.

4. **Finite Hall support.** [K3 x E-fin]: finite-type semistable substacks in bounded HN height, with base `E` Pic/Bun directions bounded, rigidified, or included in the full charge. Current anchor: `main.tex:9982-10057`.

5. **Finite d-critical Hall atlas.** [K3 x E-atlas]: finite object, extension, and flag stacks; finite residual inertia; BBDJS vanishing cycles; orientations; semiregularity cosections; admissible six-functor pull-push; reduced `E` quotient as a functor. Current anchor: `main.tex:10058-10089`.

6. **HN inverse system.** Cofinal finite HN subsystem, transition maps, and [ML] stable-image condition on every finite window. Current anchor: `main.tex:10090-10120`.

7. **Finite `K3 -> E` rectification.** Objects `A^{E_3}_{X,R}`, `F^{(0)}_{X,R}`, `F^{(1)}_{X,R}`, `(p_E)_!^{fact}A^{E_3}_{X,R}`, maps `Sp_R`, `\kappa_{E,R}`, `\pi^{ch}_{*,R}`, product/unit squares, and obstruction tuple `\mathfrak O^{K3->E}_R=0`. Current anchors: `main.tex:5854-6012`.

8. **Projection-finite local sector.** Closed configuration stacks over `E^I`, exceptional pushforward admissibility, Thom--Sebastiani compatibility, and recovery of open-support notation as a theorem, not primary data. Current anchors: `main.tex:7176-7242`.

9. **Wrapped sector.** Rigidified wrapped prequotients, unit-weight/lossless anchors, anchor transition compatibility, wrapped Borel--Moore spaces, and vanishing of `\mathfrak o^\lambda_R`. Current anchors: `main.tex:7244-7331`.

10. **Mixed and wrapped correspondences.** Local-local, ordered local-wrapped, wrapped-local, and wrapped-wrapped extension stacks before quotienting; admissible `q_!`, `p^*`, Thom--Sebastiani, and anchor memory. Current anchors: `main.tex:7333-7508`.

11. **Associativity/coherence.** Eight two-step binary flags `LLL`, `LLW`, `LWL`, `WLL`, `LWW`, `WLW`, `WWL`, `WWW`, plus four-input pentagon and higher colored configuration residual `\mathfrak o^{col}_R`. Current anchors: `main.tex:7510-7569`, `7738-7802`.

12. **Quotient-after-correspondence.** Functor `Q_{E,R}` on the finite correspondence category after local/wrapped/mixed correspondences exist; comparison maps `\theta^Q_{\mu,R}`; quotient residuals `\mathfrak o^{Q,*}_R=0`. Current anchors: `main.tex:7571-7634`, `8051-8080`.

13. **Protected integration.** Chain-level character `I_R^{prot}` compatible with products, coproducts, primitives, colored refinements, quotient maps, and transitions; homogeneous `s`-degree equal to elliptic degree `b_R`. Current anchors: `main.tex:7636-7736`.

14. **Hybrid residual.** Full vanishing of `\mathfrak O_{hyb,R}` for every finite `R`, including transition components. Current anchors: `main.tex:7738-7850`, open problem `main.tex:8254-8303`.

15. **Normal-ordered charge extension.** Lattice extension `\widehat\Gamma_X`, finite labels `\widehat\Gamma_R`, no-overcount residuals, and chain-level `\Theta_{\Pi,R}` acting on actual correspondence targets. Current anchors: `main.tex:10127-10173`, `10414-10440`, `12004-12048`.

16. **Finite Hall source kernel.** Source kernel `\mathfrak S_R`, finite bialgebra object, product/coproduct, primitive bracket, transition-compatible kernels. Current anchors: `main.tex:10994-11174`.

17. **Finite Hall--Dirac atlas.** `\mathfrak A_R`, Dirac complex, Pfaffian square, compact parity lifts, protected integration, successor transition diagrams. Current anchors: `main.tex:11282-11516`.

18. **Source chiral Koszul data.** `C_{X,R}`, filtration, collision coproduct, bar comparison to the hybrid source, cobar quasi-isomorphism to the target current envelope, Koszul [ML], and residual `\mathfrak O_{Kos,R}=0`. Current anchors: `main.tex:12049-12103`, `13363-13394`.

19. **Primitive recognition.** Source-side root representatives, parities, BKM relations, real Serre checks, isotropic relations, pairing radical quotient, generation/PBW/no-extra-relations. Current anchors: `main.tex:12124-12308`, `13395-13408`.

20. **Forbidden implication audit.** Each use must explicitly block:
   `D_X = \Delta_5` does not imply compact `D_X`;
   `\Delta_5^2` does not imply orientation monodromy;
   `g_{\Delta_5}` does not imply compact Hall source;
   target current envelope does not imply source coalgebra;
   quotient by `E` before wrapped correspondences destroys mixed Hall data.

## Current Anchors

Attack-source anchors:

- Initial underdefinition of `E_3` and repair language: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:493-623`.
- Hall grading repair: physical charges, Gram pushforward, cocycle defect, and bracket descent: `1594-1713`, `1780-1835`, `3147-3423`, `3800-4027`.
- Constructive local/BV/factorization/hybrid story: `2140-2503`, bracket/descent language `2535-2576`.
- Later diagnosis that local factorization is physically right but mathematically underdefined: `5368-5422`.
- Hybrid object promoted to `Ran^{hyb}(E)` / wrapped module sectors: `5453-5510`, `6706-6774`, `9760-9870`.
- Compact Dirac--Igusa finite atlas as the actual open theorem: `10272-10340`.
- Current warning that `E_3` still needs the source category and operad before obstruction lists: `20819-20839`.
- Required local/hybrid checklist items: `21455-21487`, `24472-24584`.
- Formal current envelope should be curve-universal, with `E` the physical specialization: `17368-17406`, `18621-18687`.

Manuscript anchors:

- Abstract no-overclaim ledger and compact source requirements: `main.tex:131-169`.
- Introduction: compact and hybrid factorization, projection-finite obstruction, mixed Hall data: `main.tex:226-258`.
- Local object and `Ran(E)` obstruction: `main.tex:480-559`.
- Local protected observable algebra schema: `main.tex:570-618`; external assumptions and compactness gap: `621-635`.
- Formal target current envelope: `main.tex:5724-5768`.
- Holomorphic `E_3` upgrade and BD/CG comparison language: `main.tex:5770-5853`.
- Rectified finite `K3 -> E` diagram and obstruction tuple: `main.tex:5854-6012`.
- Compact `E_3` source interface, finite QME/anomaly/formality/HN package: `main.tex:6024-6140`.
- Formal finite BV skeleton caveat and first wrapped primitive test `(0,1,1)`: `main.tex:6142-6190`.
- Typed compact `E_3` obstruction tuple and zero-source equivalence: `main.tex:6192-6267`.
- Open problem requiring QME, anomaly, formality, finite-first HN, hybrid repair: `main.tex:6320-6355`.
- Projection-finite/wrapped/hybrid strata and locality lemma: `main.tex:7039-7119`.
- Hybrid certificate: `main.tex:7121-7850`.
- Consequences, no quotient-first repair, O2/hybrid compatibility, and hybrid open problem: `main.tex:7970-8303`.
- Conditional normal-ordered Hall descent theorem, including homotopy `E_3` caveat: `main.tex:8603-8685`.
- Sectorial Hall truncation and finite HN shape: `main.tex:9930-9970`.
- `D_0` finite-first certificate and [K3 x E-fin] / [K3 x E-atlas] / [ML]: `main.tex:9973-10450`.
- Finite Hall source kernel and source package: `main.tex:10994-11174`.
- Finite Hall--Dirac atlas and exact parity/Pfaffian ambiguity: `main.tex:11282-11660`.
- Full Dirac--Igusa certificate: `main.tex:11750-12121`.
- Primitive recognition certificate: `main.tex:12124-12308`.
- State-side construction open problem: `main.tex:13276-13414`.

Bibliography anchors:

- Beilinson--Drinfeld chiral algebras: `proj.bib:61-66`.
- Kontsevich--Soibelman CoHA: `proj.bib:311-320`.
- Operad/formality references: `proj.bib:323-353`.
- Costello / Costello--Li / Costello--Gwilliam: `proj.bib:406-449`.
- BBDJS vanishing cycles: `proj.bib:627-635`.
- No Ginzburg reference is present in `main.tex` or `proj.bib`.

## Rewrite Actions

1. Insert an early convention box:
   "Model conventions for factorization/chiral language." It must choose the primary holomorphic factorization model, state how BD chiral algebras enter on the curve, state whether Ginzburg is unused or cited, and reserve `\kappa_E` for a supplied comparison.

2. Rewrite `main.tex:5770-5853` into three separate definitions:
   - holomorphic factorization source;
   - local `E_3` shadow after formality/framing;
   - rectified finite `K3 -> E` specialization.
   Remove any unqualified "equivalently" between CG factorization, BD chiral algebra, and operadic `E_3`.

3. Replace all theorem-level uses of `\mathcal A_X^{E_3}` with "supplied source interface" unless the sentence is explicitly inside the compact-realization datum or open problem.

4. In the QME paragraph `main.tex:6091-6099`, choose one quantum master equation convention and remove the "or". Define degrees and signs for `\Delta_R^{BV}`, the bracket, and `Q_R`.

5. In the abstract and introduction, keep the phrase "projection-to-`E` support-locality obstruction"; audit any remaining bare "locality obstruction" or "locality failure" language.

6. Strengthen the BD/CG paragraph `main.tex:5821-5847`:
   state that `\mathcal F_X^{(0)}`, `\mathcal F_X^{(1)}`, and `(p_E)_!^{fact}\mathcal A_X^{E_3}` are distinct until `\mathfrak O^{K3->E}_R=0`; do not call them equivalent before that.

7. Keep Definition `main.tex:7121-7850`, but add a short "not enough" sentence before the degree shadow: `Ran(E) x {b}` is not the hybrid category. The current text says this at `main.tex:7058-7079`; make it impossible to miss.

8. Add a theorem-status table near the compact section:
   formal current envelope = constructed target;
   finite Hall kernel = supplied source input;
   hybrid wrapped source = open finite certificate;
   source chiral Koszul coalgebra = open source construction;
   primitive recognition = certificate, not determinant theorem.

9. If retaining the formal current envelope only over `E`, add a sentence explaining that `E` is chosen because of the compact `K3 x E` physical source, not because the BD current construction is intrinsically elliptic. Better: define the formal current envelope over a smooth curve `C`, then specialize to `C=E`.

10. Keep `main.tex:13276-13414` as the final open obligation, but cross-reference it from every theorem that says "suppose a compact Hall/factorization construction supplies..."

11. Add a local "forbidden implications" table:
   determinant identity does not construct source;
   target current envelope does not construct source coalgebra;
   orientation line does not compute Maass character;
   projection-finite Ran object does not see the `s`-direction;
   scalar Fock/Hecke factor does not give mixed Hall brackets;
   `\Gamma_{gram}` is not the raw Hall charge lattice.

## Residuals

1. **Primary model residual.** The manuscript has a good finite obstruction language, but no single primary holomorphic factorization category or chain operad has been fixed. This is the largest remaining underdefinition.

2. **BD/CG/Ginzburg residual.** BD and CG are cited; Ginzburg is absent. The manuscript must either remove Ginzburg-type ambiguity by convention or add the missing reference and comparison. Current "BD/CG/formality comparison" language is conditional but still too compressed for theorem-level use.

3. **Formality residual.** A Tamarkin--Kontsevich formality torsor point is named, but no exact operadic quasi-isomorphism, field, associator, or compatibility with holomorphic polydiscs and HN transitions is fixed.

4. **QME/anomaly residual.** The finite BV skeleton and anomaly cocycle are typed. No compact finite cyclic `L_\infty` source is constructed, and the quantum equation convention remains ambiguous until the "or" is removed.

5. **Specialization residual.** `Sp^{ch}_{K3,E}`, `\kappa_E`, and `\pi_*^{ch}` are now correctly treated as supplied finite-chain comparison data. They remain unconstructed.

6. **Hybrid residual.** The hybrid wrapped certificate is detailed and serious. Its existence remains open: finite-type local/wrapped stacks, lossless anchors, admissible pull-push maps, quotient-after-correspondence, higher colored coherence, protected integration, and HN transitions are all required.

7. **Wrapped `s`-direction residual.** The `\delta_2` channel `(0,1,1)` is the first decisive test. A projection-finite source cannot supply it. The reportable certificate must produce a rigidified wrapped object of `b_R=1`, its anchor, mixed correspondences, quotient descent, and Pfaffian wall compatibility.

8. **Finite-first residual.** [K3 x E-fin], [K3 x E-atlas], and [ML] remain hypotheses. The paper should keep them visibly separate from proved lattice normal-ordering.

9. **Normal-ordering residual.** The lattice extension is proved. The chain-level `\Theta` package acting on Hall correspondences, cyclic trace, Frobenius pairing, and Hopf radical remains a source-side finite certificate.

10. **Source Koszul residual.** The target current envelope and target bar--cobar counit are constructed target objects. They do not construct `C_X`, `b_X`, or `\Theta_{Kos}`.

11. **Primitive recognition residual.** Equality of signed exponents with `f(nm,l)` does not give compact primitive representatives, parity dimensions, Hall constants, BKM relations, pairing matrices, radical quotient, PBW compatibility, or no-extra-relations. The first low-degree compact test remains the `\delta_1+\delta_2+\delta_3` channel, where the target signed dimension `-64` must become actual compact `29|93` bases with structure constants.

12. **Curve-universality residual.** The formal current envelope is presently defined over `E`. The attack source argues it should be curve-universal with `E` a physical specialization. If the manuscript keeps only `E`, it should state why the formal target is specialized there and not confuse that with the compact source.
