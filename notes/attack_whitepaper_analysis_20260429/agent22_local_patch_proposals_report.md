# Agent 22 Local Patch Proposals Report

Date: 2026-04-29

Scope: proposals only. No patches were applied to `main.tex`, `proj.bib`, or
existing manuscript source.

Inputs consolidated:

- `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`.
- Reports present at consolidation time: `agent01` through `agent17`,
  including `agent11`. Reports `agent18` through `agent21` were not present.

This queue is restricted to low-risk, high-value local repairs that can be
made without a full manuscript rewrite. Patch IDs below are meant to be copied
into the main patching pass.

## Patch priority tiers

### P0 -- mechanical correctness and local mathematical hygiene

These should be applied first. They fix undefined notation, unsafe cochain
language, domain mismatches, and displays that currently say more than the
paper can justify.

1. **P0-A: Replace undefined `\Gamma_{\mathrm{eff}}^+`.**
   Anchor: `main.tex:1954`.
   Intent: remove the undefined plus notation; use the already-defined
   effective cone notation.

2. **P0-B: Put the radical quotient into the first primitive-recognition
   display.**
   Anchors: `main.tex:286-291`.
   Intent: the prose says "modulo radical" but the display omits the quotient.

3. **P0-C: Replace `H^2_{\mathrm{sym}}` language by explicit additive
   cochain language.**
   Anchors: `main.tex:4366-4368`, `main.tex:4811-4830`.
   Intent: avoid implying a nonstandard symmetric cohomology theory carries the
   obstruction.

4. **P0-D: Separate raw placement `i_0(c)=(c,0)` from the split section
   `s(c)=(c,\Pi_X(c))`.**
   Anchors: `main.tex:4672-4682`.
   Intent: prevent the paper from saying the physical one-particle generator
   is placed by the normal-ordering split.

5. **P0-E: Add the normal-ordering flag formula.**
   Anchor: insert after `main.tex:4881`, before `main.tex:4883`.
   Intent: make the failure of raw pushforward concrete and local.

6. **P0-F: Define raw homogeneous and strict fixed-lift pushforwards before
   the no-go theorem.**
   Anchor: insert before `main.tex:4883`; retitle theorem at
   `main.tex:4883-4884`.
   Intent: the theorem currently uses "raw pushforward" before defining the
   object it rules out.

7. **P0-G: Replace denominator-comparison language that says the grading is
   "well defined modulo the cocycle `B`".**
   Anchors: `main.tex:5678-5690`.
   Intent: compare additive gradings through `\overline\Pi_X`; do not treat
   the quadratic raw map as a bracket-recognition target.

8. **P0-H: Repair open cochain equations.**
   Anchors: `main.tex:8305-8346`.
   Intent: distinguish ordinary `\Gamma_{\mathrm{gram}}`-valued cochains from
   Picard/line-valued cochains.

9. **P0-I: Repair NO3 quantifiers.**
   Anchors: `main.tex:9192-9199`.
   Intent: do not evaluate the physical character cocycle on
   normal-ordered labels.

10. **P0-J: Clarify D0-N normal-ordered character language.**
    Anchors: `main.tex:10501-10516`.
    Intent: say whether the displayed degree shift is a physical cochain plus
    `T`-record bookkeeping, or a normal-ordered character with zero boundary.

11. **P0-K: Fix grammar "Orientation data enters".**
    Anchor: `main.tex:2519-2520`.
    Intent: mechanical grammar repair.

### P1 -- theorem/status names and theorem-scope repairs

Apply after P0 because these rely on the corrected notation and cochain
vocabulary.

1. **P1-A: Rename the one-particle section.**
   Anchor: `main.tex:640`.
   Intent: stop calling the virtual Borcherds package a literal one-particle
   index.

2. **P1-B: Convert the Dirac/Pfaffian recognition "proposition" into an open
   problem or definition.**
   Anchors: `main.tex:882-918`.
   Intent: avoid presenting the first-order Dirac object as constructed.

