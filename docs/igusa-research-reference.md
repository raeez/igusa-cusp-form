# Igusa research reference

Read the sections relevant to the mathematical claim under review.
This reference preserves the mathematical conventions and conditional obligations.
Verify status against the current theorem and retained-data ledgers before asserting completion.

## I. The thesis

The programme relates the Igusa cusp form Δ_5 of weight 5 on Sp(2,ℤ)\𝓗_2
to five descriptions. The compact chiral E_3-algebra **𝔄_{K3×E}** remains conditional
on retained data. The obstruction criteria below control the status of each description:

  ① **Automorphic.** Δ_5 is the Borcherds–Gritsenko–Nikulin section of the weight-5
     automorphic line over the genus-2 Siegel space.
  ② **Borcherds–Kac–Moody denominator.** Δ_5 is the denominator of a generalized
     Borcherds–Kac–Moody Lie superalgebra g_{Δ_5} on the root lattice Λ_{II}^{2,1}.
  ③ **Compact Pfaffian.** *(Conditional on retained data.)* Δ_5 is the protected Pfaffian of 𝔄_{K3×E}, presented at
     finite stage as the pro-object 𝔇_X^DI = lim_R (𝒜_{X,R}^{E_3}, F_{X,R}^{hyb},
     Γ_{X,R}, Π_X, Φ_R, o_R, H_R, P_R^Π, C_{X,R}, Θ_{Kos,R}, ℒ_{Pf,R}, pf_{X,R},
     ε_{o,R}, Rec_R) with eight build algorithms and four named obstructions.
  ④ **Mirror discriminant.** *(Conjectural.)* Δ_5^{-2} is the discriminant of the
     K3-mirror period family; the Igusa programme then sits inside mirror symmetry on
     K3×E.
  ⑤ **Singular theta lift.** Δ_5 is the lift of the weight-zero index-one weak Jacobi
     form φ_{0,1} under the Howe correspondence Mp(4,ℝ) ↔ O(3,2), bridged by the
     exceptional isomorphism Sp(4) ≅ Spin(3,2).

The cross-level identities ①↔②, ②↔⑤, ①↔⑤ are theorems (Borcherds 1995,
Gritsenko–Nikulin 1998). The cross-level identity ②↔③ — the Pfaffian–Dirac theorem —
is the conditional contribution of this manuscript: under (D0), (O1), (O1⁺), (O2),

  Pf_{prot}(𝔇_X^DI) = Δ_5,    ε_o = ν_{Δ_5},    P_X ≅ g_{Δ_5}.

The level-n scalar shadow Z_BPS^{K3×E} = (Φ_{10}^{un})^{-1} = Δ_5^{-2} on the closed
K3×E ↦ point cobordism is the BPS partition function; promotion to a 3d gravitational
path integral requires the Hall–Borcherds residual (Vol II) and is not claimed.

## II. The chapter spine

| Part | Ch. | Content |
|---|---|---|
| Frontispiece | — | Five-fold thesis (~50 lines) |
| 0 — Road map | 1 | Pentadic Δ_5 (~300) |
| I — Given | 2 | K3×E setup, Mukai dictionary, lattice polarization, normal-ordered Gram, hybrid Ran^{hyb}(E) carrier (~1500) |
| | 3 | Borcherds–Gritsenko–Nikulin import (View ①) (~800) |
| | 4 | BKM denominator algebra g_{Δ_5} (View ②): Cartan, Chevalley, real and imaginary roots, denominator identity (~2500) |
| | 7 | Singular theta lift (View ⑤); Sp(4) ≅ Spin(3,2) bridge (~600) |
| II — Built | 5 | The Dirac–Igusa pro-object 𝔇_X^DI (View ③) — §5.1 Ran^{hyb}(E); §5.2 cosection-twisted reduced d-critical orientation; §5.3 Hall correspondences; §5.4 Dirac + Pfaffian; §5.5 Koszul source coalgebra; §5.6 primitive recognition; §5.7 eight build algorithms; §5.8 four obstructions (~5000) |
| III — Certified | 6 | The cross-level identity ②↔③: the Pfaffian–Dirac theorem, ε_o = ν_{Δ_5}, the primitive recognition theorem P_X ≅ g_{Δ_5} (~3000) |
| IV — Shadowed | 8 | Mirror discriminant (View ④, conjectural) (~400) |
| | 9 | Z_BPS^{K3×E} = Δ_5^{-2}; Hall–Borcherds residual; the K3×E threefold realization question (~1000) |
| | 10 | Open obstructions and the next frontier — Mathieu / umbral moonshine adjacency (~500) |
| Appendices | A–F | Lattice computations; Borcherds-product expansion; Mukai–Gram dictionary; Hall-correspondence proofs; Pfaffian wall normal-form; eight build algorithms in pseudocode (~3000) |

