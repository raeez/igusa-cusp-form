# Agent 25 Finite Source Data Schema Report

Scope: turn the compact-source and NO1--NO7 obligations into an executable finite-data schema plan.  Sources mined: the April 29 attack transcript, `main.tex`, `compute/verify_square_root.py`, `compute/verify_lattice.py`, and the prior attack reports, especially Agent 06, 08, 12, 16, and 17.

Status: no compact finite source data exists in the repository.  The current scripts verify target-side Borcherds/Gritsenko--Nikulin arithmetic and lattice conventions.  They do not verify a compact Hall source, a chain-level normal-ordering package, a Hopf radical, PBW compatibility, orientation/cyclic lifts, or HN transition compatibility.

The schema below is the minimum finite-data interface that would make those claims executable.  A target-only fixture may be useful for regression tests, but it must never be accepted as a compact-source certificate.

Anchors:

- Primitive recognition was attacked as tautological at `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:448-485`.
- Chain-level normal ordering and NO1--NO7 are demanded at `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:11811-11893` and expanded into source-built checks at `:14556-14696`.
- Construction algorithms for normal-ordered source, finite stages, orientation-gerbe twist, hybrid source, source coalgebra, and Dirac object appear at `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:19893-20318`.
- Current finite normal-ordering diagrams are in `main.tex:9132-9319`.
- The finite \(D_0\)-certificate and finite source kernel are in `main.tex:9973-10590` and `main.tex:10994-11174`.
- Primitive recognition clauses are in `main.tex:12124-12429`, finite-window clauses in `main.tex:12479-12588`, and the first \(W_{\le 3}\) protocol in `main.tex:12941-13274`.

## Required data objects

The source certificate must be finite at each HN stage \(R\).  Every datum below is part of the certificate, not prose attached to it.

