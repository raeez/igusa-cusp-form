# Agent45 finite source certificate latest report

Scope: proposal-only finite-source-data and certificate review for `/Users/raeez/igusa-cusp-form`.  No source edits.  Writable surface limited to this report.

Latest attack source reviewed:

- `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`
- extracted text: `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`
- PDF timestamp: 2026-04-29 19:27:14
- PDF sha256: `d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1`

Compared against:

- `main.tex`, sha256 `fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280`
- `compute/verify_lattice.py`, sha256 `b467b61a5532d923c42a513bf694d7462698151856aa592485afc6a66f66dec4`
- `compute/verify_square_root.py`, sha256 `6c3e9a8c70ba0e4fb26feda9395ef31ce4c1bf5dc9250c1ced2c5be5d28db766`

Commands run:

```bash
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
rg -n -i "finite|certificate|executable|schema|row|witness|comput|verify|primitive|recognition|table|source data|machine|artifact|JSON|CSV|hash|reproduc" materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt main.tex compute/*.py
find compute -maxdepth 3 -type f -print
find . -maxdepth 3 \( -name '*.json' -o -name '*.csv' -o -name '*.yaml' -o -name '*.yml' -o -name '*.sage' -o -name '*.magma' -o -name '*.lean' -o -name '*.coq' -o -name '*.out' -o -name '*.log' \) -print
```

Verdict: no primitive-recognition claim may ship as a construction.  It may ship only as a conditional recognition certificate or open realization problem until the finite source certificate below exists and its gates pass.

## 1. Latest PDF demands

The latest PDF moves beyond the current manuscript's "if the compact finite Hall-Dirac source exists" posture.  It demands construction of a finite-source algebraic object before any K3 x E realization comparison.

Confirmed from the latest extraction:

- The PDF states that the current manuscript still identifies the finite atlas `A_R`, hybrid wrapped factorization, chain-level normal ordering, source coalgebra, and primitive comparison as missing state-side construction data, not consequences of the determinant or target denominator algebra (`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:27833-27845`).
- It demands a universal finite Dirac-Igusa Hall source with normal-ordered charge grading, finite Hall multiplication and coproduct, primitive Lie bracket, orientation-gerbe-first twisted states, hybrid local/wrapped colored factorization, source chiral coalgebra, Dirac block operator, super-Pfaffian, and machine-checkable NO1-NO7, PBW, radical, and transition tests (`:27861-27879`).
- It states that K3 x E geometry should be a realization functor into this already constructed universal object, preserving degrees, correspondences, orientations, hybrid operations, primitives, coalgebras, and Pfaffians (`:27881-27892`, `:27923-27948`).
- It demands a finite normal-ordered charge group, product law, inverse, and additive Gram map, with raw inclusion, zero-Gram splitting, and linear target lift kept distinct (`:27980-28209`).
- It demands finite active windows `A_R`, downward saturation, two-stage multiplication windows, and the rule that fixed finite stages need not be internally closed under multiplication, but the tower must be (`:28211-28293`).
- It demands finite BKM/source Lie data, Hall-Lyndon/PBW bases, radical quotient data, matrix NO1-NO7 checks, orientation-gerbe-first Dirac modules, hybrid local/wrapped source data, finite source coalgebra, Dirac blocks, Pfaffian, and a geometric realization theorem (`:28295-28953`, `:29750-29943`).
- It explicitly says the finite machine-readable layer has degree tables, bracket tensors, pairing matrices, product tensors, coproduct tensors, PBW bases, radical kernels, normal-ordering tables, hybrid operation tables, and transition matrices (`:29802-29943`).

The key sentence for shipping discipline is the PDF's final theorem-spine replacement:

```text
virtual determinant -> normal-ordered lattice -> universal finite Hall-Dirac source
```

with geometry and recognition second (`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:30037-30043`, `:30168-30170`).

## 2. Current repository state

Confirmed:

- `main.tex` now contains a strong conditional certificate scaffold.  The first-order `D_0` certificate starts at `main.tex:10065`.  It requires finite-type bounded HN stages, finite d-critical/cosection Hall atlases, and Mittag-Leffler descent (`main.tex:10074-10213`).
- `main.tex` defines finite support windows, target/test windows, finite stage packages, and successor transition residuals (`main.tex:10219-10430`).
- `main.tex` defines NO1-NO7 finite verification diagrams for normal ordering (`main.tex:9217-9368`).
- `main.tex` defines a cofinal finite-window primitive-recognition certificate with R1-R8 clauses: representatives, relations, full parity dimensions, Hopf pairing/radical, no extra relations, generation, PBW, exact triangular completion (`main.tex:12577-12686`).
- `main.tex` correctly says that finite objects must be produced; otherwise a completed isomorphism is only a determinant or character comparison (`main.tex:12688-12729`).
- `main.tex` gives the first saturated recognition window and exact finite NO7 source protocol, including explicit compact primitive bases, parity splittings, pairing matrices, radical bases, product matrices, coproduct matrices, bracket matrices, and successor matrices (`main.tex:13039-13360`).
- `main.tex` ends the relevant open problem by stating that the proved lattice normal-ordering theorem, imported denominator algebra, and scalar square do not construct the compact state-side certificate (`main.tex:13374-13511`).

