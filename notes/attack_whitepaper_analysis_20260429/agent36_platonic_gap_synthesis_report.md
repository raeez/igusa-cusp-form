# Agent 36 Platonic Gap Synthesis Report

Scope: adversarial synthesis of the attack PDF and all reports currently present in
`notes/attack_whitepaper_analysis_20260429/` at the time of writing. Present reports
are Agents 01-17, 19-29, and 31-33. Agents 18 and 30 are absent from the directory.

This is not the final integrated repair ledger. It is a ranked gap taxonomy for what
prevents the paper from becoming the platonic ideal paper.

## Ranked critical gaps

### 1. The compact source object is not constructed

Class: object-construction gap.

Current paper has: a long compact realization interface: finite source kernels,
Hall-Dirac atlases, recognition certificates, finite-window protocols, and open
problems around compact Dirac-Igusa realization. These are useful contracts, but
they are mostly certificate scaffolds. They do not construct the compact source
whose primitives are compared to `\mathfrak g_{\Delta_5}`.

Ideal paper needs: a constructed hierarchy:
`H^{pre}_{X,\Gamma}` from derived compact-object stacks and exact-triangle
correspondences; `H^{tw}_{X,\Gamma}` over the orientation square-root gerbe;
a hybrid local/wrapped source for the projection-to-`E` locality obstruction;
a source coalgebra or chiral coalgebra; a primitive protected quotient; and only
then a comparison theorem
`\overline\Pi_* H^0 Prim_{prot}(H^{tw}_{X,\Gamma})/Rad \cong
\mathfrak g_{\Delta_5}`.

Minimum viable repair: demote all compact realization language to a precise
problem/specification section. State explicitly that the manuscript constructs
the target automorphic determinant and target BKM algebra, proves the charge
descent obstruction/repair, and records source certificates still needed. Do not
claim a compact Dirac-Igusa realization.

Repair type: new mathematics for the ideal; section rewrite for the minimum
viable paper.

Main anchors: `main.tex:5704`, `6024`, `6192`, `6506`, `6731`, `7039`, `7121`,
`8254`, `10994`, `11282`, `11750`, `12124`, `12479`, `12590`, `13276`.

### 2. Source-side finite certificates are absent

Class: proof/certificate gap.

Current paper has: target-side arithmetic checks, especially the `W_{\le 3}`
target multiplicities including `29|93` at `\delta_1+\delta_2+\delta_3`.
The current compute scripts verify target coefficients and lattice data. They do
not provide source bases, source brackets, source coproducts, pairings, radical
quotients, PBW checks, or transition maps.

Ideal paper needs: executable finite source data. At minimum, the first saturated
window needs source basis files for each normal-ordered degree, product and
bracket matrices for all relevant mixed maps, Jacobi checks, pairing matrices,
radical bases, primitive quotient dimensions, PBW/no-extra-relation checks, and
transition/ML exactness checks. The `29|93` target count must be matched by a
compact source computation, not merely quoted from the denominator.

Minimum viable repair: label all finite source protocols as protocols or required
certificates, not as achieved source construction. Preserve the target
`W_{\le 3}` calculation as a target arithmetic fact only.

Repair type: new mathematics plus data/schema work for the ideal; local status
patches for the minimum viable paper.

Main anchors: `main.tex:9973`, `10994`, `11282`, `11518`, `11750`, `12124`,
`12479`, `12590`, `12838`, `12941`, `13205`.

### 3. Orientation is not gerbe-first

Class: object-construction gap and proof/certificate gap.

Current paper has: substantial orientation-certificate material: O1/O1+/O2,
finite stabilizer language, orientation character language, and Pfaffian
normalization targets. Some of it is likely correct as a certificate framework,
but the paper too often starts from an oriented object or from a global
orientation certificate.

Ideal paper needs: the square-root gerbe first. Define
`Or_{R,\hat c}=\sqrt{K_{R,\hat c}}`, the tautological half-density line, and
`H^{tw}_{R,\hat c}` as the anti-invariant Borel-Moore object over the gerbe.
Products, coproducts, and primitives must be constructed on the twisted object
before any O1 trivialization. O1 is then a choice/trivialization theorem, not the
starting point. The Weyl cocycle `c_o`, orientation character `\omega`, local
wall charts for O2, and `N_\delta^{Pf}=1` need actual finite certificates.