| object | required content | proof obligation served |
|---|---|---|
| `manifest` | schema version, coefficient ring, stage IDs, window IDs, exact source anchors, generator ordering, SHA-256 hashes of every matrix file, and script version | prevents silent drift between manuscript, data, and checks |
| `root_lattice` | basis \(\delta_1,\delta_2,\delta_3\); Gram matrix \(2\) on diagonal, \(-2\) off diagonal; map \(\gamma(c_1,c_2,c_3)=(c_1,c_1+c_2-c_3,c_2)\); Weyl vector and real-string exponent rule | target root arithmetic and Serre exponents |
| `gram_charge_lattice` | \(\Gamma_X^{form}\), \(\Gamma_{gram}\), \(\Pi_X(Q,P)\), \(B(c,c')\), \(\widehat\Gamma_X\), \(\star\), \(\overline\Pi_X(c,T)=\Pi_X(c)-T\), finite flag word labels | normal-ordered degree law; NO1 finite fibres |
| `target_window` | target roots, parity dimensions, target generators, target relation templates, target bracket templates, target coproduct templates | reference object for \(W_{\le 3}\), PBW, and no-extra-relations |
| `hn_stage` | \(R\), successor/predecessor IDs, finite charge set \(F_{\sigma,S}(R)\), finite HN words, \(\widehat\Gamma_R\), \(\Gamma_R^\Pi\), \(\Gamma_R^{test}\), finite fibre lists for \(\overline\Pi_X\) | finite-first condition and NO1 |
| `source_spaces` | homogeneous bases for \(P^X_{R,\beta,\bar p}\), \(P^X_{R,-\beta,\bar p}\), Cartan, state object, observable shadow, Dirac complex, and source coalgebra pieces | primitive representatives and full parity dimensions |
| `source_provenance` | for every basis vector: stack/stratum ID, orientation-gerbe component, vanishing-cycle coefficient, compact-support convention, protected integration map, and HN word label | blocks fabricated target bases from posing as compact source |
| `representatives` | source linear combinations for \(e_i^X,f_i^X,h_i^X,E_{ij}^X,u_{ij,r}^{\pm,X},T_a^X,M_{ij,r}^X,w_s^{\pm,X}\) where applicable | primitive recognition R1--R3 |
| `product_matrices` | \(M_{\alpha,\beta}\colon P_\alpha\otimes P_\beta\to P_{\alpha+\beta}\), before quotient, for every retained ordered pair | NO2, NO6, NO7, Hall source kernel |
| `bracket_matrices` | \(B_{\alpha,\beta}\colon P_\alpha\otimes P_\beta\to P_{\alpha+\beta}\), with supercommutator sign convention recorded | relations, Jacobi, primitive recognition |
| `coproduct_matrices` | \(D_{\rho}^{\mu,\nu}\colon P_\rho\to P_\mu\otimes P_\nu\), before quotient, for every retained decomposition | NO2, NO7 coideal |
| `pairing_matrices` | positive-negative Hopf pairings \(G_{\beta,\bar p}\), parity blocks, quotient pairings, Frobenius trace form | NO6, NO7, radical quotient |
| `radicals` | kernel bases \(K_{\beta,\bar p}\), splittings \(P=K\oplus L\), quotient maps \(Q_{\beta,\bar p}=[0\ I]\), transition images of kernels | Hopf radical ideal/coideal and closedness |
| `relations` | finite matrices/vectors for Chevalley, Cartan, real Serre, isotropic orthogonality, super sign, Jacobi, real-string, and \(T_1+T_2+T_3=0\) checks | primitive recognition R2 and no-extra-relations |
| `free_lie_presentation` | finite Hall/Lyndon word basis, Borcherds--Kac relation matrix, target radical matrix, source presentation map \(\pi_W\), kernel basis | no-extra-relations theorem |
| `pbw` | PBW monomial ordering, filtration degrees, associated-graded bases, source/target comparison matrices, strict transition maps | PBW compatibility and exact completion |
| `normal_ordering_cochains` | \(\Theta_{\Pi,R}^{phys}\), \(\widehat\Theta_{\Pi,R}\), \(B_{ch,R}\), degree-shift translations, Hochschild differential matrices | NO3 Hochschild |
| `negative_cyclic` | chain complexes, \(b\), \(B_C\), \(u\)-truncation convention, \(\Theta^-_{\Pi,R}\), \(B^-_{ch,R}\), null-homotopy data | NO3/NO6 cyclic lift |
| `flag_coherences` | two-step and colored flag stacks or their finite pull-push matrices, associators, \(\vartheta\)-transports, pentagon residuals | NO4 |
| `orientation` | \(\operatorname{Or}_{R,\hat c}\), tautological square-root lines, \(\alpha^{red}\), \(\alpha^{E,free}\), \(\widetilde\beta^{E,N}\), \(\lambda^{E,N}\), null-trivializations, Weyl cocycle \(c_o\), torsor defects \(\omega_{i,C}\), O2 local wall data | orientation/Pfaffian and cyclic compatibility |
| `transitions` | matrices \(\rho^H,\rho^F,\rho^K,\rho^P,\rho^{Pf}\), source coalgebra transitions, PBW filtration transitions, cochain transitions, and target truncation maps | finite HN inverse system, [ML], exact completion |

Adversarial rule: if a datum can be filled from `compute/verify_square_root.py` alone, it is target data.  It cannot satisfy a compact-source field unless it carries source provenance and source operation matrices.

## Suggested file/schema layout under `compute/` or `data/`

Do not put source certificate data inside `main.tex`.  It must be machine-readable and checkable.

```text
data/finite_source/v1/
  manifest.json
  lattices/
    root_lattice.json
    gram_charge_lattice.json
  targets/
    gn_wle3_target.json
    gn_wle3_brackets.json
    gn_wle3_pbw.json
  stages/
    R000/
      stage.json
      hnewords.jsonl
      fibres_over_pi.jsonl
      spaces.csv
      bases/
        P_pos.csv
        P_neg.csv
        Cartan.csv
      representatives/
        simple_roots.csv
        isotropic_roots.csv
        timelike_delta123.csv
      pairings/
        G__*.mtx
        quotient_pairing__*.mtx
      radicals/
        K__*.mtx
        Q__*.mtx
        splitting__*.json
      operations/
        products/M__*.mtx
        brackets/B__*.mtx
        coproducts/D__*.mtx
      relations/
        chevalley.jsonl
        serre.jsonl
        orthogonality.jsonl
        jacobi.jsonl
        real_string.jsonl
      pbw/
        word_basis.csv
        relation_matrix.mtx
        source_presentation.mtx
        kernel_expected.mtx
        gr_source.mtx
        gr_target.mtx
        gr_comparison.mtx
      no/
        theta_phys.json
        theta_hat.json
        hochschild_differentials/
        negative_cyclic/
        flag_pentagons/
        jacobi/
        frobenius/
      orientation/
        gerbes.jsonl
        quotient_classes.jsonl
        finite_stabilizers.jsonl
        null_trivializations.jsonl
        weyl_lifts.json
        pfaffian_walls.jsonl
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
      pbw_filtration_maps/
      cochain_maps/
      transition_residuals.json
```

```text
compute/finite_source/
  schema.py
  exact_linalg.py
  root_window.py
  tensor_basis.py
  free_lie.py
  pbw.py
  verify_schema.py
  verify_target_wle3.py
  verify_no1_finite_fibres.py
  verify_no2_operations_transitions.py
  verify_no3_cochains.py
  verify_no4_flag_pentagon.py
  verify_no5_jacobi.py
  verify_no6_frobenius.py
  verify_no7_hopf_radical.py
  verify_primitive_recognition.py
  verify_pbw_no_extra.py
  verify_orientation_cyclic.py
  verify_transitions_ml.py
  verify_all.py
```

Format choices:

- Use JSON/JSONL for finite sets, root IDs, stage metadata, and relation specifications.
- Use Matrix Market `.mtx` or compressed sparse coordinate JSON for matrices.  Every matrix file must be exact rational or integer.  Floats are forbidden.
- Use CSV only for flat basis tables.  Basis tables are metadata, not arithmetic.
- Every file must declare `schema_version`, `coefficient_ring`, `domain_basis`, `codomain_basis`, and `source_kind` where applicable.

Required `source_kind` values:

- `target_reference`: imported GN/Kac/automorphic target data.
- `mock_source_fixture`: fake finite source used only to test scripts.
- `compact_source_candidate`: actual claimed source certificate.  Verification scripts must reject this value unless source provenance fields are populated.

## Matrix conventions

All conventions must be fixed once in `manifest.json`.

1. Coefficient ring: default `QQ`.  Integers are allowed as a subring.  No floating-point matrices.

2. Vector convention: column vectors.  A matrix \(A\colon V\to W\) has shape `dim(W) x dim(V)` and acts by `w = A v`.

3. Tensor basis: lexicographic product.  If `basis(V)=[v_i]` and `basis(W)=[w_j]`, then `basis(V tensor W)` is `(v_0 tensor w_0), (v_0 tensor w_1), ..., (v_1 tensor w_0), ...`.

4. Root IDs: use tuples and stable labels.

```json
{"id":"d1","coeffs":[1,0,0],"gamma":[1,1,0],"height":1}
{"id":"a12","coeffs":[1,1,0],"gamma":[1,2,1],"height":2}
{"id":"tau","coeffs":[1,1,1],"gamma":[1,1,1],"height":3}
{"id":"neg_tau","coeffs":[-1,-1,-1],"gamma":[-1,-1,-1],"height":-3}
```

5. Parity blocks: store even and odd spaces separately.  A matrix with mixed parity domain/codomain must be decomposed into parity blocks unless it is explicitly an odd operator.

6. Pairing matrices: \(G_{\beta,\bar p}\) pairs \(P_{\beta,\bar p}\) against \(P_{-\beta,\bar p}\).  Rows are the positive basis; columns are the negative basis.  The transpose block \(G_{-\beta,\bar p}\) is stored independently if the source convention is not symmetric.

7. Radical convention:

\[
K_{\beta,\bar p}=\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t}.
\]

The `K__beta__p.mtx` matrix has columns equal to a basis of \(K_{\beta,\bar p}\) in source coordinates.  If a splitting \(P=K\oplus L\) is chosen, source coordinates are ordered as `K` then `L`, and

\[
Q_{\beta,\bar p}=[0\ I]
\]

has shape `dim(L) x dim(P)`.

8. Product matrices: \(M_{\alpha,\beta}\) has rows indexed by `basis(P_{alpha+beta})` and columns indexed by `basis(P_alpha tensor P_beta)`.

9. Coproduct matrices: \(D_{\rho}^{\mu,\nu}\) has rows indexed by `basis(P_mu tensor P_nu)` and columns indexed by `basis(P_rho)`.

10. Bracket convention:

\[
[x,y]_\Theta=M_{\alpha,\beta}(x\otimes y)
-(-1)^{|x||y|}M_{\beta,\alpha}(y\otimes x).
\]

If bracket matrices are supplied directly, the verifier still recomputes this equation when product matrices are present.  A mismatch is fatal unless the manifest explicitly chooses bracket-as-primary and product-as-absent.

11. Transition matrices: \(\rho^P_{R^+R,\beta}\) maps the larger-stage basis to the smaller-stage basis.  Shape is `dim(P_R,beta) x dim(P_Rplus,beta)`.  Kernel preservation means every column of \(\rho^P K_{R^+,\beta}\) lies in the span of \(K_{R,\beta}\).

12. PBW ordering: choose shortlex on generator IDs, with the order recorded in `pbw/generator_order.csv`.  The first \(W_{\le 3}\) fixture should use:

```text
Cartan: h1 < h2 < h3
positive: e1 < e2 < e3 < E12 < E13 < E23 < u12_01 < ... < u23_09 < w001 < ... < w093
negative: f1 < f2 < f3 < F12 < F13 < F23 < u12m_01 < ... < wminus093
```

The precise order is conventional.  It is not allowed to vary between PBW, relation, and no-extra-relations checks.

13. Matrix orientation for relations: a relation matrix \(R_W\) has columns equal to free presentation words and rows equal to source quotient basis coordinates.  The relation holds when \(R_W v=0\) after applying \(Q\) and the presentation map.

## Verification scripts to add

### `verify_schema.py`

Checks file presence, schema version, exact rationals, root IDs, basis uniqueness, matrix shapes, tensor-basis declarations, source-kind values, and manifest hashes.

Failure mode caught: a target table posing as a source certificate.

### `verify_target_wle3.py`

Builds the target \(W_{\le 3}\) table from `compute/verify_square_root.py` and `compute/verify_lattice.py`, then compares `data/finite_source/v1/targets/gn_wle3_target.json`.

Checks:

- \(\delta_i:1|0\).
- \(a_{ij}:10|0\).
- \(2\delta_i+\delta_j:1|0\), \(i\ne j\).
- \(\tau=\delta_1+\delta_2+\delta_3:29|93\).
- root strings: real-real exponent \(3\), complementary real-isotropic exponent \(5\), real-timelike exponent \(3\).

This script verifies only the target reference.

### `verify_no1_finite_fibres.py`

Checks finite fibres of

\[
(\overline\Pi_{R,*}^{\Theta}V_R)_\gamma
=
\prod_{\overline\Pi_X(c,T)=\gamma}(V_R)_{(c,T)}
\]

and the successor square

\[
\rho^\Pi_{R^+R}\overline\Pi_{R^+,*}^{\Theta_{R^+}}
=
\overline\Pi_{R,*}^{\Theta_R}\rho_{R^+R}.
\]

Inputs: `stage.json`, `fibres_over_pi.jsonl`, transition maps.

### `verify_no2_operations_transitions.py`

Checks product, coproduct, and pairing transition squares:

\[
\rho m_{R^+}=m_R(\rho\otimes\rho),
\qquad
(\rho\otimes\rho)\Delta_{R^+}=\Delta_R\rho,
\]

\[
\langle\rho x,\rho y\rangle_R=\langle x,y\rangle_{R^+}.
\]

All equations are matrix equations in exact arithmetic.

### `verify_no3_cochains.py`

Checks that the domain has not been mixed:

- physical-charge version:

\[
d_{\mathrm{Hoch}}\Theta_{\Pi,R}^{phys}=B_{ch,R};
\]

- normal-ordered-label version:

\[
\widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)},\qquad
d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0.
\]

