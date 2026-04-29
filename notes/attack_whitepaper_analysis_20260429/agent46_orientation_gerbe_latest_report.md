# Agent46 Orientation-Gerbe / \(H^{\mathrm{tw}}\) Latest Attack Report

CONTROL: proposal-only reviewer.  Writable path limited to this report.  No manuscript files edited.

Sources read:

- `AGENTS.md`, `CLAUDE.md`, `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`.
- `~/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`.
- `~/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md` because `references/protocol.md` is absent in this repo root.
- Latest trusted extracted analysis: `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`.
- Latest trusted raw PDF path was present: `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`.
- Prior synthesis requested at `notes/attack_whitepaper_analysis_20260429/INTEGRATED_DECISION_LEDGER.md` was not present in this checkout.  I used the available synthesis reports `agent39_final_synthesis_adversary_report.md`, `agent40_final_grep_gate_report.md`, `agent41_post_patch_gap_gate_report.md`, and the prior orientation passes `agent07_orientation_gerbe_report.md`, `agent29_orientation_htw_second_pass_report.md`.

Commands used for evidence:

```bash
rg -n "orientation|Orient|gerbe|H_tw|H_\{tw\}|Htw|O1\+|O1|O2|global quotient|quotient orientation|sign|spin|Pfaff|determinant|Dirac" materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt
rg -n -C 3 -i 'O1|O1\+|O2|orientation gerbe|square-root gerbe|H\^\{\\mathrm\{tw\}\}|Htw|quotient orientation|global orientation|Maass|epsilon_o|OP minus|4096|scalar.*orientation|finite stabilizer|Weyl.*orientation|Pfaffian wall' main.tex
rg --files | rg 'INTEGRATED_DECISION_LEDGER|DECISION_LEDGER|ledger|orientation|htw|H_tw|O1|O2'
```

## Verdict

No stable source-side orientation theorem exists yet.

The stable core is narrower:

1. The OP/DT scalar square is orientation-forgetful.
2. The Maass character \(\nu_{\Delta_5}\) is automorphic target data.
3. The Hall orientation character \(\epsilon_o\) exists only after O1, O1+, and O2 are constructed.
4. A square-root gerbe can be defined once the reduced determinant line \(K_{R,\hat c}\) is defined.
5. \(H^{\mathrm{tw}}\) is at most a proposed gerbe-twisted source interface until the finite stacks, gerbe-lifted correspondences, Thom-Sebastiani maps, anti-invariant sector, transitions, and primitive/radical data are constructed.

The current `main.tex` already contains many correct firewalls:

- `main.tex:100-115`: the scalar OP/DT branch is orientation-forgetful; compact orientation system, Weyl transport, and type-II wall atlas remain open.
- `main.tex:127-129`: \(4096\) and the OP minus sign do not fix character or compact orientation monodromy.
- `main.tex:970-1055`: O2 local data are not read from divisor order or Maass character.
- `main.tex:1181-1317`: O1 includes ordinary square-root, quotient gerbe classes, finite Borel classes, and degree-one finite-stabilizer characters.
- `main.tex:1320-1408`: O1+ names the projective Weyl cocycle \(c_o\), quotient torsor defects \(\omega_{i,\mathcal C}\), and the finite action groupoid issue.
- `main.tex:1411-1480`: O2 requires local wall charts, tangent/normal splitting, invariant unit, rank-one Pfaffian normal model, and component/boundary/overlap compatibility.
- `main.tex:1517-1526`: no Hall signs on chamber-permuting \(S_3\) reflections without a semidirect Hall action.
- `main.tex:1636-1678`: orientation technologies do not prove the reduced \(K3\times E\) quotient orientation or type-II Weyl lift.
- `main.tex:13955-14052`: constants are not orientation data.

The remaining danger is architectural: the latest 19:23 analysis proposes a gerbe-first construction strongly enough that it can be misread as already built.  This must be written as a construction target / conditional interface unless the manuscript actually supplies the missing source geometry.

## Latest-PDF Evidence

The 19:23 analysis is explicit about the desired gerbe-first replacement:

- `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:21564-21589`: move full O1/O1+/O2 to an appendix; construct the square-root gerbe; define twisted Hall states over it; global orientation is a section; define \(H^{\mathrm{tw}}_X\); O1 is the trivialization problem for \(H^{\mathrm{tw}}_X\).
- `...revision-1923.txt:21643-21649`: do not imply Joyce-Upmeier proves reduced \(E\)-quotient orientation; do not imply Borisov-Joyce CY4 orientation proves CY3 reduced quotient orientation; define O1+ as Weyl lift of the entire quotient-orientation package.
- `...revision-1923.txt:21657-21676`: Maass character does not kill \(c_o\); automorphic monodromy does not construct Hall monodromy; local Pfaffian wall charts must be independent of automorphic divisor; O2 must hold for component, boundary, and overlap strata.
- `...revision-1923.txt:21894-21917`: \(H^{\mathrm{tw}}_X\) is constructed over the orientation gerbe, and the compact realization theorem is the later comparison \(\Pi_{X,*}H^0\operatorname{Prim}(H^{\mathrm{tw}}_X)/\operatorname{Rad}\stackrel{?}{\simeq}\mathfrak g_{\Delta_5}\).  The question mark is load-bearing.
- `...revision-1923.txt:23243-23335`: the square-root gerbe \(\operatorname{Or}_{R,c}=\sqrt{K_{R,c}}\), tautological line, and lifted correspondence object are the replacement for assuming a global orientation.
- `...revision-1923.txt:23360-23373`: the twisted state space is Borel-Moore homology on \([\mathfrak M^{or}_{R,c}/E]\) with the tautological square-root line and \(\mu_2\)-anti-invariant sector.
- `...revision-1923.txt:26432-26538`: same gerbe-first construction repeated as a theorem-spine patch, with the warning that global orientation untwists the theory but is not needed to define the twisted source.
- `...revision-1923.txt:27228-27246`: OP/DT scalar branch is orientation-forgetful; \(-4096=(-1)_{\mathrm{OP}}\cdot64^2\) fixes neither automorphic reflection character nor Hall orientation monodromy.
- `...revision-1923.txt:27265-27343`: \(\epsilon_o=\nu_{\Delta_5}\) follows only if geometric orientation-gerbe transport supplies an honest action and local Pfaffian wall models give the three signs.
- `...revision-1923.txt:28956-29064`: algebraic finite model suggests a square-root gerbe and \(H^{\mathrm{tw}}\) before global orientation; for geometry the finite moduli stack must replace the point.
- `...revision-1923.txt:29955-30036`: the latest analysis claims the universal source repairs the missing orientation-gerbe-first theory, but for geometry says quotient orientation remains a realization constraint and OP scalar square does not construct orientation, Hall product, or primitives.

## Destroyed Claims

The following claims must not appear as theorem-level conclusions in the platonic ideal paper.

1. `O1/O1+/O2 construct the compact source.`

   False.  O1 is orientation/trivialization, O1+ is Weyl transport, O2 is local Pfaffian wall data.  They do not construct finite moduli stacks, exact-triangle correspondences, six-functor formalism, primitive representatives, PBW, radical quotient, or source-to-target comparison.  Current safe wording at `main.tex:1527-1541` still risks compression: it says under D0/O1/O1+/O2 the supplied first-order theory refines the determinant and has monodromy \(\nu_{\Delta_5}\).  It must keep “supplied” visible.

2. `The square-root gerbe alone constructs \(H^{\mathrm{tw}}\).`

   False.  The gerbe gives the base and tautological line.  \(H^{\mathrm{tw}}\) also requires finite-type stacks, coefficient complexes, \(E\)-quotient stack control, lifted correspondences, Thom-Sebastiani isomorphisms, product/coproduct, anti-invariant sector preservation, and transitions.  Latest analysis lines `23243-23373` define the gerbe and state space, but the missing hypotheses must be part of the definition, not hidden.

3. `A global orientation is the first orientation object.`

   False.  The first object is \(\operatorname{Or}_{R,\hat c}=\sqrt{K_{R,\hat c}}\).  A global orientation is a section/trivialization.  Current `main.tex:2476-2511` still begins with “Orientation line of the protected sector.”  It correctly says no such line is constructed, but the platonic paper should put the square-root gerbe before this definition.

