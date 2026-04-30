# A019 report: Gram cocycle proof and cohomological status

Runtime id: `019ddbd9-87e4-73f3-b36a-b05e0c2b9e51`.
Nickname: Feynman.
Status: completed.
Files changed by agent: none.

## Verdict

No fatal formula defect. For \(c=(Q,P)\) and \(c'=(Q',P')\),
\[
\Pi_X(c+c')-\Pi_X(c)-\Pi_X(c')
=(Q\!\cdot\!Q',\,Q\!\cdot\!P'+Q'\!\cdot\!P,\,P\!\cdot\!P')=B(c,c').
\]
Thus \(B\) is symmetric bilinear, \(\delta B=0\), and
\[
B(c,c)=(Q^2,2Q\!\cdot\!P,P^2)=2\Pi_X(c).
\]
This is pure lattice polarization, not orientation, parity, Bott, or
Pfaffian data.

## Cohomological Status

With the manuscript convention
\[
(\delta q)(c,c')=q(c)+q(c')-q(c+c'),
\]
one has \(B=-\delta\Pi_X\). Hence \([B]=0\) in ordinary group
cohomology. The extension
\(\widehat\Gamma_X=\Gamma_X^{\rm phys}\oplus_B\Gamma_{\rm gram}\) is
split by \(s(c)=(c,\Pi_X(c))\), and
\((c,T)\mapsto(c,T-\Pi_X(c))\) identifies it with the direct sum. The
real obstruction is not nontrivial extension cohomology; it is that raw
placement \(i_0(c)=(c,0)\) is not additive for bracket degrees, and no
linear cochain trivializes the quadratic defect.

Main anchors:
`main.tex:4441`, `main.tex:4707`, `main.tex:4733`, `main.tex:4877`,
`main.tex:4898`, `main.tex:4932`.

## Firewalls

The orientation/Bott firewall holds. The explicit firewall is at
`main.tex:2585`; grep found no positive use of Bott or orientation to
prove \(B(c,c)=2\Pi_X(c)\). Later \(\Theta_\Pi\)-descent requires
compatibility with orientation and cyclic data, but as supplied
chain-level structure, not as the proof of the lattice identity.

Anchors:
`main.tex:8656`, `main.tex:8745`, `main.tex:9232`, `main.tex:9470`,
`main.tex:10845`.

## Notation Risks

The line `main.tex:9850` writes \([B]=[B_{\mathrm{ch}}]\). Since
\([B]=0\) earlier and
\(B_{\mathrm{ch}}=d_{\mathrm{Hoch}}\Theta_\Pi\) when the datum is
supplied, this should be rewritten as a degree-shadow/trivialization
statement, not as a cohomology-class equality.

Suggested replacement:
\[
B_{\mathrm{ch}}\text{ has degree shadow }B,\quad
d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}
\]
when \(\Theta_\Pi\) is supplied; the negative-cyclic lift maps to that
Hochschild representative.

Minor wording risk: "ordinary additive cochains" can be read as
additive homomorphisms. Safer wording is "ordinary cochains on the
additive group" at `main.tex:4454`, `main.tex:4919`, and
`main.tex:8664`.

## Cross-Checks

A003 confirms the cocycle and fixed-lift no-go boundary:
`notes/swarm_20260430/reports/A003_normal_ordering.md:17`. The guide
sections 4--5 state the right firewall:
`notes/attack_whitepaper_analysis_20260430_guide.md:127`. CYQG
AP-CY359/AP-CY361/AP-CY386 agree on Gram-vs-Hall grading and
fixed-lift scope. AP-CY393 remains a nearby notation warning: the data
entry \((D_X)\) collides with \(\mathcal D_X,D_5,\mathfrak D_X\);
A014 also flags this.

## Residual Obligations

Rewrite the \([B]=[B_{\mathrm{ch}}]\) remark; consider adding "split
as an abstract extension, nontrivial only relative to raw placement"
after the first \(\oplus_B\) display; preserve AP-CY386 by never
upgrading the fixed-lift raw no-go into a fibre-summed raw no-go.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, `git status --short`, and
`git diff --stat`; no build.
