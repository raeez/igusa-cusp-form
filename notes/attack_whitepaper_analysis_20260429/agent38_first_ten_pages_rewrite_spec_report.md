# Agent 38 first-ten-pages rewrite spec report

Scope: implementation-grade specification for rewriting the abstract and
opening ten pages of `main.tex`.  This report does not edit `main.tex`,
`proj.bib`, appendices, or existing source.

Sources mined:

- Attack PDF: `materials/raw/2026-04-29-attack-whitepaper-analysis.pdf`,
  especially the executive verdict, the first eight attack pages, the Dirac
  principle discussion, and the later rewrite/upgrade lists.
- Current manuscript opening: `main.tex:57-918`.
- Required swarm reports:
  `agent10_manuscript_architecture_report.md`,
  `agent13_opening_rewrite_report.md`,
  `agent19_standalone_voice_overclaim_report.md`,
  `agent22_local_patch_proposals_report.md`,
  `agent23_theorem_status_taxonomy_report.md`,
  `agent32_section_order_rewrite_sequence_report.md`.

Adversarial premise: a hostile reader must not be able to infer compact
Hall/factorization geometry, a Hilbert-space half, an analytic square root, an
orientation character, or a microscopic bracket from the Borcherds product,
the OP scalar square, or the Gritsenko--Nikulin denominator algebra.  The first
ten pages must make the theorem spine visible before any residual ledger.

## Opening narrative

The opening must be reorganized around one principle:

```tex
scalar square != first-order square root
```

The "Igusa square root" is not an analytic branch of `Delta_5^2`.  It is a
Dirac-style first-order problem: construct a protected algebraic/Pfaffian datum
whose orientation-sensitive determinant is `Delta_5`, and whose scalar,
orientation-forgetting shadow is the OP/DT branch
`-4096 Delta_5^{-2}`.

The first ten pages should therefore have this narrative order:

1. Protected K3 index is the only theorem-level physical input at the start.
2. Replacing `Z_K3 = 2 phi_{0,1}` by the arithmetic Borcherds half
   `phi_{0,1}` gives only arbitrary Grothendieck representatives
   `U_{n,l}` with signed superdimension `f(n,l)`.
3. Those representatives package the known Borcherds--Gritsenko--Nikulin
   product as a virtual `K_0` determinant:
   `D_X = Delta_5`.
4. Gritsenko--Nikulin supply the denominator target
   `den(g_{Delta_5}) = 64^{-1} Delta_5(2Z)` with active signed
   supermultiplicities `f(nm,l)`.
5. OP/Oberdieck supply a scalar square only:
   `Z^X_OP/DT = -4096 Delta_5^{-2}`.  Constants `64`, `4096`, and the OP
   minus sign are normalization data, not orientation data.
6. The real compact obstruction is charge-theoretic: `(n,l,m)` is a
   Fourier/root/Gram degree, not an additive Hall charge.  The compact source,
   if built, must grade upstairs by `Gamma_X^{form}` and descend only through
   the normal-ordered additive map.
7. Normal-ordered Gram descent is a central theorem, not a later technical
   appendix: `widehat Gamma_X = Gamma_X^{form} \oplus_B Gamma_{gram}` and
   `overline Pi_X(c,T)=Pi_X(c)-T` are the degree repair.
8. Compact Dirac--Igusa realization remains open unless the source,
   orientation/Pfaffian, hybrid wrapped locality, normal-ordered descent, and
   primitive recognition data are supplied.

Do not begin with a caveat list.  Begin with the Dirac principle and the
theorem program, then state the claim-status table.  The current introduction
has the right safety vocabulary, but it reads as a ledger before it reads as a
paper.

## Abstract paragraph plan

Replace `main.tex:57-172` as a whole.  Keep five paragraphs.  No row details.
No spin `L`-factor.  No full compact-source checklist.  Do not write a
full-length proof in the abstract.

Paragraph 1: protected index and virtual determinant.

- Start with `S` a K3 surface and `X=S x E` only as the eventual compact
  problem.
- State that the only theorem-level protected-index input used before the
  compact problem is:
  `Z_K3 = 2 phi_{0,1}`, `phi_{0,1} = sum f(n,l) q^n r^l`.
- Say `phi_{0,1}` is the arithmetic Borcherds input.
- Say `U_{n,l}` are arbitrary Grothendieck representatives with
  `sdim U_{n,l}=f(n,l)`.
