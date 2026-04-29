# Agent 16 Source Objects Report: \(H^{\mathrm{pre}}\), \(H^{\mathrm{tw}}\), Hybrid Source

Scope: mine `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`
and current `main.tex` for the source-object construction program:
\(H^{\mathrm{pre}}_{X,\Gamma}\),
\(H^{\mathrm{tw}}_{X,\Gamma}\), the
orientation-gerbe-twisted protected Hall object, primitive protected Hall
extraction, hybrid local/wrapped source, and the source/target firewall.

Verdict: current `main.tex` is honest but still certificate-forward on the
compact source. It proves the determinant, imported denominator target,
OP scalar square, normal-ordered charge algebra, and raw-descent
obstruction. It does not yet define the named source objects
\(H^{\mathrm{pre}}_{X,\Gamma}\) or \(H^{\mathrm{tw}}_{X,\Gamma}\).
The attack file's construction-first rewrite is mathematically plausible
only if it distinguishes three levels: pre-integrated derived
correspondences, gerbe-twisted protected state spaces, and the final
source-to-target primitive comparison.

## Object inventory

1. **Formal normal-ordered degree group.**
   Current theorem-level object:
   \[
   \widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
   \qquad
   (c,T)\star(c',T')=(c+c',T+T'+B(c,c')),
   \]
   \[
   \overline\Pi_X(c,T)=\Pi_X(c)-T.
   \]
   This is present and proved as lattice algebra in `main.tex`.
   It is not a Hall category and not a source object.

2. **\(H^{\mathrm{pre}}_{X,\Gamma}\): geometric normal-ordered
   Hall correspondence source.**
   Attack construction:
   let \(M_c\subset \mathrm{Perf}^{\mathrm{cpt}}(X)\) be the derived
   stack of compact objects of formal Mukai charge \(c\), set
   \[
   M_{(c,T)}:=M_c\times\{T\},
   \]
   and define exact-triangle stacks
   \[
   M_{(c,T)}\times M_{(c',T')}
   \xleftarrow{p}
   E_{(c,T),(c',T')}
   \xrightarrow{q}
   M_{(c,T)\star(c',T')}.
   \]
   Triple flags \(F_{c_1,c_2,c_3}\) control associativity. The key point is
   that the target map lands in the normal-ordered label
   \((c,T)\star(c',T')\), so the \(B\)-correction is built into the
   source correspondence, not applied after integration.

   Current `main.tex` has all ingredients as supplied or conditional
   inputs, but not the named object. It has a local schema using supplied
   derived moduli stacks `main.tex:570-618`, finite d-critical stacks and
   extension stacks in the \(D_0\) certificate `main.tex:9973-10080`,
   and a finite Hall source kernel `main.tex:10994-11091`. It does not
   state the theorem:
   \[
   H^{\mathrm{pre}}_{X,\Gamma}
   =(\{M_{\hat c}\},\{E_{\hat c,\hat c'}\},\{F_{\hat c_1,\hat c_2,\hat c_3}\})
   \]
   is an associative \(\widehat\Gamma_X\)-graded algebra object in
   correspondences of derived stacks.

3. **Finite \(H^{\mathrm{pre}}_{X,\Gamma,R}\).**
   Attack construction:
   choose \((\sigma,S,h_S,R)\), define the finite HN charge set
   \[
   \widehat\Gamma_{X,R}
   =\{(c_1,0)\star\cdots\star(c_k,0): c_i\in F_{\sigma,S}(R),
   \sum_i h_S(c_i)\le R\},
   \]
   and restrict the object and extension stacks to this finite set.

   Current `main.tex` has conditional finite charge-support Hall quotients
   `main.tex:9887-9971`, but not finite \(H^{\mathrm{pre}}_{X,\Gamma,R}\)
   as a named pre-integration object.

4. **Orientation gerbe \(\operatorname{Or}_{R,\hat c}\).**
   Attack construction:
   for each finite d-critical/shifted-symplectic stack \(M_{R,\hat c}\),
   let \(K_{R,\hat c}\) be the virtual canonical/determinant line and set
   \[
   \operatorname{Or}_{R,\hat c}:=\sqrt{K_{R,\hat c}},
   \]
   the \(\mu_2\)-gerbe whose objects over \(U\to M_{R,\hat c}\) are
   pairs \((L,\phi:L^{\otimes2}\simeq K_{R,\hat c}|_U)\). It carries a
   tautological line \(L^{1/2}_{R,\hat c}\). A global orientation is a
   section/trivialization of this gerbe.

   Current `main.tex` discusses orientation gerbes and obstruction
   classes, e.g. `main.tex:2878-2900`, `main.tex:4262-4305`, and
   `main.tex:8540-8600`, but it does not package
   \(\operatorname{Or}_{R,\hat c}\) as the construction base for the Hall
   source. It still treats orientation mostly as certificate data.

5. **\(H^{\mathrm{tw}}_{X,\Gamma}\): orientation-gerbe-twisted protected
   Hall object.**
   Attack construction:
   lift the exact-triangle correspondences to the orientation gerbes and
   define
   \[
   H^{\mathrm{tw}}_{R,\hat c}
   =
   H_*^{\mathrm{BM}}\bigl([\operatorname{Or}_{R,\hat c}/E],
   \Phi^{\mathrm{or}}_{R,\hat c}\otimes L^{1/2}_{R,\hat c}\bigr)_{\mathrm{anti}}.
   \]
   The subscript anti is the \(\mu_2\)-anti-invariant summand, the natural
   home of Pfaffian states. Pull--Thom--Sebastiani--push gives product,
   the opposite pull-push gives coproduct, and
   \[
   P_R^{\mathrm{tw}}
   =
   \ker(\Delta_R-\mathrm{id}\otimes 1-1\otimes\mathrm{id})
   \]
   gives primitives. Normal-ordered pushforward gives
   \(P_R^{\Pi,\mathrm{tw}}\).

   Current `main.tex` does not contain this object. It has a protected
   Hall integration criterion `main.tex:2817-2845`, conditional
   normal-ordered Hall descent `main.tex:8603-8724`, and a finite Hall
   source kernel that produces \(\mathcal H_R^{or}\) only when the kernel
   is supplied `main.tex:10994-11174`.

6. **Untwisted/oriented Hall object \(H^{or}\).**
   This exists only after a global orientation section or compatible
   trivialization of the orientation gerbe. It should not be a prerequisite
   for the twisted source. Current `main.tex` sometimes correctly states
   this as an open orientation problem, e.g. `main.tex:2472-2506` and
   `main.tex:2914-2934`, but it does not yet use the gerbe-first hierarchy.

7. **Hybrid local/wrapped source.**
   Current `main.tex` correctly proves the support-locality obstruction:
   positive elliptic degree projects onto all of \(E\), so ordinary
   \(\operatorname{Ran}(E)\)-locality sees only \(b=0\)
   `main.tex:7039-7119`. It then defines a finite hybrid certificate
   `main.tex:7121-7144` and leaves the construction open
   `main.tex:8254-8303`.

   Attack construction demands actual source objects:
   projection-finite local stacks, wrapped stacks, rigidified wrapped
   prequotients using the elliptic anchor
   \[
   \lambda(A)=\det Rp_{E,*}A\otimes\mathcal O_E(-\chi(A)0_E)\in\operatorname{Pic}^0(E),
   \]
   four correspondence types (LL, LW, WL, WW), and eight two-step flag
   types (LLL, LLW, LWL, WLL, LWW, WLW, WWL, WWW). Current text has the
   certificate interface, not the constructed finite correspondence object.

8. **Source coalgebra \(C_X\).**
   Current `main.tex` has the right firewall: the target bar--cobar
   counit does not define the source coalgebra `main.tex:6404-6504`.
   It defines a chiral Koszul source certificate `main.tex:6506-6728`.
   The object \(C_{X,R}^{\mathrm{tw}}=\bar B_E^{\mathrm{ch}}
   (\mathcal F^{\mathrm{hyb,tw}}_{X,R})\) is not constructed because
   \(\mathcal F^{\mathrm{hyb,tw}}_{X,R}\) is not constructed.

9. **Primitive protected Hall extraction.**
   Current `main.tex` makes primitive recognition correctly conditional:
   `main.tex:12124-12446` assumes source primitives, representatives,
   relations, Hopf pairing, radical quotient, no-extra-relations, PBW, and
   exact completion. This is not a source construction. The attack demands
   that this consume \(H^{\mathrm{tw}}_{X,\Gamma}\), not an abstract
   supplied \(\mathcal F_X\).

## What is theorem-level now

1. **The virtual determinant is theorem-level.**
   The \(K_0\)-determinant built from arbitrary Grothendieck
   representatives gives the theta-normalized \(\Delta_5\). Current
   synthesis: `main.tex:14031-14060`.

2. **The denominator target is imported theorem-level.**
   Gritsenko--Nikulin supplies \(\mathfrak g_{\Delta_5}\) and
   \(\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)\).
   Current anchors: `main.tex:83-98`, `main.tex:5560-5635`,
   `main.tex:13543-13562`, `main.tex:14087-14109`.

3. **The OP/DT scalar square is imported theorem-level.**
   The scalar branch is
   \[
   Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}.
   \]
   It is orientation-forgetful. Current anchors: `main.tex:117-129`,
   `main.tex:13724-13855`, `main.tex:14111-14134`.

4. **Normal-ordered charge algebra is theorem-level.**
   The formal Mukai lattice, Gram map, cocycle \(B\), extension
   \(\widehat\Gamma_X\), and homomorphism \(\overline\Pi_X\) are proved.
   Anchors: `main.tex:4316-4381`, `main.tex:4590-4808`,
   `main.tex:4832-4881`.

5. **Raw fixed-lift Gram descent no-go is theorem-level.**
   Strict raw \(\Pi_X\)-descent cannot realize the type-II real-root
   strings. Anchor: `main.tex:4883-4905`.

6. **Projection-to-\(E\) locality obstruction is theorem-level.**
   Positive elliptic degree is wrapped/global over \(E\), not
   projection-finite Ran-local. Anchors: `main.tex:7039-7119`.

7. **Several finite source consequences are conditional theorem-level.**
   If finite stacks, orientations, vanishing cycles, pull-push
   admissibility, and flag coherences are supplied, then finite Hall
   products, source kernels, and primitive brackets follow. Anchors:
   `main.tex:7853-7998`, `main.tex:10994-11174`.

8. **Orientation statements are criteria, not global construction.**
   The text has conditional gerbe-vanishing and multiplicative-orientation
   criteria, not a full orientation-gerbe-twisted Hall object. Anchors:
   `main.tex:2848-2900`, `main.tex:4262-4305`, `main.tex:8540-8600`.

## What the PDF demands

1. **The PDF itself forbids source-from-target shortcuts.**
   It states that the denominator algebra is the target and not a compact
   source: `main.tex:94-98`, `main.tex:5707-5716`. Any rewrite must keep
   this firewall.

2. **The PDF demands additive Hall charge before Gram descent.**
   It explicitly says \((n,l,m)\) is not the Hall grading and that the
   compact Hall source must be graded upstairs before normal-ordered
   pushforward: `main.tex:131-168`, `main.tex:4431-4453`,
   `main.tex:11768-11796`.

3. **The PDF demands finite source data before compact claims.**
   The compact \(E_3\) source interface is an inverse-limit construction
   from finite data, not an existence theorem for those data:
   `main.tex:6024-6140`. The finite \(D_0\) certificate explicitly assumes
   bounded finite-type \(K3\times E\) substacks and a finite d-critical
   Hall atlas: `main.tex:9973-10080`.

4. **The PDF demands quotient-after-correspondence.**
   The \(E\)-quotient may not be taken before local/wrapped extension
   correspondences are formed. This is stated in the hybrid certificate
   and compact realization datum: `main.tex:7121-7144`,
   `main.tex:11798-11859`, `main.tex:11950-11954`.

5. **The PDF demands orientation as geometry, not normalization.**
   Constants \(64\), \(4096\), and the OP minus sign do not construct
   \(\epsilon_o\). Anchors: `main.tex:127-129`,
   `main.tex:2914-2934`, `main.tex:14168-14179`.

6. **The PDF demands primitive recognition beyond signed dimensions.**
   Equality of \(\sdim=f(nm,l)\) is not enough. The source must provide
   primitive representatives, relations, Hopf pairing, radical quotient,
   no-extra-relations, PBW, parity dimensions, and exact completion.
   Anchors: `main.tex:12124-12446`, `main.tex:14180-14190`.

7. **The attack PDF/transcript demands a construction-first upgrade.**
   It proposes the chain:
   \[
   H^{\mathrm{pre}}\;\to\;H^{\mathrm{tw}}\;\to\;\mathcal F^{\mathrm{hyb,tw}}
   \;\to\;C_X^{\mathrm{tw}}\;\to\;P_X^{\Pi,\mathrm{tw}}
   \;\to\;\mathfrak g_{\Delta_5}.
   \]
   Anchors in the attack file:
   `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:21840-21961`,
   `:22055-22108`, `:23051-23489`, `:24646-24831`.

## Minimal honest rewrite

If no new construction is inserted into `main.tex`, the rewrite must say:

1. The paper constructs the virtual Borcherds determinant, proves the
   normal-ordered charge algebra, imports the denominator target, imports
   the OP scalar square, and proves several obstructions.

2. The compact source is not constructed. The current objects
   \(\mathcal A_X^{E_3}\), \(\mathcal F_X^{\mathrm{hyb}}\),
   \(C_X\), \(\Theta_{\mathrm{Kos}}\), and
   \(H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)\)
   are interfaces or certificate outputs.

3. The honest replacement sentence is:

   "A compact Dirac--Igusa source would first be a normal-ordered derived
   correspondence object \(H^{\mathrm{pre}}_{X,\Gamma}\). After lifting to
   the square-root orientation gerbes and applying a protected integration
   functor, it would give an orientation-gerbe-twisted protected Hall
   object \(H^{\mathrm{tw}}_{X,\Gamma}\). The comparison
   \[
   \overline\Pi_{X,*}H^0\Prim_{\mathrm{prot}}(H^{\mathrm{tw}}_{X,\Gamma})/
   \operatorname{Rad}\cong\mathfrak g_{\Delta_5}
   \]
   remains open in this paper."

4. If the paper wants one new theorem without solving compact physics,
   it can safely state only the pre-integrated theorem:

   "The derived substacks \(M_{(c,T)}=M_c\times\{T\}\), exact-triangle
   stacks, and two-step flag stacks define an associative
   \(\widehat\Gamma_X\)-graded object in the correspondence category of
   derived stacks."

   This theorem must explicitly add: no finite protected cohomology, no
   orientation, no \(E\)-quotient integration, no primitive comparison,
   and no Pfaffian equality is claimed.

5. The phrase "orientation-gerbe-twisted Hall object is constructed" is
   honest only if the text defines the gerbes, the lifted
   correspondences, the tautological square-root line, the
   \(\mu_2\)-anti-invariant state spaces, and the pull--TS--push product
   in a specified compact-support formalism. If it only lists those as
   required data, it is still a certificate.

## Maximal construction pathway

1. **Build \(\widehat\Gamma_X\) first.**
   Keep current lattice theorem. Add the finite flag formula:
   \[
   (c_1,0)\star\cdots\star(c_k,0)
   =
   \left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right),
   \qquad
   \overline\Pi_X=\sum_i\Pi_X(c_i).
   \]

2. **Define \(H^{\mathrm{pre}}_{X,\Gamma}\).**
   Use \(M_c\subset\mathrm{Perf}^{\mathrm{cpt}}(X)\), labels
   \(M_{(c,T)}=M_c\times\{T\}\), exact-triangle stacks, target map to
   \(M_{(c,T)\star(c',T')}\), and two-step flags. Prove associativity in
   the correspondence category from exact-triangle flag associativity and
   associativity of \(\star\).

3. **Define finite \(H^{\mathrm{pre}}_{X,\Gamma,R}\).**
   Choose stability/HN sector, strict sector, height, finite charge set,
   and restrict stacks and correspondences. State boundedness and
   finite-type as hypotheses unless proved.

4. **Construct orientation gerbes before orientations.**
   For every finite \(M_{R,\hat c}\), define \(K_{R,\hat c}\),
   \(\operatorname{Or}_{R,\hat c}\), tautological \(L^{1/2}_{R,\hat c}\),
   and lifted extension/flag correspondences over the gerbes. State global
   orientation as a section/trivialization, not as input to the twisted
   source.

5. **Define \(H^{\mathrm{tw}}_{X,\Gamma,R}\).**
   Pull vanishing-cycle sheaves to \(\operatorname{Or}_{R,\hat c}\),
   take Borel--Moore or compact-support cohomology on
   \([\operatorname{Or}_{R,\hat c}/E]\), and extract the
   \(\mu_2\)-anti-invariant summand. Product and coproduct come from
   lifted correspondences and Thom--Sebastiani. Primitives come after the
   coproduct, not from the determinant.

6. **Construct the hybrid local/wrapped source.**
   Define local and wrapped stacks, wrapped anchors, rigidified wrapped
   prequotients, LL/LW/WL/WW correspondences, and the eight two-step flags.
   Do quotient-after-correspondence. Then define
   \(\mathcal F^{\mathrm{hyb,pre}}_{X,R}\) and, after twisted integration,
   \(\mathcal F^{\mathrm{hyb,tw}}_{X,R}\).

7. **Construct the source coalgebra.**
   Define
   \[
   C^{\mathrm{tw}}_{X,R}
   =\bar B_E^{\mathrm{ch}}(\mathcal F^{\mathrm{hyb,tw}}_{X,R})
   \]
   with source filtration, collision coproduct, conilpotence, transition
   maps, and Mittag--Leffler exactness. Do not import it from
   \(\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E})\).

