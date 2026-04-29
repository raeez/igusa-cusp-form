# Agent 19 Standalone Voice / Overclaim Report

Scope: audit standalone readability, mathematical voice, overclaim language, and forbidden conflations in `main.tex`, against `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`.

Verdict: the paper has become much safer than the attacked draft because it repeatedly says "target", "supplied", "open", "not constructed", "not a Hilbert space", and "not determined by the scalar square". The remaining danger is lexical, not only mathematical. The opening ten pages still use words whose ordinary meaning lets a hostile referee read formal target data as a compact physical construction. The rewrite must make every high-risk word carry its status locally, not three sections later.

## High-risk language inventory

### 1. `physical`

Risk: `physical` is too strong when the object is only a protected index, a formal Mukai bookkeeping lattice, an automorphic target, or a supplied compact-source problem. It invites the reader to ask for a full physical Hilbert space, U-duality group, wall-crossing theory, locality model, and compact BPS category.

Unsafe classes:

- `theorem-level physical input` for the K3 elliptic genus. This sounds like a theorem of compact spacetime physics. Use "theorem-level protected-index input".
- `The physical question` as a section title. It promises more physics than the manuscript constructs.
- `physical host` for the eight rows unless immediately followed by "certificate" and the missing data.
- `physical charge lattice` unless the sentence distinguishes the additive Mukai/formal lattice from the Gram triple.

Current anchors:

- `main.tex:58` says "theorem-level physical input".
- `main.tex:464` titles a section "The physical question".
- `main.tex:349-354` and `main.tex:14289-14336` use "physical host" / "Physical-host certificate".
- `main.tex:261-265` correctly says `\Gamma_X^{phys}` is mnemonic, not the four-dimensional charge lattice.
- `main.tex:14062-14085` correctly separates additive formal lattice from quadratic Gram shadow.

Safe class: "physics motivation", "protected-index input", "compact source problem", "Hall-side data", "automorphic target", "row-host certificate".

### 2. `BPS`

Risk: `BPS` is read by physicists as a microscopic sector or Hilbert-space statement. Here most objects are protected Euler characteristics, Grothendieck representatives, or conditional Hall primitives.

Unsafe classes:

- `BPS theory`, `BPS Hilbert space`, `BPS operator product`, `BPS partition function`, unless the sentence says "not constructed", "if supplied", or "open".
- `BPS space in degree (n,l)` for the K3 worldsheet cohomology is acceptable only because the definition is explicitly the K3 protected index, not the compact `K3 x E` D-brane Hilbert space.

Current anchors:

- `main.tex:96-98` correctly negates compact BPS Hilbert/product claims.
- `main.tex:180-186` says "A compact BPS theory ... should produce"; this should be demoted to "A compact protected-source theory, if constructed...".
- `main.tex:686-700` defines K3 `\mathcal H^{BPS}_{n,l}(S)`; keep this fenced to the K3 sigma-model localization theorem.
- `main.tex:829-830` correctly says compact BPS meaning is separate.
- `attack_whitepaper_analysis.txt:66-75` flags the same issue.

Safe class: "protected K3 cohomology", "protected index", "compact Hall source, if supplied", "source-side primitive class".

### 3. `operator`

Risk: `operator` suggests a defined domain, spectrum, trace-class or determinant-class analysis, and functional calculus. The paper has a formal first-order algebraic/Pfaffian target unless a compact certificate is supplied.

Unsafe classes:

- `first-order protected operator/algebra` without "supplied" or "open".
- `operator product` unless it is explicitly absent.
- `Dirac operator` as more than analogy.

Current anchors:

- `main.tex:103-110` introduces `\mathfrak D_X` as an operator/algebra; the surrounding "open recognition problem" helps but should be stronger.
- `main.tex:882-917` explicitly says the determinant does not produce an operator with a spectrum; this is good and should be echoed in the abstract.
- `main.tex:11561-11563` correctly says finite source data are not yet `\mathfrak D_X`.

