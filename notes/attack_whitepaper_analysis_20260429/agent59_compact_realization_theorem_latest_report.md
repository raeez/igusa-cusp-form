# Agent59 Compact Realization Theorem Latest Report

Date: 2026-04-29.

Role: proposal-only compact-realization theorem reviewer.  No manuscript
source edited.  Writable surface limited to this report.

Sources read:

- `AGENTS.md`, `CLAUDE.md`.
- Attack-heal skill:
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`.
- Attack-heal protocol:
  `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`.
- Latest attack analysis extraction:
  `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`.
- Live manuscript: `main.tex`.
- Local second-wave reports: `INTEGRATED_DECISION_LEDGER.md`, Agent43,
  Agent48, Agent49, Agent50, Agent51, Agent52, Agent53, Agent54, Agent55.

## Verdict

Stable core:

1. Introduce a finite target/reference tower only as a target-derived
   Borcherds--Kac / Gritsenko--Nikulin object.
2. Define compact \(K3\times E\) geometry as a separate finite source
   domain, not as the target tower.
3. Define the comparison as a realization functor
   \[
   \mathsf{Real}_{X,R}:
   \mathfrak H^{\mathrm{geom}}_{X,R}
   \longrightarrow
   \mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}.
   \]
4. State the compact Igusa theorem only as a conditional proposition:
   if the finite geometric source and realization functor exist and
   preserve the listed structures, then the geometric Pfaffian pulls back
   the normalized target/reference Pfaffian and equals \(\Delta_5\).
5. State the construction of \(\mathfrak H^{\mathrm{geom}}_{X,R}\) and
   \(\mathsf{Real}_{X,R}\) as an open problem.

Destroyed claim:

The latest PDF's "universal finite Dirac--Igusa Hall source" language is
unsafe.  Its displayed object is built from
\(\mathfrak g_{\Delta_5}\), \(U(\mathfrak g_{\Delta_5})\), the BKM
bracket, target PBW, target radical quotient, and GN signed
multiplicities (`revision-1923.txt:29390-29732`).  That is a target
reference tower.  It is not a compact \(K3\times E\) Hall source.

## Safest Names

Use these names if the target tower is added:

\[
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}
\]

for the finite Dirac--Igusa target reference tower at height \(R\), and

\[
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L}
=\{\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}\}_R
\]

for the compatible tower/pro-object.  The superscript
\(\mathrm{ref}\) is load-bearing: it says the object is target-derived
reference data, not compact source geometry.

Use

\[
\mathfrak H^{\mathrm{geom}}_{X,R}
\]

for the finite geometric source domain at HN height \(R\), and

\[
\mathfrak H^{\mathrm{geom}}_X
=\varprojlim_R \mathfrak H^{\mathrm{geom}}_{X,R}
\]

only after transition maps and the finite-slice Mittag--Leffler condition
are supplied.

Use

\[
\mathsf{Real}_{X,R}
\]

for the finite realization functor.  Do not use \(R_X\): `main.tex`
already uses \(R_X\) for primitive recognition in the certificate
(`main.tex:12240-12256`).  Do not use \(H_X^{\mathrm{geom}}\): `main.tex`
already uses \(H_X\) for the hybrid-interface certificate slot
(`main.tex:11933-11995`) and \(\mathcal H_X\) for the oriented Hall object
(`main.tex:11996-12023`).

## Target Reference Tower

The target tower may be a theorem/proposition, because it imports known
target data.  It must not be called compact geometry.

Safe TeX:

```tex
\begin{definition}[Finite Dirac--Igusa target reference tower]
Fix a finite downward-saturated active window \(A_R\subset
\Gamma_{\mathrm{gram}}\) and a bookkeeping lift
\(s_L:A_R\to\widehat\Gamma_X\).  Let
\[
\mathfrak g^{\mathrm{ref}}_{\Delta_5,R}
:=\bigoplus_{\gamma\in A_R}
\mathfrak g_{\Delta_5,\alpha(\gamma)}
\]
with the Borcherds--Kac bracket, the Gritsenko--Nikulin parity spaces,
and the standard invariant form, all imported from the denominator
algebra.  Let
\[
\mathsf U^{\mathrm{PBW}}_{\Delta_5,R}
\subset U(\mathfrak g_{\Delta_5})
\]
be the finite PBW span of monomials whose total Gram degree lies in
\(A_R\), with products landing in larger windows in the tower sense.
The finite Dirac--Igusa target reference tower
\(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}\) is the package
\[
\bigl(
A_R,\ s_L,\ \mathfrak g^{\mathrm{ref}}_{\Delta_5,R},\
\mathsf U^{\mathrm{PBW}}_{\Delta_5,R},\
\langle\, ,\,\rangle_{\mathrm{GN}},\
\operatorname{Rad}_{\mathrm{GN}},\
\mathsf H^{\mathrm{hyb,ref}}_R,\
C^{\mathrm{ref}}_R,\
\mathfrak D^{\mathrm{ref}}_R,\
\operatorname{pf}^{\mathrm{ref}}_R
\bigr),
\]
where the hybrid, coalgebra, Dirac, and Pfaffian entries are formal
target-reference structures seeded by
\(\mathfrak g_{\Delta_5}\).  This tower is not a compact
\(K3\times E\) Hall source.
\end{definition}
```

Safe target-side proposition:

```tex
\begin{proposition}[Target reference normalization]
For the target reference tower
\(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L}\), after the stated
finite-window Pfaffian convention and the Weyl cusp normalization,
\[
\operatorname{pf}^{\mathrm{ref}}
\bigl(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L}\bigr)
=\Delta_5 .
\]
This is the Borcherds--Gritsenko--Nikulin product formula expressed in
the target reference tower.  It constructs no compact Hall source, no
geometric orientation gerbe, no compact primitive representatives, no
source coalgebra, and no geometric Pfaffian line.
\end{proposition}
```

## Finite Geometric Source Domain

A finite geometric source domain is not just a category.  It is a finite
Hall--Dirac source datum at height \(R\), with enough structure for the
realization functor to test product, coproduct, orientation, primitive,
coalgebra, Pfaffian, and transition compatibility.

Safe TeX:

```tex
\begin{definition}[Finite compact geometric source domain]
Let \(X=S\times E\).  A finite compact geometric source domain at height
\(R\) is a datum
\[
\mathfrak H^{\mathrm{geom}}_{X,R}
=\bigl(
\mathfrak M^\sigma_{X,R},\
\mathsf{Corr}^{\mathrm{Hall}}_{X,R},\
\widehat\Gamma_{X,R},\
\overline\Pi_{X,R},\
\mathcal O^{\mathrm{or}}_{X,R},\
\mathsf{Corr}^{E,\mathrm{hyb}}_{X,R},\
\mathcal F^{\mathrm{hyb}}_{X,R},\
C_{X,R},\
P^{\Pi,\mathrm{red}}_{X,R},\
\mathfrak D_{X,R},\
\mathscr L_{\mathrm{Pf},X,R},\
\rho^{\mathrm{geom}}_{R^+R}
\bigr)
\]
consisting of finite-type compactly supported \(B\)-brane Hall substacks
on \(X\), exact-triangle and collision correspondences, the
normal-ordered charge extension and descended Gram degree, determinant
square-root gerbes and quotient orientation data, hybrid local/wrapped
correspondences over \(E\), a source chiral coalgebra, descended protected
primitive spaces with pairing/radical/PBW data, first-order Dirac blocks,
Pfaffian lines with cusp trivializations, and successor transition maps.
The pro-domain
\(\mathfrak H_X^{\mathrm{geom}}\) exists only after these finite data are
compatible in \(R\) and satisfy the finite-slice Mittag--Leffler
condition.
\end{definition}
```

This definition should remain a definition of required data, not an
existence theorem.  It is intentionally source-side: none of its
geometric entries may be defined by the target-internal bar--cobar
counit or by setting primitives equal to
\(\mathfrak g_{\Delta_5}\).

## Realization Functor

The safest signature is:

```tex
\[
\mathsf{Real}_{X,R}:
\mathfrak H^{\mathrm{geom}}_{X,R}
\longrightarrow
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}.
\]
```

It should be described as a morphism of finite Hall--Dirac data, not as
an ordinary functor between two unspecified categories.  The pro-version
is:

```tex
\[
\mathsf{Real}_{X}:
\mathfrak H^{\mathrm{geom}}_{X}
\longrightarrow
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L},
\qquad
\mathsf{Real}_{X}\rho^{\mathrm{geom}}_{R^+R}
=
\rho^{\mathrm{ref}}_{R^+R}\mathsf{Real}_{X,R^+}.
\]
```

## Required Preservation Clauses

The realization definition should require the following clauses.  These
are not optional polish; without them the conditional theorem does not
pull the target reference identity back to compact geometry.

Safe TeX:

```tex
\begin{definition}[Dirac--Igusa realization functor]
Assume that \(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}\) has been
defined.  A finite Dirac--Igusa realization of \(X=S\times E\) at height
\(R\) is a finite compact geometric source domain
\(\mathfrak H^{\mathrm{geom}}_{X,R}\) together with a morphism of finite
Hall--Dirac data
\[
\mathsf{Real}_{X,R}:
\mathfrak H^{\mathrm{geom}}_{X,R}
\longrightarrow
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}
\]
satisfying the following conditions.
\begin{enumerate}
\item[\textup{(Real-1)}] It preserves the finite normal-ordered charge
labels: the source labels in \(\widehat\Gamma_{X,R}\) descend by
\(\overline\Pi_{X,R}\) to the target window \(A_R\), and the target
monomial \(q^nr^ls^m\) is attached to
\(\gamma=(n,l,m)=\overline\Pi_{X,R}(\widehat c)\).  The raw quadratic
map \(\Pi_X\) is not used as an additive bracket grading.

