# KICKSTART — igusa-cusp-form (resume prompt)

> Paste this file (or `@KICKSTART.md`) as the first message in a fresh
> `/clear` session at `~/igusa-cusp-form/`. The original swarm-launch
> kickstart is preserved as `KICKSTART_swarm_legacy.md` — that work is
> complete; this file resumes from the current stable state.

---

## 1. What this repository is

The manuscript *The Igusa Square Root: The Borcherds determinant of
φ_{0,1}, its denominator algebra, and the K3×E realization problem*
— the April 2026 reconstitution of an original 2020 note by Raeez
Lorgat, the canonical statement of the five-fold thesis on Δ_5.

**Five-fold thesis (CLAUDE.md §I).** Δ_5 ∈ M_5(Sp(4,Z), ν_{Δ_5}) is
one chiral E_3-algebra 𝔄_{K3×E} of the K3×E formal target, valued at
five categorical-dimensional levels:

  ① automorphic Borcherds–Gritsenko–Nikulin section D_X = Δ_5;
  ② BKM denominator den(g_{Δ_5}) = 64⁻¹ Δ_5(2Z) on Λ²,¹_II;
  ③ protected Pfaffian Pf_prot(𝔇_X^DI) of the Dirac–Igusa pro-object;
  ④ mirror discriminant of the K3-mirror period family **(conjectural)**;
  ⑤ singular theta lift Θ(φ_{0,1}) under Sp(4) ≅ Spin(3,2).

## 2. Current build state

- **234 pages**, exit 0, zero undefined refs, zero undefined citations.
- Build: `make fast` clean; `make` full bibtex+latex pipeline.
- PDF: `out/main.pdf`.

**16-file integrated manuscript:**
- `main.tex` (skeleton, preamble + \input directives)
- `chapters/01_pentadic.tex` (frontispiece + Ch.1 pentadic road map)
- `chapters/02_k3xe_setup.tex` (Mukai/Gram dictionary)
- `chapters/03_view1_automorphic.tex` (BGN import)
- `chapters/04_view2_bkm.tex` (BKM denominator)
- `chapters/05_view3_dirac_igusa.tex` (Dirac–Igusa pro-object, climax theorem)
  - `chapters/05_subsections/05_1_hybrid.tex` through `05_8_obstructions.tex`
- `chapters/06_pfaffian_dirac.tex` (Pfaffian–Dirac theorem)
- `chapters/07_view5_theta_lift.tex` (singular theta lift)
- `chapters/08_view4_mirror.tex` (mirror discriminant conjecture)
- `chapters/09_zbps_realization.tex` (Z_BPS = Δ_5⁻², Saito–Kurokawa)
- `chapters/10_open_obstructions.tex` (Mathieu/umbral moonshine)
- `appendices/A_lattices.tex` through `appendices/F_build_algorithms.tex`
- `appendices/G_obstruction_discharges.tex` **(the discharge proofs)**
- `appendices/boundary_compatibility_conditions.tex`

Legacy preserved: `main_legacy.tex` (758KB, the 18,629-line original).

## 3. The four-obstruction discharge (Appendix G)

The cross-level identity ②↔③ — the Pfaffian–Dirac theorem — was
originally conditional on four obstructions. **All four are now
discharged on K3×E** in Appendix G:

| Obstruction | Discharge |
|---|---|
| (D0) D0-degeneration limit of cosection-reduced d-critical orientation | Theorem G.1 (Joyce–Upmeier + Bojko + Mittag–Leffler) |
| (O1) strong reduced orientation on K3×E-quotient self-Ext frame | Theorem G.3 + Lemma G.1 (Klein-four detection, rank-2) + Lemma G.2 (P³-Pin^c vanishing, rank≥3) |
| (O1)⁺ Weyl-equivariant transport along W^{(2)}(Λ²,¹_II) | Theorem G.4 ((3,3,3) abelianisation + Maass character match) |
| (O2) local Pfaffian wall normal form + (R1)↔(R2) reconciliation | Theorems G.5–G.7 (rank-one + Weyl-orbit transport + 4096 = 2^{χ_top(K3)/2}) |