Minimum viable repair: rewrite orientation as a required gerbe/certificate
interface and avoid implying that the oriented compact source has been built.
Keep Pfaffian recognition as a target or conditional recognition statement.

Repair type: new mathematics for the ideal; section rewrite for the minimum
viable paper.

Main anchors: `main.tex:1139`, `5724`, `5743`, `5770`, `6024`, `6192`, `6506`,
`6731`, `7121`, `8603`, `11750`.

### 4. The theorem spine is hidden by certificate ledgers

Class: architecture/voice gap.

Current paper has: many important correct components, but the reader meets them
through a sprawling sequence of labels, ledgers, certificates, duplicated
denominator statements, row appendices, and recognition protocols. The attack PDF
rightly says the compact side reads like a list of certificates rather than a
constructed hierarchy.

Ideal paper needs: a spine with theorem-level contributions in this order:
virtual automorphic determinant; D6-D2-D0 Mukai-Gram dictionary; normal-ordered
charge descent theorem; raw fixed-lift no-go; conditional normal-ordered descent;
projection-to-`E` locality obstruction and hybrid wrapped repair; formal target
denominator algebra; compact source construction; primitive recognition; Dirac
Pfaffian certificate; scalar square and row consequences.

Minimum viable repair: reorder around the stable theorem spine and move row,
spin, and source-certification ledgers out of the main proof flow. Make the
compact realization problem visibly open unless the missing source construction
is supplied.

Repair type: section rewrite.

Main anchors: `main.tex:177`, `464`, `640`, `2383`, `2634`, `4309`, `5560`,
`5704`, `13701`, `13957`, `14269`, `14558`, `14689`.

### 5. The formal algebraic target is not separated from compact geometry

Class: object-construction gap and architecture/voice gap.

Current paper has: a target denominator Lie superalgebra imported from
Gritsenko-Nikulin and a formal current envelope over `E`. It does not clearly
construct the curve-universal algebraic target independent of compact geometry.

Ideal paper needs: a target object such as
`D^{alg}_{\Delta_5,C,L}`. Start with `\mathfrak g_{\Delta_5}` and a section
`L:\Gamma_{gram}\to\Gamma_{form}`. Define
`s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)` into the normal-ordered extension,
prove `\overline\Pi_X s_L=id`, regrade `\mathfrak g_{\Delta_5}` along `s_L`,
then build the curve current envelope for a smooth curve `C`. Only after this
specialize to `C=E` and ask for a compact Hall source.

Minimum viable repair: add a short target/source firewall. State that the
automorphic target is constructed independently; compact geometry is a separate
realization problem.

Repair type: section rewrite now; modest new construction for the ideal.

Main anchors: `main.tex:5560`, `5590`, `5614`, `5724`, `5743`, `6404`, `13543`,
`13603`, `13652`.

### 6. Normal-ordering is conceptually right but still has chain-level leaks

Class: proof/certificate gap and notation/build gap.

Current paper has: the correct strategic repair: two lattices, a quadratic
Gram-index map, an additivity defect `B`, a normal-ordered extension
`\widehat\Gamma_X`, additive `\overline\Pi_X`, and a raw fixed-lift no-go.
Reports identify local errors in the cochain language and placement of the raw
split.

Ideal paper needs: a clean chain-level normal-ordering theorem. Distinguish
`B`, `B_{ch}`, `B_C`, and `\overline B_E^{ch}`; define raw homogeneous/fixed-lift
pushforward before the no-go; avoid false `H^2_{sym}` implications; use the split
`s(c)=(c,\Pi(c))` when required; and state denominator grading comparison through
the additive extension.

Minimum viable repair: apply the local cochain and notation patches before
claiming normal-ordered Hall descent. Keep the conditional descent theorem
conditional on source data and compatibility.

Repair type: local patch plus section rewrite.

Main anchors: `main.tex:4316`, `4431`, `4523`, `4590`, `4614`, `4832`, `4883`,
`8348`, `8603`, `9132`, `9654`.

### 7. The D6-D2-D0 dictionary is a theorem but is under-promoted

Class: architecture/voice gap and notation/build gap.

