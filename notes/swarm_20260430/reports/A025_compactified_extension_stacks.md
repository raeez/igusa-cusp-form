# A025 report: compactified extension stacks and properness

Runtime id: `019ddbdd-d40e-7f00-870a-fb0653e0c8fc`.
Nickname: Heisenberg.
Status: completed.
Files changed by agent: none.

## Verdict

Retained Hall multiplication is admissible only as a retained
Liu-Hilbert, compactified closed-filtration/flag-Quot construction, or
as an explicitly nonproper exceptional-compact-support six-functor
construction. Raw exact-triangle pull-push is not enough.

## Valid Attacks

1. \(C_R\) as a finite set of full Liu classes is too weak. The finite
stage must be indexed by retained Liu-Hilbert classes
\[
\Xi=(\gamma,[a,b],(P_i),N)
\]
with fixed standard cohomology amplitude, Hilbert polynomials, and
regularity. Otherwise finite type and Quot compactification are not
construction-level data.

Anchors:
`main.tex:13008`,
`notes/swarm_20260430/reports/A002_retained_liu_boundedness.md:1`,
CYQG AP-CY373.

2. Properness of the compactified correspondence is not automatic from
semistability. Semistability is normally open in bounded families; an
open substack of a projective Quot scheme is not proper. The retained
substacks must be specialization-closed in the bounded Quot/Postnikov
ambient, and closed under the subobjects and quotients appearing in the
correspondence. The manuscript has this in the local-local proposition
at `main.tex:8186`, but the global theorem should require it
explicitly.

3. The raw stack
\[
\mathfrak E^{\mathrm{geom}}_{R,\widehat c,\widehat c'}
\]
of exact triangles at `main.tex:13121` is finite-type only under
supplied hypotheses; ordinary \(q\)-properness is not asserted and is
false in general. The text fences this at `main.tex:13289` and
`main.tex:13704`, but the retained theorem should name the compactified
stack separately.

4. Mixed and wrapped properness is underspecified. The determinant
anchor, its translation law, induced anchors on subobjects/quotients,
and closedness of those anchor conditions in families must be part of
the stack definition. Otherwise "closed moduli of filtrations inside
the output" at `main.tex:13700` is only a slogan.

5. Two-step flags are not yet construction-level in the finite Hall
theorem. The flag stack at `main.tex:13145` must include intermediate
retained classes, maps to both iterated correspondence fibre products,
and Beck-Chevalley/Thom-Sebastiani/orientation data. The eight-word
atlas at `main.tex:7832` gives binary associativity only; full hybrid
factorization still needs colored tree flags, as the text admits at
`main.tex:7887`.

## Required Stack Package

For each finite height \(R\), supply a finite retained schedule
\(\mathcal X_R\) of classes \(\Xi\), with normal-ordered lifts
\(\widehat c_\Xi\), local/wrapped color, closure under retained sums,
subobjects, quotients, duals, and all intermediate flag classes.

Object stacks:
\[
\mathfrak M^{\mathrm{sc}}_{\Xi},\quad
\mathfrak M^{\mathrm{loc}}_{\Xi,I}\subset
\mathfrak M^{\mathrm{sc}}_\Xi\times E^I,\quad
\mathfrak M^{\mathrm{wr}}_{\Xi}
\]
must carry scalar and \(E\)-translation rigidification, finite residual
inertia, BBDJS coefficients, reduced obstruction theory, and orientation
gerbe/line.

For the compactified binary extension stack, use the convention
\[
0\to A\to C\to B\to0:
\]
\[
\overline{\mathfrak E}^{\mathrm{ret}}_{\Xi_A,\Xi_B;\Xi_C}
=\{(C,A\hookrightarrow C): C\in\mathfrak M_{\Xi_C},\
A\in\mathfrak M_{\Xi_A},\ C/A\in\mathfrak M_{\Xi_B}\}.
\]
Maps:
\[
p(C,A\subset C)=(A,C/A),\qquad q(C,A\subset C)=C.
\]
The stack must be a closed derived substack of a relative
Quot/flag-Quot or retained Postnikov-Quot presentation over the output.
Then \(q\) is projective/proper in the compactified model. If the raw
exact-triangle model is used instead, replace properness by a specified
admissible \(q_!\) with finite compact-support realization.

Two-step flag stacks:
\[
\overline{\mathfrak F}^{(2),\mathrm{ret}}_{\Xi_1,\Xi_2,\Xi_3;
\Xi_{12},\Xi_{23},\Xi_{123}}
=\{0\subset F_1\subset F_2\subset C\}
\]
must include graded pieces \(\Xi_1,\Xi_2,\Xi_3\), intermediates
\(\Xi_{12},\Xi_{23}\), output \(\Xi_{123}\), and maps to both iterated
extension fibre products. Properness over the output comes from closed
flag-Quot only under the closed/specialization hypotheses above.

For local/mixed/wrapped colors, the same stacks must retain support
configurations and all input/intermediate/output anchors before
quotienting by \(E\).

Six-functor hypotheses:
admissible \(p^*\) or Gysin pullback, admissible \(q_!\), independent
admissible \(p_!\) for coproduct, finite-dimensional compact-support
realization, base-change for flag squares, projection formula, and
coherent reduced Thom-Sebastiani transport.

Quotient hypotheses:
\(Q_{E,R}\) is a pseudofunctor on the finite correspondence category,
not an object-stack quotient; it must preserve extension and flag
correspondences, coefficients, orientations, and all associativity
2-morphisms. Anchor: `main.tex:7893`.

## Anchors

Guide:
`notes/attack_whitepaper_analysis_20260430_guide.md:196`,
`notes/attack_whitepaper_analysis_20260430_guide.md:241`.

Critique:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:37940`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:38344`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43923`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44076`.

A004 agrees on the compactified-correspondence and colored-tree gap.
A016 confirms rank-one closure is not the live Hall-source issue.

## Residual Obligations

Expand \((\mathrm{Bnd})\) from full Liu classes to retained
Liu-Hilbert schedules. Prove or assume closed/specialization-stable
retained substacks, not merely open semistable loci. Define
compactified mixed/wrapped extension and colored flag stacks with
anchors. Verify \(p^*,q_!,p_!\), flag base-change, Thom-Sebastiani
coherence, orientation-gerbe descent, finite stabilizer characters, and
\(R'\to R\) transition compatibility.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, one `find` over CYQG, and
`git status --short`; no build or tests.
