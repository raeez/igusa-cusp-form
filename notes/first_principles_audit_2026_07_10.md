# First-Principles Audit of the Mathematics — igusa-cusp-form

**Date:** 2026-07-10.
**State audited:** HEAD `172dd61` ("release pdf", 2026-05-28) plus the
working tree (350 files modified; appendices A–G under active edit;
`F_build_algorithms.tex` deleted in favor of
`F_finite_constructions.tex`). Line numbers as of this read.
**Method:** two independent adversarial deep reads — (i) the five-level
Δ₅ thesis (automorphic / BKM denominator / compact Pfaffian / mirror
discriminant / singular theta lift); (ii) the compute layer,
certificates, and physics labelling — with status conventions
distrusted and every attackable number recomputed from standard
definitions in exact arithmetic. Load-bearing findings independently
confirmed at the main line are marked ✓M. Companion audits in the four
sibling repos and `~/ecosystem/swarm-reports/`.

---

## 1. Executive verdict

**Overall grade: B+. The classical spine is excellent and massively
verified; the novel level is honest architecture, not construction;
two concrete defects need repair.** Every number attacked — by two
referees independently and by my own from-scratch theta computation —
verifies exactly. The manuscript's own contribution (level ③, the
compact Pfaffian) is scrupulously conditional in the body; the
repo-level CLAUDE.md, however, oversells it ("discharged", "closed"),
and one Chapter 1 display states a false denominator identity.

## 2. Independently verified at the main line (✓M)

1. **φ₀,₁ from scratch** (my own theta-constant computation, sympy,
   exact): φ₀,₁ = (y⁻¹ + 10 + y) + q(10y⁻² − 64y⁻¹ + 108 − 64y + 10y²) + …;
   c(0,0) = 10 → Borcherds weight 5 (Δ₅); Ell(K3) = 2φ₀,₁ →
   c(0,0) = 20 → weight 10 (χ₁₀ = Δ₅²). The factor-of-2 chain that
   anchors the whole repo is correct. Referee recomputations extend
   this: discriminant table through Δ = 24
   (1, 10, −64, 108, −513, 808, −2752, 4016, −11775, 16524, −43200,
   58640, −141826, 188304) all matching
   `compute/verify_square_root.py:478–525` and the manuscript rows.
2. **The false display** (`chapters/01_pentadic.tex:329–333`, read
   verbatim ✓M): den(𝔤_{Δ₅}) = Σ_{w∈W⁽²⁾} sgn(w)·w(e^ρ) = 64⁻¹Δ₅(2Z)
   — the Gritsenko–Nikulin imaginary-simple correction terms are
   missing. As displayed, the naive alternating sum is the
   denominator of the *uncorrected* hyperbolic KM algebra; correcting
   it is GN's entire theorem. Machine check (referee): D₅ has
   coefficient −9 at exponent ρ + 2f₂, which is not a Weyl translate
   of ρ. Chapter 4 (`04_view2_bkm.tex:765–780`) has the correct
   corrected display; Chapter 1 must match it.

## 3. The five levels