Current paper has: the corrected dictionary
`v_X(I_Y)=(1,0,1-d)\otimes 1_E+(0,-\beta,-n)\otimes\omega_E` and
`\Pi_X(Q_Y,P_Y)=(\beta^2/2,n,d-1)`, so for `\beta_h` one gets
`(h-1,n,d-1)`. It is presently easy for this to be buried as a lemma.

Ideal paper needs: this as one of the main theorems. It is the bridge that turns
physical charges into Gram indices and makes the normal-ordering problem
mathematically unavoidable.

Minimum viable repair: promote it in the introduction and theorem list; ensure
all later `m` variables consistently mean `d-1`; add a boxed warning that the
raw triple is not an additive Hall charge.

Repair type: local patch plus section rewrite.

Main anchors: `main.tex:2634`, `2661`, `2760`, `4309`, `4316`, `4431`.

### 8. Determinant data are repeatedly over-read as Hall structure

Class: proof/certificate gap and architecture/voice gap.

Current paper has: a correct imported BKM denominator and coefficient
dictionary, but multiple sections risk implying that the automorphic determinant
determines brackets, parity splits, PBW structure, Hopf radicals, or compact
source operations.

Ideal paper needs: a strict determinant-forgets-structure firewall. The
denominator determines signed superdimensions and Weyl/imaginary-root
multiplicities under the imported GN theorem. It does not determine Hall
constants, source brackets, parity refinements, no-extra-relations, or compact
realization data.

Minimum viable repair: keep the existing "what denominator determines" material
but move it earlier and enforce it everywhere recognition language appears.

Repair type: local patch plus section rewrite.

Main anchors: `main.tex:2530`, `5590`, `5614`, `12804`, `13543`, `13603`,
`13652`, `14031`.

### 9. Source citations do not yet support the exact burdens placed on them

Class: source/citation gap.

Current paper has: many relevant sources, but reports identify missing or
insufficiently pinned primary-source anchors. The highest-risk items are GN/GNII
normalization, OP/Oberdieck scalar square and chamber/sign conventions,
Clery-Gritsenko and Govindarajan row data, orientation/factorization technology,
group cohomology/stabilizer calculations, and Borel-Moore convolution if used.

Ideal paper needs: every imported theorem and every row-level numerical datum
with exact primary anchors. Technology sources must be used only for the
technology they actually provide. If the paper uses Borel-Moore convolution, it
needs a standard convolution reference. If finite stabilizer cohomology is used
without source, make those computations self-contained.

Minimum viable repair: build a citation audit table and remove unsupported
appendix claims from the main theorem path.

Repair type: local patch plus companion note/citation appendix.

Main anchors: `main.tex:2530`, `13724`, `13806`, `13885`, `14339`, `14575`,
`14986`, `15470`.

### 10. Row and spin material pollute dependency closure

Class: architecture/voice gap and source/citation gap.

Current paper has: eight diagonal-divisor rows and spin `L`-factor
normalization material. Reports agree these are not dependencies for the core
`N=1` determinant/descent theorem. They carry high source burden and distract
from the main object-construction gap.

Ideal paper needs: either a compact independent consequences section with exact
status tags, or companion notes. The spin material especially should not be in
the main proof path unless the paper is explicitly about spin factorization.

Minimum viable repair: quarantine rows as independent checks/consequences and
move spin to a companion note or a one-sentence pointer near the scalar square.

Repair type: companion note or appendix compression.

Main anchors: `main.tex:14269`, `14289`, `14339`, `14558`, `14575`, `14689`,
`14986`, `15470`.

### 11. The opening still overclaims with physical vocabulary

Class: architecture/voice gap.

Current paper has: phrases such as physical, BPS, operator, one-particle,
realization, recognition, canonical, and Dirac-Pfaffian in contexts where the
mathematical status varies from proved target theorem to conditional certificate
to open compact source problem.

Ideal paper needs: status-controlled vocabulary. "Physical" should mean a
dictionary or interpretation with named hypotheses; "BPS" should not substitute
for a constructed protected cohomology object; "recognition" should be a finite
certificate theorem or explicitly conditional; "realization" should be reserved
for an actual source object and comparison map.