The script rejects a file that quantifies over \((c,T)\in\widehat\Gamma_R\) while using the physical equation \(d\Theta=B_{ch}\).

It also checks the negative-cyclic equation if the required matrices are supplied:

\[
(b+uB_C)\Theta^-_{\Pi,R}=B^-_{ch,R}.
\]

### `verify_no4_flag_pentagon.py`

For every retained two-step Hall flag, checks

\[
(\mathsf A_{a,b,c}\circ(\vartheta_{a,b}\otimes1)\circ\vartheta_{a+b,c})
-
((1\otimes\vartheta_{b,c})\circ\vartheta_{a,b+c})=0.
\]

The degree identity for \(B\) is a necessary precheck.  It is not accepted as the chain proof.

### `verify_no5_jacobi.py`

Checks the transported super-Jacobi identity for every homogeneous triple whose total degree remains in the retained finite window:

\[
(-1)^{|x||z|}[x,[y,z]]
+(-1)^{|y||x|}[y,[z,x]]
+(-1)^{|z||y|}[z,[x,y]]=0.
\]

This runs on source bracket matrices before quotient and again after quotient when \(Q\)-maps are supplied.

### `verify_no6_frobenius.py`

Checks

\[
\langle[x,y]_\Theta,z\rangle_R
+(-1)^{|x||y|}\langle y,[x,z]_\Theta\rangle_R=0
\]

