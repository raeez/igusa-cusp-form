# Agent 03 Borcherds/Gritsenko--Nikulin Report

## verified target theorem

Status: verified as an imported automorphic/denominator theorem, not as a new compact \(K3\times E\) construction.

The stable theorem is:
\[
D_5(Z):=64^{-1}\Delta_5^\theta(Z)
=q^{1/2}r^{1/2}s^{1/2}
\prod_{(n,l,m)>0}(1-q^nr^ls^m)^{f(nm,l)},
\]
where \(\phi_{0,1}=\sum f(n,l)q^nr^l\), \((n,l,m)>0\) is the standard cusp order, and \(\Delta_5^\theta\) is the theta-product normalization with leading coefficient \(64\).

The denominator identity is:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})
=D_5(2Z)=64^{-1}\Delta_5^\theta(2Z).
\]
With
\[
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2},
\qquad
q^nr^ls^m=\exp(-\pi i(\alpha(n,l,m),z)),
\]
the visible positive signed root supermultiplicities satisfy
\[
\smult\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
\]
on active support, i.e. for \((n,l,m)\in\Gamma_{\mathrm{eff}}\) with \(f(nm,l)\ne0\). This does not exclude root spaces of zero signed superdimension and does not determine even/odd dimensions separately.

Local checks run:

- `python3 compute/verify_square_root.py`: confirms the displayed \(\phi_{0,1}\) coefficients through \(q^2\), \([qrs]D_5/(qrs)^{1/2}=93\), first timelike split \(29|93\), and the signed/additive gaps.
- `python3 compute/verify_lattice.py`: confirms the Gram matrix, type-II simple-root matrix, \(\rho=f_2-\frac12f_3+f_{-2}\), and the exponential dictionary.

## normalization chain

1. Eichler--Zagier/GN coefficient convention:
\[
\phi_{0,1}=(r^{-1}+10+r)+q(10r^{-2}-64r^{-1}+108-64r+10r^2)+O(q^2).
\]
Hence \(f(0,0)=10\), so the Borcherds lift has weight \(f(0,0)/2=5\).

2. GN 1997 theta convention:
\[
[q^{1/2}r^{1/2}s^{1/2}]\Delta_5^\theta=64,
\qquad D_5=64^{-1}\Delta_5^\theta.
\]
GNII sometimes writes the monic lifted form itself as \(\Delta_5\). The manuscript should keep \(D_5\) for the monic product and \(\Delta_5\) only for the theta-normalized section.

3. Borcherds/GN product:
\[
D_5=q^{1/2}r^{1/2}s^{1/2}\prod(1-q^nr^ls^m)^{f(nm,l)}.
\]
The product cone includes the \(m=0\) boundary: \(m>0\), or \(m=0,n>0\), or \(m=n=0,l<0\).

4. Denominator rescaling:
\[
q^nr^ls^m=\exp(-\pi i(\alpha,z)).
\]
The Weyl--Kac--Borcherds denominator uses \(\exp(-2\pi i(\alpha,z))\). Therefore the denominator is \(D_5(2Z)\), not \(D_5(Z)\).

5. Weyl vector:
\[
\rho=\frac12(\delta_1+\delta_2+\delta_3)
=f_2-\frac12f_3+f_{-2},
\qquad
q^{1/2}r^{1/2}s^{1/2}=\exp(-\pi i(\rho,z)).
\]

6. Maass character:
\[
\nu_{\Delta_5}(s_{\delta_i})=-1\quad(i=1,2,3),
\]
and the three chamber-permuting reflections listed in the manuscript have Maass value \(+1\). This is character data, not scalar normalization data.

7. OP scalar conversion:
\[
\chi_{10}^{\mathrm{OP}}=D_5^2=4096^{-1}\Delta_5^2,
\qquad
Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}
=-4096\Delta_5^{-2}.
\]
The factor \(4096=64^2\) is theta-to-monic normalization. It is not an orientation sign.

