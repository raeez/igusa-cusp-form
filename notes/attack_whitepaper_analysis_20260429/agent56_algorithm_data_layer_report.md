# Agent56 Algorithm/Data-Layer Report

Scope: proposal-only algorithm/data-layer review for
`/Users/raeez/igusa-cusp-form`.  No source edits.  Writable surface limited
to this report.

Latest attack source reviewed:

- `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`
- extracted text:
  `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`
- PDF timestamp: 2026-04-29 19:27:14
- PDF sha256:
  `d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1`

Compared against:

- `main.tex`, sha256
  `fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280`
- `compute/verify_lattice.py`, sha256
  `b467b61a5532d923c42a513bf694d7462698151856aa592485afc6a66f66dec4`
- `compute/verify_square_root.py`, sha256
  `6c3e9a8c70ba0e4fb26feda9395ef31ce4c1bf5dc9250c1ced2c5be5d28db766`

Commands run:

```bash
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
find . -maxdepth 4 \( -path './.git' -o -path './out' -o -path './.build_logs' -o -path './materials/raw' \) -prune -o -type f \( -name '*.json' -o -name '*.jsonl' -o -name '*.csv' -o -name '*.yaml' -o -name '*.yml' -o -name '*.mtx' -o -name '*.sage' -o -name '*.magma' -o -name '*.lean' -o -name '*.v' \) -print
rg -n "algorithm|machine|checkable|finite source|UDI|source certificate|target check|executable" materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt main.tex compute notes/attack_whitepaper_analysis_20260429/agent*.md
```

## Verdict

The current repository has executable target checks.  It does not have a
machine-checkable finite source certificate.

The latest PDF introduces `UDI` as a finite source object and lists
algorithms/data tables for it.  As written, those algorithms are executable
only after a data layer exists.  In the checkout, no such data layer exists:
there is no `data/finite_source/`, no manifest, no source provenance table,
no JSON/CSV/MTX certificate files, no source operation tensors, no radical
kernel files, no PBW comparison artifacts, and no finite-source verification
suite.

The manuscript should distinguish three objects.

1. `target_reference`: the Gritsenko--Nikulin/Kac/Borcherds target
   denominator algebra and its finite windows.  This is currently partly
   executable.
2. `UDI^{alg}`: a finite target-built algebraic envelope, if introduced.
   It can be machine-checked as an algebraic restatement of the imported
   denominator algebra.  It is not a compact Hall source.
3. `compact_source_candidate`: actual `K3 x E` source data with compact
   provenance, finite Hall correspondences, orientations, product/coproduct
   matrices, pairings, radicals, PBW data, and transitions.  This does not
   exist in the checkout.

Therefore `main.tex` is currently safe where it says "target check",
"conditional certificate", or "open realization problem".  It becomes false
if it says that UDI constructs the compact finite source, that NO1--NO7 hold
for a source, or that primitive recognition has been constructed without the
finite certificate.

## Latest PDF Claims

Confirmed from
`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`:

- Lines 27833--27845 say the current manuscript identifies the finite atlas,
  hybrid wrapped factorization, chain-level normal ordering, source
  coalgebra, and primitive comparison as missing state-side construction
  data.
- Lines 27848--27879 propose to construct a universal finite
  Dirac--Igusa Hall source with normal-ordered grading, finite Hall
  multiplication/coproduct, primitive Lie bracket, orientation-gerbe twisted
  states, hybrid local/wrapped factorization, source chiral coalgebra, Dirac
  block, super-Pfaffian, and machine-checkable NO1--NO7/PBW/radical/transition
  tests.
- Lines 27923--27948 call this the universal compact finite Hall--Dirac
  source and make `K3 x E` geometry a realization functor into it.
- Lines 29517--29732 state the central UDI theorem: NO1--NO7 hold, PBW
  monomials form a basis, radical quotient is already taken, source coalgebra
  is finite conilpotent, and the Pfaffian limit is `Delta_5`.
- Lines 29802--29943 list machine-checkable finite data: degree tables,
  bracket tensors, pairing matrices, product tensors, coproduct tensors,
  PBW bases, radical kernels, normal-ordering tables, hybrid operation
  tables, and transition matrices.

The attack point is not that such a layer is impossible.  The point is that
the checkout does not contain it, and the proposed UDI proof at lines
29685--29724 imports the BKM bracket, Kac presentation, invariant form, GN
multipities, and Borcherds product.  That is a target-envelope proof unless
independent source data are supplied.

## Current Executable Checks

