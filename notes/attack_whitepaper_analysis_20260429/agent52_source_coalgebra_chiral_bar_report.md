# Agent52 Source Coalgebra / Chiral Bar Report

Date: 2026-04-29.

Scope: proposal-only review of the latest PDF's claim that the finite
source chiral bar coalgebra can be explicitly built.  No source edits.
Writable surface limited to this report.

Evidence base:

- latest PDF: `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`, sha256 `d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1`;
- extracted text: `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`, sha256 `c2035d6ce0f995ad41b16ad295d2bba1d110612385aea3a7d6197f8d1f7e5b17`;
- live manuscript: `main.tex`, sha256 `fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280`;
- attack-heal protocol: `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md` and `references/protocol.md`.

Commands used: `rg`, `nl -ba`, `sed`, `ls -lt`, `git status --short`,
`shasum -a 256`.

## Verdict

Stable core:

At finite height \(R\), once a finite hybrid source
\(\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}\) has already been supplied
with augmentation, bounded non-vacuum word length, finite collision flag
coherences, quotient-after-correspondence compatibility, and transition
maps, the finite reduced chiral bar coalgebra can be written explicitly as
\[
C^{\mathrm{bar}}_{X,R}
=\bar B_E^{\mathrm{ch}}
\bigl(\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}},
\varepsilon_{X,R}^{\mathrm{hyb}}\bigr).
\]
This is exactly what `main.tex:6812-6945` proves conditionally.

No stable core:

The latest PDF's later claim that this produces "the constructed finite
compact source object" is false as written.  The PDF defines the proposed
object from target/BKM data and then calls the resulting bar construction a
source coalgebra (`...revision-1923.txt:29517-29620`, `:29685-29724`).  That
is a target-derived algebraic envelope with source-like notation, not a
compact \(K3\times E\) Hall/factorization source.  It does not close the
hybrid-source, geometric provenance, primitive-recognition, orientation,
or source-to-target cobar comparison obligations.

The right formulation is:

\[
\text{finite hybrid source supplied}
\quad\Longrightarrow\quad
\text{finite source-bar coalgebra explicitly built}.
\]

Not:

\[
\text{target denominator algebra}
\quad\Longrightarrow\quad
\text{compact finite source built}.
\]

## Latest PDF Claim

The latest PDF contains two different coalgebra claims.

First, the good conditional claim:

- It says "Once the hybrid source exists" one should define the source
  coalgebra from the source, not from the target (`...revision-1923.txt:11895-11921`).
- It states the source-to-target Koszul comparison separately from the
  target counit (`:11922-11940`).
- It repeats the firewall: \(C_{X,R}\), its filtration, and its collision
  coproduct may not be defined by \(\bar B_E^{\mathrm{ch}}(\mathrm{Den})\) or
  by a target counit (`:20759-20769`).

Second, the overclaim:

- It says to "Define the finite source chiral bar coalgebra explicitly" by
  \(C_R=B_E^{\mathrm{ch}}(F_R)\) (`:29254-29265`).
- It asserts conilpotence because every tensor word has finite length and
  total degree in \(A_R\), hence \(C_R\) is a finite conilpotent source
  coalgebra (`:29329-29342`).
- It says the source-to-target map is induced by identity on primitive
  generators (`:29353-29380`).
- It then packages \(C_R=B_E^{\mathrm{ch}}(F_R^{\mathrm{hyb}})\) inside
  \(\mathrm{UDI}_R\) and says this is the constructed finite compact source
  object (`:29517-29620`).
- Its central theorem says the source coalgebra is finite conilpotent,
  \(\Theta_{\mathrm{Kos},R}\) is identity on primitive generators, and the
  Pfaffian equals \(\Delta_5\) by GN multiplicities and the Borcherds product
  (`:29655-29732`).

The overclaim fails because the proposed \(F_R\) is not shown to be a
source hybrid object with finite Hall correspondences.  The PDF's proof
uses the BKM bracket, \(U(\mathfrak g_{\Delta_5})\), Kac PBW, invariant
form, and GN multiplicities (`:29545-29555`, `:29685-29724`).  That builds a
target envelope.  It does not build compact source geometry.

## Comparison With `main.tex`

Current `main.tex` has the correct conditional architecture.

