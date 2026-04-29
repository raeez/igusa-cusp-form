# Agent57 source/target firewall patch report

CONTROL: proposal-only source/target firewall patch reviewer.  No source
files edited.  Writable surface limited to this report.

Date: 2026-04-29.

## Evidence read

- Attack-heal skill and protocol:
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`;
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`.
- Latest PDF text:
  `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`.
- Current manuscript: `main.tex`.
- Required reports:
  `agent48_universal_finite_source_adversary_report.md`,
  `agent50_pbw_radical_latest_report.md`,
  `agent51_dirac_block_superpfaffian_report.md`,
  `agent53_hybrid_wrapped_source_latest_report.md`.

## Stable core

There is no stable core for \(UDI_R\) as a compact \(K3\times E\) source.
There is a stable target-side core:

\[
P_R^{\mathrm{tar}}
=\bigoplus_{\gamma\in A_R}\mathfrak g_{\Delta_5,\alpha(\gamma)},
\qquad
U_R^{\mathrm{tar}}
\subset U(\mathfrak g_{\Delta_5})
\]

with BKM bracket, Kac/Gritsenko--Nikulin invariant form, radical quotient,
PBW basis, and signed multiplicities imported from the denominator target.
Calling this object a source is circular: the latest PDF sets
\(V_\gamma=\mathfrak g_{\Delta_5,\gamma}\)
(`...revision-1923.txt:29390-29397`), takes
\(H_R=U(\mathfrak g_{\Delta_5})_{\le R}\)
(`:29545-29555`), and proves PBW/radical/Pfaffian statements by the same
target algebra (`:29696-29724`).

Current `main.tex` already has the right firewall at:

- `main.tex:5639-5783`: denominator algebra is target.
- `main.tex:5788-5849`: formal current envelope is target-side, not compact
  BPS states.
- `main.tex:10993-11027`: finite \(K_0\)-Pfaffian shadow is target invariant,
  not a Pfaffian line or first-order operator.
- `main.tex:12189-12212`: target-internal bar-cobar counit does not supply
  source coalgebra.
- `main.tex:12233-12586`: primitive recognition is conditional on
  independently supplied source data.

The patch should strengthen that firewall by giving the UDI-shaped object a
safe target name and by banning source language for it.

## Destroyed claims

1. "This is the constructed finite compact source object" is false.
   Latest PDF lines `29517-29620` define \(UDI_R\) from the target; lines
   `29622-29732` state the central theorem.  Agent48 and Agent50 both find
   this is a target envelope, not compact Hall geometry.

2. "PBW monomials give a source basis" is false unless finite source
   representatives and a source PBW comparison are supplied.  Target PBW is
   valid for \(U(\mathfrak g_{\Delta_5})\), but `main.tex:12481-12497` says
   it does not transfer to the compact source without finite-stage
   isomorphisms.

3. "The radical quotient is already taken" is a target tautology, not a
   source theorem.  The source radical must be a closed Lie ideal and coideal
   with transition-compatible finite kernel matrices (`main.tex:12419-12450`).

4. "Hyb_R plus F_R is an actual hybrid source" is false for \(K3\times E\).
   Latest PDF lines `29110-29244` define a colored PROP with BKM/product maps.
   Agent53 correctly classifies it as a comparison interface, not wrapped
   stacks, anchors, mixed Hall correspondences, quotient descent, or protected
   integration.

5. "The super-Pfaffian product is a compact Pfaffian" is false unless a
   Pfaffian line, orientation-gerbe convention, square map, and geometric
   trivialization are supplied.  Agent51 classifies the PDF block at
   `29390-29515` as a finite algebraic block/product convention.

## Patch map

### Patch 1 -- abstract firewall

Location: after `main.tex:94-98`, immediately after:

```tex
Thus the denominator algebra supplies the
algebraic square root target and its target-internal Borcherds bracket.
It does not supply a compact BPS Hilbert space, compact Hall
correspondences, an orientation, or a BPS operator product/local
collision map.
```

Add:

```tex
Any finite PBW tower built by taking primitive pieces
\(\mathfrak g_{\Delta_5,\gamma}\), state object
\(U(\mathfrak g_{\Delta_5})_{\le R}\), BKM bracket, GN/Kac invariant
pairing, and Borcherds product exponents is therefore a target reference
tower.  It is not a compact Hall source, not a \(K3\times E\) geometric
realization, and not evidence for source PBW, source radical, source
coalgebra, or source Pfaffian data.
```

Reason: catches the UDI overclaim before the reader reaches the body.

### Patch 2 -- introduce target reference tower

Location: after `main.tex:5849`, immediately after the proof of
Proposition `Formal current envelope` and before
`\begin{definition}[Holomorphic \(E_3\) quantum upgrade]`.

Insert:

```tex
\begin{definition}[Finite Borcherds--Kac target reference tower]
\label{def:bk-target-reference-tower}
Let \(A_R\subset\Gamma_{\mathrm{gram}}\) be a finite downward-saturated
active window for the Borcherds--Kac presentation of
\(\mathfrak g_{\Delta_5}\).  If a linear lift
\(L_R:A_R\to\widehat\Gamma_X\) is chosen, it is only a bookkeeping lift of
target degrees; it is not a geometric Hall charge lift.

Define the finite target primitive span
\[
P_R^{\mathrm{tar}}
:=
\bigoplus_{\gamma\in A_R}
\mathfrak g_{\Delta_5,\alpha(\gamma)}
\]
and the finite PBW target span
\[
U_R^{\mathrm{tar}}
:=
\operatorname{span}\{
x_{\gamma_1,i_1}\cdots x_{\gamma_k,i_k}
\mid
\gamma_j\in A_R,\ 
\gamma_1+\cdots+\gamma_k\in A_R
\}
\subset U(\mathfrak g_{\Delta_5}),
\]
for a fixed ordered homogeneous PBW basis of
\(\mathfrak g_{\Delta_5}\).  Multiplication and coproduct are inherited
from \(U(\mathfrak g_{\Delta_5})\) as tower maps
\[
\mu^{\mathrm{tar}}_{R,R'}:
U_R^{\mathrm{tar}}\otimes U_{R'}^{\mathrm{tar}}
\longrightarrow U_{R+R'}^{\mathrm{tar}},
\qquad
\Delta_R^{\mathrm{tar}}:
U_R^{\mathrm{tar}}\longrightarrow
\bigoplus_{R_1+R_2\le R}
U_{R_1}^{\mathrm{tar}}\otimes U_{R_2}^{\mathrm{tar}} .
\]
The bracket on \(P_R^{\mathrm{tar}}\), the invariant form, and the
radical quotient are the imported Borcherds--Kac/Gritsenko--Nikulin
target structures.  The package
\[
\mathsf{BKRef}_{R,L}
:=
(A_R,L_R,P_R^{\mathrm{tar}},U_R^{\mathrm{tar}},
\mu^{\mathrm{tar}},\Delta_R^{\mathrm{tar}},
\langle\, ,\,\rangle_{\mathrm{GN}},
\operatorname{Rad}_{\mathrm{GN},R})
\]
is the finite Borcherds--Kac target reference tower.
\end{definition}

\begin{proposition}[Target reference tower normalization]
\label{prop:bk-target-reference-tower-normalization}
The tower \(\mathsf{BKRef}_{R,L}\) has target primitives
\(P_R^{\mathrm{tar}}\), target PBW bases, the standard target invariant
form, the standard target radical quotient, and visible signed
multiplicities
\[
\smult\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
\]
on active support.  Its normalized target product
\[
\mathcal D_R^{\mathrm{tar}}
:=
64q^{1/2}r^{1/2}s^{1/2}
\prod_{\gamma=(n,l,m)\in A_R}
(1-q^nr^ls^m)^{
\smult\mathfrak g_{\Delta_5,\alpha(\gamma)}
}
\]
is the finite-window truncation of the imported
Borcherds--Gritsenko--Nikulin product for \(\Delta_5\).

This constructs no compact \(K3\times E\) Hall source, no geometric
extension correspondence, no quotient orientation gerbe, no source
coalgebra, no source Hopf radical, and no geometric Pfaffian line.  A
Dirac--Igusa realization is a source-side system
\[
R_{X,R}:H^{\mathrm{geom}}_{X,R}\longrightarrow\mathsf{BKRef}_{R,L}
\]
preserving Hall products, coproducts, primitives, orientations, source
coalgebras, Hopf pairings, radical kernels, PBW filtrations, Pfaffian
lines, and transition maps.
\end{proposition}
```