## manuscript risks

1. Novelty risk. The paper must not sound as if it constructs the Borcherds product for \(\Delta_5\) from compact geometry. GN already supplies the product and denominator algebra. The paper's defensible contribution is the normalization ledger, the \(K_0\)-superdeterminant packaging, and the separation of this imported automorphic target from the open compact realization.

2. Notation drift risk. The manuscript uses \(\Gamma_{\mathrm{eff}}\) as the product cone, but one occurrence still says \(\Gamma_{\mathrm{eff}}^+\) at `main.tex:1954`. Unless \(\Gamma_{\mathrm{eff}}^+\) is defined elsewhere, this should be replaced by \(\Gamma_{\mathrm{eff}}\).

3. GN notation risk. GN/GNII switch between theta-normalized and monic normalizations. The manuscript mostly fixes this with \(D_5=64^{-1}\Delta_5\), but any theorem statement copied from GNII must say whether GNII's symbol \(\Delta_5\) means the monic lift or the theta-product section.

4. Active-support risk. Statements of the form "the same coefficients are the root multiplicities" must always read "visible positive signed root supermultiplicities on active support." The product does not determine invisible zero-superdimension root spaces or parity splits.

5. Boundary risk. The \(m=0\) factors are cusp/Weyl boundary factors. The current bulk/cusp split is correct, but section titles and prose should not call \(\mathcal V\) a literal one-particle Hilbert space.

6. Simple-imaginary versus product-exponent risk. GN's \(m(a)\) and \(\tau(a)\) are additive/Weyl-sum simple-root data. The product exponents \(f(nm,l)\) are visible signed root supermultiplicities on the product side. The manuscript currently distinguishes them; preserve that distinction everywhere.

7. Maass/orientation risk. \(\nu_{\Delta_5}\) is an automorphic character. A compact orientation character \(\epsilon_o\) remains conditional on the orientation-line, Weyl transport, and Pfaffian wall certificates. Scalar constants \(64\), \(4096\), and the OP minus sign supply no evidence for \(\epsilon_o\).

## exact rewrite instructions

1. Near the first theorem-level statement, insert a sentence:

> The identity \(D_5=\operatorname{Borch}(\phi_{0,1})\) is imported from Borcherds--Gritsenko--Nikulin. The present construction repackages this product as a virtual \(K_0\)-superdeterminant and fixes the theta-versus-monic normalization.

2. Replace `\Gamma_{\mathrm{eff}}^+` at `main.tex:1954` by `\Gamma_{\mathrm{eff}}`, or define \(\Gamma_{\mathrm{eff}}^+\) explicitly as the same cone before it appears.

3. Rename any theorem title that suggests a new physical construction. Preferred title:

> Normalized \(K_0\)-determinant form of the Gritsenko--Nikulin product.

4. In every duplicated denominator statement, keep the same form:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z)=64^{-1}\Delta_5(2Z).
\]
Do not write \(\operatorname{den}=D_5(Z)\).

5. Where the text says "same coefficients are signed root supermultiplicities," rewrite to:

> On \(\Gamma_{\mathrm{act}}\), the product exponents \(f(nm,l)\) are the visible positive signed root supermultiplicities of the imported GN denominator algebra.

6. Where the text cites reflection values, cite GN Proposition 2.1 and Proposition 2.2, not just GN Theorem 2.1. The product is GN Theorem 4.1 / GNII Example 2.4; the denominator rescaling is GN Proposition 3.1.

7. Keep the \(m=0\) language exactly boundary-level:

> \(\mathcal V^{\mathrm{bulk}}\) is the Borcherds/Hecke exponent package for \(m>0\); \(\mathcal V^{\mathrm{cusp}}\) is the cusp/Weyl boundary package; neither is a microscopic one-particle Hilbert space.

8. In the abstract or introduction, state the novelty boundary in one line:

> The paper does not construct a compact BPS Hilbert space or compact Hall product; it states the imported automorphic target and the certificates a compact realization must satisfy.

## current anchors

- Product cone and chamber: `main.tex:640-666`.
- \(K_0\) half-index and first coefficients: `main.tex:722-740`; coefficient dictionary: `main.tex:13960-14012`.
- Bulk/cusp split and \(m=0\) boundary warning: `main.tex:771-816`.
- Virtual determinant and \(64\) normalization: `main.tex:818-850`, `main.tex:14048-14060`.
- Maass character and theta product: `main.tex:2383-2470`.
- Weyl chamber, root map, Weyl vector, active support: `main.tex:5159-5458`.
- Denominator algebra identity: `main.tex:5560-5702`; duplicate denominator theorem: `main.tex:13520-13601`.
- What the denominator does and does not determine: `main.tex:13603-13650`.
- OP scalar normalization and \(4096\): `main.tex:13924-13955`, `main.tex:14111-14124`.
- Late normalization lemma for \(D_5(2Z)\): `main.tex:14796-14839`.
- Computation anchors: `compute/verify_square_root.py:414-495`; lattice anchors: `compute/verify_lattice.py:92-125`.

## primary-source verification needed

Checked in this pass from arXiv source, not only the attack transcript:

- GN 1997, `alg-geom/9504006`: Maass multiplier formula (1.3)--(1.5), Fourier coefficient divisibility (1.6)--(1.8), reflection signs Proposition 2.1, Weyl vector (2.3)--(2.4), Weyl expansion Theorem 2.3, denominator identity Proposition 3.1, product Theorem 4.1.
- GNII 1998, `alg-geom/9611028`: general Borcherds product Theorem 2.1, \(\Delta_5\) Example 2.4 / (2.16), Lie-type formula (5.1), \(M_t=U(4t)\oplus\langle2\rangle\), \(\rho_{t,II,\bar0}=(1/(2t),1/2,1/(2t))\), and the \(t=1,2,3,4\) type-II simple-root lists.
- Clery--Gritsenko 2011, `arXiv:0812.3962`: exactly eight dd-modular forms and the row weights \(\Delta_5,\Delta_2,\Delta_1,\Delta_{1/2},\nabla_3,\nabla_2,\nabla_{3/2},Q_1\).

Still needed before manuscript lock:

1. Check the published AJM/IJM versions against the arXiv sources for equation numbering. GN arXiv source has at least one evident typo in the formula for \(a\) in the proof of Theorem 2.3; the manuscript's \(+(m-1)f_{-2}\) is the context-correct version.
2. Verify Maass 1964 directly for the character formula if the manuscript wants to cite Maass independently rather than through GN.
3. Verify the Borcherds 1995 theorem citation only as the general singular-theta/infinite-product theorem; the constants \(64\), \(D_5\), and \(\Delta_5(2Z)\) are GN-specific.
4. If the eight-row appendix remains, verify each row against Clery--Gritsenko plus Govindarajan/Gopala Krishna at the exact row, group/cover, character, Weyl chamber, and denominator theorem level.

## residuals

1. The Borcherds/GN normalization chain is stable. No fatal mathematical error found in the current \(D_5\), \(64\), \(2Z\), Weyl-vector, or active-support conventions.

2. The manuscript still has a presentation residual: the title and some section labels can invite a reader to think the compact first-order object has been built. The text mostly says the opposite, but theorem names and first-page wording must keep the contribution at "imported target plus normalization plus conditional recognition."

3. The undefined \(\Gamma_{\mathrm{eff}}^+\) occurrence is a local notation defect.

4. The eight-row material is outside the minimal \(\Delta_5\) theorem. It is defensible as a certificate appendix only if every row has a compact table fixing group/cover, character, seed, product degree lattice, Weyl data, source theorem, and status. Otherwise it should be moved out of the main proof spine.

5. No edit to `main.tex` was made by this agent.
