# Reconstitution Architecture — The Igusa Square Root

Date: 2026-04-28.
Integration owner: main thread.

This note is the working architecture for reconstituting `main.tex` into
the strongest form currently supported by the mathematics.  It is an
internal planning document.  The external manuscript must remain
standalone: no process labels, no references to this note, no attack-log
language, no prior-draft language.

## Supremum Discipline

The governing rule is not maximal rhetoric.  It is maximal proof.

Every choice takes the harder mathematical road when that road produces
deeper understanding, sharper statements, or a stronger obstruction.
The manuscript must prefer:

- a proved theorem over an attractive assertion;
- an exact obstruction over a vague open problem;
- a first-principles derivation over a citation used as a black box;
- two independent verifications over one plausible argument;
- a conditional theorem with named hypotheses over a hidden existence
  claim;
- a structural no-go theorem over a defensive caveat;
- a real construction target over a recognition slogan.

False strength is rejected.  If a sentence sounds strong because it
forgets a hypothesis, it is weakened or split.  If a section is
mathematically true but does not serve the Dirac spine, it moves to an
appendix or companion ledger.

## Organizing Principle

The square root is Dirac, not analytic.

The scalar OP/DT branch is
\[
Z^X_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}.
\]
This is a second-order, orientation-forgetting scalar object.  The
first-order object sought by the paper is not a chosen branch of
\(\Delta_5^2\).  It is a protected Pfaffian / primitive algebra whose
determinant is \(\Delta_5\), with extra data that the scalar square
forgets:

\[
\text{orientation/Pfaffian line}
\quad+\quad
\text{primitive Hall bracket}
\quad+\quad
\text{normal-ordered Gram descent}
\quad+\quad
\text{hybrid local/wrapped factorization}.
\]

The paper must therefore be organized as:

\[
\text{local protected operations}
\to
\text{physical Mukai charges}
\to
\text{normal-ordered Gram descent}
\to
\text{BKM denominator target}
\to
\text{Pfaffian square root}
\to
\text{OP/DT scalar square}.
\]

The current automorphic determinant remains essential, but it is not the
main new mechanism.  The new mechanism is the normal-ordered descent
from additive physical charge to the Igusa/Borcherds Gram degree.

## The Central Mechanism

The core chain is
\[
\Gamma_X^{\mathrm{phys}}
\longrightarrow
\Gamma_X=\Gamma_X^{\mathrm{phys}}\oplus_B\Gamma_{\mathrm{gram}}
\xrightarrow{\ \overline\Pi\ }
\Gamma_{\mathrm{gram}}
\longrightarrow
\mathfrak g_{\Delta_5}
\quad\text{only after the finite Dirac--Igusa recognition certificate}.
\]