8. **Extract primitives and define the source Dirac/Pfaffian object.**
   Let \(V^{\mathrm{src}}_{R,\gamma}=(P_R^{\Pi,\mathrm{tw}})_\gamma\).
   Define the finite Dirac block and source Pfaffian from those source
   primitives. The equality \(\operatorname{Pf}^{\mathrm{tw}}_X=\Delta_5\)
   is a theorem only after proving
   \(\sdim V^{\mathrm{src}}_{(n,l,m)}=f(nm,l)\) in the limit.

9. **Only then state the compact realization theorem.**
   The comparison morphism is source-to-target:
   \[
   \Phi_X^{DI}:D_X^{DI}\to D^{\mathrm{alg}}_{\Delta_5,E,L}.
   \]
   Its theorem is equivalence after normal-ordered primitive pushforward,
   closed radical quotient, PBW/exact-completion checks, and orientation
   trivialization/monodromy comparison.

## Forbidden shortcuts

1. Do not define \(H^{\mathrm{pre}}\), \(H^{\mathrm{tw}}\), \(C_X\), or
   primitive representatives from the Borcherds product.

2. Do not define the source coalgebra by taking a homotopy inverse of the
   target bar--cobar counit.

3. Do not call \(\mathsf{Den}_{\Delta_5,E}\) a compact source. It is a
   target current envelope.

