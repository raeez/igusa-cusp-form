# Agent 30 Row Companion Atlas Report

Scope: plan for moving the eight Clery--Gritsenko diagonal-divisor row
material out of the main paper into a companion/independent atlas.

Sources mined:

- `main.tex:169-171`, `194-210`, `339-355`, `390-450`,
  `14014-14264`, `14267-14552`, `14689-16081`.
- `appendices/boundary_compatibility_conditions.tex:1-121`.
- `materials/raw/2026-04-29-attack-whitepaper-analysis.pdf`, checked
  through `pdftotext`; processed extraction at
  `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:774-806`,
  `5689-5707`, `7827-7870`, `8552-8554`, `9236-9240`,
  `13041-13048`.
- Row reports:
  `notes/attack_whitepaper_analysis_20260429/agent09_eight_rows_boundary_report.md`,
  `agent10_manuscript_architecture_report.md`,
  `agent11_primary_source_verification_report.md`,
  `agent20_bibliography_primary_sources_report.md`,
  `agent21_appendix_quarantine_compression_report.md`,
  `agent22_local_patch_proposals_report.md`,
  `agent23_theorem_status_taxonomy_report.md`.
- Prior row source material:
  `agent_material/12_eight_rows_hosts_F1_F4_attack_heal.tex`,
  `agent_material/12_eight_rows_hosts_F5_F8_attack_heal.tex`,
  `agent_material/10_boundary_row_physical_hosts.tex`,
  `agent_material/13_eight_row_certificate_attack_repair.tex`.

Verdict: move the detailed row material to a companion atlas if the main
paper is meant to be the `N=1` Dirac--Igusa theorem paper.  The row
material is valuable as an audit ledger.  It is poison if it reads as a
dependency of the `N=1` theorem or as a physical-host catalogue.

## Companion Atlas Purpose

The companion atlas should be an independent audit document:

1. It fixes the eight diagonal-divisor automorphic rows of
   Clery--Gritsenko.
2. It records product data, denominator data, scalar-square data, and
   physical-host certificates as separate levels.
3. It prevents false row maps from CHL notation, comparison-symbol
   notation, scalar squares, or shared weights.
4. It records exactly what is sourced from Clery--Gritsenko,
   Gritsenko--Nikulin, Cheng--Dabholkar, Govindarajan, and
   Govindarajan--Gopala Krishna.
5. It keeps the main paper focused on the `N=1` determinant,
   denominator target, normal-ordered charge repair, OP/DT scalar square,
   and compact realization problem.

Working title:

`Diagonal-Divisor Row Atlas: Automorphic Products, Denominator Rows, and
Physical-Host Certificates`

The title must not contain `CHL boundary physics` unless a physical host
is actually constructed.  The atlas is an automorphic/denominator ledger,
not a compact Hall or CY/DT construction.

## Main-Paper Residue

Leave at most a one-page independence ledger in `main.tex`.

Required residue:

1. One abstract sentence replacing the current row close at
   `main.tex:169-171`:
   `The diagonal-divisor row atlas is independent extension data; it is
   not used in the N=1 determinant, denominator, normal-ordering, OP/DT
   scalar-square, or compact-realization arguments.`

2. Remove the row from the dependency chain at `main.tex:194-210`, or
   change the last line to an independent side branch:
   `Clery--Gritsenko rows -> independent certificate ledger for future
   boundary hosts.`

3. Keep a compact status paragraph near `main.tex:339-355`:
   the eight rows are
   `Delta_5, Delta_2, Delta_1, Delta_{1/2}, nabla_3, nabla_2,
   nabla_{3/2}, Q_1`; rows `1--4` have Gritsenko--Nikulin denominator
   data; rows `5--8` have Govindarajan CHL/WKB denominator data; `F_7`
   lives on the `mu_4` multiplier cover; physical row maps require the
   five-level certificate.

4. Keep one small table with columns:
   `row`, `automorphic product`, `denominator source`,
   `scalar source`, `physical host status`.
   No product formulae, no cusp tables, no fractional-root discussion.

5. Keep the strict exclusion:
   `No row data below is used in the proof of the N=1 theorem.`

6. Keep the `N=1` boundary compatibility appendix, because it is scoped
   correctly.  Its current exclusions at
   `appendices/boundary_compatibility_conditions.tex:84-88` and
   `114-121` should remain in the main paper even if the atlas moves out.

7. Remove row extension from the final theorem closure at
   `main.tex:14014-14264`.  The final synthesis may point to the companion
   atlas, but the rows must not sit in the theorem spine.