- State the determinant formula:
  `D_X(Z)=64 q^{1/2} r^{1/2} s^{1/2} prod_{Gamma_eff}
  (1-q^n r^l s^m)^{f(nm,l)} = Delta_5(Z)`.
- Status wording: "computed from the virtual `K_0` package and identified with
  the theta-normalized Borcherds--Gritsenko--Nikulin product."
- Required denial: "not a microscopic Hilbert space; not a canonical
  half-Hilbert space; not an operator product."

Paragraph 2: imported denominator target.

- State the root-degree map
  `alpha(n,l,m)=2n f_2 - l f_3 + 2m f_{-2}` only if space permits.
- State:
  `den(g_{Delta_5}) = 64^{-1} Delta_5(2Z)`,
  `smult g_{Delta_5,alpha(n,l,m)} = f(nm,l)` on active support.
- Status wording: "imported Gritsenko--Nikulin denominator algebra."
- Required denial: "target-internal bracket; no compact Hall source; no compact
  orientation; no compact BPS operator product."

Paragraph 3: OP scalar square.

- State `D_5 = 64^{-1} Delta_5` and
  `chi_{10}^{OP}=D_5^2`.
- State `Z^X_OP/DT=-4096 Delta_5^{-2}`.
- Status wording: "imported reduced scalar branch."
- Required denial: "sees `D_5^2`, not `D_5`; orientation-forgetful; `64`,
  `4096`, and the OP minus sign do not determine the Maass/reflection
  character or Hall orientation monodromy."

Paragraph 4: formal dyonic lattice and normal ordering.

- Introduce:
  `Gamma_X^{form}=Lambda_S \oplus Lambda_S`.
- Introduce the quadratic Gram shadow:
  `Pi_X(Q,P)=(Q^2/2,Q.P,P^2/2)`.
- Introduce additivity defect:
  `B(c,c')=(Q.Q', Q.P' + Q'.P, P.P')`.
- State:
  `widehat Gamma_X = Gamma_X^{form} \oplus_B Gamma_{gram}`,
  `overline Pi_X(c,T)=Pi_X(c)-T`.
- State that strict fixed-lift raw Gram descent cannot realize the type-II
  real-root strings.
- Status wording: "formal lattice theorem proved here."
- Required denial: "`Gamma_{gram}` is not the Hall charge lattice."

Paragraph 5: open compact Dirac problem.

- Define "Dirac's sense" in one sentence: first-order algebraic/Pfaffian datum
  whose scalar square forgets sign/orientation.
- State the compact source must supply: finite-first compact
  Hall/factorization source, orientation/Pfaffian line comparison, hybrid
  wrapped elliptic-degree sectors, normal-ordered Gram descent, primitive
  radical quotient.
- Include the recognition target display only with radical quotient:
  `H^0 Prim_prot(overline Pi_{X,*}^{Theta} F_X) /
  overline Rad ~= g_{Delta_5}`.
- Status wording: "open problem / certificate consequence."
- Required denial: no compact first-order object is asserted until the source
  and Pfaffian-to-automorphic line comparison are supplied.

## First-ten-pages plan

Target boundary: current `main.tex:57-918`.  The rewritten first ten pages
should not enter the detailed O1/O1+/O2 Pfaffian wall certificate at current
`main.tex:920` before the theorem spine and determinant section are visible.

### Page-order specification

1. Abstract: five paragraphs above.
2. Table of contents remains after the abstract unless the main agent decides
   to move the theorem-status ledger before the TOC.  If moved, it must remain
   short.
3. Rename `main.tex:177` to:
   `\section{Introduction: The Dirac Problem}`.
4. Opening paragraph of Section 1:
   - state the Dirac principle;
   - state that the determinant proof does not use a compact source;
   - state that the compact source problem is the upgrade problem, not an input
     to the determinant.
5. Theorem-program display:
   ```tex
   \text{K3 protected index}
   \to K_0\text{-Borcherds determinant}
   \to \text{GN denominator target}
   \to \text{normal-ordered Gram descent}
   \to \text{compact Dirac--Igusa realization problem}.
   ```
6. "What is proved/imported/conditional/open" table.  One table only.
7. Forbidden-implications box.  This must be visible before any long compact
   source paragraph.
8. Notation-not-to-confuse table.
9. Short protected-locality paragraph:
   - states are sectors;
   - operations/collisions are first;
   - partition functions are traces and cannot reconstruct operations.
