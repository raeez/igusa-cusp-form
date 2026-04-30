# A020 report: raw/split/cochain notation for \(\Pi\) and \(\Theta_\Pi\)

Runtime id: `019ddbd9-7f40-7d10-9aa7-0a38f3da22e2`.
Nickname: Avicenna.
Status: completed.
Files changed by agent: none.

## Conflations Found

### `P_X^{\Pi,\mathrm{raw}}` is not raw

At `main.tex:12535` it is defined as
\[
H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)
=\overline\Pi_{X,*}^{\Theta}\widetilde P_X,
\]
that is, after normal-ordered \(\Theta\)-descent. This conflicts with
the actual raw pushforwards \(\Pi_{X,*}^{\mathrm{raw}}\) and
\(\Pi_{X,*}^{\mathrm{raw},L}\) at `main.tex:5023`. Safe replacement:
\(P_X^\Pi\) or \(P_X^{\Pi,\mathrm{preRad}}\); reserve "raw" for raw
\(\Pi_X\)-pushforward only.

### Root degree \(\beta\) is used as a Gram coordinate

In the target normal form, \(W\subset Q_+\), so \(\beta\in W\) is a
root-lattice degree. But `main.tex:14263` writes
\(\operatorname{pr}_3\overline\Pi_X(\beta)\), and `main.tex:14345`
writes \(\widehat c^0_\beta=(0,-\beta)\in\widehat\Gamma_X\). This is a
domain error unless \(\beta\) is silently replaced by its Gram preimage.
Safe notation:
\[
\gamma_\beta=(n,\ell,m)\in\Gamma_{\mathrm{gram}},\quad
\alpha(\gamma_\beta)=\beta,\quad
\widehat c^0_\beta=(0,-\gamma_\beta).
\]

### Physical and normal-ordered \(\Theta\) drift

Correct domains:
\[
\Theta_{\Pi,R}^{\mathrm{phys}}:\Gamma_X^{\mathrm{phys}}\to\mathsf{Pic}^{dg},
\quad
d_{\mathrm{Hoch}}\Theta_{\Pi,R}^{\mathrm{phys}}=B_{\mathrm{ch},R},
\]
whereas
\[
\widehat\Theta_{\Pi,R}:\widehat\Gamma_R\to\mathsf{Pic}^{dg},
\quad
d_{\mathrm{Hoch}}\widehat\Theta_{\Pi,R}=0.
\]
The manuscript states this cleanly at `main.tex:9530`, but later
shorthand drops `phys` in places such as `main.tex:10848`. Keep the
superscripts.

### Degree arrows are written like chain quasi-isomorphisms

At `main.tex:10865` the display
\[
\Theta_{(c,T),(c',T')}:\Pi_X(c+c')-T-T'-B(c,c')\to
(\Pi_X(c)-T)+(\Pi_X(c')-T')
\]
is a map between equal Gram degrees, not between coefficient objects.
The chain-level datum should be written as a natural quasi-isomorphism
between translated coefficient summands, or as the strict equality
\[
\overline\Pi_X((c,T)\star(c',T'))=
\overline\Pi_X(c,T)+\overline\Pi_X(c',T').
\]

### Fixed-lift raw no-go title is risky

The proof at `main.tex:5042` excludes strict fixed-lift raw
\(\Pi_X\)-descent, not all fibre-summed or chain-level raw
constructions. The later fence at `main.tex:5119` matches CYQG
AP-CY386. Retitle to "strict fixed-lift raw \(\Pi_X\)-pushforward
no-go."

### `B` has three unrelated meanings

Safe domains:
\[
B(c,c'):\Gamma_X^{\mathrm{phys}}\times\Gamma_X^{\mathrm{phys}}
\to\Gamma_{\mathrm{gram}},
\]
\[
B_{\mathrm{ch}}(c,c')=\mathsf T_{B(c,c')},
\]
and the source-matrix bracket
\[
B_{\alpha,\beta}:P_\alpha\otimes P_\beta\to P_{\alpha+\beta}
\]
at `main.tex:13879` and `main.tex:15282`. Rename the last to
\(\operatorname{br}_{\alpha,\beta}\) or \(C_{\alpha,\beta}\) in
source-matrix sections.

## Safe Table

\[
\Pi_X:\Gamma_X^{\mathrm{phys}}\to\Gamma_{\mathrm{gram}}
\]
is quadratic, not additive.

\[
i_0(c)=(c,0)
\]
is raw generator placement; \(\overline\Pi_X(i_0(c))=\Pi_X(c)\), and it
is not additive.

\[
s(c)=(c,\Pi_X(c))
\]
is the additive split section; \(\overline\Pi_X(s(c))=0\), and it is
not the Igusa-degree placement.

\[
\overline\Pi_X(c,T)=\Pi_X(c)-T
\]
is a homomorphism \(\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}\).

\[
\overline\Pi_{X,*}^{\Theta}
\]
is chain-level descent only after supplied finite Hall stages,
\(\Theta\)-coherences, cyclic lift, Frobenius, HN finite-fibre topology,
and Hopf-radical ideal/coideal checks.

## Residual Obligations

Fibre-summed raw descent remains unanalyzed. Chain-level \(\Theta_\Pi\)
on the reduced compact/wrapped sector remains open or supplied. Source
matrices \(M,D,G,K,Q\), source bases, radical coideal checks,
PBW/no-extra-relations, and transitions remain source-side obligations;
A003 and A006 correctly say target arithmetic does not supply them.

Commands run by agent:
read-only `sed`, `nl -ba | sed -n`, `rg -n/-F`, and
`git status --short`; no build.