Main-paper residue table:

| Row | Form | Product | Denominator | Scalar | Physical host |
|---:|---|---|---|---|---|
| 1 | `Delta_5` | CG + Borcherds/GN product | GN `g_{Delta_5}`, `64^{-1}Delta_5(2Z)` | OP/DT `-4096 Delta_5^{-2}` | compact Hall/chiral host open |
| 2 | `Delta_2` | CG/GNII product | GNII row `g_2^{GN}` | none certified | none certified |
| 3 | `Delta_1` | CG/GNII product | GNII row `g_3^{GN}` | none certified | none certified |
| 4 | `Delta_{1/2}` | CG/GNII product on cover | GNII row `g_4^{GN}` on cover | none certified | none certified |
| 5 | `nabla_3` | CG product | Govindarajan `G_1(2)` | CHL scalar square only | none certified |
| 6 | `nabla_2` | CG product | Govindarajan `G_1(3)` | CHL scalar square only | none certified |
| 7 | `nabla_{3/2}` | CG product on order-four multiplier cover | Govindarajan `G_1(4)` on `mu_4` cover | `F_7^2=Phi_3` only | none certified |
| 8 | `Q_1` | CG `(t,N)=(2,2)` product | Govindarajan `G_2(4)` | CHL scalar square only | none certified |

## Companion Outline

### 1. Purpose and Independence

State the independence theorem:

`The atlas is independent of the N=1 Dirac--Igusa theorem package.  It
records row certificates and forbidden inferences.  It constructs no
compact Hall source, no CY/DT host beyond the row-1 OP/DT scalar branch,
and no physical comparison row.`

Use the attack PDF warning explicitly as architecture, not as authority:
the row ledger is useful but row-map danger is high
(`materials/processed/...txt:774-806`, `5689-5707`, `7827-7870`).

### 2. Row Order, Groups, Characters, Divisors

Move and clean `main.tex:14689-14739`.

Content:

- Clery--Gritsenko source order:
  `Delta_5, Delta_2, nabla_3, Delta_1, nabla_2, Delta_{1/2},
  nabla_{3/2}, Q_1`.
- Present order:
  `Delta_5, Delta_2, Delta_1, Delta_{1/2}, nabla_3, nabla_2,
  nabla_{3/2}, Q_1`.
- Exact `(t,N)`, group, weight, character/multiplier, divisor
  multiplicity-one row.
- Warning that plus-groups used by Gritsenko--Nikulin for `t=2,3,4` are
  denominator normalizations, not always the source-group labels in the
  CG table.

### 3. Five-Level Certificate Formalism

Move `main.tex:14289-14337`.

Use the five independent entries:

- `A_j`: automorphic product certificate.
- `D_j`: Weyl--Kac--Borcherds denominator certificate.
- `S_j`: CHL/dyon scalar-square certificate.
- `Z_j`: reduced CY/DT scalar-host certificate.
- `H_j`: compact Hall/chiral primitive-bracket certificate.

Add a theorem-level firewall:

`No entry implies another unless a cited theorem constructs the
implication.`

### 4. Rows 1--4: Full-Paramodular Denominator Rows

Move `main.tex:14796-15096`, plus the safe row-1 normalization from
`main.tex:14796-14824`.

Content:

- `D_5=64^{-1}Delta_5`.
- `den(g_{Delta_5})=D_5(2Z)=64^{-1}Delta_5(2Z)`.
- For rows `2,3,4`, use `M_t=U(4t)+<2>`,
  `e_t^{(n,l,m)}=q^n r^l s^{tm}`, and
  `rho_t=(1/(2t),1/2,1/(2t))`.
- Product formulae for `Delta_2`, `Delta_1`, `Delta_{1/2}`.
- Simple real roots:
  `P_2`, `P_3`, `P_4` exactly as in `main.tex:14930-14943`.
- Denominator theorem with `C'_j=1`, `a_j=1` in `e_t` normalization.
- Source check: GNII equations `(2.21)`, `(2.20)`, `(2.11)`, Lemma 2.5,
  Section 5.1.1.

### 5. Rows 5--8: Clery--Gritsenko Congruence Products

Move `main.tex:15098-15321`.

Content:

- Jacobi seeds:
  `4(xi_{1,0}^{(2)})^2`,
  `3 xi_{3,1}^{(6)} xi_{3,5}^{(6)}`,
  `2 xi_{2,1}^{(4)} xi_{2,3}^{(4)}`,
  `2 xi_{1,0}^{(2)}(tau,2z)`.