Minimum viable repair: rewrite the opening as a mathematical paper: theorem
spine first, status tags second, physical interpretation third. Rename the
one-particle section if it is really an index/determinant construction.

Repair type: section rewrite.

Main anchors: `main.tex:177`, `464`, `640`, `833`, `853`, `882`, `1139`.

### 12. Notation and build hygiene still threaten correctness

Class: notation/build gap.

Current paper has: multiple colliding names for charge lattices, determinant
objects, scalar normalizations, normal-ordering cochains, and recognition
certificates. Reports also identify local build or label hazards, including
undefined symbols and misleading aliases.

Ideal paper needs: a notation firewall:
`\Gamma_{form}` for additive Hall/formal charge, `\Gamma_{gram}` for Borcherds
Gram degree, raw `\Pi_X` for the quadratic map, `\overline\Pi_X` for the
additive extension, `D_5=64^{-1}\Delta_5`, `\mathcal D_X` for the virtual
determinant only if consistently defined, and separate names for certificates
versus constructed objects.

Minimum viable repair: fix undefined `\Gamma_{eff}^+`, label aliases, raw split
notation, OP variable conventions, and determinant names before any integrated
rewrite.

Repair type: local patch.

Main anchors: `main.tex:286`, `833`, `853`, `1954`, `2383`, `4366`, `4811`,
`5743`, `13724`, `13806`, `13885`.

## Gap taxonomy table

| Rank | Gap | Class | Current paper has | Ideal paper needs | Minimum viable repair | Repair type |
|---:|---|---|---|---|---|---|
| 1 | Compact source object absent | object-construction | Interfaces, atlases, kernels, recognition certificates | Constructed `H^{pre}`, `H^{tw}`, hybrid source, source coalgebra, primitive quotient, comparison theorem | Demote to compact realization problem/spec | Section rewrite now; new mathematics for ideal |
| 2 | Source finite certificates absent | proof/certificate | Target `W_{\le3}` arithmetic and denominator coefficients | Source bases, matrices, radicals, PBW, Jacobi, transitions, ML exactness | Say target calculation is target-only; list missing source certificates | Local status patches; new data/math |
| 3 | Orientation not gerbe-first | object-construction / proof | O1/O1+/O2 certificate language | Square-root gerbe, tautological line, `H^{tw}`, gerbe-lifted operations before trivialization | Recast as gerbe/certificate interface | Section rewrite; new mathematics |
| 4 | Theorem spine hidden | architecture/voice | Ledger-heavy sequence of certificates and appendices | Ordered theorem narrative from determinant through descent to source comparison | Reorder, compress ledgers, expose open compact problem | Section rewrite |
| 5 | Formal algebraic target not isolated | object-construction / architecture | GN denominator plus current envelope over `E` | `D^{alg}_{\Delta_5,C,L}` independent of compact geometry | Add target/source firewall | Section rewrite; modest new construction |
| 6 | Normal-ordering chain leaks | proof/certificate / notation | Correct high-level extension and no-go | Clean cochains, raw pushforward definitions, additive comparison | Apply cochain/split/status patches | Local patch plus section rewrite |
| 7 | D6-D2-D0 bridge under-promoted | architecture/voice / notation | Correct dictionary as buried lemma | Main theorem-level bridge with `m=d-1` discipline | Promote and add raw-charge warning | Local patch plus section rewrite |
| 8 | Determinant over-read as Hall structure | proof/certificate / architecture | Denominator and coefficient dictionary | Firewall: determinant gives signed dimensions only | Move/enforce "denominator forgets structure" | Local patch plus section rewrite |
| 9 | Citations underpinned unevenly | source/citation | Relevant but not exact source use | Exact primary anchors for every imported theorem/datum | Citation audit table; remove unsupported claims from main path | Local patch / companion note |
| 10 | Rows and spin pollute closure | architecture/voice / source | Row ledger and spin appendix in main flow | Independent consequences or companion notes | Quarantine/compress; move spin out | Companion note / appendix compression |
| 11 | Physical vocabulary overclaims | architecture/voice | Status-mixed terms in opening and theorem names | Status-controlled mathematical language | Rewrite opening and rename overloaded sections | Section rewrite |
| 12 | Notation/build hazards | notation/build | Colliding symbols and labels | Single notation firewall and clean labels | Fix undefined symbols, aliases, OP variables, determinant names | Local patch |

