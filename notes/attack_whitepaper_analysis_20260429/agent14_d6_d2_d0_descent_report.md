# Agent 14: D6--D2--D0 / Mukai / Equivariant Descent Report

Scope: Lemma 5.1 replacement, \(K3\times E\) as CY3, Todd factor, reduced scalar quotient integration, protected D-brane index conjecture, connected \(E\)-descent, finite \(E[N]\) and \(E[2]\), quotient-before-correspondence hazards, and variable dictionary consistency.

## verified section repairs

1. The old Lemma 5.1 attack is substantively repaired. The current draft has a self-contained `D6--D2--D0 Mukai--Gram dictionary` at `main.tex:2661`. It states \(X=S\times E\) with \(S\) K3 and \(E\) elliptic, not a fourfold, and computes
   \[
   v_X(\mathcal I_Y)=(1,0,1-d)\otimes 1_E+(0,-\beta,-n)\otimes\omega_E
   \]
   with \(n=\chi(\mathcal O_Y)\), \(P_Y=(1,0,1-d)\), \(Q_Y=(0,-\beta,-n)\), and
   \[
   \Pi_X(Q_Y,P_Y)=\left(\frac{\beta^2}{2},n,d-1\right).
   \]
   For \(\beta_h^2=2h-2\), this gives \((h-1,n,d-1)\). Anchors: `main.tex:2661-2750`. Attack source: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:4847-4956`, `6013-6094`, `21104-21164`, `22400-22477`.

2. The CY3/fourfold error is removed in the local computation. The proof says \(X=S\times E\) is a Calabi--Yau threefold at `main.tex:2697`; no `smooth projective fourfold` or `Todd correction` string remains. The remaining `fourfold` uses at `main.tex:1643-1650` are scoped to CY4 orientation analogues, not to \(K3\times E\).

3. The Todd factor is now exact, not a hidden correction. The proof uses
   \[
   \sqrt{\mathrm{td}(X)}=\pi_S^*(1,0,1)\cup 1,\qquad \sqrt{\mathrm{td}(E)}=1,
   \]
   and shows directly that the third Kunneth component is \(-n\). Anchors: `main.tex:2697-2731`. The attacked phrase \(k=n-\text{Todd correction}\) is gone.

4. The reduced scalar quotient branch is correctly separated from Hall/CoHA integration. Proposition `Reduced scalar quotient integration` defines Behrend-weighted quotient numbers over \(\mathrm{Hilb}^n(X,(\beta,d))/E\) and \(P_n(X,(\beta,d))/E\), cites Oberdieck, and states: scalar integration only, not Hall product, not CoHA integration, not an orientation character. Anchors: `main.tex:2760-2799`; bibliography: `proj.bib:277-288`, `451-461`.

5. The protected D-brane index is no longer asserted as constructed. It is a conjecture conditional on a supplied compact physical Hilbert space and is explicitly not used in the scalar theorem. Anchors: `main.tex:2801-2815`. The follow-on `Protected Hall integration criterion` lists the missing compact Hall/CoHA data before any comparison with \(\mathfrak g_{\Delta_5}\). Anchors: `main.tex:2817-2845`.

6. The connected \(E\)-descent repair is in place. The current lemma separates connected and finite stabilizers and uses
   \[
   H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,\quad
   H^1(BE;\mathbb F_2)=0,\quad H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2.
   \]
   It explicitly removes the false \(E_2^{1,1}\) obstruction and puts the connected obstruction in \(E_2^{2,0}\oplus E_2^{0,2}\). Anchors: `main.tex:3197-3290`. Attack source: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:4958-5076`, `6101-6168`, `11262-11335`.

7. The finite \(E[N]\) and \(E[2]\) repairs are in place. For \(E[2]\), the draft uses \(E[2]\simeq(\mathbb Z/2)^2\) and
   \[
   H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\quad |x_i|=1,\quad
   H^2(BE[2];\mathbb F_2)=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle.
   \]
   It separates degree-two gerbe bits \(r_i\) from degree-one linearization bits \(\rho_i\). Anchors: `main.tex:3290-3349`, `3395-3632`, `3714-3814`.