- Multi-cusp product formulae for `F_5,F_6,F_7,F_8`.
- Cusp sets:
  `K_5=K_6=K_8={infty,S}`, `K_7={infty,M,S}`.
- Degree maps:
  `alpha_5(infty)=alpha_1(n,l,m)`,
  `alpha_5(S)=alpha_1(2n,2l,2m)`;
  `alpha_6(S)=alpha_1(3n,3l,3m)`;
  `alpha_7(M)=alpha_1(2n,2l,2m)`,
  `alpha_7(S)=alpha_1(4n,4l,4m)`;
  `alpha_8(infty)=alpha_2(n,l,m)`,
  `alpha_8(S)=alpha_2(2n,2l,2m)`.
- Product prefactors:
  `rho_5=rho_6=rho_7=alpha_1(1/2,1/2,1/2)`,
  `rho_8=alpha_2(1/4,1/2,1/4)`.
- `F_7` half exponent:
  `tilde c_{7,M}=c_{7,M}/2`, integral only in the sourced `mu_4`
  multiplier-cover product datum.

### 6. Rows 5--8: Govindarajan CHL/WKB Denominator Data

Move `main.tex:15470-15839`.

Content:

- `nabla_3 <-> G_1(2)`.
- `nabla_2 <-> G_1(3)`.
- `nabla_{3/2} <-> G_1(4)` on the `mu_4` cover.
- `Q_1 <-> G_2(4)`.
- For rows `5,6,7`: `L=M_1`, `P=P^{(1)}`,
  `rho=alpha_1(1/2,1/2,1/2)`, `epsilon=det`.
- For row `8`: `L=M_2`, `P=P^{(2)}`,
  `rho=alpha_2(1/4,1/2,1/4)`, `epsilon=det`.
- Chambers:
  `M_1={v>=0, v<=2w, v<=2u}`;
  `M_2={v>=0, v<=4w, 3v<=4(u+w), v<=4u}`.
- Cartan matrices `A^{(1)}` and `A^{(2)}` from `main.tex:15522-15540`.
- Imaginary coefficient conventions:
  `N_5,N_6` divisor sums; `N_7` theta-product coefficient extraction;
  `N_8` `Q_1` coefficient extraction.
- Explicit statement: these are denominator rows, not compact physical
  row maps.

### 7. Scalar Squares and Why They Do Not Promote

Move `main.tex:14505-14531`, `15582-15598`.

Content:

- `nabla_3^2=Phi_6^{(1,2)}`.
- `nabla_2^2=Phi_4^{(1,3)}`.
- `F_7^2=Phi_3` in the fixed composite `N=4` branch.
- `Q_1^2=Phi_2^{(2,4)}`.
- These fill only `S_j`.
- They do not carry denominator sign, parity, Weyl chamber, Weyl
  alternating side, reduced obstruction theory, or compact Hall source.

### 8. Formal Product/Current Rows

Move `main.tex:15323-15404`, but rename it.

Safe title:

`Formal product-current shadows`

Forbidden title:

`Physical current rows`

Content:

- For rows `5--8`, the abelian product current envelope realizes signed
  product exponents only.
- For rows `2--4`, current envelopes can be made from the imported GN
  BKM algebras.
- For row `1`, the current envelope is the target-side
  `g_{Delta_5}` current.
- None is a compact Hall/factorization source.

### 9. Comparison Symbols and Fractional-Root No-Go

Move or compress `main.tex:15893-16055`.

In the companion atlas, keep the full forbidden-identification analysis.
In the main paper, keep at most a box.

Essential claims:

- CG present-order weights:
  `(5,2,1,1/2,3,2,3/2,1)`.
- Comparison tuple:
  `(5,2,1,1,1/2,1,1/4,0)` is not the CG table.
- `Phi^{cmp}_5=F_5`, `Phi^{cmp}_7=F_7`, `Phi^{cmp}_8=F_8` are false by
  weight.
- A formal branch is not a modular form until parent, cover, cocycle,
  character root, divisor divisibility, and branch are supplied.
- The `mu_4` cover of `F_7` of weight `3/2` is not a certificate for a
  weight `1/4` comparison object.

### 10. Physical-Host Certificate Ledger

Move `main.tex:15866-15891`, plus the refined status material from
`agent_material/10_boundary_row_physical_hosts.tex`.

For every row, require:

- host/background `X_j`;
- physical charge lattice;
- duality group;
- exact automorphic group or cover;
- one-particle protected index;
- reduced obstruction theory when `Z_j` is claimed;
- scalar theorem `Z_j^{red}=C_j F_j^{-2}` when claimed;
- Hall/chiral primitive bracket comparison when `H_j` is claimed;
- orientation/reflection character compatibility.