Observed in `compute/`:

- Only two scripts exist: `compute/verify_lattice.py` and `compute/verify_square_root.py`.
- `compute/verify_lattice.py` declares itself target-side: Gram/Pfaffian lattice pairings, not compact Hall Hopf pairings (`compute/verify_lattice.py:1-6`).
- `compute/verify_square_root.py` declares itself target-side: Borcherds/Gritsenko-Nikulin arithmetic only, not compact Hall stacks, protected representatives, Hopf pairings, coproducts, or radical kernels (`compute/verify_square_root.py:1-18`).
- `python3 compute/verify_lattice.py` passed.  It prints the Pfaffian Gram matrix, type-II simple-root Gram matrix, `rho`, and "All lattice checks passed."
- `python3 compute/verify_square_root.py` passed.  It verifies the displayed `phi_{0,1}` rows, `[q*r*s] = 93`, `29|93`, height-four `108|90|18`, doubled isotropic `10|9|1`, and real-string exponent checks.

Confirmed missing from repository:

- no `data/finite_source/` tree;
- no JSON/JSONL/CSV/MTX certificate artifacts;
- no finite source manifest;
- no source provenance table;
- no compact source basis tables;
- no bracket/product/coproduct/pairing matrix files;
- no radical kernel matrices;
- no PBW comparison artifacts;
- no transition matrices;
- no executable NO1-NO7 verification suite;
- no primitive recognition verifier;
- no orientation-gerbe finite artifact verifier;
- no hybrid local/wrapped operation table or eight-word checker.

Therefore the current paper is honest if it says "certificate/open"; it is false if it says "primitive recognition constructed" or "compact source recognized" without the finite certificate.

## 3. Finite certificate schema

The certificate must be finite at each stage `R`.  It must be machine-readable.  Prose in `main.tex` is not the certificate.

Suggested path:

```text
data/finite_source/v1/
  manifest.json
  lattices/
    root_lattice.json
    gram_charge_lattice.json
  targets/
    gn_target_windows.jsonl
    gn_bkm_relations.jsonl
    gn_wle3_target.json
    gn_wle3_pbw.json
  stages/
    R000/
      stage.json
      degree_table.jsonl
      source_provenance.jsonl
      hnewords.jsonl
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
        imaginary_simple.csv
        isotropic.csv
        timelike_delta123.csv
        negative_half.csv
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

Required top-level `manifest.json` fields:

```json
{
  "schema_version": "finite-source-v1",
  "coefficient_ring": "QQ",
  "source_kind": "compact_source_candidate",
  "paper_commit": null,
  "main_tex_sha256": "fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280",
  "attack_pdf_sha256": "d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1",
  "stage_ids": ["R000"],
  "generator_order_file": "stages/R000/pbw/generator_order.csv",
  "hashes": {}
}
```

Allowed `source_kind` values:

- `target_reference`: imported GN/Kac/Borcherds target data.  Cannot satisfy compact-source fields.
- `mock_source_fixture`: artificial source for testing scripts.  Cannot satisfy compact-source fields.
- `universal_algebraic_source`: constructed target-side universal source.  Can support the PDF's universal-source theorem, but not K3 x E geometric realization unless realization maps are present.
- `compact_source_candidate`: actual K3 x E source certificate.  Must include source provenance, finite stack/stratum IDs, operation matrices, orientation data, and transitions.

Matrix conventions:

- exact rational or integer entries only; floats forbidden;
- column-vector convention;
- tensor basis lexicographic and recorded in every matrix metadata block;
- parity blocks stored separately unless a matrix is explicitly odd;
- product matrix `M_{alpha,beta}` has shape `dim(P_{alpha+beta}) x dim(P_alpha tensor P_beta)`;
- coproduct matrix `D_{rho}^{mu,nu}` has shape `dim(P_mu tensor P_nu) x dim(P_rho)`;
- bracket matrix `B_{alpha,beta}` is recomputed from products when products are present;
- pairing matrix `G_beta` pairs `P_beta` against `P_{-beta}` and has an independently recorded transpose convention;
- radical basis `K_beta` is stored as columns in source coordinates;
- quotient map `Q_beta` is explicit, not inferred from a basis order unless the splitting file declares that order.

## 4. Row witnesses

The first mandatory witness is `W_{\le 3}` because it is the first saturated finite primitive-recognition window named in `main.tex`.

For each `beta` in:

```text
W_le3 = {beta = c1*d1 + c2*d2 + c3*d3 :
         c_i >= 0, 1 <= c1+c2+c3 <= 3}