`compute/verify_lattice.py` declares its scope at lines 2--6:
target-side lattice and normal-form checks only; its pairings are
Gram/Pfaffian lattice pairings, not compact Hall Hopf pairings.

It verifies:

- Pfaffian Gram matrix in the basis
  `(f_1,f_2,f_3,f_-2,f_-1)`;
- type-II simple-root Gram matrix
  `[[2,-2,-2],[-2,2,-2],[-2,-2,2]]`;
- Weyl vector `rho=(1,-1/2,1)` with `(rho,delta_i)=-1`;
- reflection invariance for the three simple roots;
- sample `alpha(n,l,m)` to `z`-pairing substitutions.

`compute/verify_square_root.py` declares its scope at lines 1--18:
exact target-side Borcherds/Gritsenko--Nikulin arithmetic only; it does not
construct compact Hall stacks, protected source representatives, Hopf
pairings, coproducts, or radical kernels.

It verifies:

- `phi_{0,1}` coefficients through the hard-coded window at lines 416--429;
- `prod_{k>=1}(1-q^k)^9` through `q^9`;
- `[q*r*s] 64^{-1} Delta_5/(qrs)^{1/2}=93`;
- first timelike target presentation split `29|93`, with signed difference
  `29-93=-64`;
- height-four additive checks
  `(2,1,1)=(1,2,1)=(1,1,2)=90` and `(2,2,2)=-540`;
- height-four signed/additive/residual checks `108|90|18`;
- doubled isotropic checks `10|9|1`;
- real-string pairing/exponent checks:
  real-real exponent `3`, complementary real-isotropic exponent `5`,
  real-timelike exponent `3`.

The scripts passed in this run.  They verify target arithmetic.  They verify
zero compact source data.

## Current Manuscript Posture

`main.tex` already contains the correct firewall in several places:

- Lines 886--921: the Dirac/Pfaffian object is an open recognition target;
  existence of the first-order protected operator is open.
- Lines 1143--1178: the Dirac--Pfaffian theorem assumes a supplied compact
  first-order certificate; the proved part is the normal-ordered lattice
  homomorphism and the imported target part is the Borcherds--GN denominator
  algebra.
- Lines 10065--10430: the `D_0` certificate is finite-stage data with
  transition residuals; these equalities are not consequences of inverse-limit
  notation.
- Lines 10982--11015: the strongest object constructed from automorphic input
  alone is the finite `K_0` Pfaffian shadow; it is not a compact Hall object,
  not a Pfaffian line, and not a first-order operator.
- Lines 11044--11090: source computation of the Igusa exponents is an open
  problem.
- Lines 12577--12686: finite-window primitive recognition requires
  representatives, relations, full parity dimensions, Hopf pairing/radical,
  no-extra-relations, PBW, and exact triangular completion.
- Lines 13183--13187: `compute/verify_square_root.py` is target-only and does
  not verify compact Hall representatives, Hopf pairings, coproducts, or
  radicals.
- Lines 13303--13360: finite `W_{\le3}` NO7 verification requires source
  matrices; target tables do not supply them.
- Lines 13374--13511: state-side construction of `D_0` and the
  Dirac--Igusa certificate remains open.

Thus the manuscript should not absorb the PDF's UDI theorem as written.
The safe move is to add an algebraic target-envelope layer, or leave UDI as
a proposed data interface, while preserving the compact realization problem.

## Data That Should Exist

Two separate data trees should exist.  One is target reference data.  The
other is source certificate data.  Mixing them is the main failure mode.