4. Do not grade the Hall category by \(\Gamma_{\mathrm{gram}}\). The Hall
   product is additive upstairs; \(\Gamma_{\mathrm{gram}}\) appears only
   after normal-ordered pushforward.

5. Do not use strict fixed-lift raw \(\Pi_X\)-descent for the type-II
   real-root bracket. Current text proves this fails.

6. Do not treat \(64\), \(4096\), or the OP minus sign as an orientation
   character.

7. Do not treat existence of orientation lines as construction of the
   orientation-gerbe-twisted source. The gerbe, its tautological line, and
   lifted correspondences must be defined.

8. Do not quotient by \(E\) before constructing local/wrapped and mixed
   correspondences. Quotienting first forgets relative \(E\)-position.

9. Do not append a detached global Hecke/Fock \(s\)-factor and call it the
   hybrid source. It must act through mixed Hall correspondences before the
   reduced \(E\)-quotient.

10. Do not infer primitive recognition from signed dimensions. Full parity
    dimensions, representatives, relations, Hopf radical, no-extra-relations,
    PBW, and completion are required.

11. Do not call a finite obstruction tuple a construction. It becomes a
    construction only when the object and null-trivializations are supplied.

12. Do not use \(\mathbb U_{n,l}\in K_0(\mathrm{sVect})\) as a compact
    Hilbert space or protected Hall state.