The chapter map and approximate line counts record the original plan. Inspect current sources for the active chapter structure.

## III. The Beilinson cut

A statement is not allowed to be primitive if it is only true after choosing a boundary
object, passing to a trace, averaging from ordered to symmetric, taking a protected
index, completing a category, imposing endpoint hypotheses, or installing descent data.
**Reconstitution order: primitive objects first, cross-level identities second, scalar
shadows last.**

Every load-bearing claim locates itself on one of two chains, which are the same chain
seen from two entry points, meeting at the holomorphic factorization algebra Φ_d^{FA}:

```
(X, D, τ) → C^op → b → A_b → Bar(A_b) → Z^{der}_{ch}(A_b) → Tr_C / Θ_C → scalar
CY_d-cat → E_d-HolFA(X) → Sp^{ch}_{Σ_{d-1}, C} → chiral shadow → Y^+ → G → κ-tuple
```

**Banned identifications.** Each row is a categorical-dimensional level confusion;
use the distinction in the right column when reviewing the affected claim.

| Banned | Required |
|---|---|
| "the boundary algebra A is the primitive open object" | "C is the primitive factorization dg-category on (X, D, τ); A_b = End_C(b) is the chart at boundary vacuum b" |
| "Bar(A) = bulk" | "Bar(A) = MC twisting / coupling coalgebra; Z^{der}_{ch}(A) ≃ ChirHoch^•(A,A) = bulk" |
| "the closed chiral algebra is modular" | "the open category carries cyclic trace + clutching; the closed shadow has modular consequences" |
| "the κ-invariant of K3×E" (singular) | "the κ-tuple (κ_cat, κ_ch^Hodge, κ_ch^Heis, κ_BKM, κ_fiber) = (0, 0, 3, 5, 24) — cat-Hodge / refined-Hodge / Heisenberg rank / cusp-form weight / χ_top(K3). The additive collapse κ_BKM = κ_ch + χ(O_fiber) confuses χ_top(K3) = 24 with χ(O_K3) = 2 and fails at N = 1 (Vol III counterexample)." |
| "Δ_5 = compact BPS Hilbert space" | "Δ_5 is the protected scalar shadow of 𝔄_{K3×E}; the operator-level package is 𝔇_X^DI as a pro-object, conditional on (D0), (O1), (O1⁺), (O2)" |
| "Z_BPS = 3d gravitational path integral" | "Z_BPS is the level-n protected trace of 𝔄_{K3×E}; the path-integral promotion requires the Hall–Borcherds residual and is not claimed" |
| "Universal Holography constructs quantum gravity" | "Universal Holography identifies (boundary = A, bulk = Z^{der}_{ch}(A), interaction = SC^{ch,top}-brace); for A = Vir_c this is the holographic HT sector of pure 3d gravity, not the dynamical metric path integral" |
| "Y^+(X) = G(X)" | "Y^+(X) is the Hall positive half; G(X) is the Drinfeld double, after pairing / completion / integral form / stable-envelope transport" |
| "CoHA(ℂ³) = W_{1+∞}" | "CoHA(ℂ³) = Y^+(gl_1); W_{1+∞} appears after Drinfeld doubling / centre / vacuum evaluation" |
| "6d hCS = 3d Chern–Simons in disguise" | "6d hCS supplies Φ_3^{FA} on verified loci; the one-loop obstruction is ∫_X Tr_{ad}(A(F_A)^3), quartic" |
| "formal local Hamiltonian BF ⇒ global compact target" | "formal Darboux + descent / QME / anomaly / locality + (local Hamiltonian or vanishing holomorphic de Rham obstruction) ⇒ candidate compact target" |
| "PVA λ-Jacobi ⇒ all-loop quantum HT theory" | "λ-Jacobi gives classical gauge invariance; all-loop quantum theory needs KZ analytic SDR + Stokes + reflected weights + lift of T = [Q_{tot}, G]" |
| "W_∞[λ] ⇒ E_∞ from finite spin checks" | "spin-≤8 checks are evidence; the E_∞ endpoint is conditional on Prochazka triangular truncation, Creutzig–Kanade–Linshaw parafermion compatibility, Pope–Romans–Shen / Bakas, Yamada weight-window" |
| "quadratic chiral duality = chiral Koszul duality" | "Hom(A,B) ↪ MC(A^! ⊗ B) injection; Koszulness is the separate theorem in a homotopy setting" |
| "class M works chain-level in ordinary complexes" | "class M holds in the completed ambient (analytic HS-sewing / coderived BV = bar / weight-completed / pro / J-adic)" |
| "smooth projective fourfold" (in §5) | "K3×E threefold; n = χ(O_Y) directly" |
| "Bott-element B(c, c) = 2 Π(c) explanation" | "lattice polarization B is the full structural content; the Bott-element framing is removed" |
| "the OP minus sign sources the orientation character" | "the OP minus sign is a scalar branch convention; ε_o = ν_{Δ_5} on W^{(2)}(Λ_{II}^{2,1}) is fixed by group theory + one local Pfaffian wall computation" |