4. `The reduced quotient orientation follows from known orientation literature.`

   False.  `main.tex:1643-1659` correctly says Joyce-Song/Joyce-Upmeier/Borisov-Joyce/Oh-Thomas supply technology and analogues, not the reduced \(K3\times E\) quotient orientation or type-II Weyl-equivariant lift.  Latest analysis lines `21643-21645` require preserving this.

5. `Finite-stabilizer triviality follows from an underlying fixed line.`

   False.  After degree-two gerbe null-trivialization, finite-stabilizer linearisations form an \(H^1(BE[N];\mathbb F_2)\)-torsor.  Current `main.tex:1222-1239`, `1256-1269`, `1307-1317`, and `12019-12047` are the right obstruction split.  The ideal paper needs a one-line example: an ordinary fixed line for \(\mathbb Z/2\) can still carry the sign character.

6. `The \(E[2]\) test proves all finite stabilizer descent.`

   False.  Current `main.tex:1270-1317` and `12030-12047` correctly state even \(N\ge4\) has two-primary classes with mixed coefficient \(A_{12}^{(N)}\) and residual \(H^1\) characters invisible to \(E[2]\).  Latest analysis lines `21624-21636` demand the same warning.

7. `The Maass character constructs the Hall orientation character.`

   False.  It gives target values.  It does not kill \(c_o\), \(\omega_{i,\mathcal C}\), finite characters, or quotient descent.  Current `main.tex:1438-1441`, `1512-1526`, `2923-2943`, and `12074-12085` are safe.

8. `Automorphic divisor order proves \(N_\delta^{\mathrm{Pf}}=1\).`

   False.  Divisor order is a target check.  O2 requires a local reduced Hall normal-mode calculation.  Current `main.tex:970-1055` and `1411-1480` are safe and should be preserved.

9. `The OP minus sign or \(-4096\) is a Pfaffian sign.`

   False.  Current `main.tex:13955-14052` is the correct firewall.  Latest analysis lines `27228-27246` require exactly this separation.

10. `A bare determinant-line square equality is a Pfaffian comparison.`

    False.  The comparison needs
    \[
    \iota_{\mathrm{aut}}:\mathscr L_{\mathrm{Pf},X}\xrightarrow{\sim}\mathcal L^5\otimes\nu_{\Delta_5}
    \]
    compatible with cusp trivialization and squaring.  Current `main.tex:1483-1499` states this correctly.  Any later equality to \(\Delta_5^2\) must be through \(\iota_{\mathrm{aut}}^{\otimes2}\), not a naked determinant-line assertion.

## Minimal Safe Patch Specifications

These are proposal-only patches.  Do not apply blindly; integrate by semantic rewrite.

### Patch A: Insert Gerbe-First Definitions Before `main.tex:2476`

Add before `\begin{definition}[Orientation line of the protected sector]`:

```tex
\begin{definition}[Square-root orientation gerbe and tautological Pfaffian line]
\label{def:square-root-orientation-gerbe}
Fix a finite HN height \(R\) and a normal-ordered charge \(\hat c\).  Suppose
\(\mathfrak M_{R,\hat c}\) is a finite-type reduced d-critical stack with
coefficient complex \(\Phi_{R,\hat c}\), reduced virtual
canonical/determinant line \(K_{R,\hat c}\), and an \(E\)-translation action
lifting to \(K_{R,\hat c}\).  Define the square-root gerbe
\[
\operatorname{Or}_{R,\hat c}:=\sqrt{K_{R,\hat c}}
\xrightarrow{\pi_{R,\hat c}}\mathfrak M_{R,\hat c}.
\]
Its objects over \(U\to\mathfrak M_{R,\hat c}\) are pairs
\((L,\phi)\), \(\phi:L^{\otimes2}\xrightarrow{\sim}K_{R,\hat c}|_U\).
The tautological line \(L^{1/2}_{R,\hat c}\) on
\(\operatorname{Or}_{R,\hat c}\) satisfies
\[
(L^{1/2}_{R,\hat c})^{\otimes2}\simeq \pi_{R,\hat c}^*K_{R,\hat c}.
\]
A global orientation is a section/trivialization of this gerbe.  It is not
part of the definition of the gerbe.
\end{definition}
```

### Patch B: Define \(H^{\mathrm{tw}}\) as a Conditional Twisted Object

