# A026 report: d-critical structures, vanishing cycles, and orientation data

Runtime id: `019ddbdd-dda4-74c3-b270-40967a988f42`.
Nickname: Erdos.
Status: completed.
Files changed by agent: none.

## Verdict

No fatal conflation found. The finite retained Hall theorem mostly
separates retained boundedness from the extra geometric package:
\(\mathrm{Bnd}\), \(\mathrm{dCrit}\), \(\mathrm{RedOr}\), and
\(\mathrm{Six}\) are named as supplied data at `main.tex:13022`, and
the proof explicitly says the Hall source exists only after those
inputs are supplied at `main.tex:13186`.

## Valid Attacks

1. Retained boundedness proves at most finite-type retained slices. It
does not imply quasi-smoothness, d-critical charts, BBDJS coefficients,
orientation lines, or compact-support six-functor admissibility. A002
states this at
`notes/swarm_20260430/reports/A002_retained_liu_boundedness.md:57`.

2. The local formula
\[
o_{R,c}:=\det \operatorname{Ext}^{1}_{\mathrm{red}}(A,A)^{-1}
\]
at `main.tex:13073` is safe only as a Darboux-chart representative
after \(\mathrm{RedOr}\) has supplied a global square-root/gerbe
section. It should not be read as a construction of global orientation
data. A005 flags the same risk.

3. BBDJS vanishing cycles require an oriented d-critical locus. The
manuscript states this correctly at `main.tex:485` and `main.tex:524`.
Primary check: Bussi-Brav-Joyce-Dupont-Szendroi construct the perverse
sheaf for an oriented d-critical locus, not from boundedness alone.
Source: `arXiv:1211.3259`.

4. Joyce-Upmeier orientation data is square-root data with
exact-sequence/direct-sum compatibility on CY3 moduli. It does not
automatically give the reduced \(K3\times E\) quotient,
cosection-reduced orientation, finite-stabilizer linearization, or Weyl
monodromy. The manuscript keeps these in \(\mathrm{RedOr}\),
\((\mathrm{D0\text{-}Q})\), and the quotient-orientation criterion:
`main.tex:10702`, `main.tex:4107`, `main.tex:13454`. Source:
`arXiv:2001.00113`.

5. Six-functor operations are supplied. The text uses exceptional
\(q_!\), not proper \(q_*\), and explicitly says ordinary properness of
the raw exact-triangle map is not asserted: `main.tex:11381`,
`main.tex:13289`.

## Assumption Ledger

\(\mathrm{Bnd}\):
finite-type/quasi-smooth retained derived Artin stacks. Supplied at
`main.tex:13026`; partially reducible by the finite-stack proposition
only after quasi-smooth object stacks and bounded Ext amplitudes are
assumed at `main.tex:13235`.

\(\mathrm{dCrit}\):
PTVV shifted symplectic plus BBDJS d-critical charts. Supplied at
`main.tex:13033`. PTVV gives ambient shifted symplectic structures for
derived moduli under CY hypotheses, not the retained atlas by itself.
Source: `arXiv:1111.3209`.

\(\mathrm{RedOr}\):
reduced orientation lines, quotient descent, Joyce-Upmeier transports.
Supplied, not proved. Open globally at `main.tex:2548` and
`main.tex:2995`.

\(\mathrm{Six}\):
compact-support pull-push and Thom-Sebastiani coherence. Supplied at
`main.tex:13039`, reused at `main.tex:13637`.

Gerbe-first critique:
useful architecture, not primary proof. The processed critique at
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:38526`
and `materials/processed/2026-04-30-attack-whitepaper-analysis.txt:41286`
proposes twisted state spaces on orientation gerbes; the manuscript
instead demands ordinary oriented finite stages. That is conservative
and currently safer.

## Residual Obligations

Compute actual reduced orientation gerbes and finite-stabilizer
characters on every retained object, extension, mixed/wrapped, and flag
stratum. Prove or keep supplied the retained quasi-smooth d-critical
atlas. Prove six-functor admissibility and finite compact-support
realization for every retained correspondence. Tighten wording around
the Darboux-chart orientation line so it cannot be read as a global
construction.

Commands run by agent:
read-only `sed`, `rg`, `nl -ba | sed -n`; read-only `curl` to arXiv
source/abstract pages for BBDJS, PTVV, Joyce-Upmeier; no build, tests,
or git mutation.