## main.tex anchors

1. `main.tex:94-98`: denominator algebra is target; it does not supply
   compact Hall correspondences, orientation, or BPS product.

2. `main.tex:131-168`: compact realization would require formal charge
   lattice, Hall support, normal-ordered extension, \(E_3\) source,
   hybrid local/wrapped correspondences, and primitive comparison.

3. `main.tex:226-258`: hybrid source is open; positive elliptic degree
   requires wrapped correspondence data.

4. `main.tex:260-296`: primitive recognition is conditional, not
   reconstruction from the determinant.

5. `main.tex:391-445`: status table correctly marks compact
   Dirac--Igusa source as certificate/conditional/open.

6. `main.tex:570-618`: local protected observable algebra is a
   pre-interface using supplied derived stacks, vanishing cycles, and
   orientations.

7. `main.tex:2472-2506`: orientation line is defined as supplied data;
   no such line is constructed.

8. `main.tex:2817-2845`: protected Hall integration criterion lists
   required compact Hall/CoHA data; no \(K3\times E\) datum is constructed.

9. `main.tex:2914-2934`: orientation monodromy character is open and must
   be produced by determinant-line transport, not normalization.

10. `main.tex:4316-4381`, `main.tex:4590-4808`, `main.tex:4832-4881`:
    formal normal-ordered charge algebra is proved.