```text
data/udi/v1/
  manifest.json
  target_reference/
    root_lattice.json
    phi_01_coefficients.jsonl
    gn_product_windows.jsonl
    gn_wle3_target.json
    gn_wle3_brackets.json
    gn_wle3_pbw_reference.json
    height4_target_residuals.json
  udi_alg/
    windows/
      R000/
        window.json
        primitive_spaces.jsonl
        generators.csv
        brackets/
          B__*.mtx
        pairings/
          G__*.mtx
        radicals/
          target_radical__*.mtx
          quotient_maps__*.mtx
        pbw/
          generator_order.csv
          hall_lyndon_words.csv
          relation_matrix.mtx
          quotient_basis.csv
          gr_comparison.mtx
        normal_ordering/
          sL_table.jsonl
          N_gamma_eta.jsonl
        hybrid/
          colors.json
          operation_table.jsonl
          eight_word_checks.jsonl
        coalgebra/
          bar_generators.csv
          differential.mtx
          coproducts/*.mtx
        dirac/
          blocks.jsonl
          pfaffian_factors.jsonl
          cusp_trivialization.json
      R001/
        ...
    transitions/
      R001_to_R000/
        primitive_projection__*.mtx
        pbw_projection.mtx
        coalgebra_projection.mtx
        pfaffian_projection.json
  compact_realization/
    README.md
    stages/
      R000/
        stage.json
        hnewords.jsonl
        source_provenance.jsonl
        fibres_over_pi.jsonl
        spaces.csv
        bases/
          primitives_pos.csv
          primitives_neg.csv
          cartan.csv
          hall_state.csv
          source_coalgebra.csv
        representatives/
          real_simple.csv
          isotropic.csv
          timelike_delta123.csv
          negative_roots.csv
        operations/
          products/*.mtx
          brackets/*.mtx
          coproducts/*.mtx
          hybrid/*.jsonl
        pairings/
          G__*.mtx
          quotient_pairing__*.mtx
        radicals/
          K__*.mtx
          Q__*.mtx
          splitting__*.json
        relations/
          chevalley.jsonl
          serre.jsonl
          orthogonality.jsonl
          super_sign.jsonl
          jacobi.jsonl
          real_string.jsonl
          no_extra_relations.jsonl
        pbw/
          generator_order.csv
          word_basis.csv
          relation_matrix.mtx
          source_presentation.mtx
          target_presentation.mtx
          kernel_expected.mtx
          gr_source.mtx
          gr_target.mtx
          gr_comparison.mtx
        normal_ordering/
          theta_phys.json
          theta_hat.json
          hochschild_differentials/*.mtx
          negative_cyclic/*.mtx
          flag_pentagons.jsonl
          frobenius.jsonl
        orientation/
          gerbes.jsonl
          quotient_classes.jsonl
          finite_stabilizers.jsonl
          null_trivializations.jsonl
          weyl_lifts.json
          pfaffian_walls.jsonl
        dirac/
          blocks.jsonl
          pfaffian.json
          leading_cusp_trivialization.json
      R001/
        ...
    transitions/
      R001_to_R000/
        maps.json
        rho_P__*.mtx
        rho_H__*.mtx
        rho_F__*.mtx
        rho_K__*.mtx
        rho_Pf__*.mtx
        pbw_filtration_maps/*.mtx
        cochain_maps/*.mtx
        transition_residuals.json
```

The top-level `manifest.json` must declare:

```json
{
  "schema_version": "udi-finite-data-v1",
  "coefficient_ring": "QQ",
  "source_kind": "target_reference | udi_alg | compact_source_candidate",
  "paper_sha256": "fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280",
  "attack_pdf_sha256": "d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1",
  "stage_ids": ["R000"],
  "window_ids": ["W_le3"],
  "matrix_convention": "column_vectors",
  "tensor_basis": "lexicographic",
  "hashes": {}
}
```

Allowed `source_kind` values:

- `target_reference`: imported denominator target data.  Cannot satisfy a
  source certificate.
- `udi_alg`: target-built finite algebraic envelope.  Can support a target
  envelope proposition, not a compact Hall theorem.
- `mock_source_fixture`: artificial data used to test scripts.  Cannot
  satisfy a theorem.
- `compact_source_candidate`: actual `K3 x E` source candidate.  Requires
  source provenance and source operation tensors.

Every matrix file must be exact rational/integer data.  Floats are forbidden.
Every matrix must record domain basis, codomain basis, parity convention,
and source kind.

## Scripts That Should Exist

The current two scripts should remain target checks.  New scripts should be
separated by layer.

```text
compute/target/
  verify_lattice.py
  verify_square_root.py
  verify_target_wle3.py
  verify_height4_residuals.py
  verify_op_normalization.py

compute/udi/
  schema.py
  exact_linalg.py
  root_window.py
  tensor_basis.py
  free_lie.py
  pbw.py
  load_manifest.py
  verify_manifest.py
  verify_schema_integrity.py
  verify_udi_alg_target_envelope.py
  verify_udi_alg_pwb_and_radical.py
  verify_udi_alg_normal_ordering.py
  verify_udi_alg_hybrid_words.py
  verify_udi_alg_dirac_pfaffian.py
  verify_udi_alg_transitions.py
  verify_all_udi_alg.py

compute/finite_source/
  load_certificate.py
  verify_manifest.py
  verify_schema_integrity.py
  verify_source_provenance.py
  verify_no1_finite_fibres.py
  verify_no2_operations_transitions.py
  verify_no3_cochains.py
  verify_no4_flag_pentagon.py
  verify_no5_jacobi.py
  verify_no6_frobenius.py
  verify_no7_hopf_radical.py
  verify_wle3_primitive_recognition.py
  verify_pbw_no_extra.py
  verify_orientation_cyclic.py
  verify_hybrid_eight_words.py
  verify_source_coalgebra.py
  verify_dirac_pfaffian.py
  verify_transitions_ml.py
  verify_all.py
```