| Level | Verdict | Decisive evidence |
|---|---|---|
| ① Automorphic (`03_view1_automorphic.tex:227–240`) | **CLASSICAL-CORRECT** | Correct φ₀,₁ input, weight 5 = f(0,0)/2, theta-leading 64 = 2⁶, simple-Humbert divisor, Maass det-character; factor-of-2 discipline explicit at 03:117–119, 03:682, 02:148; the Fock-superdeterminant reading honestly scoped ("no vertex, chiral, or holomorphic E₃ structure", 03:534–537) |
| ② BKM denominator (`04_view2_bkm.tex:868–903`) | **CLASSICAL-CORRECT** (one Ch. 1 error, §2.2) | Signed supermultiplicity vs simple-fibre dimension distinguished (04:513–515); isotropic split 10 = 1 + 9 with η⁹ exponents verified (a(3/2,·) = −9, a(5/2,·) = 27 ✓); 29\|93 parity split at δ₁₂₃ with m(δ₁₂₃) = −93 verified against [q^{3/2}r^{3/2}s^{3/2}]D₅ = +93 and 29 − 93 = −64 = f(1,1); height-3 root table verified entry-by-entry |
| ③ Compact Pfaffian (`01_pentadic.tex:445–463`; `06_pfaffian_dirac.tex:581–633`; `05_view3_dirac_igusa.tex:352–503`; App G) | **GAP by explicit design; NOT overclaimed in the manuscript** | 𝔄_{K3×E} is a "chosen/retained datum", not constructed (`e3_source_certification=false`, `pro_object_certification=false`, 05:69–77, 539–545); the "Dirac operator" is a formal 2×2 skew block with "no analytic Dirac operator … asserted" (05_4:256–258); **Pf² = det is part of the assumed datum** (clauses (P1)–(P2) of (P_fin), 05_4:88–106), not a theorem; every App G "discharge" is titled criterion, with ledgers `certified:false`; the hypotheses encode Δ₅'s Fourier data, so `Pf_prot = Δ₅` is q-expansion rigidity, not construction; the 2¹² = 4096 = 64² wall count is stipulated in (O2_atlas), not derived (App G:50–95, honestly called "scalar only" at G:734–779) |
| ④ Mirror discriminant (`08_view4_mirror.tex:484–515`) | **CONJECTURE, properly labelled** | ClaimStatusConjectured; "is not a hypothesis of any theorem" (01:541–544) |
| ⑤ Singular theta lift (`07_view5_theta_lift.tex:511, 751, 787`) | **CLASSICAL-CORRECT** | Weil-representation input weight −½ for Λ³,² = U⊕U⊕⟨2⟩ correct; PSp₄(ℝ) ≅ SO(3,2)₊ ∧²-bridge correct; `compute/verify_lattice.py` genuinely verifies the Gram-matrix realization |

Genuinely proved new fragments (modest, correct, worth keeping):
W⁽²⁾ ≅ ℤ/2∗ℤ/2∗ℤ/2 with abelianization (ℤ/2)³ and the
orientation-character rigidity ε_o = ν_{Δ₅} (App G:562–666); the
Klein-four/two-primary detection lemmas (App G:409–499); the
scalar-Pfaffian-data-not-a-section monodromy proposition
(05_4:177–222).

## 4. Compute layer and certificates — grade **A−**

- **Two species, honestly separated.** Genuine arithmetic:
  `verify_square_root.py:47–118` computes φ₀,₁ from theta definitions
  at every run (compute-then-compare); the Jacobi window certificate
  recomputes f-values live against a separately-provenanced target
  fixture — every value matches independent recomputation.
  Absence ledgers: the D0/O1/O2/Pfaffian/trace packets are openly
  `mock_empty_blocked`, `certified:false` — they verify only that
  the list of missing obligations is well-formed, and the prose says
  exactly this (App G:144–149). 102 of 249 compute scripts certify
  *obstructions*. No certificate claims to verify a conditional
  statement.
- **First in-ecosystem verification of the foundational identity.**
  Neither repo script ever computed the ten-even-theta-constant
  product; the +64 normalization was citation-anchored. Both referees
  computed it independently: exact equality with the Borcherds
  product on all tested coefficients (one referee: 50 coefficients;
  the other: 120 monomials through q,s ≤ 7/2), including the monic
  drivers 93, 540, −90 of the BKM chapter. **Latent sign trap
  (established by direct computation):** in the manuscript's declared
  phase convention (03:176) the product is +64·D₅; in the equally
  standard Mumford convention it is −64·D₅. The manuscript is correct
  because it pins its convention; the certificate CSV
  (`certificates/normalizations/delta5_theta_leading/normalizations.csv`)
  records "+64, GN Theorem 4.1" without recording the convention.
- **Flag: the c_N(0) ladder.** `thm:bkm-kappa-universal`
  (`04_view2_bkm.tex:1530–1602`): c_N(0) = (8,6,4,2) for
  N ∈ {2,3,4,6} rests solely on Cheng–Harrison Table 2,
  un-recomputed in-repo, and the proof's gloss
  "c_N(0) = χ^{g_N}(K3)" is normalization-inconsistent with its own
  N = 1 column (c₁(0) = 10 ≠ χ(K3) = 24; the text silently switches
  to the EZ-normalized input at N = 1). The values at N ≥ 2 are
  plausibly right (frame shapes 1⁸2⁸, 1⁶3⁶, 1⁴2²4⁴, 1²2²3²6² give
  a₁ = 8,6,4,2; a twined-genus consistency check supports N = 2),
  but N ≥ 2 deserves a compute path and the Lefschetz sentence a
  qualifier. **Cross-repo note:** Vol III inscribes the same ladder
  with wrong attributions (Sp₄(ℤ) scalar forms — impossible;
  Eichler–Zagier Table 1; Govindarajan–Krishna square-root weights,
  which are (5,3,2,3/2,1), a different family). See the Vol III
  audit F-III.6: this repo's convention-mixing at N = 1 is the seed
  of that corruption.
