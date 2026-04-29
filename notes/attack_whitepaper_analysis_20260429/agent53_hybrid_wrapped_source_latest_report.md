# Agent53 hybrid wrapped source latest report

CONTROL: proposal-only hybrid local/wrapped source reviewer.  No source
edits.  Writable surface limited to this report.

Sources read:

- attack-heal skill:
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`
- attack-heal protocol:
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`
- latest raw PDF:
  `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`
  (`sha256 d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1`)
- latest extracted text:
  `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`
  (`sha256 c2035d6ce0f995ad41b16ad295d2bba1d110612385aea3a7d6197f8d1f7e5b17`)
- current manuscript:
  `main.tex`
  (`sha256 fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280`)
- prior local reports: Agent06, Agent16, Agent44, Agent45 in
  `notes/attack_whitepaper_analysis_20260429/`.

## Verdict

Stable core:

1. The projection-to-\(E\) support-locality obstruction is theorem-level:
   positive geometric elliptic degree projects onto all of \(E\), so an
   ordinary support-local object on \(\operatorname{Ran}(E)\) sees only the
   projection-finite sector.  Current anchors:
   `main.tex:7120-7200`.
2. A full Igusa compact source needs a hybrid local/wrapped finite
   correspondence system: local closed-configuration stacks, wrapped
   prequotients with anchors, LL/LW/WL/WW extension correspondences,
   eight two-step flag stacks, quotient-after-correspondence, protected
   integration, and HN transitions.  Current anchors:
   `main.tex:7202-7935`, `8338-8386`, `11896-11957`.
3. The \(\delta_2\) wall is the first decisive wrapped test because its
   type-II Gram label is \((0,1,1)\).  It cannot be supplied by the
   projection-finite Ran sector.  Current anchors:
   `main.tex:6247-6264`, `8255-8335`, `11056-11087`.

Destroyed claim:

The latest PDF's sentence "This is now an actual finite hybrid
local/wrapped source, not a certificate" at extracted lines
`29222-29244` is not true for the geometric \(K3\times E\) compact
source.  It constructs at most a universal finite colored algebraic
interface \(\mathsf{Hyb}_R\) with colors and BKM/product maps.  That is a
comparison target or presentation skeleton.  It does not construct the
geometric wrapped stacks, anchors, vanishing-cycle coefficient systems,
mixed Hall correspondences, quotient functor, protected trace, or
Pfaffian wall compatibility.

## The Central Degree Issue

The manuscript must separate two degree functions everywhere:

\[
m_R=\operatorname{pr}_3\overline\Pi_X
\]

is the Borcherds/Igusa \(s\)-exponent after normal-ordered Gram descent.

\[
b_R^{\mathrm{geom}}
\]

is the geometric elliptic curve-class degree deciding whether a sector is
projection-finite or wrapped.

The D6--D2--D0 dictionary proves

\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1)
\]

at `main.tex:2665-2701`.  Therefore, on the rank-one D6--D2--D0 branch,

\[
m_R=d-1,\qquad b_R^{\mathrm{geom}}=d=m_R+1.
\]

For the type-II wall

\[
\delta_2\leftrightarrow(0,1,1),
\]

the trace exponent is \(m_R(\delta_2)=1\).  If the object is read inside
the rank-one D6--D2--D0 curve-degree dictionary, its geometric elliptic
degree is \(b_R^{\mathrm{geom}}(\delta_2)=2\), not \(1\).  If the
manuscript wants \(b_R(\delta_2)=1\), then \(b_R\) is not geometric
elliptic degree; it is the Gram trace exponent and should be renamed
\(m_R\) or \(b_R^{\mathrm{trace}}\).

Current problematic anchors:

- `main.tex:6253-6254` says \(b_R(\delta_2)=1\).
- `main.tex:7764-7781` says monomials have \(s\)-degree \(b_R(\gamma)\)
  but displays \(s^{m_R(\gamma)}\).
- `main.tex:7790-7795`, `7816`, and `8097` use \(b_R\) as the \(s\)
  exponent.
- `main.tex:8276-8278` demands \(b_R(\eta)=1\) for the \(\delta_2\)
  wrapped object.
- `main.tex:11056-11087` repeats the same wrapped test.

Minimal repair: define \(m_R\) and \(b_R^{\mathrm{geom}}\) in the hybrid
definition, use \(b_R^{\mathrm{geom}}\) only for L/W sector color, and use
\(m_R\) only for \(s\)-degree.

