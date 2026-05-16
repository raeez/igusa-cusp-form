# Ninth Reconstitution Roadmap Attack-Heal Ledger

Date: 2026-04-28.

Integration owner: main thread in `/Users/raeez/igusa-cusp-form`.

This is the fresh six-lane attack pass requested after the new criticism
documents landed.  It does not replace
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md`; it tests
that ledger, the roadmap, and `main.tex` again.

All lanes were read-only.  No lane edited files, staged changes,
committed, built the manuscript, or ran destructive git.

## Lanes

| Lane | Runtime id | Nickname | Scope |
|---|---|---|---|
| A9-LATTICE | `019dd464-f26b-7440-95f0-37a368780772` | Goodall | Mukai lattice, torsion-one descent, raw descent, `(c,T)`, normal ordering |
| A9-AUTO | `019dd464-f52c-7f52-9ec2-740fca9ed8be` | Euler | Automorphic normalization, BKM attribution, OP/DT square |
| A9-D0 | `019dd464-f71a-72e3-b68a-fecaef17e0cf` | Schrodinger | Compact Hall/D0 source and Pfaffian source exponents |
| A9-ORIENT | `019dd464-f991-78c3-a25f-c4293ce3386d` | Feynman | O1/O1+/O2, Pfaffian line, Weyl signs |
| A9-HYBRID | `019dd464-ff64-7a82-8515-8ed58625fc1f` | Laplace | Hybrid locality, quotient-after-correspondence, Koszul/cobar |
| A9-ROADMAP | `019dd464-fcbe-75f2-9582-780704a7a5c4` | Pascal | Status vocabulary, dependency DAG, provenance, guide transfer |

## Verdict

The fresh pass confirms the eighth ledger and sharpens its boundary:
there is a stable formal and target-side core, but there is no closed
compact Dirac-Igusa source roadmap yet.

The strongest current stable core is:

1. Formal lattice algebra: Mukai pairing convention, Gram map, bilinear
   defect `B`, central extension law, and additivity of
   `\overline\Pi_X`.
2. Formal primitive lift as a full topological Mukai-lattice statement,
   not as algebraic/effective Hall existence and not as torsion-one
   descent.
3. Target automorphic normalization as imported/computed data:
   `D_5=64^{-1}\Delta_5`, `D_X=\Delta_5`, and
   `\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z)`.
4. OP/DT scalar arithmetic:
   `\chi_{10}^{OP}=D_5^2=4096^{-1}\Delta_5^2`, hence
   `Z^X_{OP/DT}=-4096\Delta_5^{-2}`, pending a recorded primary-source
   audit.
5. Target Maass character values as automorphic facts, explicitly
   separated from compact Hall orientation.

Everything involving compact source construction, Hall support,
orientation descent, hybrid wrapped factorization, source exponents,
source-to-target Koszul comparison, or Pfaffian-line comparison remains
conditional/open.

## Consolidated Valid Attacks

### A. Lattice And Charge

#### A9-L-01. Full Mukai Lattice Is Not Yet The Hall Charge Lattice

Status: valid. Severity: 5.

Targets: `main.tex:3926`, `main.tex:4071`, `main.tex:4101`;
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:62`;
`notes/reconstitution_plan_20260428.md:93`.

The primitive-lift theorem uses the full topological Mukai lattice and
two hyperbolic planes.  Compact Hall and OP/D6-D2-D0 objects only see
algebraic/effective Chern characters.  A formal full-Mukai lift need not
be algebraic, effective, or represented by a compact Hall object.

Minimal heal:

- Split the formal full Mukai lattice from the algebraic/effective
  D6-D2-D0 sector.
- Do not call the full `H^*(S,Z) \oplus H^*(S,Z)` lattice the compact
  microscopic Hall source.
- Add effectivity and nonempty-moduli hypotheses wherever a Hall object
  is inferred.

Deciding evidence: a theorem identifying compact Hall charge support
with the stated lattice sector.

#### A9-L-02. Primitive Saturation Is Not Torsion-One Descent

Status: valid. Severity: 4.

Targets: `main.tex:4101`, `main.tex:4127`, `main.tex:4142`;
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:197`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:135`.