Current status: only row `1` has a reduced CY/DT scalar-host theorem.
No row has a compact Hall/chiral host in the manuscript.

### 11. Source Audit and Residual Checks

Import the source-status tables from Agent 11 and Agent 20.  The atlas
should carry its own primary-source checklist rather than bury this debt
inside the main paper.

## Required Row Tables

### Table A. Row-Order Crosswalk

Columns:

`source-order index`, `present row j`, `F_j`, `(t,N)`, `group`,
`weight`, `character/multiplier`, `cover note`.

Required entries:

| Source order | Present row | Form | `(t,N)` | Group | Weight | Character/multiplier | Cover note |
|---:|---:|---|---|---|---:|---|---|
| 1 | 1 | `Delta_5` | `(1,1)` | `Gamma_1` | `5` | `v_eta^{12} x v_H` | none beyond Maass character |
| 2 | 2 | `Delta_2` | `(2,1)` | `Gamma_2` / `Gamma_2^+` for denominator | `2` | `v_eta^6 x v_H`, `chi_4` on plus group | denominator normalization |
| 4 | 3 | `Delta_1` | `(3,1)` | `Gamma_3` / `Gamma_3^+` | `1` | `v_eta^4 x v_H`, `chi_6` | denominator normalization |
| 6 | 4 | `Delta_{1/2}` | `(4,1)` | `Gamma_4` / `Gamma_4^+` | `1/2` | `v_eta^3 x v_H`, `v_8` | degree-eight multiplier cover |
| 3 | 5 | `nabla_3` | `(1,2)` | `Gamma_0^{(2)}(2)` | `3` | `chi_2^{(2)} x v_H` | congruence product |
| 5 | 6 | `nabla_2` | `(1,3)` | `Gamma_0^{(2)}(3)` | `2` | `chi_2^{(3)} x v_H` | congruence product |
| 7 | 7 | `nabla_{3/2}` | `(1,4)` | `Gamma_0^{(2)}(4)` | `3/2` | `chi_4^{(4)} x v_H` | denominator only on associated `mu_4` multiplier cover |
| 8 | 8 | `Q_1` | `(2,2)` | `Gamma_2(2)` | `1` | `chi_4^{(2)} x v_H` | special `G_2(4)` row |

### Table B. Automorphic Product Certificate `A_j`

Columns:

`j`, `F_j`, `Jacobi input(s)`, `cusp labels`, `product lattice`,
`prefactor`, `degree maps`, `product source`, `divisor`.

Required entries:

- `F_1`: seed `phi_{0,1}`; product is the Borcherds/GN product;
  `D_5=64^{-1}Delta_5`; denominator uses `2Z`.
- `F_2`: `phi_{0,2}`, `M_2`, `rho=(1/4,1/2,1/4)`,
  `e_2^{(n,l,m)}=q^n r^l s^{2m}`.
- `F_3`: `phi_{0,3}`, `M_3`, `rho=(1/6,1/2,1/6)`.
- `F_4`: `phi_{0,4}`, `M_4`, `rho=(1/8,1/2,1/8)`.
- `F_5`: `4(xi_{1,0}^{(2)})^2`, cusps `{infty,S}`,
  maps `alpha_1(n,l,m)`, `alpha_1(2n,2l,2m)`.
- `F_6`: `3 xi_{3,1}^{(6)} xi_{3,5}^{(6)}`, cusps `{infty,S}`,
  maps `alpha_1(n,l,m)`, `alpha_1(3n,3l,3m)`.
- `F_7`: `2 xi_{2,1}^{(4)} xi_{2,3}^{(4)}`, cusps
  `{infty,M,S}`, maps `alpha_1(n,l,m)`, `alpha_1(2n,2l,2m)`,
  `alpha_1(4n,4l,4m)`, with `c_{7,M}/2` only on the sourced cover.
- `F_8`: `2 xi_{1,0}^{(2)}(tau,2z)`, cusps `{infty,S}`,
  maps `alpha_2(n,l,m)`, `alpha_2(2n,2l,2m)`.

### Table C. Denominator Certificate `D_j`

Columns:

`j`, `denominator source`, `lattice`, `simple real roots`, `Weyl vector`,
`Weyl group/chamber`, `reflection character`, `imaginary coefficient
convention`, `normalization`.

Required entries:

- `F_1`: GN `g_{Delta_5}`, lattice `Lambda^{2,1}_{II}` in the main
  notation, roots `delta_1=2f_2-f_3`,
  `delta_2=2f_{-2}-f_3`, `delta_3=f_3`,
  `rho=f_2-1/2 f_3+f_{-2}`, denominator `64^{-1}Delta_5(2Z)`.
- `F_2`: GNII `M_2`, `P_2={(0,-1,0),(1,1,0),(1,3,1),(0,1,1)}`,
  `rho=(1/4,1/2,1/4)`, `epsilon=det`, `C'=a=1`.
- `F_3`: GNII `M_3`, `P_3={(0,-1,0),(1,1,0),(2,5,1),(2,7,2),
  (1,5,2),(0,1,1)}`, `rho=(1/6,1/2,1/6)`,
  `epsilon=det`, `C'=a=1`.
- `F_4`: GNII `M_4`, `P_4={delta in M_4 | (delta,delta)=2,
  (delta,rho_4)=-1}`, `rho=(1/8,1/2,1/8)`,
  `epsilon=det`, `C'=a=1`.
- `F_5,F_6,F_7`: Govindarajan/CHL `M_1`,
  `P^{(1)}={(0,-1,0),(1,1,0),(0,1,1)}`,
  `rho=alpha_1(1/2,1/2,1/2)`, `epsilon=det`, `C'=a=1`;
  `F_7` only on `mu_4` cover.
- `F_8`: Govindarajan/CHL `M_2`,
  `P^{(2)}={(0,-1,0),(1,1,0),(1,3,1),(0,1,1)}`,
  `rho=alpha_2(1/4,1/2,1/4)`, `epsilon=det`, `C'=a=1`.

### Table D. Five-Level Certificate Status

Columns:

`j`, `A_j automorphic product`, `D_j denominator`, `S_j scalar square`,
`Z_j reduced CY/DT host`, `H_j compact Hall/chiral host`, `row map`.

Required status:

| Row | `A_j` | `D_j` | `S_j` | `Z_j` | `H_j` | Row map |
|---:|---|---|---|---|---|---|
| 1 | filled by CG/Borcherds/GN | filled by GN | Igusa square only, no CHL row map used | filled only for reduced `K3 x E` OP/DT scalar branch | open | no extra boundary row map |
| 2 | filled by CG/GNII | filled by GNII | none certified | none certified | none certified | none certified |
| 3 | filled by CG/GNII | filled by GNII | none certified | none certified | none certified | none certified |
| 4 | filled by CG/GNII on cover | filled by GNII on same cover | none certified | none certified | none certified | none certified |
| 5 | filled by CG | filled by Govindarajan `G_1(2)` | scalar square `nabla_3^2=Phi_6^{(1,2)}` only | none certified | none certified | none certified |
| 6 | filled by CG | filled by Govindarajan `G_1(3)` | scalar square `nabla_2^2=Phi_4^{(1,3)}` only | none certified | none certified | none certified |
| 7 | filled by CG on order-four multiplier cover | filled by Govindarajan `G_1(4)` on `mu_4` cover | `F_7^2=Phi_3` only, branch-sensitive | none certified | none certified | none certified |
| 8 | filled by CG | filled by Govindarajan `G_2(4)` | `Q_1^2=Phi_2^{(2,4)}` only | none certified | none certified | none certified |

### Table E. Banned Identifications

Columns:

`claim`, `status`, `reason`, `source anchor`.

Required rows:

- `Phi^{cmp}_5=F_5`: false by weight.
- `Phi^{cmp}_7=F_7`: false by weight; `F_7` has weight `3/2`, not
  `1/4`.
- `Phi^{cmp}_8=F_8`: false by weight; no CG weight-zero row.
- `Delta_2` same weight as `nabla_2` implies row map: false; groups,
  seeds, product lattices, and sources differ.
- `F_7 mu_4 cover` implies arbitrary modular root: false; root object
  needs parent, cover, cocycle, character root, branch, divisor
  divisibility.
- `CHL scalar square` implies denominator: false; square forgets
  reflection sign and Weyl alternating side.
- `denominator theorem` implies compact physical host: false; no reduced
  obstruction theory or Hall/chiral primitive source is supplied.

## Source/Certificate Statuses

Retain these source claims in the companion atlas, with exact
theorem/equation anchors added before publication.

