# Agent 02 Gram/Charge Report

Scope: `\Gamma_X^{\mathrm{phys}}`, `\Gamma_X^{\mathrm{form}}`,
`\Gamma_{\mathrm{gram}}`, `\Pi_X`, `B(c,c')`, normal-ordered extension,
primitive/torsion-one descent, raw-descent no-go, D6--D2--D0
Mukai--Gram dictionary, and additive degree law.

Status: the fatal old error "`\Gamma_{\mathrm{gram}}` is the Hall charge
lattice" is mostly healed in `main.tex`. The stable core is the formal
Mukai lattice calculation, the split normal-ordering extension, the
fixed-lift raw-descent obstruction, and the D6--D2--D0 Gram dictionary.
The remaining defects are statement discipline, missing definitions, and
one chain-level cochain notation bug.

## Definitions forced

1. `\Gamma_X^{\mathrm{phys}}` must be defined as a mnemonic alias for the
formal even Mukai bookkeeping lattice, not as the full physical
four-dimensional charge lattice and not as compact Hall support:
\[
\Gamma_X^{\mathrm{phys}}:=\Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S,
\qquad \Lambda_S=\widetilde H(S,\mathbb Z).
\]
Current anchors: `main.tex:4316-4347`, `main.tex:4489-4521`.

2. The actual Hall support must remain a supplied algebraic/effective
semigroup
\[
\Gamma_{X,\sigma}^{\mathrm{eff}}\subset
\Gamma_X^{\mathrm{alg}}\subset\Gamma_X^{\mathrm{form}}.
\]
No formal lattice calculation proves membership, nonemptiness, stability,
or compact moduli. Current anchors: `main.tex:4343-4347`,
`main.tex:8613-8617`, `main.tex:11768-11777`.

3. `\Gamma_{\mathrm{gram}}=\mathbb Z^3` is Fourier/root/Gram degree only.
It is not a Hall charge lattice. Current anchor: `main.tex:4431-4454`.

4. The quadratic Gram map and polarization cocycle must be fixed once:
\[
\Pi_X(Q,P)=\left({Q^2\over2},Q\cdot P,{P^2\over2}\right),
\]
\[
B((Q,P),(Q',P'))=(Q\cdot Q',\,Q\cdot P'+Q'\cdot P,\,P\cdot P').
\]
Then
\[
\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c'),\qquad B(c,c)=2\Pi_X(c).
\]
Current anchors: `main.tex:4351-4368`, `main.tex:4590-4612`.

5. The normal-ordered extension must distinguish two sections:
\[
i_0(c)=(c,0),\qquad s(c)=(c,\Pi_X(c)).
\]
`i_0` is the raw one-particle/Hall placement; it is not additive for
`\star`. The split section `s` is additive but satisfies
`\overline\Pi_X(s(c))=0`; it is not the physical placement of a generator
whose displayed Gram degree is `\Pi_X(c)`. Current text states the split
section but does not force this warning near the definition
(`main.tex:4832-4860`, `main.tex:10425-10428`).

6. Define primitive/torsion-one before using it:
\[
M_c=\mathbb Z Q+\mathbb Z P\subset\Lambda_S,\qquad
I(Q,P)=\gcd\{\text{coordinates of }Q\wedge P\}.
\]
Torsion-one means `I(Q,P)=1`, equivalently `M_c` is saturated in the
ambient unimodular lattice. Current anchor: `main.tex:4523-4588`.

7. Define or delete `H^2_{\mathrm{sym}}`. Current text uses
`[B]=0` and then says the class is nontrivial "as a class in linear
cochains" (`main.tex:4366-4368`, `main.tex:4813-4822`). Correct
mathematics: the ordinary cocycle class is zero because
`B=-\delta\Pi_X`; the residual is only the absence of an additive linear
trivialization. That residual is not the same cohomology class.

## Theorem statements forced