The manuscript proves primitive saturation by a minor-one argument.  It
does not define the dyonic torsion invariant
`I(Q,P)=gcd(Q\wedge P)`, prove orbit uniqueness, or prove descent of
protected indices.  The displayed lift likely has `I(Q,P)=1` because the
`e_1 \wedge e_2` coefficient is `1`, but this is not stated or used.

Minimal heal:

- Define `I(Q,P)`.
- Prove the displayed lifts have torsion one.
- Keep torsion-one arithmetic separate from effectivity and duality-orbit
  descent.

Deciding evidence: an explicit torsion-one descent theorem for the
relevant lattice orbits and source indices.

#### A9-L-03. Raw Descent No-Go Is Only Fixed-Lift So Far

Status: valid. Severity: 4.

Targets: `main.tex:4419`, `main.tex:4457`, `main.tex:4479`,
`main.tex:4482`, `main.tex:10743`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:93`.

The proof reuses the same physical lift `c_i` in the second bracket.  A
fibre-summed raw pushforward could represent a simple root by a sum over
several lifts in the same Gram fibre, so the outer bracket could use a
different lift.

Minimal heal:

- Rename the theorem as a strict homogeneous fixed-lift raw-descent
  obstruction.
- Make mixed-lift fibre summation an open case unless ruled out.

Deciding evidence: a proof or counterexample for fibre-summed raw
pushforward satisfying the needed Chevalley/Serre/Jacobi relations.

#### A9-L-04. `(c,T)` Is Not Yet A Functorial Hall Degree

Status: valid. Severity: 5.

Targets: `main.tex:8627`, `main.tex:8636`, `main.tex:8863`,
`main.tex:8875`, `main.tex:7192`, `main.tex:7230`.

`T_R(c)` is a set of pairwise `B`-sums over decompositions.  It is not
yet an intrinsic degree map on moduli or correspondences.  The same total
charge can appear with `T=0` as a single sector and with
`T=B(a,b)` as a two-factor sector, so naive `(c,T)` strata can overcount
source states.

Minimal heal:

- Make `T` a coefficient-system, central-translation, or
  factorization-tree datum.
- Prove no-overcount for `\overline\Pi_*^\Theta`.
- Prove transition compatibility.

Deciding evidence: a functorial `(c,T)` grading theorem for finite Hall
correspondences.

#### A9-L-05. Current Compute QA Does Not Check Normal Ordering

Status: valid. Severity: 2.

Targets: `compute/verify_lattice.py:61`,
`compute/verify_lattice.py:92`, `compute/verify_lattice.py:130`,
`compute/verify_square_root.py:379`;
`notes/reconstitution_plan_20260428.md:627`.

`verify_lattice.py` checks the Pfaffian/root lattice, Weyl vector,
reflections, and degree normalization.  It does not check Mukai lifts,
`B`, `\overline\Pi_X`, raw-descent no-go, or torsion one.  The `gcd` in
`verify_square_root.py` is Witt multidegree arithmetic, not dyonic
torsion.

Minimal heal: add a Mukai-normal-ordering verification script checking
`Q,P`, `B`, additivity, primitive minors, and torsion one.

### B. Compact Hall / D0 Source

#### A9-D0-01. The Finite D0 Source Is Not Constructed

Status: valid as roadmap attack; contained in current manuscript.
Severity: 5.

Targets: `main.tex:8543`, `main.tex:8589`, `main.tex:9244`,
`main.tex:9829`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:180`.

Finite-type semistable stacks, HN support, oriented critical Hall
correspondences, admissible pull-push, and transition morphisms are still
hypotheses.  The finite Hall source kernel is supplied data.

Minimal heal: keep all finite source results conditional until the
actual finite kernels `\mathfrak S_R` are built.

Deciding evidence: explicit finite-type d-critical stacks, BBDJS
complexes, extension correspondences, proper/admissible pull-push, and
transition morphisms.

#### A9-D0-02. Finite Normal-Ordered Support Is Conditional

Status: valid. Severity: 4.

Targets: `main.tex:8589`, `main.tex:9719`, `main.tex:9847`.