Required verifier behavior:

- `verify_manifest.py`: all declared files exist; hashes match; source kind is
  supported; coefficient ring is exact.
- `verify_schema_integrity.py`: dimensions, bases, tensor bases, parity
  blocks, and matrix shapes match.
- `verify_udi_alg_target_envelope.py`: confirms that `UDI^{alg}` is built
  from the imported target presentation and labels the result as target-built.
- `verify_source_provenance.py`: rejects `compact_source_candidate` if any
  basis vector lacks stack/stratum, vanishing-cycle, orientation, compact
  support, and HN-word provenance.
- `verify_no1_finite_fibres.py`: finite fibres over normal-ordered degree
  labels.
- `verify_no2_operations_transitions.py`: product/coproduct/protected
  integration commute with transitions.
- `verify_no3_cochains.py`: Hochschild and negative-cyclic normal-ordering
  equations.
- `verify_no4_flag_pentagon.py`: two-step flag/associator pentagon residuals.
- `verify_no5_jacobi.py`: bracket Jacobi on retained triples.
- `verify_no6_frobenius.py`: Hopf adjointness and Frobenius compatibility.
- `verify_no7_hopf_radical.py`: radical is both Lie ideal and coideal; quotient
  pairing is non-degenerate; transitions preserve kernels.
- `verify_wle3_primitive_recognition.py`: first source recognition window,
  including `29|93` compact bases in degree `delta_123`.
- `verify_pbw_no_extra.py`: finite presentation kernel equals the
  Borcherds--Kac plus invariant-pairing radical kernel.
- `verify_dirac_pfaffian.py`: checks the declared finite operator, Pfaffian
  line, parity convention, and cusp trivialization.  It must reject a pure
  formal factor table as a compact Pfaffian line.

## First Mandatory Window

The first source witness is `W_{\le3}`.  It must include positive,
negative, and Cartan pieces:

```text
W_le3 = {c1*d1 + c2*d2 + c3*d3 :
         c_i >= 0, 1 <= c1+c2+c3 <= 3}
```

Target reference dimensions:

```text
d_i:                  1|0
d_i+d_j:              10|0
2*d_i+d_j:            1|0
d1+d2+d3:             29|93
```

The last row is decisive.  The script currently verifies the target split
`29|93`.  A source certificate must exhibit 29 even compact primitive basis
vectors and 93 odd compact primitive basis vectors, plus product, bracket,
coproduct, pairing, radical, PBW, and transition data.  Signed dimension
`-64` is not recognition.

## Immediate Safe Manuscript Wording

Safe replacement for the UDI theorem as written:

```tex
\begin{definition}[Universal algebraic Dirac--Igusa target envelope]
Fix a finite downward-saturated root window \(R\).  Let
\(\mathfrak g_{\Delta_5,\le R}\) be the corresponding finite truncation of
the imported Gritsenko--Nikulin/Kac denominator algebra, with its parity
spaces, invariant pairing, radical quotient, and PBW word convention.  The
algebraic Dirac--Igusa target envelope
\(\mathrm{UDI}^{\mathrm{alg}}_R\) is the finite package consisting of this
truncated primitive Lie superalgebra, its truncated enveloping algebra, the
chosen PBW basis, the target normal-ordered degree labels, the formal
target hybrid operation table, the formal target bar coalgebra, and the
formal first-order factors whose normalized product is the
Borcherds--Gritsenko--Nikulin product.
\end{definition}
```

```tex
\begin{proposition}[Target-envelope normalization]
For \(\mathrm{UDI}^{\mathrm{alg}}_{\Delta_5,E,L}\), the associated formal
product is \(\Delta_5\) after the stated cusp normalization.  This is a
finite-window restatement of the Borcherds--Gritsenko--Nikulin product
formula.  It does not construct a compact \(K3\times E\) Hall source,
orientation gerbe, protected primitive representatives, source coalgebra,
or geometric Pfaffian line.
\end{proposition}
```