Safe class: "first-order protected algebraic datum", "Pfaffian-line datum", "operator-like datum after certificate", "not an operator with a spectrum".

### 4. `one-particle`

Risk: `one-particle` is the worst local phrase in the opening. It suggests microscopic states. The manuscript's object is a virtual `K_0` determinant package and a Borcherds exponent package; the `m=0` factors are boundary/Weyl factors.

Unsafe classes:

- Section title "The one-particle index and its determinant".
- `one-particle index` when referring to `\mathbb U_{n,l}` or `\mathcal V_{(n,l,m)}`.
- `protected one-particle index` unless the compact primitive object has been supplied.

Current anchors:

- `main.tex:640` section title.
- `main.tex:561-565` calls the determinant "the normalized automorphic determinant of the virtual protected one-particle index".
- `main.tex:776-777` correctly says neither sector is a microscopic one-particle Hilbert space.
- `attack_whitepaper_analysis.txt:241-321` and `735-768` identify this as dangerous.

Safe class: "virtual `K_0` determinant package", "Borcherds exponent package", "boundary/Weyl correction package", "protected primitive class, if supplied".

### 5. `realization`

Risk: `realization` can mean "constructed model". The paper often means "open problem" or "certificate target".

Unsafe classes:

- `compact realization` without "open", "would", "if supplied", "certificate", or "problem" in the same sentence.
- `physical realization` unless it is a future construction obligation.
- `realization theorem` anywhere.

Current anchors:

- `main.tex:7` title says `K3\times E realization problem`. Acceptable if the abstract immediately says no realization is constructed.
- `main.tex:131-168` uses "A compact realization would..." correctly, but the paragraph is dense and should repeat "open source problem" at its end.
- `main.tex:11750-11766` defines "Dirac--Igusa realization certificate" and states non-consequence; good.
- `main.tex:14142-14146` correctly says the microscopic comparison is open unless a certificate is supplied.

Safe class: "compact source problem", "Dirac--Igusa realization certificate", "open compact realization problem", "source construction, not supplied".

### 6. `recognition`

Risk: `recognition` can be tautological. A theorem that assumes primitive representatives, parity splits, relations, no-extra-relations, PBW compatibility, and radical equality should not read like a new construction theorem.

Unsafe classes:

- `recognition theorem` when the hypotheses already include the source-side presentation.
- `recognition target` if it is not clear that the target is not an existence statement.

Current anchors:

- `main.tex:260-296` correctly says the recognition criterion is conditional.
- `main.tex:882-917` uses "open recognition target".
- `main.tex:12124` title "Primitive recognition certificate; no source construction" is good.
- `attack_whitepaper_analysis.txt:448-478` says the theorem is useful as a certificate checklist, weak as a theorem.

Safe class: "recognition certificate", "sufficient criterion after supplied data", "presentation-identification certificate", "no source construction".

### 7. `E_3`

Risk: `E_3` is underdefined for a complex threefold. A reader can ask whether this is real little 3-disks, holomorphic disks, framed `E_3`, `E_6`, or a Costello-Gwilliam factorization model.

Unsafe classes:

- `holomorphic E_3-factorization algebra` before the operadic model, formality point, and framing/homotopy witness are named.
- `E_3 source` without "interface", "open", or "supplied".

Current anchors:

- `main.tex:131-136` puts `E_3` in the abstract. Too early unless it is explicitly "open source interface".
- `main.tex:570-617` defines a conditional local protected observable schema and correctly says it becomes compact `E_3` only after finite witnesses.
- `main.tex:5770-5790` now defines the intended holomorphic `E_3` sense and denies `SO(6)`/`SO(3)` claims. Good, but this clarification occurs far after the abstract.
- `main.tex:6317-6355` correctly makes compact `E_3` source an open problem.
- `attack_whitepaper_analysis.txt:493-560` gives the hostile objection.

Safe class: "holomorphic factorization algebra on `X`", "holomorphic `E_3` source interface, open", "chosen operadic model with formality/framing datum", "not a constructed functor".

### 8. `Hall source`