The relevant finiteness result depends on support property, HN property,
finite-type semistable stacks, and oriented critical Hall
correspondences.  It should not be recorded as unconditional compact
geometry.

Minimal heal: relabel as proved conditional on sectorial HN/support
hypotheses.

#### A9-D0-03. General PTVV/BBDJS/Joyce Technology Is Not A Source
Construction

Status: valid, mostly contained. Severity: 4.

Targets: `main.tex:7333`, `main.tex:7403`, `main.tex:7490`,
`main.tex:9262`.

Shifted symplectic and d-critical language does not by itself give
BBDJS coefficient systems, Thom-Sebastiani transport, proper Hall
pull-push, cyclic lift, or quotient-compatible orientations.

Minimal heal: cite these sources as technology after the finite stacks
and correspondences are supplied, not as construction of the compact
source.

#### A9-D0-04. D0 Observable Shadow Depends On Hybrid Wrapped Repair

Status: valid. Severity: 4.

Targets: `main.tex:8890`, `main.tex:6336`, `main.tex:6453`,
`main.tex:6532`, `main.tex:11256`.

Positive elliptic degree requires hybrid local/wrapped repair before
quotienting by `E`.  The quotient functor `Q_{E,R}`, admissibility,
properness, and mixed/wrapped pull-push are still supplied data.

Minimal heal: factor a common finite Hall/hybrid source kernel below D0
and prove `\mathfrak O_{\mathrm{hyb},R}=0`.

#### A9-D0-05. Target Windows Do Not Prove Source Coverage

Status: valid. Severity: 5.

Targets: `main.tex:8660`, `main.tex:9166`, `main.tex:9177`,
`main.tex:9401`.

`N_R^\Delta` is bookkeeping, not a theorem relating HN height to
automorphic height.  Active target degrees must already lie in
`\Gamma_R^\Pi`; this is a condition, not a result.

Minimal heal: prove source-support coverage, or choose target windows
only inside verified source image.

#### A9-D0-06. D0-Pf Recognizes Supplied Exponents

Status: valid. Severity: 5.

Targets: `main.tex:1055`, `main.tex:1072`, `main.tex:9070`,
`main.tex:9151`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:362`.

D0-Pf assumes signed primitive superdimensions equal `f(nm,l)` and then
imports the Borcherds/Gritsenko-Nikulin product to identify the product
with `\Delta_5`.  This is recognition, not independent source evidence.

Minimal heal: split source exponent computation from target recognition.

Deciding evidence: an independent compact Hall calculation of primitive
source dimensions, beginning with low-degree channels such as the `-64`
test.

### C. Orientation, Weyl, And Pfaffian Line

#### A9-O-01. O1 Needs Full Equivariant Cohomology

Status: valid. Severity: 5.

Targets: `main.tex:3550`, `main.tex:3615`, `main.tex:3622`,
`main.tex:3633`, `main.tex:3679`, `main.tex:3712`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:204`.

The finite-stabilizer obstruction is not just point-stabilizer data in
`H^2(BE[N])` plus `H^1(BE[N])`.  Total degree two may include
`H^1(BE[N];H^1(M_red;F_2))`, stabilizer action on `H^q(M_red)`, and
differentials.

Minimal heal:

- Replace the tuple by a full class in `H^2_{E[N]}(M_red;F_2)`.
- Or add hypotheses killing `H^1(M_red)`, stabilizer action, and
  differentials.

Deciding evidence: stratum-by-stratum equivariant cohomology for every
object, extension, and flag stratum.

#### A9-O-02. O1+ Is Finite Action-Groupoid Cohomology First

Status: valid, partly healed. Severity: 4.

Targets: `main.tex:1213`, `main.tex:1227`, `main.tex:1231`,
`main.tex:1267`, `main.tex:1811`, `main.tex:1888`,
`main.tex:1906`, `main.tex:1923`.

Finite HN stages carry a partial action groupoid on strata, not
automatically a global constant-coefficient Weyl action.  The manuscript
now names finite-stage groupoid cocycles; the roadmap must treat that
as primary.

