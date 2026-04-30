# A032 report: wrapped anchors and determinant-anchor transport

Runtime id: `019ddbe4-31e8-77c0-b123-57efae33bda1`.
Nickname: Volta.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Mixed/wrapped retained correspondences may use the determinant anchor
\[
\lambda(F)=\det Rp_{E,*}F\otimes O_E(-\chi(F)0_E)
\in \operatorname{Pic}^0(E)\simeq E
\]
to rigidify wrapped support, transport anchors through local/wrapped
extension stacks, impose closed anchor equations in families, then
quotient by \(E\).

## Verdict

Partially healed, not construction-level. `main.tex` correctly says the
wrapped prequotient, anchor, translation law, losslessness, mixed/WW
compatibility, and transition compatibility are finite data, not
consequences: `main.tex:7566`--`main.tex:7640`. It also correctly
forbids quotient-first repair: `main.tex:7893`--`main.tex:7944` and
`main.tex:8377`--`main.tex:8404`.

The remaining gap is in the geometric retained theorem/atlas: it still
says the wrapped stack is the fibre of the determinant anchor over
\(0_E\), and that the determinant anchor is imposed as a closed
condition, without separately giving induced anchor maps on subobjects,
quotients, intermediate flag terms, and specialization-closed retained
compactifications. Anchors: `main.tex:13100`--`main.tex:13108`,
`main.tex:13212`--`main.tex:13216`, and
`main.tex:13698`--`main.tex:13704`.

## Failure Mode

The determinant anchor candidate has translation weight \(\chi(F)\), not
unit weight in general: `main.tex:7593`--`main.tex:7600`. Thus it is
legal only after a fixed convention, finite cover/division, or
replacement Abel-Jacobi/framing datum is supplied. On \(\chi=0\) strata
it may remember no relative \(E\)-position. The manuscript notices this
and gives the Ext counterexample showing finite divisor/determinant
shadows are not lossless: `main.tex:7602`--`main.tex:7621`.

For an exact sequence \(0\to A\to C\to B\to0\), determinant of
cohomology gives the required anchor law only after explicit determinant
functor choices:
\[
\lambda(C)=\lambda(A)+\lambda(B),
\]
with projection-finite local terms replaced by their Abel-Jacobi anchor.
These induced maps must be recorded on every LL/LW/WL/WW stack and every
two-step intermediate. The critique proposes formulas such as
\(\lambda(W_C)=\lambda(W_B)+AJ(L_A)\),
\(\lambda(W_C)=\lambda(W_A)+AJ(L_B)\), and
\(\lambda(W_C)=\lambda(W_A)+\lambda(W_B)\), but those are critique
architecture, not yet source truth:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44500`
--`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44546`.

## Exact Finite-Stage Hypotheses Needed

1. A retained Liu-Hilbert schedule \(\mathcal X_R\), not just full Liu
classes, closed under subobjects, quotients, extensions, duals,
local/wrapped anchors, and all flag intermediates.

2. For each wrapped class \(\eta\), a finite-type rigidified wrapped
prequotient with universal family and an actual morphism
\(\lambda_{\eta,R}\to E\), with proved translation law
\(\lambda(tW)=\lambda(W)+N_\eta t\), unit normalization or finite-cover
division, finite residual stabilizers, and transition compatibility.

3. For every compactified retained extension/flag stack,
determinant-functor isomorphisms inducing anchor equations on input,
output, quotient, and intermediate terms. These equations must satisfy
two-step and colored-tree coherence.

4. Closedness in families: the retained object/subobject/quotient loci
must be closed or specialization-stable inside the retained
Quot/flag-Quot ambient; semistable open substacks alone do not give
proper \(q\). A025 flags this directly.

5. Quotient by \(E\) only after the unreduced local, mixed, wrapped, and
flag correspondences exist, with anchors retained, quotient-orientation
gerbes killed, finite-stabilizer characters computed and zero, and
\(Q_{E,R}\) supplied as a pseudofunctor on the finite correspondence/BM
category. AP-CY364, AP-CY367, AP-CY376, AP-CY377 all apply.

## Claim-Status Recommendation

Keep the current conditional language. Strengthen the geometric retained
theorem so "determinant anchor imposed as a closed condition" is replaced
by an explicit finite-stage anchor-transport axiom package. Do not claim
mixed/wrapped compactified properness or legal \(E\)-quotient from the
determinant anchor alone.

## Residual Obligations

Construct the retained anchor transport diagrams; prove the
determinant/AJ anchor equations are closed in the retained
flag-Quot compactifications; compute finite stabilizer linearization
characters on object, extension, mixed, wrapped, and flag strata;
replace eight-word binary coherence by colored-tree coherence before
full hybrid factorization is claimed.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, and `git status --short`; no build or
tests.