\item[\textup{(Real-2)}] It sends source Hall extension
correspondences, with their proper/admissible pull-push maps and
Thom--Sebastiani orientation transport, to the target reference product,
including two-step flag coherences.

\item[\textup{(Real-3)}] It sends source collision/decomposition
correspondences to the target reference coproduct and preserves the
Frobenius/Hopf adjointness pairing.

\item[\textup{(Real-4)}] It sends compact protected primitives to the
target primitive spaces, preserving Cartan data, simple-root
representatives, positive and negative representatives, parity splits,
the Borcherds--Kac relations, full parity dimensions, and the primitive
bracket.

\item[\textup{(Real-5)}] It preserves the completed Hopf pairing,
radical kernels, Lie-ideal and coideal conditions, radical quotient,
PBW filtration, and no-extra-relations comparison in finite windows.

\item[\textup{(Real-6)}] It preserves determinant square-root gerbes,
orientation twists, quotient finite-stabilizer data, Weyl lifts,
type-II wall signs, and the induced orientation character whenever that
character is defined geometrically.

\item[\textup{(Real-7)}] It sends local/wrapped geometric operations to
the target hybrid reference operations, preserving projection-finite
local sectors, wrapped sectors with anchors, LL/LW/WL/WW operations,
the eight two-step word coherences, quotient-after-correspondence, and
protected integration.  The geometric wrapped degree
\(b_R^{\mathrm{geom}}\) remains distinct from the trace exponent
\[
m_R=\operatorname{pr}_3\overline\Pi_{X,R}.
\]

