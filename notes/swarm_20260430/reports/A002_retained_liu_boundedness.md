# A002 report: retained Liu-Hilbert boundedness

Runtime id: `019ddbc4-ec9b-70a1-a2de-b3997aadd57e`.
Nickname: Kuhn.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Fixing a retained Liu-Hilbert class
\[
\Xi=(\gamma,[a,b],(P_i)_{i=a}^b,N)
\]
proves a finite-type retained semistable stack, and might therefore
close fixed-class Liu boundedness.

## Verdict

Conditionally proved only for the retained slice. It does not prove full
fixed-class Liu boundedness.

Fixing \(\Xi\) proves boundedness because it imposes the data
boundedness would otherwise have to produce: fixed standard cohomology
amplitude, fixed Hilbert polynomials, and fixed
Castelnuovo--Mumford regularity. The Quot/Postnikov finite-type argument
is coherent after repair. The critique's version is too compressed:
"assembled by \(\operatorname{Ext}^1(F_i,F_{i-1})\)" must be replaced
by a finite Postnikov/derived-complex construction with closed
compatibility equations.

## Exact Proven Statement

For fixed \(\Xi\), the stack of objects \(F\in D^b\operatorname{Coh}(X)\)
satisfying
\[
F\in\mathcal A_{s,t},\quad [F]=\gamma,\quad
H^i(F)=0\ (i\notin[a,b]),\quad
P_H(H^i(F))=P_i,\quad
H^i(F)\text{ is }N\text{-regular},
\]
and \(\sigma_{s,t}\)-semistability is finite type, provided the hidden
hypotheses below hold.

First-principles core:
\(N\)-regularity gives
\[
\mathcal O_X(-N)^{P_i(N)}\twoheadrightarrow H^i(F),
\]
so each \(H^i(F)\) lies in a finite-type Quot scheme. A bounded complex
with these cohomology sheaves is obtained by a finite Postnikov tower
over a finite product of Quot schemes; properness of \(X\) makes the
relative \(\mathbf R\mathcal Hom\) complexes perfect/coherent. Thus the
ambient retained complex stack is finite type. If heart-membership and
semistability are open in this bounded family, the retained semistable
locus is finite type.

## Hidden Hypotheses

1. \(X=S\times E\) is projective over \(\mathbb C\), with fixed ample
   \(H\).
2. \([a,b]\) is standard cohomological amplitude, not merely
   Tor-amplitude. Tor-amplitude alone does not give the Quot proof.
3. The \(P_i\) are fixed and compatible with \(\gamma\). A full Liu class
   does not by itself determine individual standard-cohomology Hilbert
   polynomials.
4. The bounded complex stack is represented by a finite-type derived
   Artin stack, using perfect/universally gluable complexes or an
   equivalent finite Postnikov presentation.
5. Liu's heart \(\mathcal A_{s,t}\) is noetherian, and
   \(F\in\mathcal A_{s,t}\) is open in the retained bounded family.
6. \(\sigma_{s,t}\)-semistability is open in bounded families in that
   heart.
7. Quasi-smoothness, finite residual inertia, d-critical charts, BBDJS
   coefficients, orientations, and compact-support six-functor
   operations are not consequences of \(\Xi\); they remain supplied
   Hall-sector hypotheses.

## Why Full Liu Boundedness Is Not Proved

Fixing \(\Xi\) proves:
\[
\mathfrak M^{ss}_{\Xi}\text{ is finite type}.
\]

Full fixed-class Liu boundedness asks:
\[
\mathfrak M^{ss}_{\sigma_{s,t}}(\gamma)\text{ is finite type}.
\]

Equivalently, for each fixed full Liu class \(\gamma\), one must prove
that finitely many retained refinements
\[
\Xi_j=(\gamma,[a_j,b_j],(P_{j,i}),N_j)
\]
cover all \(\sigma_{s,t}\)-semistable objects of class \(\gamma\). A
retained schedule is a domain choice, not proof that all compact objects
occur in it.

## Recommended Wording

Theorem: Retained Liu-Hilbert finite-type slice. Under the hypotheses
above, \(\mathfrak M^{ss}_{\Xi}\) is a finite-type derived Artin stack.

Open Problem: Full fixed-class Liu boundedness. For each full Liu
numerical class \(\gamma\), prove that
\(\mathfrak M^{ss}_{\sigma_{s,t}}(\gamma)\) is covered by finitely many
retained Liu-Hilbert refinements \(\Xi_j\), equivalently by a uniform
boundedness theorem producing finite amplitude, finite Hilbert-polynomial
data, and uniform regularity bounds.

## Anchors

Main missing boundedness statement: `main.tex:10381`.
Supplied retained Hall hypotheses: `main.tex:13026`.
Theorem already says it is not Liu boundedness: `main.tex:13186`.
Finite extension-stack proposition: `main.tex:13235`.
Guide judgement: `notes/attack_whitepaper_analysis_20260430_guide.md:186`.
Critique retained theorem:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43620`.
CYQG locks `AP-CY373`/`AP-CY374`.
Local bibliography: Liu/AP/PTVV at `proj.bib:869`.

Commands run by agent: read-only `sed`, `rg`, and `nl -ba | sed -n`.
No build, no tests, no git mutation.

## Residual Obligations

Prove openness for Liu heart-membership and semistability in these
retained bounded families; replace adjacent-\(\operatorname{Ext}^1\)
prose by a correct Postnikov/derived-complex construction; state
quasi-smooth/d-critical/orientation/six-functor data separately; keep
full fixed-class Liu boundedness open.