## What Must Be Constructed

### 1. Projection-Finite Local Sector

Required geometric construction:

- finite HN window \(\Gamma_{\sigma,S}^{HN}(R)\);
- closed-support incidence stacks over \(E^I\);
- coefficient systems \(\Phi_{\alpha,R,I}^{\mathrm{loc}}\);
- orientation lines \(o_{\alpha,R,I}^{\mathrm{loc}}\);
- exceptional-pushforward/proper-support witnesses;
- recovery of open-support notation by restriction from the closed
  configuration atlas.

Current `main.tex:7257-7323` is the right interface.  It is not a proof
that the finite stacks exist.

### 2. Wrapped Sector

Required geometric construction:

- wrapped substacks
  \(\mathcal M_{\eta,R}^{\mathrm{wr}}\) for
  \(b_R^{\mathrm{geom}}(\eta)>0\);
- rigidified prequotients
  \(\mathcal M_{\eta,R}^{\mathrm{wr,rig}}\to
  \mathcal M_{\eta,R}^{\mathrm{wr}}\);
- an anchor retaining enough relative \(E\)-position for wrapped Hall
  correspondences;
- a proof of unit translation law or a declared finite cover/rigidifying
  replacement;
- losslessness for the Ext/correspondence data, not merely a
  determinant or finite divisor shadow;
- HN transition compatibility.

The determinant anchor

\[
\lambda(A)=\det Rp_{E,*}A\otimes\mathcal O_E(-\chi(A)0_E)
\in\operatorname{Pic}^0(E)\simeq E
\]

is a candidate.  Current `main.tex:7325-7412` correctly says it has
translation weight \(\chi(A)\) and is not automatically unit-weight or
lossless.

### 3. Mixed Hall Correspondences

Required geometric construction:

- LL correspondences;
- ordered LW correspondences;
- ordered WL correspondences;
- ordered WW correspondences;
- the two-sided mixed stacks with local inputs on both sides of the
  wrapped input;
- retention of input, intermediate, and output anchors before the reduced
  \(E\)-quotient;
- admissible \(p^*\), \(q_!\), Thom--Sebastiani transport, finite inertia,
  and proper-support/compact-support control.

Current `main.tex:7414-7589` is a good specification.  The universal PDF
operations

\[
L_\gamma\otimes W_{\eta,a}\to W_{\gamma+\eta,a+AJ_R(\gamma)},\qquad
W_{\gamma,a}\otimes L_\eta\to W_{\gamma+\eta,a+AJ_R(\eta)}
\]

at extracted lines `29180-29191` are color-level maps.  They do not
construct the geometric extension stacks or the Hall pull-push maps.

### 4. Eight Word Identities

Required geometric construction:

- for each word
  \[
  LLL,\ LLW,\ LWL,\ WLL,\ LWW,\ WLW,\ WWL,\ WWW,
  \]
  a two-step flag stack;
- comparison maps to both iterated correspondence fibre products;
- equality of pull-push maps after vanishing cycles, orientation signs,
  quotient by height \(>R\), and the reduced \(E\)-quotient comparison
  maps;
- four-input pentagon;
- higher colored configuration atlas, units, symmetry/order conventions,
  refinements, descent, and overlaps as a separate residual.

Current `main.tex:7591-7650` correctly states this.  The latest PDF's
argument at extracted lines `29208-29217` that all eight diagrams commute
strictly because degree addition and \(AJ_R\) are homomorphisms proves
only color-label associativity.  It does not prove equality of geometric
Hall operations.

### 5. Quotient-After-Correspondence

Required construction:

- \(Q_{E,R}\) as a functor on the finite correspondence/BM module
  category, not on object stacks alone;
- reduced correspondences \(\overline e\);
- comparison isomorphisms \(\theta^Q_{\mu,R}\);
- finite-stabilizer orientation-gerbe checks;
- compatibility with all flag \(2\)-morphisms and HN transitions.

Current `main.tex:7652-7715` is the right interface.  Quotient-first
forgets relative \(E\)-position and cannot recover mixed Hall
convolution.

### 6. Protected Integration

Required construction:

- chain-level character \(I_R^{\mathrm{prot}}\);
- compatibility with products, coproducts, primitives, colored
  refinements, quotient maps, and transitions;
- homogeneity for the full Gram label
  \(\overline\Pi_X(\gamma)=(n,l,m)\), hence trace degree \(s^{m_R}\);
- no substitution by a determinant-level Fock/Hecke scalar.