Risk: "source" implies existence. A finite Hall source kernel is one of the missing compact data, not something the product gives.

Unsafe classes:

- `Hall source` without `supplied`, `finite`, `kernel`, `open`, `certificate`, or `not constructed`.
- `source construction` unless it says "no source construction" or "open".

Current anchors:

- `main.tex:212-213` correctly says scalar OP/DT is not an input to the compact Hall source.
- `main.tex:5707-5716` correctly separates target from source.
- `main.tex:10994-11093`, `11552-11569`, `11646-11659` use "finite Hall source" in a supplied/open way.

Safe class: "finite Hall source kernel, if supplied", "source-side compact data", "compact Hall source problem".

### 9. `orientation`

Risk: orientation is the first-order/Pfaffian data that the scalar square forgets. Any wording that lets `64`, `4096`, OP/DT, or `Delta_5^2` determine orientation is fatal.

Unsafe classes:

- `orientation character` near scalar normalization unless the sentence says not determined.
- `orientation data exists` unless the quotient, finite-stabilizer, and Weyl transport obstructions are named.
- "orientation line" as if Joyce-Upmeier alone proves the reduced `K3 x E` quotient monodromy.

Current anchors:

- `main.tex:100-129` correctly says scalar is orientation-forgetful.
- `main.tex:331-337`, `13924-13955`, `14168-14179` correctly deny scalar-to-orientation inference.
- `main.tex:1177-1238` correctly expands strong orientation into quotient gerbe and finite-stabilizer data.
- `attack_whitepaper_analysis.txt:431-448` and `2578-2693` stress this point.

Safe class: "orientation-line monodromy condition", "supplied quotient-orientation package", "Pfaffian datum", "not scalar normalization".

### 10. `compact`

Risk: `compact` sounds like the constructed compact `K3 x E` theory. The word is safe only if it is paired with "open", "would", "if supplied", "certificate", or "not constructed".

Current anchors:

- `main.tex:96-98`, `223-224`, `829-830`, `860-863` correctly negate compact construction.
- `main.tex:180-186` needs stronger local status.
- `main.tex:1142-1174` uses compact in assumptions and explicitly says state-side construction remains open. Good.

Safe class: "compact source, if constructed", "compact realization problem", "compact certificate", "not a compact state space".

### 11. `canonical`

Risk: `canonical` is false unless there is a universal property or a cited canonical construction. Many objects here require choices: half-index representative, parity split, orientation line, formality point, framing, quotient linearization, branch.

Unsafe classes:

- `canonical half`.
- `canonical source`.
- `canonical branch` unless the branch is fixed by a named normalization and the word means "chosen convention after normalization".

Current anchors:

- `main.tex:365-366`, `733-738`, `869-870` correctly deny canonical half-Hilbert space.
- `main.tex:6731` title "Canonical finite source-bar coalgebra" is suspicious unless the construction is canonical inside a supplied certificate. It should be retitled "Supplied finite source-bar coalgebra" or "Finite source-bar coalgebra attached to a supplied source".
- `main.tex:15952` "Canonical fractional branch" should be audited. If the branch is a chosen normalized branch on a cover, say that.

Safe class: "chosen", "fixed", "normalized", "target-internal universal", "imported".

### 12. `proof`

Risk: theorem names and prose can overstate conditional packages. A "proof" that unpacks a supplied certificate is a verification or consequence, not a construction proof.

Unsafe classes:

- `proof of compact...` where the construction is open.
- "proves orientation" when only a local sign after residual vanishing is computed.
- `theorem` titles that hide "conditional".

Current anchors:

- `main.tex:1054-1122` correctly says conditional finite local-sign computation.
- `main.tex:11518-11661` title explicitly separates proved/imported/conditional/open parts. Good.
- `main.tex:14031` "Coefficient dictionary and claim-strength synthesis" is acceptable, but its first item at `14048` overstates "Igusa square root".

Safe class: "proved in this paper", "imported theorem", "conditional consequence", "finite check", "certificate equivalence".