for all retained triples with degrees summing to zero.  It also verifies Hopf adjointness of product and coproduct:

\[
\langle M_{\alpha,\beta}(x\otimes y),z\rangle_R
=
\langle x\otimes y,D^{\alpha,\beta}_{\alpha+\beta}z\rangle_R.
\]

### `verify_no7_hopf_radical.py`

Computes \(K_{\beta,\bar p}\), compares it with supplied radical bases, and checks:

\[
Q_{\alpha+\beta}B_{\alpha,\beta}(P_\alpha\otimes K_\beta)=0,
\]

\[
Q_{\alpha+\beta}B_{\alpha,\beta}(K_\alpha\otimes P_\beta)=0,
\]

\[
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_{\rho}K_\rho=0.
\]

It also checks quotient-tensor nondegeneracy and transition preservation

\[
\rho^P_{R^+R}(K_{R^+,\beta})\subset K_{R,\beta}.
\]

This is the decisive script.  Matching the quotient bracket table while failing the \(QD(K)=0\) coideal check is a fatal failure.

### `verify_primitive_recognition.py`

Implements finite-window R1--R8:

1. representatives and parities;
2. relation checks;
3. full parity dimensions;
4. Hopf pairing and radical;
5. no-extra-relations kernel equality;
6. generation;
7. PBW associated-graded compatibility;
8. exact triangular completion metadata.