\item[\textup{(Real-8)}] It sends the source chiral coalgebra
\[
C_{X,R}
\]
with finite filtration, collision coproduct, bar comparison, and cobar
map to the target reference coalgebra.  This clause requires
\(C_{X,R}\) to be source-supplied; the target-internal bar--cobar
counit does not define it.

\item[\textup{(Real-9)}] It intertwines finite first-order Dirac blocks
and preserves Pfaffian lines, Pfaffian square-root torsors, compact
parity lifts, and the leading cusp trivialization.  The scalar OP square
and the target super-Pfaffian product are not substitutes for this
geometric line comparison.

\item[\textup{(Real-10)}] It is compatible with successor transitions
\(R^+\to R\), including products landing in larger windows, radicals,
PBW filtrations, coalgebras, orientation data, Pfaffian lines, and the
finite-slice Mittag--Leffler condition.
\end{enumerate}
\end{definition}
```

## Conditional Theorem

This is the strongest safe compact theorem after the target reference
tower is introduced:

```tex
\begin{proposition}[Conditional compact Dirac--Igusa realization]
Assume that the target reference tower
\(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L}\) is defined and satisfies
\[
\operatorname{pf}^{\mathrm{ref}}
\bigl(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L}\bigr)
=\Delta_5 .
\]
If \(X=S\times E\) admits a compatible pro-realization
\[
\mathsf{Real}_{X}:
\mathfrak H^{\mathrm{geom}}_{X}
\longrightarrow
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L}
\]
in the sense of Definition~\textup{...}, then the realized compact
Pfaffian line has normalized section
\[
\operatorname{pf}^{\mathrm{geom}}_X=\Delta_5 .
\]
\end{proposition}