### 13. `certificate`

Risk: "certificate" can become a talisman. It must be defined as data plus tests. It must not imply nonemptiness.

Unsafe classes:

- `certificate` without saying whether it is supplied, open, a zero locus, or nonempty.
- `certificate theorem` if the theorem only restates the certificate.

Current anchors:

- `main.tex:390-397` defines certificate vocabulary. Good.
- `main.tex:6192-6231` correctly says the zero groupoid is not a single obstruction complex before the finite problem is solved.
- `main.tex:6269-6279` correctly says no nonemptiness follows.
- `main.tex:11750-11766` correctly says the realization certificate is not a consequence of the product/scalar/current envelope.

Safe class: "finite list of data and tests", "zero locus", "supplied certificate", "nonemptiness open".

### 14. `target`

Risk: `target` is mostly safe, but it must not blur into "source". The target is automorphic/denominator/formal current data. It is not compact geometry.

Current anchors:

- `main.tex:94-98`, `298-310`, `5707-5716`, `12804-12836` correctly separate target and source.
- `main.tex:1435-1437` says automorphic target checks do not use scalar normalization. Good.

Safe class: "automorphic target", "denominator target", "target-internal", "target check only".

### 15. `scalar`

Risk: scalar facts are true but weak. Scalar equality cannot prove orientation, Pfaffian line, compact source, parity split, bracket, or Hall correspondences.

Current anchors:

- `main.tex:117-129`, `312-337`, `13701-13955`, `14111-14133` correctly state scalar normalization.
- `attack_whitepaper_analysis.txt:390-448` says OP/DT scalar square is not evidence for the square root.

Safe class: "reduced OP/DT scalar branch", "orientation-forgetful scalar square", "normalization conversion", "not a source of first-order data".

## Safe replacement vocabulary

| Current phrase class | Replace with | Required local status |
|---|---|---|
| theorem-level physical input | theorem-level protected-index input | "K3 sigma-model index only" |
| physical question | compact source problem | "no source constructed" |
| compact BPS theory | compact protected-source theory | "if constructed / if supplied" |
| BPS Hilbert space | compact D-brane Hilbert space | "not constructed" |
| one-particle index | virtual `K_0` determinant package | "not a state space" |
| one-particle object | Borcherds exponent package / boundary-Weyl package | split bulk/cusp |
| first-order operator | first-order protected algebraic/Pfaffian datum | no spectrum unless domain supplied |
| operator product | product/collision map | supplied by Hall/factorization data |
| compact realization | compact source certificate / open compact realization problem | "open" in same sentence |
| recognition theorem | recognition certificate / sufficient criterion | "no source construction" |
| holomorphic `E_3`-factorization algebra | holomorphic factorization source interface | named operad + formality/framing datum |
| Hall source | finite Hall source kernel, if supplied | nonemptiness open |
| orientation character | orientation-line monodromy character | not scalar normalization |
| canonical half | chosen Grothendieck representative | no Hilbert-space half |
| canonical branch | normalized/chosen branch on the stated cover | branch convention named |
| target proves | target records / target constrains | source data still missing |
| scalar square proves | scalar square checks normalization | orientation-forgetful |

## First-ten-pages rewrite rules

1. The abstract must be a status ledger, not a physics manifesto. Its chain should be:
   protected K3 index -> arbitrary `K_0` half representative -> normalized Gritsenko-Nikulin product -> imported denominator target -> imported OP/DT scalar square -> open compact source certificate.

2. Replace `main.tex:58` with a non-physical opening:
   "For `X=K3 x E`, the only theorem-level index input used below is the protected K3 elliptic genus."
   Then immediately state that it is not a compact D-brane Hilbert space.

3. Move the `E_3` phrase out of the first abstract paragraph. If it stays in the abstract at `main.tex:131-136`, write:
   "A compact source, not constructed here, would have to supply a holomorphic factorization source interface, including a chosen `E_3` operadic model, formality/framing datum, and finite HN control."