1. The abstract and introduction already say the denominator algebra supplies
   the target and target-internal bracket, but not compact Hall
   correspondences, orientation, or collision maps (`main.tex:83-98`).
   The recognition criterion is explicitly conditional and not an existence
   theorem (`main.tex:278-300`).

2. The compact-realization section opens with the source/target split:
   the current envelope is an observable target and contains no Hall
   extension correspondences; the target-side bar-cobar counit is internal
   to that target (`main.tex:5788-5797`).

3. The finite \(K3\)-to-\(E\) and hybrid source data remain supplied/open:
   \(\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\), \(\kappa_E\), \(\pi_*^{\mathrm{ch}}\),
   model categories, finite diagrams, wrapped correspondences, quotient, and
   transition coherences are all separate data (`main.tex:5851-6060`,
   `main.tex:11896-11957`).

4. The target-internal bar-cobar counit is fenced:
   \[
   \Omega_E^{\mathrm{ch}}\bar B_E^{\mathrm{ch}}
   (\mathsf{Den}_{\Delta_5,E})\to\mathsf{Den}_{\Delta_5,E}
   \]
   reconstructs only the already defined target; it is not the compact
   Koszul comparison and does not supply \(C_X\), \(\Delta_R^{\mathrm{ch}}\),
   or the source comparison map (`main.tex:6485-6531`).

5. The source-target separation lemma requires, before comparison, a finite
   hybrid source, \(C_{X,R}\), \(F^{\mathrm{co}}_{R,\bullet}\),
   \(\Delta_R^{\mathrm{ch}}\), \(b_{X,R}\), and
   \(\Theta_{\mathrm{Kos},R}\), all independent of the target counit
   (`main.tex:6533-6585`).

6. The chiral Koszul source certificate names the exact finite requirements:
   a coaugmented conilpotent chiral coalgebra with counit, finite source
   filtration, finite pull-push collision coproduct, coassociativity, counit,
   transition compatibility, bar comparison, cobar comparison, hybrid
   compatibility, normal-ordered descent, source/target separation, and
   primitive restriction (`main.tex:6587-6810`).

7. The "canonical finite source-bar coalgebra" proposition explicitly builds
   the coalgebra only under hypotheses: \(\mathfrak O_{\mathrm{hyb},R}=0\),
   transition/properness data, bounded word length \(N_R\), and augmentation
   of the supplied hybrid source (`main.tex:6812-6829`).  Under those
   hypotheses it gives the finite bar construction, length filtration,
   coaugmentation/counit, deconcatenation/collision coproduct,
   coassociativity/counit, conilpotence, identity bar comparison, and
   transition residual (`main.tex:6831-6919`).

8. The next corollary keeps the surviving obstruction alive:
   source-internal bar-cobar admissibility and a source-to-target
   quasi-isomorphism
   \(\vartheta_R:\mathcal F^{\mathrm{hyb}}_{X,\sigma,S,\le R}\to
   \mathsf{Den}_{\Delta_5,E,\le R}\) remain independent finite assertions
   (`main.tex:6947-7049`).

9. The final open problem still lists the full chiral Koszul source
   certificate as open, including the finite hybrid source, conilpotent
   compact source coalgebra, finite conilpotent filtration, collision
   coproduct with coassociativity/counit/transition diagrams, bar comparison,
   and cobar quasi-isomorphism, rather than using the target-internal counit
   (`main.tex:13461-13492`).

## Requirement Audit

### 1. Conilpotence

Current `main.tex` status: conditionally present.

- Certificate requires \(C_{X,R}\) to be coaugmented conilpotent and its
  reduced iterated coproduct nilpotent on finite stages
  (`main.tex:6632-6643`).
- Residual is explicitly
  \[
  \mathfrak o^{\mathrm{conil}}_R
  :=(\overline\Delta_R^{\mathrm{ch}})^{N_R+1}
  \]
  (`main.tex:6759-6768`).
- The finite bar construction proves
  \((\overline\Delta_R^{\mathrm{bar}})^{N_R+1}=0\) only after bounded
  word length is supplied (`main.tex:6818-6823`, `:6880-6884`, `:6922-6938`).

Latest PDF gap: it asserts finite conilpotence from finite tensor length
(`...revision-1923.txt:29329-29342`) but has not proved that the hybrid
source has a positive height on every non-vacuum surviving color, bounded
word length under all allowed local/wrapped colors, or transition-compatible
truncation.  In `main.tex`, those are hypotheses, not consequences.