Three Δ_5 names live in the manuscript and must be tagged distinctly on first use per
chapter: the automorphic section D_X = Δ_5 (View ①); the BKM denominator
den(g_{Δ_5}) = 64^{-1} Δ_5(2Z) (View ②); the compact protected Pfaffian
Pf_{prot}(𝔇_X^DI) (View ③, conditional). The handle "Δ_5" alone never substitutes for
any of the three.

## IV. Voice and standards

`~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`
governs mathematical manuscript prose. Operational reports remain outside manuscript sources. The seven combined voices are Witten,
Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto. A sentence that does not state
mathematics or physics is a defect.

Standard-terminology rule (`writing standard §II`): the accepted name in algebra, geometry,
number theory, homotopy theory, or mathematical physics is the default. Coining
requires the four-part test (`writing standard §III`): scope (no accepted name covers it),
material (precise mathematical object, not attitude or workflow), subject (Greek/Latin
or composition with accepted prefixes), inner yearning (the structure forces the name).
Most failures of writing in this constellation come from coining terms that have an
accepted mathematical name; the accepted name is the default; the coining bears the
burden of proof.

Binding terminology for this manuscript: Igusa cusp form, Siegel modular form,
Borcherds product, theta lift, Borcherds–Kac–Moody (BKM) algebra, denominator formula,
Weyl–Kac character formula, factorization algebra (Beilinson–Drinfeld; not synonymous
with vertex algebra or chiral algebra), vertex operator algebra, chiral algebra
(`D`-module on a curve), derived chiral centre Z^{der}_{ch}(𝒞), perfect obstruction
theory, virtual fundamental class [X]^{vir}, Mukai vector, Mukai lattice, Donaldson–
Thomas (DT) / Pandharipande–Thomas (PT) / Maulik–Nekrasov–Okounkov–Pandharipande
(MNOP), CHL (Chaudhuri–Hockney–Lykken) point. The handle "Δ_5" works in this repo;
in manuscript prose specify "Φ_{10}^{1/2}" or "the level-five Borcherds–Kac–Moody
denominator" on first occurrence per chapter. Φ_{10} = χ_{10}.

Banned rhetorical patterns (`writing standard §V`): meta-narration ("we now turn to"),
bookkeeping ("Theorem A, Theorem B"), catalogue IDs ("phase j", "wave N", "round M"),
branding ("matrix microscope", "magic identity", "inner music", "X spine"), hedging
("we believe", "essentially", "arguably"), negative framing for identifications ("would
collapse", "cannot identify"), approximation language for exact equalities ("is closely
related to" when "$=$" holds), computer-science vocabulary ("certificate" → "identity"
or "theorem"; "pipeline" → "construction"; "spec", "schema", "API", "metadata"
forbidden in body prose).

Honest epistemic status on every load-bearing claim: *proved / conjectured / heuristic
/ computed / expected / folklore / unverified*. Use *one proves* for proved statements,
*it is expected that* for conjectures, *heuristically* for physics arguments without
mathematical footing — followed by whatever rigour is available. Mathematical-repair
doctrine (`INVARIANTS.md §XI`): heal the proof, statement, or construction; never
delete, demote, or quietly narrow scope as a way to close a defect.

