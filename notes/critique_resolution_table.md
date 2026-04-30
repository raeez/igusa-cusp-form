# Critique resolution table

Date: 2026-04-30.
Source: `notes/attack_whitepaper_analysis_20260430_guide.md`.

Internal audit ledger.  The manuscript remains standalone and must not
refer to this file.

Supremum discipline: a failed overclaim is not resolved by weakening as
an end state. The resolution target is the strongest true theorem obtained
by adding the missing construction, hypothesis, calculation, or citation.
Conditional status below is a proof-ledger marker until the stronger
mathematical statement is proved or a precise obstruction is established.

| Objection | Current resolution in `main.tex` | Remaining status |
|---|---|---|
| \((n,l,m)\) was used as physical charge, Fourier/root degree, and Hall degree. | `main.tex` separates \(\Gamma_X^{\mathrm{phys}}\), \(\Gamma_{\mathrm{gram}}\), raw \(\Pi_X\), and \(\widehat\Gamma_X\). | Lattice theorem repaired. Compact Hall source still open. |
| Raw Gram descent is not additive. | The normal-ordered homomorphism \(\overline\Pi_X(c,T)=\Pi_X(c)-T\) is theorem-level. | Chain-level \(\Theta_\Pi\) construction remains open. |
| Raw \(\Pi\)-descent might still be presented as optional. | The raw-descent no-go theorem shows it cannot realize full BKM real-root strings. | Formal obstruction repaired. |
| The D6-D2-D0 dictionary used fourfold/Todd-correction language. | The CY3 Mukai-Gram theorem gives \(v_X(I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E\) and \(\Pi_X(Q_Y,P_Y)=(h-1,n,d-1)\). | Computation repaired; keep central. |
| The algebraic even Mukai sector was called the full physical charge lattice. | The abstract and charge sections now distinguish the algebraic D6-D2-D0/OP sector from larger full \(N=4\) charge data. | Wording repaired; check every occurrence. |
| Orientation data was treated as construction of \(\mathfrak D_X\). | Dirac-Pfaffian statements are conditional on supplied \(D_0\), (O1), (O1)+, and (O2). | Compact first-order object remains open. |
| OP minus sign and \(4096\) were blurred with orientation data. | OP/DT scalar normalization is stated as orientation-forgetful and not evidence for Hall monodromy. | Wording repaired; orientation character still to compute. |
| Connected \(BE\) and finite \(BE[2]\) were conflated. | The equivariant obstruction package separates \(H^1(BE)=0\), \(H^2(BE)\), and \(H^2(BE[2])\). | Finite-stabilizer linearization still open. |
| Translation invariance was treated as equivariant linearization. | The orientation package distinguishes ordinary line invariance from \(E[N]\)-linearization characters. | Character computations remain open. |
| Holomorphic \(E_3\) was underdefined. | The text distinguishes holomorphic factorization, local \(E_3\)-shadow after formality/framing, and supplied specialization. | Actual compact source remains open. |
| Projection-to-\(E\) support-locality was called a generic locality failure. | `main.tex` states positive elliptic degree is wrapped/global after projection, not failure of locality on \(X\). | Hybrid object remains open. |
| Hybrid wrapped factorization was a slogan. | The finite hybrid certificate names ordered local/wrapped correspondences, anchors, quotient residuals, and protected integration residuals. | Construction remains open. |
| Primitive recognition was close to a dimension count. | Recognition now requires presentation, parity, relations, Hopf radical, no-extra-relations, PBW, and finite-window checks. | Global primitive recognition remains open. |
| The formal current envelope looked like compact geometry. | It is now named as an imported target/current envelope, not a compact Hall source. | Wording repaired. |
| Boundary rows could distract from the \(N=1\) theorem. | Boundary rows are treated as independent certificates. | Decide later whether to split into companion paper. |
| Spin \(L\)-factor material invites irrelevant audit. | Appendix is marked independent of the Dirac-Igusa construction. | Consider moving to separate note. |
| Fixed weak Liu numerical class was treated as a finite compact Hall source. | New intake requires retained Liu-Hilbert classes \(\Xi=(\gamma,[a,b],(P_i),N)\) for any finite-stage construction. | Full fixed-class Liu boundedness remains open; retained finite stages are the only admitted theorem lane. |
| Retained finite stage could be mistaken for the unrestricted compact theorem. | The guide separates retained finite-stage boundedness from cofinal compact realization. | Every theorem statement must name retained hypotheses and cofinality data. |
| Hall multiplication was described before compactified retained correspondences existed. | New plan requires finite retained moduli, compactified extension stacks, full flag stacks, and proper source/target maps. | Properness, d-critical structures, vanishing cycles, and orientation coefficients remain to prove. |
| Eight LL/LW/WL/WW words were treated as full hybrid factorization. | New plan demands colored tree flag stacks, units, symmetry/order conventions, refinement maps, descent, and overlap coherences. | Hybrid factorization remains a finite-stage construction target. |
| Orientation line was treated as primitive input. | New plan moves to orientation-gerbe-first source: construct the gerbe, then ask for sections, quotient descent, and finite-stabilizer linearization. | Actual obstruction classes and stabilizer characters remain to compute. |
| Type-II wall signs were read from automorphy or scalar data. | New plan requires retained wall atoms, local charts, reduced Ext complexes, splittings, units, and Pfaffian ranks. | The wrapped middle wall \(\delta_2\leftrightarrow(0,1,1)\) is only a candidate until semistability, charge matching, and quotient orientation are proved. |
| \(W_{\le3}\) target arithmetic was treated as compact source data. | New plan requires source matrices \(M,D,B,G,K,Q\), radical/quotient maps, pairings, and source-built comparison maps \(A_\beta\). | Target scripts verify target arithmetic only; source matrices remain to construct. |
| Target bar-cobar was allowed to suggest source coalgebra. | New plan enforces source/target firewall: \(C_X\) and \(\Theta_{\mathrm{Kos}}\) must be source-built or explicitly target-internal. | Source chiral coalgebra remains conditional on retained Hall source data. |
| Dirac block algebra was treated as compact operator construction. | New plan treats \(D_\beta^X=\begin{psmallmatrix}0&1-x_\beta\\1&0\end{psmallmatrix}\) as finite algebraic model conditional on source primitives. | Pfaffian equality remains conditional on parity-preserving cofinal primitive comparison. |
| \([B]\) was at risk of being read as nonzero ordinary group cohomology. | A019 shows \(B=-\delta\Pi_X\); the extension is abstractly split. | Rewrite any \([B]=[B_{\mathrm{ch}}]\) language as degree-shadow/Hochschild-trivialization data. |
| Normal-ordered primitives were labelled raw. | A020 separates raw \(\Pi_X\)-pushforward from \(\overline\Pi_*^\Theta\)-descended primitives. | Rename \(P_X^{\Pi,\mathrm{raw}}\) to \(P_X^\Pi\) or \(P_X^{\Pi,\mathrm{preRad}}\). |
| A BKM root \(\beta\) was used as a Gram coordinate. | A020 requires \(\gamma_\beta\in\Gamma_{\mathrm{gram}}\) and a separate normal-ordered lift. | Patch all \(\overline\Pi_X(\beta)\) and \((0,-\beta)\in\widehat\Gamma_X\) occurrences. |
| Finite global \(\overline\Pi\)-fibres were implicitly assumed. | A022 shows finiteness only at fixed HN height \(R\); global pushforward is a completed inverse limit. | Add ML, closed radical, and transition hypotheses wherever a global pushforward is used. |
| Compact Hall product was inferred from source/target maps. | A025/A027/A028 require retained Liu-Hilbert schedules, compactified closed-filtration/flag-Quot stacks, or explicit exceptional \(q_!\). | Rewrite retained Hall theorem as supplied finite atlas theorem; do not infer properness from raw exact triangles. |
| Finite type plus d-critical/BBDJS was read as finite cohomology. | A026/A029 separate finite residual inertia, characteristic-zero coefficients, compact support, and finite cohomological dimension. | Keep finite protected cohomology as an input or prove it for every retained stratum. |
| Full global recognition followed from finite checks. | A030 requires strict transition compatibility, finite-slice ML, closed radicals, and PBW strictness. | Demote to pro-comparison unless all limit hypotheses are supplied. |
| Local/wrapped color was assigned by \(m_{\mathrm{Bch}}\). | A031 shows source color is \(b_R^{\mathrm{geom}}\), not the third Gram exponent; \(m_{\mathrm{Bch}}=0\) can mean \(d_E=1\). | Patch formal colored normal form and table labels before source geometry uses them. |
| Wrapped determinant anchor was treated as enough for legal quotient/properness. | A032 shows anchor transport, translation weight, induced subobject/quotient/flag maps, and closedness are extra data. | Replace "anchor imposed as closed condition" by an explicit finite-stage anchor-transport axiom package. |
| Quotient orientation could be inferred from finite edge tests. | A037-A042 show the Cech-Borel criterion separates ordinary gerbe, connected \(BE\), finite Borel edge, degree-one characters, overlaps, correspondences, flags, TS, and transitions. | Keep O1/O1+/O2 conditional; compute every class on actual retained strata. |
| Type-II wall atoms were treated as constructed. | A043-A045 show \(\delta_i\) are target roots plus conditional rank-one local models; reducible/graph-isogeny geometries are candidates only. | Do not call any \(\delta_i\) atom constructed until wall objects, semistability, full charge, reduced Ext, orientation, unit, and overlaps are proved. |
| Pfaffian wall sign was inferred from Maass/divisor/scalar data. | A046/A047 preserve the firewall: Maass and divisor orders are target data; local rank-one Ext is conditional; OP constants are scalar normalization. | State \(\epsilon_o=\nu_{\Delta_5}\) only under supplied O1/O1+/O2 plus independent Maass computation. |
| Primitive recognition was still vulnerable to target dimension matching. | A049/A052/A055/A056 show \(1|0,10|0,1|0,29|93\) and \(29-93=-64\) are target arithmetic, not compact source construction. | Source recognition needs neutral basis ids, provenance, \(M,D,B,G,K,Q\), \(A_{\beta,\bar p}\), no-extra-relations, PBW, and transitions. |
| Chevalley, Serre, and Borcherds relation rows were target-importable. | A050-A052 show GN/Kac supplies the target presentation only; source relation rows must be Hall bracket matrices after quotienting by the radical. | Verify Chevalley, real Serre exponent \(3\), isotropic orthogonality, complementary exponent \(5\), mixed rows, and \(T_1+T_2+T_3=0\) from source matrices. |
| Hopf radical descent was allowed to imply the rest of recognition. | A053/A054 show radical ideal/coideal checks make the quotient legitimate but do not prove kernel equality, PBW, or no-extra-relations. | Add explicit \(QB(P\otimes K)\), \(QB(K\otimes P)\), \((Q\otimes Q)DK\), quotient tensor nondegeneracy, kernel equality, and PBW associated-graded checks. |
| Target basis labels risk becoming source basis names. | A056 quarantines \(e_i,E_{ij},u_{ij,r},Y_{i;ij},T_i,M_{ij,r},w_s\) as target fixtures or codomain labels for \(A_{\beta,\bar p}\). | Use neutral source labels \(b^X_{R,\beta,\bar p,a}\) until \(Q\) and \(A_{\beta,\bar p}\) map them to target basis vectors. |
| \(W_{\le3}\) was treated as relation-closed. | A063-A066 show no-extra/PBW can be checked in \(W_{\le3}\) only for rows whose outputs remain there; real Serre, doubled-isotropic, and complementary-string terminal rows require heights \(4\) through \(7\). | Add an enlarged downward-saturated \(W_{\le7}\) source certificate, or explicitly separate the \(W_{\le3}\) first-window theorem from terminal relation closure. |
| GNII was overused as algebra-construction citation. | A068 shows GNII supplies explicit product-lift data, while GN Sections 3-4 / Proposition 3.1 supply the Lorentzian automorphic correction algebra; Borcherds 1988 should support the generalized Kac-Moody presentation convention. | Patch the proof near the denominator-algebra theorem and add the Borcherds GKM citation in the presentation section. |
| Conditional recognition lacked a supremum theorem ladder. | A069 reconstructs the target theorem sequence: finite \(W_{\le3}\) certificate, relation-closed \(W_{\le7}\) certificate, cofinal ML completion, and compact Dirac-Igusa realization corollary. | Rewrite the recognition section around this ladder so conditional status marks missing certificate data rather than weakening the intended theorem. |

## Remaining proof obligations

1. Construct the compact first-order Dirac-Igusa \(D_0\) datum.
2. Construct strong reduced orientation (O1) on compact/wrapped sectors.
3. Prove Weyl-equivariant orientation transport (O1)+.
4. Compute the type-II Pfaffian local wall model (O2).
5. Prove finite \(E[N]\)-linearization characters, including \(E[2]\).
6. Construct \(\operatorname{Ran}^{\mathrm{hyb}}(E)\) and its ordered
   local/wrapped correspondences.
7. Lift normal ordering from lattice level to chain-level Hall descent.
8. Prove primitive recognition against \(\mathfrak g_{\Delta_5}\) at
   presentation level, including no-extra-relations, radical quotient,
   and completed PBW.
9. Replace weak fixed-class compactness with retained Liu-Hilbert finite
   stages and state full fixed-class Liu boundedness as an open theorem.
10. Build compactified retained Hall correspondences and full flag stacks.
11. Prove quotient-after-correspondence for the hybrid local/wrapped base.
12. Compute retained type-II wall atoms, especially the wrapped middle
   wall \(\delta_2\leftrightarrow(0,1,1)\).
13. Construct the first \(W_{\le3}\) source table: bases, \(M,D,B,G,K,Q\),
   radical kernels, quotient maps, and comparison maps \(A_\beta\).
14. Prove finite-window transition identities and Mittag-Leffler stable
   image conditions for the cofinal retained tower.
15. Patch the \([B]\)-cohomology language and raw/pre-radical notation.
16. Replace \(m_{\mathrm{Bch}}\)-based local/wrapped color by
   \(b_R^{\mathrm{geom}}\) plus retained support/anchor data.
17. Supply wrapped anchor-transport diagrams for inputs, outputs,
   quotients, and flag intermediates before quotienting by \(E\).
18. Compute the Cech-Borel orientation descent package on every object,
   extension, mixed/wrapped, flag, and transition stratum.
19. Construct or demote the \(\delta_1,\delta_2,\delta_3\) wall atoms;
   current reducible/graph-isogeny models are candidates only.
20. Prove the equivariant reduced Morse normal form and invariant
   Pfaffian unit before any type-II sign theorem is reader-facing.
21. Quarantine all target basis labels from source basis provenance until
   explicit \(Q\) and \(A_{\beta,\bar p}\) matrices exist.
22. Prove source Chevalley, Serre, isotropic, complementary-string, and
   mixed relation rows by Hall product/bracket matrices.
23. Prove Hopf radical ideal/coideal descent by finite matrix identities,
   quotient tensor nondegeneracy, and transition-compatible kernels.
24. Prove \(W_{\le3}\) no-extra-relations by kernel equality against the
   BK plus GN radical ideal.
25. Prove \(W_{\le3}\) PBW by associated-graded rank/isomorphism checks,
   not by target multiplicity tables.
26. Enlarge the relation-checking source certificate through height \(7\)
   for terminal real-Serre, doubled-isotropic, and complementary-string
   rows.
27. Patch GN/GNII/Borcherds/Kac citation boundaries so product,
   automorphic correction algebra, presentation, and PBW conventions are
   sourced independently.
28. Reorganize primitive recognition into a four-step theorem ladder:
   \(W_{\le3}\) certificate, \(W_{\le7}\) closure, cofinal ML completion,
   and compact Dirac-Igusa corollary.