10. Projection-to-`E` support-locality paragraph:
    - positive elliptic degree is a support-locality obstruction for a naive
      `Ran(E)` pushforward;
    - it is not a denial of spacetime locality on `K3 x E`.
11. Short primitive recognition paragraph:
    - use the radical quotient display;
    - call it conditional/certificate consequence;
    - move the long certificate list out of the opening.
12. Compress denominator and OP scalar summaries into the front table or into
    one paragraph each.  They should not occupy a whole page before the reader
    sees normal ordering.
13. Remove current `main.tex:339-355` eight-row host-certificate paragraph from
    the opening.  Replace with one sentence at most: independent row
    certificates are recorded later and are not used in the `N=1` theorem
    spine.
14. Merge current `main.tex:357-453` into the one status table.  Do not keep two
    front tables.
15. Retitle `main.tex:462`:
    `\part{The virtual automorphic square root}` or remove the part boundary.
    If "square root" remains, it must appear only after the Dirac principle.
16. Rename `main.tex:464`:
    `\section{The compact source problem}` or
    `\section{Protected Operations Before Traces}`.
17. Keep current `main.tex:467-565` only after compression and local caveats.
    Every use of `BPS`, `physical`, `E_3`, `operator`, `source`, `realization`,
    or `orientation` must carry a local status tag.
18. Keep current `main.tex:570-638` only as a conditional schema and only after
    the reader has seen the source/target firewall.  Do not let bare
    `holomorphic E_3-factorization algebra` appear before the model is called
    supplied/open/interface.
19. Rename `main.tex:640`:
    `\section{Virtual Borcherds Package and the \(K_0\)-Determinant}`.
20. Keep current `main.tex:667-738`, but preserve the fence: K3 worldsheet
    protected cohomology only; no compact `K3 x E` D-brane Hilbert space.
21. Keep current `main.tex:772-830`, but call `mathcal V` a virtual Borcherds
    determinant package.  Keep the bulk/cusp split and "neither sector is a
    microscopic one-particle Hilbert space."
22. Convert current `main.tex:882-918` from proposition to definition/open
    problem.  It names the missing first-order datum; it proves no proposition.
23. Orientation/Pfaffian detailed subcertificates starting at current
    `main.tex:920` should move out of the first-ten-page experience unless the
    pages have already displayed the determinant theorem, status table,
    forbidden implications, and open target specification.

### Required first-ten-pages checks

The first ten pages after rewrite must contain all of these before detailed
orientation certificates:

- `U_{n,l}` is an arbitrary `K_0` representative.
- `mathcal V` is a virtual `K_0` determinant package.
- `(n,l,m)` is a Gram/Fourier/root degree, not an additive Hall charge.
- `g_{Delta_5}` is an imported denominator target.
- OP/DT is an orientation-forgetful scalar square.
- `64` is theta-leading normalization and `4096` is scalar normalization.
- Compact Hall/factorization/source data are not constructed.
- Recognition is a certificate/criterion, not an existence theorem.

## Required tables/boxes

### Table 1: theorem-status ledger

Location: immediately after the theorem-program display in Section 1, replacing
the two current tables at `main.tex:357-453`.

Columns:

```text
Object | Status | Source | What it proves | What it does not prove
```

Required rows:

1. K3 elliptic genus `Z_K3=2 phi_{0,1}`.
   - Status: imported/protected-index theorem.
   - Does not prove: compact `K3 x E` D-brane Hilbert space.
2. Virtual `K_0` determinant `D_X=Delta_5`.
   - Status: formal `K_0` computation plus imported GN/Borcherds product.
   - Does not prove: operator, Pfaffian line, compact source.
3. Gritsenko--Nikulin denominator algebra `g_{Delta_5}`.
   - Status: imported theorem.
   - Does not prove: compact Hall bracket or source-side structure constants.
4. Formal Mukai/normal ordering.
   - Status: proved formal lattice algebra.
   - Does not prove: effective Hall support or nonempty compact moduli.
5. OP/DT scalar square.
   - Status: imported reduced scalar theorem/check.
   - Does not prove: `D_5`, orientation character, Pfaffian square root.
6. Compact Dirac--Igusa source.
   - Status: certificate/conditional/open.
   - Does not prove: existence unless source, orientation, descent, PBW,
     radical, and completion data are supplied.