The **level-𝖹 Hall–Borcherds residual** is also discharged on K3×E
(Theorem G.10): verify the chain-level inputs (UH.1)–(UH.5) of the
universal stage chain on (K3×E, D, τ) at boundary vacuum b with
chart A_b = C_X (Lemma G.9), then apply Vol I Theorem H (chiral
Hochschild concentration on the Koszul locus) together with Vol II's
chiral-Hochschild stage stratification, clauses (i)+(ii) (chain-level
bulk identification and CY-orientation trace pairing of degree
−dim_ℂ(K3×E) = −3) to obtain
`Tr^{bulk}_n((-1)^F · id)_{Z^{der}_{ch}(C_X)} = -4096 Δ_5⁻²`. No
appeal is made to the Vol II Universal Holography master theorem,
whose standard-landscape scope (affine KM, W_{N,c}, Vir, Schellekens,
Monster, VSKR+BGG-tempered cosets on a smooth projective curve) does
not include the BKM-derived hybrid factorisation chart C_X on K3×E.

The Pfaffian–Dirac theorem `thm:ch6-pfaffian-dirac` therefore holds
**unconditionally on K3×E at the chiral-shadow / level-𝖹 stage**,
conditional only on:
- (X1) Vol I Theorem H + Vol II chiral-Hochschild stage stratification
  clauses (i)+(ii) being correct theorems;
- (X2) cited foundational results (Joyce–Upmeier, Bojko, BBDJS,
  Cao–Kool–Monavari, Maulik–Pandharipande, Oberdieck–Pandharipande,
  Kiem–Li, PTVV) applying as published.

The **level-𝖠 gravity-line operator-algebra promotion** (Vol II
Construction Problem 2) is named in App G as the new open item
(O*5) and remains open per Vol II.

## 4. What is genuinely open mathematics (not defects)

App G §G.7 records the classification (C1)–(C5) closed,
(X1)–(X2) external, (O*1)–(O*5) open mathematics:

- **(O*1) Mirror discriminant.** Conjecture conj:mirror-discriminant
  of Ch.8: [Δ_5⁻²] = 2[𝔇_per] = 2[H₂^Hum]. The divisor identity is
  a theorem; global comparison-line trivialization is conjectural.
  Four named sub-conjectures (M1)–(M4).
- **(O*2) Mathieu/umbral moonshine adjacency.** Cheng–Duncan–Harvey–Gannon
  umbral moonshine for the four **non-surfing classes**
  {7A, 7B, 15A, 15B} of M_24 is open. Precise conjecture in Ch.10:
  `den(g_{Δ_5}^{(g)}) = Θ(φ^{(g),Weil}_{0,1})|_{H_2}` for each
  g ∈ M_24.
- **(O*3) Universal Holography bulk construction.** Explicit
  chain-level construction of Z^{der}_ch(A_b) on K3×E lives in Vol II
  (`~/chiral-bar-cobar-vol2`).
- **(O*4) Type II sigma-model on K3×E.** Physics-grade quantum field
  theory whose BPS partition function is Δ_5⁻² — separate
  construction.
- **(O*5) Level-𝖠 Hall–Borcherds residual (Vol II CP2).** Gravity-line
  operator algebra at level 𝖠 acting on the boundary chiral algebra
  with Pentagon-face scalar trace Φ_{10}^{un} = Δ_5². Vol II names
  this Construction Problem 2; it remains open. The level-𝖹 trace
  promotion of Theorem G.10 is strictly weaker (trace pairing on
  Z^{der}_{ch}(C_X), not an acting algebra on a gravity-line module).

## 5. Voice and discipline

**Read first:**
- `~/ecosystem/INVARIANTS.md` — ecosystem-wide rules.
- `~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md` — seven voices + four-part coining test.
- `./CLAUDE.md` — repo-local canonical doc.
- `./AGENTS.md` — Codex / GPT-5 mirror.

**The Beilinson cut (CLAUDE.md §III)** is the law: primitive objects
first, cross-level identities second, scalar shadows last. Every
load-bearing claim locates on the universal stage chain
`(X,D,τ) → C^op → b → A_b → Bar(A_b) → Z^{der}_{ch}(A_b) → Tr_C / Θ_C → scalar`.

**Banned identifications** (CLAUDE.md §III, ~17 rows) — delete on
sight. Particularly:
- "Δ_5 = compact BPS Hilbert space" → "Δ_5 is the protected scalar shadow"
- "Z_BPS = 3d gravitational path integral" → "Z_BPS is the level-n protected trace"
- "Bar(A) = bulk" → "Bar(A) = MC twisting; Z^{der}_{ch}(A) = bulk"
- "the boundary algebra A is the primitive open object" → "C is the primitive factorization dg-category on (X,D,τ); A_b = End_C(b) is the chart"