Minimal heal: state conilpotence as conditional on a finite hybrid source
with an explicit height function \(h_R\), \(h_R(x)>0\) on non-vacuum colors,
bounded \(N_R\), and transition maps preserving the length filtration.

### 2. Finite Filtration

Current `main.tex` status: conditionally present.

- The certificate demands
  \[
  0=F^{\mathrm{co}}_{R,-1}\subset\cdots\subset
  F^{\mathrm{co}}_{R,N_R}=C_{X,R}
  \]
  with finite-dimensional associated graded pieces in each
  \(\Gamma_R^\Pi\)-degree (`main.tex:6632-6642`).
- The bar model uses the bar-length filtration
  \(F^{\mathrm{co}}_{R,p}C^{\mathrm{bar}}_{X,R}\)
  (`main.tex:6854-6865`).
- Filtration residuals include differential compatibility and coproduct
  compatibility with \(\sum_{i+j\le p}F_i\otimes F_j\)
  (`main.tex:6743-6757`).

Latest PDF gap: it says the filtration is by HN height, number of collision
points, and wrapped degree (`...revision-1923.txt:14723-14731`), and later
uses a finite window \(A_R\), but does not give the actual increasing
filtration, finite-dimensional graded pieces, compatibility with the bar
differential, or boundary behavior when multiplication/collision leaves the
finite window.

Minimal heal: define the finite filtration explicitly, name its index set,
state whether it is bar length, HN height, wrapped degree, or lexicographic
multi-filtration, and prove \(d_C\) and \(\Delta_R^{\mathrm{ch}}\) preserve it
in the quotient/truncation.

### 3. Collision Coproduct

Current `main.tex` status: conditionally present.

- The certificate requires a collision coproduct attached to local-local,
  ordered local-wrapped, wrapped-wrapped, and eight-word flag stacks, as a
  finite pull-push construction before \(Q_{E,R}\), satisfying coalgebra
  identities after quotient (`main.tex:6643-6657`).
- The bar model writes
  \[
  \Delta_R^{\mathrm{bar}}[x_1|\cdots|x_p]
  =1\otimes x+x\otimes1+\sum_{i=1}^{p-1}
  [x_1|\cdots|x_i]\otimes[x_{i+1}|\cdots|x_p],
  \]
  with cuts realized by finite collision and flag pull-push maps
  (`main.tex:6866-6880`).
- The proof says coassociativity is exactly equality of iterated finite flag
  cut maps (`main.tex:6929-6935`).

Latest PDF gap: it gives deconcatenation/collision splitting
(`...revision-1923.txt:29294-29305`) and a binary collision differential
(`:29317-29329`), but it does not supply the finite flag stacks,
pull-push admissibility, Thom-Sebastiani transport, quotient-after-
correspondence, or the four-input pentagon in a source category.  If the
operations are BKM bracket/product maps (`:29241-29243`), the construction
is target algebra, not source collision geometry.

Minimal heal: require a named finite correspondence category
\(\mathsf{Corr}^{E,\mathrm{hyb}}_R\), the four operation families, all
eight two-step flags, higher colored residuals, admissible pull-push maps,
and explicit coassociativity diagrams before declaring
\(\Delta_R^{\mathrm{ch}}\) constructed.

### 4. Counit

Current `main.tex` status: present in the conditional bar model, but must be
kept source-internal.

- The certificate requires coaugmentation \(\eta_R^C:k\to C_{X,R}\) and
  counit \(\varepsilon_R^C:C_{X,R}\to k\) (`main.tex:6632-6635`).
- The counit identities are part of \(\mathfrak o^{\Delta,\mathrm{ch}}_R\)
  (`main.tex:6650-6657`, `:6770-6777`).
- The bar model uses vacuum inclusion and projection to the vacuum summand
  (`main.tex:6865-6867`).
- The surviving source-internal counit
  \[
  \varepsilon^{\mathrm{src}}_{\mathrm{bar},R}:
  \Omega_E^{\mathrm{ch}}C^{\mathrm{bar}}_{X,R}\to
  \mathcal F^{\mathrm{hyb}}_{X,\sigma,S,\le R}
  \]
  must be admissible and a quasi-isomorphism; this is not the target counit
  (`main.tex:6956-6967`, `:7033-7048`).

