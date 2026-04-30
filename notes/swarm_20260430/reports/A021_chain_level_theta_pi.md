# A021 report: chain-level \(\Theta_\Pi\) residual

Runtime id: `019ddbd9-91d8-7fe0-94e5-0ad1eb7d6970`.
Nickname: Darwin.
Status: completed.
Files changed by agent: none.

## Verdict

The valid attack is chain-level only. The lattice identity is closed; the
Hall-chain \(\Theta_\Pi\) realization remains supplied/open. No fatal
place was found in the main \(\Theta_\Pi\) lane where the manuscript
claims the compact chain-level construction is proved unconditionally.

## Proved Lattice Boundary

\(\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c')\) and
\(B(c,c)=2\Pi_X(c)\):
`main.tex:4683`.

\(\widehat\Gamma_X\) with
\[
(c,T)\star(c',T')=(c+c',T+T'+B(c,c'))
\]
is associative, and
\[
\overline\Pi_X(c,T)=\Pi_X(c)-T
\]
is additive:
`main.tex:4707`, `main.tex:4932`.

The proof explicitly says this does not strictify Hall chains:
`main.tex:4898`.

Raw fixed-lift \(\Pi_X\)-descent no-go is theorem-level:
`main.tex:5042`.

## Surviving Residuals

HN finite-fibre/topology:
finite fibres are formal only after finite \(\widehat\Gamma_R\),
coefficient dg category, degree truncation, and transition maps are
supplied. The actual topological obstruction is
\[
\mathfrak o_\Theta^{top}
=(\mathfrak o^{fib},\mathfrak o^m,\mathfrak o^\Delta,
\mathfrak o^{\langle,\rangle}).
\]
Anchors:
`main.tex:8681`, `main.tex:9186`, `main.tex:9482`.

Hochschild/cochain identity:
\[
d_{\rm Hoch}\Theta_\Pi=B_{\rm ch}
\]
is formal for central translations, but its action on Hall
correspondence targets is extra data.
Anchors:
`main.tex:8723`, `main.tex:9079`, `main.tex:9375`.

Triple coherence/Jacobi:
the lattice shadow \(\delta B=0\) does not give the Hall flag pentagon;
\(\operatorname{Pent}_\Theta=0\) and \(\operatorname{Jac}_\Theta=0\)
remain finite chain conditions.
Anchors:
`main.tex:9100`, `main.tex:9386`, `main.tex:9551`.

Cyclic/Frobenius:
negative-cyclic lift is not obtained by forgetting to Hochschild;
Frobenius is not implied by pairing nondegeneracy or determinant data.
Anchors:
`main.tex:9135`, `main.tex:9530`, `main.tex:9666`.

Radical stability:
Frobenius gives the Lie-ideal half only. Coideal stability needs Hopf
adjointness, quotient tensor nondegeneracy, coproduct matrices, and
closed HN-compatible radical kernels.
Anchors:
`main.tex:9419`, `main.tex:9581`, `main.tex:9742`,
`main.tex:15373`.

## Theorem Boundary

Theorem \(\Theta_\Pi\) boundary is correct: it assumes supplied
\((P,E,O,\Theta,F,\mathrm{Cyc})\) and radical stability, then gives
descended \(H^0\) bracket and obstruction ledger:
`main.tex:8934`.

The manuscript explicitly says constructing \(\Theta_\Pi\) on the
reduced compact/wrapped sector is open:
`main.tex:10845`.

A003 agrees: \(\Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)}\) proves only the
degree-shadow identity, not Hall strictification/cyclic/Frobenius/radical
coideal:
`notes/swarm_20260430/reports/A003_normal_ordering.md:67`.

A006 agrees: \(W_{\le3}\) target arithmetic is not source matrices,
radical, PBW, or no-extra-relations:
`notes/swarm_20260430/reports/A006_wle3_source_matrices.md:8`.

## Status Recommendation

Keep lattice normal-ordering and raw-descent no-go as proved. Keep
chain-level \(\Theta_\Pi\), cyclic lift, Frobenius compatibility, finite
HN topology, and Hopf radical coideal as supplied/open until a finite
source fixture provides NO1--NO7, especially \(M,D,B,G,K,Q\) matrices and
transition-compatible radical kernels.

Commands run by agent:
read-only `rg`, `find`, `nl -ba | sed -n`, `wc -l`, and
`git status --short`. No build.