Immediately after Patch A:

```tex
\begin{definition}[Gerbe-twisted protected state object]
\label{def:gerbe-twisted-protected-state}
Under the hypotheses of Definition~\ref{def:square-root-orientation-gerbe},
set
\[
\Phi^{or}_{R,\hat c}:=\pi_{R,\hat c}^*\Phi_{R,\hat c},
\qquad
H^{tw}_{R,\hat c}:=
H_*^{BM}\!\left(
[\operatorname{Or}_{R,\hat c}/E],
\Phi^{or}_{R,\hat c}\otimes L^{1/2}_{R,\hat c}
\right)_{\mu_2\text{-anti}} .
\]
The subscript means that the \(\mu_2\)-band acts by the sign character.
Let \(H^{tw}_R=\bigoplus_{\hat c}H^{tw}_{R,\hat c}\).
This object is gerbe-twisted.  An O1 trivialization identifies it with an
ordinary oriented Pfaffian state object only after quotient descent,
multiplicativity, finite-stabilizer characters, and transition coherences
have been supplied.
\end{definition}
```

### Patch C: Add Lifted Correspondence Warning

Add after Patch B or before the protected Hall integration criterion:

```tex
\begin{remark}[Gerbe-lifted correspondences are extra data]
For an extension correspondence
\[
\mathfrak M_{R,\hat c}\times\mathfrak M_{R,\hat c'}
\xleftarrow{p}
\mathfrak E_{R,\hat c,\hat c'}
\xrightarrow{q}
\mathfrak M_{R,\hat c\star\hat c'},
\]
the product on \(H^{tw}_R\) requires a lifted correspondence over the
square-root gerbes, a Thom--Sebastiani isomorphism for the tautological
Pfaffian lines, and two-step flag coherences.  If the gerbe
multiplicativity class is nonzero, the result remains a twisted
correspondence object and must not be identified with an ordinary oriented
Hall product.
\end{remark}
```

### Patch D: Rename Existing Orientation-Line Definition

Change the heading at `main.tex:2476`:

```tex
\begin{definition}[Global orientation trivialization of the protected sector]
```

Then add first sentence:

```tex
This is an O1 solution of the square-root gerbe problem of
Definition~\ref{def:square-root-orientation-gerbe}, not the first
orientation object.
```

### Patch E: Split the Overloaded Conditional Theorem

Replace the long theorem body around `main.tex:1139-1543` by shorter pieces:

1. `Definition: compact Dirac-Igusa datum` with D0/O1/O1+/O2 as supplied data.
2. `Proposition: Pfaffian-to-automorphic comparison` using \(\iota_{\mathrm{aut}}\).
3. `Theorem: OP scalar square is orientation-forgetting`, sourced only from OP/Oberdieck.
4. `Lemma: local Pfaffian wall sign after O1/O1+/O2`.
5. `Lemma: group-theoretic character extension after O1+`, concluding \(\epsilon_o=\nu_{\Delta_5}\) only after the Hall character exists.

This prevents the reader from reading O1/O1+/O2 as a source construction.

### Patch F: Add False-Implication Box

After the opening claim-status table, add:

```tex
\[
\Delta_5^2\not\Rightarrow \epsilon_o,\qquad
-4096\not\Rightarrow \text{Hall Pfaffian sign},\qquad
\nu_{\Delta_5}\not\Rightarrow [c_o]=0,\qquad
d_\delta^{aut}=1\not\Rightarrow N_\delta^{Pf}=1.
\]
```

Follow with one sentence:

```tex
The left sides are scalar or automorphic target data; the right sides are
reduced quotient-orientation, Weyl-transport, and local Hall/Pfaffian
calculations.
```

## Exact Definition/Proof Structure Required For The Platonic Paper

The ideal paper should use this order.

1. **Automorphic target.** Define \(\Delta_5\), \(D_5=64^{-1}\Delta_5\), \(\nu_{\Delta_5}\), the diagonal divisor, and the Gritsenko-Nikulin denominator algebra.  Status: imported/proved target.

2. **Scalar square.** State OP/Oberdieck scalar theorem \(Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}\).  Status: imported scalar theorem.  Add constants-not-orientation firewall.