7. Boundary row certificates.
   - Status: independent extension ledger.
   - Does not prove: the `N=1` Dirac--Igusa construction.

### Box 1: forbidden implications

Location: directly after Table 1.

Required entries:

```tex
\mathcal D_X=\Delta_5 \not\Rightarrow \mathfrak D_X.
\Delta_5^2 \text{ in OP/DT} \not\Rightarrow \epsilon_o.
\mathfrak g_{\Delta_5} \not\Rightarrow \text{compact Hall/factorization source}.
\Gamma_{\mathrm{gram}} \neq \text{Hall charge lattice}.
```

Add two more if space permits:

```tex
64,4096 \not\Rightarrow \text{orientation data}.
\sdim P_\gamma=f(nm,l) \not\Rightarrow \text{bracket constants}.
```

### Table 2: notation not to confuse

Location: after forbidden-implications box or before the first technical
section.

Rows:

- `mathcal D_X`: theta-normalized virtual `K_0` determinant.
- `D_5`: monic Borcherds product, `64^{-1} Delta_5`.
- `Delta_5`: theta-normalized Igusa cusp form.
- `chi_{10}^{OP}`: OP monic square, `D_5^2`.
- `Gamma_X^{form}`: formal dyonic Mukai bookkeeping lattice.
- `Gamma_{X,sigma}^{eff}`: supplied effective compact Hall support, if any.
- `Gamma_{gram}`: Fourier/root/Gram degree lattice, not Hall charge lattice.
- `widehat Gamma_X`: normal-ordered extension by `B`.
- `overline Pi_X`: additive corrected Gram map.
- `g_{Delta_5}`: imported denominator target.
- `mathfrak D_X`: sought first-order protected algebraic/Pfaffian datum, not
  constructed in the determinant proof.

### Box 2: scalar-square rule

Location: front table may include it, but it must also reappear locally in the
OP section at `main.tex:13701-13955`.

Required content:

```tex
OP/DT proves the reduced scalar square.  It detects D_5^2, not D_5.  It
does not construct a first-order square root, a Pfaffian line, or an
orientation sign.
```

### Box 3: compact source firewall

Location: before any mention of `E_3` source interfaces in the opening.

Required content:

```tex
The compact source is not used in the determinant proof.  It is a separate
construction problem.  Until supplied, all compact Hall/factorization,
orientation, hybrid locality, and primitive-recognition statements are
certificate or conditional statements.
```

## Banned/replacement language

Apply these rules in the abstract and first ten pages.  A banned phrase may
survive only inside an explicit negation or hostile-objection quotation.

| Banned or dangerous phrase | Replacement | Required local qualifier |
|---|---|---|
| theorem-level physical input | theorem-level protected-index input | K3 sigma-model index only |
| The physical question | The compact source problem / Protected operations before traces | no compact source constructed |
| compact BPS theory | compact protected-source theory | if constructed / if supplied |
| BPS Hilbert space | compact D-brane Hilbert space | not constructed |
| half-index object | arithmetic Borcherds half / Grothendieck half-index representative | arbitrary `K_0` representative |
| canonical half | chosen/arbitrary Grothendieck representative | no Hilbert-space half |
| one-particle index | virtual `K_0` determinant package / Borcherds exponent package | not a microscopic state space |
| one-particle object | virtual Borcherds package / cusp-Weyl boundary package | bulk/cusp split |
| first-order operator | first-order protected algebraic/Pfaffian datum | no analytic operator with spectrum |
| operator product | product/collision map | supplied by Hall/factorization data |
| compact realization | open compact source problem / realization certificate | open in same sentence |
| recognition theorem | recognition certificate / sufficient criterion | no source construction |
| holomorphic `E_3`-factorization algebra | holomorphic factorization source interface | supplied/open model, formality/framing datum |
| Hall source | finite Hall source kernel, if supplied | nonemptiness open |
| physical charge lattice | formal dyonic Mukai bookkeeping lattice | not full 4d charge lattice |
| Hall charge degree `(n,l,m)` | Gram/Fourier/root degree | not additive Hall grading |
| orientation character | orientation-line monodromy character | not scalar normalization |
| scalar square proves | scalar square checks normalization | orientation-forgetful |
| target proves | target records / constrains | source data missing |
| canonical branch | normalized/chosen branch on stated cover | convention named |
| construction protocol | protocol from supplied data / certificate | no nonemptiness unless proved |

Hard zero-hit phrases for the opening:

```text
constructed compact BPS
compact BPS partition function
physical Hall charge
Hall charge degree
realization theorem
canonical half
canonical source
operator with a spectrum
analytic square root of Delta
orientation from scalar
4096 orientation
64 orientation
scalar proves orientation
Borcherds product constructs Hall
determinant constructs Hall
```

Allowed only with immediate negation:

```text
one-particle
physical
BPS
operator
realization
recognition
E_3
Hall source
orientation
canonical
```

Theorem-status wording:

- Use `Theorem` only for a proved formal statement, an explicitly imported
  source theorem, or a conditional implication whose first sentence states the
  supplied data.
- Use `Definition` for data packages, target interfaces, normalized branches,
  certificate packages.
- Use `Open Problem` for compact source, orientation monodromy, hybrid wrapped
  sector, primitive source construction, row physical hosts.
- Use `Certificate` for finite data plus tests.  Do not let "certificate"
  imply nonemptiness.
- Use `Criterion` for necessary/sufficient checks after data are supplied.

Unsafe theorem names:

```text
Igusa square-root theorem
BPS determinant theorem
Compact realization theorem
Recognition theorem
Physical charge theorem
```

Safe theorem names:

```text
Normalized K_0-determinant form of the Gritsenko--Nikulin product
D6--D2--D0 Mukai--Gram dictionary
Normal-ordered Gram descent
Raw homogeneous Pi_X-pushforward obstruction
Gritsenko--Nikulin denominator algebra identity
Reduced DT/PT/OP scalar square
```

## Exact anchors

Current opening anchors to patch or move:

| Anchor | Current issue | Required action |
|---:|---|---|
| `main.tex:57-172` | Abstract is honest but overloaded; mixes determinant, denominator, OP, compact source, normal ordering, rows. | Replace as five-paragraph abstract. |
| `main.tex:58` | "theorem-level physical input" overpromises. | Replace with "theorem-level protected-index input"; specify K3 index only. |
| `main.tex:64-69` | "Borcherds half" can read as Hilbert split. | Use "arithmetic Borcherds half" and "arbitrary Grothendieck representatives." |
| `main.tex:83-98` | Denominator paragraph stable but must be imported/active-support. | Add "imported Gritsenko--Nikulin" and "active support"; deny compact source. |
| `main.tex:100-115` | "operator/algebra" can read as constructed. | Recast as open Dirac/Pfaffian problem; no analytic operator with spectrum. |
| `main.tex:117-129` | OP scalar content stable but too much abstract space. | Compress; state scalar square only and constants are normalization data. |
| `main.tex:131-171` | Abstract compact-source checklist too long; bare `E_3` too early. | Compress to formal lattice, `B`, normal ordering, raw no-go, open compact problem. |
| `main.tex:177` | Section title is accurate but weak. | Rename to `Introduction: The Dirac Problem`; preserve old label for refs. |
| `main.tex:180-213` | Starts with local-object prose and busy dependency chain. | Replace with Dirac principle plus theorem-program display. |
| `main.tex:214-224` | Protected localization input good. | Keep after theorem program under "Known protected input." |
| `main.tex:226-258` | Compact/hybrid paragraph too dense. | Split into projection-to-`E` obstruction and hybrid remedy; keep open status. |
| `main.tex:260-296` | Certificate list too long; display omits radical quotient. | Compress; add radical quotient; move list later. |
| `main.tex:298-337` | Denominator and OP summaries stable but too expansive for first page. | Fold into table plus short paragraphs. |
| `main.tex:339-355` | Row-host certificates distract from `N=1` opening. | Remove from opening; one independent-row sentence only. |
| `main.tex:357-453` | Two status tables; good content but repetitive. | Merge into one table with "does not prove" column. |
| `main.tex:462` | `The automorphic square root` before sufficient guardrails. | Retitle `The virtual automorphic square root` or remove part boundary. |
| `main.tex:464` | `The physical question` is a dangerous scan title. | Rename `The compact source problem` or `Protected Operations Before Traces`. |
| `main.tex:467-565` | Physics narrative good but loaded nouns need local caveats. | Compress; keep operations-before-traces; deny determinant-to-source inference. |
| `main.tex:570-638` | Conditional schema good but too early if `E_3` undefined. | Keep as conditional source interface after firewall; no bare construction claim. |
| `main.tex:640` | "one-particle index" is the most dangerous local phrase. | Rename to `Virtual Borcherds Package and the K_0-Determinant`. |
| `main.tex:667-738` | K3 `BPS` cohomology acceptable only fenced. | Keep; explicitly K3 worldsheet only; no compact D-brane Hilbert space. |
| `main.tex:772-830` | Bulk/cusp split strong and should stay. | Keep "neither sector is microscopic"; call `mathcal V` virtual package. |
| `main.tex:833-853` | Determinant proposition too low-status for spine. | Main agent may combine with GN product as headline theorem later. |
| `main.tex:882-918` | Proposition only names an open target. | Convert to definition/open problem; replace `operator/algebra` wording. |
| `main.tex:920-1122` | Pfaffian local certificate starts too early. | Move out of first-ten-page flow or place after determinant and guardrails. |
| `main.tex:1139-1174` | Conditional theorem mixes supplied data, Pfaffian, scalar, sign. | Split later; opening should only summarize. |
| `main.tex:2383-2630` | Normalized cusp form belongs early but after determinant. | Keep core normalization; move detailed sign computations later. |
| `main.tex:2661-2755` | D6 dictionary is theorem-level but later and labeled lemma. | Promote and move before normal ordering/scalar integration. |
| `main.tex:4309-4977` | Strongest new formal theorem appears too late. | Move into main spine before compact realization. |
| `main.tex:4883` | Raw no-go good but raw pushforward needs definition first. | Define raw homogeneous and fixed-lift pushforward before theorem. |
| `main.tex:5560-5702` | Denominator target main-spine material. | Keep after normal ordering; add determinant-does-not-determine-brackets warning. |
| `main.tex:5724-5768` | Formal current envelope can impersonate compact source. | Rename target-current envelope; curve-universal if introduced. |
| `main.tex:13701-13955` | OP scalar square correctly late. | Keep late; add scalar-square-only box. |
| `main.tex:13957-14264` | Synthesis overpackages status and rows. | Split theorem from ledger; no row/spin dependency closure. |
| `main.tex:14267-end` | Rows/spin dilute core. | Quarantine as independent ledger or companion. |