3. **P1-C: Rename the Borcherds/Gritsenko--Nikulin proposition.**
   Anchor: `main.tex:2530`.
   Intent: state exactly what is proved: a normalized `K_0`-determinant form
   imported from Gritsenko--Nikulin, not a new construction of the algebra.

4. **P1-D: Promote and clean the D6--D2--D0 Mukai--Gram dictionary.**
   Anchors: `main.tex:2661-2755`, with a dependent variable-note patch near
   `main.tex:13714-13721`.
   Intent: make the dictionary theorem precise, define the Mukai pairing before
   using it, and separate geometric elliptic degree from the Borcherds/Gram
   exponent.

5. **P1-E: Add a forbidden-implication box after the opening status tables.**
   Anchor: after `main.tex:453`.
   Intent: explicitly block the common false arrows identified by agents 01,
   04, 06, 10, 13, and 17.

6. **P1-F: Add OP scalar-square warning near the OP/DT comparison.**
   Anchors: `main.tex:13701-13955`.
   Intent: OP/DT sees a scalar square such as `D_5^2`; it does not construct
   `D_5`, a Pfaffian, or an orientation sign.

7. **P1-G: Add row/spin independence disclaimers and soften the part title.**
   Anchors: `main.tex:14267-14278`, `main.tex:14558-14686`.
   Intent: prevent the eight-row and spin-normalization material from being
   read as part of the N=1 Dirac--Igusa proof.

### P2 -- local clarity patches with moderate coupling

These are still local, but they touch prose that other agents may be actively
editing. Apply after checking the current working copy.

1. **P2-A: Minimal title/abstract repair.**
   Anchors: `main.tex:7`, `main.tex:57-172`.
   Intent: keep the title; compress and qualify the abstract so it says
   "arbitrary Grothendieck representatives", "imported GN denominator input",
   "open Dirac--Igusa problem", and "raw homogeneous fixed-lift pushforward".

2. **P2-B: Rename/alias the formal current envelope as a curve-formal target.**
   Anchors: `main.tex:5724-5768`.
   Intent: do not imply the compact Hall source has already supplied a
   holomorphic `E_3` factorization algebra.

3. **P2-C: Fix the QME "or" display by choosing one BV convention.**
   Anchors: `main.tex:6091-6099`.
   Intent: remove the impression that two different equations are equivalent
   without a convention choice.

4. **P2-D: Repair the hybrid `b_R` / `m_R` degree convention if the D6 note is
   adopted.**
   Anchors: `main.tex:7048-7056`, `main.tex:7683-7697`,
   `main.tex:13714-13721`.
   Intent: geometric elliptic degree and Borcherds exponent differ by one on
   the D6 rank-one OP branch.

## Exact main.tex anchors

| Patch ID | Exact anchors | Current local issue |
|---|---:|---|
| P0-A | `main.tex:1954` | Undefined `\Gamma_{\mathrm{eff}}^+`. |
| P0-B | `main.tex:286-291` | Prose says radical quotient; display omits it. |
| P0-C | `main.tex:4366-4368`, `main.tex:4811-4830` | Unsafe `H^2_{\mathrm{sym}}` / cohomology-class wording. |
| P0-D | `main.tex:4672-4682` | Split section `s` can be mistaken for raw physical placement. |
| P0-E | after `main.tex:4881` | No displayed flag formula for multiplying raw lifts. |
| P0-F | before and at `main.tex:4883-4884` | Raw homogeneous/fixed-lift pushforward not defined before no-go theorem. |
| P0-G | `main.tex:5678-5690` | Denominator comparison is described as grading modulo `B`. |
| P0-H | `main.tex:8305-8346` | Ordinary and Picard cochain equations are conflated. |
| P0-I | `main.tex:9192-9199` | `B_{\mathrm{ch},R}` is evaluated on the wrong domain. |
| P0-J | `main.tex:10501-10516` | D0-N mixes physical character cochain and normal-ordered labels. |
| P0-K | `main.tex:2519-2520` | Grammar: "Orientation data enters". |
| P1-A | `main.tex:640` | Section title overstates "one-particle index". |
| P1-B | `main.tex:882-918` | Open target is typed as a proposition. |
| P1-C | `main.tex:2530` | Theorem name overclaims Borcherds--GN identification. |
| P1-D | `main.tex:2661-2755`, `main.tex:13714-13721` | D6 dictionary needs theorem status, Mukai-pairing setup, and degree convention. |
| P1-E | after `main.tex:453` | False implication warnings are scattered rather than boxed. |
| P1-F | `main.tex:13701-13955` | OP scalar-square result can be misread as square-root/orientation data. |
| P1-G | `main.tex:14267-14278`, `main.tex:14558-14686` | Row/spin material needs explicit independence status. |
| P2-A | `main.tex:7`, `main.tex:57-172` | Abstract still overcompresses source/target distinctions. |
| P2-B | `main.tex:5724-5768` | `E`-specific current envelope reads as compact Hall source. |
| P2-C | `main.tex:6091-6099` | QME display presents an unqualified "or". |
| P2-D | `main.tex:7048-7056`, `main.tex:7683-7697`, `main.tex:13714-13721` | Potential off-by-one between elliptic degree `d` and Gram exponent `m=d-1`. |