8. The even \(E[N]\), \(N\ge4\), residual is no longer inferred from \(E[2]\). The draft computes
   \[
   H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
   \quad H^2=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle,
   \]
   and states that \(A_{12}^{(N)}x_1x_2\) is invisible to cyclic restrictions. Anchors: `main.tex:3816-3928`, `3930-3997`. Attack source: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:11402-11430`, `12658-12709`, `21603-21621`.

9. The OP scalar sign is correctly separated from orientation. The draft states \(-4096=-(64)^2\), with the leading minus an OP scalar convention and not an orientation character. Anchors: `main.tex:117-129`, `13936-13954`, `14111-14124`, `14168-14179`. The cosection parity shift is likewise declared not to be the source of the OP minus sign. Anchors: `main.tex:1636-1672`, `3068-3183`.

10. The normal-ordered charge extension and raw-descent obstruction are theorem-level. The draft defines \(\Gamma_X^{\mathrm{form}}\), \(\Gamma_{\mathrm{gram}}\), \(\Pi_X\), \(B\), \(\widehat\Gamma_X\), \(\star\), and \(\overline\Pi_X(c,T)=\Pi_X(c)-T\), then proves associativity, inverse, splitting, and additivity. Anchors: `main.tex:4316-4382`, `4590-4809`, `4832-4881`. The raw fixed-lift no-go theorem proves the type-II real-root obstruction. Anchors: `main.tex:4883-4975`.

11. The quotient-before-correspondence hazard is repaired in the hybrid source section. The draft requires local, wrapped, and mixed extension correspondences to be formed before reduced \(E\)-quotienting, and defines \(Q_{E,R}\) as a functor on the finite correspondence category, not as an object-space quotient. Anchors: `main.tex:7333-7435`, `7571-7634`, `8051-8081`, `11768-12012`.

## remaining wording bugs

1. The corrected Mukai computation is still a `lemma`, though the attack asked for a central theorem. The mathematics is repaired; the status label is weaker than the requested manuscript architecture. Anchor: `main.tex:2661`.

2. The lemma statement uses \(\Lambda_S=H^*(S,\mathbb Z)\) before defining the Mukai pairing, while later sections use \(\widetilde H(S,\mathbb Z)\) and define the pairing explicitly. Align the statement with the later convention and move the pairing before the Gram formula. Anchors: `main.tex:2671-2674`, `2733-2736`, `4491-4499`. Attack source: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:21104-21108`.

3. The notation \(\Gamma_X^{\mathrm{phys}}\) remains as an alias for \(\Gamma_X^{\mathrm{form}}\). The text warns that this is only mnemonic for the formal even Mukai sector, not the full \(\mathcal N=4\) charge lattice, but the repeated `phys` superscript still invites misreading. Anchors: `main.tex:4327-4347`, `4489-4521`, `5683-5690`.

4. The raw no-go theorem title still says `Strict fixed-lift raw Gram descent`. The proof and caveat are honest, but the attack requested the clearer phrase `raw homogeneous \(\Pi_X\)-pushforward` and a separate fixed-lift variant. Anchors: `main.tex:4883-4968`; attack source: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:21233-21256`.

5. The hybrid variable dictionary still has a shift hazard. The OP table says elliptic degree \(d-1\) is the Borcherds \(s\)-exponent. The hybrid source later says the displayed condition records elliptic degree \(m=b_R(\gamma)\). If \(b_R\) is geometric elliptic degree \(d\), the exponent should be \(d-1\); if \(b_R\) is the Gram exponent \(m\), it should not be called elliptic degree without the shift. Anchors: `main.tex:13714-13721`, `7048-7056`, `7683-7697`. Attack source: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:12872-12891`, `21147-21156`.

6. Minor grammar: `Orientation data enters` should be `Orientation data enter` or `The orientation datum enters`. Anchor: `main.tex:2516-2521`.

## theorem replacements

1. Promote `D6--D2--D0 Mukai--Gram dictionary` from lemma to theorem. It should be the local theorem bridging OP/DT variables and Mukai Gram variables. Current proof is adequate for the promoted statement. Anchor: `main.tex:2661-2750`.

2. Keep `Reduced scalar quotient integration` as a proposition. Its claim strength is now correct: it imports scalar quotient invariants and refuses Hall/CoHA content. Anchor: `main.tex:2760-2799`.