Report anchors:

- Agent 10: minimal stable spine; maximal construction-first spine; normal
  ordering under-promoted; rows/spin independent.
- Agent 13: five-paragraph abstract skeleton; exact first-page stable claims;
  radical quotient in opening recognition display.
- Agent 19: high-risk vocabulary and first-ten-pages rewrite rules.
- Agent 22: local patch IDs P0/P1/P2; especially radical quotient, section
  retitles, raw pushforward definition, flag formula, forbidden box.
- Agent 23: theorem-status taxonomy and required demotions/promotions.
- Agent 32: section-order rewrite sequence and build/checkpoint plan.

## Patch sequence

This is for the main integrating agent.  Preserve labels during block moves;
rename labels only after a clean build.

1. Preflight.
   - Run `git status --short`.
   - Record current section anchors:
     `rg -n -F '\section{' main.tex` and `rg -n -F '\part{' main.tex`.
   - Do not revert or overwrite other agents.

2. Apply opening P0 hygiene before prose rewrite.
   - Add radical quotient to `main.tex:286-291`.
   - Repair undefined or unsafe notation called out by Agent 22 where it
     affects the opening.
   - Do not move large blocks yet.

3. Replace abstract `main.tex:57-172`.
   - Five paragraphs in the order specified above.
   - No rows, no spin, no detailed `E_3`, no full certificate list.

4. Rewrite Section 1 in place.
   - Rename `main.tex:177`.
   - Replace `main.tex:180-213` with Dirac principle plus theorem-program
     display.
   - Move protected K3 input after the program.
   - Merge status tables.
   - Insert forbidden-implications box and notation table.
   - Remove row-host paragraph from the opening.

5. Retitle early sections without moving.
   - `main.tex:462`: virtual automorphic square root or remove part boundary.
   - `main.tex:464`: compact source problem / protected operations before
     traces.
   - `main.tex:640`: virtual Borcherds package and `K_0` determinant.
   - Convert `main.tex:882-918` from proposition to definition/open problem.

6. Compress current compact-source narrative in the opening.
   - Split `main.tex:226-258` into support-locality and hybrid remedy.
   - Compress `main.tex:260-296`; move certificate list later.
   - Keep `main.tex:570-638` conditional and source-interface-only.

