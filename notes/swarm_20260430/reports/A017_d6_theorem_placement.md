# A017 report: D6 theorem placement before scalar quotient

Runtime id: `019ddbd3-3649-7f21-af9e-55fbc217c481`.
Nickname: Euclid.
Status: completed.
Files changed by agent: none.

## Verdict

Current `main.tex` has a real placement leak, but not in the local
D6/scalar block.

## Architecture Attacks

### Local D6 Section

Local order is correct. `main.tex:2737` proves the D6-D2-D0 Mukai-Gram
theorem, including
\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1)
\]
at `main.tex:2764-2772`, before scalar quotient integration at
`main.tex:2841-2863`. This satisfies the guide obligation at
`notes/attack_whitepaper_analysis_20260430_guide.md:101-125`.

### Later OP Scalar Theorem

The later OP scalar theorem is downstream. OP normalization starts at
`main.tex:15894`, and the scalar-square theorem at `main.tex:15976`
explicitly depends on reduced quotient integration at
`main.tex:15991-15996`.

### Early Dirac/Pfaffian Leak

The leak is earlier:
`main.tex:785-820` states a Dirac/Pfaffian recognition target with
scalar trace
\[
-4096\Delta_5^{-2}
\]
before the D6 theorem and before the OP normalization branch is defined.

Worse, `main.tex:1128-1498` states the Dirac--Pfaffian theorem before
the physical-charge theorem lane, and `main.tex:1731-1754` uses
Proposition `\ref{prop:op-normalization}` by forward reference. That is
narrative inversion / proof leakage.

### Final Synthesis Spine

The final synthesis spine at `main.tex:16186-16198` says "formal charge
and normal ordering" but does not name the D6-D2-D0 Mukai-Gram theorem
as the bridge from physical DT variables to Gram variables. This
underplays the central theorem demanded by the critique at
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:4629-4737`
and the theorem order at
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:5483-5571`.

## Required Reorder/Rename

Move or demote the early `Dirac/Pfaffian recognition target`
(`main.tex:785`) and `Dirac--Pfaffian normalization and orientation
character` theorem (`main.tex:1128`) until after:
D6-D2-D0 theorem, reduced scalar quotient integration, formal
normal-ordering, and OP scalar branch.

Minimal acceptable patch:
rename the early proposition/theorem as a target preview and remove the
explicit \(-4096\) scalar trace there, replacing it by "must match the
OP/DT scalar branch after the D6-D2-D0 dictionary and OP normalization
below."

Rename the synthesis spine item to:
`D6-D2-D0 Mukai-Gram dictionary and formal normal ordering`
before the scalar-square item.

## Residual Obligations

A009/A012 scalar firewalls survive: OP gives scalar normalization only,
not Pfaffian orientation. A007's residual warning applies to
`main.tex:1744-1754`: \(C_{\square,X}=-4096\) is valid only after a
trace comparison to the OP/DT branch is included in the datum.

Commands run by agent:
read-only `sed`, `rg`, `nl -ba`, and `git status --short`. No build.