11. `main.tex:4883-4905`: raw fixed-lift Gram descent no-go.

12. `main.tex:5704-5716`: source/target distinction in the compact
    realization section.

13. `main.tex:6024-6140`: compact \(E_3\) source interface is finite-first
    datum, not nonemptiness.

14. `main.tex:6404-6504`: target-internal bar--cobar counit does not
    construct the source coalgebra.

15. `main.tex:6506-6728`: chiral Koszul source certificate lists source
    coalgebra data and residuals.

16. `main.tex:7039-7119`: projection-finite/wrapped distinction and
    support-locality obstruction.

17. `main.tex:7121-7144`: finite hybrid local/wrapped factorization is a
    certificate datum.

18. `main.tex:8254-8303`: hybrid wrapped factorization remains open.

19. `main.tex:8540-8600`: multiplicative orientation criterion is
    restricted and conditional; full compact/wrapped orientation remains
    open.

20. `main.tex:8603-8724`: normal-ordered Hall descent theorem assumes a
    supplied oriented Hall/factorization object and correspondences.

21. `main.tex:9887-9971`: finite charge-support Hall quotient is
    conditional on support, HN, finite type, and oriented correspondences.

22. `main.tex:9973-10080`: \(D_0\)-certificate assumes finite-type
    \(K3\times E\) substacks and finite d-critical/cosection Hall atlas.