4. `main.tex:100-110` should not say "operator/algebra" without a local denial of analytic operator status. Use:
   "The first-order object sought is an algebraic/Pfaffian protected datum. No operator with a spectrum is constructed."

5. `main.tex:177-213` should begin with claim strength, not "The local object comes first." The present sentence is good physics prose but unsafe standalone mathematics. Rewrite as:
   "The compact source problem is not used in the determinant proof. It is the open problem whose solution would upgrade the target data to a first-order protected object."

6. Rename `\section{The physical question}` at `main.tex:464` to `\section{The compact source problem}` or `\section{Protected-source problem}`. A section title is scanned before qualifiers.

7. The first ten pages must not contain `\Gamma_X^{phys}` unless a boxed warning appears before it:
   "`\Gamma_X^{phys}` is mnemonic for the formal full-Mukai bookkeeping lattice in this paper. It is not the full four-dimensional U-duality charge lattice."
   Better: use `\Gamma_X^{form}` from the first occurrence and reserve `phys` for quoted hostile objections only.

8. Rename `\section{The one-particle index and its determinant}` at `main.tex:640`. Use:
   "`The virtual K_0 determinant and the Borcherds product`".
   The K3 `Q_R`-cohomology may still be called a protected K3 BPS cohomology, but `\mathcal V` must not be called one-particle.

9. Every paragraph in the opening that contains `compact`, `Hall`, `orientation`, `E_3`, or `source` must also contain one of:
   `open`, `if supplied`, `would`, `not constructed`, `certificate`, `target check only`.

10. The first ten pages must contain the "four nots" before the first theorem:
    - `\mathbb U_{n,l}` is not a Hilbert-space half.
    - `(n,l,m)` is not an additive Hall charge.
    - `\Delta_5^{-2}` is not a first-order object.
    - `\mathfrak g_{\Delta_5}` is not automatically a compact BPS algebra.

## Theorem/proposition/open-problem naming rules

### Theorem

Use `theorem` only when one of these is true:

- the paper proves a new formal/lattice/product statement from displayed definitions;
- the theorem is explicitly imported and named by source;
- the result is a conditional implication whose title begins with `Conditional` and whose first sentence says what data are assumed.

Do not use a theorem title that sounds like it constructs compact physics when the proof only unpacks supplied data.

Safe theorem titles:

- `Normalized K_0-determinant form of the Gritsenko--Nikulin product`
- `Reduced DT/PT/OP scalar square`
- `Strict fixed-lift raw Gram descent obstruction`
- `Conditional finite type-II local-sign computation`
- `Finite D_0 certificate: proved, imported, conditional, and open parts`

Unsafe theorem titles:

- `Igusa square-root theorem`
- `BPS determinant theorem`
- `Compact realization theorem`
- `Recognition theorem`
- `Physical charge theorem` unless it proves an additive charge theorem and separates Gram shadow.

### Proposition

Use `proposition` for:

- a finite calculation;
- a target-side algebraic fact;
- an obstruction statement;
- a certificate equivalence;
- a "does not determine" separation.

Good current examples:

- `main.tex:853` `Virtuality of the square root`
- `main.tex:12804` `The determinant does not determine compact Hall constants`
- `main.tex:6269` `No nonemptiness from the finite source certificate`

Risky current examples:

- `main.tex:882` `Dirac/Pfaffian recognition target` should be `Open Dirac--Pfaffian target specification` or `First-order Pfaffian target; no operator constructed`.
- `main.tex:5743` `Formal current envelope` is safe, but the label `thm:factorization-square-root` at `main.tex:5745` is unsafe and should be renamed when source edits are allowed.

### Definition

Use `definition` for:

- certificate data;
- target interfaces;
- formal envelopes;
- normalized branches;
- obstruction tuples.

If a definition contains `compact`, its first sentence should say whether the datum is supplied, open, or only a candidate. `main.tex:6024-6140` does this well.

### Open problem

Every construction obligation that a referee could ask for must be an open problem, not a theorem hypothesis hidden in prose.

Required open-problem names:

- Compact holomorphic factorization / `E_3` source.
- Rectified `K3`-to-`E` specialization.
- Hybrid wrapped positive elliptic-degree sector.
- Strong reduced orientation and quotient gerbe trivialization.
- Orientation monodromy equals Maass character.
- Primitive Hall recognition after normal-ordered Gram descent.
- Row-by-row physical-host certificates.

## Abstract/intro voice rules

1. Use status verbs:
   `computes`, `packages`, `imports`, `records`, `proves`, `formulates`, `does not construct`.

2. Avoid mission verbs:
   `realizes`, `explains`, `derives physically`, `constructs the square root`, `builds a BPS object`, `identifies the compact theory`.

3. The Dirac analogy is allowed only after the scalar/first-order distinction has been made formally:
   "Dirac" means first-order algebraic/Pfaffian datum whose square loses sign/orientation data. It does not mean an analytic operator has been constructed.

4. Every loaded noun must be typed:
   - `Delta_5`: theta-normalized automorphic form.
   - `D_5`: monic Borcherds product.
   - `\mathbb U_{n,l}`: arbitrary Grothendieck representative.
   - `\mathcal V`: virtual `K_0` determinant package.
   - `(n,l,m)`: Gram/Fourier/root degree, not additive Hall charge.
   - `\mathfrak g_{\Delta_5}`: imported denominator target.
   - `Z^X_{OP/DT}`: reduced scalar branch.
   - `\mathfrak D_X`: sought first-order protected datum, not constructed.

5. The introduction should not ask the reader to remember a later caveat. If a sentence contains a dangerous noun, it carries its caveat locally.

6. Standalone cold-reader rule: a reader who stops after page 3 must know exactly what is proved, what is imported, what is conditional, and what is open.

## main.tex grep anchors

Critical anchors to inspect in the rewrite queue:

- `main.tex:7` title/subtitle: `realization problem` is acceptable only if the abstract remains no-overclaim.
- `main.tex:58-69` abstract opening: `theorem-level physical input`, protected index, virtual object.
- `main.tex:94-98` target/source separation around denominator algebra and compact BPS absence.
- `main.tex:100-115` Dirac/Pfaffian square-root language, `operator/algebra`, orientation monodromy.
- `main.tex:131-168` compact realization and `E_3` source obligations in the abstract.
- `main.tex:177-213` introduction dependency chain and scalar/Pfaffian separation.
- `main.tex:226-258` compact/hybrid factorization; ensure "open" remains local.
- `main.tex:260-296` primitive recognition; keep the tautology warning.
- `main.tex:339-355` eight-row physical-host certificate language.
- `main.tex:390-397` status vocabulary definition. This should move earlier if possible.
- `main.tex:464` section title `The physical question`.
- `main.tex:467-565` physical/locality narrative; every `BPS`, `E_3`, `realization`, and `target` must be status-tagged.
- `main.tex:570-617` local protected observable algebra schema; good conditional framing, but `E_3` must stay "after finite witnesses".
- `main.tex:640` section title `The one-particle index and its determinant`.
- `main.tex:667-738` K3 BPS cohomology and Grothendieck half; keep the "no canonical half" line.
- `main.tex:772-830` bulk/cusp split; keep "neither sector is microscopic".
- `main.tex:882-917` Dirac/Pfaffian recognition target; rename proposition and weaken `operator`.
- `main.tex:920-1122` local Pfaffian subcertificate; keep "subcertificate" and "does not construct".
- `main.tex:1139-1174` conditional Dirac/Pfaffian theorem; keep "assumption" and "state-side construction remains open".
- `main.tex:5704-5716` compact realization section opening; good target/source separation.
- `main.tex:5743-5756` formal current envelope; rename `thm:factorization-square-root` label when edits are allowed.
- `main.tex:5770-5790` `E_3` definition; this clarification should be summarized in the opening.
- `main.tex:6192-6279` compact `E_3` source certificate and nonemptiness denial.
- `main.tex:9973-10125` first-order `D_0` certificate; good assumptions but lexically heavy.
- `main.tex:11518-11661` finite `D_0` theorem; good status separation.
- `main.tex:11750-11766` Dirac--Igusa realization certificate; good non-consequence statement.
- `main.tex:12124-12168` primitive recognition certificate; good "no source construction" title.
- `main.tex:12804-12836` determinant does not determine Hall constants; this proposition should be cited in the introduction.
- `main.tex:13701-13955` scalar square; keep scalar/orientation separation.
- `main.tex:14031-14201` main synthesis theorem; replace `theta-normalized Igusa square root` at `main.tex:14048` with "theta-normalized Gritsenko--Nikulin product packaged as a virtual `K_0` determinant".
- `main.tex:14289-14336` physical-host certificate; consider "row-host certificate".
- `main.tex:15952` canonical fractional branch; audit `canonical`.