It must reject target-only fixtures and any source fixture without positive and negative halves.

### `verify_pbw_no_extra.py`

Builds the finite free Lie/presentation words in the retained window, applies the Borcherds--Kac relation matrix and radical matrix, and checks

\[
\ker\pi_W=
\bigl(\overline{J_{BK}+\operatorname{Rad}_{GN}}\bigr)_W.
\]

It then checks

\[
\operatorname{gr}_{PBW}U(P_X^{\Pi,red})_{\le W}
\cong
\operatorname{gr}_{PBW}U(\mathfrak g_{\Delta_5})_{\le W}
\]

with strict transition maps.

This script can start with \(W_{\le 3}\), but it must be written for arbitrary downward-saturated windows.

### `verify_orientation_cyclic.py`

Checks the finite orientation/cyclic package:

- connected \(BE\) class fields use \(H^2(BE;\mathbb F_2)\), not \(H^1(BE;\mathbb F_2)\);
- finite \(E[N]\) classes are Borel classes \(\widetilde\beta^{E,N}\) until mixed terms and spectral sequence differentials are killed;
- \(E[2]\) degree-two bits \(r_i\) are separate from degree-one characters \(\rho_i\);
- for even \(N\ge4\), the mixed \(x_1x_2\) term is not inferred from cyclic restrictions;
- Weyl lift cocycle \(c_o\) is killed by a recorded \(1\)-cochain;
- O2 local wall data record \(u_\delta\), tangent/normal splitting, invariant Pfaffian unit, and \(N_\delta^{Pf}\);
- negative-cyclic \(\Theta^-_{\Pi,R}\) is compatible with the orientation data.

This script does not prove the compact orientation exists.  It verifies that supplied finite orientation data are internally coherent.

### `verify_transitions_ml.py`

Checks finite transition systems:

- stable images for each fixed finite window;
- strict PBW filtration preservation;
- closed radical subsystem;
- exact passage through kernels, cokernels, radicals, PBW gradeds, and parity pieces;
- composite compatibility for non-successor maps.

The script should print whether each finite window is strictly surjective, ML by stable image, or failed.

### `verify_all.py`

Runs the checks in dependency order:

1. schema;
2. target reference;
3. finite fibres;
4. operation transitions;
5. cochains;
6. flag pentagon;
7. Jacobi;
8. Frobenius;
9. Hopf radical;
10. PBW/no-extra-relations;
11. primitive recognition;
12. orientation/cyclic;
13. ML transitions.