## Proposed replacement language/formulas

### P0-A -- undefined effective cone plus

At `main.tex:1954`, replace

```tex
\Gamma_{\mathrm{eff}}^+
```

with

```tex
\Gamma_{\mathrm{eff}}
```

unless the main patcher first adds a local definition of the plus notation.
The low-risk choice is to remove the plus.

### P0-B -- opening radical quotient

At `main.tex:286-291`, replace the displayed recognition line by:

```tex
\[
H^0\Prim_{\mathrm{prot}}\!\left(\overline\Pi_{X,*}^{\Theta}\mathcal F_X\right)
/
\overline{\operatorname{Rad}\langle\cdot,\cdot\rangle_X}
\;\cong\;
\mathfrak g_{\Delta_5}.
\]
```

If the local notation already defines a reduced primitive object, the shorter
version is acceptable:

```tex
\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}.
\]
```

but only if `P_X^{\Pi,\mathrm{red}}` is defined immediately before the display.

### P0-C -- cochain language replacing `H^2_{\mathrm{sym}}`

At `main.tex:4366-4368`, replace the cohomology-class sentence with:

```tex
As an ordinary additive two-cocycle, \(B\) is a coboundary once quadratic
cochains are allowed:
\[
  B=-\delta\Pi_X,\qquad
  (\delta q)(c,c')=q(c)+q(c')-q(c+c').
\]
The obstruction used below is therefore not a nonzero ordinary cohomology
class. It is the absence of an additive linear trivialization compatible with
the physical grading and bracket channels.
```

At `main.tex:4811-4830`, replace the remark by:

```tex
\begin{remark}[What the cocycle obstruction is not]
The ordinary additive cocycle class of \(B\) vanishes after allowing the
quadratic cochain \(-\Pi_X\):
\[
  d_{\mathrm{Hoch}}(-\Pi_X)=B .
\]
The no-go statement in this section is not a claim that \(B\) defines a
nonzero ordinary class in a symmetric group cohomology theory. It says that
the raw physical grading \(c\mapsto\Pi_X(c)\) is quadratic, while bracket
recognition requires an additive grading target. Normal ordering records the
defect in the second coordinate of \(\widehat\Gamma_X\); raw fixed-lift
pushforward forgets precisely that record.
\end{remark}
```

### P0-D -- raw placement versus split section

At `main.tex:4672-4682`, add the raw placement before the split section and
adjust the prose to:

```tex
There are two maps from the physical charge group into
\(\widehat\Gamma_X\) which must not be confused:
\[
  i_0(c):=(c,0),\qquad s(c):=(c,\Pi_X(c)).
\]
The map \(i_0\) is the raw one-particle Hall placement. It is not a group
homomorphism for the normal-ordered law unless \(B\equiv0\). The map \(s\) is
the split additive section; it is a group homomorphism and satisfies
\[
  \overline\Pi_X(i_0(c))=\Pi_X(c),\qquad
  \overline\Pi_X(s(c))=0.
\]
Thus the split section is useful for proving the extension is split as an
abstract abelian group, but it is not the raw physical placement used by the
one-particle bracket.
```

