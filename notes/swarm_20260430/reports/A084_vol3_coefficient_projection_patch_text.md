# A084 Vol III coefficient-projection patch text

No files edited by the agent.

## Anchors

- Target overclaim:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex:177-207`.
- Dependent prose: the same file at `:106`, `:4201`, `:4222`.
- Existing local criterion to cite:
  `chapters/examples/k3e_bkm_chapter.tex:1485`, label
  `thm:k3e-positive-half-hall-borcherds-criterion`.
- Keep old label `constr:k3e-hcs-hall-borcherds-comparison` as an alias
  to avoid breaking existing references.
- New primary label:
  `prop:k3e-borcherds-coefficient-recognition-gate`.

## Patch-ready replacement for `:177-207`

```tex
\begin{proposition}[Borcherds coefficient extraction and finite Hall--Borcherds recognition]
\label{prop:k3e-borcherds-coefficient-recognition-gate}
\label{constr:k3e-hcs-hall-borcherds-comparison}
\index{hCS-to-Hall comparison!K3 times E}
\index{Hall--Borcherds recognition!K3 times E}
Let $\Obs_{\hCS}^{\mathrm{red}}(X)$ be the K3-cosection-reduced quantum factorisation algebra of holomorphic Chern--Simons observables on $X = K3\times E$, oriented by $\Omega_{K3}\wedge dz_E$. Suppose the oriented DWR/Ran hCS--Hall datum of Definition~\ref{def:cy3-oriented-hcs-hall-comparison-datum} is equipped with a trivialisation of $\mathfrak o_{\hCS\to\Hall}^{\mathrm{comp}}(X)$, with the finite Rees gluing datum of Definition~\ref{def:k3e-finite-rees-gluing}, and with the compact CY$_3$ closure input: either Costello's corrected TCFT carrier $B_{\mathrm{TCFT}}^{(2)}$ or a complete exhaustive separated strongly convergent filtration theorem proving $HH^{-2}_{E_1}=0$ for the compact bar complex. Then the hCS--Hall source map is the composite
\[
\ThetaHCSHall\colon
H^0\!\left(\int_{K3}\Obs_{\hCS}^{\mathrm{red}}(X)\right)
\xrightarrow{\;\mathrm{BV\;trace}\;}
H^\bullet_{\mathrm{van}}\!\left(\mathrm{RPerf}(X),\phi_{\mathrm{CS}}\right)
\xrightarrow{\;\mathrm{Hall\;integration}\;}
\widehat{\CoHA}^{\mathrm{red}}_{\Lambda^{2,1}_{\mathrm{II}}}(X).
\]
The Gritsenko--Nikulin denominator formula supplies the target multiplicity function
\[
m_{\Delta_5}(\gamma)
=
c_{\phi_{0,1}}\!\left(-\tfrac12(\gamma,\gamma),\ell_\gamma\right),
\]
with the coefficient read from the K3 elliptic genus $2\phi_{0,1}$ in the Borcherds normalisation. This is target arithmetic for $\fg_{\Delta_5}$. It is not a morphism from the compact Hall algebra and it does not compare Hall products, brackets, radicals, PBW filtrations, or transition maps.

For a finite downward-saturated Borcherds-cone window $W$, a finite Hall--Borcherds recognition datum consists of source primitive blocks, product and coproduct matrices $M,D$, super-bracket matrices $B$, Hopf-pairing matrices $G$, radical kernels $K$, quotient maps $Q$, comparison matrices $A_\beta$, relation-row certificates, no-extra-relations kernel equality, parity-refined PBW associated-graded comparison, and strict transition/Mittag--Leffler compatibility. Only under this datum does the notation
\[
\ThetaHallBorch|_W\colon
Q_W\widehat{\CoHA}^{\mathrm{red}}_{\Lambda^{2,1}_{\mathrm{II}}}(X)
\longrightarrow
\left(\widehat{U^{\chir}\!\bigl(\fn_+(\fg_{\Delta_5})\bigr)}\right)_W
\]
denote a Hall--Borcherds comparison, where $Q_W$ is the finite source-radical quotient. It is precisely the finite-height comparison isolated by Theorem~\ref{thm:k3e-positive-half-hall-borcherds-criterion}.
\end{proposition}

\begin{proof}
Definition~\ref{def:cy3-oriented-hcs-hall-comparison-datum} supplies the typed hCS--Hall morphism after the orientation line, Tate twist, cohomological shift, completion, and Thom--Sebastiani coherences are fixed. The additional compact closure input rules out the false shortcut in which the raw second bar term is treated as the TCFT carrier: the datum is either $B_{\mathrm{TCFT}}^{(2)}$ itself or the filtered $HH^{-2}_{E_1}$ vanishing theorem. Applying it on the DWR/Ran nerve and then taking the K3-cosection-reduced compact section gives the displayed map $\ThetaHCSHall$.

The denominator formula computes root supermultiplicities on the Borcherds target side. That coefficient extraction verifies the multiplicity row in Theorem~\ref{thm:k3e-positive-half-hall-borcherds-criterion}; it does not verify the Hall bracket, the source radical quotient, the no-extra-relations equality, PBW, or inverse-system compatibility. Those are exactly the finite recognition datum listed above. Hence shared charge support on $\Lambda^{2,1}_{\mathrm{II}}$ is necessary bookkeeping, not product compatibility.
\end{proof}
```

## Dependent replacements

At `:106`, replace the final sentence with:

```tex
The reduced Gromov--Witten/PT theory factors through $\mathcal T_X$ by applying the Hall integration map to the stack of $\mathcal T_X$-perfect modules and then the K3 cosection reduction; this is the map denoted $\ThetaQNCCRDT$, and it feeds the hCS--Hall source side of Proposition~\ref{prop:k3e-borcherds-coefficient-recognition-gate}.
```

At `:4201`, replace the clause referring to the old construction with:

```tex
the finite Hall--Borcherds recognition datum of Proposition~\ref{prop:k3e-borcherds-coefficient-recognition-gate}, satisfying the finite-height criterion of Theorem~\ref{thm:k3e-positive-half-hall-borcherds-criterion},
```

At `:4222`, replace the paragraph with:

```tex
The non-abelian positive-half sector is not obtained by calling the BKM object a Yangian, and not by coefficient projection. The oriented map $\ThetaHCSHall$ produces the compact Hall source; the Gritsenko--Nikulin denominator supplies the target Borcherds multiplicity function. Only after the finite Hall--Borcherds recognition datum of Proposition~\ref{prop:k3e-borcherds-coefficient-recognition-gate} is supplied does the source quotient identify with $\fn_+(\fg_{\Delta_5})$ on the Borcherds charge lattice. The Maulik--Okounkov $R$-matrix remains the $E_2$ chamber-braiding datum on the K3 stable-envelope side; the $E_1$ output on $E$ acquires its braided representation category only after the Drinfeld-centre passage encoded in the CY-C centre/double assembly data.
```

Terminology check: no conflict found for the new primary label or phrase.
The plan uses existing Vol III terms: compact hCS--Hall datum, finite
Rees gluing, positive-half Hall--Borcherds criterion,
Hall--Drinfeld double, and no bare `\kappa`.