| Claim | Status | Source role |
|---|---|---|
| CG gives exactly eight genus-two dd-modular rows and excludes the ninth `(2,4;1/2)` candidate | imported; source-sensitive | `GC` Theorem 1.4, Proposition 1.2 |
| CG gives diagonal divisor multiplicity one and product displays for `nabla_3,nabla_2,nabla_{3/2},Q_1` | imported; source-sensitive | `GC` Theorem 3.1 and final Section 3 displays |
| GN/GNII give `D_5=64^{-1}Delta_5` and `den(g_{Delta_5})=64^{-1}Delta_5(2Z)` | imported; high-risk normalization | `GN`, `GNII`; verify `2Z` conversion |
| GNII gives rows `F_2,F_3,F_4` as denominator identities in `e_t` variables | imported; notation-heavy | `GNII` equations `(2.21),(2.20),(2.11)`, Section 5.1.1 |
| CG congruence products alone do not give Weyl chamber, simple roots, reflection character, or Weyl sum | negative source-role claim; safe if phrased as boundary | local logical comparison with `GC` theorem content |
| Govindarajan/CHL gives WKB denominator rows for `F_5--F_8` | imported; fragile | `Gov11BKM` Table 3, Sections 4.2--4.3; `CD09BKM`, `GK09CHL`, `GK10Composite` |
| `F_7` is denominator only on the `mu_4` multiplier cover and has scalar square `F_7^2=Phi_3` | imported; highest-risk row claim | `GC`, `GK10Composite`, `Gov11BKM`; verify cover, branch, theta normalization |
| `Q_1` is special `G_2(4)` and uses `M_2` notation | imported; source-sensitive | `Gov11BKM` Appendices C--D, `CD09BKM` `N=2` data |
| Row `1` has reduced `K3 x E` scalar host `-4096 Delta_5^{-2}` | imported scalar theorem | `OB`, `OPand`, `OberdieckReducedPT`; not a Hall/Pfaffian theorem |
| No row has a compact Hall/chiral host in the current manuscript | local status claim | checked against current `main.tex`; retain as open |

Certificate statuses:

- `A_j`: filled for all eight rows as automorphic product data, subject to
  final source anchoring.
- `D_j`: filled for all eight rows by GN/GNII/Govindarajan, but rows
  `5--8` are filled in CHL/WKB normalization, not by CG product alone.
- `S_j`: filled only where a scalar-square theorem is sourced; it is not
  filled for rows `2--4`; row `1` has OP/DT scalar-square context but no
  CHL row map is used.
- `Z_j`: filled only for row `1`, and only in the reduced
  quotient-by-`E`, Behrend-weighted `K3 x E` scalar branch.
- `H_j`: open for every row.
- `row map`: open or absent for every row except the internal identity of
  the automorphic row with its sourced denominator theorem.  No physical
  row map is constructed.

## Banned Inferences

These must be stated as prohibitions in the atlas and enforced in the
main-paper residue.

1. `CG product => BKM denominator` is banned for rows `5--8`.  The CG
   product gives product, divisor, character, and cusp data.  The BKM
   chamber, simple roots, reflection character, parity, and Weyl-sum side
   come from Govindarajan/CHL, not from CG alone.

2. `CHL scalar square => denominator theorem` is banned.  Squaring erases
   the denominator sign and the anti-invariant Weyl side.

3. `Govindarajan denominator => reduced CY/DT scalar host` is banned.
   A WKB denominator theorem is not a reduced obstruction theory and not a
   compact enumerative partition theorem.

4. `Govindarajan denominator => compact Hall/chiral host` is banned.
   No protected one-particle state space, orientation package, primitive
   bracket, radical quotient, or Hall/factorization source is constructed.

5. `OP/DT row-1 scalar square => first-order Pfaffian or orientation`
   is banned.  OP/DT sees `D_5^2`, not the Dirac square root or Hall
   orientation character.

6. `64`, `4096`, or the OP minus sign => orientation monodromy is banned.
   They are scalar normalizations.

7. `formal product current envelope => compact source` is banned.  For
   rows `5--8` the current object built from product exponents is abelian
   and non-unique.

8. `product exponents mu_j => imaginary simple-root coefficients N_j(a)`
   is banned.  Product-side exponents and additive-side imaginary
   corrections are different data.

9. `same weight => same row` is banned.  `Delta_2` and `nabla_2` both
   have weight `2` but are different rows with different groups, seeds,
   product data, and denominator sources.

10. `F_7 mu_4 cover => arbitrary fractional comparison row` is banned.
    `F_7` has weight `3/2`; a weight `1/4` comparison object needs its
    own parent, cover, cocycle, character-root computation, branch, and
    source theorem.

11. `Phi^{cmp}_5=F_5`, `Phi^{cmp}_7=F_7`,
    `Phi^{cmp}_8=F_8` are banned.  They are false by the displayed
    weights.