Any compact-source theorem should cite this command with a data directory:

```bash
python3 compute/finite_source/verify_all.py data/finite_source/v1/stages/R000 --window W_le3
```

## Minimal `W_{\le 3}` fixture

The first fixture should be `target_reference`, not `compact_source_candidate`.

File: `data/finite_source/v1/targets/gn_wle3_target.json`.

Positive roots:

```text
d1   = (1,0,0), gamma=(1,1,0), dim=1|0
d2   = (0,1,0), gamma=(0,1,1), dim=1|0
d3   = (0,0,1), gamma=(0,-1,0), dim=1|0
a12  = (1,1,0), gamma=(1,2,1), dim=10|0
a13  = (1,0,1), gamma=(1,0,0), dim=10|0
a23  = (0,1,1), gamma=(0,0,1), dim=10|0
d112 = (2,1,0), gamma=(2,3,1), dim=1|0
d122 = (1,2,0), gamma=(1,3,2), dim=1|0
d113 = (2,0,1), gamma=(2,1,0), dim=1|0
d133 = (1,0,2), gamma=(1,-1,0), dim=1|0
d223 = (0,2,1), gamma=(0,1,2), dim=1|0
d233 = (0,1,2), gamma=(0,-1,1), dim=1|0
tau  = (1,1,1), gamma=(1,1,1), dim=29|93
```

Mirror all nonzero roots with negative IDs, and include a three-dimensional even Cartan.

Target bases:

```text
d_i: e_i
-d_i: f_i
Cartan: h_i
a_ij: E_ij, u_ij_01, ..., u_ij_09
d_i+a_ij: Y_i_ij
tau even: T1, T2, M12_01..M12_09, M13_01..M13_09, M23_01..M23_09
tau odd: w_001..w_093
```

Relations and bracket templates in the target fixture:

- \(E_{ij}=[e_i,e_j]\), \(E_{ji}=-E_{ij}\).
- \([e_i,u_{ij,r}]=[e_j,u_{ij,r}]=0\).
- If \(\{i,j,k\}=\{1,2,3\}\), then \([e_k,u_{ij,r}]=M_{ij,r}\).
- \(T_1=[e_1,E_{23}]\), \(T_2=[e_2,E_{31}]\), \(T_3=[e_3,E_{12}]=-T_1-T_2\).
- Odd \(\tau\)-basis vectors \(w_s\) are simple generators; no bracket produces them in \(W_{\le 3}\).
- Positive-negative target pairing may be identity against dual bases for the target fixture; radical is zero.

The corresponding `mock_source_fixture` may copy this target algebra only to test scripts.  It must carry:

```json
{
  "source_kind": "mock_source_fixture",
  "not_a_compact_source": true,
  "reject_for_manuscript_theorem": true
}
```

A real compact-source fixture must replace the target basis labels by source basis labels and provenance:

```json
{
  "basis_id": "src_tau_even_001",
  "root": "tau",
  "parity": 0,
  "stage": "R000",
  "source_stack": "M_R000_<charge>",
  "orientation_component": "Or_R000_<charge>",
  "vanishing_cycle_complex": "Phi_R000_<charge>",
  "protected_integration_map": "I_R000_prot",
  "normal_ordered_label": {"charge": "...", "T": [0,0,0]},
  "maps_to_target_basis": {"T1": "1"}
}
```

Minimal \(W_{\le 3}\) source-mode pass criteria:

1. Source has compact provenance for all \(P_{\beta,\bar p}\) in \(W_{\le 3}\cup(-W_{\le 3})\cup\{0\}\).
2. Quotient dimensions match \(1|0\), \(10|0\), \(1|0\), \(29|93\).
3. Bracket matrices reproduce the displayed target templates after \(Q\).
4. Pairing matrices produce radical kernels and quotient maps.
5. \(QB(P\otimes K)=0\), \(QB(K\otimes P)=0\), and \(QD(K)=0\).
6. \(\ker\pi_{W_{\le3}}\) equals the finite Borcherds--Kac plus GN radical kernel.
7. PBW associated graded agrees on the truncated enveloping span.
8. All matrices are preserved by successor maps when a successor is supplied.

## Nonnegotiable proof obligations

1. Finite source first.  The source data must be supplied on finite HN stages before any inverse limit or completion.