- **Process weakness:** the Makefile wires none of the 249 verifiers
  into any build target; the verification layer protects only those
  who run it by hand.

## 5. Physics labelling — PASS, emphatically

The gravity-line/path-integral promotion is a scope block with
ClaimStatusOpen ("The construction of the gravity-line operator
algebra is open", 09:574–591); "no microscopic state space ℋ_{K3×E}
is asserted" (09:602–605); the Hall–Borcherds residual is a labelled
Conjecture (09:616–640); Z_DT = Z_OP = Z_PT = −4096·Δ₅⁻² is
ProvedElsewhere with the right sources, the OP sign quarantined as a
chamber convention; Z_BPS := (Φ₁₀^{un})⁻¹ = Δ₅⁻² is a Definition —
always the square, never the square root; the 1/χ₁₀-vs-1/Δ₅
distinction is kept sharp throughout; the mixed-HT route is correctly
blocked by h^{0,1}(K3×E) = 1 ≠ 0. The parent constellation's
forbidden slogans are explicitly negated in-text. KKV is never
invoked (nothing to mislabel).

## 6. The two required repairs

1. **The false denominator display**, `01_pentadic.tex:329–333`
   (✓M §2.2): add the GN imaginary-simple correction terms (as
   Chapter 4 has them), or replace the display with a pointer to the
   corrected form.
2. **Stale CLAUDE.md §VII overclaims**: "discharged" (Theorems
   G.1/G.3/G.4), "verified… (Lemma G.9)" (no such lemma exists in
   App G), "the five-fold thesis is closed on K3×E at the
   chiral-shadow level", and the "(3,3,3) abelianisation" (refuted by
   the manuscript itself at App G:657–666 — the off-diagonal −2 is an
   infinite Coxeter exponent, no order-three braid relation). The
   manuscript is healed; its summary file is not. Also: record the
   theta phase convention in the normalization certificate; add a
   compute path for c_N(0) at N ≥ 2; wire the verifiers into a make
   target; note the label `thm:G-four-obstruction-discharge` vs its
   title "…criterion" (healing fossil).

## 7. Systemic diagnosis

Same inversion as mixed-holomorphic-topological-strings: **the body
is more honest than the summary layer.** The manuscript underwent a
real healing pass (conditionals, criteria, absence certificates,
firewalls) and its unconditional content — a well-verified,
well-organized account of Gritsenko–Nikulin plus a clean
orientation-character rigidity lemma — would survive referee
scrutiny. CLAUDE.md §VII still describes the pre-healing ambitions as
achievements. With the two repairs of §6, this is an honest A−
conditional-programme paper.

**Provenance.** ✓M = verified by my own from-scratch computation or
verbatim main-line reading (φ₀,₁ expansion and weight bookkeeping;
the Chapter 1 display). Referee recomputations (independent scripts,
exact arithmetic): the discriminant table, the 120-monomial
theta-product identity, m(δ₁₂₃) = ±93 bookkeeping, η⁹ exponents,
det-character antisymmetry, lattice certificates, and the
sign-convention trap — all pass in the manuscript's declared
conventions.

---

# Part II — Mathematical yield (fresh-eyes pass, same date)

Stricter second pass: referee forbidden from reading CLAUDE.md,
KICKSTART, notes/, certificate narratives, or Part I; graded only
**true + proved + new** against the Igusa/Borcherds/Gritsenko–Nikulin
baseline; hypothesis-contains-conclusion = zero. A third independent
recomputation of the Δ₅ Fourier coefficients (theta-product route)
again found the arithmetic correct everywhere tested.

**Yield grade: C− (C/D boundary).** Nothing false; the manuscript's
failure mode is that its headline theorems assume their conclusions.

**True + proved + new (complete list):**
1. **The parity-resolved root space of 𝔤_{Δ₅} at δ₁₂₃**
   (`04_view2_bkm.tex:1302–1346`, tables :1174–1258, window rows
   :1372–1396): even dimension 29 (2 free-Lie words + 27 mixed
   brackets with the nine even η⁹-isotropic simples), odd dimension
   93 (the odd imaginary simples, m(δ₁₂₃) = −93), with
   29 − 93 = −64 = f(1,1). Verified against independent theta
   computation (5952/64 = 93); the parity forcing (isotropic simples
   even, δ₁₂₃-simples odd) is valid. New as an explicit computation
   — GN give signed multiplicities, never parity-resolved bases —
   but it is a forced count from GN's data, which the manuscript
   itself says (:2371–2373). Marginal expert interest: a pleasant
   worked example, roughly an afternoon's exercise from GN's
   presentation.