Current `main.tex:7717-7820` is correct in shape but should repair the
\(b_R\) vs. \(m_R\) language.

## What Is Only Interface

The following are interfaces or comparison targets unless supplied by the
geometric finite data above:

1. \(\operatorname{Ran}^{\mathrm{hyb}}(E)=\bigsqcup_b\operatorname{Ran}(E)_{[b]}\).
   This is a degree shadow.  It is not the hybrid category.
2. The latest PDF's \(\mathsf{Hyb}_R\) colored PROP
   (`29208-29244`).  It is a universal algebraic presentation, not a
   compact \(K3\times E\) Hall source.
3. The assignment \(F_R^{\mathrm{hyb}}(L_\gamma)=V_\gamma\) and
   \(F_R^{\mathrm{hyb}}(W_{\gamma,a})=V_\gamma\).  This is target-side
   vector-space bookkeeping unless \(V_\gamma\) is built from geometric
   vanishing-cycle BM chains on the local/wrapped stacks.
4. The BKM bracket/product maps used as the four binary operations.  They
   can test recognition; they do not construct the Hall correspondences.
5. The determinant anchor \(\lambda(A)\) by itself.  It is not lossless
   without the rigidification/unit-weight/multi-anchor/transition data.
6. The eight word list by itself.  It is only a table until the flag
   stacks and pull-push equalities are supplied.
7. A scalar Fock/Hecke factor.  It can reproduce determinant-level
   \(s\)-dependence; it cannot supply local-wrapped primitive brackets.

## Main.tex Changes Recommended

1. **Define the two degree maps at the start of the hybrid certificate.**

   Near `main.tex:7232-7255`, replace the single \(b_R\) role with:

   ```tex
   b_R^{\mathrm{geom}}:\Gamma_{\sigma,S}^{HN}(R)\to\mathbb Z_{\ge0},
   \qquad
   m_R=\operatorname{pr}_3\overline\Pi_X.
   ```

   Then set

   ```tex
   \Gamma_R^{\mathrm{loc}}=\{\alpha\mid b_R^{\mathrm{geom}}(\alpha)=0\},
   \qquad
   \Gamma_R^{\mathrm{wr}}=\{\eta\mid b_R^{\mathrm{geom}}(\eta)>0\}.
   ```

   State that \(m_R\) is additive in the normal-ordered source degree and
   determines \(s\)-exponents, while \(b_R^{\mathrm{geom}}\) determines
   local/wrapped support.

2. **Repair the \(\delta_2\) wrapped degree statements.**

   At `main.tex:6253-6254`, `8276-8278`, and `11056-11087`, replace
   "\(b_R(\delta_2)=1\)" with:

   ```tex
   m_R(\delta_2)=1,\qquad b_R^{\mathrm{geom}}(\delta_2)>0.
   ```

   If the sentence is explicitly in the rank-one D6--D2--D0 branch, add:

   ```tex
   b_R^{\mathrm{geom}}(\delta_2)=2
   ```

   by the dictionary \((h-1,n,d-1)\).

3. **Repair the protected integration exponents.**

   At `main.tex:7764-7781`, `7790-7795`, `7816`, and `8097`, use
   \(s^{m_R(\gamma)}\), not \(s^{b_R(\gamma)}\).  Add one sentence:

   "The wrapped color is controlled by \(b_R^{\mathrm{geom}}\); the
   automorphic monomial is controlled by \(m_R\).  On the rank-one
   D6--D2--D0 branch \(m_R=b_R^{\mathrm{geom}}-1\)."

4. **Do not import the latest PDF's \(\mathsf{Hyb}_R\) as a geometric
   construction.**

   If main.tex mentions it, introduce it only as
   \(\mathsf{Hyb}^{\mathrm{univ}}_R\): a finite algebraic comparison PROP
   whose representation is a target-side model.  Its realization theorem
   must require a functor from the geometric hybrid correspondence category
   \(\mathsf{Corr}^{E,\mathrm{hyb}}_R\) to
   \(\mathsf{Hyb}^{\mathrm{univ}}_R\) preserving LL/LW/WL/WW operations,
   eight flags, quotient-after-correspondence, protected integration, and
   HN transitions.

5. **Keep the current "certificate/open" posture.**

   The title
   `Finite hybrid local/wrapped factorization certificate` at
   `main.tex:7202` is safer than "construction."  The sentence
   `main.tex:7869-7871` saying the notation names an obstruction problem
   without \(\mathfrak O_{\mathrm{hyb},R}=0\) should remain.