## Mandatory banned/required grep list

Run these after the rewrite. Any positive hit in the banned list needs manual review, not automatic deletion.

### Banned or zero-hit phrase classes

```bash
rg -n -i 'constructed compact BPS|compact BPS partition function|BPS partition function|physical Hall charge|Hall charge degree|realization theorem|recognition theorem|canonical half|canonical BPS|canonical source|operator with a spectrum|analytic square root of Delta|orientation from scalar|4096.*orientation|64.*orientation|scalar.*proves.*orientation|scalar.*constructs|Borcherds product.*constructs.*Hall|determinant.*constructs.*Hall' main.tex
```

```bash
rg -n -i 'E_3-factorization algebra|E3-factorization algebra|holomorphic E_3-factorization algebra' main.tex
```

Every hit of the second command must be in a sentence containing at least one of:
`open`, `supplied`, `interface`, `chosen operadic model`, `formality`, `framing`, `not constructed`.

```bash
rg -n -i 'one-particle index|one-particle object|one-particle Hilbert|one-particle K3' main.tex
```

Allowed only in negated warning sentences or in a section title after it has been renamed away.

```bash
rg -n -i 'physical question|physical host|physical charge lattice|physical derivation|physical meaning' main.tex
```

Each hit must be either replaced or locally qualified as protected-index motivation, formal charge data, or a row-host certificate.

### Required guardrail hits

These phrases, or close TeX equivalents, must remain visible near the opening:

```bash
rg -n -i 'not.*Hilbert|not.*state space|not.*operator product|not.*compact.*source|not.*constructed|not.*existence theorem|orientation-forgetful|not.*orientation character|not.*additive Hall grading|Gram.*quadratic|source.*target|signed root supermultiplicities|not.*Hall constants' main.tex
```

Required exact concepts:

- `\mathbb U_{n,l}` is an arbitrary `K_0` representative.
- `\mathcal V` is a virtual `K_0` determinant package.
- `(n,l,m)` is a Gram/Fourier/root degree, not an additive Hall charge.
- `\mathfrak g_{\Delta_5}` is imported denominator target data.
- `Z^X_{OP/DT}` is a reduced scalar branch and orientation-forgetful.
- `64` is theta-leading normalization; `4096` is scalar normalization; neither is orientation.
- compact Hall/factorization/source data are not constructed.
- recognition is a certificate, not an existence theorem.

## Patch queue

1. Abstract line 58: replace "theorem-level physical input" with "theorem-level protected-index input". Keep the K3 sigma-model theorem, but remove the immediate physics overclaim.

2. Abstract lines 100-110: replace "first-order protected operator/algebra" with "first-order protected algebraic/Pfaffian datum". Add "No operator with a spectrum is constructed."

3. Abstract lines 131-168: compress the compact realization paragraph. Move fine-grained `E_3`, HN, QME, and hybrid details to the compact source section; in the abstract state only the finite classes of missing data.

4. Introduction line 177: retitle "Introduction and claim strength" to "Claim strength and source-target separation" or move the status table before the physics prose.