12. `boundary row` may not mean `physical boundary host`.  Use
    `row`, `denominator row`, `scalar square`, or `host certificate`
    according to the filled level.

## Move Map From Current Anchors

| Current anchor | Current content | Companion destination | Main-paper residue |
|---|---|---|---|
| `main.tex:169-171` | abstract row close | Companion purpose if expanded | one sentence: row atlas independent |
| `main.tex:194-210` | dependency chain includes rows | Companion not needed | remove row as dependency or mark side branch |
| `main.tex:339-355` | intro eight-row certificate paragraph | Companion certificate summary | compressed paragraph plus one table |
| `main.tex:382-385`, `446-450` | status table row line | Companion status matrix | one row: certificate/open |
| `main.tex:14014-14028` | synthesis arrow includes row extension | Companion introduction | delete from main theorem spine |
| `main.tex:14195-14200` | final row certificate condition | Companion purpose/certificate formalism | short cross-reference only |
| `main.tex:14267-14278` | row part title and opening | Companion Section 1 | if retained, rename to independent ledger |
| `main.tex:14289-14337` | five-level physical-host certificate | Companion Section 3 | small definition summary only |
| `main.tex:14339-14369` | CG theorem and row table | Companion Table A | optional compressed residue table |
| `main.tex:14374-14444` | five-level row status table | Companion Table D | one-page residue table, not full prose |
| `main.tex:14446-14459` | source-role distinction rows `2--8` | Companion source-status section | one negative sentence |
| `main.tex:14461-14503` | extension separation and open certificates | Companion certificate formalism | keep one sentence: no row used in `N=1` proof |
| `main.tex:14505-14531` | CHL squares vs denominator signs | Companion scalar-square section | optional one-line warning |
| `main.tex:14534-14552` | comparison tuple warning | Companion forbidden-identifications section | delete or box |
| `main.tex:14689-14739` | row order and characters | Companion Table A | not in main |
| `main.tex:14740-14766` | candidate denominator datum | Companion Section 3 | not in main |
| `main.tex:14768-14824` | `M_t` and normalization | Companion normalization appendix | not in main except `D_5(2Z)` |
| `main.tex:14841-15096` | rows `F_2--F_4` GN data | Companion Section 4 | not in main |
| `main.tex:15098-15321` | rows `F_5--F_8` CG products | Companion Section 5 | not in main |
| `main.tex:15323-15404` | formal product/current rows | Companion Section 8, renamed | not in main |
| `main.tex:15406-15468` | nonabelian promotion test | Companion firewall theorem | not in main |
| `main.tex:15470-15839` | Govindarajan denominator rows | Companion Section 6 | not in main |
| `main.tex:15841-15864` | row data remark | Companion status section | not in main |
| `main.tex:15866-15891` | physical-host open problem | Companion host-certificate section | one line: all `H_j` open |
| `main.tex:15893-16055` | comparison-row/fractional-root tests | Companion Section 9 | forbidden-identifications box at most |
| `main.tex:16057-16080` | final `N=1` boundary comparison paragraph | Main one-page residue seed | keep compressed in main |
| `appendices/boundary_compatibility_conditions.tex:1-121` | `N=1` boundary compatibility | Keep as main appendix or duplicate as atlas appendix | retain exclusions at lines `84-88`, `114-121` |

## Patch Queue

If the split is approved, patch in this order.

1. Create a companion TeX or Markdown source for the atlas.  Do not make
   it an appendix hidden behind the main theorem.  The filename should not
   imply a draft version.  Candidate path:
   `notes/diagonal_divisor_row_atlas.md` for internal planning, or a
   dedicated `row-atlas/main.tex` if it is to be typeset.

2. Copy the detailed row material from `main.tex:14267-14552` and
   `14689-16081` into the companion.  Preserve labels only after renaming
   them so they cannot collide with the main paper.

3. Replace `main.tex:14267-14552` with the one-page independence ledger
   described above, or remove the part entirely and cite the companion in
   one paragraph.

4. Remove row extension from the final synthesis theorem around
   `main.tex:14014-14264`.  The final theorem may say that row extension
   is outside the theorem closure.

5. Move `\input{appendices/boundary_compatibility_conditions}` so it is
   part of the main `N=1` boundary appendix, not nested after the row
   atlas.  Keep its exclusions intact.

6. Rename every occurrence of `Diagonal-divisor rows and CHL boundary
   physics` to `Independent diagonal-divisor denominator row ledger` or
   remove the title with the section.

