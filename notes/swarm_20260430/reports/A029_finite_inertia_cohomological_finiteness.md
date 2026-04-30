# A029 report: finite inertia and cohomological finiteness

Runtime id: `019ddbe2-8c52-79d3-81b5-3050936afe38`.
Nickname: Hilbert.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Finite-type d-critical retained stacks with BBDJS vanishing cycles
automatically give finite-dimensional protected cohomology.

## Verdict

False without finite residual inertia and coefficient discipline.
Conditional-safe in the manuscript because `main.tex:10402` and
`main.tex:11401` explicitly impose finite residual inertia, BBDJS
complexes, compact-support six-functor admissibility, and finite
protected cohomology. It is not a theorem from retained boundedness
alone.

## Failure / Proof

Counterexample:
the d-critical point stack \(B\mathbb G_m\) with trivial
vanishing-cycle coefficient is finite type, but
\[
H^\bullet(B\mathbb G_m,\mathbb C)\simeq\mathbb C[u]
\]
is infinite-dimensional in total degree. The manuscript records this at
`main.tex:11408`.

Heal:
if the retained quotient is finite type with finite residual inertia,
finite-type coarse moduli, and characteristic-zero constructible
coefficients, then protected compact-support cohomology is finite:
\[
\mathcal H^{\mathrm{or}}_{R,\widehat c}
=
H_c^\bullet(\mathfrak M_{R,\widehat c},
\Phi_{R,\widehat c}\otimes o_{R,\widehat c}).
\]
Finite stabilizers are harmless over \(\mathbb C\) or \(\mathbb Q\)
because finite-group invariants are exact. They are not harmless for
\(\mathbb F_2\) orientation obstruction theory.

Quotient stack issue:
a free \(E\)-quotient formed as an actual quotient stack or algebraic
space can be finite. Raw equivariant cohomology before descent carries
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,
\]
and finite stabilizers carry
\[
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\quad |x_i|=1.
\]
Hence quotient orientation requires the Borel classes and characters at
`main.tex:4107`, not just translation invariance.

BBDJS coefficient choice:
BBDJS gives the perverse sheaf for an oriented d-critical locus; it does
not by itself prove finite cohomology, quotient descent, finite inertia,
or Hall pull-push admissibility. Protected vector spaces should use
characteristic-zero coefficients. Mod-2 belongs to obstruction classes
\(\widetilde\beta^H\), \(\lambda^H\), not to the protected cohomology
dimension claim.

Compact support/properness:
finite dimensionality does not require properness if \(H_c^\bullet\) is
used on finite-type finite-inertia stacks. Hall multiplication still
requires admissible \(q_!\). The manuscript correctly says properness
of the raw exact-triangle map \(q\) is not asserted: `main.tex:11381`,
`main.tex:13289`.

## Local Anchors

Charge finiteness is only charge-index finiteness, not cohomological
finiteness: `main.tex:10311`.

Retained atlas hypothesis names finite residual inertia, BBDJS,
orientations, six functors: `main.tex:10411`.

Finite source package uses finite cohomology as S1 input:
`main.tex:11452`.

ML remains necessary for strict inverse-limit recognition:
`main.tex:10435`.

The unrestricted compact construction remains open:
`main.tex:12007`.

## Critique Anchors

A005:
orientation line is only safe after gerbe and quotient descent data
vanish.

A022:
finite-type stacks do not imply finite protected cohomology if residual
inertia survives.

A026:
BBDJS/d-critical/orientation/six-functor data are supplied, not produced
by retained boundedness.

CYQG AP-CY377:
orientation-gerbe source before global line.

CYQG AP-CY387:
finite-stabilizer edge formulas are tests, not vanishing theorems.

Primary source check:
BBDJS `arXiv:1211.3259` constructs vanishing-cycle perverse sheaves for
oriented d-critical loci; Joyce-Upmeier `arXiv:2001.00113` constructs
CY3 orientation data, not quotient linearizations or retained compact
sources.

## Recommendation

Keep the retained compact theorem conditional. Do not state
"finite type d-critical + BBDJS" implies finite-dimensional protected
cohomology. The safe formulation is:

finite retained charge window + finite-type d-critical stack + finite
residual inertia after rigidification + characteristic-zero BBDJS
coefficient complex + compact-support six-functor admissibility imply
finite-dimensional protected cohomology at fixed \(R\). The completed
theorem still requires ML, closed radicals, transition compatibility,
and source primitive/parity comparison.

## Residual Obligations

Prove finite residual inertia on all object, extension, flag, mixed, and
wrapped strata; state protected coefficients as \(\mathbb C/\mathbb Q\);
construct stacky BBDJS descent or keep it supplied; prove \(q_!\) finite
compact-support realization for every retained correspondence; prove ML
and radical closedness for the inverse system.

Commands run by agent:
read-only `sed`, `nl -ba | sed -n`, `rg`, `find`, and
`git status --short`; arXiv source checks for BBDJS and Joyce-Upmeier;
no build.