\begin{proof}
The target equality is the Borcherds--Gritsenko--Nikulin product written
in the target reference tower.  By the realization hypotheses,
\(\mathsf{Real}_X\) preserves the normal-ordered degree, Hall product and
coproduct, primitive comparison, radical/PBW quotient, orientation
gerbe, source coalgebra, first-order Dirac blocks, Pfaffian line, and
leading cusp trivialization.  Therefore the normalized target Pfaffian
section pulls back to the normalized geometric Pfaffian section.  The
result is conditional on the existence of the source domain and the
realization functor; no compact source construction is inferred from the
target identity.
\end{proof}
```

Do not label this as "the compact realization theorem" unless the word
"conditional" is in the theorem title or the hypotheses are impossible to
miss.  Without the hypotheses it overclaims.

## Open Problem Structure

The open problem should follow the conditional proposition and be the
place where the geometric burden is visible.

Safe TeX:

```tex
\begin{openproblem}[Compact realization of the target reference tower]
Construct a compatible system of finite compact geometric source domains
\[
\mathfrak H^{\mathrm{geom}}_{X,R}
\]
and realization morphisms
\[
\mathsf{Real}_{X,R}:
\mathfrak H^{\mathrm{geom}}_{X,R}
\longrightarrow
\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}
\]
satisfying \textup{(Real-1)--(Real-10)} for all finite heights \(R\),
with transition compatibility and the finite-slice Mittag--Leffler
condition.  Equivalently, construct the compact Hall source, orientation
gerbe, hybrid local/wrapped correspondence atlas, source coalgebra,
primitive recognition data, first-order Pfaffian line, and transition
system needed to realize the target reference tower.
\end{openproblem}
```

Then list the open clauses:

```tex
\begin{enumerate}
\item[\textup{(Open-G1)}] finite compact Hall substacks, extension
correspondences, pull-push maps, and two-step Hall flag coherences;
\item[\textup{(Open-G2)}] determinant square-root gerbes, quotient
finite-stabilizer orientation data, Weyl lifts, and type-II wall signs;
\item[\textup{(Open-G3)}] hybrid local/wrapped source data over \(E\),
including anchors, LL/LW/WL/WW operations, eight two-step word
coherences, quotient-after-correspondence, and protected integration;
\item[\textup{(Open-G4)}] source chiral coalgebras \(C_{X,R}\), finite
conilpotent filtrations, collision coproducts, bar comparisons, cobar
quasi-isomorphisms, and source/target separation;
\item[\textup{(Open-G5)}] compact primitive representatives, full
parity dimensions, Hall bracket constants, Borcherds--Kac relation
checks, positive-negative Hopf pairing matrices, radical ideal/coideal
checks, no-extra-relations, and finite PBW comparison;
\item[\textup{(Open-G6)}] geometric first-order Dirac blocks,
Pfaffian square-root lines, compact parity lifts, and leading cusp
trivializations;
\item[\textup{(Open-G7)}] transition maps \(R^+\to R\), strict
compatibility of radicals, PBW filtrations, source coalgebras,
orientation data, Pfaffian lines, and the finite-slice
Mittag--Leffler exactness condition.
\end{enumerate}
```

These clauses should remain open until source-side objects, maps, and
finite matrices exist in the repository.  Target PBW, target radical
quotient, target primitive bracket, and target Pfaffian normalization may
be theorem-level inside \(\mathsf{TDI}^{\mathrm{ref}}\), but they do not
close any `Open-G*` clause.

## Source/Target Overclaim Warnings

Use these as hard manuscript guardrails.

Forbidden:

```tex
We construct the compact finite Hall--Dirac source
\(\mathsf{UDI}_{\Delta_5,E,L}\).
```

Safe:

```tex
We construct a target-derived finite Dirac--Igusa reference tower
\(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}\).  A compact
\(K3\times E\) source must still realize this tower through
\(\mathsf{Real}_{X,R}\).
```

Forbidden:

```tex
The source coalgebra is
\(C_R=\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E})\).
```

Safe:

```tex
The target-internal bar--cobar counit reconstructs only the target
observable algebra.  A compact realization must supply a source coalgebra
\(C_{X,R}\) and a separate comparison
\[
\Theta_{\mathrm{Kos},R}:
\Omega_E^{\mathrm{ch}}C_{X,R}
\longrightarrow
\mathsf{Den}_{\Delta_5,E,\le R}.
\]
```

Forbidden:

```tex
PBW and the radical quotient hold for the compact source because
\(H_R=U(\mathfrak g_{\Delta_5})_{\le R}\).
```

Safe:

```tex
PBW and the standard radical quotient hold in the target reference tower
because they are inherited from the imported Borcherds--Kac/Kac
presentation.  Compact PBW and compact radical compatibility remain
source-side realization conditions.
```

Forbidden:

```tex
The universal orientation is trivial, hence the geometric quotient
orientation is solved.
```

Safe:

```tex
A formal target-reference orientation convention carries no quotient
orientation content.  The geometric realization must compute determinant
square-root gerbes, finite-stabilizer Borel classes, Weyl cocycles, and
type-II wall signs.
```

Forbidden:

```tex
\operatorname{pf}^{\mathrm{ref}}=\Delta_5
\quad\Rightarrow\quad
\operatorname{pf}^{\mathrm{geom}}_X=\Delta_5 .
```

Safe:

```tex
\[
\operatorname{pf}^{\mathrm{geom}}_X=\Delta_5
\]
only after \(\mathsf{Real}_X\) preserves the Pfaffian line, square-root
torsor, compact parity lifts, and leading cusp trivialization.
```

Forbidden:

```tex
s^{b_R(\gamma)}
```

when \(b_R\) means geometric elliptic support degree.

Safe:

```tex
s^{m_R(\gamma)},\qquad
m_R=\operatorname{pr}_3\overline\Pi_{X,R}(\gamma),
\qquad
b_R^{\mathrm{geom}}\ \hbox{controls local/wrapped support.}
```

## Claim-Status Recommendation

The manuscript can safely carry this status table:

| Claim | Status |
|---|---|
| Borcherds--Gritsenko--Nikulin product for \(\Delta_5\) | proved/imported target theorem |
| Denominator algebra \(\mathfrak g_{\Delta_5}\) and signed multiplicities | imported target data |
| finite target reference tower \(\mathsf{TDI}^{\mathrm{ref}}\) | theorem/definition if explicitly written from target data |
| target reference Pfaffian equals \(\Delta_5\) | target-side proposition, restating BGN product under a Pfaffian convention |
| finite geometric source \(\mathfrak H^{\mathrm{geom}}_{X,R}\) | open construction |
| realization functor \(\mathsf{Real}_{X,R}\) | open construction/condition |
| compact geometric Pfaffian equals \(\Delta_5\) | conditional proposition only |

## Attack Ledger

```yaml
id: A59-01
severity: 1
status: valid
lens: source_target_firewall
target: revision-1923 lines 27848-27948, 29517-29732
claim: "The universal finite Dirac-Igusa Hall source is the constructed compact source object."
broken_step: The object is built from g_Delta5, U(g_Delta5), BKM bracket, target PBW, target radical quotient, and GN multiplicities.
evidence_type: line_reference
evidence_ref: materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:29390-29732; main.tex:5825-5834; main.tex:12222-12303; main.tex:13411-13549
confidence: high
minimal_heal: Rename it as a finite target reference tower and state compact geometry as a realization problem.
residual: finite compact geometric source data and realization functor are not constructed.
deciding_evidence: source-side finite stacks/correspondences/orientations/coalgebras/primitives/Pfaffian lines plus transition-compatible Real maps.