**The three Δ_5 names** must be tagged distinctly on first use per
chapter: automorphic section D_X (View ①); BKM denominator
den(g_{Δ_5}) = 64⁻¹ Δ_5(2Z) (View ②); compact protected Pfaffian
Pf_prot(𝔇_X^DI) (View ③).

**Banned rhetorical patterns** (CLAUDE.md §IV): meta-narration,
bookkeeping (Wave N, round M, batch K), CS jargon (certificate,
pipeline, spec, schema, API, metadata), hedging, branding ("Surgical
fix", "Honest summary", "firewall" as metaphor).

**Voice:** Russian-school + math-physics-frontier — Gelfand, Manin,
Drinfeld, Beilinson, Etingof, Kazhdan, Witten, Costello, Gaiotto,
Borcherds, Gritsenko, Mukai, Kac, Moore, Chriss-Ginzburg.

## 6. Load-bearing constants (verify before assuming)

- **Λ²,¹_II is the index-4 sublattice** of Λ²,¹ = U(-1) ⊕ ⟨2⟩;
  abstractly **U(4) ⊕ ⟨2⟩**, **discriminant −32**. NOT disc −2.
- **Type-II Cartan matrix** A = **4 I_3 − 2 J_3** =
  ((2,−2,−2),(−2,2,−2),(−2,−2,2)); det A = −32;
  **eigenvalues (−2, 4, 4)**. NOT (−2,−2,6).
- **Weyl vector** ρ = ½(δ_1+δ_2+δ_3) = f_2 − ½f_3 + f_{−2};
  (ρ, ρ) = −3/2; (ρ, δ_i) = −1.
- **Leading Fourier coefficient** c_Δ(1,1,1) =
  [q^{1/2}r^{1/2}s^{1/2}]Δ_5 = **64 = 2^6 = 2^{χ_top(K3)/4}**.
- **Three Igusa names**:
  - Δ_10 (theta-normalized, leading 4096)
  - χ_10 = Φ_10^un = Δ_5² (Igusa unimodular)
  - χ_10^OP = D_5² = 4096⁻¹ Δ_5² (Oberdieck–Pixton monic)
- **4096 = 2^12 = 2^{χ_top(K3)/2}** from both readings:
  (R1) Spin^c rank of half-Hilbert orbit;
  (R2) squared theta-leading c_Δ(1,1,1)² = 64².
- **Fourier coefficients of φ_{0,1}** (verified by
  `compute/verify_square_root.py`):
  f(0,0)=10, f(0,±1)=1, f(1,0)=108, f(1,±1)=−64, f(1,±2)=10,
  f(2,0)=808, f(2,±1)=−513, f(2,±2)=108, f(2,±3)=1,
  f(3,0)=4016, f(3,±1)=−2752, f(3,±2)=808, f(3,±3)=−64,
  f(4,0)=16524, ...
- **κ-tuple** (κ_cat, κ_ch^Hodge, κ_ch^Heis, κ_BKM, κ_fiber) = **(0, 0, 3, 5, 24)**.
- **κ-universal identity** κ_BKM(Φ_N) = c_N(0)/2 across CHL frame:
  N=1,2,3,4,6 → κ_BKM = 5,4,3,2,1, c_N(0) = 10,8,6,4,2.
- **Saito–Kurokawa**: Δ_5² is the SK lift of g = Δ E_6 ∈ S_{18}(SL_2(Z));
  L_spin(s, Δ_10^θ) = ζ(s−8) ζ(s−9) L(s, g);
  dim Maaß_10 = dim S_{18}(SL_2(Z)) = 1 forces g = Δ E_6.
- **First-timelike parity** 29 | 93 at δ_{123} = δ_1+δ_2+δ_3:
  29 = 2 (Witt-2 free Lie) + 3·9 (3 isotropic mixings × η^9);
  93 = −m(δ_{123}); 29 − 93 = −64 = f(1,1). ✓
- **Singular theta integrand** on **Λ^{3,2}** (NOT Λ²,¹_II);
  Weil-rep pairing, antiholomorphic part, du dv/v² regularization.
- **ν_{Δ_5} pullback path**: Sp(4,Z) → Spin(3,2) → W^{(2)}(Λ²,¹_II)
  via the exceptional isomorphism, Λ²,¹_II ↪ Λ^{3,2}.

## 7. Build commands

```bash
cd ~/igusa-cusp-form
make fast       # single pdflatex pass — fast iteration
make            # full pdflatex → bibtex → pdflatex × 3
make clean      # remove build debris

# Reference integrity check
grep -hoE '\\(?:ref|cref|Cref|autoref)\{[^}]+\}' chapters/*.tex chapters/*/*.tex appendices/*.tex | \
  grep -oE '\{[^}]+\}' | tr -d '{}' | sort -u > /tmp/refs.txt
grep -hE '\\label\{' main.tex chapters/*.tex chapters/*/*.tex appendices/*.tex | \
  grep -oE '\\label\{[^}]+\}' | sed 's/\\label{//; s/}$//' | sort -u > /tmp/labels.txt
comm -23 /tmp/refs.txt /tmp/labels.txt   # should be empty

# Arithmetic fixtures
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
```

## 8. Auto-memory

`~/.claude/projects/-Users-raeez-igusa-cusp-form/memory/MEMORY.md`
indexes:
- Supremum discipline (every choice takes the high road)
- Beilinson cut (primitive first, shadows last)
- Attack-whitepaper analyses
- Dirac–Igusa reconstitution architecture

Read on session start; update when durable wisdom enters.

## 9. Cross-volume constellation

| Repo | Role |
|---|---|
| `~/chiral-bar-cobar` | Vol I — Modular Koszul Duality |
| `~/chiral-bar-cobar-vol2` | **Vol II — Universal Holography master theorem; (X1) lives here** |
| `~/calabi-yau-quantum-groups` | Vol III — Calabi–Yau quantum groups / κ-stratification |
| `~/chiral-bar-cobar-vol4` | Vol IV — Realization |
| `~/mixed-holomorphic-topological-strings` | BCOV / Kodaira–Spencer companion |

Disagreement across volumes is the deliverable; report, do not silently reconcile.

## 10. Suggested next-session priorities (pick at most one)

1. **Cross-volume Master Critique** — read `materials/raw/` (Igusa
   adversarial-review PDFs) and the 2026-05-09 cross-volume Master
   Critique on Desktop. Address findings that affect this manuscript.

2. **Vol II handoff** — verify that Vol II Universal Holography
   master-theorem hypotheses (UH.1)–(UH.5) cited in Lemma G.9 are
   statable from current Vol II content. If not, either strengthen
   Vol II or weaken Lemma G.9.

3. **Submission polish** — line-by-line read of the 234-page PDF,
   normalize voice, kill remaining banned patterns, apply
   Chriss–Ginzburg inevitability test (every sentence forced by
   what precedes it).

4. **Compute layer extension** — extend
   `compute/verify_square_root.py` to depth 6 or 8, verify
   κ_BKM(Φ_N) = c_N(0)/2 at each N ∈ {1,2,3,4,6} arithmetically.

5. **Mathieu moonshine adjacency** — try to make progress on the
   four non-surfing classes {7A, 7B, 15A, 15B} via a sigma-model
   construction on Hilb^*(K3). Honest expectation: hard, may not
   close in one session.

6. **Ch.5 climax restructure deeper** — restructure each subsection's
   prose to support the climax theorem
   `thm:ch5-construction-of-dirac-igusa-pro-object` step-by-step
   (currently subsections still read as a checklist).

## 11. Last action of previous session (2026-05-15)

Wrote this KICKSTART.md. Tasks #19–#27 all completed:
- Tightened App G Lemmas G.1, G.2, G.9 from sketch to rigorous proofs
- Added κ_BKM-universal table for N ∈ {1,2,3,4,6} (Theorem in Ch.4)
- Added higher-order Fourier coefficient verification table
  (Proposition in Ch.4 to depth n=4)
- Added Saito–Kurokawa Hecke eigenvalue proposition (Ch.9)
- Fixed Makefile exit-status quirk (check log for `^!`/`^Fatal`
  instead of pdflatex exit code)
- Wrote App G §G.7 final accountability with (C1)–(C5), (X1)–(X2),
  (O*1)–(O*4) five-category classification

## 12. Resume protocol

1. **Read this file (KICKSTART.md) and `CLAUDE.md` end-to-end.**
2. Verify the build is still clean: `make fast` returns `ok
   out/main.pdf`, and the `comm -23 /tmp/refs.txt /tmp/labels.txt`
   check is empty.
3. Read `MEMORY.md` and skim any new entries.
4. **Ask the user which of §10's priorities to address** (or whether
   they have a different directive). Do not start work without
   confirmation — the manuscript is at a stable closing state.
5. If asked for status: the honest answer is App G §G.7. Closed
   (C1)–(C5), external (X1)–(X2), genuinely open (O*1)–(O*4). The
   Pfaffian–Dirac theorem holds on K3×E at the chiral-shadow level
   granted (X1)+(X2).
