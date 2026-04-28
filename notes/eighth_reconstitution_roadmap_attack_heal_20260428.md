# Eighth Reconstitution Roadmap Attack-Heal Ledger

Date: 2026-04-28.

Integration owner: main thread in `/Users/raeez/igusa-cusp-form`.

Input criticism documents:

- `materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt`
- `notes/attack_whitepaper_analysis_20260428_090346_guide.md`
- `notes/reconstitution_plan_20260428.md`
- `notes/critique_resolution_table.md`

Six read-only attack lanes were run against the reconstitution roadmap:
lattice and normal ordering; automorphic and BKM normalization; compact
Hall and hybrid locality; orientation, Pfaffian, and Weyl signs; physics
dictionary and scalar square; roadmap status and provenance.  The
reports supply evidence, not authority.  This ledger records the
main-thread adjudication.

## Verdict

The full compact Dirac-Igusa roadmap has not converged.  The stable
core is narrower than the guide and roadmap currently suggest:

1. The elementary lattice algebra for the bilinear defect `B`, the
   extension law, and the normal-ordered Gram map survives direct
   attack.
2. The target-side automorphic constants `64`, the `D_5` normalization,
   the `D_5(2Z)` factor, the Maass character separation, and the OP/DT
   scalar square survive the current attacks.
3. The Mukai-Gram calculation and the CY3 dictionary survive after
   restricting the phrase "physical charge lattice" to the algebraic
   even D6-D2-D0 Mukai sector.
4. The compact source, reduced orientation, hybrid locality, and
   Pfaffian-square-root recognition remain conditional.  They must not
   be presented as constructed until the finite-stage Hall geometry,
   orientation descent, groupoid signs, and source-to-target comparison
   are supplied.

The next manuscript pass should not add stronger claims.  It should
split the roadmap into a stable theorem core, conditional compact-source
theorems, and explicitly open source-realization obligations.

## Stable Core

### Lattice Algebra

The formulas
`\Pi(c+c')=\Pi(c)+\Pi(c')+B(c,c')`,
`(c,T)\star(c',T')=(c+c',T+T'+B(c,c'))`, and
`\overline\Pi(c,T)=\Pi(c)-T` survive direct expansion.  The attack found
no sign error in `B` or in `\overline\Pi`.  The stable claim is purely
lattice-theoretic unless and until a Hall grading by `(c,T)` is
constructed.

Main anchors: `main.tex:4144`, `main.tex:4318`,
`main.tex:7192`, `main.tex:7260`, `main.tex:7700`.

### Target Automorphic Normalization

The target-side normalization of the Igusa square root survived the
automorphic attack: `D_X=64 D_5`, the monic normalization, the `D_5(2Z)`
factor, and the cusp factors are consistent with the present target
calculation.  The target formula is still an imported Borcherds /
Gritsenko-Nikulin theorem, not a new compact Hall construction.

Main anchors: `main.tex:739`, `main.tex:772`,
`main.tex:2221`, `main.tex:2242`.

### Scalar Square

The scalar OP/DT square
`Z^X_{OP/DT}=-4096 \Delta_5^{-2}` survived the current roadmap attack as
a target-side scalar identity, subject to a primary-source audit of the
exact Hilbert quotient, Behrend sign, and absence of an extra MacMahon
factor.

Main anchors: `main.tex:11748`, `main.tex:11772`,
`main.tex:11782`, `main.tex:11791`.

### Mukai-Gram Calculation

The Mukai-Gram shifts checked in the manuscript survived attack.  The
stable wording is not "the full physical microscopic charge lattice" but
"the algebraic even D6-D2-D0 Mukai sector used by the OP branch."

Main anchors: `main.tex:3926`, `main.tex:4071`,
`main.tex:4101`, `main.tex:4127`.

## Valid Attacks

### 1. Raw Descent No-Go Is Overstated

Status: valid, severity 1.

The no-go proof for raw descent assumes the same physical lift `c_i`
inside the second bracket.  A fibre-summed raw pushforward could combine
different lifts over the same Gram root.  The theorem is valid only for
a strict homogeneous fixed-lift raw pushforward, unless a separate
argument rules out mixed-lift fibre summation.

Main anchors: `main.tex:4419`, `main.tex:4457`,
`main.tex:4482`, `main.tex:10384`.

Heal:

- Rename the theorem to a strict homogeneous raw-descent obstruction.
- Add the mixed-lift fibre-summed case as an open obstruction, or prove
  a no-extra-mixed-lifts lemma before claiming the broader no-go.