```

and for `-W_le3` and `0`, the certificate must include:

- root ID, coefficient vector, Gram triple, height, parity block;
- target parity dimensions, not only signed superdimension;
- source basis vectors, with source provenance;
- positive-negative pairing matrix;
- radical basis and quotient map;
- representative maps for real simple roots, isotropic roots, timelike `delta123`, negative root spaces, and Cartan;
- product, bracket, and coproduct matrices for every retained pair/decomposition;
- relation rows for Chevalley, real Serre, isotropic orthogonality, super sign, Jacobi, real-string checks, and `T_1+T_2+T_3=0`;
- PBW word basis and associated-graded comparison;
- transition maps to/from adjacent finite windows.

Minimum `W_{\le 3}` target witnesses:

```text
d_i:                  1|0
d_i+d_j:              10|0
2*d_i+d_j:            1|0
d1+d2+d3:             29|93
```

The last row is the first hard witness.  The source must exhibit 29 even and 93 odd compact primitive basis vectors, not merely signed dimension `-64`.  It must also supply bracket/coproduct/pairing/radical/PBW data on those spaces.  `compute/verify_square_root.py` verifies the target arithmetic at `compute/verify_square_root.py:401-438`; it does not supply compact primitives.

Height-four is not optional if the paper claims more than `W_{\le 3}`:

- signed target multiplicities `108`;
- additive simple coefficients `90`;
- residual `18`;
- real-string maps `(ad e_i)^3 w_s = 0`;
- even simple generators of multiplicity `90`;
- lower-word relations producing the residual `18`;
- pairing/radical/PBW compatibility.

This is already identified in `main.tex:13211-13260`.

## 5. Missing executable checks

Add a finite-source verification suite only after data exists.  Suggested path:

```text
compute/finite_source/
  schema.py
  exact_linalg.py
  load_certificate.py
  root_window.py
  tensor_basis.py
  free_lie.py
  pbw.py
  verify_manifest.py
  verify_target_arithmetic.py
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
  verify_dirac_pfaffian.py
  verify_transitions_ml.py
  verify_all.py