## VI. Research constellation

| Repo | Role | Interaction with this repo |
|---|---|---|
| `~/chiral-bar-cobar` | Vol I — Modular Koszul Duality (bar / cobar, Koszul) | Bar / Z^{der}_{ch} firewall; class M completion; chiral Koszulness as separate theorem. den(g_{Δ_5}) is a chiral shadow, not bulk. |
| `~/chiral-bar-cobar-vol2` | Vol II — A_∞-Chiral Algebras and Chiral Hochschild Cohomology | Primitive package (X, D, τ; C^op, b, A_b, Z^{der}_{ch}(C), Θ_C, Tr_C); Universal Holography master theorem (boundary = A, bulk = Z^{der}_{ch}(A), interaction = SC^{ch,top}-brace); modular functor as trace + clutching; Hall–Borcherds residual; KZ analytic SDR for finite-jet PVA. |
| `~/calabi-yau-quantum-groups` | Vol III — Calabi–Yau quantum groups / κ-stratification | κ-ladder (0, 0, 3, 5, 24); two-stage CY_d-Cat → E_d-HolFA(X) → ChirAlg(C); Drinfeld doubling Y^+ → G; 6d hCS quartic obstruction. The κ_BKM = 5 entry is this manuscript's value; the 8-row Gritsenko–Cléry catalogue carries the row producing Δ_5. |
| `~/chiral-bar-cobar-vol4` | Vol IV — Realization | Modular functor at level 5; scalar partition function at level n. |
| `~/mixed-holomorphic-topological-strings` | BCOV / Kodaira–Spencer companion | Local model ℝ²_{top} × ℂ²_{hol} + brane completion; global obstruction = holomorphic de Rham obstruction class. Z_BPS^{K3×E} = Δ_5^{-2} does not promote to the global target via formal Hamiltonian BF; Vol II's Hall–Borcherds residual carries the bridge. |

Load-bearing claims about Δ_5, φ_{0,1}, Borcherds-product exponents, the BKM
denominator, or the κ-ladder must be consistent across these repos. Disagreement is the
deliverable; report, do not silently reconcile.

## VII. Obstruction criteria (Appendix G)

The cross-level identity ②↔③ on K3×E is **conditional**: Appendix G proves
criterion theorems (granted the retained data), not discharges. The retained
obstruction datum (D0_HN, O1_quot, 𝒯_W, O2_atlas, P_fin, Z_HB) is *chosen*, and
the repo's own certificate ledgers record its components as unsupplied
(`certified:false` absence ledgers; App G).

| Obstruction | Statement | Criterion theorem (granted the retained data) |
|---|---|---|
| (D0) | D0-degeneration limit of the cosection-reduced d-critical orientation theory | "(D0) criterion" (`thm:G-D0`): reduction to the retained D0-HN datum (Joyce–Upmeier + Bojko + Mittag–Leffler technology) |
| (O1) | Strong reduced orientation on the K3×E-quotient self-Ext frame bundle | "(O1) quotient-orientation criterion" (`thm:G-O1`) + Klein-four / two-primary detection lemmas (`lem:G-Klein-four`, `lem:G-two-primary-stabilizer`) — the lemmas are proved but do not construct the null-trivialisations |
| (O1⁺) | Weyl-equivariant transport along W^{(2)}(Λ_{II}^{2,1}) reflections | "(O1)⁺ Weyl transport criterion and type-II character comparison" (`thm:G-O1-plus`): W^{(2)} ≅ ℤ/2∗ℤ/2∗ℤ/2 (universal Coxeter group; off-diagonal Cartan entry −2 is an infinite Coxeter exponent, **no order-three braid relation**), abelianisation (ℤ/2)³, Maass character match on the three generators granted the (O2) wall signs |
| (O2) | Local Pfaffian wall normal form + (R1)↔(R2) reconciliation | "(O2) wall-atlas consequence / scalar separation / orbit transport" (`thm:G-O2-normal-form`, `thm:G-R1-R2`, `thm:G-O2-orbit-transport`); the 2¹² = 4096 = 64² wall count is stipulated in (O2_atlas), not derived |