### 2. Full Mukai Lattice And Algebraic Source Are Being Confused

Status: valid, severity 1.

The guide and roadmap use a full topological Mukai language, while the
Hall source can only see algebraic/effective compact objects.  A
primitive lift in the full Mukai lattice does not prove existence of an
algebraic compact Hall object.

Main anchors: `main.tex:3922`, `main.tex:3926`,
`main.tex:4071`, `main.tex:4101`.
Guide anchors: `notes/attack_whitepaper_analysis_20260428_090346_guide.md:62`,
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:68`.

Heal:

- Use "full even Mukai lattice" only for formal lattice statements.
- Use "algebraic even Mukai sector" for Hall, OP/DT, and D6-D2-D0
  claims.
- Add one sentence after the primitive-lift theorem: formal primitive
  recognition does not imply effectivity, nonempty moduli, or BPS
  existence.

### 3. Torsion-One Descent Is Missing

Status: valid, severity 1.

The new criticism documents require primitive/torsion-one descent, but
the manuscript currently proves a primitive saturated lift, not orbit
uniqueness, duality invariance, descent of indices, or the torsion
invariant needed for the DVV/Igusa interpretation.

Main anchors: `main.tex:4101`, `main.tex:4110`,
`main.tex:4127`, `main.tex:4142`.
Guide anchors: `notes/attack_whitepaper_analysis_20260428_090346_guide.md:197`,
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:208`.

Heal:

- Define `I(Q,P)=gcd(Q\wedge P)` in the lattice section.
- Prove the displayed lifts have `I(Q,P)=1`, or fence the statement as a
  conjectural/target compatibility.
- Do not infer DVV/Igusa primitive-sector descent from primitive
  saturation alone.

### 4. The `T` Label Is Not Yet A Functorial Hall Degree

Status: valid, severity 1.

`T_R(c)` is currently a bookkeeping set of pairwise `B`-sums.  It has
not been constructed as a functorial degree map on finite-stage moduli
or as a coefficient-system lift.  The pair `(c,T)` risks duplicating
source states unless `T` is central-translation data rather than an
independent object label.

Main anchors: `main.tex:8627`, `main.tex:8636`,
`main.tex:8863`, `main.tex:8875`, `main.tex:9249`,
`main.tex:9334`.

Heal:

- Define `T` as a coefficient-system lift or central-translation
  equivalence datum.
- Prove that the pushforward through `\overline\Pi` does not overcount
  source states.
- Keep all finite-stage claims conditional until the grading is
  realized by correspondences.

### 5. Finite Compact Hall Source Is Still Supplied, Not Built

Status: valid, severity 1.

The finite-first pro-object roadmap still assumes finite-type
semistable stacks, HN support, oriented critical Hall correspondences,
and admissible compact/wrapped extension stacks.  The new blueprint
states constraints, but it does not construct the source geometry.

Main anchors: `main.tex:8543`, `main.tex:8589`,
`main.tex:9250`, `main.tex:9276`.
Processed criticism anchors:
`materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt:13285`,
`materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt:13311`.

Heal:

- State finite-stage source theorems with explicit hypotheses on
  finite type, support property, orientation data, and admissible
  pull-push.
- Avoid treating PTVV/d-critical structure as sufficient for BBDJS
  coefficients, Thom-Sebastiani, or compact Hall operations without
  these hypotheses.

### 6. Orientation Descent Has A Missing Equivariant Obstruction

Status: valid, severity 1.

The finite-stabilizer O1 descent collapses the Borel spectral sequence
too quickly.  The obstruction is not just point-stabilizer data.  Mixed
terms such as `H^1(BE[N];H^1(M_red;F_2))`, stabilizer actions, and
differentials can contribute.

Main anchors: `main.tex:3615`, `main.tex:3624`,
`main.tex:3661`, `main.tex:3673`, `main.tex:3712`,
`main.tex:3719`.

Heal:

- Replace the finite tuple of stabilizer signs by a full class in
  `H^2_{E[N]}(M_red;F_2)`.
- Or add hypotheses forcing the mixed terms to vanish, the stabilizer
  action to be trivial, and the spectral sequence to degenerate.

### 7. O2 Produces Local Signs, Not A Global Pfaffian Sign

Status: valid, severity 1.

O2 supplies a local normal-Pfaffian wall sign.  The global
`\epsilon_o` exists only after O1 and O1+ supply orientation descent and
Weyl equivariance.