Here
\[
\Gamma_X^{\mathrm{phys}}=\Lambda_S\oplus\Lambda_S
\]
is the additive algebraic even Mukai sector relevant to the
D6--D2--D0 / OP branch, not the full \(N=4\) Narain charge lattice.
For \(c=(Q,P)\),
\[
\Pi(c)=\left(\frac{Q^2}{2},\,Q\cdot P,\,\frac{P^2}{2}\right)
\]
is the quadratic Gram map, and
\[
B(c,c')=
\bigl(Q\cdot Q',\;Q\cdot P'+Q'\cdot P,\;P\cdot P'\bigr)
\]
is the bilinear defect:
\[
\Pi(c+c')=\Pi(c)+\Pi(c')+B(c,c').
\]

The corrected extension is
\[
\Gamma_X=\Gamma_X^{\mathrm{phys}}\oplus_B\Gamma_{\mathrm{gram}},
\qquad
(c,T)\star(c',T')=(c+c',T+T'+B(c,c')).
\]
The normal-ordered Gram map is
\[
\overline\Pi(c,T)=\Pi(c)-T.
\]
It is a homomorphism:
\[
\overline\Pi((c,T)\star(c',T'))
=\overline\Pi(c,T)+\overline\Pi(c',T').
\]

This must become the visible mathematical center of the manuscript.
The chain-level \(\Theta\)-descent is then a categorification of this
degree-level normal ordering, not the first explanation of it.

## Surviving Theorem Spine

### A. Automorphic Square Root

Status: proved here from the formal determinant identity plus imported
Borcherds--Gritsenko--Nikulin product.

Statement:
\[
\mathcal D_X(Z)
=64q^{1/2}r^{1/2}s^{1/2}
\prod_{\Gamma_{\mathrm{eff}}}
(1-q^nr^ls^m)^{f(nm,l)}
=\Delta_5(Z).
\]

Proof routes:

1. Fock/superdeterminant identity from \(K_0(\mathrm{sVect})\).
2. Borcherds--Gritsenko--Nikulin product formula for
   \(\operatorname{Borch}_\theta(\phi_{0,1})\).
3. Direct coefficient check via `compute/verify_square_root.py` for
   the Jacobi coefficients used in the first product rows.

Boundary:
This is a virtual determinant.  It does not construct a compact Hilbert
space, an operator product, or a compact Hall bracket.

### B. D6--D2--D0 Mukai--Gram Dictionary

Status: must be proved in the manuscript as a central theorem, not a
side lemma.

For \(Y\subset S\times E\) one-dimensional, with
\[
[Y]=(\beta,d),\qquad \chi(\mathcal O_Y)=n,
\]
the ideal sheaf satisfies
\[
v_X(I_Y)
=(1,0,1-d)\otimes 1_E+(0,-\beta,-n)\otimes\omega_E.
\]
With
\[
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n),
\]
one gets
\[
\Pi(Q_Y,P_Y)=\left(\frac{\beta^2}{2},\,n,\,d-1\right).
\]
For \(\beta=\beta_h\), \(\beta_h^2=2h-2\), this is
\[
\Pi(Q_Y,P_Y)=(h-1,n,d-1).
\]

Proof routes:

1. Chern-character computation:
   \(\ch(I_Y)=1-\ch(\mathcal O_Y)\), with
   \(\ch_2(\mathcal O_Y)=\operatorname{PD}[Y]\) and
   \(\ch_3(\mathcal O_Y)=\chi(\mathcal O_Y)\) in the CY3 convention.
2. Kunneth decomposition against \(1_E,\omega_E\), using
   \(\td(E)=1\) and \(\sqrt{\td(S)}=(1,0,1)\) in Mukai notation.
3. Pairing check:
   \(Q_Y^2/2=\beta^2/2\), \(Q_Y\cdot P_Y=n\),
   \(P_Y^2/2=d-1\).

Required correction:
Remove every occurrence of "fourfold" and every vague "Todd correction"
from this lemma.  \(K3\times E\) is a Calabi--Yau threefold.

### C. Gram Cocycle and Normal-Ordered Extension

Status: proved lattice theorem.

Statements:

1. \(B\) is symmetric, bilinear, normalized, and satisfies the additive
   \(2\)-cocycle identity.
2. \(B(c,c)=2\Pi(c)\) is pure polarization.
3. \(\Gamma_X=\Gamma_X^{\mathrm{phys}}\oplus_B\Gamma_{\mathrm{gram}}\)
   is an abelian central extension.
4. \(\overline\Pi(c,T)=\Pi(c)-T\) is a homomorphism.
5. The extension is split by the quadratic section \(c\mapsto(c,\Pi(c))\),
   but not by a linear cochain.

Proof routes:

1. Direct expansion of quadratic terms.
2. Cocycle calculation \(\delta B=0\).
3. Associativity of \(\star\) from \(\delta B=0\).
4. Homomorphism calculation for \(\overline\Pi\).

Required correction:
Delete the Bott-periodicity explanation of \(B(c,c)=2\Pi(c)\).
Orientation and Bott/Pfaffian signs belong only in the orientation
section.

### D. Primitive Lift of Every Gram Triple

Status: proved lattice lemma.

If \(\Lambda_S\) contains two orthogonal hyperbolic planes
\[
U_1\oplus U_2
=\mathbb Ze_1\oplus\mathbb Zf_1\oplus
\mathbb Ze_2\oplus\mathbb Zf_2,
\]
then every \((n,l,m)\in\mathbb Z^3\) has a primitive saturated lift:
\[
Q=e_1+nf_1,\qquad P=lf_1+e_2+mf_2.
\]
Then
\[
Q^2=2n,\qquad P^2=2m,\qquad Q\cdot P=l.
\]
The sublattice \(\mathbb ZQ+\mathbb ZP\) is primitive because the
coefficient matrix contains a \(2\times2\) minor of determinant \(1\).

Role:
This proves the obstruction is not pointwise existence of physical
charge planes.  The obstruction is compatibility with Hall addition and
brackets.

### E. No-Go for Raw Gram Descent

Status: new theorem to insert.

Correct statement:
Let \(P=\bigoplus_c P_c\) be a
\(\Gamma_X^{\mathrm{phys}}\)-graded Lie superalgebra with
\[
[P_c,P_{c'}]\subset P_{c+c'}.
\]
Raw pushforward along the quadratic map \(\Pi\) can be a
\(\Gamma_{\mathrm{gram}}\)-graded Lie algebra only on bracket channels
where
\[
B(c,c')=0.
\]
The full BKM real-root strings of \(\mathfrak g_{\Delta_5}\) cannot be
realized by such raw \(B\)-isotropic descent, because repeated brackets
force self-interactions with
\[
B(c_i,c_i)=2\Pi(c_i)\ne0
\]
for nonzero real simple lifts.  Therefore the full comparison with
\(\mathfrak g_{\Delta_5}\) requires \(B\)-corrected normal ordering.

Proof routes:

1. Degree calculation:
   \(\Pi(c+c')=\Pi(c)+\Pi(c')\) is equivalent to \(B(c,c')=0\).
2. Real simple root calculation:
   for a real simple lift \(c_i\), \(\Pi(c_i)\ne0\), hence
   \(B(c_i,c_i)=2\Pi(c_i)\ne0\).
3. BKM relation check:
   the Cartan matrix has off-diagonal entries \(-2\), so for
   \(i\ne j\) the real Serre length is not killed at the first bracket;
   repeated brackets are visible in the real-root string.

Scope guard:
The theorem does not say no special chosen lift can make a single
bracket channel additive.  It says raw functorial pushforward cannot
realize the full BKM bracket.  The normal-ordered extension is forced.

### F. BKM Denominator Target

Status: imported theorem, structurally central.

The Gritsenko--Nikulin automorphic correction supplies
\[
\mathfrak g_{\Delta_5}
\]
and
\[
\operatorname{den}(\mathfrak g_{\Delta_5})
=64^{-1}\Delta_5(2Z).
\]
On active visible support,
\[
\operatorname{smult}\mathfrak g_{\Delta_5,\alpha(n,l,m)}
=f(nm,l).
\]

Boundary:
The determinant and denominator determine signed supermultiplicities.
They do not determine parity dimensions, Hall structure constants,
compact primitive representatives, no-extra-relations, or completed PBW.

### G. OP/DT Scalar Square

Status: imported theorem.

The scalar branch is
\[
Z^X_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}.
\]
The constant decomposes as
\[
-4096=-64^2.
\]
Here \(64^2\) is the theta-to-monic normalization and the leading minus
is OP scalar convention.

Boundary:
The scalar sign is not the Hall orientation character.  It cannot prove
\(\epsilon_o=\nu_{\Delta_5}\), because scalar squaring forgets the
character.

Required correction:
Strike every sentence that says or implies that the OP minus sign
sources the Hall orientation monodromy.  Replace with compatibility
language only.

### H. Orientation-Character Theorem

Status: conditional theorem plus group-theoretic consequence.

Clean statement:
If a compact orientation monodromy character
\[
\epsilon_o:W^{(2)}(\Lambda^{2,1}_{II})\to\{\pm1\}
\]
exists and satisfies
\[
\epsilon_o(s_{\delta_i})=-1,\qquad i=1,2,3,
\]
on the three type-II simple reflections, then
\[
\epsilon_o=\nu_{\Delta_5}
\]
on \(W^{(2)}(\Lambda^{2,1}_{II})\).

Proof routes:

1. \(W^{(2)}(\Lambda^{2,1}_{II})\) is generated by the three simple
   reflections.
2. The corresponding Coxeter exponents between distinct simple
   reflections are infinite; its abelianization is \((\mathbb Z/2)^3\).
3. A character is determined by its values on the three generators.
4. The Maass character has value \(-1\) on the same three generators.

Boundary:
The geometric work is exactly the local Pfaffian calculation
\(\epsilon_o(s_{\delta_i})=-1\).  Everything after that is group
theory.

### I. Conditional Dirac--Igusa Recognition

Status: certificate theorem, not construction theorem.

Correct statement:
Suppose a compact Dirac--Igusa datum supplies:

- a \(\Gamma_X\)-graded protected primitive Lie superalgebra;
- normal-ordered pushforward along \(\overline\Pi\);
- Cartan \(\Lambda^{2,1}_{II}\otimes\mathbb C\);
- real simple primitive representatives;
- imaginary simple-root fibres with GN parity data;
- Borcherds--Kac relations;
- completed Hopf pairing and the same radical quotient;
- no-extra-relations theorem;
- completed PBW compatibility;
- full parity dimensions.

Then
\[
\overline\Pi_* P_X\cong\mathfrak g_{\Delta_5}.
\]
Consequently
\[
\operatorname{den}(\overline\Pi_*P_X)=64^{-1}\Delta_5(2Z).
\]

Boundary:
This theorem verifies a supplied compact construction.  It does not
construct the compact Hall/factorization object.

## New Manuscript Architecture

### Part I. The Automorphic Square Root

Purpose:
Fix the automorphic object, the determinant normalization, and the
imported denominator theorem.

Sections:

1. Claim status and Dirac principle.
2. K3 protected index and \(K_0\)-half.
3. Borcherds determinant \(\mathcal D_X=\Delta_5\).
4. Gritsenko--Nikulin denominator algebra.
5. OP/DT scalar square.

Rule:
This part proves or imports scalar and automorphic facts.  It does not
construct the compact first-order object.

### Part II. Physical Charge and Normal Ordering

Purpose:
Make the new mathematical mechanism central.

Sections:

1. Algebraic even Mukai charge sector.
2. D6--D2--D0 Mukai--Gram theorem.
3. Quadratic Gram map.
4. Primitive lift of every Gram triple.
5. Defect cocycle \(B\).
6. Normal-ordered extension \(\Gamma_X\).
7. No-go theorem for raw descent.
8. Normal-ordered primitive recognition target.

Rule:
The scalar square must come after this part in the logical reading, even
if some automorphic normalization remains earlier for exposition.

### Part III. Compact Dirac--Igusa Realization Problem

Purpose:
Define the compact first-order object that would make the square root
physical.

Sections:

1. States versus observables.
2. Local protected observable algebra on \(X\).
3. Holomorphic \(E_3\) source.
4. \(K3\to E\) chiral specialization.
5. Projection-finite sectors and wrapped elliptic sectors.
6. Hybrid local/wrapped factorization target.
7. Orientation/Pfaffian monodromy.
8. Dirac--Igusa realization certificate.

Rule:
Do not write "constructed" unless the chain-level object and maps are
actually constructed.  Otherwise write "datum", "certificate", or
"target", with exact hypotheses.

### Part IV. Boundary-Row Certificates

Purpose:
Record the diagonal-divisor row catalogue without letting it distract
from the \(N=1\) theorem.

Sections:

1. Clery--Gritsenko eight-row catalogue.
2. Product row versus denominator row.
3. CHL scalar square.
4. Reduced CY/DT scalar host.
5. Compact Hall/chiral host certificate.
6. Row-by-row status ledger.

Rule:
Part IV is independent of the proof of the \(N=1\) Dirac--Igusa
theorem.  No physical row map is claimed without a row certificate.

### Appendices

A. Normalizations and Fourier conventions.
B. Lattice and Weyl chamber tables.
C. Boundary-row ledger.
D. Spin \(L\)-factor note, only if retained as independent arithmetic
   normalization; otherwise remove from the main paper.

## Immediate Fatal Repairs

These are not cosmetic.  They must be completed before the large
restructure.

1. Replace the Mukai-vector lemma.
   - Locus: `main.tex`, lemma "Mukai vector of an ideal sheaf on
     \(S\times E\)".
   - Remove "fourfold".
   - Remove "Todd correction".
   - Insert exact CY3 computation.

2. Correct connected \(BE\) cohomology.
   - Locus: `main.tex`, lemma "\(E\)-equivariant descent of the
     orientation line".
   - Connected \(BE\simeq BT^2\):
     \(H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2]\), \(|u_i|=2\).
   - Finite \(E[2]\):
     \(H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2]\), \(|x_i|=1\).
   - Split the lemma or rewrite it as connected descent plus finite
     stabilizer descent.

3. Downgrade small-orbit vanishing to a criterion unless equivariant
   linearization is explicitly proved.
   - Translation invariance of the underlying line is not enough.
   - A fixed line can carry nontrivial equivariant character.

4. Delete Bott explanation from the Gram-cocycle section.
   - Replace with a short remark:
     \(B(c,c)=2\Pi(c)\) is polarization, independent of orientation.

5. Separate OP scalar sign from Hall orientation.
   - OP minus is scalar convention.
   - Reflection character requires determinant-line monodromy.

6. Split the current Pfaffian theorem.
   - Orientation data normalizes a Pfaffian once the object exists.
   - It does not construct \(\mathfrak D_X\).

## Execution Phases

### Phase 0. Architecture and Fatal Repairs

Deliverables:

- this architecture note;
- exact Mukai--Gram theorem;
- corrected \(BE/BE[N]\) descent;
- Bott deletion;
- OP sign separation;
- Pfaffian theorem split.

Verification:

- grep for forbidden defects:
  `fourfold`, `Todd correction`, `H^1(BE`, `H^2(BE` with rank-three
  connected claim, `Bott-element sign normalization`, OP sign sourcing
  orientation.

### Phase 1. Normal-Ordered Part II

Deliverables:

- primitive lift lemma;
- normal-ordered map \(\overline\Pi(c,T)=\Pi(c)-T\);
- no-go theorem for raw descent;
- rewritten recognition target using \(\overline\Pi_*\), with
  \(\Theta\) as chain-level categorification.

Verification:

- direct proof of \(\overline\Pi\) homomorphism;
- direct proof of raw-descent no-go;
- coefficient/root check for real simple roots.

### Phase 2. Dirac Reordering

Deliverables:

- new abstract;
- new introduction;
- theorem-status ledger;
- moved scalar square into correct logical relation;
- automorphic theorem package tightened.

Verification:

- every theorem labeled proved / imported / conditional / open;
- no hidden construction claims.

### Phase 3. Compact Certificate

Deliverables:

- Dirac--Igusa realization certificate;
- hybrid wrapped factorization target;
- local/wrapped/mixed Hall correspondence requirements;
- orientation-character theorem separated from Pfaffian normalization.

Verification:

- no statement says compact \(E_3\) source exists unless it is an
  assumption;
- every open construction has a falsifiable structural obligation.

### Phase 4. Boundary Rows

Deliverables:

- Part IV explicitly independent of \(N=1\);
- row certificate table;
- spin \(L\)-factor moved or quarantined.

Verification:

- no row called physical without host certificate;
- \(F_5\)--\(F_8\) separated from GN rows and tied only to the
  Govindarajan CHL/WKB theorem where appropriate.

### Phase 5. Attack--Heal

Deliverables:

- critique-resolution table;
- hostile audit of signs, constants, \(BE/BE[N]\), Mukai vector,
  normal-ordering, orientation, and row claims;
- final build.

Verification:

- `python3 compute/verify_square_root.py`;
- `python3 compute/verify_lattice.py`;
- `make`;
- targeted grep scans.

## Subagent Topology If Authorized

The main thread remains integration owner.  Agents supply evidence, not
authority.  Agents do not vote truth into existence.

Suggested axes:

1. Mukai--Gram and OP dictionary.
2. \(BE/BE[N]\) equivariant descent.
3. Normal-ordered cocycle and raw-descent no-go.
4. Dirac/Pfaffian orientation theorem.
5. Hybrid wrapped factorization target.
6. Boundary-row certificates.

Each agent must return:

- claim attacked;
- proof or failure mode;
- local anchors;
- exact formulas/constants;
- source anchors where needed;
- files changed, if any;
- computations run;
- remaining obstruction.

No subagent commits.  No destructive git.  Main thread integrates by
deep semantic merge.

## Done Criteria

The reconstitution is done only when all of the following hold.

1. The manuscript's first page states the Dirac principle without
   overclaim.
2. The D6--D2--D0 variables are derived from the CY3 Mukai vector.
3. \((n,l,m)\) is never treated as a microscopic Hall charge.
4. \(\Gamma_X^{\mathrm{phys}}\), \(\Gamma_X\), and
   \(\Gamma_{\mathrm{gram}}\) are distinct and consistently named.
5. Formal normal-ordered lattice descent is theorem-level and central;
   compact Hall realization remains an explicit open construction
   problem.
6. Raw descent is ruled out by a precise no-go theorem.
7. The scalar OP/DT square is stated as imported and
   orientation-forgetful.
8. The orientation character is a determinant-line monodromy problem,
   not a scalar-normalization problem.
9. Compact Hall/factorization realization is a certificate with exact
   hypotheses.
10. Boundary rows are independent certificates, not hidden support for
    the \(N=1\) proof.
11. Every load-bearing claim has status: proved, imported, computed,
    conditional, open, conjectural, or heuristic.
12. The targeted computations and final TeX build pass, or any failure
    is named with its exact obstruction.