## Minimum viable paper path

The minimum viable paper should not try to become the full compact
Dirac-Igusa realization. It should become a clean, honest automorphic-descent
paper with an explicit compact-realization frontier.

Recommended minimum theorem spine:

1. Normalize the target determinant: `Z_{K3}=2\phi_{0,1}`, arbitrary
Grothendieck half-index, virtual determinant `\mathcal D_X=\Delta_5`, and
`D_5=64^{-1}\Delta_5`.
2. Import the GN/Borcherds denominator theorem with exact normalization:
`D_5(2Z)` and the BKM algebra `\mathfrak g_{\Delta_5}`.
3. Promote the D6-D2-D0 Mukai-Gram dictionary:
`v_X(I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E` and
`\Pi_X(Q_Y,P_Y)=(\beta^2/2,n,d-1)`.
4. Prove the raw charge defect: the Gram triple is not an additive Hall charge.
5. Prove the normal-ordered extension theorem and raw fixed-lift no-go, with
clean cochain notation.
6. State the projection-to-`E` locality obstruction: positive elliptic degree is
not projection-finite on `Ran(E)`.
7. State the hybrid local/wrapped source as the required repair, but mark it as
construction still needed unless supplied.
8. Include OP/Oberdieck scalar square only as scalar evidence:
`Z_{OP/DT}=-4096\Delta_5^{-2}` with an orientation-forgetful warning.
9. End with a compact realization problem/certificate ledger: what a source
construction must provide and what finite windows must verify.

Material to demote or move out of the minimum path:

- Detailed compact source kernels, Hall-Dirac atlases, and primitive recognition
protocols: keep as a frontier section, not proved construction.
- Eight-row boundary ledger: appendix or companion note unless exact source
anchors and independence status are made explicit.
- Spin `L`-factor normalization: companion note or one-sentence pointer.
- Dirac/Pfaffian recognition: definition/open problem/conditional certificate,
not a main theorem unless the source object and orientation gerbe are built.

Local patches required before the minimum viable paper is defensible:

- Fix undefined `\Gamma_{eff}^+`.
- Repair early primitive quotient display to include radical quotient.
- Remove unsafe `H^2_{sym}` language.
- Separate `B`, `B_{ch}`, `B_C`, and `\overline B_E^{ch}`.
- Define raw fixed-lift pushforward before the no-go.
- Replace raw split notation where `s(c)=(c,\Pi(c))` is required.
- State denominator grading comparison through `\overline\Pi_X`.
- Rename overloaded "one-particle" and "Dirac/Pfaffian theorem" language.

## Platonic ideal path

The platonic paper is not merely the minimum viable paper with more
certificates. It is construction-first.

The ideal path:

1. Construct the algebraic target `D^{alg}_{\Delta_5,C,L}`.
   - Start from GN's `\mathfrak g_{\Delta_5}`.
   - Choose `L:\Gamma_{gram}\to\Gamma_{form}`.
   - Define `s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)`.
   - Prove `\overline\Pi_X s_L=id` and monoidality.
   - Regrade the BKM algebra and build the curve current envelope for a smooth
     curve `C`.
2. Construct the geometric pre-source `H^{pre}_{X,\Gamma}`.
   - Use derived compact-object moduli stacks indexed by additive charge data.
   - Define exact-triangle correspondences and their compatibility with
     normal-ordered labels.
   - Produce finite HN/stability windows `H^{pre}_R`.
3. Construct the orientation-gerbe twisted source `H^{tw}_{X,\Gamma}`.
   - Define square-root gerbes `Or_{R,\hat c}`.
   - Define anti-invariant Borel-Moore objects with the tautological half line.
   - Lift products/coproducts through the gerbe.
   - Only afterward formulate O1 trivialization and O2 wall compatibility.
4. Construct the hybrid local/wrapped source.
   - Prove raw projection to `E` fails locality.
   - Define projection-finite local strata and wrapped positive-degree strata.
   - Prove mixed compatibility and finite hybrid certificates.
5. Build the source coalgebra/chiral coalgebra and protected primitive quotient.
   - Define radicals, pairings, coproducts, primitives, and PBW filtration.
   - Prove no-extra-relation statements in finite windows and pass to the limit.