2. Source provenance.  Every compact-source basis vector must point to a source object/stratum, coefficient complex, orientation gerbe component, and protected integration map.

3. Target arithmetic is not source geometry.  The scripts now in `compute/` can populate target reference files only.

4. Full parity dimensions.  Signed dimension \(f(nm,l)\) is not enough.  The first timelike channel requires compact \(29|93\) bases, not just \(-64\).

5. Positive and negative halves.  Primitive recognition and Hopf pairing require \(W\cup(-W)\cup\{0\}\).  Cusp-positive data alone cannot verify the radical quotient.

6. Relations as matrices.  Chevalley, Serre, orthogonality, Jacobi, real-string, and super sign relations must be checked as finite matrix equations.

7. Hopf radical is ideal and coideal.  Rank equality or quotient bracket equality is insufficient.

8. No-extra-relations is a kernel equality.  It cannot be replaced by equal dimensions or determinant agreement.

9. PBW is associated-graded and transition-strict.  Target PBW does not transfer to the source without source PBW bases and comparison matrices.

10. Normal ordering is chain-level.  The lattice identity for \(\overline\Pi_X\) is necessary.  It does not supply \(\Theta_{\Pi,R}\) on correspondence targets, cyclic lifts, Frobenius trace, or radical compatibility.

11. Orientation is not scalar normalization.  The constants \(64\), \(4096\), OP signs, and Maass character values do not construct a compact orientation gerbe, finite-stabilizer descent, or Pfaffian wall chart.

12. Transitions are data.  `R+ -> R` compatibility must be checked by matrices.  Non-successor maps must be composites or satisfy a recorded cocycle identity.

13. No hidden infinity.  Any object called finite must have finite fibres, finite protected cohomology, finite matrix files, and finite tensor products in the retained window.

14. No floats.  Floating-point rank, kernel, or determinant checks are invalid for this proof.

## What current scripts already cover

`compute/verify_lattice.py` covers:

- Pfaffian Gram matrix in the \(f_1,f_2,f_3,f_{-2},f_{-1}\) basis.
- Type-II simple-root Gram matrix
  \[
  \begin{pmatrix}
  2&-2&-2\\
  -2&2&-2\\
  -2&-2&2
  \end{pmatrix}.
  \]
- Weyl vector \(\rho=(1,-1/2,1)\).
- Reflection length preservation.
- Sample \(\alpha(n,l,m)\) and exponential dictionary checks.

It does not cover source charge support, source primitive bases, Hall products, coproducts, Hopf pairings, radicals, PBW, orientations, or transitions.

`compute/verify_square_root.py` covers:

- \(\phi_{0,1}\) theta-series coefficients through the hard-coded range.
- \(\prod(1-q^k)^9\) through \(q^9\).
- Borcherds product coefficient extraction after the leading monomial.
- \([qrs]D_5/(qrs)^{1/2}=93\).
- First timelike target presentation split \(29|93\).
- \(m(\delta_1+\delta_2+\delta_3)=-93\).
- Height-four additive checks \(90,90,90,-540\).
- Height-four signed/additive/gap checks \(108|90|18\).
- Doubled isotropic signed/simple/gap checks \(10|9|1\).
- Real-string pairing and exponent checks.

It does not cover compact representatives, source parity bases, bracket constants, pairing matrices, coproduct matrices, radical kernels, quotient maps, no-extra-relations, PBW, orientation gerbes, negative-cyclic lifts, or HN transitions.

Agent 12 correctly states the computational boundary: target arithmetic is in good condition; executable source-side certification is absent.

## Patch queue for manuscript references to executable checks

No `main.tex` edits are made here.  When the schema and scripts exist, patch the manuscript as follows.

1. Near `main.tex:9132-9319`, add a sentence after the NO1--NO7 proposition:

```tex
For the finite matrix form used in computations, see
\texttt{compute/finite_source/verify_no1_finite_fibres.py} through
\texttt{verify_no7_hopf_radical.py}; these scripts require the finite
source data schema of \texttt{data/finite_source/v1}.
```

2. Near `main.tex:9236-9301`, reference `verify_no7_hopf_radical.py` explicitly.  This is the matrix theorem, not a target arithmetic check.

3. Near `main.tex:9973-10590`, point the finite \(D_0\)-certificate clauses to `data/finite_source/v1/stages/R*/stage.json`, `hnewords.jsonl`, and transition maps.