Latest PDF gap: it discusses the target-internal counit as a different
object (`...revision-1923.txt:14741-14755`, `:26849-26880`, `:29380-29381`)
but the explicit coalgebra block at `:29254-29342` does not state the
coaugmentation, counit, counit identities, or source-internal bar-cobar
quasi-isomorphism.  It also risks hiding the counit inside generic "standard
Koszul bar signs."

Minimal heal: display \(\eta_R^C\), \(\varepsilon_R^C\), the two counit
identities, and separately display
\(\varepsilon^{\mathrm{src}}_{\mathrm{bar},R}\) with a cone residual.

### 5. Bar Comparison

Current `main.tex` status: conditionally present.

- The certificate demands a charge-preserving quasi-isomorphism of
  conilpotent chiral coalgebras
  \[
  b_{X,R}:C_{X,R}\xrightarrow{\simeq}
  \bar B_E^{\mathrm{ch}}
  (\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}},
  \varepsilon_{X,R}^{\mathrm{hyb}})
  \]
  (`main.tex:6677-6693`).
- The canonical bar model sets \(b_{X,R}\) to the identity only because
  \(C_{X,R}\) has been replaced by the bar coalgebra of the supplied hybrid
  source (`main.tex:6893-6897`).

Latest PDF gap: the later `UDI` construction sets \(C_R=B_E^{\mathrm{ch}}(F_R)\)
and makes the comparison tautological, but \(F_R\) is built from
\(\mathfrak g_{\Delta_5}\) target primitives and BKM operations.  A
tautological target bar comparison is not evidence of a source bar
comparison.

Minimal heal: split notation:

- \(C^{\mathrm{alg}}_R=\bar B_E^{\mathrm{ch}}(F^{\mathrm{alg}}_R)\) for a
  target-derived algebraic envelope;
- \(C^{\mathrm{src}}_{X,R}\) for compact source data;
- \(b^{\mathrm{src}}_{X,R}:C^{\mathrm{src}}_{X,R}\to
  \bar B_E^{\mathrm{ch}}(\mathcal F^{\mathrm{hyb}}_{X,R})\) as a source
  quasi-isomorphism, not a definition from the target.

### 6. Source-To-Target Cobar Comparison

Current `main.tex` status: explicitly still open after the bar coalgebra is
built.

- The certificate requires
  \[
  \Theta_{\mathrm{Kos},R}:\Omega_E^{\mathrm{ch}}C_{X,R}
  \xrightarrow{\simeq}\mathsf{Den}_{\Delta_5,E,\le R}
  \]
  (`main.tex:6695-6723`).
- The source-bar corollary splits the residual into the source-internal
  bar-cobar counit defect and the source-to-target quasi-isomorphism defect
  \(\mathfrak o^\vartheta_R\) (`main.tex:6947-7037`).
- It says no target homotopy inverse enters (`main.tex:7039-7048`).

Latest PDF gap: it says the source-to-target map is identity on primitive
generators (`...revision-1923.txt:29353-29380`, `:29669-29675`).  If the
primitive generators are already \(V_\gamma=\mathfrak g_{\Delta_5,\gamma}\),
then the comparison is tautological and cannot prove compact source
recognition.  It may define a target-envelope normalization only.

Minimal heal: require a non-tautological \(\vartheta_R\) from source hybrid
operations to the target current envelope, with differential, product, unit,
transition, cone, and primitive-restriction residuals as in
`main.tex:6998-7031`.

### 7. Target/Source Firewall

Current `main.tex` status: strong and should be preserved.

- The target current envelope is not a compact BPS state space and contains
  no Hall extension correspondences (`main.tex:5788-5797`).
- The target counit reconstructs only the target (`main.tex:6485-6531`).
- The source certificate forbids defining \(C_{X,R}\),
  \(F^{\mathrm{co}}_{R,\bullet}\), or \(\Delta_R^{\mathrm{ch}}\) from
  \(\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E,\le R})\) or from a
  homotopy inverse to the target counit (`main.tex:6610-6617`).
- The \(D_X\) entry repeats that the target-internal counit does not supply
  \(C_X\), \(b_X\), or \(\Theta_{\mathrm{Kos}}\) (`main.tex:12147-12201`).