Main anchors: `main.tex:973`, `main.tex:1022`,
`main.tex:1213`, `main.tex:1284`, `main.tex:1811`,
`main.tex:1848`, `main.tex:2589`.

Heal:

- Rename the O2 output as a local wall-chart sign.
- Reserve global `\epsilon_o` for a theorem whose hypotheses include
  O1 and O1+.

### 8. One Wall Chart Does Not Globalize

Status: valid, severity 1.

One generic wall chart does not cover all compact Hall wall components,
small-orbit boundary strata, or finite HN stages.

Main anchors: `main.tex:840`, `main.tex:883`, `main.tex:895`,
`main.tex:912`, `main.tex:1891`, `main.tex:1930`,
`main.tex:6868`, `main.tex:6908`.

Heal:

- Introduce an atlas of O2 charts indexed by wall components and finite
  HN windows.
- Prove compatibility on overlaps before using wall signs globally.

### 9. O1+ Is Groupoid Cohomology, Not Just `H^2(W;F_2)`

Status: valid, severity 1.

The Weyl-equivariant orientation obstruction is attached to a partial
action groupoid on strata, not automatically to constant-coefficient
group cohomology of `W`.

Main anchors: `main.tex:1222`, `main.tex:1234`,
`main.tex:1811`, `main.tex:1848`, `main.tex:1906`,
`main.tex:1909`.

Heal:

- Formulate the obstruction in groupoid cohomology.
- Add a reduction theorem before replacing it by `H^2(W;F_2)`.

### 10. Hybrid Locality Checks Only A Binary Shadow

Status: valid, severity 2.

The eight-word atlas checks a binary two-colored associativity shadow.
Full factorization needs units, symmetric group actions, all finite
partitions, descent/cosheaf compatibility, and higher operadic
coherence.