Reason: this absorbs the legitimate UDI-shaped content while preventing
UDI-as-source.  Prefer `\mathsf{BKRef}_{R,L}` or
`\mathsf{DenRef}_{R,L}` over `UDI_R`; if `UDI` is retained at all, it must
be `\mathrm{UDI}^{\mathrm{tar}}_R`, never source.

### Patch 3 -- protect the finite \(K_0\)-Pfaffian section

Location: after `main.tex:11010-11012`, immediately after:

```tex
This shadow is a target invariant.  It is not a compact Hall object, not
a Pfaffian line on the reduced quotient, and not a first-order operator.
```

Add:

```tex
Equivalently, choosing finite algebraic blocks with
\(V_\gamma=\mathfrak g_{\Delta_5,\alpha(\gamma)}\) and product
\(\prod_\gamma(1-x^\gamma)^{\sdim V_\gamma}\) gives only a target
normalization model for this \(K_0\)-shadow.  It does not upgrade the
shadow to a compact Dirac operator or to a source Pfaffian.
```

Reason: Agent51's `D_\gamma` block is safe only as target algebraic
normalization.

### Patch 4 -- strengthen source coalgebra firewall

Location: after `main.tex:12189-12212`, immediately after:

```tex
... were supplied independently of the target counit.
```

Add:

```tex
Nor is \(C_{X,R}\) supplied by taking the chiral bar construction of a
target-colored PROP whose values are
\(\mathfrak g_{\Delta_5,\alpha(\gamma)}\).  Such a bar construction is a
target comparison coalgebra.  It becomes a source coalgebra only after the
finite hybrid \(K3\times E\) correspondence source, with its local,
wrapped, mixed, quotient, orientation, and protected-integration data, has
been constructed independently.
```

Reason: blocks the latest PDF move `C_R=B_E^{ch}(F_R)` with
`F_R(L_gamma)=F_R(W_gamma,a)=V_gamma=g_gamma`.

### Patch 5 -- add target-reference cross-reference in primitive recognition

Location: after `main.tex:12274-12277`, immediately after:

```tex
This target-side statement is imported from the Gritsenko--Nikulin/Kac
construction; it is not a compact Hall construction.
```

Add:

```tex
The finite target reference tower
\(\mathsf{BKRef}_{R,L}\) of
Definition~\ref{def:bk-target-reference-tower} is a finite-window
bookkeeping form of this same imported target.  It may be the codomain of
a compact realization functor.  It cannot discharge any of the source-side
assumptions \textup{(S1)--(S10)} below.
```

Reason: makes the new target tower subordinate to the existing
recognition theorem.

### Patch 6 -- split geometric degree from trace exponent

Location: `main.tex:7208-7225`, in the tuple for the hybrid certificate.
Replace

```tex
b_R,\,
```

with:

```tex
b_R^{\mathrm{geom}},\,m_R,\,
```

Location: `main.tex:7232-7255`.  Replace the single-map paragraph with:

```tex
\item \emph{Finite Hall stage, geometric elliptic degree, and trace
exponent.}
\(\mathcal C_{\sigma,S,\le R}\) is a supplied extension-closed finite
charge-support HN quotient of the candidate compact Hall category, under
the finite-type hypothesis \textup{[K3\(\times\)E-fin]}, with finite-type
charge substacks \(\mathfrak M_{\gamma,R}\), vanishing-cycle coefficients
\(\Phi_{\gamma,R}\), and orientation lines \(o_{\gamma,R}\).  The
geometric elliptic-degree map is
\[
b_R^{\mathrm{geom}}:
\Gamma_{\sigma,S}^{HN}(R)\longrightarrow\mathbb Z_{\ge0}.
\]
It determines local versus wrapped support.  The automorphic trace
exponent is
\[
m_R:=\operatorname{pr}_3\overline\Pi_X.
\]
It determines the \(s\)-power in the Igusa monomial.  Write
\[
\Gamma_R^{\mathrm{loc}}
=\{\alpha\mid b_R^{\mathrm{geom}}(\alpha)=0\},
\qquad
\Gamma_R^{\mathrm{wr}}
=\{\eta\mid b_R^{\mathrm{geom}}(\eta)>0\}.
\]
The ideal of height \(>R\) is already killed at this stage, and all
operations below are understood to be zero when their output has height
\(>R\).  The map \(b_R^{\mathrm{geom}}\) is additive on extensions that
remain in the quotient, while \(m_R\) is additive because the source
degree has already been normal-ordered:
\[
b_R^{\mathrm{geom}}(0)=0,\qquad
b_R^{\mathrm{geom}}(\gamma+\gamma')
=b_R^{\mathrm{geom}}(\gamma)+b_R^{\mathrm{geom}}(\gamma'),
\qquad
m_R(\gamma+\gamma')=m_R(\gamma)+m_R(\gamma')
\]
whenever \(\gamma,\gamma',\gamma+\gamma'\in
\Gamma_{\sigma,S}^{HN}(R)\).
```

Reason: Agent53 identifies this as the central degree firewall.  Use
\(b_R^{\mathrm{geom}}\) only for local/wrapped color; use \(m_R\) only for
automorphic \(s\)-exponent.

### Patch 7 -- repair \(\delta_2\) degree statements

Location: `main.tex:6253-6254`.  Replace:

```tex
one has \(b_R(\delta_1)=b_R(\delta_3)=0\) and
\(b_R(\delta_2)=1\).
```

with:

```tex
one has \(m_R(\delta_1)=m_R(\delta_3)=0\) and
\(m_R(\delta_2)=1\).  The middle wall must have
\(b_R^{\mathrm{geom}}(\delta_2)>0\); in the rank-one
D6--D2--D0 curve-degree dictionary, \(b_R^{\mathrm{geom}}(\delta_2)=2\).
```

Location: `main.tex:8287-8289`.  Replace:

```tex
x_{\delta_2,R}\in\mathcal M_{\eta,R}^{\mathrm{wr,rig}},\qquad
\overline\Pi_X(x_{\delta_2,R})=(0,1,1),\qquad b_R(\eta)=1,
```

with:

```tex
x_{\delta_2,R}\in\mathcal M_{\eta,R}^{\mathrm{wr,rig}},\qquad
\overline\Pi_X(x_{\delta_2,R})=(0,1,1),\qquad
m_R(\eta)=1,\qquad b_R^{\mathrm{geom}}(\eta)>0,
```

Location: `main.tex:11069-11072`.  Replace:

```tex
b_R(\eta_2)=1,\qquad \overline\Pi_X(\eta_2)=(0,1,1),
```

with:

```tex
m_R(\eta_2)=1,\qquad b_R^{\mathrm{geom}}(\eta_2)>0,\qquad
\overline\Pi_X(\eta_2)=(0,1,1),
```

Reason: prevents the trace exponent from being read as geometric elliptic
degree.

### Patch 8 -- repair protected integration exponents

Location: `main.tex:7764-7781`.  Replace the sentence

```tex
... every nonzero monomial in
\(I_R^{\mathrm{prot}}(Q_{E,R}x)\) has \(s\)-degree \(b_R(\gamma)\):
```

with:

```tex
... every nonzero monomial in
\(I_R^{\mathrm{prot}}(Q_{E,R}x)\) has \(s\)-degree \(m_R(\gamma)\):
```

After `main.tex:7777-7781`, add:

```tex
The wrapped colour is controlled by \(b_R^{\mathrm{geom}}\); the
automorphic monomial is controlled by \(m_R\).  On the rank-one
D6--D2--D0 branch, \(m_R=b_R^{\mathrm{geom}}-1\).
```

Location: `main.tex:7788-7795`.  Replace:

```tex
For products, the displayed character law and additivity of \(b_R\) give
\[
s^{b_R(\gamma_1+\cdots+\gamma_k)}
=
\prod_i s^{b_R(\gamma_i)}
\]
```

with:

```tex
For products, the displayed character law and additivity of \(m_R\) give
\[
s^{m_R(\gamma_1+\cdots+\gamma_k)}
=
\prod_i s^{m_R(\gamma_i)}
\]
```

Location: `main.tex:7816`.  Replace:

```tex
The coefficient of a monomial \(q^nr^ls^{b_R(\gamma)}\) is a protected
```

with:

```tex
The coefficient of a monomial \(q^nr^ls^{m_R(\gamma)}\) is a protected
```

Location: `main.tex:8104-8112`.  Replace:

```tex
I_R^{\mathrm{prot}}(x)\in
s^{b_R(\gamma)}\C[q^{\pm1},r^{\pm1}],
...
because \(b_R\) is additive inside the finite quotient.
```

with:

```tex
I_R^{\mathrm{prot}}(x)\in
s^{m_R(\gamma)}\C[q^{\pm1},r^{\pm1}],
...
because \(m_R\) is additive inside the normal-ordered finite quotient.
```

Location: `main.tex:7902-7908`.  Keep this about geometric degree but
rename:

```tex
b_R^{\mathrm{geom}}(\gamma)=b_{R'}^{\mathrm{geom}}(\gamma').
```

Reason: this keeps \(s\)-degree and wrapped support from being identified.

### Patch 9 -- warn against colored-PROP associativity as geometric proof

Location: after `main.tex:7646-7650`.

Add:

```tex
Degree-label associativity in a universal colored PROP is not this axiom.
The axiom is equality of the two geometric pull-push operations induced by
the supplied two-step flag stack, after vanishing cycles,
Thom--Sebastiani transport, orientation signs, finite HN quotienting, and
the reduced \(E\)-quotient comparison maps.
```

Reason: latest PDF lines `29208-29217` prove only color-label
associativity.

### Patch 10 -- final-summary firewall

Location: after `main.tex:14251-14255`.

Add:

```tex
A finite Borcherds--Kac target reference tower may package the imported
denominator algebra, PBW basis, invariant form, radical quotient, and
finite product normalization.  It does not change the status of the
compact realization problem: the source-side Hall geometry, orientation,
hybrid correspondences, source coalgebra, primitive representatives, Hopf
pairing, radical quotient, PBW comparison, and Pfaffian line still have to
be supplied independently.
```

Reason: final reader-visible summary should block the UDI-as-source
interpretation.

## Optional algebraic Dirac block wording

If the main thread wants to keep the PDF's \(D_\gamma\) construction, put
it only under the target reference tower, not in the compact source
section:

```tex
\begin{definition}[Finite algebraic target Dirac block]
\label{def:finite-algebraic-target-dirac-block}
Fix a finite target window \(A_R\).  For each
\(\gamma=(n,l,m)\in A_R\), choose a finite super vector space
\(V_\gamma^{\mathrm{tar}}\) with
\[
\sdim V_\gamma^{\mathrm{tar}}
=\smult\mathfrak g_{\Delta_5,\alpha(\gamma)}
=f(nm,l),
\qquad
x^\gamma=q^nr^ls^m.
\]
Set
\[
K_\gamma^{\mathrm{tar}}
:=V_\gamma^{\mathrm{tar}}\oplus
\Pi(V_\gamma^{\mathrm{tar}})^\vee .
\]
Define the odd algebraic block
\[
D_\gamma^{\mathrm{tar}}
=
\begin{pmatrix}
0&1-x^\gamma\\
1&0
\end{pmatrix},
\qquad
(D_\gamma^{\mathrm{tar}})^2
=(1-x^\gamma)\operatorname{id}_{K_\gamma^{\mathrm{tar}}}.
\]
After a stated finite algebraic super-Pfaffian convention, put
\[
\operatorname{sPf}^{\mathrm{tar}}_R(D)
:=\prod_{\gamma\in A_R}(1-x^\gamma)^{
\sdim V_\gamma^{\mathrm{tar}}}.
\]
This is a target algebraic block model for the Borcherds product.  It is
not an analytic Dirac operator, not a compact Hall state space, and not a
geometric Pfaffian line.
\end{definition}
```

