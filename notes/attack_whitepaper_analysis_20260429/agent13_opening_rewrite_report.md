# Agent 13 opening rewrite report

Scope: title, abstract, introduction, first-page signal, claim-strength tables,
first theorem statements, and the false perception that the compact
Dirac--Igusa object has already been built.

Sources read: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`,
`main.tex`, `proj.bib`, and current reports `agent01`--`agent10`.

Status rule: attack prose is testimony, not authority. The report below uses
current `main.tex` anchors for manuscript state and imports other agents only
where their claims are anchored to `main.tex`, `proj.bib`, or local scripts.

## current opening diagnosis

The title at `main.tex:7` can remain. It is provocative but defensible because
the subtitle already says "realization problem." It must be protected on page
one by the Dirac interpretation: the square root is first-order
Pfaffian/protected structure, not a Hilbert-space half, not an analytic branch,
and not something obtained from the scalar square.

The abstract `main.tex:57-172` is honest but too long. It performs six jobs at
once: K3 protected index, virtual determinant, GN denominator, OP scalar square,
formal Mukai/Gram correction, compact Hall/factorization requirements, and
eight-row boundary ledger. The first-page signal is therefore a ledger rather
than a theorem spine. A serious reader can see the caveats, but the density
still lets "certificate," "target," "operator," "E_3," and "realization" blur.

The first true claim spine is stable:
\[
Z_{\mathrm{K3}}=2\phi_{0,1}
\rightsquigarrow
\mathcal D_X=\Delta_5
\rightsquigarrow
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
\]
plus the formal normal-ordering theorem
\[
\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T.
\]
This spine is not visually first. The normal-ordering theorem, one of the
strongest new contributions, starts only at `main.tex:4309`.

The opening already repairs the old fatal error that
`\Gamma_{\mathrm{gram}}` is a Hall charge lattice. It says at `main.tex:140-145`
and `main.tex:4316-4454` that `(n,l,m)` is a quadratic Gram shadow, not the
additive Hall grading. The remaining risk is placement: the reader sees
`\mathcal D_X`, `\mathfrak D_X`, "holomorphic \(E_3\)-factorization algebra,"
and "recognition target" before seeing a compact "not constructed" firewall in
a compact table.

The current section title `Introduction and claim strength` at `main.tex:177`
is accurate but weak. It should become `Introduction: The Dirac Problem` or
`Introduction: The First-Order Problem`. The first page should state the
problem, then the theorem spine, then the status ledger.

## stable first-page claims

Preserve these claims on page one, with the same status discipline.

1. **Protected K3 input.** `main.tex:58-69`, `214-224`, `667-740`.
   The theorem-level physical input is the protected K3 index:
   \[
   Z_{\mathrm{K3}}=2\phi_{0,1},\qquad
   \phi_{0,1}=\sum f(n,l)q^nr^l.
   \]
   The Borcherds input is the arithmetic half \(\phi_{0,1}\), represented
   by arbitrary Grothendieck representatives
   \(\mathbb U_{n,l}\) with \(\sdim \mathbb U_{n,l}=f(n,l)\).
   It is not a canonical half-Hilbert space.

2. **Virtual \(K_0\)-determinant.** `main.tex:70-81`, `771-831`,
   `833-880`, `2530-2558`.
   The determinant package is virtual:
   \[
   \mathcal D_X(Z)
   =64q^{1/2}r^{1/2}s^{1/2}
   \prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}
   =\Delta_5(Z).
   \]
   The equality with \(\Delta_5\) is the theta-normalized form of the
   imported Borcherds--Gritsenko--Nikulin product.

3. **Normalization.** `main.tex:79-81`, `2530-2599`.
   The monic product is \(D_5=64^{-1}\Delta_5\). The coefficient
   \(64\) is theta-normalization, not orientation data.

4. **BKM denominator target.** `main.tex:83-98`, `298-310`,
   `5560-5702`, `13543-13601`.
   Gritsenko--Nikulin supply the denominator algebra:
   \[
   \operatorname{den}(\mathfrak g_{\Delta_5})=
   64^{-1}\Delta_5(2Z),
   \qquad
   \smult \mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
   \]
   on active support. This is target algebra, not compact Hall geometry.

5. **OP scalar square.** `main.tex:117-129`, `312-337`,
   `13701-13955`.
   OP/Oberdieck gives the reduced scalar branch
   \[
   Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}.
   \]
   It sees \(D_5^2\), not \(D_5\), and cannot determine \(\epsilon_o\).

6. **Formal Mukai/Gram correction.** `main.tex:131-155`,
   `4316-4382`, `4590-4881`.
   The additive bookkeeping lattice is
   \[
   \Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S.
   \]
   The Igusa degree is the quadratic Gram shadow
   \[
   \Pi_X(Q,P)=\left(Q^2/2,Q\cdot P,P^2/2\right),
   \]
   with additivity defect \(B(c,c')\). Normal ordering makes
   \(\overline\Pi_X\) additive.

7. **Raw descent obstruction.** `main.tex:146-154`, `4883-4975`.
   Strict fixed-lift raw \(\Pi_X\)-descent cannot realize the type-II
   real-root strings. Normal-ordered descent is forced at degree level.

8. **Compact realization is open.** `main.tex:96-98`, `109-115`,
   `154-169`, `226-296`, `5704-5716`, `11750-12124`.
   The paper does not construct a compact BPS Hilbert space, compact Hall
   correspondences, a compact orientation, or a BPS operator product.
   It formulates the compact Dirac--Igusa realization problem and its
   certificates.

## misleading first-page claims

These are not necessarily false in context. They mis-signal if left in the
opening without compression or stronger status tags.

1. **`For \(X=K3\times E\)` at `main.tex:58`.**
   The opening can sound as if a compact \(K3\times E\) source is already
   being used. Rewrite the first sentence to say that the only theorem-level
   physical input used before the compact realization problem is the K3
   protected index.

2. **"Borcherds half" at `main.tex:64`.**
   "Half" invites Hilbert splitting. Use "arithmetic Borcherds half" or
   "Borcherds input \(\phi_{0,1}\)" and immediately say "arbitrary
   Grothendieck representative."

3. **"The same coefficients are the signed root supermultiplicities" at
   `main.tex:83-98`.**
   This is stable only with "visible positive signed root
   supermultiplicities on active support" and "imported GN denominator."
   It must not imply parity dimensions or compact primitives.

4. **"recognition target is a first-order protected operator/algebra" at
   `main.tex:103-110`.**
   This still reads as if \(\mathfrak D_X\) has been specified. Rewrite:
   "the open Dirac--Igusa problem is to construct a first-order protected
   operator/algebra..." Then list what is required.

5. **"holomorphic \(E_3\)-factorization algebra" at `main.tex:135` and
   `226-238`.**
   The term is too expensive for the abstract unless the chosen
   holomorphic factorization model and formality/framing datum have already
   been defined. In the abstract use "finite-first compact
   Hall/factorization source." Define \(E_3\) later.

6. **"formal dyonic charge lattice" at `main.tex:131-139`.**
   Keep, but do not call it "physical charge lattice" in the abstract.
   In the introduction add once: \(\Gamma_X^{\mathrm{form}}\) is not the
   full four-dimensional \(\mathcal N=4\) electric--magnetic charge lattice
   and not compact Hall support.

7. **The dependency chain `main.tex:194-210`.**
   It is correct but visually busy. It should become a theorem-program
   diagram plus a compact "new/imported/open" table. The current chain
   contains too many labels before the reader knows the objects.

8. **The compact/hybrid paragraph `main.tex:226-258`.**
   It combines source object, specialization, support-locality obstruction,
   wrapped sector, mixed correspondences, and open status in one paragraph.
   Split it. The first-page version should state only the obstruction and
   the shape of the remedy.

9. **Primitive recognition paragraph `main.tex:260-296`.**
   The long certificate list is too dense for the opening. It also omits
   the radical quotient in the displayed comparison. Compress to one
   paragraph and move the list to the compact realization section.

10. **Two front status tables `main.tex:357-453`.**
    The content is good. The opening should keep one table with columns
    "object, status, source, proves, does not prove." Move the second or
    merge it.

11. **Section names and first theorem signals.**
    - `main.tex:462` "The automorphic square root" is acceptable only
      after the Dirac principle is explicit.
    - `main.tex:640` "The one-particle index and its determinant" should
      be `Virtual Borcherds Package and the \(K_0\)-Determinant`.
    - `main.tex:882` "Dirac/Pfaffian recognition target" should be a
      definition or open problem, not a proposition.
    - `main.tex:2661` D6--D2--D0 Mukai--Gram dictionary should be promoted
      to theorem-level if kept in the main spine.
    - `main.tex:4614` normal-ordering should be theorem-level and near
      the front.

## exact rewrite instructions

1. **Title, `main.tex:7`: preserve.**
   Keep `The Igusa Square Root` and the current subtitle. Do not weaken
   the title. The repair is first-page interpretation, not title retreat.

2. **Abstract `main.tex:57-172`: replace as a whole.**
   Preserve its mathematical content but cut it to five paragraphs:
   protected index/K0 determinant; GN denominator; OP scalar square;
   formal Mukai/normal ordering; compact Dirac problem. Remove the
   eight-row sentence from the abstract unless the rows remain central.

3. **Abstract paragraph `main.tex:58-81`: rewrite, not delete.**
   Use "arbitrary Grothendieck representatives" instead of "For virtual
   super vector spaces." Say the determinant equality is computed from the
   \(K_0\) package and identified with \(\Delta_5\) by imported GN/Borcherds
   theory.

4. **Abstract paragraph `main.tex:83-98`: preserve with status upgrade.**
   Add "imported" and "active support." Suggested line:
   "The imported Gritsenko--Nikulin denominator algebra has visible
   positive signed root supermultiplicities \(f(nm,l)\) on
   \(\Gamma_{\mathrm{act}}\)."

5. **Abstract paragraph `main.tex:100-115`: rewrite.**
   Make it a Dirac principle paragraph:
   scalar square is second-order and orientation-forgetting; the first-order
   object is open and requires source, orientation/Pfaffian line,
   normal-ordered descent, and primitive recognition.

6. **Abstract paragraph `main.tex:117-129`: compress.**
   Keep \(D_5=64^{-1}\Delta_5\), \(\chi_{10}^{\mathrm{OP}}=D_5^2\), and
   \(Z_{\mathrm{OP/DT}}^X=-4096\Delta_5^{-2}\). End with:
   "The constants \(64\), \(4096\), and the OP minus sign are scalar
   normalization data."

7. **Abstract paragraph `main.tex:131-171`: compress and move detail.**
   Keep \(\Gamma_X^{\mathrm{form}}\), \(\Pi_X\), \(B\),
   \(\widehat\Gamma_X\), \(\overline\Pi_X\), and raw-descent no-go.
   Move the formality/QME/HN/hybrid checklist and the eight-row ledger out
   of the abstract.

8. **Rename `main.tex:177`.**
   Proposed:
   ```tex
   \section{Introduction: The Dirac Problem}
   ```

9. **Replace `main.tex:180-213`.**
   Start the introduction with the Dirac principle, then the theorem
   program:
   \[
   \text{protected K3 index}
   \to K_0\text{-Borcherds determinant}
   \to \text{GN denominator target}
   \to \text{normal-ordered Gram descent}
   \to \text{compact Dirac--Igusa realization problem}.
   \]
   Then add a short "new/imported/open" table.

10. **Keep `main.tex:214-224`, but move after the program.**
    This is the clean protected-localization input. It should be under a
    "Known protected input" paragraph.

11. **Split `main.tex:226-258`.**
    Paragraph A: projection-to-\(E\) support-locality obstruction, not
    spacetime locality failure. Paragraph B: the hybrid wrapped remedy is
    a finite compact-source requirement and remains open.

12. **Compress `main.tex:260-296`.**
    Replace the certificate list by:
    \[
    H^0\Prim_{\mathrm{prot}}
    (\overline\Pi_{X,*}^{\Theta}\mathcal F_X)/
    \overline{\operatorname{Rad}}
    \cong \mathfrak g_{\Delta_5}
    \]
    conditional on source representatives, parities, bracket constants,
    Hopf pairing/radical, PBW, no-extra-relations, and exact completion.
    Move details to the primitive-recognition section.

13. **Keep `main.tex:298-337` as content, compress into the status table.**
    The denominator and OP scalar paragraphs are stable. They should not
    occupy the entire first page after the rewrite.

14. **Move `main.tex:339-355` out of the opening.**
    Boundary rows are not part of the first-page \(N=1\) theorem signal.
    If retained, give one sentence: "The final part records independent
    diagonal-divisor row certificates."

15. **Merge `main.tex:357-453` into one front table.**
    Required columns:
    `Object`, `Status`, `Source`, `What it proves`, `What it does not
    prove`.
    Required rows:
    K3 elliptic genus; \(K_0\)-determinant; GN denominator algebra; OP
    scalar square; formal Mukai/normal ordering; compact Dirac--Igusa
    realization; boundary row certificates.

16. **Add a forbidden-implications table immediately after the status table.**
    It must contain:
    \[
    \mathcal D_X=\Delta_5 \not\Rightarrow \mathfrak D_X,
    \qquad
    \Delta_5^2 \not\Rightarrow \epsilon_o,
    \qquad
    \mathfrak g_{\Delta_5}\not\Rightarrow \text{compact Hall source},
    \qquad
    \Gamma_{\mathrm{gram}}\not= \text{Hall charge lattice}.
    \]

17. **Add a notation table near the opening.**
    Include:
    \(\mathcal D_X\), \(D_5\), \(\Delta_5\),
    \(\chi_{10}^{\mathrm{OP}}\),
    \(\Gamma_X^{\mathrm{form}}\),
    \(\Gamma_{\mathrm{gram}}\),
    \(\widehat\Gamma_X\),
    \(\mathfrak g_{\Delta_5}\),
    \(\mathfrak D_X\).

18. **Rename `main.tex:640`.**
    Replace:
    ```tex
    \section{The one-particle index and its determinant}
    ```
    with:
    ```tex
    \section{Virtual Borcherds Package and the \(K_0\)-Determinant}
    ```
    Use "one-particle" only as "virtual Borcherds one-particle package."

19. **Convert `main.tex:882-918`.**
    Change proposition to definition/open problem:
    ```tex
    \begin{openproblem}[Dirac--Pfaffian target problem]
    ```
    or
    ```tex
    \begin{definition}[Dirac--Pfaffian target problem]
    ```
    depending on local theorem-style conventions. It names the missing
    first-order object; it does not prove one.

20. **Promote `main.tex:2661-2750`.**
    Make the D6--D2--D0 Mukai--Gram dictionary a theorem or headline
    proposition. Correct any wording that says the triple is "in the Mukai
    lattice of \(X\)"; it is a Gram-index triple of the two K3 Mukai
    components.

21. **Move `main.tex:4309-4975` earlier.**
    The normal-ordering theorem and raw no-go should appear before the
    compact realization section. Add the flag formula:
    \[
    (c_1,0)\star\cdots\star(c_k,0)
    =
    \left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right).
    \]

22. **Define raw fixed-lift pushforward before `main.tex:4883`.**
    The no-go theorem is good but needs the attacked object stated before
    the theorem.

23. **Rename the formal current envelope `main.tex:5724-5768`.**
    Do not let \(\mathsf{Den}_{\Delta_5,E}\) sound like a compact
    \(E\)-source. Prefer a curve-universal target name such as
    \(\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}\) or
    \(\operatorname{CurEnv}_C(\mathfrak g_{\Delta_5,L})\), with \(C=E\)
    only at the compact specialization.

24. **Box the scalar-square rule in `main.tex:13701-13955`.**
    "OP/DT proves the scalar square, not the first-order square root."

25. **Move row and spin material out of the first-page expectation.**
    The row material should be an independent part or companion. The spin
    \(L\)-factor appendix should be moved to a separate arithmetic
    normalization note unless used in a theorem.

## proposed replacement abstract/intro skeleton

### Abstract skeleton

```tex
\begin{abstract}
For a K3 surface \(S\), the theorem-level physical input used here is
the protected K3 index:
\[
Z_{\mathrm{K3}}=2\phi_{0,1},\qquad
\phi_{0,1}=\sum f(n,l)q^nr^l.
\]
The Borcherds input is the arithmetic half \(\phi_{0,1}\).  Choosing
arbitrary Grothendieck representatives
\(\mathbb U_{n,l}\in K_0(\mathrm{sVect}_{\mathrm{fd}})\) with
\(\sdim\mathbb U_{n,l}=f(n,l)\) gives a virtual \(K_0\)-determinant,
not a microscopic Hilbert space:
\[
\mathcal D_X(Z)
=64q^{1/2}r^{1/2}s^{1/2}
\prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}
=\Delta_5(Z).
\]
The last equality is the theta-normalized Borcherds--Gritsenko--Nikulin
product.  Thus \(D_5=64^{-1}\Delta_5\).