### P0-E -- normal-ordering flag formula

Insert after `main.tex:4881`:

```tex
\begin{lemma}[Normal-ordering flag formula]
For physical charges \(c_1,\ldots,c_k\), multiplication of raw lifts in
\(\widehat\Gamma_X\) gives
\[
  i_0(c_1)\star\cdots\star i_0(c_k)
  =
  \left(\sum_i c_i,\ \sum_{i<j} B(c_i,c_j)\right).
\]
Consequently
\[
  \overline\Pi_X\!\left(i_0(c_1)\star\cdots\star i_0(c_k)\right)
  =
  \sum_i \Pi_X(c_i).
\]
\end{lemma}
```

If the group law is written additively rather than with `\star` in the local
section, use the existing local multiplication symbol. The formula itself
should not be weakened.

### P0-F -- raw homogeneous and fixed-lift pushforward definition

Insert before `main.tex:4883`:

```tex
\begin{definition}[Raw homogeneous and fixed-lift \(\Pi_X\)-pushforward]
Let \(P=\bigoplus_{c\in\Gamma_X^{\mathrm{form}}}P_c\) be a physically graded
primitive object. The raw homogeneous \(\Pi_X\)-pushforward attempts to grade
by the quadratic value alone:
\[
  \left(\Pi_{X,*}^{\mathrm{raw}}P\right)_\gamma
  :=
  \bigoplus_{\Pi_X(c)=\gamma} P_c .
\]
It carries no \(T\)-label and no normal-ordering record. A strict fixed-lift
raw pushforward is the still narrower operation obtained by choosing one lift
\(L(\gamma)\) for each retained \(\gamma\) and setting
\[
  \left(\Pi_{X,*}^{\mathrm{raw},L}P\right)_\gamma := P_{L(\gamma)} .
\]
\end{definition}
```

Then retitle the theorem at `main.tex:4883-4884` to:

```tex
\begin{theorem}[Raw homogeneous fixed-lift \(\Pi_X\)-pushforward cannot realize the type-II real-root strings]
```

### P0-G -- denominator comparison

At `main.tex:5678-5690`, replace the grading-comparison paragraph with:

```tex
The denominator algebra is additively graded by
\(\Gamma_{\mathrm{ind}}\cong\mathbb Z^3\) and by its Lorentzian image. A Hall
source is additively graded upstairs by \(\Gamma_X^{\mathrm{form}}\), or after
normal ordering by \(\widehat\Gamma_X\). The comparison with the denominator
grading is made by the additive map
\(\overline\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}\). The raw
quadratic map \(\Pi_X\) is not itself a bracket-recognition target unless all
visible bracket channels are \(B\)-isotropic.
```

### P0-H -- open cochain equations

At `main.tex:8305-8346`, replace the mixed equations by the two-level
statement:

```tex
At the level of ordinary \(\Gamma_{\mathrm{gram}}\)-valued cochains, the
quadratic cochain \(-\Pi_X\) satisfies
\[
  d_{\mathrm{Hoch}}(-\Pi_X)=B .
\]
The geometric orientation problem is different. It asks for a Picard- or
line-valued cochain \(\Theta_\Pi\) whose boundary is the character-valued
bracket defect:
\[
  d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}} .
\]
The first identity is formal normal ordering; the second is orientation data.
Neither identity constructs the other.
```

### P0-I -- NO3 quantifier repair

At `main.tex:9192-9199`, use the physical-label version:

```tex
\item[(NO3)] For every finite physical charge pair
\(c,c'\in\Gamma_X^{\mathrm{form}}\) whose \(T\)-recorded bracket channels
occur at height \(R^+\), the finite character cochain satisfies
\[
  d_{\mathrm{Hoch}}\Theta_{\Pi,R}^{\mathrm{phys}}(c,c')
  =
  B_{\mathrm{ch},R}(c,c') .
\]
Equivalently, after passing to normal-ordered labels one uses the character
\[
  \widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)},
\]
whose Hochschild boundary is zero on \(\widehat\Gamma_{R^+}\).
```