2. The scalar-Pfaffian-data-not-a-section monodromy proposition
   (`05_4:177–222`) — true, proved, and the classical
   multiplier-system ambiguity of square roots formalized in a
   paragraph. New-but-trivial.
3. The Klein-four / two-primary detection lemmas (App G:409–499) —
   correct textbook F₂ group cohomology; the manuscript's own remark
   concedes they "do not construct the null-trivialisations".

**Candidates that dissolve:** W⁽²⁾ ≅ ℤ/2∗ℤ/2∗ℤ/2 is immediate
universal-Coxeter theory ((∞,∞,∞)-triangle group; generation is
Nikulin/GN, and the manuscript's proof is exactly that observation);
the ε_o = ν_{Δ₅} "rigidity" is character-freeness (trivial for a free
product) plus the assumption ε_o(s_δ) = −1 supplied by the (O1)⁺/(O2)
retained data — which the repo's own ledgers record as unsupplied.
κ_BKM(Φ_N) = c_N(0)/2 is Borcherds' weight formula applied to known
inputs. The K₀-firewall propositions are true, trivial folklore.
Chapters 03/07/09 are correct, honestly-cited assembly of
Igusa–Maass–Borcherds–GN–Andrianov–Saito–Kurokawa–Oberdieck–
Pandharipande material. Chapter 08 contains no proved statement.

**The Pfaffian chapters, stripped:** the only proved statement in
chapters 05/06 whose hypotheses do not encode the conclusion is the
monodromy proposition (plus the one-line Pf(0,u;−u,0) = u). The
boxed `Pf_prot(𝔇_X^DI) = Δ₅` (`01_pentadic.tex:445–463`,
`06:581–633`) is a definition dressed as a theorem: hypothesis (P3)
is the conclusion's exponent table with leading coefficient 64,
after which "Pf = Δ₅" is GN's product theorem. The level-Z trace
identity (App G:934–1001) additionally cites two unpublished
companion volumes "as established theorems". The manuscript's own
ledgers record every retained datum as unsupplied
(d0/o2/pfaffian/trace certification = false).

**One-paragraph core:** the genuine new mathematics is the δ₁₂₃
anatomy cluster (item 1) plus two micro-lemmas; everything else is
either honest reorganization of classical material or conditional
scaffold whose hypotheses contain the theorems. The "K3×E
realization problem" of the title is, on the manuscript's own
accounting, entirely open: no obstruction discharged, no Pfaffian
section constructed, no recognition datum supplied.

**Consequences for Part I:** the B+ stands as a
correctness-and-honesty assessment (nothing false; classical spine
massively verified); as mathematical yield the manuscript is a C−.
The two Part I repairs (Ch. 1 denominator display; CLAUDE.md §VII)
remain the immediate items; add: state plainly in the introduction
that the unconditional new content is the δ₁₂₃ computation and the
monodromy lemma.

---

# Part III — Healing ledger (2026-07-10, same date)

All seven repairs of the healing directive executed. Line numbers as
of this write.

1. **False denominator display healed** —
   `chapters/01_pentadic.tex:339–374`. The naive alternating sum
   den(𝔤_{Δ₅}) = Σ_w sgn(w) w(e^ρ) = 64⁻¹Δ₅(2Z) replaced by the
   corrected Borcherds–Weyl–Kac form
   Σ_w sgn(w) w(e^ρ − Σ_{a∈Λ²,¹_II∩ℝ_{>0}𝒫_II} m(a) e^{ρ+a}) =
   64⁻¹Δ₅(2Z), matching Chapter 4's
   `thm:bkm-weyl-alternating-sum` (04:765–780) in Chapter 1's
   formal-exponential notation; 𝒫_II and m(a) glossed at first use
   with forward reference and [GN Thm 2.1] citation. Gloss added
   (01:366–374): the correction terms are the content of GN's theorem;
   the naive sum is the denominator of the uncorrected hyperbolic KM
   algebra; witness inscribed: ρ+2f₂ carries coefficient −9 in
   64⁻¹Δ₅(2Z) yet lies on no Weyl translate of ρ. The −9 is verified
   three ways: hand expansion of the product factors with s = 0
   ((1−q)¹⁰ gives −10, (1−qr)(1−r⁻¹) gives +1), the η⁹ leading
   exponents already in the manuscript (a(3/2)=−9), and the new
   machine check ((12,2,4)-unit coefficient −576 = 64·(−9) in
   `compute/verify_theta_product_identity.py`); norm check
   (ρ+2f₂)² = −11/2 ≠ −3/2 = ρ² confirms off-orbit.

2. **CLAUDE.md §VII de-overclaimed** — `CLAUDE.md:207–268` rewritten.
   (a) Section retitled "Obstruction criteria (Appendix G)"; table
   column now "Criterion theorem (granted the retained data)" with App
   G's actual titles and labels (`thm:G-D0`, `thm:G-O1`,
   `thm:G-O1-plus`, `thm:G-O2-normal-form`, `thm:G-R1-R2`,
   `thm:G-O2-orbit-transport`); "unconditional at the chiral-shadow
   level" → conditional criterion relative to the chosen retained
   datum, components recorded as unsupplied by the repo's own
   ledgers. (b) "verified … (Lemma G.9)" and the "(UH.1)–(UH.5)
   verification" deleted (no Lemma G.9 exists in App G); level-𝖹
   paragraph now states `thm:G-vol2-discharge` is titled "…trace
   criterion", granted (Z_HB) clauses (Z1)–(Z5) (not supplied; trace
   packet is an absence ledger) plus Vol I Thm H and Vol II
   stratification as established theorems; no chain-level input is
   verified in-repo. (c) Five-level status paragraph (CLAUDE.md:256):
   ①②⑤ classical-proved; ③ conditional recognition architecture with
   retained data unsupplied; ④ conjecture; thesis **not closed**;
   unconditional new content named
   (`prop:bkm-delta123-presentation-count`,
   `prop:scalar-pfaffian-data-not-section`). (d) "(3,3,3)
   abelianisation" corrected to W⁽²⁾ ≅ ℤ/2∗ℤ/2∗ℤ/2 (universal
   Coxeter; off-diagonal −2 = infinite exponent, **no order-three
   braid relation**), abelianisation (ℤ/2)³ — matching App G:620–666.

