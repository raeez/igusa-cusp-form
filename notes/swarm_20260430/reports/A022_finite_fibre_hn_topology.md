# A022 report: finite-fibre/HN topology assumptions

Runtime id: `019ddbd9-9ae6-7191-8504-ad382346b982`.
Nickname: Dirac.
Status: completed.
Files changed by agent: none.

## Verdict

A global fibre \(\overline\Pi_X^{-1}(\gamma)\) is not finite. The
manuscript is safe only where \(\overline\Pi_{R,*}^{\Theta}\) is taken
at finite HN height \(R\), over finite \(\widehat\Gamma_R\), and the
global object is the completed inverse limit
\[
(\overline\Pi_{X,*}^{\Theta}V)_\gamma
=\varprojlim_R(\overline\Pi_{R,*}^{\Theta_R}V_R)_\gamma.
\]

Anchors:
`main.tex:8762`, `main.tex:8777`, `main.tex:8783`.

## Finite / Completed / Formal

Finite:
fixed \(R\), finite \(\widehat\Gamma_R\), finite fibres of
\(\overline\Pi_X:\widehat\Gamma_R\to\Gamma_{\rm gram}\). This uses
sectorial HN finiteness and bounded HN words, not lattice finiteness.

Anchors:
`main.tex:10281`, `main.tex:10472`, `main.tex:12025`.

Completed:
\(P_X^\Pi\), completed tensor products, coproducts, pairings, radicals,
bar/cobar systems. These are inverse limits of finite operations;
strictness needs transition compatibility and Mittag--Leffler.

Anchors:
`main.tex:8690`, `main.tex:9015`, `main.tex:10435`,
`main.tex:11114`.

Formal only:
the lattice law \((c,T)\star(c',T')\), additivity of
\(\overline\Pi_X\), and the Picard translation cochain \(\Theta_\Pi\).
These do not construct Hall pull-push, cyclic lift, Frobenius pairing,
radical coideal, or compact source data.

Anchor:
`main.tex:8745`.

## Attacks

1. The processed critique's direct formula
   \((\Pi_*P)_\gamma=\oplus_{\Pi(c)=\gamma}P_c\) and "automatic"
   pushforward theorem are unsafe without finite support or HN
   completion.

   Anchors:
   `materials/processed/2026-04-30-attack-whitepaper-analysis.txt:3794`,
   `materials/processed/2026-04-30-attack-whitepaper-analysis.txt:9120`.

2. Fixed retained Liu-Hilbert data prove only retained finite slices, not
   full fixed-class Liu boundedness or compact-source cofinality.

   Anchors:
   `notes/swarm_20260430/reports/A002_retained_liu_boundedness.md:21`,
   `main.tex:10381`.

3. Finite-type stacks do not by themselves give finite protected
   cohomology if residual inertia survives. The finite-inertia clause is
   load-bearing.

   Anchor:
   `main.tex:11401`.

4. \(q_!\) is legitimate only as exceptional compact-support pushforward
   in a chosen six-functor theory, or under a proper-support
   compactification. Ordinary properness of raw exact-triangle \(q\) is
   not asserted.

   Anchors:
   `main.tex:11381`, `main.tex:13289`.

5. Even finite stages do not make the limit strict unless ML,
   continuity, and radical closedness hold. If [ML] fails, recognition
   weakens to a pro-comparison.

   Anchor:
   `main.tex:10457`.

## Hypotheses Needed

Support property, HN property, strict sector, finite bounded-height
semistable stacks; finite retained Liu-Hilbert schedules; finite-type
quasi-smooth d-critical stacks; finite residual inertia; BBDJS
coefficients; reduced orientations and Thom--Sebastiani coherence;
admissible compact-support pull-push; finite cohomology; NO1--NO7;
finite-slice ML; closed radicals; no-overcount acyclicity
\(\mathfrak o^{\rm no}_{R,c,T}=0\).

Anchor:
`main.tex:10501`.

## Residual Obligations

Construct actual retained finite Hall kernels; prove or assume cofinal
retained schedules; verify NO1--NO7 on every successor arrow; prove ML
and radical closedness; compute \(W_{\le3}\) source matrices instead of
importing target dimensions. A006 confirms target arithmetic does not
supply source matrices.

Commands run by agent:
read-only `sed`, `nl -ba ... | sed -n`, `rg -n/-F`, and `rg --files`;
no build.