This avoids evaluating `B_{\mathrm{ch},R}` on normal-ordered labels.

### P0-J -- D0-N normal-ordered character language

Before the display at `main.tex:10509`, insert:

```tex
On normal-ordered labels the corresponding character is
\[
  \widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)},
\]
so \(d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0\). The following two-variable
display is the induced bookkeeping shift coming from the physical cochain
together with the recorded \(T,T'\)-labels.
```

If this makes the existing display redundant, delete the redundant display
rather than keeping two inconsistent formulas.

### P0-K -- grammar

At `main.tex:2519-2520`, replace:

```tex
Orientation data enters later
```

with either:

```tex
Orientation data enter later
```

or:

```tex
The orientation datum enters later
```

Prefer the second if the surrounding paragraph treats orientation as one
chosen object.

### P1-A -- section title

At `main.tex:640`, replace:

```tex
\section{The one-particle index and its determinant}
```

with:

```tex
\section{Virtual Borcherds package and the \(K_0\)-determinant}
```

No label change is required.

### P1-B -- Dirac/Pfaffian target status

At `main.tex:882`, replace:

```tex
\begin{proposition}[Dirac/Pfaffian recognition target]
```

with:

```tex
\begin{openproblem}[Dirac--Pfaffian recognition target]
```

and change the matching `\end{proposition}` at `main.tex:918` to
`\end{openproblem}`. If the manuscript has no `openproblem` environment,
use:

```tex
\begin{definition}[Dirac--Pfaffian recognition target]
```

and explicitly begin the text with:

```tex
The open target is the construction of ...
```

### P1-C -- GN theorem name

At `main.tex:2530`, replace the proposition title with:

```tex
\begin{proposition}[Normalized \(K_0\)-determinant form of the Gritsenko--Nikulin product]
```

Add one sentence after the statement if not already present:

```tex
The denominator algebra and product input are imported from the
Gritsenko--Nikulin theorem; the local assertion is the normalized
\(K_0\)-determinant realization of that input.
```

Do not introduce a new source citation unless the bibliography key is already
known and verified.

### P1-D -- D6--D2--D0 Mukai--Gram dictionary

At `main.tex:2661`, replace:

```tex
\begin{lemma}[D6--D2--D0 Mukai--Gram dictionary]
```

with:

```tex
\begin{theorem}[D6--D2--D0 Mukai--Gram dictionary]
```

and change the matching `\end{lemma}` to `\end{theorem}`.

Near `main.tex:2671-2674`, define the K3 Mukai lattice before using the Gram
triple:

```tex
Let
\[
  \Lambda_S:=\widetilde H(S,\mathbb Z)
  =H^0(S,\mathbb Z)\oplus H^2(S,\mathbb Z)\oplus H^4(S,\mathbb Z)
\]
with Mukai pairing
\[
  \langle (r,\ell,s),(r',\ell',s')\rangle
  =
  \ell\cdot\ell' - rs' - r's .
\]
For the rank-one D6--D2--D0 vector \(v=(1,\ell,n)\), the associated Gram data
are ...
```

Keep the existing local formula if its signs match this convention; otherwise
make the sign convention explicit in the theorem.

At `main.tex:2752-2755`, replace language saying the triple is "in the Mukai
lattice of \(X\)" with:

```tex
Thus the D6--D2--D0 data determine the Gram-index triple of the two K3 Mukai
components. The dictionary is a comparison of Gram data, not an assertion that
the triple itself is an element of a Mukai lattice of \(X\).
```

Near the OP table at `main.tex:13714-13721`, add:

```tex
Here \(d\) denotes the geometric elliptic degree. The Borcherds/Gram exponent
is \(m=d-1\), while the D0/Fourier index is \(n=\chi(\mathcal O_Y)\).
```

### P1-E -- forbidden implication box

Insert after the opening status tables, preferably after `main.tex:453`:

```tex
\begin{center}
\fbox{\begin{minipage}{0.92\linewidth}
\textbf{Forbidden implications used in this paper.}
\[
\begin{array}{rcl}
  \mathcal D_X=\Delta_5 &\not\Rightarrow& \text{a constructed Dirac operator }\mathfrak D_X,\\
  \Delta_5^2\text{ in OP/DT} &\not\Rightarrow& \text{an orientation sign or a Pfaffian square root},\\
  \mathfrak g_{\Delta_5} &\not\Rightarrow& \text{a compact Hall/factorization source},\\
  \Gamma_{\mathrm{gram}} &\neq& \text{the Hall charge lattice}.
\end{array}
\]
\end{minipage}}
\end{center}
```

If the manuscript already has a status-box environment, use it instead of
manual `\fbox`.

### P1-F -- OP scalar-square warning

Near the OP/DT comparison at `main.tex:13701-13955`, add:

```tex
\begin{remark}[Scalar square only]
The OP/DT comparison detects the scalar square, equivalently the
\(\Delta_5^2\) or \(D_5^2\) normalization depending on convention. It does
not construct a first-order square root, a Pfaffian line, or an orientation
sign. Those data belong to the separate Dirac/orientation problem.
\end{remark}
```

If the forbidden implication box P1-E is added, this remark can be shorter,
but it should remain local to the OP discussion because readers may enter the
paper at that theorem.

### P1-G -- row/spin independence

At `main.tex:14267`, replace:

```tex
\part{Diagonal-divisor rows and CHL boundary physics}
```

with:

```tex
\part{Diagonal-divisor rows and denominator certificates}
```

At `main.tex:14269-14278`, add before the first paragraph:

```tex
This part is independent of the N=1 Dirac--Igusa recognition target in the
preceding parts. It records row certificates and boundary-normalization
evidence for the denominator package; it is not used as a construction of the
compact Hall source or of the Dirac/Pfaffian square root.
```

At the beginning of the spin-normalization section around `main.tex:14558`,
add:

```tex
The spin-normalization calculation below is an independent arithmetic
normalization check. It does not identify the Hall source and does not supply
orientation data for the Dirac target.
```

### P2-A -- minimal title/abstract repair

At `main.tex:7`, do not change the title unless the principal specifically
requests it. The current title is acceptable because it frames the object as a
realization problem rather than a completed operator construction.

In `main.tex:57-172`, make only local replacements:

1. Replace the opening "For \(X=K3\times E\)" sentence by:

```tex
For a K3 surface \(S\), the Gritsenko--Nikulin Borcherds product supplies the
Igusa cusp form \(\Delta_5\), whose square is \(\chi_{10}\). For
\(X=S\times E\), this paper formulates the realization problem of recovering
that square root from protected compact Donaldson--Thomas/Hall data.
```

2. Replace "For virtual super vector spaces..." by:

```tex
For arbitrary Grothendieck representatives of virtual super vector spaces, the
Berezinian determinant is not determined by the superdimension alone. We
therefore work with a normalized \(K_0\)-determinant package rather than a
literal one-particle Hilbert space.
```

3. Replace the "same coefficients are signed root multiplicities" paragraph by:

```tex
The arithmetic Borcherds input imported from Gritsenko--Nikulin supplies
positive signed root supermultiplicities on the active support of the
denominator product. This is a target denominator package, not a construction
of the compact Hall source.
```

4. Replace any abstract claim that the paper constructs `\mathfrak D_X` by:

```tex
The open Dirac--Igusa problem is to construct a first-order object
\(\mathfrak D_X\) whose determinant/Pfaffian package realizes this scalar
square-root normalization.
```

5. Replace "strict fixed-lift raw Gram descent" by:

```tex
strict fixed-lift raw homogeneous \(\Pi_X\)-pushforward
```

6. Remove or soften any abstract sentence saying the row or spin material
proves the N=1 recognition theorem. Use:

```tex
The diagonal-row and spin-normalization sections are independent arithmetic
checks on the denominator package.
```

### P2-B -- curve-formal current envelope

At `main.tex:5724-5768`, prefer an alias rather than a global rename:

```tex
\begin{definition}[Curve-formal target current envelope]
For a smooth complex curve \(C\), define the curve-formal target current
envelope
\[
  \mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C}:=\cdots
\]
by the same completed-current construction below. For the compact geometry
\(X=S\times E\), we write
\[
  \mathsf{Den}_{\Delta_5,E}:=\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,E}.
\]
This is a target envelope. It is not a claim that a compact Hall or
factorization source on \(E\) has already been constructed.
\end{definition}
```

The placeholder `\cdots` must be replaced by the existing definition body, not
left in the manuscript.

### P2-C -- QME display convention

At `main.tex:6091-6099`, replace the two-equation "or" display by one
convention:

```tex
d_R S_R+\frac12\{S_R,S_R\}_R+\hbar\Delta_R^{\mathrm{BV}}S_R
=\omega_{\mathrm{QME},R}.
```

Then add:

```tex
The classical master equation is the specialization obtained by setting
\(\hbar=0\). A different sign convention for the BV Laplacian changes this
display uniformly; it is not a second independent obstruction equation.
```

### P2-D -- `b_R` versus `m_R`

If P1-D adds the degree convention note, then repair the integration paragraph
at `main.tex:7683-7697` so the Gram/Borcherds exponent is not confused with
geometric elliptic degree:

```tex
Under this integration map, every nonzero monomial in the finite algebraic
model lands in the corresponding Borcherds monomial with \(s\)-degree
\(m_R(\gamma)\):
\[
  q^{a_R(\gamma)} r^{c_R(\gamma)} s^{m_R(\gamma)} .
\]
Here \(m_R\) denotes the Gram/Borcherds exponent recorded by
\(\overline\Pi_X(\gamma)=(a_R(\gamma),c_R(\gamma),m_R(\gamma))\). On the
rank-one D6--D2--D0 OP branch, \(m_R=d_R-1\), where \(d_R\) is the geometric
elliptic degree.
```

Do not change `main.tex:7048-7056` if it intentionally defines geometric
degree. The local fix is to use a different name for the Gram exponent in the
integration theorem.

## Risk level per patch

| Patch ID | Risk | Reason |
|---|---|---|
| P0-A | Low | Single undefined-symbol repair. |
| P0-B | Low | Matches existing prose and later radical-quotient section. |
| P0-C | Low | Replaces unsafe cohomology claim with explicit coboundary identity. |
| P0-D | Low | Clarifies maps already implicit in the normal-ordering section. |
| P0-E | Low | Direct consequence of the displayed group law. |
| P0-F | Low | Adds definitions needed by the immediately following theorem. |
| P0-G | Low | Removes overclaim; preserves comparison through `\overline\Pi_X`. |
| P0-H | Low | Separates formal normal ordering from orientation data. |
| P0-I | Low | Domain correction; avoids evaluating cochains on wrong labels. |
| P0-J | Low | Local explanatory repair in D0-N. |
| P0-K | Low | Grammar only. |
| P1-A | Low | Section title only; no labels affected. |
| P1-B | Medium-low | Environment change may require `openproblem` support; fallback is `definition`. |
| P1-C | Low | Theorem-title accuracy; no proof change. |
| P1-D | Medium | The theorem promotion is low-risk, but sign/degree convention must be checked. |
| P1-E | Low | Adds summary warning; no theorem dependency. |
| P1-F | Low | Local warning consistent with OP/DT content. |
| P1-G | Low | Independence disclaimer and part-title softening. |
| P2-A | Medium | Abstract is visible and may be edited by other agents; merge carefully. |
| P2-B | Medium | Adds an alias around a symbol that may have many references. |
| P2-C | Medium-low | Requires one BV convention choice; formula itself is local. |
| P2-D | Medium | Degree convention touches multiple later formulas; apply only after P1-D. |

## Dependencies between patches

- **P0-C before P0-H, P0-I, P0-J.** The cochain vocabulary should be fixed
  before repairing later finite and open conditions.
- **P0-D and P0-E before P0-F.** The raw placement and flag formula motivate
  the raw/fixed-lift pushforward definition and theorem.