1. **Normal-ordering lattice theorem.** State as the main formal theorem:
`B` is symmetric bilinear; `\star` makes
`\widehat\Gamma_X=\Gamma_X^{\mathrm{phys}}\oplus_B\Gamma_{\mathrm{gram}}`
a split abelian group; `\overline\Pi_X(c,T)=\Pi_X(c)-T` is a homomorphism;
and
\[
(c_1,0)\star\cdots\star(c_k,0)
=\left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right),
\]
\[
\overline\Pi_X\bigl((c_1,0)\star\cdots\star(c_k,0)\bigr)
=\sum_i\Pi_X(c_i).
\]
The flag formula is used later in `D_0` support but is not stated near
the group-law theorem. Current anchors: `main.tex:4614-4810`,
`main.tex:4832-4881`, `main.tex:10131-10146`.

2. **Raw homogeneous fixed-lift no-go.** Define the object before the
theorem: a strict fixed-lift raw pushforward chooses lifts
`L(\gamma)` and requires every nonzero bracket channel to satisfy
`\Pi_X(L(\gamma)+L(\eta))=\gamma+\eta`. Then the theorem proves the
condition forces `B(L(\gamma),L(\eta))=0` on every visible bracket
channel. For the real-root string
\[
[e_i,e_j]\ne0,\qquad [e_i,[e_i,e_j]]\ne0,\qquad
(\operatorname{ad}e_i)^3e_j=0,
\]
this is impossible because
\[
B(c_i,c_i+c_j)=B(c_i,c_i)+B(c_i,c_j)=2\gamma_i\ne0.
\]
Current theorem has the proof but not a formal definition of the raw
pushforward variant. Current anchors: `main.tex:4883-4975`,
`main.tex:12633-12702`.

3. **Formal primitive lift theorem.** The present theorem is only a
formal lift theorem, not descent:
\[
Q=e_1+nf_1,\qquad P=lf_1+e_2+mf_2
\]
gives `\Pi_X(Q,P)=(n,l,m)` and `I(Q,P)=1`. Current anchor:
`main.tex:4523-4588`. Do not promote this to a protected-index descent
without a separate orbit and invariance theorem.

4. **Primitive/torsion-one descent theorem, if claimed.** Any actual
descent statement must add hypotheses: an even unimodular indefinite
lattice with enough hyperbolic planes, primitive saturated rank-two
charge plane, fixed signature/chamber, control of the discriminant form,
and invariance of the protected index under the relevant duality group.
The current manuscript correctly refuses this theorem at
`main.tex:4585-4587`.

5. **D6--D2--D0 Mukai--Gram dictionary.** Current lemma is basically
correct and should stay theorem-level:
\[
v_X(\mathcal I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
\]
\[
P_Y=(1,0,1-d),\quad Q_Y=(0,-\beta,-n),\quad
\Pi_X(Q_Y,P_Y)=\left({\beta^2\over2},n,d-1\right).
\]
For `\beta_h=s_1+hF`, this is `(h-1,n,d-1)`. Current anchor:
`main.tex:2661-2750`.

6. **Chain-level normal-ordering theorem.** The finite/HN theorem must
separate the physical cochain equation
`d_{\mathrm{Hoch}}\Theta_{\Pi}^{\mathrm{phys}}=B_{\mathrm{ch}}` on
`\Gamma_X^{\mathrm{phys}}` from the normal-ordered character equation
`d_{\mathrm{Hoch}}\widehat\Theta_\Pi=0` on `\widehat\Gamma_X`.
Current anchors: `main.tex:8348-8525`, `main.tex:8603-8998`,
`main.tex:9132-9319`.

7. **Optional algebraic normal-ordered BKM lift.** The prior analysis
forces this if the paper wants a formal non-geometric source model:
choose a group homomorphism `L:\Gamma_{\mathrm{gram}}\to
\Gamma_X^{\mathrm{form}}` and define
\[
s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma).
\]
Then `s_L` is a homomorphism into `\widehat\Gamma_X`, and the target
BKM algebra can be regarded as a `\widehat\Gamma_X`-graded algebra
supported on `s_L(\Gamma_{\mathrm{gram}})`. Current `main.tex` has no
`s_L` theorem.

