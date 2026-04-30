# A038 report: finite \(BE[N]\) and stabilizer-character tests

Runtime id: `019ddbea-6386-7ec3-adca-8b814e8ad4ff`.
Nickname: Faraday.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Finite \(BE[N]\) and stabilizer-character tests prove
quotient-orientation vanishing.

## Verdict

No fatal upgrade found. The manuscript treats \(E[2]\) cyclic
restrictions as edge tests, not as global quotient-orientation
vanishing. It repeatedly requires the full Borel class, mixed terms,
stabilizer action, differentials, and residual \(H^1\)-characters to
vanish before (O1) or finite quotient orientation is concluded.

## Failure Mode Ruled Out

The dangerous false implication is
\[
r_1=r_2=r_3=0
\quad\Rightarrow\quad
\text{global quotient orientation}.
\]
The manuscript does not appear to assert this. It says this only kills
the \(N=2\) point-stabilizer degree-two class after reduction to
\(H^2(BE[2])\), and still requires connected \(BE\), Borel/Cech terms,
finite linearization characters, and higher even-\(N\) data.

## Core Local Anchors

Connected vs finite:
`main.tex:3317` states \(BE\simeq BT^2\),
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,
\]
so \(H^1(BE)=0\). `main.tex:3390` states
\(E[2]\cong(\mathbb Z/2)^2\),
\[
H^*(BE[2])=\mathbb F_2[x_1,x_2],\quad |x_i|=1.
\]

\(E[2]\) edge formula:
`main.tex:3518`
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,\quad
r_1=b_{20},\ r_2=b_{02},\ r_3=b_{20}+b_{11}+b_{02}.
\]
Joint cyclic restriction detects \(H^2(BE[2])\) in the \(N=2\)
point-stabilizer reduction.

Degree-one characters:
`main.tex:3578` says that after \(\beta^{E,E[2]}=0\), linearizations
form
\[
H^1(BE[2];\mathbb F_2)=\mathbb F_2\langle x_1,x_2\rangle;
\]
\[
\lambda=\lambda_1x_1+\lambda_2x_2,\quad
\rho_1=\lambda_1,\ \rho_2=\lambda_2,\ \rho_3=\lambda_1+\lambda_2.
\]
Trivial linearization requires \(\rho_1=\rho_2=\rho_3=0\). This is
separate from \(r_i=0\).

Even \(N\ge4\):
`main.tex:3902` says that for \(2^a\parallel N,\ a\ge2\),
\[
H^2(B(\mathbb Z/2^a)^2;\mathbb F_2)=
\mathbb F_2\langle y_1,x_1x_2,y_2\rangle,
\]
\[
\beta=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
\]
\(A_{12}^{(N)}\) is invisible on cyclic restrictions; \(E[2]\) bits do
not decide even \(N\ge4\).

Borel spectral sequence:
`main.tex:4023` and `main.tex:4144` say point-stabilizer formulas apply
only after mixed Borel terms, stabilizer action on
\(H^\bullet(S;\mathbb F_2)\), and total-degree-two differentials are
killed.

Finite-stage descent:
`main.tex:13454` is correctly conditional: quotient orientation descends
only after the Cech-Borel total obstruction splits and all ordinary,
connected-free, finite-stabilizer, linearization, overlap,
correspondence, flag, and transition defects vanish.

## Claim-Status Recommendation

Keep the current structure. Do not weaken the caveats. Preserve the
phrase-level firewall: "point-stabilizer edge calculation after Borel
terms vanish," never "edge restriction vanishing implies quotient
orientation."

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, and `git status --short`; no
edits, staging, reverts, or mutation.