Main anchors: `main.tex:6476`, `main.tex:6528`,
`main.tex:7357`.
Guide anchor:
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:319`.

Heal:

- State the eight-word atlas as a necessary binary check.
- Add the full factorization axioms as the remaining construction.

### 11. Quotient-After-Correspondence Is Not Yet A Functor

Status: valid, severity 1.

The hybrid quotient `Q_{E,R}` and its compatibility morphisms
`\theta^Q` are supplied as data, not constructed as a pseudofunctor on
the correspondence category.

Main anchors: `main.tex:6532`, `main.tex:6570`,
`main.tex:6836`, `main.tex:10014`.

Heal:

- Construct `Q_{E,R}` as a pseudofunctor with coherent `\theta^Q`
  maps.
- Until then, state hybrid comparison theorems conditional on this
  quotient data.

### 12. Wrapped Legs May Need Multiple Anchors

Status: valid, severity 1.

A single determinant anchor can lose relative data when several wrapped
legs occur.  A finite multiset of anchors, or a proof that all anchors
collapse losslessly, is required.

Main anchors: `main.tex:6134`, `main.tex:6273`,
`main.tex:6329`, `main.tex:6385`, `main.tex:6506`.

Heal:

- Replace the single-anchor datum by a finite anchor multiset in the
  wrapped sector.
- Or prove the single-anchor collapse theorem.

### 13. Source Cobar And Koszul Claims Depend On An Unbuilt Source

Status: valid, severity 2.

`C_{X,R}=B_E^{ch}(F_X,R^{hyb})` is valid only after the source exists,
is augmented, lies in the appropriate finite-generation or coderived
domain, and has bounded bar length in the relevant windows.

Main anchors: `main.tex:5831`, `main.tex:5953`.

Heal:

- Make the source coalgebra theorem conditional on the finite-stage
  source package and the augmentation/domain hypotheses.

### 14. Source Windows And Target Windows Are Not Matched

Status: valid, severity 2.

`N_R^\Delta` is bookkeeping.  It does not by itself prove that active
source degrees lie inside `\Gamma_R^\Pi`, or that HN height matches
automorphic height.

Main anchors: `main.tex:8660`, `main.tex:9166`,
`main.tex:9401`.

Heal:

- Add a source-support theorem relating HN height, active compact
  degrees, and automorphic window height.
- Otherwise keep finite-window equality conditional.

### 15. D0-Pf Can Become Tautological

Status: valid, severity 1.

If D0-Pf assumes the target exponents, the Pfaffian equality becomes a
recognition theorem, not source evidence.

Main anchors: `main.tex:9070`, `main.tex:9151`,
`main.tex:9400`, `main.tex:10607`, `main.tex:10914`.

Heal:

- Separate "source computation of exponents" from "recognition against
  the target denominator."
- Mark the latter as conditional recognition unless the former is
  produced.

### 16. Automorphic Attribution Is Too Compressed

Status: valid, severity 2.

The exact `\Delta_5` product, denominator interpretation, and 64
normalization are attributed too broadly under "Borcherds."  The exact
paper trail should name the Gritsenko-Nikulin sources used for this
normalization, while keeping Borcherds as the general automorphic-product
machine.

Main anchors: `main.tex:2221`, `main.tex:2242`.

Heal:

- Cite Borcherds for the general theorem.
- Cite the Gritsenko-Nikulin `\Delta_5` product/denominator source for
  the exact constants and denominator identity.
- Add a row-by-row source map before using the eight-row
  Gritsenko-Clery catalogue as a proved import.

### 17. `D_X^{-1}` Has A Sign Regression

Status: valid, severity 2.

The manuscript fixes the normalized determinant `D_X`, but later writes
`Z^{vir}_{Borch}:=\pm D_X^{-1}`.  That reintroduces an ambiguity already
removed by normalization.

Main anchors: `main.tex:745`, `main.tex:749`,
`main.tex:11831`, `main.tex:11839`.

Heal:

- Write the target inverse as `D_X^{-1}`.
- Reserve any sign ambiguity for the orientation-lifted Pfaffian before
  O1/O1+ are proved.

### 18. Rank-One Brauer/Pin Parity Is Not Yet A Class

Status: valid, severity 2.

The criterion `c_1(L)^2/2 mod 2` is a scalar intersection parity unless
GRR identifies it with the required class in `H^2(M_red;F_2)`.

Main anchors: `main.tex:2526`, `main.tex:2576`.

Heal:

- Add the GRR comparison producing the obstruction class.
- Or present the formula as a numerical diagnostic, not the full
  obstruction class.

### 19. Reduced Orientation Transport Needs Its Own Hypotheses

Status: valid, severity 1.

Joyce-Upmeier or BBDJS orientation on unreduced CY3 moduli does not
automatically survive reduced cosection, quotient, finite stabilizers,
and age terms.

Main anchors: `main.tex:1378`, `main.tex:1395`,
`main.tex:2570`, `main.tex:2575`, `main.tex:3861`,
`main.tex:3895`.
Bibliography anchor: `proj.bib:471`.

Heal:

- State the reduced orientation transport theorem with all reduction,
  quotient, and finite-stabilizer hypotheses.
- Keep compact reduced Hall coefficients conditional until this theorem
  is proved.

### 20. Pfaffian Line Comparison Is Missing

Status: valid, severity 2.

Choosing a sign or leading coefficient does not construct an isomorphism
between the source Pfaffian line and the automorphic line, nor does it
prove uniqueness of the top-cohomology generator.

Main anchors: `main.tex:1055`, `main.tex:1072`,
`main.tex:1446`, `main.tex:1459`, `main.tex:3738`,
`main.tex:3848`.

Heal:

- Add line comparison as explicit D0/Pf data.
- Or weaken the target statement to equality of normalized
  q-expansions after a supplied line comparison.

### 21. Status Vocabulary Is Inconsistent

Status: valid, severity 1.

The guide, roadmap, critique table, and manuscript use inconsistent
status words such as solved, corrected, conditional, roadmap, and
constructed.  This hides unresolved proof obligations.

Guide anchors:
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:517`,
`notes/attack_whitepaper_analysis_20260428_090346_guide.md:518`.
Plan anchors: `notes/reconstitution_plan_20260428.md:682`,
`notes/reconstitution_plan_20260428.md:683`.
Main anchors: `main.tex:361`, `main.tex:384`.

Heal:

- Adopt a canonical status vocabulary:
  proved, computed, imported, conditional, conjectural, open,
  obstructed.
- Split "wording repaired" from "mathematics closed" in
  `notes/critique_resolution_table.md`.

### 22. Proof Order And Dependency Graph Are Not Clean

Status: valid, severity 1.

The roadmap says the scalar square comes after the chain, but Part I
already contains OP/DT material.  D0, hybrid, and O2 also risk a
dependency cycle.

Plan anchors: `notes/reconstitution_plan_20260428.md:58`,
`notes/reconstitution_plan_20260428.md:76`,
`notes/reconstitution_plan_20260428.md:412`,
`notes/reconstitution_plan_20260428.md:424`,
`notes/reconstitution_plan_20260428.md:446`,
`notes/reconstitution_plan_20260428.md:448`.
Critique anchor: `notes/critique_resolution_table.md:21`.
Main anchors: `main.tex:100`, `main.tex:127`, `main.tex:11643`.