7. Deduplicate row tables.  The main paper gets one small residue table.
   The companion gets the complete tables A--E.

8. Rename `prop:eight-formal-current-rows` / `thm:eight-formal-current-rows`
   in the companion to avoid theorem-style leakage.  Use a status-bearing
   name such as `formal-product-current-shadow`.

9. In the companion, add a `Source role` paragraph before every theorem:
   `imported product`, `imported denominator`, `scalar square`, `formal
   target`, `open host`.

10. For `F_7`, add a special boxed statement:
    order-four CG multiplier; denominator theorem only after pullback to
    the associated `mu_4` multiplier cover; `F_7^2=Phi_3` is scalar in a
    fixed composite `N=4` branch; no comparison row or physical host
    follows.

11. Add exact theorem/equation anchors before publishing the companion.
    Do not rely on local row tables as primary-source substitutes.

12. Run post-patch greps:
    - `rg -n "CHL boundary physics" main.tex appendices`
    - `rg -n "Phi\\^\\{\\\\mathrm\\{cmp\\}\\}_[578].*=F_[578]" main.tex appendices`
    - `rg -n "physical host|compact Hall|CY/DT" main.tex appendices`
    - `rg -n "4096.*orientation|orientation.*4096|64.*orientation|orientation.*64" main.tex appendices`
    - `rg -n "eight-formal-current-rows|prop:no-unbuilt-denominator" main.tex appendices`

13. Build only after the integration owner has moved the material.  This
    report-only task should not touch `main.tex`.

## Residual Source Checks

Before either the main residue or companion atlas is publication-grade,
these checks remain.

1. `GC`:
   verify Proposition 1.2, Theorem 1.4, Theorem 3.1, row order, weights,
   groups, characters, multiplier orders, diagonal divisor multiplicity
   one, and the final Section 3 products for
   `nabla_3,nabla_2,nabla_{3/2},Q_1`.

2. `GN` and `GNII`:
   verify `D_5=64^{-1}Delta_5`, the `2Z` denominator normalization,
   `M_t=U(4t)+<2>`, `e_t^{(n,l,m)}=q^n r^l s^{tm}`, GNII product
   equations `(2.21),(2.20),(2.11)`, Lemma 2.5, Section 5.1.1, and the
   `t=4` parabolic equality case.

3. `Gov11BKM`:
   verify Table 3 mapping
   `nabla_3 -> G_1(2)`,
   `nabla_2 -> G_1(3)`,
   `nabla_{3/2} -> G_1(4)`,
   `Q_1 -> G_2(4)`;
   verify Sections 4.2--4.3 for integrality, real roots, Weyl sign, and
   WKB denominator formula; verify Appendices C--D for `Q_1`.

4. `CD09BKM`, `GK09CHL`, `GK10Composite`:
   verify the CHL real-root systems, Cartan matrices, scalar square
   identities, `nabla_3`/`nabla_2` divisor sums, `F_7` theta product and
   branch, and sign convention `m_j(a)=-N_j(a)` where the manuscript uses
   plus-sign Weyl sums.

5. `F_7` cover:
   independently check the order-four multiplier, the associated `mu_4`
   cover, what becomes single-valued, why the middle-cusp exponent
   `c_{7,M}/2` is integral in the sourced cover normalization, and the
   exact scalar square `F_7^2=Phi_3`.

6. `Q_1`:
   verify the theta characteristic formula, the `Z'=(tau,2z;2z,4sigma)`
   convention, the four first monomials
   `r^{-1}, q r, r s^2, q r^3 s^2`, and the translation to `P^{(2)}`.

7. OP/Oberdieck:
   verify that row `1` is the only filled reduced CY/DT scalar host:
   `K3 x E`, primitive nonzero K3 class, quotient-by-`E`,
   Behrend-weighted reduced branch, variables, and constant
   `-4096`.

8. Fractional comparison:
   if retained, verify the Weil/Shimura metaplectic background and the
   elementary character-order statement for fourth roots of exact
   order-four characters.  Keep Borcea--Voisin and higher-dimensional
   curve-counting sources as possible future sources only, not evidence.

9. Bibliography hygiene:
   add exact page/theorem/equation anchors to row claims.  Agent 20
   already identifies row source anchors as `proj.bib:158-227` for
   CG/Govindarajan/CHL and `proj.bib:100-134` for GN/GNII.

10. Independence check:
    after the split, no statement in the `N=1` main theorem should depend
    on rows `F_2--F_8`, comparison symbols, fractional roots, or
    Govindarajan/CHL data.

