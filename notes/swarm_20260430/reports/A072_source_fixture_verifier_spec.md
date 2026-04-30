# A072 - Source Fixture Verifier Specification

Proposal only. No files edited by the agent.

Target checks passed via `compute/verify_lattice.py` and
`compute/verify_square_root.py`: Gram matrix, `29|93`, height-four
`108|90|18`, doubled isotropic `10|9|1`, Serre exponents `3,5`.

## Scope

Verifier name: `verify_source_fixture` in specification only.

Windows:

```tex
W_{\le3}=\{\sum c_i\delta_i:c_i\ge0,\ 1\le\sum c_i\le3\}.
```

`S_W=W\cup(-W)\cup\{0\}`. For `W_le7`, use the downward-saturated
height window through `ht <= 7`, with all relation outputs for real
Serre, doubled isotropic rows, `\tau`-real strings, and complementary
strings `a_{ij}+s\delta_k`, `0 <= s <= 5`. Any target parity data in
height `4..7` must come from a target fixture, not from signed
coefficients.

Primary anchors: `main.tex` near lines 15268, 15373, 15004, 12714, and
12743.

## Inputs

Use A067 packet exactly:

`manifest.yaml`, `degrees.csv`, `basis_provenance.csv`, `pairs.csv`,
`decompositions.csv`, `matrix_index.csv`, sparse `M,D,B,G,K,Q,A,T` entry
files, `relation_rows.csv`, `pbw.csv`, `no_extra.csv`,
`transitions.csv`, `ml_stable_images.csv`, `orientation_protected.csv`.

Required additions for `W_le7`: `target_degrees.csv`,
`target_basis.csv`, `target_relation_rows.csv`, `target_pbw.csv`, and
explicit `coverage_scope=certified|deferred|target_only`. `W_le3` must
mark height-four and height-seven terminal rows as deferred. `W_le7`
must certify them.

All scalar entries must be exact: integers, rationals, or declared
number-field elements. Floats fail.

## Sign Conventions

All matrices act on column coordinates. The flip
`\tau(x\otimes y)=y\otimes x` is ordinary. The super sign is only

```tex
B_{\alpha,\beta}
 =
M_{\alpha,\beta}
-(-1)^{|x||y|}M_{\beta,\alpha}\tau .
```

Thus even-even brackets are antisymmetric; odd-odd brackets are
symmetric in the super sense. Target sign checks include
`E_{31}=-E_{13}` and `T_3=-T_1-T_2` from `main.tex` near line 15060.

## Verifier Gates

1. Schema/firewall gate.
   Source basis ids must be neutral `b^X_{R,\beta,\bar p,a}`. Target
   names `e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s` are forbidden outside
   `target_basis.csv` and `A_entries.csv`. This enforces
   AP-CY384/AP-CY419.

2. Window gate.
   Check downward saturation. Check positive, negative, and zero
   degrees. For `W_le3`, exact target dimensions are

```tex
\delta_i:1|0,\quad a_{ij}:10|0,\quad
2\delta_i+\delta_j:1|0,\quad \tau:29|93 .
```

3. Radical gate.
   For each parity block,

```tex
K_{\beta,\bar p}
=\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^t .
```

Check by exact rank:

```tex
G_\beta K_\beta=0,\quad G_{-\beta}^tK_\beta=0,\quad
\rank K_\beta
  =\nullity\begin{bmatrix}G_\beta\\G_{-\beta}^t\end{bmatrix}.
```

Check `P=K\oplus L`, `QK=0`, `Q|_L=I`, and nondegeneracy of the
restricted quotient pairing.

4. NO7 gate.
   For every retained pair/decomposition:

```tex
Q_{\alpha+\beta}B_{\alpha,\beta}(P_\alpha\otimes K_\beta)=0,
```

```tex
Q_{\alpha+\beta}B_{\alpha,\beta}(K_\alpha\otimes P_\beta)=0,
```

```tex
(Q_\mu\otimes Q_\nu)D^{\mu,\nu}_\rho K_\rho=0,
```

and Hopf adjointness

```tex
M_{\alpha,\beta}^tG_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D^{\alpha,\beta}_{\alpha+\beta}.
```

5. Relation gate.
   Check Chevalley rows for all retained simple fibres, including the
   `9` isotropic copies and `93` odd `\tau` copies; adjacent isotropic
   orthogonality; Jacobi `T_1^X+T_2^X+T_3^X=0`; the `27` mixed maps;
   real Serre exponent `3`; complementary exponent `5`. `W_le3` defers
   terminal rows outside the window. `W_le7` must certify them.

6. Comparison gate.
   Each `A_{\beta,\bar p}:L_{\beta,\bar p}\to
   \mathfrak g_{\Delta_5,\beta,\bar p}` is parity-preserving, full-rank,
   and satisfies bracket, coproduct, and pairing intertwining as near
   `main.tex` line 14037.

7. No-extra gate from A063.
   Compute the finite presentation map `pi_W` from source brackets. Let
   `N=ker(pi_W)` and `S=[BK_relation_span GN_radical_span]`. Pass iff

```tex
\pi_W S=0,\quad \rank N=\rank S=\rank[N\ S].
```

This is separate from NO7.

8. PBW gate from A064.
   Compare associated gradeds, not only Hilbert series:

```tex
H_X=\prod_{\beta\in W}
(1-tx^\beta)^{-\dim L_{\beta,\bar0}}
(1+ztx^\beta)^{\dim L_{\beta,\bar1}}.
```

For every recorded `(d,\bar p,\eta)`, require equal source/target
dimensions and exact full-rank `gr_map_matrix_id`. For `W_le3`, required
target ranks include `\tau`: `d=1:29|93`, `d=2:30|0`, `d=3:1|0`.

9. Transition/ML gate.
   Check cocycles, preservation of `M,D,B,G,K,Q,A`, PBW strictness

```tex
T^U(F^dU')=T^U(U')\cap F^dU,
```

and stable-image ranks

```tex
\rank M_{\mu\nu}=\rank M_{\mu_0\nu}
=\rank[M_{\mu\nu}\ M_{\mu_0\nu}].
```

## Expected Failures

Current repo should fail with `MISSING_SOURCE_FIXTURE`. A target-only
packet fails `SOURCE_TARGET_FIREWALL`, `MISSING_MDGKQA`, `NO_NO_EXTRA`,
and `NO_PBW`. Signed-dimension-only evidence fails AP-CY416. Radical
descent without no-extra/PBW fails AP-CY418. `W_le3` claiming
height-four or height-seven terminal certification fails. `W_le7`
deferring those rows fails.

## Output

Emit `verifier.json` and `verifier-summary.tex` with per-gate
`PASS|FAIL|DEFERRED`, exact ranks, matrix hashes, command line, and
certificate id. `main.tex` should cite it only on `PASS`, for example
after `main.tex` line 15360:

```tex
The finite source datum for \(W_{\le3}\) is the certificate
\(\mathcal C_{\le3}(R)\); the exact verifier output
\texttt{certificates/wle3/<id>/verifier.json} records PASS for NO7,
no-extra-relations, PBW, and strict ML transition gates.
```

Until then, cite failures only as obstruction evidence, not as proof.