Minimal heal: formulate O1+ in finite action-groupoid cohomology, and
reduce to `H^2(W;F_2)` only after complete orbits, constant coefficients,
and HN-compatible splittings are proved.

#### A9-O-03. O2 Needs A Finite Wall Atlas

Status: valid. Severity: 5.

Targets: `main.tex:840`, `main.tex:895`, `main.tex:973`,
`main.tex:1024`, `main.tex:6868`, `main.tex:6952`.

Three generic rank-one wall charts do not cover all wall components,
small-orbit boundary strata, finite HN transitions, or the hybrid
wrapped `m=1` wall for `\delta_2`.

Minimal heal: build a finite wall atlas indexed by HN height, wall
component, and boundary stratum, with overlap and transition coherence.

#### A9-O-04. Reduced Orientation Transport Is Not Automatic

Status: valid. Severity: 4.

Targets: `main.tex:1378`, `main.tex:1393`, `main.tex:2032`,
`main.tex:2761`, `main.tex:2808`, `main.tex:3861`;
`proj.bib:471`.

Unreduced Joyce-Upmeier/BBDJS/PTVV orientation data do not automatically
survive cosection reduction, quotient by `E`, finite stabilizers, inertia
age terms, or HN extension transport.

Minimal heal: state a reduced orientation transport theorem with all
cosection, quotient, stabilizer, and Thom-Sebastiani hypotheses.

#### A9-O-05. Rank-One Parity Is Only A Diagnostic Until GRR

Status: valid. Severity: 3.

Targets: `main.tex:2526`, `main.tex:2556`, `main.tex:2576`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:416`.

`c_1(L)^2/2 mod 2` is a numerical parity until GRR or a determinant-line
calculation identifies it with the class in `H^2(M_red;F_2)`.

Minimal heal: add the GRR/Stiefel-Whitney comparison, or state the
formula only as a diagnostic.

#### A9-O-06. Pfaffian Equality Needs A Line Comparison

Status: valid. Severity: 4.

Targets: `main.tex:1325`, `main.tex:1446`, `main.tex:1458`,
`main.tex:9070`, `main.tex:9142`, `main.tex:4654`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:451`.

A normalized q-expansion and leading coefficient do not construct an
isomorphism from the source Pfaffian line to
`\mathcal L^5 \otimes \nu_{\Delta_5}`, nor the claimed unique
top-cohomology generator.

Minimal heal: add Pfaffian-to-automorphic line comparison as explicit
D0-Pf data, equivariant under the relevant group and cusp trivialization.

### D. Hybrid, Wrapped, And Koszul

#### A9-H-01. The Eight-Word Atlas Is Not Full Factorization

Status: valid. Severity: 4.

Targets: `main.tex:6476`, `main.tex:6528`, `main.tex:7357`;
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:319`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:280`.

The eight-word atlas proves only binary two-color associativity for
triples, plus a four-input pentagon.  Full Ran/factorization structure
also needs unit/vacuum compatibility, symmetric-group equivariance, all
finite partition/coarsening diagrams, restriction/descent/cosheaf
compatibility, and higher operadic coherence.

Minimal heal: rename the atlas as the binary associativity
subcertificate and add a full colored factorization certificate.

#### A9-H-02. `Q_{E,R}` Is Data, Not A Constructed Pseudofunctor

Status: valid. Severity: 4.

Targets: `main.tex:6532`, `main.tex:6561`, `main.tex:6570`,
`main.tex:6836`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:295`.

`Q_{E,R}` is specified with comparison maps `\theta^Q`, but not built as
a pseudofunctor on the correspondence bicategory.  A derived
pull-push setting needs identity, composition, base-change, 2-morphism,
flag, and transition coherence.

Minimal heal: define unreduced and reduced correspondence 2-categories
and construct `Q_{E,R}` with coherent `\theta^Q` modifications.

#### A9-H-03. Single Wrapped Anchors May Lose Relative Data

Status: valid. Severity: 3.

Targets: `main.tex:6134`, `main.tex:6273`, `main.tex:6380`,
`main.tex:6506`;
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:301`.