Heal:

- Add a one-page dependency DAG.
- Treat OP/DT in Part I as target motivation and scalar check, not as
  proof of the primitive Pfaffian source.
- Factor a common finite Hall source kernel below D0, hybrid, and O2.

### 23. Provenance And QA Are Not Complete

Status: valid, severity 2.

The criticism guide should record extraction command, tool version,
page anchors, and verification route for guide-derived claims.  The
final QA commands have not been recorded for the current roadmap.

Heal:

- Add extraction and verification metadata to the provenance note.
- Before manuscript integration, run and record:

```bash
git diff --check
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
make
```

## False Or Contained Attacks

The following attacks did not break the current stable core:

- No sign error was found in the bilinear defect `B` or
  `\overline\Pi`.
- The `D_5(2Z)` factor survived target-side automorphic checking.
- The monic `D_5`, factor `64`, and `m=0` cusp factors remain
  consistent.
- The Maass character issue is target-side and remains separate from
  Hall orientation signs.
- Negative Fourier coefficients are not being interpreted as literal
  negative Hilbert-space dimensions in the stable text.
- The Mukai-Gram shifts checked in the manuscript survived attack.
- The manuscript does not currently claim a fully constructed compact
  BPS Hilbert operator trace; its strongest compact claims remain
  conditional, though the roadmap language must be tightened.
- The checked CY3 passages do not contain the alleged CY3/CY4 Todd/Bott
  confusion.  Any CY4 reference should remain explicitly analogical.

## Healed Roadmap

The next roadmap revision should be:

1. Begin with the stable lattice theorem: formal Mukai-Gram algebra,
   bilinear defect, central extension, and normal-ordered Gram map.
2. Immediately restrict Hall language to the algebraic even D6-D2-D0
   Mukai sector.
3. Add the torsion invariant `I(Q,P)` and separate primitive saturation
   from torsion-one duality descent.
4. State the raw-descent obstruction only for strict homogeneous
   fixed-lift raw pushforwards, with mixed-lift fibre summation as an
   open case.
5. Treat `(c,T)` as coefficient-system or central-translation data, and
   prove no overcount before using it as a source degree.
6. Insert a common finite Hall source kernel below D0, hybrid, O2,
   orientation, and cobar comparison.
7. Replace O1 by a full equivariant obstruction class, O1+ by groupoid
   cohomology, and O2 by local wall signs until globalization is proved.
8. Demote the eight-word hybrid atlas to a necessary binary check, not
   the full factorization theorem.
9. Keep D0-Pf as conditional source recognition unless the compact
   source computes exponents independently of the target denominator.
10. Fix automorphic attribution: Borcherds for the general product
    theorem; Gritsenko-Nikulin for the exact `\Delta_5` denominator
    normalization used here; Gritsenko-Clery only after a row-by-row
    source map.
11. Write the normalized inverse as `D_X^{-1}`, not `\pm D_X^{-1}`.
12. Add a status ledger with the vocabulary
    proved/computed/imported/conditional/conjectural/open/obstructed.

## Residual Proof Obligations

The current evidence needed to move claims into the stable core is:

- a mixed-lift raw pushforward theorem or counterexample;
- a torsion-one primitive descent theorem for the relevant lattice
  orbits;
- a finite-type compact Hall source with support, orientation, and
  pull-push hypotheses verified;
- a functorial `(c,T)` grading and no-overcount theorem;
- a full equivariant reduced orientation class and Weyl groupoid
  cocycle calculation;
- an O2 wall atlas covering all finite HN windows and boundary strata;
- a hybrid pseudofunctor `Q_{E,R}` with coherent `\theta^Q` maps;
- a full factorization proof beyond binary two-colored associativity;
- a source exponent computation independent of target recognition;
- a Pfaffian-line-to-automorphic-line comparison;
- a primary-source audit of the OP/DT scalar square and exact
  Gritsenko-Nikulin normalization.

Until these are supplied, the correct manuscript status is:

- lattice normal ordering: proved formal algebra;
- target automorphic determinant: imported/computed;
- OP/DT scalar square: imported/computed after source audit;
- compact Dirac source: conditional/open;
- Pfaffian square-root realization: conditional recognition;
- K3 x E physical realization: conjectural/open beyond the algebraic
  even sector.