7. Promote/move theorem-spine material after the first-ten-page rewrite builds.
   - Move normalized target core `main.tex:2383-2630` after determinant.
   - Promote D6--D2--D0 dictionary at `main.tex:2661`.
   - Move normal ordering `main.tex:4309-4977` before compact realization.
   - Define raw pushforward before `main.tex:4883`.

8. Keep denominator and OP scalar in correct relation.
   - Denominator algebra after normal ordering.
   - OP scalar remains late at `main.tex:13701-13955`.
   - Add local scalar-square-only box.

9. Quarantine orientation, rows, and spin.
   - Move detailed O1/O1+/O2 from early main flow to appendix or later compact
     section.
   - Rows start with independence disclaimer if retained.
   - Spin `L`-factor leaves the main paper unless cited by a main theorem.

10. Label and theorem-status cleanup.
    - Rename only after section order is stable.
    - Fix environment-label mismatches flagged by Agent 23.
    - Do not delete compatibility labels before ref scan.

11. Build/check.
    - After small retitles: `make fast`.
    - After large moves: static label scan, then `make fast`.
    - Before handoff: full `make`.
    - Inspect first ten rendered pages.  They must show Dirac principle,
      theorem program, status table, forbidden implications, notation table,
      determinant setup, and open target specification before residual ledgers.

Post-rewrite grep gates:

```sh
rg -n -i 'constructed compact BPS|compact BPS partition function|BPS partition function|physical Hall charge|Hall charge degree|realization theorem|recognition theorem|canonical half|canonical BPS|canonical source|operator with a spectrum|analytic square root of Delta|orientation from scalar|4096.*orientation|64.*orientation|scalar.*proves.*orientation|scalar.*constructs|Borcherds product.*constructs.*Hall|determinant.*constructs.*Hall' main.tex
```

```sh
rg -n -i 'one-particle index|one-particle object|one-particle Hilbert|one-particle K3|physical question|physical host|physical charge lattice|physical derivation|physical meaning' main.tex
```

Each positive hit requires manual review, not mechanical deletion.

Required guardrail grep concepts:

```sh
rg -n -i 'not.*Hilbert|not.*state space|not.*operator product|not.*compact.*source|not.*constructed|not.*existence theorem|orientation-forgetful|not.*orientation character|not.*additive Hall grading|Gram.*quadratic|source.*target|signed root supermultiplicities|not.*Hall constants' main.tex
```

## Residual risk

1. Minimal versus construction-first architecture remains undecided.  The safe
   opening above assumes the current minimal stable paper: virtual determinant,
   imported denominator, normal-ordered formal degree repair, scalar check,
   open compact Dirac problem.  If the main agent actually constructs
   `D^{alg}_{Delta_5,C,L}`, `H^{pre}_{X,Gamma}`, and `H^{tw}_{X,Gamma}`, the
   abstract can be upgraded only after those objects exist in source.

2. The first ten pages can become too defensive.  The fix is not more caveats.
   The fix is order: theorem program first, status table second, residuals
   later.

3. `E_3` remains expensive.  If it appears in the abstract or first page, a
   reader will ask for the operad, category, formality point, framing datum,
   and finite model.  Prefer "holomorphic factorization source interface" in
   the opening.

4. Normal ordering is still downstream in current source.  Until moved, the
   opening must preview it strongly enough that `(n,l,m)` cannot be read as a
   Hall charge.

5. Primitive recognition remains tautological if titled as a theorem without
   "certificate" and "no source construction."  Keep it as certificate/criterion
   unless source representatives, parity, relations, radical, PBW, and exact
   completion are actually proved from constructed source data.

6. OP scalar contamination is the easiest relapse.  No sentence may pass from
   `-4096 Delta_5^{-2}` to orientation/Pfaffian/source without the phrase
   "would require supplied data" or equivalent.

7. Row and spin material add hostile-referee audit surface without helping the
   first ten pages.  They must be independent ledgers or companions.

8. Public paper must not cite the attack PDF or swarm reports as sources.  They
   are integration evidence only.  Mathematical claims need primary sources or
   internal proofs.

9. Build risk is label churn.  Preserve labels during moves; semantic label
   cleanup comes last.

10. Stop condition for the opening rewrite: first ten rendered pages show the
    Dirac principle, determinant target, denominator target, normal-ordering
    necessity, scalar-square firewall, notation table, and open compact source
    problem.  If any detailed certificate table appears before those, the
    rewrite failed.
