# Eight Rows / Boundary Certificate / Spin \(L\)-Factor Report

Scope: Clery--Gritsenko eight dd-modular forms, GN/Govindarajan denominator rows, CHL scalar squares, boundary-row physical-host certificates, and the spin \(L\)-factor appendix.

Files read:

- `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`
- `main.tex`
- `proj.bib`
- `appendices/boundary_compatibility_conditions.tex`
- `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`

Primary-source spot checks used:

- Gritsenko--Clery, arXiv:0812.3962, abstract/Theorem 0.1/Theorem 1.4 source stream: exactly eight dd-modular forms; nine candidates with \((2,4;\frac12)\) excluded.
- Govindarajan, arXiv:1006.3472, abstract/source stream: square roots of twisted CHL Siegel forms are dd-modular forms classified by Clery--Gritsenko and arise as Weyl--Kac--Borcherds denominator formulae.
- Cheng--Dabholkar, arXiv:0809.4258, abstract/source stream: \(N=1,2,3\) CHL models have BKM denominator interpretation and finite Weyl chambers.
- Govindarajan--Gopala Krishna, arXiv:0907.1410 source stream: composite \(N=4\) square-root/theta-product data for \(\Delta_{3/2}\) and related BKM claims.

## Stable Row Facts

The stable core is an automorphic/denominator ledger, not a physical-host theorem.

1. Clery--Gritsenko classify exactly eight genus-two dd-modular forms with diagonal divisor. In the manuscript's present order:

| row | form | \((t,N)\) | group/cover label in `main.tex` | weight | character/multiplier |
|---:|---|---:|---|---:|---|
| 1 | \(\Delta_5\) | \((1,1)\) | \(\Gamma_1\) | \(5\) | \(v_\eta^{12}\times v_H\) |
| 2 | \(\Delta_2\) | \((2,1)\) | \(\Gamma_2\) | \(2\) | \(v_\eta^{6}\times v_H\) |
| 3 | \(\Delta_1\) | \((3,1)\) | \(\Gamma_3\) | \(1\) | \(v_\eta^{4}\times v_H\) |
| 4 | \(\Delta_{1/2}\) | \((4,1)\) | \(\Gamma_4\) | \(1/2\) | \(v_\eta^{3}\times v_H\), degree \(8\) |
| 5 | \(\nabla_3\) | \((1,2)\) | \(\Gamma_0^{(2)}(2)\) | \(3\) | \(\chi_2^{(2)}\times v_H\) |
| 6 | \(\nabla_2\) | \((1,3)\) | \(\Gamma_0^{(2)}(3)\) | \(2\) | \(\chi_2^{(3)}\times v_H\) |
| 7 | \(\nabla_{3/2}\) | \((1,4)\) | \(\Gamma_0^{(2)}(4)\), \(\mu_4\)-multiplier cover for denominator use | \(3/2\) | \(\chi_4^{(4)}\times v_H\), order \(4\) |
| 8 | \(Q_1\) | \((2,2)\) | \(\Gamma_2(2)\) | \(1\) | \(\chi_4^{(2)}\times v_H\) |

Current anchors: `main.tex:14339-14369`, `main.tex:14692-14739`. The row-order warning is necessary: the Clery--Gritsenko source order differs from the manuscript's present order (`main.tex:14692-14710`).