The imported Gritsenko--Nikulin denominator algebra has
\[
\operatorname{den}(\mathfrak g_{\Delta_5})
=64^{-1}\Delta_5(2Z),
\qquad
\smult\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
\]
on active support.  It supplies the automorphic denominator target and
its target-internal bracket.  It does not supply compact Hall
correspondences, a compact orientation, or a compact BPS operator product.

The reduced OP/DT scalar branch is
\[
Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}.
\]
This sees \(D_5^2\), not \(D_5\).  The factor \(4096=64^2\) is the
theta-to-monic conversion and the minus sign is OP scalar normalization;
neither determines the Maass/reflection character or compact orientation
monodromy.

The compact \(K3\times E\) problem starts from an additive formal dyonic
Mukai lattice
\[
\Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S
\]
and the quadratic Gram shadow
\[
\Pi_X(Q,P)=\left(Q^2/2,Q\cdot P,P^2/2\right).
\]
Its additivity defect is the symmetric bilinear cocycle
\[
B(c,c')=(Q\cdot Q',Q\cdot P'+Q'\cdot P,P\cdot P').
\]
The normal-ordered extension
\[
\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T
\]
makes the Gram degree additive.  Strict fixed-lift raw Gram descent
cannot realize the type-II real-root strings; normal-ordered descent is
forced at degree level.

The square root is therefore meant in Dirac's sense.  The open problem is
to construct a finite-first compact protected Hall/factorization source
on \(K3\times E\), with orientation/Pfaffian data, hybrid wrapped
elliptic-degree sectors, normal-ordered Gram descent, and primitive
radical quotient
\[
H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)/
\overline{\operatorname{Rad}}
\cong \mathfrak g_{\Delta_5}.
\]
Only after such a source and Pfaffian-to-automorphic line comparison are
supplied can one assert a compact first-order object with protected
Pfaffian \(\Delta_5\).
\end{abstract}
```

### Introduction skeleton

1. **Dirac principle.**
   Start:
   "A scalar square is not square-rooted here by choosing a branch. It is
   square-rooted, in Dirac's sense, by constructing a first-order
   protected algebra whose Pfaffian has the missing character."

2. **Theorem program.**
   Display:
   \[
   \text{K3 protected index}
   \to K_0\text{-Borcherds determinant}
   \to \text{GN denominator target}
   \to \text{normal-ordered Gram descent}
   \to \text{compact Dirac--Igusa realization problem}.
   \]

3. **What is new / imported / open.**
   One table:
   - New/formal here: \(K_0\)-determinant packaging, normalization ledger,
     Mukai--Gram dictionary, \(B\)-cocycle, normal-ordered extension,
     raw-descent no-go, compact certificate framework.
   - Imported: K3 elliptic genus, Borcherds/GN product, GN denominator
     algebra, OP/Oberdieck scalar square, Clery--Gritsenko rows where used.
   - Open: compact source, orientation-gerbe trivialization, hybrid
     wrapped Hall object, source Koszul object, primitive PBW/radical
     recognition, compact Pfaffian equality.

4. **Degree conventions.**
   State once:
   \(\Gamma_X^{\mathrm{form}}\) is formal even Mukai bookkeeping, not the
   full four-dimensional \(\mathcal N=4\) charge lattice and not effective
   compact Hall support.  \(\Gamma_{\mathrm{gram}}\cong\mathbb Z^3\) is
   Fourier/root/Gram degree.  The compact Hall source, if constructed,
   is graded upstairs and only later pushed forward by
   \(\overline\Pi_X\).

5. **Support locality.**
   State narrowly:
   positive elliptic degree is a projection-to-\(E\) support-locality
   obstruction for a naive \(\operatorname{Ran}(E)\) model. It is not a
   denial of spacetime locality on \(K3\times E\). The remedy is a hybrid
   local/wrapped compact source, still open unless constructed later.

6. **Forbidden implications.**
   Put the four forbidden arrows in a small table. This table should be
   visible before the first technical section.

7. **Claim-strength table.**
   Use one table with "does not prove" column. Do not start the paper
   with residual checklists.

## residuals

1. Decide whether the paper is the minimal stable paper or the
construction-first paper. The opening above is safe for the current
minimal architecture. If the manuscript constructs
\(D^{\mathrm{alg}}_{\Delta_5,C,L}\), \(H^{\mathrm{pre}}_{X,\Gamma}\), and
\(H^{\mathrm{tw}}_{X,\Gamma}\), the abstract should be upgraded only after
those objects exist in `main.tex`.

2. Primary-source exact checks remain outside this opening pass: GN/GNII
normalization, OP/Oberdieck scalar sign and hypotheses, Clery--Gritsenko
row data, Govindarajan CHL rows, and spin \(L\)-factor sources if the
appendix remains.

3. The introduction must include the radical quotient in the primitive
comparison. Current `main.tex:289-291` omits it while later theorems need
it.

4. The formal lattice core needs local cleanup flagged by Agent 02:
separate raw placement \(i_0(c)=(c,0)\) from split section
\(s(c)=(c,\Pi_X(c))\), add the flag formula, define raw fixed-lift
pushforward, and repair the `H^2_{\mathrm{sym}}` wording.

5. The compact source language remains expensive. If terms like
"holomorphic \(E_3\)-factorization algebra" stay in the opening, the paper
must first define the holomorphic factorization category, local \(E_3\)
shadow, formality/framing datum, and finite model. Otherwise move the term
out of the abstract.

6. The row material and spin \(L\)-factor appendix should not set
first-page expectations. They are independent ledgers unless a theorem in
the main spine uses them.

7. After the rewrite, inspect the first ten pages. They must show the
Dirac principle, theorem spine, degree conventions, forbidden
implications, and claim-status table before the compact residual ledger.

No edit to `main.tex` was made by Agent 13.
