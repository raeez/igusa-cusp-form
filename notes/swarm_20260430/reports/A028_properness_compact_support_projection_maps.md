# A028 report: properness and compact-support projection maps

Runtime id: `019ddbe2-3efa-7922-aae2-b783faccbb4b`.
Nickname: Nietzsche.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Raw exact-triangle extension stacks and the displayed \(p/q\) Hall
correspondences are proper compact-support projection maps.

## Verdict

Partially valid, but only after weakening. Raw exact-triangle stacks are
formal Hall correspondences until compact-support admissibility is
supplied. Properness belongs to the closed-filtration/flag-Quot
compactification, not to the raw exact-triangle \(q\)-map.

## Failure Mode

Raw exact triangles:
finite type only under supplied bounded finite-stage hypotheses;
ordinary \(q\)-properness is not asserted and is false in general. The
DVR cone example at `main.tex:13724` shows valuative failure.

Compactified closed-filtration stack:
\[
\overline{\mathfrak E}^{\mathrm{ret}}_{\Xi_A,\Xi_B;\Xi_C}
=\{(C,A\hookrightarrow C): C\in\mathfrak M_{\Xi_C},\
A\in\mathfrak M_{\Xi_A},\ C/A\in\mathfrak M_{\Xi_B}\}
\]
has
\[
p(C,A\subset C)=(A,C/A),\qquad q(C,A\subset C)=C.
\]
Here \(q\) is projective/proper only in the closed relative
Quot/flag-Quot model, under specialization-closed retained hypotheses.
\(p\) is finite-type/admissible for pullback, not generally proper.

The \(q\)-map is not finite: even locally,
\(\mathcal O_x\subset\mathcal O_x^{\oplus2}\) gives a
\(\mathbb P^1\)-family; see `main.tex:8289`.

Mixed/wrapped properness is still conditional: anchors, translation
laws, subobject/quotient anchors, and closedness in families must be
part of the stack, not slogans.

## Map Status

Raw exact-triangle \(p,q\):
finite type only under supplied bounded Ext/perfectness; not proper;
only formal until \(p^*,q_!,p_!\) are admitted in a compact-support
six-functor theory.

Closed-filtration/flag-Quot \(q\):
representable/projective/proper over fixed output when retained
substacks are closed in the bounded Quot/Postnikov ambient.

Closed-filtration/flag-Quot \(p\):
finite type/admissible; not generally proper.

Two-step and higher flag stacks:
proper over output only in closed flag-Quot compactification;
Beck-Chevalley, Thom-Sebastiani, orientations, and quotient descent
remain extra data.

Reduced \(Q_{E,R}\):
must be a pseudofunctor on the finite correspondence category, not an
object-stack quotient; anchor `main.tex:7893`.

## Theorem Statements To Weaken

At `main.tex:13002`, replace "finite set of full effective Liu classes"
by retained Liu-Hilbert schedules
\[
\Xi=(\gamma,[a,b],(P_i),N).
\]
The theorem should be "from supplied retained Liu-Hilbert compactified
sector datum."

At `main.tex:13235`, retitle/weaken "Fixed-class boundedness gives the
finite Hall stack." Full fixed-class Liu boundedness remains open;
retained Liu-Hilbert boundedness gives only retained finite slices.

At `main.tex:13637`, keep the statement only as binary/two-step hybrid
atlas. Full factorization needs colored tree flags and
\(\mathfrak o^{\mathrm{col}}_R=0\).

At `main.tex:11701`, "proper on the support" should be read as supplied
proper-support or exceptional compact-support admissibility, not raw
exact-triangle properness.

## Anchors

Local:
`notes/swarm_20260430/reports/A025_compactified_extension_stacks.md:8`,
`notes/swarm_20260430/reports/A002_retained_liu_boundedness.md:17`,
`notes/swarm_20260430/reports/A004_hybrid_correspondences.md:34`,
`notes/swarm_20260430/reports/A022_finite_fibre_hn_topology.md:75`.

CYQG:
AP-CY373/AP-CY375.

## Claim-Status Recommendation

Keep the compactified Hall architecture, but state it as conditional
retained compactified data. Do not let any theorem infer proper Hall
multiplication from raw exact triangles, weak Liu classes, or finite
type alone.

## Residual Obligations

Construct retained Liu-Hilbert schedules; prove specialization-closed
retained substacks; define compactified mixed/wrapped anchors as closed
conditions; build colored tree flag stacks; verify \(p^*,q_!,p_!\),
base change, Thom-Sebastiani, orientation descent, finite inertia, and
\(R'\to R\) compatibility.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, `find`, and
`git status --short`; no build or tests.