2. Rows \(1\)--\(4\) have Gritsenko--Nikulin denominator theorems. Row \(1\) uses the main \(N=1\) normalization
\[
D_5=64^{-1}\Delta_5,\qquad \operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z)=64^{-1}\Delta_5(2Z).
\]
Rows \(2,3,4\) use the \(e_t^{(n,l,m)}=q^nr^ls^{tm}\) normalization with \(C'_j=a_j=1\), lattices \(M_t=U(4t)\oplus\langle2\rangle\), and Weyl vectors \((1/(2t),1/2,1/(2t))\). Current anchors: `main.tex:14826-15060`.

3. Rows \(5\)--\(8\) have Clery--Gritsenko product data. The product theorem supplies automorphic products, diagonal divisors, cusp-labelled coefficients, product-degree maps, and prefactors. It does not by itself supply simple real roots, Weyl chambers, reflection character, parity, or Weyl-sum side. Current anchors: `main.tex:15100-15321`, especially `main.tex:15191-15193` and `main.tex:15311-15320`.

4. Rows \(5\)--\(8\) have Govindarajan CHL/WKB denominator data in CHL normalization:
\[
\nabla_3\leftrightarrow \mathcal G_1(2),\quad
\nabla_2\leftrightarrow \mathcal G_1(3),\quad
\nabla_{3/2}\leftrightarrow \mathcal G_1(4),\quad
Q_1\leftrightarrow \mathcal G_2(4).
\]
For \(F_5,F_6,F_7\): \(L=M_1\), \(P^{(1)}=\{(0,-1,0),(1,1,0),(0,1,1)\}\), \(\rho=\alpha_1(1/2,1/2,1/2)\). For \(F_8\): \(L=M_2\), \(P^{(2)}=\{(0,-1,0),(1,1,0),(1,3,1),(0,1,1)\}\), \(\rho=\alpha_2(1/4,1/2,1/4)\). In all four rows the real simple roots are even and \(\epsilon=\det\). Current anchors: `main.tex:15470-15580`, `main.tex:15788-15839`.

5. CHL scalar squares are only scalar-square data:
\[
\nabla_3^2=\Phi_6^{(1,2)},\qquad
\nabla_2^2=\Phi_4^{(1,3)},\qquad
F_7^2=\Phi_3,\qquad
Q_1^2=\Phi_2^{(2,4)}.
\]
They do not supply denominator signs, parity, Weyl chamber, reduced CY/DT host, or compact Hall/chiral host. Current anchors: `main.tex:14379-14440`, `main.tex:14505-14531`, `main.tex:15582-15598`.

6. The \(N=1\) OP/DT scalar host is stable only for the Igusa row:
\[
Z^{K3\times E}_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}.
\]
It is a reduced quotient-by-\(E\), Behrend-weighted scalar theorem in the specified OP chamber, not a compact Hall/Pfaffian construction. Current anchors: `main.tex:13724-13855`, `main.tex:13857-13955`.

## Invalid Physical-Host Claims

No surviving explicit theorem in `main.tex` claims that rows \(2\)--\(8\) have compact physical hosts. The manuscript mostly quarantines the danger. The following inferences are invalid and must remain excluded:

| invalid inference | why invalid | current quarantine |
|---|---|---|
| Clery--Gritsenko product \(\Rightarrow\) BKM denominator | product side lacks Weyl chamber, real roots, reflection character, parity, Weyl sum | `main.tex:15406-15468` |
| CHL scalar square \(\Rightarrow\) denominator theorem | square kills the sign/reflection character | `main.tex:14505-14531`, `main.tex:15582-15598` |
| Govindarajan denominator \(\Rightarrow\) CY/DT or compact Hall/chiral host | CHL/WKB denominator is not a reduced obstruction theory or compact factorization object | `main.tex:14446-14459`, `main.tex:15866-15891` |
| \(\mu_4\)-cover for \(F_7\) \(\Rightarrow\) arbitrary fractional comparison row | \(F_7\) has weight \(3/2\); comparison symbols of weights \(1/4\) or \(0\) need separate root/cocycle certificates | `main.tex:15916-16009` |
| \(\Phi^{\mathrm{cmp}}_5=F_5\), \(\Phi^{\mathrm{cmp}}_7=F_7\), \(\Phi^{\mathrm{cmp}}_8=F_8\) | false by weight against the eight-row table | `main.tex:15893-15938` |
| \(64\), \(4096\), or spin \(L\)-data determine orientation | constants and \(L\)-factor data are scalar/eigenline normalizations; orientation is line-monodromy data | `main.tex:13924-13955`, `main.tex:14677-14686` |

Residual wording risk: the part title "Diagonal-divisor rows and CHL boundary physics" at `main.tex:14267` overstates the host status. The content is disciplined; the title can be read as physical-host language. Prefer "Diagonal-divisor rows and denominator certificates" unless this part is moved to a companion paper.

## Required Certificate Table Fields

The current five-level certificate definition is correct (`main.tex:14289-14337`). The row table should be forced into one compact schema, with no prose-only certificate claims.

Required fields per row:

| field | purpose |
|---|---|
| row id and row order | prevents source-order/present-order/CHL-table mismatch |
| \(F_j\), \((t,N)\), weight | pins the Clery--Gritsenko row |
| modular group or exact cover | especially \(\Gamma_t^+\), \(\Gamma_0^{(2)}(N)\), \(\Gamma_2(2)\), \(\mu_4\)-cover |
| character/multiplier and exact order | separates scalar modularity from denominator sign |
| diagonal divisor and multiplicity | Clery--Gritsenko dd condition |
| Jacobi seed at every cusp | needed for \(F_5,F_6,F_7,F_8\) multi-cusp products |
| product prefactor and product-degree lattice | \(\rho^{\mathrm{pref}}\), \(M_t\), and cusp-labelled \(\alpha_j^{\mathrm{prod}}\) |
| product theorem source | CG Theorem 3.1 / GNII product theorem |
| denominator source | GN/GNII or Govindarajan CHL/WKB; mark "none" where absent |
| Weyl vector, simple real roots, chamber, Weyl group, reflection character | only populated after a denominator theorem |
| imaginary simple-root coefficient convention | distinguishes product exponents \(\mu_j\), GN additive \(N_t(a)\), and Govindarajan sign conventions |
| CHL/dyon square source | scalar square level \(\mathscr S_j\), not denominator level |
| reduced CY/DT scalar host | \(\mathscr Z_j\); only row \(1\) currently filled |
| compact Hall/chiral host | \(\mathscr H_j\); open for all rows |
| row map / comparison-symbol status | explicit "no row map" unless a certificate is supplied |
| normalization \((C'_j,a_j)\) | separates \(D_5(2Z)\) from \(e_t\)-normalizations |

Minimum table for publication:

\[
(F_j,\Gamma_j,\mathrm{cover},\nu_j,\phi_j,\rho_j,L_j,
\mathrm{product\ source},\mathrm{denominator\ source},
\mathrm{scalar\ source},\mathscr Z_j,\mathscr H_j,\mathrm{row\ map}).
\]

For \(F_7\), the table must say: "order-four Clery--Gritsenko multiplier; denominator theorem only after pullback to the associated \(\mu_4\)-multiplier cover; \(F_7^2=\Phi_3\) is a scalar square in the fixed composite \(N=4\) branch; no comparison row or physical host follows."

## Current `main.tex` Anchors

Core claim-strength anchors:

- Abstract row-quarantine statement: `main.tex:169-171`.
- Dependency chain row: `main.tex:194-210`.
- Intro certificate paragraph: `main.tex:339-355`.
- Status tables: `main.tex:382-385`, `main.tex:446-450`.
- OP/DT scalar-square theorem and sign quarantine: `main.tex:13724-13955`.

Eight-row main section:

- Five-level physical-host certificate: `main.tex:14289-14337`.
- Clery--Gritsenko theorem and row table: `main.tex:14339-14369`.
- Five-level status table: `main.tex:14374-14444`.
- Extension separation: `main.tex:14461-14471`.
- Certificates beyond known rows: `main.tex:14473-14503`.
- CHL squares and denominator signs: `main.tex:14505-14531`.
- Final separation statement: `main.tex:14534-14552`.

Spin \(L\)-factor appendix:

- Section: `main.tex:14558-14686`.
- The appendix already states independence from Dirac--Igusa at `main.tex:14677-14686`.

Eight-row boundary appendix:

- Row order/table/characters: `main.tex:14689-14739`.
- Candidate denominator proof datum: `main.tex:14740-14766`.
- GN row data \(2,3,4\): `main.tex:14841-15060`.
- CG congruence products: `main.tex:15100-15321`.
- Formal product algebra/current rows: `main.tex:15323-15404`.
- Nonabelian promotion test: `main.tex:15406-15468`.
- Govindarajan denominator rows: `main.tex:15470-15839`.
- Nonabelian row-data remark: `main.tex:15841-15864`.
- Physical-host open problem: `main.tex:15866-15891`.
- Comparison-row weight rejection: `main.tex:15893-16055`.
- Boundary compatibility input: `appendices/boundary_compatibility_conditions.tex:1-121`.

## Material To Move / Delete / Compress

1. Move the detailed eight-row ledger out of the main theorem spine. The attack ledger repeatedly flags this as a distraction (`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:774-830`, `5665-5732`, `7827-7870`, `20853-20860`, `21803-21810`, `24569-24571`). The clean main paper needs at most a one-page independent certificate ledger plus a sentence: "This part is not used in the \(N=1\) theorem."

2. If the row material stays in this paper, keep `main.tex:14289-14552` as a compressed main-text section and move `main.tex:14689-16081` into an optional appendix or companion note. The current manuscript has two row catalogues: a main-status table and a detailed appendix. The duplication invites row-order mismatch.

3. Compress the comparison-symbol material. `main.tex:15893-16055` is mathematically useful but should be a short "forbidden identifications" box, not a long fractional-root discussion, unless the paper wants a full modular-root certificate appendix.

4. Rename or move "Diagonal-divisor rows and CHL boundary physics." The title should not imply a physical host. Preferred title: "Diagonal-divisor rows and denominator certificates."

5. Move the spin \(L\)-factor appendix to a separate arithmetic normalization note unless it is explicitly used in a theorem. It does not construct \(\mathfrak D_X\), \(\epsilon_o\), \(\mathcal F_X^{\mathrm{hyb}}\), the primitive comparison, a row certificate, or a compact host. If retained, keep only the independence remark and cite the external note.

6. Keep `appendices/boundary_compatibility_conditions.tex` as an \(N=1\) boundary-compatibility appendix. It is correctly scoped: it states no row map and no CY/DT/chiral host for \(F_5,\ldots,F_8\) (`appendices/boundary_compatibility_conditions.tex:114-121`).

## Residual Primary-Source Checks

These are still debt before publication. The local manuscript assertions are coherent, but every item below needs a page/theorem-level source check in the final bibliography pass.

1. Clery--Gritsenko `GC`: verify Theorem 1.4 row table, Proposition 1.2 nine-candidate list, exclusion of \((2,4;\frac12)\), character orders, and Section 3 product displays for \(\nabla_3,\nabla_2,\nabla_{3/2},Q_1\).

2. Gritsenko--Nikulin `GNII`: verify Theorem 2.1 product formulae for \(\Delta_2,\Delta_1,\Delta_{1/2}\), Lemma 2.5 active-support chamber condition, Section 5.1.1 Weyl chambers/simple roots, and the \(t=4\) parabolic infinite-root convention.

3. Gritsenko--Nikulin `GN`: verify Proposition 3.1 normalization
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)
\]
against the manuscript's \(D_5=64^{-1}\Delta_5\) convention.