The Vol II Hall–Borcherds residual splits by level on the universal stage chain.
The **level-𝖹 facet** — chain-level CY-orientation trace pairing on
Z^{der}_{ch}(C_X) — is a criterion theorem, not a discharge: "Level-𝖹
Hall–Borcherds trace criterion on K3×E" (`thm:G-vol2-discharge`; the label's
"discharge" is a healing fossil). Granted the retained trace datum (Z_HB)
(clauses (Z1)–(Z5), **not supplied** — the trace packet
`certificates/trace/k3e_protected_trace` is a finite absence ledger with
`protected_trace_certification=false`), and granted Vol I Theorem H (chiral
Hochschild concentration on the Koszul locus) and Vol II's chiral-Hochschild
Beilinson stratification as established theorems, the trace identity
`Tr^{bulk}_n((-1)^F · id)_{Z^{der}_{ch}(C_X)} = Δ_5^{-2}` follows, with the OP
chamber branch the separate scalar representative `-4096·Tr^{bulk}_n`. No
chain-level input is verified in-repo; the criterion's hypotheses place the
compact source in the companion volumes' domain by assumption. No appeal is
made to the Vol II Universal Holography master theorem, whose standard-landscape
scope (affine KM at non-critical level, W_{N,c} at generic c, Vir_c at generic
c ≠ 0, Schellekens, Monster, VSKR+BGG-tempered cosets on a smooth projective
curve) does not include the BKM-derived hybrid factorisation chart C_X on K3×E.

The **level-𝖠 facet** — gravity-line operator algebra acting on the boundary with
Pentagon-face scalar trace Φ_{10}^{un} = Δ_5^2 — is Vol II's Construction Problem 2
and **remains open in Vol II**. No statement of this manuscript closes CP2; the
level-𝖹 trace pairing is strictly weaker than the level-𝖠 acting algebra.

The Pfaffian–Dirac theorem `thm:ch6-pfaffian-dirac`, the orientation-character match
`thm:ch6-orientation-character`, the primitive recognition theorem
`thm:ch6-primitive-recognition`, and the level-𝖹 Z_BPS trace identity hold
**relative to retained data** whose components the repo's own ledgers record as
unsupplied (d0 / o2 / pfaffian / trace certification = false). Pf² = det is part of
the assumed datum (clauses (P1)–(P2) of (P_fin)), and the hypotheses of (P_fin)
encode Δ_5's Fourier data, so `Pf_prot = Δ_5` is q-expansion rigidity relative to
the datum, not a construction. The level-𝖠 gravity-line operator algebra (Vol II
CP2) is the open frontier (App G O*5).

**Five-level status.** ① ↔ ② proved (Borcherds–Gritsenko–Nikulin); ② ↔ ⑤ and ① ↔ ⑤
proved (Borcherds 1995); levels ①, ②, ⑤ are classical-proved. Level ③ is a
conditional recognition architecture: criterion theorems relative to retained data
that remain unsupplied per the repo's own certificate ledgers; its edges to ② and ①
hold only relative to that datum. Level ④ is a conjecture (mirror discriminant, §I).
The five-fold thesis is **not closed** on K3×E; the manuscript's unconditional new
mathematical content is the parity-resolved δ₁₂₃ root-space computation (29|93 with
29 − 93 = −64 = f(1,1); `prop:bkm-delta123-presentation-count`) and the
scalar-Pfaffian monodromy proposition (`prop:scalar-pfaffian-data-not-section`).
The level-𝖠 operator-algebra promotion to a gravity-line module remains open as
Vol II CP2.


## Historical obstruction probes

These identifiers locate prior investigations. Check current sources before using their conclusions.

| Obstruction | Statement | Swarm probe |
|---|---|---|
| (D0) | D0-degeneration limit of the cosection-reduced d-critical orientation theory | A005, A011, A026, A037, A042 |
| (O1) | Strong reduced orientation on the K3×E-quotient self-Ext frame bundle | A074, A076, A082 |
| (O1⁺) | Weyl-equivariant transport of the orientation along W^{(2)}(Λ_{II}^{2,1}) reflections | A047, A049, A089 |
| (O2) | Local Pfaffian wall normal form on type-II walls (the 4096 = 2^{12} sign sum on the half-Hilbert orbit) | A047, A092, A100 |

Discharging any obstruction tightens the conditioning of ②↔③; verify swarm state
before asserting unconditionally.