3. Keep `Protected D-brane index` as a conjecture. It should not be promoted until the compact Hilbert/Hall object exists. Anchor: `main.tex:2801-2815`.

4. Keep `Connected and finite-stabilizer E-descent of the orientation line` as a lemma or split it into two adjacent lemmas for readability. The mathematical split is already present internally. Anchor: `main.tex:3197-3393`.

5. Keep `Klein-four criterion` and `Even finite-stabilizer residuals beyond two torsion` as separate results. They correctly prevent the \(E[2]\) computation from being promoted to all even \(N\). Anchors: `main.tex:3395-3632`, `3816-3928`.

6. Rename the no-go theorem to `Raw homogeneous \(\Pi_X\)-pushforward cannot realize the type-II real-root strings`, and reserve `fixed lift` for the proof hypothesis/caveat. Anchor: `main.tex:4883-4975`.

7. Keep `Conditional normal-ordered Hall descent certificate and obstruction` conditional. It depends on supplied PTVV host, reduced quotient completion, \(S^1\)-equivariant multiplicative orientation, \(\Theta\)-coherences, Frobenius pairing, and cyclic lift. Anchors: `main.tex:8603-9122`.

## equations/constants

1. Mukai vector:
   \[
   v_X(\mathcal I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E.
   \]
   Anchor: `main.tex:2675-2679`.

2. Mukai pairing:
   \[
   (r,D,s)\cdot(r',D',s')=D\cdot D'-rs'-r's.
   \]
   Anchor: `main.tex:2733-2736`.

3. D6--D2--D0 Gram triple:
   \[
   (Q_Y^2/2,Q_Y\cdot P_Y,P_Y^2/2)=(\beta^2/2,n,d-1),
   \qquad \beta_h^2=2h-2 \Rightarrow (h-1,n,d-1).
   \]
   Anchors: `main.tex:2680-2693`, `2737-2750`.

4. Scalar branch:
   \[
   Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}=-4096\,\Delta_5^{-2},
   \qquad -4096=-(64)^2.
   \]
   Anchors: `main.tex:117-129`, `14111-14124`, `14234-14245`.

5. Connected \(E\)-cohomology:
   \[
   H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\ |u_i|=2,\ H^1(BE)=0,\ H^2(BE)=\mathbb F_2u_1\oplus\mathbb F_2u_2.
   \]
   Anchor: `main.tex:3233-3271`.

6. \(E[2]\)-cohomology:
   \[
   E[2]\simeq(\mathbb Z/2)^2,\quad
   H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\ |x_i|=1,
   \]
   \[
   H^2(BE[2];\mathbb F_2)=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle.
   \]
   Anchors: `main.tex:3306-3316`, `3414-3423`.

7. \(E[2]\) coefficient conversion:
   \[
   r_1=b_{20},\quad r_2=b_{02},\quad r_3=b_{20}+b_{11}+b_{02},
   \]
   hence
   \[
   b_{20}=r_1,\quad b_{02}=r_2,\quad b_{11}=r_1+r_2+r_3.
   \]
   Anchor: `main.tex:3431-3451`.

8. Even \(E[N]\) two-primary class:
   \[
   \beta^{E,N}_{\mathcal C,(2)}
   =A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
   \]
   The mixed term is invisible to cyclic restrictions. Anchors: `main.tex:3816-3866`.

9. Normal-ordered charge law:
   \[
   (c,T)\star(c',T')=(c+c',T+T'+B(c,c')),
   \quad
   \overline\Pi_X(c,T)=\Pi_X(c)-T.
   \]
   Anchors: `main.tex:4370-4377`, `4832-4861`.

10. Gram defect:
    \[
    \Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c'),\quad B(c,c)=2\Pi_X(c).
    \]
    Anchors: `main.tex:4357-4368`, `4590-4612`, `4640-4641`.

## main.tex anchors

1. Executive scalar/orientation separation: `main.tex:117-129`.
2. Status table for determinant, lattice normal ordering, raw Gram obstruction, scalar branch, compact Hall problem: `main.tex:400-443`.
3. D6--D2--D0 protected-index dictionary: `main.tex:2634-2845`.
4. Orientation monodromy open problem and rank-one quotient checks: `main.tex:2914-3195`.
5. Connected and finite-stabilizer \(E\)-descent: `main.tex:3197-3393`.
6. \(E[2]\) Klein-four criterion: `main.tex:3395-3632`.
7. Even finite-stabilizer residuals and finite \((O1)\) obstruction: `main.tex:3816-4008`.
8. Formal Mukai lattice and normal-ordered Gram descent: `main.tex:4309-4995`.
9. Hybrid quotient-after-correspondence rule: `main.tex:7571-7634`, `8051-8081`.
10. Conditional normal-ordered descent theorem: `main.tex:8603-9122`.
11. Dirac--Igusa realization certificate entries \(L_X,H_X,O_X,D_X,R_X\): `main.tex:11768-12123`.
12. OP/DT variable table and scalar square: `main.tex:13714-13731`, `13936-14124`.
13. Coefficient dictionary and synthesis theorem: `main.tex:13957-14265`.

## residual source checks

1. Verify the exact theorem numbering used for Oberdieck's reduced stable-pair quotient invariant and reduced DT/PT comparison before externalizing the manuscript. Current citations use `OberdieckReducedPT` Theorem 1 and Theorem 3(i): `main.tex:2776-2779`, `2792-2795`; bib entry at `proj.bib:277-288`.

2. The finite group cohomology computations for \(BE[2]\) and \(B(\mathbb Z/2^a)^2\) are proved in-text but cite only `Cartan--Eilenberg folklore` at `main.tex:3557-3558`; `proj.bib` has no Cartan--Eilenberg or group cohomology reference. Add a source or remove the folklore citation and keep the calculation self-contained.

3. The CY3 orientation technology references are present and correctly scoped: Joyce--Upmeier, Joyce--Tanaka--Upmeier, PTVV, BBDJS, Bojko, and CY4 analogues are cited in `main.tex:1636-1655`, `2947-2951`, `3070-3084`; bib entries at `proj.bib:566-636`. No cited source currently proves the reduced \(E\)-quotient orientation; the draft states this accurately.

4. The Mukai lattice sources are present: Mukai 1984 and 1987 at `proj.bib:848-867`, cited at `main.tex:4323-4326`. The local D6--D2--D0 computation is elementary enough to stand without a Mukai citation, but the notation should still match the formal Mukai lattice convention.

5. The quotient-after-correspondence rule is formulated internally as certificate data, not sourced to an external theorem. That is acceptable because it is a definition/obstruction package. No source claim should be added unless a functorial quotient theorem is actually imported.

## rewrite actions

1. Promote `main.tex:2661` from lemma to theorem and update references. Title: `D6--D2--D0 Mukai--Gram dictionary`.

2. In that theorem, define \(\widetilde H(S,\mathbb Z)\), the Mukai pairing, \(P_Y\), and \(Q_Y\) before the displayed Gram triple. Avoid bare \(H^*(S,\mathbb Z)\) in the theorem statement unless explicitly identified with \(\widetilde H(S,\mathbb Z)\).

3. Add one explicit variable line near the OP table: geometric elliptic degree is \(d\), Borcherds/Gram exponent is \(m=d-1\), and D0/Fourier index is \(n=\chi(\mathcal O_Y)\). Then repair the hybrid \(b_R\) sentence: either \(b_R=d\) and the \(s\)-degree is \(b_R-1\), or \(b_R=m\) and it is a Gram exponent, not geometric elliptic degree.

4. Rename the raw no-go theorem to `Raw homogeneous \(\Pi_X\)-pushforward cannot realize the type-II real-root strings`; keep the fixed-lift proof and caveat as clauses inside the theorem.

5. Normalize notation: use \(\Gamma_X^{\mathrm{form}}\) for the formal even Mukai lattice, \(\widehat\Gamma_X\) for the \(B\)-normal-ordered extension, and \(\Gamma_{\mathrm{gram}}\) for \(\mathbb Z^3\). Keep \(\Gamma_{\mathrm{ind}}\) only as the denominator-index alias where needed.

6. Add a group cohomology source to `proj.bib`, or delete `Cartan--Eilenberg folklore` and leave the \(BE[2]\) proof as a direct calculation.

7. Fix the one grammar defect at `main.tex:2519`: `Orientation data enter` or `The orientation datum enters`.

No `main.tex` edits were made in this pass.