3. **Label fossil renamed** — `thm:G-four-obstruction-discharge` →
   `thm:G-four-obstruction-criterion` repo-wide (7 sites: label at
   `appendices/G_obstruction_discharges.tex:193`; refs at
   `chapters/02_k3xe_setup.tex:21`,
   `chapters/05_view3_dirac_igusa.tex:357,501`,
   `chapters/07_view5_theta_lift.tex:594`,
   `chapters/09_zbps_realization.tex:738`,
   `chapters/10_open_obstructions.tex:629`). Zero stale occurrences
   remain in .tex/.md sources. The theorem's title "Relative
   Pfaffian-orientation criterion on K3×E" is unchanged; the label
   now matches it.

4. **Theta phase convention certified + compute path inscribed** —
   (i) `certificates/normalizations/delta5_theta_leading/normalizations.csv:2`
   now records the manuscript convention
   exp(πi(z[l+a/2]+ᵗb·l)) on the +64 row; new row :3
   `Delta5_theta_leading_mumford` records −64 in the Mumford
   convention exp(πi(z[l+a/2]+ᵗ(l+a/2)b)) — the sign trap.
   (ii) `manifest.json:6` new `phase_convention` key; :27 new
   limitations line stating the trap and the compute path.
   (iii) README updated with the trap and the run line.
   (iv) New `compute/verify_theta_product_identity.py`: computes the
   ten-even-theta-constant product (both conventions, exact integer
   Laurent arithmetic in q^{1/8}, r^{1/4}, s^{1/8} units) and the
   Borcherds product side (exponents from the theta-quotient φ₀,₁ of
   `verify_square_root.py`, widened to nm ≤ 9) and asserts exact
   monomial-by-monomial equality including the +64 on the box
   q,s ≤ 7/2 (120 monomials; the directive's q,s ≤ 5/2 box is the
   50-monomial subset), Mumford = −(manuscript) on the whole box,
   leading ±64, structural cusp-lattice congruences, and the drivers
   −576 = 64·(−9) at q^{3/2}r^{1/2}s^{1/2} (and its q↔s mirror) and
   5952 = 64·93 at q^{3/2}r^{3/2}s^{3/2}. Runtime 0.05 s.
   `verify_theta_normalization_fixture.py` re-run against the edited
   packet: SCALAR_NORMALIZATION_VERIFIED.