23. `main.tex:10946-10991`: source computation of Igusa exponents is
    open; a detached \(K_0\) shadow is insufficient.

24. `main.tex:10994-11174`: supplied finite Hall source kernel determines
    finite state-side Hall object, product, coproduct, primitives, and
    CE differential. The kernel itself is not constructed.

25. `main.tex:11750-12122`: Dirac--Igusa realization certificate is a list
    of data, not a consequence of determinant, OP square, target current
    envelope, target bar--cobar counit, or orientation lines alone.

26. `main.tex:12124-12446`: primitive recognition theorem assumes source
    presentation data; it is explicitly "no source construction."

27. `main.tex:13276-13310`: state-side construction of \(D_0\) and the
    Dirac--Igusa certificate is open.

28. `main.tex:14031-14190`: claim-strength synthesis states determinant,
    normal-ordering, denominator, scalar square, and compact comparison
    status correctly.

29. `main.tex:14289-14336`: physical-host certificate separates
    automorphic product, denominator, scalar square, reduced CY/DT host,
    and compact Hall/chiral host.

## Patch queue

1. Add a short section after the introduction titled "Constructed Objects,
   Not Certificates."

2. Introduce notation
   \[
   H^{\mathrm{pre}}_{X,\Gamma},\qquad
   H^{\mathrm{tw}}_{X,\Gamma},\qquad
   \mathcal F^{\mathrm{hyb,pre}}_{X,R},\qquad
   \mathcal F^{\mathrm{hyb,tw}}_{X,R}.
   \]
   State explicitly which are constructed, conditional, or open.

3. Add a theorem "Geometric normal-ordered Hall correspondence source"
   if willing to claim the derived correspondence object. Keep it
   pre-integrated and non-numerical.

4. Add a definition of orientation gerbe and tautological square-root line
   before the strong orientation certificate. Recast global orientation as
   a section/trivialization.

5. Rewrite the protected Hall section so \(H^{\mathrm{tw}}\) is the object
   consumed by primitive recognition, not an unnamed supplied
   \(\mathcal F_X\).