5. Lines 180-186: replace "The local object comes first. A compact BPS theory..." with a no-overclaim formulation:
   "The determinant proof does not use a compact source. The compact source problem asks for protected local operations whose trace would have the displayed determinant."

6. Lines 226-258: keep the projection-to-`E` obstruction, but make the heading "Open compact and hybrid factorization problem".

7. Lines 260-296: keep the conditional recognition paragraph, but change "proved later" to "verified later as a certificate consequence". The proof is mostly "if the certificate exists, the named comparison follows".

8. Line 464: rename `The physical question` to `The compact source problem`. If "physical" remains, make it a paragraph label, not a section title.

9. Line 640: rename `The one-particle index and its determinant` to `The virtual K_0 determinant and its Borcherds product`.

10. Lines 667-738: keep `\mathcal H^{BPS}_{n,l}(S)` only for the K3 worldsheet protected cohomology. Do not let `BPS` attach to `\mathcal V`.

11. Lines 882-917: rename proposition to `Open Dirac--Pfaffian target specification`. Replace "operator/algebra" with "first-order algebraic/Pfaffian datum"; if "operator" remains, append "in the formal protected sense, not an analytic operator with a spectrum."

12. Lines 5743-5745: label rename needed when source edits are allowed. `\label{thm:factorization-square-root}` is lexically false for a proposition on the formal current envelope.

13. Lines 5770-5790: move a one-sentence compressed definition of the holomorphic `E_3` source interface into the opening before any `E_3` use.

14. Lines 6731 and 15952: audit `Canonical`. Retitle if the construction depends on supplied source data or branch choice.

15. Lines 14031-14201: in the synthesis theorem, replace "the virtual determinant is the theta-normalized Igusa square root" with "the virtual determinant is the theta-normalized Gritsenko--Nikulin product". Save "square root" for the Dirac/Pfaffian open problem.

16. Lines 14289-14336: consider `Row-host certificate` instead of `Physical-host certificate`. If "physical" stays, the first sentence must say "This is a certificate checklist, not a host construction."

## Residual editorial checks

1. Local caveat check: every occurrence of `physical`, `BPS`, `operator`, `one-particle`, `realization`, `recognition`, `E_3`, `Hall source`, `orientation`, `compact`, `canonical`, `proof`, `certificate`, `target`, and `scalar` in the first ten pages must be readable in isolation.

2. Theorem-strength check: for every theorem title, ask whether a hostile referee can say "the hypotheses already assume the conclusion". If yes, rename to `certificate`, `criterion`, `conditional consequence`, or `open problem`.

3. Scalar contamination check: no sentence may move from `Z^X_{OP/DT}=-4096 Delta_5^{-2}` to Pfaffian/orientation/compact source without an explicit "would require supplied data" clause.

4. Gram-charge check: no sentence may grade a Hall category directly by `(n,l,m)` unless it is after normal-ordered descent. Before descent, the grading is by the supplied additive formal/effective charge support.

5. Target/source check: any paragraph mentioning `\mathsf{Den}_{\Delta_5,E}`, `\mathfrak g_{\Delta_5}`, or the formal current envelope must state that it is target-internal unless a compact source comparison is explicitly supplied.

6. `E_3` check: every `E_3` occurrence must say whether it is a chosen holomorphic operadic model, a source interface, a formality/framing datum, or an open problem. No bare `E_3` rhetoric.

7. Orientation check: every orientation claim must name which level it is about: ordinary Joyce-Upmeier line, reduced quotient line, finite-stabilizer gerbe, Weyl-equivariant lift, local Pfaffian wall sign, or global Maass-character comparison.

8. Boundary-row check: every row promotion beyond automorphic product must name row, group/cover, character, seed, product lattice, scalar theorem if claimed, orientation data, charge lattice, and primitive comparison.

9. Standalone cold-reader check: print only pages 1-10 and mark each claim as `proved`, `computed`, `imported`, `conditional`, or `open`. If any sentence resists classification, rewrite.

10. Voice check: delete mission language. The final voice should read like a theorem ledger with physical motivation, not like an announcement of a compact physical theory.