3. **Normal-ordered charge descent.** State the proved Gram/normal-ordering package.  Status: proved finite/lattice side where actually shown.

4. **Source preconditions.** Define finite stacks \(\mathfrak M_{R,\hat c}\), extension stacks, flag stacks, coefficient complexes, determinant lines, \(E\)-actions, and finite inertia.  Status: open/conditional unless constructed.

5. **Gerbe first.** Define \(\operatorname{Or}_{R,\hat c}=\sqrt{K_{R,\hat c}}\), \(L^{1/2}_{R,\hat c}\), \(\mu_2\)-band, and global orientation as section/trivialization.  Status: definition once \(K_{R,\hat c}\) exists.

6. **Twisted states.** Define \(H^{tw}_{R,\hat c}\) over \([\operatorname{Or}_{R,\hat c}/E]\), with \(\mu_2\)-anti-invariant sector.  Status: conditional on finite geometry and six-functor formalism.

7. **Gerbe-lifted correspondences.** Define lifted extension/flag correspondences and Thom-Sebastiani maps.  State associativity/coassociativity as coherences, not as automatic.  Status: open unless proved.

8. **O1.** Define the ordinary orientation/trivialization package:
   \(\alpha^{red}=0\), \(\alpha^{E,free}=0\), \(\widetilde\beta^{E,N}=0\), \(\lambda^{E,N}=0\), extension/flag/HN coherences.  Status: open on reduced \(K3\times E\).

9. **O1+.** Define Weyl transport of the whole quotient-orientation package:
   finite action groupoids \(\mathcal G_R\), \(c_{o,R}\), \([c_o]\), generator normalizations \(\tau_i^2=1\), and quotient torsor defects \(\omega_{i,\mathcal C}\).  Status: open.

10. **O2.** Define local Pfaffian wall charts: \(s_\delta(u_\delta)=-u_\delta\), tangent/normal splitting, invariant unit, \(N_{\delta_i}^{Pf}=1\), component/boundary/overlap/hybrid compatibility.  Status: open.

11. **Hall character theorem.** After O1/O1+/O2, prove local signs define a character \(\epsilon_o\) and compare to \(\nu_{\Delta_5}\) on \(W^{(2)}(\Lambda_{II}^{2,1})\).  Status: conditional.

12. **Recognition.** Only after \(H^{tw}\), product/coproduct, primitives, normal-ordered pushforward, radical quotient, PBW/no-extra-relations, transitions, and \(\iota_{\mathrm{aut}}\), state the compact comparison
   \[
   \overline\Pi_{X,*}H^0\operatorname{Prim}(H^{tw}_{X,\Gamma})/\overline{\operatorname{Rad}}
   \stackrel{?}{\simeq}\mathfrak g_{\Delta_5}.
   \]
   Status: open/conditional until proved.

## Attack Ledger