4. Govindarajan `Gov11BKM`: verify Table 3 maps \(\nabla_3,\nabla_2,\nabla_{3/2},Q_1\) to \(\mathcal G_1(2),\mathcal G_1(3),\mathcal G_1(4),\mathcal G_2(4)\); verify Sections 4.2--4.3 supply integrality, simple real roots, Weyl sign, and WKB denominator formula; verify Appendix C/D data for \(Q_1\).

5. Govindarajan--Gopala Krishna `GK09CHL` and `GK10Composite`: verify the scalar square identities and exact branches:
\[
\nabla_3^2=\Phi_6^{(1,2)},\quad
\nabla_2^2=\Phi_4^{(1,3)},\quad
\nabla_{3/2}^2=\Phi_3,\quad
Q_1^2=\Phi_2^{(2,4)}.
\]
The \(F_7\) \(\mu_4\)-cover and branch must be checked directly, not inferred from notation.

6. OP/Oberdieck sources `OB`, `OPand`, `OberdieckReducedPT`: verify that the only reduced CY/DT scalar-host certificate currently filled is the \(K3\times E\), primitive nonzero K3-class, quotient-by-\(E\) branch for row \(1\).

7. Spin \(L\)-factor sources `Andr74`, `ZagierSK`, `Manin72`, `KZ`, `Del79`: if the appendix remains, verify the exact completion convention, Saito--Kurokawa source weight, root number, pole cancellation at \(s=9\), residue at \(s=10\), and scalar-independence of the Hecke eigenline. This check is unnecessary if the appendix is moved out.

## Verdict

The row material is mathematically useful as a quarantine ledger. It should not be part of the dependency closure of the \(N=1\) Dirac--Igusa theorem. The stable core is:

\[
\text{CG product row} \;+\; \text{GN/Gov denominator row where sourced}
\;+\; \text{separate scalar square where sourced}
\;+\; \text{open physical-host certificate}.
\]

No boundary row becomes physical until \(\mathscr Z_j\) or \(\mathscr H_j\) is filled by an actual reduced scalar host or compact Hall/chiral construction. The spin \(L\)-factor appendix is independent arithmetic normalization; keep it outside the main proof.