Do not include the PDF's
\[
D_R=\bigoplus_{\gamma\in A_R}D_\gamma\otimes\operatorname{id}_{V_\gamma}
\]
unless a separate convention proves that this does not double-count
multiplicity.  The safer block is already indexed by \(V_\gamma\).

## Forbidden claims

The following claims should be grep-blocked from any patch:

- `universal finite Hall--Dirac source` for an object defined from
  \(\mathfrak g_{\Delta_5}\) or \(U(\mathfrak g_{\Delta_5})\).
- `constructed finite compact source object`.
- `compact K3\times E source is no longer an assumption`.
- `geometry must realize UDI, not invent it` unless `UDI` is renamed
  target reference and the sentence says geometry remains the source
  construction problem.
- `H_R=U(\mathfrak g_{\Delta_5})_{\le R}` is a Hall state object/source.
- `P_R=p_R` is a source primitive theorem.
- `the radical quotient is already taken` as a source statement.
- `PBW monomials give a basis` without saying target PBW or without a
  source PBW comparison.
- `NO1--NO7 hold` for the target-built tower.
- `Hyb_R` is an actual finite hybrid local/wrapped source.
- eight diagrams commute because degree addition and \(AJ_R\) are
  homomorphisms.
- `C_R=B_E^{ch}(F_R)` is the source coalgebra when \(F_R\) takes values
  \(V_\gamma=\mathfrak g_{\Delta_5,\gamma}\).
- the determinant or \(\Delta_5\) determines full parity dimensions.
- the minimal parity lift is forced by the determinant.
- the algebraic \(D_\gamma\) block is an analytic Dirac operator.
- the target super-Pfaffian is a compact source Pfaffian.
- OP/DT constructs the square root or fixes orientation.
- `64`, `4096`, or the OP minus sign fixes the Pfaffian orientation.
- \(b_R\) used simultaneously for geometric elliptic degree and Igusa
  \(s\)-exponent.

## Required safe names

Use:

- `Borcherds--Kac target reference tower`
- `target PBW tower`
- `finite algebraic target block`
- `target comparison PROP`
- `source realization functor into the target reference tower`
- `compact realization problem`

Avoid:

- `UDI_R` unless decorated as `\mathrm{UDI}^{\mathrm{tar}}_R`
- `universal compact source`
- `finite Hall--Dirac source`
- `constructed compact source object`
- `source coalgebra` for a bar construction on target values

## Residual obligations

After these patches, the manuscript still has the same hard source theorem:

\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}
\]

must be proved from independent compact source data: geometric Hall
representatives, protected bracket constants, positive-negative Hopf
pairing matrices, radical kernels stable as Lie ideals and coideals,
finite PBW comparisons, no-extra-relations, exact completion, full parity
dimensions, hybrid local/wrapped correspondences, source coalgebra, and a
geometric Pfaffian line.  The target reference tower organizes the target;
it does not supply any of those source objects.

## Verification needed after main-thread patch

Run at minimum:

```bash
rg -n "universal finite Hall|constructed finite compact|compact source is no longer|H_R=U\\(|Hyb_R.*actual|radical quotient is already taken|NO1--NO7 hold|b_R\\([^)]*\\).*s\\^|s\\^\\{?b_R|OP.*orientation|4096.*orientation|64.*orientation" main.tex
make
```

Expected result: no forbidden source-overclaim hits except in explicit
negative/warning contexts; `make` succeeds.