```yaml
- id: A46-01
  severity: 1
  status: valid
  lens: orientation-gerbe/source-construction
  target: main.tex:2476-2511; revision-1923.txt:21564-21589,23243-23335
  claim: "The orientation line is the first protected-sector orientation object."
  broken_step: "The first object should be the square-root gerbe; a global line is an O1 trivialization."
  evidence_type: line_reference
  evidence_ref: "main.tex:2476-2511 starts from a global line; revision-1923.txt:21567-21589 requires gerbe first."
  files_read: ["main.tex", "materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt"]
  tools_used: ["rg", "nl -ba", "sed"]
  confidence: high
  blast_radius: "Reader may infer O1 before the gerbe/trivialization problem is stated."
  minimal_heal: "Insert square-root gerbe and Htw definitions before the global orientation-line definition; rename existing definition as global orientation trivialization."
  residual: "Need actual finite determinant line K_{R,c} and finite source stacks."
  deciding_evidence: "Manuscript supplies K_{R,c}, Or_{R,c}, L^{1/2}, quotient stacks, and lifted correspondences before global orientation."

- id: A46-02
  severity: 1
  status: valid
  lens: Htw construction
  target: revision-1923.txt:21894-21917,23360-23373,26432-26538
  claim: "Htw is constructed once the orientation gerbe is named."
  broken_step: "A twisted Hall object also needs finite stacks, coefficient complexes, E-quotient control, lifted correspondences, Thom-Sebastiani maps, anti-invariant sector preservation, and transitions."
  evidence_type: proof_gap
  evidence_ref: "revision-1923.txt:23360-23373 gives state formula; lines 21894-21917 put recognition as later comparison with question mark."
  files_read: ["materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt", "main.tex"]
  tools_used: ["rg", "nl -ba"]
  confidence: high
  blast_radius: "Turns a construction target into an unproved Hall algebra theorem."
  minimal_heal: "Define Htw only under explicit hypotheses; mark product/coproduct and associativity as conditional on lifted gerbe correspondences."
  residual: "No source-side proof of finite correspondences and six-functor formalism."
  deciding_evidence: "Finite construction of Hpre/Htw with lifted exact-triangle and flag stacks, TS maps, anti-invariant product preservation, and transition compatibility."

- id: A46-03
  severity: 1
  status: valid
  lens: quotient orientation
  target: main.tex:1181-1317; main.tex:12019-12047; revision-1923.txt:21624-21636
  claim: "E[2] or ordinary line invariance closes quotient orientation."
  broken_step: "Degree-two gerbe classes and degree-one linearization characters are distinct; even N>=4 has mixed two-primary classes invisible to E[2]."
  evidence_type: line_reference
  evidence_ref: "main.tex:1222-1239,1256-1269,1270-1317; revision-1923.txt:21624-21636."
  files_read: ["main.tex", "materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt"]
  tools_used: ["rg", "nl -ba"]
  confidence: high
  blast_radius: "False quotient descent; fake O1."
  minimal_heal: "Keep O1 as full tuple alpha_red, alpha_E_free, beta_tilde^{E,N}, lambda^{E,N}, extension/flag/HN coherences; add fixed-line/sign-character warning example."
  residual: "Actual computations of all classes on all strata."
  deciding_evidence: "Cohomology computations and vanishing proofs for every finite stabilizer stratum used by the Hall source."

- id: A46-04
  severity: 1
  status: valid
  lens: Weyl transport
  target: main.tex:1320-1408; revision-1923.txt:21648-21663,27265-27343
  claim: "Maass character or three automorphic signs give Hall orientation character."
  broken_step: "O1+ requires an honest action on the full quotient-orientation package; Maass data does not kill c_o or omega defects."
  evidence_type: line_reference
  evidence_ref: "main.tex:1327-1358 and 1384-1408; revision-1923.txt:21657-21663."
  files_read: ["main.tex", "materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt"]
  tools_used: ["rg", "nl -ba"]
  confidence: high
  blast_radius: "Identifies target automorphic character with unconstructed Hall monodromy."
  minimal_heal: "State epsilon_o only after O1+ supplies c_o=delta a, tau_i^2=1, omega=0, and transition-compatible finite action groupoids."
  residual: "Construct Weyl lifts and compute c_o/omega."
  deciding_evidence: "A finite-to-global Weyl action on oriented quotient strata with explicit vanishing cocycles."

- id: A46-05
  severity: 1
  status: valid
  lens: O2 local signs
  target: main.tex:970-1055,1411-1480; revision-1923.txt:21669-21676
  claim: "Automorphic divisor order proves the local Pfaffian wall sign."
  broken_step: "O2 requires local d-critical charts, tangent/normal splitting, invariant unit, and rank-one normal mode on component/boundary/overlap strata."
  evidence_type: line_reference
  evidence_ref: "main.tex:973-1055 and 1438-1480; revision-1923.txt:21669-21676."
  files_read: ["main.tex", "materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt"]
  tools_used: ["rg", "nl -ba"]
  confidence: high
  blast_radius: "Replaces a local Hall calculation by automorphic target data."
  minimal_heal: "Keep divisor order as target check only; O2 theorem conditional on supplied local charts and N_delta^Pf=1."
  residual: "Construct charts and compute normal rank for all three type-II walls, including hybrid/wrapped middle wall."
  deciding_evidence: "Explicit reduced self-Ext normal complexes and Pfaffian units proving N_delta_i^Pf=1."

- id: A46-06
  severity: 2
  status: valid
  lens: scalar-sign firewall
  target: main.tex:13955-14052; revision-1923.txt:27228-27246,30028-30036
  claim: "OP scalar square, OP minus sign, or 4096 supplies orientation."
  broken_step: "Scalar square kills signs; OP minus is scalar convention; 4096 is theta-leading normalization."
  evidence_type: line_reference
  evidence_ref: "main.tex:13966-14052; revision-1923.txt:27228-27246 and 30028-30036."
  files_read: ["main.tex", "materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt"]
  tools_used: ["rg", "nl -ba"]
  confidence: high
  blast_radius: "False proof of square root from scalar branch."
  minimal_heal: "Preserve constants-not-orientation section; add false-implication box near opening."
  residual: "None if firewall remains."
  deciding_evidence: "Zero grep hits for scalar-to-orientation implication after rewrite."

- id: A46-07
  severity: 2
  status: valid
  lens: theorem architecture
  target: main.tex:1139-1543
  claim: "One theorem can carry Pfaffian comparison, scalar square, O1/O1+/O2, local signs, and character equality without overclaim."
  broken_step: "The theorem is semantically overloaded; it encourages reading supplied data as constructed data."
  evidence_type: proof_gap
  evidence_ref: "agent29 report and revision-1923.txt:21564-21589 demand moving full O1/O1+/O2 to appendix and defining Htw first."
  files_read: ["main.tex", "notes/attack_whitepaper_analysis_20260429/agent29_orientation_htw_second_pass_report.md", "materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt"]
  tools_used: ["rg", "sed", "nl -ba"]
  confidence: medium
  blast_radius: "Claim-status ambiguity across the main theorem spine."
  minimal_heal: "Split into compact datum definition, Pfaffian comparison proposition, scalar-square theorem, local-sign lemma, and group-character lemma."
  residual: "Editorial rewrite and cross-reference cleanup."
  deciding_evidence: "Reader-visible theorem labels match proof status; no supplied data is titled as constructed."

- id: A46-08
  severity: 2
  status: valid
  lens: Pfaffian comparison
  target: main.tex:1483-1499; agent29 lines 574-581
  claim: "A determinant-line square equality directly gives the Pfaffian-to-automorphic comparison."
  broken_step: "Need explicit iota_aut compatible with cusp trivialization and squaring."
  evidence_type: line_reference
  evidence_ref: "main.tex:1483-1499 already states iota_aut; prior orientation pass flags naked determinant equality as unsafe."
  files_read: ["main.tex", "notes/attack_whitepaper_analysis_20260429/agent29_orientation_htw_second_pass_report.md"]
  tools_used: ["nl -ba", "sed"]
  confidence: medium
  blast_radius: "Conflates formal product equality with line-bundle/Pfaffian comparison."
  minimal_heal: "Route every squared comparison through iota_aut^{otimes2}; never write bare det RHom = Delta_5^2."
  residual: "Construct or assume iota_aut precisely."
  deciding_evidence: "A defined Pfaffian line and automorphic line isomorphism with square compatibility."
```

