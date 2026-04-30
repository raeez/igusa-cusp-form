# A013 report: D6-D2-D0 Mukai vector computation

Runtime id: `019ddbd1-80c5-7263-a6fc-ee33f6a3088f`.
Nickname: Descartes.
Status: completed.
Files changed by agent: none.

## Status

Survives. The current theorem at `main.tex:2737` is the correct CY3
Mukai-Gram computation.

## First-Principles Check

\[
0\to I_Y\to O_X\to O_Y\to0,\qquad
\operatorname{ch}(I_Y)=1-\operatorname{ch}(O_Y).
\]

For a one-dimensional sheaf on a smooth threefold with \(c_1(X)=0\),
\[
\operatorname{ch}_2(O_Y)=\operatorname{PD}[Y],\qquad
\int_X\operatorname{ch}_3(O_Y)=\chi(O_Y)=n.
\]

For \(X=S\times E\),
\[
\sqrt{\operatorname{td}(X)}
=\pi_S^*(1+[pt_S])\pi_E^*(1)
=(1,0,1)\otimes1_E.
\]

With
\[
[Y]=\beta\times\{pt\}+d\{pt\}\times E,
\]
one has
\[
\operatorname{ch}(O_Y)
=(0,0,d)\otimes1_E+(0,\beta,n)\otimes\omega_E,
\]
where \(\beta\) is the Poincare dual K3 class. Hence
\[
\operatorname{ch}(I_Y)
=(1,0,-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
\]
and multiplication by \((1,0,1)\otimes1_E\) gives
\[
v_X(I_Y)
=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E.
\]

The signs are forced by \(I_Y=O_X-O_Y\). Then with
\[
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n),
\]
the Mukai pairing gives
\[
\frac{Q_Y^2}{2}=\frac{\beta^2}{2},\qquad
Q_Y\cdot P_Y=n,\qquad
\frac{P_Y^2}{2}=d-1.
\]
So for \(\beta_h^2=2h-2\),
\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
\]

## Old Error Status

The old fourfold/Todd error is gone: `rg` finds no `fourfold` or `Todd
correction` in `main.tex`. The only Todd contribution is the explicit K3
factor \((1,0,1)\), producing \(1-d\); it does not alter
\(n=\chi(O_Y)\).

## Recommended Theorem Wording

Keep the current theorem. Optional phrase:
"identifying \(\beta\in H_2(S,\mathbb Z)\) with its Poincare dual in
\(H^2(S,\mathbb Z)\)."

If strict CY terminology is policed, say "Calabi--Yau threefold in the
DT/PT sense \(K_X\simeq O_X\)" since \(K3\times E\) is non-strict.

## Anchors

`main.tex:2737`, `main.tex:2777`, `main.tex:2797`, `main.tex:2813`.
Guide: `notes/attack_whitepaper_analysis_20260430_guide.md:101`.
CYQG lock: `antipatterns_catalogue.md:4935`.

Primary-source cross-checks:
Bryan defines \(\operatorname{Hilb}^{\beta,n}(X)\) by
\(n=\chi(O_Z)\), arXiv:1504.02920. Oberdieck defines
\(P_n(X,\beta)\) by \(\chi(F)=n\) and DT Hilbert schemes by
\(\chi(O_Z)=n\), arXiv:1605.04631. Oberdieck--Pixton use \(S\times E\)
as a CY threefold in the primitive Igusa theorem, arXiv:1706.10100.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, and read-only `curl` streams
from arXiv source tarballs/gzips. No git commands. No build.