6. Prove primitive recognition:
   - `\overline\Pi_* H^0 Prim_{prot}(H^{tw}_{X,\Gamma})/Rad \cong
     \mathfrak g_{\Delta_5}`.
   - Match the first timelike window source-side, including `29|93`.
7. Prove the Dirac/Pfaffian certificate.
   - Construct the compact Dirac/Pfaffian object.
   - Prove its Pfaffian determinant is `\Delta_5`, not just compatible with the
     scalar square.
8. Then derive OP scalar square and row consequences as consequences, not as
   substitutes for construction.

In the platonic paper the compact source comparison is a theorem. In the
minimum viable paper it is a precise open problem with finite certificate
requirements.

## Dependencies and sequencing

### Immediate local sequence

1. Fix notation/build hazards before any architecture rewrite. Otherwise the
   rewrite will preserve wrong symbols.
2. Repair normal-ordering cochains and raw fixed-lift definitions.
3. Promote the D6-D2-D0 dictionary and insert the raw-charge nonadditivity
   warning.
4. Insert the determinant-forgets-structure firewall.
5. Rewrite the introduction and section order around the minimum theorem spine.
6. Quarantine rows and spin material.
7. Build the citation audit table.

### Mathematical dependency sequence

1. GN/Borcherds target normalization precedes all denominator claims.
2. D6-D2-D0 dictionary precedes normal-ordering because it identifies the
   nonadditive Gram triple.
3. Normal-ordered extension precedes Hall descent and any source comparison.
4. Projection-to-`E` locality obstruction precedes hybrid local/wrapped source.
5. `H^{pre}` precedes `H^{tw}` because the gerbe twists operations on the source.
6. `H^{tw}` precedes O1 trivialization; orientation data are not a substitute
   for the gerbe object.
7. Hybrid source and protected primitive quotient precede primitive recognition.
8. Primitive recognition precedes Dirac/Pfaffian realization.
9. Dirac/Pfaffian realization precedes any strong claim that compact geometry
   produces `\Delta_5`.
10. OP scalar square and diagonal rows are downstream evidence/consequences, not
    upstream construction.

### Data dependency sequence

1. Define finite source schema.
2. Populate first HN/stability windows and charge labels.
3. Provide source bases per normal-ordered degree.
4. Provide product, bracket, coproduct, and pairing matrices.
5. Compute radicals and primitive quotients.
6. Check Jacobi, coassociativity, compatibility, and PBW/no-extra-relations.
7. Check transition maps and ML exactness.
8. Only then compare source dimensions with target `W_{\le3}` dimensions.

## Main.tex anchors

Core opening and architecture:

- `main.tex:177` Introduction and claim strength.
- `main.tex:464` The physical question.
- `main.tex:640` The one-particle index and determinant.
- `main.tex:13957` Coefficient dictionary and main synthesis.

Target determinant and denominator:

- `main.tex:833` Normalized determinant proposition.
- `main.tex:853` Virtuality of square root.
- `main.tex:2383` Normalized cusp form.
- `main.tex:2530` BGN/GN identification.
- `main.tex:5560` Denominator algebra.
- `main.tex:5590` Denominator Lie superalgebra.
- `main.tex:5614` Denominator identity.
- `main.tex:13543` Duplicate denominator identity.
- `main.tex:13603` What denominator determines.
- `main.tex:13652` Determinant forgets structure.

D6-D2-D0 and charge descent:

- `main.tex:2634` D6-D2-D0 protected-index dictionary.
- `main.tex:2661` Mukai-Gram dictionary.
- `main.tex:2760` Reduced scalar quotient integration.
- `main.tex:4309` Physical charge and normal-ordered Gram descent.
- `main.tex:4316` Dyonic Mukai lattice.
- `main.tex:4431` Gram-index notation.
- `main.tex:4523` Formal primitive lift.
- `main.tex:4590` Additivity defect/cocycle.
- `main.tex:4614` Normal-ordered extension theorem.
- `main.tex:4832` Normal-ordered extension definition.
- `main.tex:4883` Raw fixed-lift no-go.

Compact source and recognition:

- `main.tex:5704` Compact Dirac-Igusa realization problem.
- `main.tex:5724` Formal current envelope.
- `main.tex:5743` Formal current envelope proposition and dangerous label alias.
- `main.tex:5770` Holomorphic E3 upgrade.
- `main.tex:6024` Compact E3 source interface.
- `main.tex:6192` Finite compact E3 source obstruction certificate.
- `main.tex:6404` Target-internal bar-cobar counit.
- `main.tex:6506` Chiral Koszul source certificate.
- `main.tex:6731` Canonical finite source-bar coalgebra.
- `main.tex:7039` Projection-finite/wrapped/hybrid strata.
- `main.tex:7121` Finite hybrid certificate.
- `main.tex:8254` Hybrid open problem.
- `main.tex:8348` Normal-ordering coefficient dg category.
- `main.tex:8603` Conditional normal-ordered Hall descent.
- `main.tex:9132` NO1-NO7 diagrams.
- `main.tex:9654` Finite normal-ordering closure criterion.
- `main.tex:9973` First-order D0 certificate.
- `main.tex:10994` Finite Hall source kernel.
- `main.tex:11282` Finite Hall-Dirac atlas.
- `main.tex:11518` Finite D0 certificate status theorem.
- `main.tex:11750` Dirac-Igusa realization certificate.
- `main.tex:12124` Primitive recognition certificate.
- `main.tex:12479` Cofinal finite-window certificate.
- `main.tex:12590` Global recognition as cofinal certificate.
- `main.tex:12838` First timelike presentation count.
- `main.tex:12941` First saturated `W_{\le3}` window.
- `main.tex:13205` Finite `W_{\le3}` NO7 source protocol.
- `main.tex:13276` State-side construction open problem.

OP scalar, rows, and spin:

- `main.tex:13701` Scalar square.
- `main.tex:13724` OP normalization.
- `main.tex:13806` OP scalar square.
- `main.tex:13885` Square-root consequence.
- `main.tex:14031` Coefficient dictionary and main synthesis.
- `main.tex:14269` Eight diagonal-divisor rows: automorphic and physical status.
- `main.tex:14289` Physical-host certificate.
- `main.tex:14339` Clery-Gritsenko.
- `main.tex:14558` Spin L-factor normalization.
- `main.tex:14575` Andrianov factorization.
- `main.tex:14689` Eight diagonal-divisor boundary rows.
- `main.tex:14986` GN denominator rows.
- `main.tex:15470` Govindarajan rows.

Known local patch anchors:

- `main.tex:286` Early primitive display missing radical quotient.
- `main.tex:882` Dirac/Pfaffian recognition target should be definition/open
  problem unless proved.
- `main.tex:1139` Conditional Dirac/Pfaffian theorem overloaded.
- `main.tex:1954` Undefined `\Gamma_{eff}^+`.
- `main.tex:4366` Unsafe cohomology/trivialization language.
- `main.tex:4811` Unsafe `H^2_{sym}` language.

## Residual unknowns

1. Agents 18 and 30 were not present in the report directory; this synthesis
   cannot incorporate reports that were not there.
2. Exact primary-source page/theorem anchors still need verification for GN/GNII,
   OP/Oberdieck/Bryan, Clery-Gritsenko, Govindarajan, Andrianov/Zagier, and any
   Borel-Moore convolution technology.
3. It is not yet decided whether the paper should attempt the platonic compact
   source construction or retreat to the minimum viable automorphic-descent
   paper with a compact-realization frontier.
4. No source-side finite data directory was found in the scan summarized by the
   reports. If another agent has produced one concurrently, this report needs a
   follow-up reconciliation.
5. The square-root orientation gerbe may require additional stabilizer and wall
   chart calculations before O1/O2 can be stated as theorems.
6. The exact boundary between main text, appendix, and companion note remains an
   editorial decision, but spin material has no visible dependency into the core
   proof path.
7. The target algebraic object `D^{alg}_{\Delta_5,C,L}` is likely constructible
   from existing target data, but it is not currently a substitute for the
   missing compact source.
8. The attack PDF's strongest ideal claim is construction-first. Any final paper
   that keeps certificate language without constructing the source should present
   itself as a target/descent paper, not as the platonic compact realization.
