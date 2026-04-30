# A030 report: retained-stage transition compatibility and ML

Runtime id: `019ddbe2-959e-7e10-a8d0-5dbd6ebf1977`.
Nickname: Bohr.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Retained compactified Hall stages plus finite checks imply global
Dirac-Igusa recognition.

## Verdict

Not proved unconditionally. The manuscript is safe only as a conditional
retained finite-stage theorem plus a conditional inverse-limit theorem.
If transition strictness, finite-slice ML, closed radicals, and strict
PBW preservation are not supplied, the global recognition claims must be
demoted to compatible pro-comparisons.

## Failure Mode / Proof

Finite NO1--NO7 checks commute with the inverse limit only under the
stated topology. Products/coproducts require
\[
\rho m_{R'}=m_R(\rho\otimes\rho),\qquad
(\rho\otimes\rho)\Delta_{R'}=\Delta_R\rho.
\]
Radicals require
\[
K_\beta=\ker G_\beta\cap\ker G_{-\beta}^t,\quad
QB(P\otimes K)=QB(K\otimes P)=0,\quad
(Q\otimes Q)DK=0,
\]
plus \(\rho(K_{R',\beta})\subset K_{R,\beta}\). PBW requires strict
filtration preservation, not only finite PBW at each stage. Exact
passage to the limit requires \(R^1\!\varprojlim=0\) on source
coalgebras, bar/cobar systems, cones, radicals, PBW associated gradeds,
kernels/cokernels, and parity pieces.

## Local Anchors

NO1--NO7 are explicit finite successor diagrams at `main.tex:9470`.
Finite-slice ML is defined at `main.tex:11114`. The global theorem is
already conditional at `main.tex:14445`, with the strict-limit
hypothesis at `main.tex:14600`. The finite source matrix criterion
states the needed \(M,D,B,G,K,Q,A_\beta\) data at `main.tex:15268`. The
\(W_{\le3}\) NO7 protocol starts at `main.tex:15373`.

## Critique Anchors

The guide forbids the unrestricted compact theorem and requires retained
finite stages plus transition identities at
`notes/attack_whitepaper_analysis_20260430_guide.md:440`. CYQG AP-CY378
says target arithmetic is not \(W_{\le3}\) source matrices, and
AP-CY382 says finite windows do not automatically have a good limit.

## Prior-Report Alignment

A006:
recognition remains conditional until source matrices exist.

A022:
finite fibres and HN topology require ML and closed radicals.

A025:
compactified extension/flag-Quot stacks and properness are not
automatic.

A026:
d-critical, BBDJS, orientation, and six-functor data are supplied
hypotheses, not boundedness consequences.

## Claim-Status Recommendations

Retain finite \(R\) Hall kernels only as supplied-data theorems. Retain
\(\mathfrak K_X=\varprojlim_R\mathfrak K_{X,R}\),
\(P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}\),
\(\Omega_E^{\mathrm{ch}}C_X\simeq\mathsf{Den}_{\Delta_5,E}\), and
\(\operatorname{pf}_X=\Delta_5\) only conditional on strict transitions,
finite-slice ML, closed radicals, PBW strictness, and source-built
comparison maps. Without those hypotheses, state only a pro-system of
finite comparisons.

## Residual Obligations

Construct \(\Xi=(\gamma,[a,b],(P_i),N)\)-indexed retained schedules;
compactified extension and flag stacks; quotient-after-correspondence
functor; source \(W_{\le3}\) matrices, including the \(29|93\)
\(\delta_{123}\) block; radical coideal checks; strict PBW transition
matrices; and finite-slice ML for every tower used in the limit.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg -n -F`, `rg --files`, `find`, and
`git status --short`; no build.