## Proof obligations

1. Define the cochain convention. With
\[
(\delta q)(c,c')=q(c)+q(c')-q(c+c'),
\]
one has `B=-\delta\Pi_X`. With translation functors
`(\mathsf T_\eta V)_\gamma=V_{\gamma+\eta}`,
\[
d_{\mathrm{Hoch}}\Theta_\Pi(c,c')
=\mathsf T_{-\Pi_X(c)-\Pi_X(c')+\Pi_X(c+c')}
=\mathsf T_{B(c,c')}.
\]
This sign check is correct in `main.tex:8504-8513`; it must be made
consistent everywhere.

2. Prove the flag formula by induction from bilinearity of `B`. This is
the additive degree law used by every finite HN word.

3. The raw no-go must cite the nonzero target string, not only the Cartan
matrix. The deciding target data are at `main.tex:12633-12702`: the
height-three roots `2\delta_i+\delta_j` have signed multiplicity `1`.

4. The D6--D2--D0 dictionary must keep the scalar OP/DT branch separate
from Hall multiplication. The rank-one D6 branch is not extension-closed;
it supplies coefficients, not a CoHA product. Current manuscript mostly
does this; the residual wording is listed below.

5. Primitive recognition requires full source data: simple primitive
representatives, parity split, Chevalley/Serre/orthogonality constants,
Hopf pairing, closed radical, no-extra-relations, PBW, and exact
completion. Signed dimensions are insufficient. Current anchors:
`main.tex:12124-12446`, `main.tex:12804-12836`.

## Formulas/constants

Core charge formulas:
\[
\Lambda_S=H^0(S,\mathbb Z)\oplus H^2(S,\mathbb Z)\oplus H^4(S,\mathbb Z),
\quad
(r,D,s)\cdot(r',D',s')=D\cdot D'-rs'-r's.
\]
\[
\Gamma_X^{\mathrm{form}}=\Gamma_X^{\mathrm{phys}}=\Lambda_S\oplus\Lambda_S,
\quad c=(Q,P),\quad \Gamma_{\mathrm{gram}}=\mathbb Z^3.
\]
\[
\Pi_X(Q,P)=\left({Q^2\over2},Q\cdot P,{P^2\over2}\right),\quad
B(c,c')=(Q\cdot Q',Q\cdot P'+Q'\cdot P,P\cdot P').
\]
\[
(c,T)^{-1}=(-c,-T+B(c,c)),\qquad
\overline\Pi_X((c,T)\star(c',T'))=
\overline\Pi_X(c,T)+\overline\Pi_X(c',T').
\]

D6--D2--D0:
\[
\ch(\mathcal I_Y)\sqrt{\operatorname{td}(X)}
=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E.
\]
\[
Q_Y^2/2=\beta^2/2,\quad Q_Y\cdot P_Y=n,\quad P_Y^2/2=d-1.
\]

Real simple Gram degrees from `main.tex:12645-12647`:
\[
\gamma_1=(1,1,0),\qquad \gamma_2=(0,1,1),\qquad \gamma_3=(0,-1,0).
\]
Cartan matrix:
\[
\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}.
\]

Normalization constants are outside the charge proof but must not be
imported into it: `64` is the theta-normalized leading coefficient;
`4096=64^2` is the OP scalar conversion; neither is an orientation
character. Current anchors: `main.tex:14048-14124`.

## Current main.tex anchors

- `main.tex:58-77`: abstract determinant statement.
- `main.tex:131-166`: abstract charge/normal-ordering summary.
- `main.tex:260-291`: primitive recognition summary; missing radical
quotient in displayed isomorphism.
- `main.tex:2634-2758`: D6--D2--D0 Mukai--Gram dictionary.
- `main.tex:4309-4382`: primary charge definition.
- `main.tex:4431-4454`: Gram-index notation and warning.
- `main.tex:4523-4588`: formal primitive torsion-one lift.
- `main.tex:4590-4810`: additivity defect and split extension proof.
- `main.tex:4832-4881`: normal-ordered extension definition.
- `main.tex:4883-4975`: fixed-lift raw-descent no-go.
- `main.tex:5678-5690`: denominator grading comparison; wording still
too loose around "`\Pi`-image modulo `B`".
- `main.tex:8305-8346`: open problem for normal-ordered descent.
- `main.tex:8348-8525`: coefficient dg category and finite Picard lift.
- `main.tex:8603-8998`: conditional Hall descent theorem.
- `main.tex:9132-9319`: finite normal-ordering verification diagrams.
- `main.tex:9973-10173`: finite `D_0` support and normal-ordering labels.
- `main.tex:10414-10563`: `D0-C` and `D0-N`.
- `main.tex:11750-12049`: full Dirac--Igusa certificate.
- `main.tex:12124-12446`: primitive recognition theorem.
- `main.tex:12633-12804`: low-degree target bracket data.
- `main.tex:14031-14201`: coefficient dictionary synthesis.

## Deletions/replacements

1. Replace `main.tex:2752-2756`.

Current problem: "`identifies the Hilbert/PT charge with a triple in the
Mukai lattice of X`" is false wording. The triple is not in the Mukai
lattice of `X`; it is the Gram-index triple of the two K3 Mukai
components.

Replacement:
> The Gram-degree triple `(Q^2/2,Q\cdot P,P^2/2)=(h-1,n,d-1)` records the
> Mukai pairings of the two K3 Mukai components of `v_X(\mathcal I_Y)`.
> It is the Gram-index data used by the Borcherds product and by the OP
> normalization, not an additive Hall charge.

2. Replace the display at `main.tex:289-291` by the radical-quotient
version:
\[
H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)/
\overline{\operatorname{Rad}\langle\,\cdot\,,\,\cdot\,\rangle_X}
\cong \mathfrak g_{\Delta_5}.
\]
The later theorem uses the quotient; the introduction must not omit it.

3. Replace `main.tex:4813-4822`.

Current problem: it says `[B]` is zero and then nontrivial as a class in
linear cochains. Replacement:
> The ordinary symmetric cocycle class of `B` is zero: `B=-\delta\Pi_X`.
> What remains is the linear-trivialization obstruction: no additive
> homomorphism `L:\Gamma_X^{\mathrm{phys}}\to\Gamma_{\mathrm{gram}}`
> satisfies `B=L(c)+L(c')-L(c+c')` unless `\Pi_X\equiv0`.

4. Add immediately after `main.tex:4832-4860`:
\[
i_0(c)=(c,0),\quad s(c)=(c,\Pi_X(c)),\quad
\overline\Pi_X(i_0(c))=\Pi_X(c),\quad \overline\Pi_X(s(c))=0.
\]
Then state: `i_0` is the raw one-particle placement; `s` is the split
extension section and is not the placement used for visible Gram degree.

5. Add the flag normal-ordering lemma after `main.tex:4863-4881`.

6. Rewrite the theorem header at `main.tex:4883-4897` to define
"strict fixed-lift raw pushforward" before proving the obstruction. The
current proof is good; the object under attack is not yet formal enough.

7. Replace `main.tex:5688-5690`.

Current phrase: "`\Pi`-image, well defined modulo the cocycle `B`".
Replacement:
> the `\Gamma_{\mathrm{ind}}`-grading of the denominator algebra is the
> normal-ordered image under `\overline\Pi_X`; the raw map `\Pi_X` is not
> additive and is not a bracket-recognition target unless the relevant
> `B`-channel vanishes.

8. Replace `main.tex:8330-8337`.

Current problem: `d_{\mathrm{Hoch}}\Theta_\Pi=B` mixes a
translation-valued cochain with a `\Gamma_{\mathrm{gram}}`-valued lattice
cocycle. Replacement:
\[
d_{\mathrm{Hoch}}(-\Pi_X)=B
\quad\text{in }\Gamma_{\mathrm{gram}}\text{-valued cochains},
\]
and
\[
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}
\quad\text{in the Picard dg groupoid of central translations}.
\]

9. Replace `main.tex:9192-9199`.

Current problem: it quantifies `c,c'\in\widehat\Gamma_{R^+}` but uses
`B_{\mathrm{ch},R}(c,c')`, defined on physical charges. Use either:
`c,c'\in\Gamma_X^{\mathrm{phys}}` for the physical cochain equation, or
write `\widehat c=(c,T)`, `\widehat c'=(c',T')` and use
`d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0` on `\widehat\Gamma_R`.

10. Clarify `main.tex:10501-10516`: the displayed
`\Theta_{(c,T),(c',T')}` is induced from the physical cochain plus the
recorded `T,T'` shifts. If instead it is meant as a cochain on
`\widehat\Gamma_R`, define `\widehat\Theta_{\Pi,R}(c,T)=\mathsf
T_{T-\Pi_X(c)}` and state its Hochschild coboundary is zero.

11. Add the optional `s_L` theorem only if the manuscript wants a formal
algebraic normal-ordered BKM lift independent of compact geometry. The
current manuscript has no such theorem; the prior analysis demands it as
a clean target-side construction.

## Residual computations

1. D6--D2--D0 dictionary check:
\[
\ch(\mathcal O_Y)=(0,0,d)\otimes1_E+(0,\beta,n)\otimes\omega_E,
\]
so
\[
1-\ch(\mathcal O_Y)=(1,0,-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E.
\]
Multiplication by `\sqrt{\operatorname{td}(S)}=(1,0,1)` gives
`P_Y=(1,0,1-d)`, `Q_Y=(0,-\beta,-n)`. The Mukai pairing gives
`Q_Y\cdot P_Y=n` and `P_Y^2/2=d-1`. The formula is sound.

2. Primitive lift check:
\[
Q=e_1+nf_1,\quad P=lf_1+e_2+mf_2
\]
gives `Q^2=2n`, `P^2=2m`, `Q\cdot P=l`. The wedge coefficient of
`e_1\wedge e_2` is `1`; hence `I(Q,P)=1`. Formal pointwise lift is
proved. Orbit descent is not proved.

3. Additive degree law:
\[
(c_1,0)\star(c_2,0)\star(c_3,0)
=\left(c_1+c_2+c_3,\ B(c_1,c_2)+B(c_1,c_3)+B(c_2,c_3)\right).
\]
Induction gives the general flag formula. Applying `\overline\Pi_X`
subtracts exactly the pairwise cross-terms and leaves
`\sum_i\Pi_X(c_i)`.

4. Raw no-go computation:
First bracket `[e_i,e_j]` forces `B(c_i,c_j)=0`. The second nonzero
bracket `[e_i,[e_i,e_j]]` forces `B(c_i,c_i+c_j)=0`. But
\[
B(c_i,c_i+c_j)=2\Pi_X(c_i)+B(c_i,c_j)=2\gamma_i\ne0
\]
in torsion-free `\Gamma_{\mathrm{gram}}`. The proof is decisive only for
fixed-lift raw descent. Fibre-summed raw descent remains open, as stated
at `main.tex:4970-4975`.

5. Chain-level cochain sign:
For physical labels,
\[
d_{\mathrm{Hoch}}\Theta_\Pi(c,c')=\mathsf T_{B(c,c')}.
\]
For normal-ordered labels,
\[
\widehat\Theta_\Pi(c,T)=\mathsf T_{T-\Pi_X(c)},\qquad
d_{\mathrm{Hoch}}\widehat\Theta_\Pi=0.
\]
This is the clean way to remove the current `NO3` ambiguity.

## Verdict

No fatal mathematical contradiction remains in the formal lattice core.
The manuscript still needs local repairs before proof-grade shipment:
define the raw pushforward variant, separate `i_0` from the split section
`s`, clean the cochain/cohomology language, repair the introduction's
missing radical quotient, correct the D6--D2--D0 wording at `main.tex:2752`,
and fix the finite `NO3` quantifier bug. The compact Hall descent,
primitive recognition, and torsion-one protected-index descent remain
conditional/open; the current text must keep them there.