For wrapped degree `b>1` or multi-leg wrapped configurations, a single
determinant/center-type anchor can collapse relative support data needed
by mixed and wrapped-wrapped extensions.

Minimal heal: replace single anchors by a finite anchor multiset/divisor
or full relative-support rigidification, unless a losslessness theorem
is proved.

#### A9-H-04. Source Koszul/Cobar Depends On The Unbuilt Hybrid Source

Status: valid, already fenced. Severity: 4.

Targets: `main.tex:5556`, `main.tex:5831`, `main.tex:5953`,
`main.tex:10200`;
`notes/seventh_koszul_cobar_attack_heal_report.md:29`.

`C_{X,R}=B_E^{ch}(F^{hyb}_{X,R})` is available only after the hybrid
source exists, is augmented, has bounded non-vacuum bar length, lies in
the BD/Francis-Gaitsgory domain, and admits a source-to-target
quasi-isomorphism `\vartheta_R`.

Minimal heal: keep the source bar coalgebra conditional on
`\mathfrak O_{\mathrm{hyb},R}=0`, then prove source-counit and
`\vartheta_R` residuals separately.

### E. Automorphic And Scalar Normalization

#### A9-A-01. Automorphic Attribution Is Too Compressed

Status: valid. Severity: 3.

Targets: `main.tex:2221`, `main.tex:12759`, `proj.bib:65`.

The first use compresses the exact `\Delta_5` product, the factor `64`,
and the denominator identity under a broad
Borcherds-Gritsenko-Nikulin label.  Later text gives the sharper split:
Borcherds for the general lift machine, GNII for the exact `D_5`
product and `64`, GN for the corrected `D_5(2Z)` denominator identity.

Minimal heal: split these citations at the first use.

Deciding evidence: primary-source audit of GN/GNII theorem and equation
labels.

#### A9-A-02. `\pm D_X^{-1}` Reintroduces A Fixed-Normalization Ambiguity

Status: valid. Severity: 3.

Targets: `main.tex:745`, `main.tex:11831`, `main.tex:12054`.

`D_X` is already normalized as `\Delta_5`, so its inverse is fixed.  The
sign ambiguity belongs to an orientation-lifted Pfaffian square root
before orientation normalization, not to the fixed target inverse.

Minimal heal: write the normalized target inverse as `D_X^{-1}` and
introduce a separate notation for the orientation-lifted sign torsor.

#### A9-A-03. "Unconditional" Needs Source-Hypothesis Qualification

Status: valid. Severity: 2.

Targets: `main.tex:2017`, `main.tex:330`.

Maass values, determinant identity, and OP scalar results are
independent of compact Hall hypotheses.  They are still imported
automorphic/enumerative results with their own source hypotheses.

Minimal heal: say "independent of compact Hall hypotheses; imported or
proved under the cited source hypotheses."

#### A9-A-04. OP/DT Scalar Square Is Internally Coherent But Needs Audit

Status: undecided until audit. Severity: 2.

Targets: `main.tex:11694`, `main.tex:11772`, `proj.bib:214`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:73`.

The formula is internally coherent, but this pass did not inspect the
primary OP/Oberdieck sources.  The audit must check primitive `\beta`,
quotient by `E`, Laurent chamber, variable map, and degree-zero factor.

#### A9-A-05. `D_5(2Z)`, `64`, `4096`, And Maass Separation Survived

Status: invalid attacks against formulas.

Targets: `main.tex:12740`, `main.tex:5211`, `main.tex:79`,
`main.tex:11694`, `main.tex:11807`, `main.tex:1611`,
`main.tex:1725`, `main.tex:11884`.

No formula error was found in the `D_5(2Z)` factor, the `64/4096`
arithmetic, or the separation of Maass character from Hall orientation.

### F. Roadmap, Provenance, And Status Discipline

#### A9-R-01. Status Vocabulary Is Not Mechanically Usable

Status: valid. Severity: 5.

Targets: `notes/attack_whitepaper_analysis_20260428_090346_guide.md:517`,
`notes/reconstitution_plan_20260428.md:682`, `main.tex:361`,
`notes/critique_resolution_table.md:10`,
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:469`.