- **P0-F before P2-A.** The abstract should use the exact phrase introduced in
  the body: "raw homogeneous fixed-lift \(\Pi_X\)-pushforward".
- **P1-D before P2-D.** Do not patch `b_R`/`m_R` until the D6 dictionary states
  the `d` versus `m=d-1` convention.
- **P1-E before P1-F and P1-G if possible.** The forbidden implication box
  gives a global place to point local warnings.
- **P1-B and P2-A should be coordinated.** The abstract should not call the
  Dirac/Pfaffian target constructed if the body marks it as open.
- **P2-B and P2-C should be coordinated with any factorization/Hall-source
  edits.** They both affect the source-versus-target distinction.

## What not to patch yet

Do not attempt these in the local patch pass:

1. **Do not construct the full compact Hall/factorization source.** Reports
   agent06, agent15, and agent16 all identify this as nonlocal work requiring
   actual source objects, not a wording patch.

2. **Do not add full `H_{\mathrm{pre}}`, `H_{\mathrm{tw}}`, or
   `\mathcal D_{\mathrm{alg}}` constructions unless the objects are actually
   built.** The current manuscript can state targets and certificates; it
   should not fabricate source constructions.

3. **Do not move the row or spin sections in this pass.** Add independence
   disclaimers now; structural relocation can wait for an architecture pass.

4. **Do not rewrite the whole abstract or title.** Keep the title. Patch only
   sentences that overclaim source construction, one-particle status, raw
   descent, or row/spin dependence.

5. **Do not add new bibliography keys opportunistically.** Agent11 verified
   existing keys resolve and noted that some desired primary-source references
   may need care. Source enrichment should be a separate bib-aware patch.

6. **Do not claim OP/DT constructs orientation data.** OP/DT supplies the
   scalar square normalization; first-order square-root, Pfaffian, and
   orientation gerbe data remain separate.

7. **Do not collapse the Hall charge lattice into the Gram lattice.** The
   comparison is via `\Pi_X` or `\overline\Pi_X`; the source and target
   lattices are distinct.

8. **Do not use the split section `s(c)=(c,\Pi_X(c))` as the raw one-particle
   placement.** Raw physical generators are placed by `i_0(c)=(c,0)`.

9. **Do not introduce a global curve-universal current envelope if only an
   alias is needed.** The low-risk patch is to mark the existing envelope as a
   target and optionally alias the curve-formal version.

## Build/test plan after patches

After the main patching agent applies the queue, run:

```bash
make
python3 compute/verify_square_root.py
python3 compute/verify_lattice.py
```

Then run targeted textual checks:

```bash
rg -n '\\Gamma_\\{\\mathrm\\{eff\\}\\}\\^\\+' main.tex
rg -n 'well defined modulo the cocycle|modulo the cocycle \\$?B' main.tex
rg -n 'H\\^2_\\{\\mathrm\\{sym\\}\\}|symmetric group cohomology' main.tex
rg -n 'd_\\{\\mathrm\\{Hoch\\}\\}\\s*\\Theta_\\Pi\\s*=\\s*B(?!_\\{\\mathrm\\{ch\\}\\})' main.tex
rg -n 'Orientation data enters' main.tex
rg -n 'strict fixed-lift raw Gram descent|raw Gram descent' main.tex
rg -n '\\Gamma_\\{\\mathrm\\{gram\\}\\}\\s*=' main.tex
```

Manual post-build checks:

1. Confirm the PDF first pages show the forbidden-implication box without
   overfull layout damage.
2. Confirm the normal-ordering section displays `i_0`, `s`, and the flag
   formula before the raw-pushforward theorem.
3. Confirm the Dirac/Pfaffian target is not presented as a proved proposition.
4. Confirm OP/DT language says scalar square only.
5. Confirm row and spin sections carry independence disclaimers.
6. Confirm the D6 dictionary uses one sign convention consistently and states
   `m=d-1` only where the geometric-degree convention is in force.

Expected result: the manuscript should still compile, the two computation
scripts should still pass, and the local text should no longer expose the
specific low-risk attack surfaces listed in this report.