Latest PDF gap: the early firewall text is correct, but the later `UDI`
claim violates the spirit of the firewall by defining a "source" out of
target primitives, target PBW, BKM brackets, and GN multiplicities, then
declaring compact source construction.  It avoids the forbidden literal
definition \(C_R=\bar B(\mathrm{Den})\), but reaches the same circularity by
building \(F_R\) from the target and then applying \(\bar B(F_R)\).

Minimal heal: forbid both direct and indirect target transport:

> \(C_R\) is not a source coalgebra if \(F_R\) is defined from
> \(\mathfrak g_{\Delta_5}\), \(U(\mathfrak g_{\Delta_5})\), target PBW,
> or GN multiplicities rather than from finite source correspondences.

## Destroyed Claims

1. "The finite source chiral bar coalgebra is constructed unconditionally."
   Destroyed.  It is constructed only after the finite hybrid source and
   bounded-length/augmentation/transition hypotheses are supplied.

2. "\(\mathrm{UDI}_R\) is the constructed finite compact source object."
   Destroyed.  The displayed \(\mathrm{UDI}_R\) uses target denominator
   algebra data.  It can be a universal algebraic target envelope only.

3. "Conilpotence follows just from finite degree window \(A_R\)."
   Destroyed.  One needs positivity on non-vacuum colors, bounded word
   length, and compatibility with the collision differential and finite
   truncation.

4. "The source-to-target Koszul map is identity on primitive generators."
   Destroyed for source claims.  Identity on primitives is tautological if
   primitives were defined as \(\mathfrak g_{\Delta_5}\).  A compact source
   theorem needs actual source primitive representatives and a
   quasi-isomorphism with cone and transition checks.

5. "Target PBW/radical/Kac presentation proves source PBW/radical."
   Destroyed.  Source PBW/radical requires finite pairing matrices, radical
   bases, Lie-ideal and coideal tests, no-extra-relations, and transition
   compatibility (`main.tex:12408-12486`, `main.tex:13303-13360`).

## Healed Construction

Safe wording for later integration:

```tex
\begin{proposition}[Finite source-bar coalgebra after a supplied hybrid source]
Fix a finite height \(R\).  Assume the finite hybrid source
\(\mathcal F^{\mathrm{hyb}}_{X,\sigma,S,\le R}\) has been constructed with
augmentation \(\varepsilon^{\mathrm{hyb}}_{X,R}\), finite collision flag
correspondences, quotient-after-correspondence compatibility,
proper/admissible pull-push operations, transition maps, and a bounded
non-vacuum bar length \(N_R\).  Then the reduced chiral bar construction
\[
C^{\mathrm{bar}}_{X,R}
=\bar B_E^{\mathrm{ch}}
(\mathcal F^{\mathrm{hyb}}_{X,\sigma,S,\le R},
\varepsilon^{\mathrm{hyb}}_{X,R})
\]
is a coaugmented counital conilpotent finite chiral coalgebra.  Its
filtration is bar length, its coproduct is the finite collision
deconcatenation coproduct, and its reduced coproduct is nilpotent of order
\(N_R+1\).  This construction is source-side.  It does not define the
hybrid source and it does not construct the source-to-target cobar
quasi-isomorphism.
\end{proposition}
```

Safe target-envelope wording:

```tex
If one defines an algebraic finite envelope from
\(\mathfrak g_{\Delta_5}\) and its current algebra, its bar coalgebra is a
target-derived algebraic bar model.  It may be useful as a comparison
object, but it is not a compact \(K3\times E\) source coalgebra until a
finite source realization with provenance, collision correspondences,
orientation data, and transition-compatible bar comparison is supplied.
```

## Residual Obligations

1. Construct \(\mathcal F^{\mathrm{hyb}}_{X,\sigma,S,\le R}\) from finite
   local/wrapped source correspondences, not from target BKM operations.

2. Give a positive height/length function and prove bounded non-vacuum word
   length \(N_R\) for every finite \(R\).

3. Define the finite filtration \(F^{\mathrm{co}}_{R,\bullet}\) and prove
   differential and coproduct compatibility.

4. Construct \(\Delta_R^{\mathrm{ch}}\) as finite source collision pull-push,
   including all local-local, local-wrapped, wrapped-wrapped, and eight-word
   flag correspondences.

