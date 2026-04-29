# Agent 10 manuscript architecture report

Source mined: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`, current `main.tex`, `proj.bib`, and reports `agent01`--`agent05`.

Scope: manuscript theorem spine, rewrite architecture, title/abstract/introduction, main-proof versus appendix placement, certificate/theorem/open-problem typography, section renames, compression, and final paper structure.

Status rule: attacker prose is testimony, not authority. Structural claims below are checked against current `main.tex` sectioning and theorem labels. Primary-source mathematical verification belongs to the theorem agents.

## ideal theorem spine

The attack transcript contains two compatible spines. The early "referee-proof" spine is the stable minimal paper; the later "Etingof--Kac style" spine is the maximal construction-first paper. The ideal architecture should expose both: what is theorem-level now, and what becomes theorem-level only after new objects are actually constructed.

### A. Minimal stable spine

This is the safe paper if no new compact source objects are constructed.

1. **Virtual Borcherds determinant theorem.**
   \[
   \mathcal D_X(Z)
   =64q^{1/2}r^{1/2}s^{1/2}
   \prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}
   =\Delta_5(Z).
   \]
   Status: computed from the arbitrary \(K_0\) representative plus imported Borcherds--Gritsenko--Nikulin product. Current anchors: `main.tex:640`, `main.tex:818`, `main.tex:833`, `main.tex:2530`, `main.tex:14031`.

2. **D6--D2--D0 Mukai--Gram theorem.**
   \[
   v_X(\mathcal I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
   \qquad
   \Pi_X(Q_Y,P_Y)=(\beta^2/2,n,d-1).
   \]
   For \(\beta_h^2=2h-2\), this is \((h-1,n,d-1)\). This should be headline theorem-level, not a side dictionary lemma. Current anchor: `main.tex:2661`.

3. **Normal-ordered charge theorem.**
   \[
   \Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
   \qquad
   (c,T)\star(c',T')=(c+c',T+T'+B(c,c')),
   \]
   \[
   \overline\Pi_X(c,T)=\Pi_X(c)-T
   \]
   is additive. Include the flag formula
   \[
   (c_1,0)\star\cdots\star(c_k,0)
   =\left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right),
   \quad
   \overline\Pi_X=\sum_i\Pi_X(c_i).
   \]
   Current anchors: `main.tex:4590`, `main.tex:4614`, `main.tex:4832`, `main.tex:4863`. The flag formula is used later but should be stated near this theorem.

4. **Raw Gram descent no-go theorem.**
   Strict fixed-lift raw \(\Pi_X\)-pushforward cannot realize the type-II real-root strings. This is the reason normal ordering is forced. Current anchor: `main.tex:4883`. It should appear before any compact realization theorem.

5. **Gritsenko--Nikulin denominator target theorem.**
   \[
   \operatorname{den}(\mathfrak g_{\Delta_5})
   =64^{-1}\Delta_5(2Z),
   \qquad
   \smult\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
   \]
   on active support. Status: imported denominator theorem. Current anchors: `main.tex:5560`, `main.tex:5614`, `main.tex:13416`, `main.tex:13543`.

6. **OP/DT scalar square theorem.**
   \[
   Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}.
   \]
   Status: imported scalar check. It sees \(D_5^2\), not the first-order square root. Current anchor: `main.tex:13806`.

7. **Compact Dirac--Igusa realization problem.**
   State as open/certificate only unless the compact source objects are constructed. The correct target is a normal-ordered primitive comparison after source construction, not an inference from determinant equality. Current anchors: `main.tex:11750`, `main.tex:12124`, `main.tex:12590`, `main.tex:14135`.

8. **Row-extension appendix or companion theorem.**
   The eight rows are independent boundary material. They should not be in the core proof unless row certificates directly feed the \(N=1\) theorem. Current anchors: `main.tex:14267`, `main.tex:14689`.

### B. Maximal construction-first spine

This is the paper the later attack transcript wants: certificates stop being substitutes for objects.

1. **Theorem A: Normal-ordered charge theorem.**
   Combine current `main.tex:4316`, `main.tex:4614`, `main.tex:4832`, and `main.tex:4883`. Make this the central new mathematical result. The slogan is theorem-level: normal ordering is forced.

2. **Theorem B: Universal algebraic Dirac--Igusa construction.**
   Construct a curve-universal algebraic target for every smooth curve \(C\) and linear lift \(L:\Gamma_{\mathrm{gram}}\to\Gamma_X^{\mathrm{form}}\):
   \[
   s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma),
   \qquad
   \Pi_{X,*}\mathfrak g_{\Delta_5,L}\cong\mathfrak g_{\Delta_5},
   \]
   \[
   \mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}
   :=U_C^{\mathrm{ch}}\operatorname{Cur}_C(\mathfrak g_{\Delta_5,L}).
   \]
   Current gap: `main.tex:5724` constructs only \(\mathsf{Den}_{\Delta_5,E}\), not a curve-universal \(D^{\mathrm{alg}}_{\Delta_5,C,L}\), no lift groupoid, and no \(s_L\) theorem.

3. **Theorem C: Geometric normal-ordered pre-Hall source.**
   Construct \(H^{\mathrm{pre}}_{X,\Gamma}\) from derived stacks \(\mathfrak M_c\), labels \((c,T)\), and exact-triangle correspondences landing in \(c\star c'\):
   \[
   \mathfrak M_{(c,T)}:=\mathfrak M_c\times\{T\},
   \qquad
   \mathfrak M_{(c,T)}\times\mathfrak M_{(c',T')}
   \leftarrow \mathfrak E_{c,c'}
   \to \mathfrak M_{(c,T)\star(c',T')}.
   \]
   Current draft has source interfaces and certificates (`main.tex:5704`--`main.tex:8254`) but not this object as the opening construction.

4. **Theorem D: Orientation-gerbe twisted protected Hall construction.**
   Construct \(H^{\mathrm{tw}}_{X,\Gamma}\) over the square-root gerbe. A global orientation is a section/trivialization of the gerbe, not a prerequisite for defining the twisted source. Current draft mostly treats orientation as certificate data; see `main.tex:2472`, `main.tex:3197`, `main.tex:11750`. Agent 05 also forces this split.

5. **Theorem E: Hybrid local/wrapped source.**
   Construct the projection-finite plus wrapped elliptic-degree factorization object. The \(\delta_2=(0,1,1)\) primitive must live in the wrapped sector. Current definition is detailed but certificate-forward: `main.tex:7039`, `main.tex:7082`, `main.tex:7121`, `main.tex:8083`.

6. **Theorem F: Source chiral coalgebra.**
   Construct the source coalgebra \(C_{X,R}\) from the source hybrid object, not from the target current envelope. Current source/target firewall is correct: `main.tex:6404`, `main.tex:6452`, `main.tex:6506`, `main.tex:6970`.

7. **Theorem G: Compact Dirac--Igusa realization theorem.**
   Only after A--F state the comparison:
   \[
   \Pi_{X,*}H^0\Prim_{\mathrm{prot}}(H^{\mathrm{tw}}_{X,\Gamma})/\operatorname{Rad}
   \cong \mathfrak g_{\Delta_5},
   \qquad
   \operatorname{Pf}^{\mathrm{tw}}_X=\Delta_5.
   \]
   The current `Primitive recognition certificate; no source construction` theorem at `main.tex:12124` remains correctly conditional but should not be the architectural center if Hpre/Htw can be built.

8. **Theorem H: Scalar square compatibility.**
   With the first-order object constructed and recognized, OP/DT gives the orientation-forgetting trace:
   \[
   \operatorname{Tr}_{\mathrm{prot}}((-1)^F\mathfrak D_X^{-2})
   =-4096\Delta_5^{-2}.
   \]
   This belongs after the first-order structure, as a second-order scalar shadow.

## current structure diagnosis

### Front matter

The title at `main.tex:7` can remain. It is provocative but the subtitle already contains "realization problem", which correctly prevents an existence claim.

The abstract at `main.tex:57`--`main.tex:172` is honest but overloaded. It states determinant, denominator, OP square, charge formalism, normal ordering, compact realization, and eight rows in one pass. The attack transcript calls it "strong but still too long and theorem-heavy." It should become shorter and more architectural:

- determinant and denominator target;
- normal-ordered charge repair;
- OP scalar square as second-order check;
- compact realization as Dirac first-order problem.

The abstract still says "recognition target" at `main.tex:103`; later attacks prefer "realization target" only after actual objects are constructed. If no \(H^{\mathrm{pre}}\), \(H^{\mathrm{tw}}\), \(D^{\mathrm{alg}}\) are constructed, keep "open realization problem" or "recognition problem"; do not blur the two.

### Introduction and claim strength

Current `main.tex:177`--`main.tex:462` is useful but certificate-heavy. It contains the correct dependency chain at `main.tex:194`--`main.tex:210` and strong status tables at `main.tex:357`--`main.tex:453`. The problem is placement and density: a reader sees caveat tables before seeing the constructive theorem spine.

Needed front-page inserts:

- a "Dirac principle" paragraph: first-order protected object first; scalar trace second;
- a "What is new / imported / open" table;
- a "forbidden implications" table:
  \[
  \mathcal D_X=\Delta_5\not\Rightarrow \mathfrak D_X,\qquad
  \Delta_5^2\not\Rightarrow\epsilon_o,\qquad
  \mathfrak g_{\Delta_5}\not\Rightarrow\text{compact Hall source}.
  \]
- a "notation never to confuse" table: \(\Gamma_X^{\mathrm{form}}\), \(\Gamma_X\) or \(\widehat\Gamma_X\), \(\Gamma_{\mathrm{gram}}\), \(\Lambda_{II}^{2,1}\), \(D_X\), \(D_5\), \(\Delta_5\), \(\chi_{10}^{\mathrm{OP}}\).

### Current parts and section order

Current order:

1. `main.tex:462` Part: The automorphic square root.
2. `main.tex:464` Physical question.
3. `main.tex:640` One-particle index and determinant.
4. `main.tex:920`--`main.tex:2383` orientation/Pfaffian certificate material, inside the first part.
5. `main.tex:2383` Normalized cusp form.
6. `main.tex:2632` Part: Physical charge and normal-ordered descent.
7. `main.tex:2634` D6--D2--D0 dictionary, then scalar quotient/orientation criteria.
8. `main.tex:4309` Physical charge and normal-ordered Gram descent.
9. `main.tex:5022` Part: Denominator algebra and compact realization.
10. `main.tex:5704` Compact Dirac--Igusa realization problem.
11. `main.tex:13701` Scalar square.
12. `main.tex:13957` Coefficient dictionary and synthesis.
13. `main.tex:14267` Rows.
14. `main.tex:14554` Appendices: spin \(L\)-factor and row boundary material, plus `appendices/boundary_compatibility_conditions`.

Diagnosis:

- The normal-ordered theorem, one of the paper's strongest contributions, appears too late (`main.tex:4309`) and after a long orientation detour.
- The O1/O1+/O2 orientation package appears too early and too fully in the main proof. The attack consistently says: main text two-page theorem; appendix full obstruction algebra.
- The D6--D2--D0 Mukai--Gram dictionary is too low-status as a lemma (`main.tex:2661`). It should be promoted and placed before scalar integration and before any OP variable table.
- The compact realization section has strong separation language (`main.tex:5707`--`main.tex:5716`) but remains certificate-first. It lists what a source would need before constructing named source objects.
- The scalar square is currently late (`main.tex:13701`), which is better than early scalar-driven framing. It should remain a consistency check, but the synthesis at `main.tex:14014` should not make scalar square a central arrow before compact realization if the paper is construction-first.
- The rows and spin \(L\)-factor material are too large relative to the core theorem. The row material is valuable but distracts unless explicitly branded independent.

### Typography and theorem status

Current theorem/proposition labels mostly preserve honesty, but several names still inflate status:

- `main.tex:882` "Dirac/Pfaffian recognition target" should be a definition or open problem, not a proposition, unless it proves a structural consequence.
- `main.tex:1139` conditional Dirac--Pfaffian theorem should be split into supplied datum, Pfaffian comparison, scalar-square consequence, local sign proposition, and group-character lemma.
- `main.tex:11518` "Finite D0-certificate: proved, imported, conditional, and open parts" is honest but too ledger-like for a main theorem.
- `main.tex:12124` "Primitive recognition certificate; no source construction" is honest. Rename to "Primitive recognition certificate theorem" unless actual generators/relations are constructed, in which case use "primitive presentation theorem."
- `main.tex:6192`, `main.tex:6506`, `main.tex:7121`, `main.tex:9973`, `main.tex:11750`, and `main.tex:12479` overuse "certificate". Some should become constructed objects; the rest should move to an appendix or "open theorem data" ledger.

## move/delete/rename actions

1. **Keep the title, compress the abstract.**
   Keep "The Igusa Square Root"; the title means Dirac first-order structure, not analytic branch choice. Shorten `main.tex:57`--`main.tex:172`. Replace "For virtual super vector spaces" with "For arbitrary Grothendieck representatives." Avoid "physical charge lattice" in the abstract; use "formal dyonic Mukai lattice."

2. **Rename Section 1.**
   Current: `Introduction and claim strength` (`main.tex:177`).
   Proposed: `Introduction: The Dirac Problem`.
   Put the claim-status table in a boxed "How to read this paper" page, not as the first sustained prose.

3. **Add after the introduction: `Constructed Objects, Not Certificates`.**
   This is the attack transcript's central architectural demand. It should introduce:
   \[
   D^{\mathrm{alg}}_{\Delta_5,C,L},\qquad
   H^{\mathrm{pre}}_{X,\Gamma},\qquad
   H^{\mathrm{tw}}_{X,\Gamma},
   \]
   and then the comparison theorem. Current `rg` confirms these objects are absent from `main.tex`.

4. **Rename `The physical question` (`main.tex:464`).**
   Proposed: `Protected Operations Before Traces` or `Dirac Principle And Support Locality`.
   Keep the states-as-sectors paragraph at `main.tex:467`--`main.tex:478`.
   Add the explicit distinction: the obstruction is support-locality after projection to \(E\), not failure of spacetime locality on \(K3\times E\).

5. **Rename `The one-particle index and its determinant` (`main.tex:640`).**
   Proposed: `Virtual Borcherds Package And The \(K_0\) Determinant`.
   Avoid "one-particle" unless immediately qualified by virtual/Borcherds. Keep the bulk/cusp split at `main.tex:771`--`main.tex:816`.

6. **Convert `Dirac/Pfaffian recognition target` (`main.tex:882`) to a definition/open problem.**
   Proposed name: `Definition. Dirac/Pfaffian target problem.`
   It does not prove a proposition; it names the missing first-order object.

7. **Move the full orientation package out of Part I.**
   The material from `main.tex:920` to `main.tex:2383` should become:
   - main text: short conditional sign theorem;
   - appendix: full O1/O1+/O2 obstruction package.
   Keep the local sign formula, but do not let orientation data appear to construct the compact Dirac object.

8. **Move or delete the Bott discussion.**
   Current negative remark at `main.tex:2509`--`main.tex:2528` is mathematically safe but still invites the wrong frame. Move it to a sign-convention appendix or delete from the main proof. It should not sit in the normalized cusp-form section.

9. **Keep `The normalized cusp form`, but slim it.**
   Current `main.tex:2383`--`main.tex:2630` should keep normalization, automorphic line, and \(D_5=64^{-1}\Delta_5\). Move full Maass generator computation to an appendix; keep only six reflection values in main text.

10. **Promote D6--D2--D0 dictionary.**
    Current `main.tex:2661` should become a theorem. Place it after the formal dyonic Mukai lattice definition or make the formal lattice definition precede it. The reader should see \(v_X=P\otimes1_E+Q\otimes\omega_E\) before scalar quotient integration.

11. **Move `Physical charge and normal-ordered Gram descent` earlier and make it central.**
    Current `main.tex:4309` should become the main new mathematical section immediately after the determinant/denominator normalization and before compact realization. Rename to `Normal-Ordered Gram Descent`.

12. **Normalize notation for the corrected degree group.**
    The attack recommends one notation, preferably \(\Gamma_X\), for the corrected group. Current draft uses \(\widehat\Gamma_X\). If \(\widehat\Gamma_X\) stays, define once and do not also use \(\Gamma_X\) informally. Distinguish the raw section \(i_0(c)=(c,0)\) from the split section \(s(c)=(c,\Pi_X(c))\).

13. **Define raw homogeneous pushforward before the no-go theorem.**
    Current `main.tex:4883` proves the right obstruction but should first define the raw fixed-lift variant it forbids.

14. **Rename and generalize the formal current envelope.**
    Current `\mathsf{Den}_{\Delta_5,E}` (`main.tex:5724`) should be renamed to one of:
    - \(\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,E,L}\),
    - \(\operatorname{CurEnv}_E(\mathfrak g_{\Delta_5})\).
    Better: define \(\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}\) for any smooth curve \(C\), then specialize \(C=E\) for \(K3\times E\).

15. **Replace certificate-first compact section with construction-first subsections.**
    Current `main.tex:5704`--`main.tex:13276` should be reorganized around:
    - algebraic target \(D^{\mathrm{alg}}_{\Delta_5,C,L}\);
    - geometric pre-Hall source \(H^{\mathrm{pre}}_{X,\Gamma}\);
    - orientation-gerbe twisted source \(H^{\mathrm{tw}}_{X,\Gamma}\);
    - hybrid local/wrapped source;
    - source coalgebra;
    - primitive comparison.

16. **Define \(\operatorname{Fact}^{\mathrm{hol}}(X)\) before \(E_3\).**
    Current `main.tex:5770` gives a useful definition, but the attack wants the primary object to be a holomorphic factorization category first, with the \(E_3\)-shadow as a local/formality consequence.

17. **Promote hybrid locality from certificate to object if possible.**
    Current `main.tex:7121` is a certificate. If the manuscript adopts the construction-first program, this becomes a finite constructed correspondence/factorization object, with residuals appended.

18. **Move scalar square into consistency-check position.**
    Current `main.tex:13701` is late, which is acceptable. The rewrite should explicitly box: "OP/DT proves the scalar square, not the first-order square root." Do not let `main.tex:14014` present scalar square as a driver of compact realization.

19. **Move rows to companion or independent part.**
    If retained, put `main.tex:14267` onward under an explicitly independent heading: "Independent Boundary Row Ledger." Add "Part IV is independent of Parts I--III." Otherwise move to companion paper.

20. **Move spin \(L\)-factor appendix out of the main paper.**
    Current `main.tex:14558`--`main.tex:14686` is independent and creates a separate normalization audit surface. Reduce to one sentence or move to a separate arithmetic normalization note.

21. **Appendix plan.**
    Add or consolidate appendices:
    - sign conventions and Bott/Pfaffian conventions;
    - Fourier variables and \(D_X,D_5,\Delta_5,\Delta_{10},\chi_{10}^{\mathrm{OP}}\) glossary;
    - automorphic line and Maass generator values;
    - orientation obstruction algebra O1/O1+/O2;
    - finite-source residual ledgers;
    - eight-row boundary ledger, if retained.

## paragraph-level rewrite priorities

1. **Abstract, first paragraph (`main.tex:58`--`main.tex:81`).**
   Replace with a compact determinant statement. Use "arbitrary Grothendieck representatives" and "virtual \(K_0\)-determinant." Keep \(Z_{\mathrm{K3}}=2\phi_{0,1}\), but state "half" as arithmetic/Borcherds normalization, not Hilbert splitting.

2. **Abstract, denominator paragraph (`main.tex:83`--`main.tex:98`).**
   Insert "imported from Borcherds--Gritsenko--Nikulin" in the first theorem-level mention. Say "visible positive signed root supermultiplicities on active support."

3. **Abstract, Dirac paragraph (`main.tex:100`--`main.tex:115`).**
   Change from recognition-target prose to Dirac principle:
   scalar branch is second-order and orientation-forgetting; the first-order problem is to construct the protected algebra/Pfaffian object. Do not imply \(\mathfrak D_X\) is obtained from the certificate.

4. **Abstract, charge paragraph (`main.tex:131`--`main.tex:169`).**
   Compress. Avoid "holomorphic \(E_3\)" before \(\operatorname{Fact}^{\mathrm{hol}}(X)\) has been defined. Use \(\Gamma_X^{\mathrm{form}}\) and say "not the full 4d \(\mathcal N=4\) charge lattice" once in the introduction, not repeatedly in the abstract.

5. **Introduction dependency chain (`main.tex:194`--`main.tex:210`).**
   Replace with a theorem-program diagram:
   \[
   \text{protected index}\to K_0\text{-Borcherds determinant}
   \to \text{GN denominator target}
   \to \Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}}
   \to \text{compact Dirac--Igusa realization}.
   \]
   Then add "new/imported/open".

6. **Compact and hybrid factorization paragraph (`main.tex:226`--`main.tex:258`).**
   Split into two paragraphs: support-locality versus spacetime locality; then hybrid local/wrapped remedy. Current paragraph is too dense and mixes concept, definition, and residual list.

7. **Primitive recognition paragraph (`main.tex:260`--`main.tex:296`).**
   Replace the long certificate list with one concise paragraph and a forward reference. Move the full list to the compact realization or appendix. Add radical quotient to the displayed isomorphism if the source comparison requires it.

8. **Status tables (`main.tex:357`--`main.tex:453`).**
   Keep one front table and one final summary. Cut repeated claim-status paragraphs elsewhere.

9. **Physical question (`main.tex:467`--`main.tex:565`).**
   Keep the hierarchy "states are sectors; operations factorize." Strengthen the line: determinant gives the signed Gram-index shadow, not "one-particle index such a realization would have."

10. **K0 determinant section (`main.tex:640`--`main.tex:918`).**
    Rename terms:
    - \(\mathcal V\): "virtual Borcherds determinant package," not "one-particle object";
    - \(\mathcal Z_{\mathrm{Borch}}^{\mathrm{vir}}\), not BPS notation;
    - \(m=0\): cusp/Weyl boundary, not microscopic K3 states.

11. **Orientation/Pfaffian material (`main.tex:920`--`main.tex:2383`).**
    Split. Main text should carry:
    - square-root gerbe exists as gerbe;
    - global orientation is a section/trivialization;
    - O1/O1+/O2 are needed for \(\epsilon_o\);
    - local rank-one signs imply \(-1\) only after those hypotheses.
    Move quotient gerbe algebra, finite stabilizer algebra, Weyl cocycles, and wall atlas to appendix.

12. **Normalized cusp form (`main.tex:2383`--`main.tex:2630`).**
    Keep automorphic line:
    \[
    \Delta_5\in H^0(\mathbb H_2,\mathcal L^5\otimes\nu_{\Delta_5}),\qquad
    \Delta_5^2\in H^0(\mathbb H_2,\mathcal L^{10}).
    \]
    This supports the Dirac/Pfaffian thesis. Move the full Maass computation.

13. **D6 dictionary (`main.tex:2634`--`main.tex:2758`).**
    Make the theorem visible and define the Mukai pairing before use. Warn that \(h,d,n\) are OP branch variables, not full charge-lattice coordinates. Put the variable dictionary in one place only.

14. **Reduced scalar quotient (`main.tex:2760`--`main.tex:2799`).**
    Keep it, but do not let it precede the formal charge theorem in the final architecture. It produces numbers coefficientwise, not CoHA integration.

15. **Normal ordering (`main.tex:4309`--`main.tex:4977`).**
    This should be the main proof narrative. Add flag formula; define raw homogeneous pushforward; keep fibre-summed caveat. Remove or repair the `H^2_{\mathrm{sym}}` wording flagged by Agent 02.

16. **Denominator algebra (`main.tex:5560`--`main.tex:5702`).**
    Put GN algebra presentation in a compact Kac-style subsection: Cartan, real simple roots, imaginary simple roots, parity, relations, invariant form, radical quotient. Add zero-bracket counterexample to prevent determinant-to-bracket inference.

17. **Formal current envelope (`main.tex:5724`--`main.tex:5768`).**
    Rename and generalize. Current notation makes \(E\) look physically built into a target-current construction. It should be curve-universal; \(E\) enters only at compact \(K3\times E\) specialization.

18. **Compact source interface (`main.tex:5770`--`main.tex:8254`).**
    Replace lead with object construction. The opening should say: the compact object is not defined by a recognition certificate; first construct the normal-ordered Hall correspondence source; then twist over the orientation gerbe; then build hybrid local/wrapped source; then compare.

19. **Primitive recognition (`main.tex:12124`--`main.tex:12631`).**
    Keep the conditions. If the source objects are not constructed, keep "recognition certificate." If they are constructed, upgrade to "primitive presentation theorem" and prove generators, relations, PBW, radical, and parity dimensions.

20. **Scalar square (`main.tex:13701`--`main.tex:13955`).**
    Add theorem statement caveat: the leading minus is OP scalar normalization, not a Hall orientation character. Keep constants out of orientation.

21. **Main synthesis (`main.tex:13957`--`main.tex:14265`).**
    Replace the current arrow chain with one of the two explicit spines above. Add "what is constructed now" and "what remains an open theorem." Do not hide the main result under a coefficient dictionary.

22. **Rows and appendices (`main.tex:14267`--end).**
    If retained, state independence before the first table. The row atlas should not be audited before the reader has absorbed the Dirac--Igusa theorem.

## standalone/readability risks

1. **Certificate fatigue.**
   The word "certificate" appears heavily throughout `main.tex` and dominates the compact half. Honesty is good, but after enough repetitions the manuscript reads as a checklist rather than a construction. Construct \(D^{\mathrm{alg}}\), \(H^{\mathrm{pre}}\), and \(H^{\mathrm{tw}}\) where possible; move residual ledgers to appendices.

2. **Theorem spine is buried.**
   The current theorem-level contributions are distributed across a 16k-line draft. A cold reader should see the spine in the first five pages and then follow sections in that order.

3. **The normal-ordering theorem is under-promoted.**
   The paper's strongest new structural argument is at `main.tex:4309`--`main.tex:4977`, not the OP square or the row atlas. It should be a central theorem near the front.

4. **"Physical" remains unstable.**
   Current draft repairs this at `main.tex:4316`--`main.tex:4347`, but the abstract and early prose still risk saying "physical charge lattice" too early. Use:
   - \(\Gamma_X^{\mathrm{form}}\): formal dyonic Mukai bookkeeping lattice;
   - \(\Gamma_{X,\sigma}^{\mathrm{eff}}\): effective Hall support;
   - full \(\mathcal N=4\) charge lattice only when explicitly discussed.

5. **The \(E_3\) term is still too expensive.**
   Current `main.tex:5770` defines it better than earlier drafts, but the manuscript should first define the actual holomorphic factorization category/model and then state \(E_3\) as a local/formality shadow.

6. **Target/source notation blurs.**
   \(\mathsf{Den}_{\Delta_5,E}\) sounds like a compact \(E\)-source. Rename to a target-current name and separate curve-universal target from elliptic compact source.

7. **The abstract is not standalone-readable.**
   It is correct but too long and front-loads too many theorem dependencies. The reader needs one narrative: determinant target, normal-ordering repair, compact Dirac problem.

8. **The row material dilutes the breakthrough.**
   Rows are valuable but not core to the \(\Delta_5\) theorem. Without a hard independence signpost, a referee will audit row maps instead of the main theorem.

9. **The spin \(L\)-factor appendix is a normalization liability.**
   It is independent and gives a hostile reader another audit surface. It should leave the manuscript unless it is used.

10. **Tables are useful but over-distributed.**
    Keep: one front claim-status table; one notation table; one final synthesis table. Move technical residual tables to appendices.

11. **The proof/object order is inverted in the compact half.**
    Current compact section often says "certificate consists of..." before constructing the underlying stack/correspondence object. The final architecture must construct object first, then state its comparison certificate.

12. **Open problem typography needs hierarchy.**
    Open problem should name a missing construction. Certificate should name finite data/tests. Theorem should prove a mathematical implication or construction. Proposition should not merely name an ambition.

## residual actions

1. Decide which target paper is being written:
   - minimal stable normalization-and-separation paper; or
   - construction-first Dirac--Igusa paper with \(D^{\mathrm{alg}}\), \(H^{\mathrm{pre}}\), and \(H^{\mathrm{tw}}\).

2. If construction-first: add the missing object-level section immediately after the introduction:
   \[
   D^{\mathrm{alg}}_{\Delta_5,C,L},\quad H^{\mathrm{pre}}_{X,\Gamma},\quad H^{\mathrm{tw}}_{X,\Gamma}.
   \]
   Then rewrite compact realization as comparison, not certificate.

3. Promote the D6--D2--D0 Mukai--Gram dictionary to a theorem and move the formal dyonic Mukai lattice before OP/DT scalar integration.

4. Move normal-ordered charge theorem and raw-descent no-go before compact realization. Add the flag formula and raw-pushforward definition.

5. Rename the formal current envelope and make it curve-universal. Add lift \(L\) and \(s_L\) if the algebraic Dirac--Igusa target is constructed.

6. Split O1/O1+/O2:
   - main text: statement and sign consequence;
   - appendix: full obstruction algebra, finite-stabilizer computations, Weyl cocycle, wall atlas.

7. Add the square-root gerbe/twisted Hall paragraph before global orientation. Global orientation is a section, not prerequisite existence of twisted states.

8. Audit all theorem names for claim strength. Convert target-naming propositions into definitions/open problems.

9. Add the forbidden-implications table and notation-not-to-confuse table.

10. Reduce the abstract and introduction after the new theorem spine is fixed.

11. Move eight-row material to a companion paper or explicitly independent final part. If kept, require row-level compact tables and a statement that it is independent of the \(N=1\) proof.

12. Move spin \(L\)-factor appendix to a separate note unless it becomes used in the proof.

13. Run a post-rewrite grep for banned conflations:
   - `compact BPS Hilbert`
   - `operator determinant`
   - `analytic root`
   - `physical charge lattice`
   - `orientation` near `64` or `-4096`
   - `raw pushforward`
   - `one-particle` without `virtual`

14. Run a post-rewrite grep for required construction objects if maximal architecture is adopted:
   - `D^{\\mathrm{alg}}`
   - `H^{\\mathrm{pre}}`
   - `H^{\\mathrm{tw}}`
   - `orientation gerbe`
   - `linear lift`
   - `curve-universal`

15. After integration, run a TeX build and inspect the first 10 pages and theorem list. The first 10 pages must show the theorem spine, not the residual ledger.

No edits to `main.tex` were made by Agent 10.