6. **Add a short warning near the degree shadow.**

   After `main.tex:7150-7160`, add:

   ```tex
   This disjoint union is only the degree shadow of the hybrid base.
   It does not contain wrapped moduli, anchors, mixed extension stacks,
   quotient descent, or protected integration.
   ```

   The manuscript already says this elsewhere; local repetition prevents
   the latest PDF's \(\operatorname{Ran}(E)[b]\) shorthand from being read
   as the actual category.

7. **Make eight-word status explicit.**

   After `main.tex:7646-7650`, add:

   ```tex
   Degree-label associativity of a universal colored PROP is not a proof
   of this axiom; the axiom is equality of the two geometric pull-push
   operations over the supplied flag stack.
   ```

8. **Tighten final summary language.**

   At `main.tex:14249-14267`, keep the current checklist but change
   "protected integration with trace degree \(s^{m_R}\)" to explicitly say
   \(m_R\), not \(b_R^{\mathrm{geom}}\), supplies the \(s\)-exponent.

## Attack Ledger

```yaml
id: A53-01
severity: 2
status: valid
lens: degree separation
target: main.tex:6253-6254, 7764-7781, 8097, 8276-8278
claim: b_R is both geometric elliptic degree and Igusa s-exponent.
broken_step: D6--D2--D0 dictionary gives m=d-1, so geometric degree and trace exponent are shifted.
evidence_type: line_reference
evidence_ref: main.tex:2665-2701; extracted latest PDF:29084-29089
minimal_heal: introduce b_R^{geom} and m_R everywhere; delta_2 has m_R=1 and b_R^{geom}>0, equal to 2 in the rank-one D6--D2--D0 branch.
residual: decide whether any non-D6 branch uses a different geometric wrapped-degree convention.
```

```yaml
id: A53-02
severity: 2
status: valid
lens: source/interface firewall
target: extracted latest PDF:29222-29244
claim: universal Hyb_R with BKM operations is an actual finite hybrid local/wrapped source.
broken_step: it supplies colors and algebraic operations, not geometric local/wrapped stacks, anchors, correspondences, quotients, or protected integration.
evidence_type: unsupported
evidence_ref: main.tex:7202-7935; main.tex:8338-8386
minimal_heal: call it a universal algebraic comparison PROP only; require a geometric realization functor from Corr_R^{E,hyb}.
residual: none if main.tex does not import the overclaim.
```

```yaml
id: A53-03
severity: 2
status: valid
lens: eight-word associativity
target: extracted latest PDF:29208-29217
claim: the eight words commute strictly because degree addition and AJ_R are homomorphisms.
broken_step: color-label associativity does not prove equality of Hall pull-push maps over geometric two-step flag stacks.
evidence_type: proof_gap
evidence_ref: main.tex:7591-7650
minimal_heal: keep eight-word vanishing as geometric flag-stack axiom; add warning against color-only proof.
residual: actual flag stacks and pentagon remain open.
```

```yaml
id: A53-04
severity: 3
status: valid
lens: quotient locality
target: hybrid wrapped source
claim: quotienting by E or adding a scalar Fock/Hecke mode repairs positive s-degree.
broken_step: quotient-first loses relative E-position; scalar mode does not encode RHom(A,W), RHom(W,A), or mixed Hall brackets.
evidence_type: line_reference
evidence_ref: main.tex:7414-7589; main.tex:7652-7715; main.tex:8135-8179
minimal_heal: maintain quotient-after-correspondence and require mixed Hall correspondences before Q_{E,R}.
residual: construct the actual quotient functor and orientation descent.
```

## Bottom Line

Do not let the latest PDF's universal colored PROP replace the current
geometric certificate.  The manuscript should say:

- \(\operatorname{Ran}(E)\) locality proves only the projection-finite
  sector.
- The full \(s\)-direction needs wrapped geometry.
- The \(\delta_2\) test has \(m_R=1\) and positive geometric wrapped
  degree; in the rank-one D6--D2--D0 dictionary that geometric degree is
  \(2\).
- The hybrid source is constructed only after actual local/wrapped stacks,
  anchors, LL/LW/WL/WW correspondences, eight flag identities,
  quotient-after-correspondence, protected integration, and HN transitions
  are supplied.
- A universal \(\mathsf{Hyb}_R\) is useful as an interface or target
  comparison object, not as the compact \(K3\times E\) source.