6. Split "twisted source exists" from "untwisted Pfaffian theory exists."
   The first lives over the \(\mu_2\)-gerbe; the second requires a global
   orientation/trivialization and monodromy computation.

7. Move the hybrid certificate language under a constructed
   local/wrapped correspondence category. The certificate then records
   properness, TS, quotient, integration, and transition residuals.

8. Keep the source/target firewall table near the compact section:
   target current envelope, target bar--cobar counit, scalar square,
   and denominator algebra are not compact source constructions.

9. Replace any wording of the form "the compact object is the certificate"
   by "the certificate is the finite list of data whose construction would
   produce the object."

10. Add the minimal theorem queue:
    Theorem 1 normal-ordered charge algebra; Theorem 2 geometric pre-Hall
    source; Theorem 3 orientation-gerbe-twisted Hall construction
    conditional on protected integration; Theorem 4 hybrid source;
    Theorem 5 source coalgebra; Theorem 6 compact realization comparison.

## Residual proof obligations

1. Prove or explicitly assume that the chosen charge substacks
   \(M_c\subset\mathrm{Perf}^{\mathrm{cpt}}(X)\) are derived Artin, locally
   manageable, and open-and-closed by the charge labels used.

2. Prove the exact-triangle stacks \(E_{\hat c,\hat c'}\) and flag stacks
   are derived Artin correspondences with the required functoriality.

3. Prove associativity of \(H^{\mathrm{pre}}\) as an algebra object in the
   relevant correspondence 2-category, not just as equality of labels.

4. Prove finite HN boundedness for the \(K3\times E\) stability/HN sector,
   including the base Picard/Bun direction. Current text correctly notes
   this is not supplied by fibrewise K3 boundedness alone.

5. Prove finite residual inertia or provide a quotient/rigidification that
   makes protected cohomology finite-dimensional. Residual
   \(B\mathbb G_m\) kills finite-dimensionality.

6. Supply a compact-support six-functor formalism in which the \(p^*\),
   \(p_!\), \(q^*\), and \(q_!\) operations used by Hall product and
   coproduct are admissible. Properness is sufficient but not the only
   possible route.

7. Construct vanishing-cycle/BPS sheaves on the finite d-critical
   truncations and prove Thom--Sebastiani compatibility on two-step and
   higher colored flags.

8. Construct the orientation gerbes, their tautological lines, and the
   lifted correspondences. Prove multiplicativity as a gerbe morphism or
   track its twist.

9. Prove the quotient-stack integration over
   \([\operatorname{Or}_{R,\hat c}/E]\) retains finite stabilizer inertia
   correctly and identify the scalarization/trivial-character projection
   only when needed.

10. Prove the hybrid wrapped anchor is functorial enough for LW/WL/WW
    correspondences, and prove the eight flag associativity coherences.

11. Prove quotient-after-correspondence compatibility \(Q_{E,R}\) for all
    local/wrapped operations and transitions.

12. Construct \(C^{\mathrm{tw}}_{X,R}\) from the hybrid source, prove
    conilpotence, source filtration, collision coproduct identities, and
    Mittag--Leffler exactness in the inverse system.

13. Prove the normal-ordering cochains act on actual correspondence
    targets, not merely on lattice labels, and satisfy the Hochschild,
    cyclic, Jacobi, Frobenius, and radical compatibilities.

14. Compute source primitive dimensions and parity splits from the compact
    source, beginning with the wrapped degree \((0,1,1)\). A detached
    one-dimensional \(K_0\) class is not a wrapped primitive.

15. Supply primitive representatives for all real and imaginary simple
    roots, verify Borcherds--Kac relations in the Hall bracket, prove
    generation, no-extra-relations, completed PBW, Hopf radical equality,
    and exact completion.

16. Prove the orientation monodromy character from the Hall determinant
    line and type-II wall charts, then compare it with
    \(\nu_{\Delta_5}\). This is not a normalization check.

17. Prove the source Pfaffian equals \(\Delta_5\) only after the primitive
    comparison and orientation/Pfaffian line comparison. Then, and only
    then, compare the orientation-forgetting scalar trace with the OP/DT
    branch \(-4096\Delta_5^{-2}\).