The guide, plan, `main.tex`, critique table, and eighth ledger use
different status systems.  The critique table uses `Corrected` for both
wording repairs and open mathematics.

Minimal heal:

- Canonical vocabulary:
  `proved`, `computed`, `imported`, `certificate`, `conditional`,
  `conjectural`, `open`, `obstructed`.
- Split "wording repaired" from "mathematics closed."

Deciding evidence: theorem-by-theorem status matrix covering every main
result and every critique-table row.

#### A9-R-02. Stable Core Needs A Dependency Table

Status: valid. Severity: 5.

Targets: `notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:23`,
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:73`,
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:95`,
`main.tex:376`, `main.tex:3926`.

The eighth ledger correctly says the compact roadmap has not converged,
but its stable core contains or neighbors claims whose prerequisites
remain open: scalar square primary-source audit, raw no-go fixed-lift
restriction, and main-text Mukai wording.

Minimal heal: stable-core table with dependencies, excluded
interpretations, and audit status.

#### A9-R-03. Roadmap Needs Separate Exposition And Proof DAGs

Status: valid. Severity: 5.

Targets: `notes/reconstitution_plan_20260428.md:58`,
`notes/reconstitution_plan_20260428.md:412`,
`notes/reconstitution_plan_20260428.md:446`, `main.tex:180`,
`main.tex:330`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:492`.

Exposition order and proof order are interleaved.  OP/DT can be mistaken
as proof input for Pfaffian/source realization.

Minimal heal: a one-page DAG with arrows marked `uses`, `imports`,
`motivates`, or `checks`.

#### A9-R-04. Provenance And Guide Transfer Are Not Yet Auditable

Status: valid. Severity: 4.

Targets: `refs/source-provenance.md:17`,
`refs/source-provenance.md:23`,
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:3`,
`materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt:1`,
`materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt:13291`,
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:516`.

Hashes exist for the latest criticism document, but extraction command,
tool/version, page map, and claim-to-page anchors are missing.  The guide
is explicitly not primary literature, yet guide recommendations have
entered the theorem architecture without a full transfer matrix.

Minimal heal:

- Add extraction command, tool version, PDF page count, and line-to-page
  map.
- Add a matrix: guide line -> main target -> primary source/computation
  -> status.

#### A9-R-05. Boundary-Row Audit Is Still A Residual

Status: valid. Severity: 3.

Targets: `notes/reconstitution_plan_20260428.md:472`,
`notes/reconstitution_plan_20260428.md:680`, `main.tex:310`,
`main.tex:353`;
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:396`,
`notes/eighth_reconstitution_roadmap_attack_heal_20260428.md:604`.

The eighth ledger mentions a row-by-row source map, but the final
residual obligations do not explicitly carry the full Clery-Gritsenko /
Govindarajan row audit and host-certificate matrix.

Minimal heal: add a table for all eight rows: product source,
denominator source, cover, character, scalar host, and physical-host
status.

#### A9-R-06. Manuscript-Facing Process Vocabulary Should Be Removed

Status: valid. Severity: 2.

Targets: `notes/reconstitution_plan_20260428.md:6`,
`notes/reconstitution_plan_20260428.md:9`, `main.tex:361`,
`notes/critique_resolution_table.md:20`.

The phrase "Theorem-status ledger" reads as internal audit language in
the manuscript.  A standalone manuscript should use ordinary
mathematical prose.

Minimal heal: rename to "Status of results" or "Claim strength of the
main results."

## Stable Core After A9

| Claim | Status | Dependencies still excluded |
|---|---|---|
| `B` and `\overline\Pi_X` formal lattice algebra | proved formal algebra | no Hall grading, no source object |
| Primitive lift of every Gram triple | proved formal full-Mukai lattice lemma | no algebraic/effective object, no torsion-one descent, no BPS existence |
| `D_X=\Delta_5`, `D_5=64^{-1}\Delta_5` | imported/computed target normalization | GN/GNII audit to record theorem/equation labels |
| `D_5(2Z)` denominator | imported target normalization | GN/GNII audit to record exact convention |
| OP/DT scalar arithmetic `-4096\Delta_5^{-2}` | imported scalar branch, internally coherent | OP/Oberdieck audit still to record |
| Maass character values | imported target-side automorphic data | no Hall orientation construction |