id: A59-02
severity: 1
status: valid
lens: notation_collision
target: proposed notation R_X:H_X^{geom}->UDI
claim: "Use R_X and H_X^{geom} for the compact realization theorem."
broken_step: R_X already denotes primitive-recognition data and H_X already denotes the hybrid certificate slot in main.tex.
evidence_type: line_reference
evidence_ref: main.tex:11885-11891; main.tex:11933-11995; main.tex:12240-12256
confidence: high
minimal_heal: Use \mathsf{Real}_{X,R} and \mathfrak H^{geom}_{X,R}.
residual: patch needed if latest-PDF notation is imported.
deciding_evidence: grep gate showing no R_X/H_X^{geom} functor usage.

id: A59-03
severity: 2
status: valid
lens: theorem_status
target: compact Pfaffian equality
claim: "Pf(UDI)=Delta_5 gives the compact geometric Igusa theorem."
broken_step: Target/reference Pfaffian equality is BGN product in new notation; geometric equality requires Pfaffian line and realization preservation.
evidence_type: proof_gap
evidence_ref: main.tex:13472-13497; Agent51 Dirac block/super-Pfaffian report
confidence: high
minimal_heal: State a target reference normalization proposition plus a conditional compact realization proposition.
residual: geometric Pfaffian line and cusp trivialization remain open.
deciding_evidence: construction of \mathscr L_{Pf,X,R}, compact parity lifts, leading trivialization, and Real compatibility.
```

## Bottom Line

After a target reference tower is introduced, the safest manuscript
structure is:

1. Definition: finite target reference tower
   \(\mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}\).
2. Proposition: target reference normalization
   \(\operatorname{pf}^{\mathrm{ref}}=\Delta_5\).
3. Definition: finite geometric source domain
   \(\mathfrak H^{\mathrm{geom}}_{X,R}\).
4. Definition: realization functor
   \(\mathsf{Real}_{X,R}:\mathfrak H^{\mathrm{geom}}_{X,R}\to
   \mathsf{TDI}^{\mathrm{ref}}_{\Delta_5,E,L;R}\) with
   \textup{(Real-1)--(Real-10)}.
5. Proposition: conditional compact realization, proving
   \(\operatorname{pf}^{\mathrm{geom}}_X=\Delta_5\) only under the
   realization hypotheses.
6. Open problem: construct \(\mathfrak H^{\mathrm{geom}}_{X,R}\),
   \(\mathsf{Real}_{X,R}\), and all open geometric preservation clauses.

Anything stronger makes target data masquerade as compact geometry.