5. Display coaugmentation, counit, counit identities, and the source-internal
   bar-cobar counit residual.

6. Prove transition compatibility of coalgebras, filtrations, coproducts,
   and bar comparisons for \(R'\ge R\).

7. Prove source-internal bar-cobar admissibility in the BD/FG domain.

8. Construct the source-to-target \(\vartheta_R\) or
   \(\Theta_{\mathrm{Kos},R}\) with cone, product, unit, primitive, and
   transition checks.

9. Keep target-derived algebraic envelopes separate from compact geometric
   source data in notation and theorem status.

## Attack Ledger

```yaml
id: A52-01
severity: 1
status: valid
lens: source_coalgebra_firewall
target: latest PDF lines 29517-29620
claim: "UDI_R is the constructed finite compact source object."
broken_step: The tuple uses target BKM/GN data and then applies a bar construction to a target-derived hybrid object.
evidence_type: line_reference
evidence_ref: materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:29517-29732; main.tex:6812-7049; main.tex:13461-13492
files_read:
  - materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt
  - main.tex
tools_used: [rg, nl, sed]
confidence: high
blast_radius: central theorem, compact realization section, source coalgebra theorem
minimal_heal: Retitle as target-derived algebraic envelope, or make the source provenance and finite hybrid correspondences explicit before calling it source.
residual: No finite source data artifacts or geometric hybrid source construction exist in this checkout.
deciding_evidence: source provenance, finite correspondence category, operation tensors, coalgebra maps, and transition checks independent of the target envelope.
```

```yaml
id: A52-02
severity: 2
status: valid
lens: conilpotence
target: latest PDF lines 29254-29342
claim: "C_R is finite conilpotent because words have finite length and total degree in A_R."
broken_step: Bounded word length for all surviving non-vacuum source colors, compatibility with the differential, and finite transition truncation are not proved.
evidence_type: proof_gap
evidence_ref: main.tex:6818-6823; main.tex:6854-6884; main.tex:6922-6938
files_read:
  - materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt
  - main.tex
tools_used: [nl, sed]
confidence: high
blast_radius: finite source-bar proposition, Koszul certificate, inverse limit
minimal_heal: Add bounded-length hypothesis and prove reduced coproduct nilpotence under the actual source filtration.
residual: Need finite hybrid source and height function.
deciding_evidence: explicit \(N_R\), filtration-preserving differential/coproduct, and nilpotence proof.
```

```yaml
id: A52-03
severity: 2
status: valid
lens: collision_coproduct
target: latest PDF lines 29294-29329
claim: "The coproduct/differential is deconcatenation plus binary collision."
broken_step: Source collision pull-push correspondences, quotient-after-correspondence, finite flag pentagons, and counit flags are not supplied.
evidence_type: proof_gap
evidence_ref: main.tex:6643-6657; main.tex:6869-6880; main.tex:6929-6935
files_read:
  - materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt
  - main.tex
tools_used: [nl, sed]
confidence: high
blast_radius: coalgebra identities, bar comparison, primitive source bracket
minimal_heal: Construct \(\mathsf{Corr}^{E,\mathrm{hyb}}_R\), all collision flags, and the finite coassociativity/counit diagrams.
residual: Hybrid local/wrapped source remains open.
deciding_evidence: finite pull-push maps and commuting two- and three-cut diagrams.
```

```yaml
id: A52-04
severity: 1
status: valid
lens: koszul_comparison
target: latest PDF lines 29353-29380
claim: "Theta_Kos,R is induced by identity on primitive generators."
broken_step: If primitive generators are already the target root spaces, the map is tautological and does not compare a compact source to the denominator envelope.
evidence_type: proof_gap
evidence_ref: main.tex:6695-6723; main.tex:6947-7049; main.tex:12570-12574
files_read:
  - materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt
  - main.tex
tools_used: [nl, sed]
confidence: high
blast_radius: source-to-target theorem, primitive recognition, central Igusa equality
minimal_heal: Split target-envelope normalization from compact source comparison; require \(\mathfrak o^\vartheta_R=0\).
residual: Need source primitive representatives and a non-tautological source-to-target quasi-isomorphism.
deciding_evidence: cone-zero quasi-isomorphism with product, unit, transition, and primitive restrictions from source data.
```