No compact-source statement is in the stable core.

## Destroyed Roadmap Claims

The fresh pass destroys the following readings:

- The full topological Mukai lattice is the compact Hall charge lattice.
- Primitive saturation automatically gives torsion-one DVV/Igusa descent.
- Raw `\Pi_X` descent is ruled out beyond strict fixed-lift homogeneous
  pushforward.
- `(c,T)` is already a functorial Hall degree.
- Current compute scripts verify the normal-ordering roadmap.
- D0 source geometry is constructed from constraints alone.
- D0-Pf computes exponents rather than recognizing supplied exponents.
- Target-window cofinality gives source coverage.
- O1 is closed by point-stabilizer `H^2(BE[N])` and `H^1(BE[N])` data.
- O1+ is closed by constant-coefficient `H^2(W;F_2)`.
- O2 is supplied by three generic wall charts.
- Rank-one parity is already a class-level Pin/Brauer obstruction.
- A q-expansion or leading coefficient constructs the source Pfaffian
  line as the automorphic line.
- The eight-word atlas is full factorization.
- `Q_{E,R}` is constructed as a pseudofunctor.
- A single wrapped anchor is proved lossless.
- Source Koszul/cobar follows from writing the source bar coalgebra.
- `\pm D_X^{-1}` is the normalized virtual inverse.
- `Corrected` means mathematical closure.

## Contained Or Refuted Attacks

- No sign error was found in `B` or `\overline\Pi_X`.
- No arithmetic inconsistency was found in `64`, `4096`, or
  `D_5=64^{-1}\Delta_5`.
- The `D_5(2Z)` denominator factor survived.
- The manuscript mostly keeps Maass character target-side and separate
  from Hall orientation.
- The eighth ledger does not claim the compact Dirac-Igusa source has
  converged.
- Current `main.tex` usually fences D0/O1/O1+/O2 as certificate data or
  open obligations; the danger is mainly roadmap/status over-reading.

## Next Repair Order

The next repair pass should proceed in this order:

1. Add a canonical status matrix and rewrite `Corrected` rows as
   wording/math/status triples.
2. Replace manuscript-facing "ledger" language with standalone prose.
3. Split full topological Mukai lattice from algebraic/effective
   D6-D2-D0 Hall sector.
4. Add `I(Q,P)=gcd(Q\wedge P)` and prove torsion one for the displayed
   primitive lifts, while keeping effectivity and duality descent open.
5. Rename the raw no-go theorem to fixed-lift homogeneous raw-descent
   obstruction, or prove the fibre-summed case.
6. Define `T` as coefficient-system/central-translation data and state
   the no-overcount theorem as an open finite-stage obligation.
7. Install a one-page DAG with a common finite source kernel below D0,
   hybrid, O1/O1+, O2, normal ordering, and Koszul.
8. Replace O1 by full equivariant obstruction classes and O1+ by
   finite action-groupoid cohomology.
9. Replace O2 generic charts by a finite wall-atlas obligation,
   including the wrapped `\delta_2` wall.
10. Demote the eight-word hybrid atlas to binary associativity and add
    full factorization axioms.
11. Treat `Q_{E,R}` as a pseudofunctor construction target, not as
    already constructed data.
12. Split source exponent computation from target recognition in D0-Pf.
13. Add Pfaffian-line-to-automorphic-line comparison as explicit data or
    weaken equality to normalized expansions after such data.
14. Split the fixed target inverse `D_X^{-1}` from orientation-lifted
    sign choices.
15. Record primary-source audits for GN/GNII and OP/Oberdieck, and add a
    guide-to-main transfer matrix.
16. Add a compute script for Mukai-normal-ordering checks.

## Verification Still Needed

No final manuscript verification was run in this A9 pass.  Before any
manuscript integration is called closed, record:

```bash
git diff --check
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
make
```

The new compute obligation is separate: add and run a
Mukai-normal-ordering verification for `B`, `\overline\Pi_X`, primitive
minors, and torsion one.