## Verification Still Needed

Run these after any manuscript rewrite:

```bash
rg -n -i '4096.*proves.*orientation|64.*proves.*orientation|scalar.*proves.*orientation|scalar.*constructs.*orientation|OP.*sign.*is.*orientation|OP.*minus.*is.*orientation|Delta_5\^2.*orientation character|D_5\^2.*orientation character' main.tex
rg -n -i 'Maass.*constructs.*orientation|automorphic.*constructs.*Hall|divisor order.*Pfaffian rank|d_\\delta.*N_\\delta|nu_\\{\\Delta_5\\}.*c_o|nu_\\{\\Delta_5\\}.*omega' main.tex
rg -n -i 'H\\^\\{tw\\}|Htw|orientation-gerbe-twisted|square-root gerbe|tautological.*Pfaffian|mu_2.*anti' main.tex
rg -n -i 'global orientation.*required.*define.*H\\^\\{tw\\}|orientation line.*constructs.*H\\^\\{tw\\}|O1.*constructs.*source|O1\\+.*constructs.*source|O2.*constructs.*source' main.tex
```

Expected:

- first two commands: zero hits, except negative/firewall statements;
- third command: positive hits after the gerbe-first definitions are inserted;
- fourth command: zero hits, except explicit false-implication warnings.

No edits were made to `main.tex`, `proj.bib`, generated PDFs, or any manuscript file.