```tex
\begin{openproblem}[Compact realization of the algebraic envelope]
Construct finite compact Hall--Dirac source data
\(H^{\mathrm{geom}}_{X,R}\) and compatible functors
\[
R_{X,R}:H^{\mathrm{geom}}_{X,R}\longrightarrow
\mathrm{UDI}^{\mathrm{alg}}_R
\]
preserving normal-ordered degrees, product, coproduct, primitive bracket,
orientation-gerbe twist, hybrid local/wrapped operations, source coalgebra,
Dirac blocks, Pfaffian line with cusp trivialization, and transition maps.
The existence of these functors is the compact \(K3\times E\) realization
problem.
\end{openproblem}
```

Forbidden until data and verifiers exist:

- "This is the constructed finite compact source object."
- "NO1--NO7 hold" without matrix data and verifier output.
- "The radical quotient is already taken" for a source.
- "The source coalgebra is constructed" if it is target bar data.
- "Quotient orientation is trivial because the universal base is finite
  algebraic" as a statement about compact geometry.
- "Primitive recognition is proved" from target dimensions or signed
  superdimensions alone.

## Attack Ledger

```yaml
- id: A56-01
  severity: 1
  status: valid
  lens: source_target_firewall
  target: revision lines 27861-27879, 29517-29620
  claim: "UDI is the universal finite compact Hall-Dirac source."
  failure: "The proposed proof builds from the BKM/GN/Kac target algebra unless independent source data are supplied."
  evidence: "revision lines 29685-29724; main.tex 10982-11015; compute/verify_square_root.py 15-18"
  repair: "Call it UDI^alg target envelope, or supply compact_source_candidate data and finite-source verifier output."

- id: A56-02
  severity: 1
  status: valid
  lens: executable_certificate
  target: revision lines 29802-29943
  claim: "The finite data layer is executable."
  failure: "No data tree, manifest, matrix files, or finite-source verifier exists in the checkout."
  evidence: "find found only ./.claude/settings.local.json among JSON/CSV/YAML/MTX/Sage/Magma/Lean/Coq-style finite data files outside pruned build/materials paths."
  repair: "Create data/udi/v1 and compute/finite_source; keep target_reference, udi_alg, and compact_source_candidate source kinds disjoint."

- id: A56-03
  severity: 1
  status: valid
  lens: no7_hopf_radical
  target: main.tex 13303-13360; revision lines 29655-29662
  claim: "NO1-NO7 hold and the radical quotient is already taken."
  failure: "Current scripts do not load product, coproduct, pairing, radical, quotient, or transition matrices."
  evidence: "compute/verify_lattice.py 2-6; compute/verify_square_root.py 15-18; main.tex 13349-13360"
  repair: "Add finite source matrices and verify_no7_hopf_radical.py; otherwise state only target PBW/radical facts."

- id: A56-04
  severity: 1
  status: valid
  lens: primitive_recognition
  target: W_le3 first hard window
  claim: "The determinant data recognize the compact primitive algebra."
  failure: "The script verifies target 29|93 but supplies no compact 29 even and 93 odd bases, pairings, radicals, operations, or PBW comparison."
  evidence: "compute/verify_square_root.py 401-438; main.tex 13131-13159"
  repair: "Require W_le3 compact source certificate before any recognition theorem label."

- id: A56-05
  severity: 2
  status: valid
  lens: orientation
  target: revision lines 29969-29972
  claim: "Quotient orientation is trivial in the universal source because the base is finite algebraic."
  failure: "A formal target algebra may choose a trivial sign device, but compact quotient orientation requires gerbes, finite stabilizer classes, Weyl lifts, wall data, and transition trivializations."
  evidence: "main.tex 1143-1178; main.tex 13400-13405"
  repair: "State triviality only for UDI^alg formal bookkeeping; keep compact orientation as realization data."

- id: A56-06
  severity: 2
  status: valid
  lens: pfaffian
  target: revision lines 29711-29724
  claim: "The UDI Dirac block super-Pfaffian proves Delta_5."
  failure: "With exponents imported as sdim g_gamma=f(nm,l), the Pfaffian product is the GN product in new notation, not a compact Pfaffian line theorem."
  evidence: "main.tex 886-921; main.tex 10994-11015; compute/verify_square_root.py 168-207"
  repair: "Use target-envelope normalization wording; require finite operator, Pfaffian line, parity convention, and cusp trivialization for compact source."
```

## Bottom Line

Current compute is useful and should be kept.  It verifies the denominator
target, not the source.  The next honest algorithmic milestone is not another
paragraph in `main.tex`; it is a finite data tree plus verifier suite whose
manifest prevents target tables from posing as compact source certificates.