4. Near `main.tex:10994-11174`, point the finite Hall source kernel definition to `source_spaces`, `product_matrices`, `coproduct_matrices`, `pairing_matrices`, and `normal_ordering_cochains`.

5. Near `main.tex:12124-12429`, point primitive recognition to `verify_primitive_recognition.py`, `verify_pbw_no_extra.py`, and `verify_no7_hopf_radical.py`.

6. Near `main.tex:12479-12588`, add that a global recognition proof is executable only through a cofinal sequence of data directories, one per downward-saturated window.

7. Near `main.tex:12633-12939`, cite `compute/verify_square_root.py` only for target arithmetic: low-degree rows, first timelike coefficient, \(29|93\), and string exponents.

8. Near `main.tex:12941-13274`, cite both:

- `verify_target_wle3.py` for the GN/Kac target fixture;
- `verify_primitive_recognition.py --window W_le3` for any claimed compact source.

Do not let the first citation substitute for the second.

9. Near `main.tex:13276-13414`, add a compact-source data gap sentence:

```tex
At present no data directory in \texttt{data/finite_source/} supplies the
compact-source matrices required by this open problem.
```

10. Near the orientation/Pfaffian clauses, point cyclic and orientation checks to `verify_orientation_cyclic.py`, but state that the script verifies supplied finite data and does not construct them.

11. Near every scalar OP/DT square reference, do not cite finite-source scripts.  The scalar branch is orientation-forgetful and source-free.

## Residual open data

The following are still open after the present target arithmetic checks.

1. Finite \(K3\times E\) semistable substacks at bounded HN height, including base Picard/Bun control.

2. Finite d-critical/cosection Hall atlas: object stacks, extension stacks, two-step flag stacks, finite residual inertia, BBDJS coefficients, semiregularity cosections, and admissible pull-push maps.

3. Actual finite Hall source kernels \(\mathfrak S_R\) for any \(R\).

4. Source primitive bases in \(W_{\le 3}\cup(-W_{\le 3})\cup\{0\}\), beginning with compact \(29|93\) in \(\delta_{123}\).

5. Hall product, bracket, coproduct, and pairing matrices on those bases.

6. Radical kernels, quotient maps, and proof that radicals are Lie ideals and coideals.

7. Finite no-extra-relations kernel equality.

8. PBW associated-graded comparison and strict transition maps.

9. Chain-level \(\Theta_{\Pi,R}\) on actual correspondence targets, not just the lattice translation formula.

10. Negative-cyclic lift \(\Theta^-_{\Pi,R}\) and \(S^1\)-equivariant orientation compatibility.

11. Two-step and colored flag coherence matrices.

12. Frobenius/CY3 trace pairing for the protected Hall bracket.

13. Orientation-gerbe-twisted Hall object: gerbes, tautological lines, lifted correspondences, anti-invariant twisted state spaces, and quotient-stack integration.

14. Finite \(E[N]\)-stabilizer obstruction classes and zero linearization characters for every stabilizer that actually appears.

15. Weyl determinant-line lifts, cocycle \(c_o\), torsor defects \(\omega_{i,C}\), and O2 local Pfaffian wall charts.

16. Hybrid local/wrapped source: wrapped anchors, LL/LW/WL/WW correspondences, eight two-step flag types, quotient-after-correspondence functor, and protected integration.

17. Source chiral Koszul coalgebra \(C_{X,R}\), collision coproduct, conilpotent filtration, bar comparison, cobar quasi-isomorphism, and Koszul ML exactness.

18. HN transition matrices for every source object, operation, radical, PBW filtration, orientation datum, cyclic cochain, and Pfaffian line.

19. ML stable-image certificates on each finite window.

20. A rule for promoting `mock_source_fixture` to `compact_source_candidate`: this must require source provenance, compact-support formalism, orientation data, operation matrices, radical/PBW checks, and transition checks.  Without that rule, the executable framework would certify its own target copy and repeat the tautology attacked on April 29.

Bottom line: the next executable milestone is not another coefficient script.  It is a `W_{\le 3}` finite-source fixture with real source bases, product/bracket/coproduct/pairing matrices, radical kernels, quotient maps, PBW data, and transition maps.  Until that exists, the compact realization remains a precisely stated open problem.