5. **c_N(0) ladder: normalization mixing stated + compute path** —
   (i) `chapters/04_view2_bkm.tex` `thm:bkm-kappa-universal`
   statement (:1537–1550): c_N(0) now defined as the constant
   coefficient of the Borcherds input of Φ_N, with the two
   normalizations explicit — N=1 square-root seed φ₀,₁
   (c₁(0)=f(0,0)=10, half of Ell(K3)=2φ₀,₁), N∈{2,3,4,6}
   twined-full (CH Table 2; frame shapes with a₁ = 8,6,4,2) — and the
   sentence "The ladder mixes two normalizations" inscribed. (ii)
   Proof gloss fixed (:1588–1608): c_N(0)=χ^{g_N}(K3) qualified "in
   the twined-full normalization and for N∈{2,3,4,6} only"; the
   Lefschetz number derived as a₁ (d-cycles contribute vanishing
   root-of-unity sums); at N=1 the identification fails explicitly:
   χ^{g₁}(K3)=24 ≠ 10 = c₁(0), the square-root seed. (iii) New
   `compute/verify_bkm_kappa_ladder.py`: hard-codes only the five
   frame shapes; computes the characteristic polynomial
   ∏(x^d−1)^{a_d} exactly, the twined Euler characteristic as
   −[x²³], the equivariant q⁰ row 2y+(χ−4)+2y⁻¹ from Hodge
   characters (row sum χ), the untwined cross-check
   2(f(0,1)+f(0,0)+f(0,−1)) = 24 = χ(K3) from the theta-quotient
   φ₀,₁, and asserts the manuscript's table (10,8,6,4,2) and
   κ = c/2 = (5,4,3,2,1), including 10 ≠ 24 at N=1. Runtime 0.04 s.

6. **Verifiers wired into make** — `Makefile:46–54` (VERIFY_SCRIPTS),
   :252–270 (`make verify` target), help line added. Runs
   verify_square_root.py (hard asserts, exits nonzero on mismatch),
   verify_lattice.py, verify_jacobi_window_fixture.py,
   verify_theta_normalization_fixture.py, and the two new scripts;
   fails on any mismatch. Full run passes; wall time ~14 s (script
   time < 0.5 s total; bounded boxes throughout).

7. **Introduction honesty statement** —
   `chapters/01_pentadic.tex:276–289`, immediately after the
   five-readings thesis paragraph of
   `sec:retained-e3-five-readings`: the unconditional new
   mathematical content is the parity-resolved δ₁₂₃ computation
   (29|93, 29−93 = −64 = f(1,1),
   Proposition~`prop:bkm-delta123-presentation-count`) and the
   scalar-Pfaffian monodromy proposition
   (`prop:scalar-pfaffian-data-not-section`); the Pfaffian–Dirac
   identity is a recognition criterion relative to the retained data
   (D0), (O1), (O1)⁺, (O2_atlas), (P_fin), which the certificate
   ledgers record as not supplied.

**Leftovers / observations.**

- **KICKSTART.md:56–68 repeats the pre-healing overclaims** healed in
  CLAUDE.md §VII ("discharged on K3×E", "Theorem G.4 ((3,3,3)…",
  "Lemma G.9", "(UH.1)–(UH.5)"). Outside the directive's scope
  ("execute the repairs, nothing else"); flagged here as the next
  summary-layer heal so future sessions do not re-import the
  falsehoods from the bootstrap file. AGENTS.md is clean.
- `out/architecture.json` still carries the old label string
  `thm:G-four-obstruction-discharge`; it is a build artifact
  regenerated by `make architecture` — not hand-edited.
- No full LaTeX build was run (builds at session end per repo rule).
  All macros used in the edits (\Poly, \R, \Z, \La) verified present
  in `main.tex`; all \ref targets verified to exist
  (`thm:bkm-weyl-alternating-sum`,
  `prop:bkm-delta123-presentation-count`,
  `prop:scalar-pfaffian-data-not-section`).
- Not repaired because not defective: the Frontispiece display
  (01:49–52) states only den(𝔤_{Δ₅}) = 64⁻¹Δ₅(2Z) without the
  alternating sum, and the edge paragraph (01:383–390) states the
  identification abstractly; both remain true as written.