```

Each verifier must reject `target_reference` and `mock_source_fixture` for compact-source claims.

Required check semantics:

- `verify_manifest.py`: every declared file exists; hashes match; coefficient ring exact; schema version supported.
- `verify_schema_integrity.py`: dimensions, bases, tensor bases, parity blocks, and matrix shapes match declared domains/codomains.
- `verify_source_provenance.py`: every source basis vector has a finite stack/stratum or universal-source generator witness.  For `compact_source_candidate`, target-only provenance is fatal.
- `verify_no1_finite_fibres.py`: fibres over `\overline\Pi_X` are finite at every stage; transitions preserve fibres.
- `verify_no2_operations_transitions.py`: products, coproducts, pairings, protected integration, and stage transitions commute.
- `verify_no3_cochains.py`: Hochschild and negative-cyclic normal-ordering equations hold.
- `verify_no4_flag_pentagon.py`: two-step Hall flag/associator pentagons vanish; degree-level bilinearity alone is insufficient.
- `verify_no5_jacobi.py`: bracket Jacobi holds on all retained homogeneous triples.
- `verify_no6_frobenius.py`: Frobenius/Hopf adjointness holds for product, coproduct, bracket, and pairing.
- `verify_no7_hopf_radical.py`: radical is a Lie ideal and coideal; quotient tensor pairing is nondegenerate; transition maps preserve radical kernels.
- `verify_wle3_primitive_recognition.py`: R1-R8 for `W_{\le 3}` pass, including `29|93`.
- `verify_pbw_no_extra.py`: finite kernel equality and PBW associated-graded comparison pass.
- `verify_orientation_cyclic.py`: quotient gerbes, finite stabilizers, Weyl lifts, wall Pfaffian local models, and cyclic lifts pass.
- `verify_hybrid_eight_words.py`: LLL, LLW, LWL, WLL, LWW, WLW, WWL, WWW identities pass.
- `verify_dirac_pfaffian.py`: finite Dirac blocks, Pfaffian product, leading cusp normalization, and source-to-target Pfaffian comparison pass.
- `verify_transitions_ml.py`: finite-slice Mittag-Leffler stable-image or strict surjective transition criterion passes on every declared finite window.

## 6. Exact ship gates before primitive recognition

Gate 0. Claim label gate.

- If only `main.tex` and current `compute/` exist, the strongest allowed claim is: "conditional primitive-recognition certificate/open compact realization problem."
- Forbidden claim: "compact primitive algebra is recognized as `g_{\Delta_5}`" unless Gates 1-12 pass.

Gate 1. Source kind gate.

- A certificate manifest exists.
- `source_kind` is `compact_source_candidate` for a K3 x E claim, or `universal_algebraic_source` for the PDF's universal-source theorem.
- `target_reference` and `mock_source_fixture` are rejected for primitive-recognition construction claims.

Gate 2. Finite window gate.

- `A_R`, `\widehat\Gamma_R`, `\Gamma_R^\Pi`, `\Gamma_{\Delta,R}`, and `\Gamma_R^{test}` are materialized for at least the first stage containing `W_{\le 3}`.
- Downward saturation is checked.
- Two-stage product windows `A_R + A_{R'} -> A_{R+R'}` are checked.

Gate 3. Source provenance gate.

- Every basis vector in each primitive, Hall state, observable, coalgebra, and Dirac space has a source witness.
- For compact claims, source witnesses name finite stacks/strata, orientation-gerbe components, vanishing-cycle coefficient systems, compact-support convention, protected integration map, and HN word label.

Gate 4. Operation tensor gate.

- Product, bracket, coproduct, and pairing matrices exist for every retained pair/decomposition.
- Bracket matrices are consistent with product matrices and super signs.
- Matrix dimensions agree with declared parity and tensor bases.

Gate 5. NO1-NO7 gate.

- All seven finite normal-ordering checks pass.
- NO7 includes both Lie-ideal and coideal radical checks, quotient tensor nondegeneracy, and transition preservation.

Gate 6. `W_{\le 3}` witness gate.

- Compact source exhibits the exact target parity dimensions in every row of `W_{\le 3}`.
- In degree `d1+d2+d3`, compact source supplies `29|93` bases, bracket/coproduct coordinates, pairing matrix, radical kernel, quotient map, and PBW comparison.
- Signed dimension `-64` alone fails the gate.

Gate 7. Primitive relations gate.

- Chevalley, Cartan, real Serre, Borcherds orthogonality, super sign, Jacobi, real-string, and isotropic relations pass as matrix equations in the source.
- The `27` mixed maps `[e_k,u_{ij,r}]` are explicit in the first window.

Gate 8. No-extra-relations gate.

- The finite presentation map `pi_nu` is materialized.
- `ker pi_nu = (J_BK + Rad_GN)_{\le W_nu}` is checked at each finite window.
- PBW associated-graded source/target comparison is an isomorphism.

Gate 9. Hopf radical and PBW completion gate.

- Positive-negative pairings have explicit kernels.
- Kernels are closed under brackets and coideals for coproducts.
- Transition maps preserve kernels.
- Exact triangular completion and `lim^1=0` are checked on finite slices.

Gate 10. Orientation and Pfaffian gate.

- Orientation gerbes, quotient obstruction classes, finite-stabilizer classes, null-trivializations, Weyl lifts, and type-II Pfaffian wall local models are materialized.
- The Hall orientation character is computed from this data, not inferred from Maass character or OP scalar square.

Gate 11. Hybrid local/wrapped gate.

- Projection-finite and wrapped sectors are both present.
- Rigidified wrapped anchors exist.
- LL, LW, WL, WW operation tables exist.
- The eight word identities pass.
- Source coalgebra is built from the hybrid source, not from the target bar-cobar counit.

Gate 12. Source-to-target realization gate.

- The geometric realization functor or compact comparison maps are materialized.
- They preserve degrees, products, coproducts, primitives, orientation-gerbe twists, hybrid operations, source coalgebras, Dirac blocks, Pfaffian lines, leading cusp trivialization, and transitions.
- Only after this gate may a K3 x E compact primitive-recognition claim ship.

## 7. Comparison summary

`compute/verify_lattice.py` and `compute/verify_square_root.py` are good target-side regression checks.  They are not finite-source certificate verifiers.  Their own headers say so.

`main.tex` is currently stronger than the scripts: it names the exact finite data and open obligations.  The latest PDF is stronger than `main.tex`: it proposes replacing certificate-first architecture with a constructed universal finite source, then treating K3 x E as a realization problem into that source.

The next correct engineering step is not another prose theorem.  It is a machine-readable finite-source artifact plus verifiers.  Until then, every primitive-recognition theorem must remain certificate/conditional/open.
