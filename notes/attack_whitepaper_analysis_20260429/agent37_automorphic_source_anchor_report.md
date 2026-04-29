# Agent 37 Automorphic Source Anchor Report

Date: 2026-04-29

Scope: primary-source/theorem-anchor audit for the automorphic core only:
Borcherds, Gritsenko--Nikulin 1997 (`GN`), Gritsenko--Nikulin Part II
(`GNII`), Maass/Igusa, Eichler--Zagier, and the normalization chain
`D_5`, `Delta_5`, `2Z`, and type-II roots.

Inputs mined: `main.tex`, `proj.bib`,
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt`,
`agent03_borcherds_gn_report.md`,
`agent11_primary_source_verification_report.md`,
`agent20_bibliography_primary_sources_report.md`, and
`agent28_formal_pfaffian_normalization_report.md`. I also checked the
primary arXiv/PDF source pages for `GN`, `GNII`, Borcherds 1995, and
Igusa 1964(II). I did not edit `main.tex`, `proj.bib`, appendices, or
existing source.

## Automorphic theorem ledger

| Claim | Current manuscript anchors | Exact source anchor | What may be cited | Downgrade / firewall |
|---|---:|---|---|---|
| General Borcherds automorphic product mechanism. | `main.tex:2538-2540`, `14826-14830`. | Borcherds, *Automorphic forms on Os+2,2(R) and infinite products*, Invent. Math. 120 (1995), Theorem 10.1, PDF pp. 28-29: product `e^{-2 pi i(rho,v)} prod(1-e^{-2 pi i(r,v)})^{c(...)}` and weight `c(0)/2`. | General automorphic-product architecture, weight mechanism, divisor/meromorphy framework. | Do not cite Borcherds 10.1 for `64`, `D_5`, `Delta_5`, the genus-two variables, Maass character, or `2Z`. Those are GN/GNII specialization data. |
| Weak Jacobi input `phi_{0,1}` and first coefficients. | `main.tex:722-740`, `2601-2618`, `1991`. | GN p. 17 around Theorem 4.1 gives `phi_{0,1}=phi_{12,1}/Delta_{12}`, support `n>=0`, `4n-l^2>=-1`, and expansion `(r^{-1}+10+r)+q(10r^{-2}-64r^{-1}+108-64r+10r^2)+...`; GNII Example 2.4, equation (2.15), p. 34, repeats the expansion and cites EZ §9. | `f(0,0)=10`, `f(0, +/-1)=1`, support of the `q^0` row, and the coefficient normalization used by the GN lift. | Direct `EZ:1` page/section still needs checking. Until then, cite GN/GNII for the exact coefficients and cite EZ only as their background source. Do not cite EZ/DMVV as constructing a canonical half-Hilbert space. |
| Monic Borcherds product. | `main.tex:1946-1958`, `2530-2558`, `14796-14839`. | GN Theorem 4.1, arXiv PDF p. 17: `1/64 Delta_5(Z)=exp(pi i(z1+z2+z3)) prod_{(n,l,m)>0}(1-exp(2 pi i(nz1+lz2+mz3)))^{f(nm,l)}`; GNII Theorem 2.1, equation (2.3), pp. 29-30, and Example 2.4, (2.15)--(2.16), p. 34. | The product cone, variables, exponent `f(nm,l)`, leading monomial, and the identity `D_5=64^{-1}Delta_5`. | GNII writes the monic product as `Delta_5`. The manuscript uses `Delta_5` for the theta-normalized section and `D_5` for the monic product. Every citation must say which convention is active. |
| Igusa theta-constant normalization and leading coefficient. | `main.tex:2383-2424`, `2560-2599`. | GN §1, equations (1.1)--(1.8): ring statement, product of ten even theta constants, Maass multiplier, Fourier expansion, `f(1,1,1)=64`, and `64 | f(n,l,m)`. Igusa 1964(II) PDF, Theorem 1, p. 397, proves normality of theta-constant rings; Igusa 1962 metadata confirms AJM 84 (1962), pp. 175--200, DOI 10.2307/2372812. | For the paper now, cite GN (1.1)--(1.8) for the theta-product and `64`; cite Igusa/Freitag/van der Geer for the classical structure theorem only after exact page anchors are inserted. | Do not use Igusa as the only support for `[q^{1/2}r^{1/2}s^{1/2}]Delta_5=64` until the exact Igusa/Freitag/van der Geer page is checked. GN gives the needed coefficient directly. |
| Maass character and six reflection signs. | `main.tex:1887-2008`, `2383-2416`, `5185-5338`. | GN (1.3)--(1.5), p. 6, records Maass's multiplier formula; GN Proposition 2.1, p. 7, gives `-1` on `2f_2-f_3`, `2f_{-2}-f_3`, `f_3`, and `+1` on `f_{-2}-f_2`, `f_2-f_3`, `f_2+f_3`; GN Proposition 2.2, p. 9, gives the type-I/type-II chamber restrictions. | Automorphic character values of `nu_{Delta_5}` on the target Weyl/chamber generators. | Direct Maass 1964, pp. 125--135, has not been checked. If `MAASS:1` is retained as an independent citation, add exact page/formula anchors. Maass character is not a Hall orientation character. |
| Type-II lattice, roots, chamber, Weyl vector. | `main.tex:5161-5355`, `5545-5550`. | GN p. 7 fixes `M_0 = Z f_2 + Z f_3 + Z f_{-2} ~= U + <2>` and the reflection formula; GN p. 9 gives subgroup indices, chamber wall sets, `P(M_II)={delta_1,delta_2,delta_3}`; GN equations (2.1)--(2.3), pp. 9-10, give the Gram matrix and Weyl-vector equations. GNII §5.1.1, case `(t,II,0)`, p. 61, gives `rho_{t,II,0}=(1/(2t),1/2,1/(2t))` and `P_{1,II,0}={(0,-1,0),(1,1,0),(0,1,1)}`. | Root set `delta_1=2f_2-f_3`, `delta_2=2f_{-2}-f_3`, `delta_3=f_3`, Gram matrix, chamber, and `rho=(delta_1+delta_2+delta_3)/2`. | The coordinate dictionaries must be stated: under `alpha(n,l,m)=2n f_2-l f_3+2m f_{-2}`, GNII `(0,-1,0)`, `(1,1,0)`, `(0,1,1)` map to `delta_3`, `delta_1`, `delta_2`. |
| Weyl-sum/additive correction and imaginary simple roots. | `main.tex:2024-2042`, `5460-5542`. | GN Theorem 2.3 is announced in the introduction p. 2; proof on pp. 10-11 gives `m(a)=-(1/64)c_Delta(n,l,m)`, `m(0)=-1`, and the isotropic identity with `tau(ta_0)=9`. GN p. 11 reduces isotropic rays to `2f_2`, `2f_{-2}`, `2f_2-2f_3+2f_{-2}` by `S_3` symmetry. | Additive-side imaginary simple-root coefficients `m(a)` and isotropic `tau(a)`, separate from product exponents. | The arXiv text has an evident typo in the displayed `a` formula, writing the last term as `(m-1)f_2`; context and manuscript use `(m-1)f_{-2}`. Check the published AJM version before final theorem lock. |
| Denominator algebra identity and the `2Z` normalization. | `main.tex:2590-2591`, `5614-5702`, `13543-13563`, `14796-14839`. | GN §3 formula (3.2), p. 13, states the Weyl--Kac denominator product with `exp(-2 pi i(...))`; GN Proposition 3.1, p. 13, states `(1/64)Delta_5(2Z)=Phi(z)`; GN Remark 3.2 explains the coefficient `2` in this equality. | `den(g_{Delta_5})=D_5(2Z)=64^{-1}Delta_5(2Z)` and visible positive signed multiplicities after comparing with the product. | Never write `den=D_5(Z)` or `den=Delta_5(Z)`. The `2Z` is a source theorem plus the exponential-character conversion, not a cosmetic variable choice. |
| Visible root supermultiplicities. | `main.tex:5642-5700`, `13565-13601`. | GN (3.4), p. 13, says for `alpha=2n f_2-l f_3+2m f_{-2}`, `mult alpha=f(nm,l)`, after Theorem 4.1 supplies the product. | On active positive support, product exponents are signed root superdimensions of the imported GN denominator algebra. | Product exponents do not determine even/odd dimensions separately, zero-superdimension root spaces, brackets, PBW, primitive representatives, or compact Hall source data. |
| Full-paramodular GNII rows `F_2,F_3,F_4`. | `main.tex:14796-15095`. | GNII Theorem 2.1, (2.3), p. 29; formulas `(2.21)`, `(2.20)`, `(2.11)`; Lemma 2.5; §5.1.1 pp. 55 and 61; formula `(5.1)` for Lie-type denominator identities. | The separate `e_t^{(n,l,m)}=q^n r^l s^{tm}` normalization for rows `Delta_2`, `Delta_1`, `Delta_{1/2}`. | Do not import the main `N=1` doubled `2Z` convention into rows 2--4. They use the GNII `e_t` product normalization directly. |
| Clery--Gritsenko/Govindarajan rows. | `main.tex:14339-15839`. | Outside this automorphic-core pass. Agent20 flagged exact row/table/theorem debt. | At most source-role boundary: CG gives products/divisors, Govindarajan/CHL gives denominator data in CHL normalization. | Downgrade all row-map, cover, and denominator claims until their own primary-source row audit is done. |

## Exact source-anchor needs

1. `main.tex:722-740`: replace the bare "Eichler--Zagier normalization" support with a two-source anchor:
   `GNII Example 2.4, (2.15)` for the displayed `phi_{0,1}` expansion and `EZ:1 §9` only after the exact book page is checked. The K3 statement `Z_K3=2 phi_{0,1}` also needs a source-role line: arithmetic normalization, not a half-Hilbert construction.

2. `main.tex:1946-1955`: the citation should be
   `GNII Theorem 2.1, (2.1)--(2.3), Example 2.4, (2.15)--(2.16); GN Theorem 4.1`.
   Also fix or define `Gamma_eff^+`; Agent03 found the undefined occurrence at `main.tex:1954`. The source cone is exactly the standard `(n,l,m)>0` order.

3. `main.tex:2383-2424`: split the source roles:
   `Igusa1962/Igusa1964II/Freitag/van der Geer` for the classical ring/theta-constant background;
   `GN (1.1)--(1.8)` for the exact facts actually used here: product of ten even theta constants, Maass multiplier, Fourier support, coefficient `64`, and `64`-divisibility.

4. `main.tex:2530-2558`: keep `Borcherds95` only for the general automorphic-product mechanism. The theorem that `mathcal D_X=Delta_5` must cite GNII/GN exactly, because all scalar and genus-two conventions come from them.

5. `main.tex:2601-2630`: source the weight identity by `GNII Theorem 2.1` weight `f(0,0)/2`, `GNII Example 2.4 (2.15)` for `f(0,0)=10`, and `GN Theorem 4.1` or `GN (1.7)` for the theta-normalized `Delta_5` convention. Do not make Clery--Gritsenko row data carry the main weight proof.

6. `main.tex:5185-5206`: replace the current `GN Theorem 2.1 and Section 4` citation with `GN (1.3)--(1.5), Proposition 2.1, Proposition 2.2`; add `GNII §5.1.1, case (t=1,II,0)` only as secondary chamber/list confirmation.

7. `main.tex:5246-5285`: `NIKULIN` metadata is weak. Until repaired, cite GN Proposition 2.2 for the concrete subgroups, indices, wall sets, and chamber decomposition actually used here. Use Nikulin only for the broader classification after exact page data is fixed.

8. `main.tex:5460-5542`: cite `GN Theorem 2.3`, `(1.8)`, and the proof on pp. 10-11 for `m(a)`, `m(0)=-1`, and `tau(ta)=9`. Add an integration note that the arXiv typo in `a` must be checked against AJM before final.

9. `main.tex:5614-5702` and `13543-13563`: cite `GN (3.2)` for the Weyl--Kac product and `GN Proposition 3.1` for `(1/64)Delta_5(2Z)=Phi(z)`. GNII Theorem 2.1 is product-side support, not the denominator-algebra equality.

10. `main.tex:14796-15095`: for rows 2--4, add exact GNII anchors beside each row: `(2.21)` for `Delta_2`, `(2.20)` for `Delta_1`, `(2.11)` for `Delta_{1/2}`, §5.1.1 for `rho_t` and `P_t`, and `(5.1)` for the denominator identity. Keep these rows out of the `D_5(2Z)` normalization.

## Normalization risk map

| Risk | Failure mode | Correct normalization |
|---|---|---|
| `Delta_5` versus `D_5`. | GNII writes the monic product as `Delta_5`; the manuscript writes theta-normalized `Delta_5`. A reader can silently lose a factor `64`. | In this manuscript: `Delta_5` is the theta-product with leading coefficient `64`; `D_5=64^{-1}Delta_5` is monic. |
| `64` as orientation. | Attack PDF repeatedly pushes the square-root/Dirac reading; scalar constants can be misread as signs. | `64` is only theta-to-monic normalization from GN (1.7)/Theorem 4.1. It does not affect Maass character or Hall orientation. |
| `2Z` in denominator. | Writing `den=D_5(Z)` collapses the product expansion and Weyl--Kac denominator normalization. | Product: `q^n r^l s^m=exp(-pi i(alpha,z))`. Denominator: `exp(-2 pi i(alpha,z))`. Therefore `den(g)=D_5(2Z)=64^{-1}Delta_5(2Z)`. |
| Type-II root coordinates. | Mixing GNII triples and manuscript roots can permute the walls. | With `alpha(n,l,m)=2n f_2-l f_3+2m f_{-2}`: `(1,1,0)->delta_1`, `(0,1,1)->delta_2`, `(0,-1,0)->delta_3`. |
| Maass character versus divisor order. | `Delta_5` vanishing order one on a wall is not the same datum as orientation-line monodromy. | Cite GN Proposition 2.1/2.2 for `nu_{Delta_5}`. O1/O1+/O2 remain extra compact-source hypotheses. |
| Product exponents versus imaginary simple roots. | Equating `f(nm,l)` with GN's additive `m(a)`/`tau(a)` corrupts the Weyl sum. | Product exponents give visible signed root supermultiplicities. Imaginary simple roots use GN Theorem 2.3 additive coefficients `m(a)` and `tau(a)`. |
| Active support. | Zero exponent is treated as no root space. | Say "visible positive signed supermultiplicity on `Gamma_act`." Zero exponent does not rule out zero-superdimension root spaces. |
| Rows 2--4. | Importing the main `N=1` doubled normalization into `Delta_2`, `Delta_1`, `Delta_{1/2}`. | GNII rows use `e_t^{(n,l,m)}=q^n r^l s^{tm}` and have no extra `2Z` scalar rescaling in that row normalization. |
| `4096`. | OP scalar branch gets used as automorphic source evidence. | `4096=64^2` is scalar square normalization outside the automorphic theorem. It is not evidence for `epsilon_o=nu_{Delta_5}`. |

## Claims safe as internal computation

1. The Fock/superdeterminant identity
   `sdet_V(1-x)=prod(1-x^lambda)^{sdim V_lambda}` is internal linear algebra (`main.tex:743-755`).

2. The `K_0` determinant package
   `mathcal D_X=64 q^{1/2}r^{1/2}s^{1/2} prod(1-q^n r^l s^m)^{f(nm,l)}`
   is safe as a formal determinant after the GN/GNII exponents and `64` are sourced.

3. The exponent dictionary
   `q^n r^l s^m=exp(-pi i(alpha(n,l,m),z))` and the consequent `Z -> 2Z`
   conversion are internal calculations once the GN root lattice is fixed.

4. The active-support cone lemma is internal arithmetic from the weak Jacobi support
   `4nm-l^2 >= -1`, after the support itself is sourced from GN/GNII/EZ.

5. The statements "the determinant/product forgets brackets, parity split,
   invisible zero-superdimension root spaces, PBW, and primitive representatives"
   are safe internal separation claims (`main.tex:13603-13699`).

6. The low-degree coefficient checks reported by Agents 03 and 11 are safe as
   computational consistency checks: `phi_{0,1}` through `q^2`, `[qrs]=93`,
   the type-II Gram matrix, and `rho=f_2-(1/2)f_3+f_{-2}`. They do not replace
   GN/GNII source citations.

## Patch queue for citations/prose

1. Insert a source-role sentence near the first product statement:
   "Borcherds supplies the general product mechanism; GN/GNII supply the genus-two
   specialization, `64`, the product cone, and the denominator algebra."

2. Replace every theorem-level citation of the product with:
   `\cite[Theorem~2.1, (2.1)--(2.3), Example~2.4, (2.15)--(2.16)]{GNII}`
   plus `\cite[Theorem~4.1]{GN}` for `64^{-1}Delta_5`.

3. Replace the Maass/reflection citation line with:
   `\cite[(1.3)--(1.5), Proposition~2.1, Proposition~2.2]{GN}`,
   and keep `\cite{MAASS:1}` only after direct page checking.

4. In the normalized cusp-form section, cite `GN (1.1)--(1.8)` for the exact
   theta product and coefficient `64`; leave Igusa/Freitag/van der Geer as
   classical structure-theorem background until exact theorem/page anchors are added.

5. Change the denominator theorem citations to `GN (3.2)` and `GN Proposition 3.1`.
   The displayed theorem should read `D_5(2Z)=64^{-1}Delta_5(2Z)` every time.

6. Add a parenthetical at the `alpha` map:
   "GNII's `(0,-1,0),(1,1,0),(0,1,1)` correspond here to
   `delta_3,delta_1,delta_2`."

7. Change every unqualified "root multiplicities are `f(nm,l)`" to
   "visible positive signed root supermultiplicities on `Gamma_act` are `f(nm,l)`."

8. Add a warning beside the `m(a)` formula: "arXiv GN has a typo in the last basis vector;
   verify against the published AJM version before lock."

9. Repair `Gamma_eff^+` at `main.tex:1954`: either define it as the GN positive product cone
   or use the already-defined `Gamma_eff`.

10. Add a row-normalization note in the appendix: rows `F_2,F_3,F_4` use GNII
   `e_t^{(n,l,m)}` and are not the main `N=1` `D_5(2Z)` denominator normalization.

11. Keep the attack-PDF "Dirac/Pfaffian" language out of automorphic theorem statements.
   The automorphic core proves/imports target product and denominator data only.

## Residual source checks

1. Check the published AJM version of GN 1997 against arXiv `alg-geom/9504006`
   for final theorem/equation/page numbering, especially Theorem 2.3, Proposition 3.1,
   Theorem 4.1, and the arXiv typo in the formula for `a`.

2. Check the published IJM version of GNII against arXiv `alg-geom/9611028`
   for final page/equation numbering of Theorem 2.1, Example 2.4, §5.1.1,
   and formulas `(2.11)`, `(2.16)`, `(2.20)`, `(2.21)`, `(5.1)`.

3. Verify Maass 1964 directly if `MAASS:1` remains an independent citation:
   exact formula/page for the multiplier of the product of ten even theta constants.

4. Verify Igusa/Freitag/van der Geer exact anchors for the ring of genus-two
   Siegel modular forms and the theta-constant square `Delta_5^2=Delta_{10}`.
   Until then, cite GN for the exact theta product and coefficient data used here.

5. Verify `EZ:1` exact page/section for `phi_{0,1}`, `phi_{12,1}/Delta_{12}`,
   support, and first coefficients. GN/GNII already quote the needed expansion,
   so this is a citation-hardening task, not a blocker for the automorphic core.

6. Verify Borcherds 1995 published theorem numbering. The Berkeley PDF gives
   Invent. Math. 120 (1995), pp. 161--213, Theorem 10.1; ensure the bibliography
   entry `Borcherds95` has stable metadata and that no stronger genus-two claim is
   assigned to that general theorem.

7. Leave Clery--Gritsenko/Govindarajan rows outside the main `Delta_5` theorem
   until a separate row-by-row source audit pins product, group/cover, character,
   Weyl chamber, and denominator source.

Primary URLs checked:

- GN 1997: https://arxiv.org/pdf/alg-geom/9504006
- GNII 1998: https://arxiv.org/pdf/alg-geom/9611028
- Borcherds 1995 PDF: https://math.berkeley.edu/~reb/papers/on2/on2.pdf
- Igusa 1964(II) PDF: https://math.ou.edu/~rschmidt/dimension_formulas/papers/1964_siegel_modular_forms_II.pdf
- Igusa 1962 metadata/PDF landing: https://math.unt.edu/~schmidt/dimension_formulas/papers/1962_siegel_modular_forms.pdf
