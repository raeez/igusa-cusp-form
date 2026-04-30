# A045 report: type-II wall \(\delta_3\) local atom

Runtime id: `019ddbf0-786c-7d01-80a4-1f110ec7a879`.
Nickname: Hubble.
Status: completed.
Files changed by agent: none.

## Claim Attacked

The \(\delta_3\) Type-II wall atom is already constructed and proves the
local O2/Pfaffian sign.

## Verdict

Not theorem-level. The theorem-safe content is target-side and
conditional. The \(\delta_3\) geometric atom is only a candidate local
model.

## What Is Safe

\(\delta_3=f_3\), Gram label
\[
(n_{\rm Bch},\ell_{\rm Bch},m_{\rm Bch})=(0,-1,0),
\]
norm \(2\), pairings \((\delta_i,\delta_j)=-2\) for \(i\ne j\).
Verified by `main.tex:1843` and `compute/verify_lattice.py`.

Automorphic target:
\[
d^{\rm aut}_{\delta_3}=f(0,-1)=1,\qquad
\nu_{\Delta_5}(s_{\delta_3})=-1.
\]
This checks the target divisor/sign only; it is not Hall orientation.
Anchor: `main.tex:1965`.

Conditional local model:
if the O2 residual vanishes, then
\[
K^{\rm nor}_{\delta_3,R}\simeq
[\mathbb R\xrightarrow{u_{\delta_3,R}}\mathbb R],\quad
\operatorname{Pf}=\upsilon_{\delta_3,R}u_{\delta_3,R},\quad
s_{\delta_3}(u)=-u,
\]
with \(s_{\delta_3}(\upsilon)=\upsilon\), hence local sign \(-1\).
Anchor: `main.tex:1040`.

## Candidate-Only

The critique proposes
\[
Y_{\delta_3}=C_1\times\{0_E\}\cup\{p\}\times E
\]
with one node and line bundles of degrees \(a_3+b_3=0\), so
\(\chi=-1\) and \((h-1,\chi,d-1)=(0,-1,0)\). Anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44561`.

The local Koszul calculation gives an unreduced rank-one normal
crossing:
\[
R=\mathbb C[[x,y,t]],\quad C_A:(x,t),\quad C_B:(y,t-x),
\]
\[
\operatorname{Ext}^1(\mathcal O_{C_A},\mathcal O_{C_B})\cong\mathbb C,
\quad
\operatorname{Ext}^2(\mathcal O_{C_A},\mathcal O_{C_B})\cong\mathbb C.
\]
This supports a candidate \(\operatorname{Crit}(uv)\), not a reduced
compact O2 chart. Anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44861`.

## Failure Modes

Local/wrapped color:
\((0,-1,0)\) has \(m_{\rm Bch}=0\), but \(m_{\rm Bch}=0\) is not
locality. On the D6/OP branch \(m_{\rm Bch}=d_E-1\), so the proposed
\(\delta_3\) atom has \(d_E=1>0\). It is mixed/wrapped, not
projection-finite local. Anchors: A031 and A014.

Semistability and wall equality:
not proved. Need Liu-heart membership, \(\sigma_{s,t}\)-semistability,
stable factors in adjacent chambers, and exact equality of the stability
wall with \(u_{\delta_3}=0\). Anchor: `main.tex:13306`.

Reduced Ext normal form:
not proved. Need reduced self-Ext, trace/K3 semiregularity quotient,
tangent/normal splitting, nonzero reduced Kuranishi pairing, and
equivariant real Morse normal form.

Invariant unit:
not proved. A nontrivial unit character changes the sign and belongs to
O1+. Anchor: `main.tex:950`.

Quotient orientation:
not proved. Need \(\alpha^{\rm red}\), \(\alpha^{E,\rm free}\),
\(\widetilde\beta^H\), \(\lambda^H\), anchor character, and
overlap/transition compatibility. Anchor: `main.tex:13454`; see A041.

Pfaffian rank:
\(N_{\delta_3}^{\rm Pf}=1\) is theorem-safe only inside the
formal/conditional crossing. For the compact reduced wall atom it
remains candidate-only. AP-CY388 is exactly this firewall.

## Comparison With \(\delta_1,\delta_2\)

\(\delta_2\) is explicitly wrapped with \(d=2\), and the manuscript
proves it cannot be projection-finite. The proposed \(\delta_3\) atom
has \(d=1\), so it is less visibly wrapped but still positive elliptic
degree in the D6 branch. Thus \(\delta_3\) follows the \(\delta_1\)
pattern, not the projection-local pattern: a reducible local/wrapped
candidate plus the same unreduced node calculation, with all O2/hybrid
obligations still open.

Commands run by agent:
read-only `sed`, `nl`, `rg`, `find`, `git status --short`,
`git diff --stat`; `PYTHONDONTWRITEBYTECODE=1 python3
compute/verify_lattice.py` passed.
