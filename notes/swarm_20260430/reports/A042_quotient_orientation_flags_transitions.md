# A042 report: quotient-orientation criterion across flags and transitions

Runtime id: `019ddbee-c64b-7ed0-9abd-eac03670f40d`.
Nickname: Lagrange.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Quotient-orientation descent across object, extension, mixed, wrapped,
two-step flag, overlap, Thom-Sebastiani, and \(R'\to R\) transition
strata.

## Verdict

No fatal globalization found. The manuscript treats quotient orientation
as a finite Cech-Borel descent criterion, not as a consequence of one
\(E[2]\) or rank-one stratum calculation. Status remains conditional and
open, not constructed.

## Proof / Failure Mode Checked

Required pieces are separated.

Ordinary gerbe:
\[
\alpha^{\mathrm{red}}_{R,S}=w_2(\mathscr D_{R,S})
=c_1(\mathscr D_{R,S})\bmod2\in H^2(S;\mathbb F_2).
\]
Anchor: `main.tex:13482`.

Connected \(BE\):
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,
\]
so \(H^1(BE)=0\),
\[
H^2(BE)=\mathbb F_2u_1\oplus\mathbb F_2u_2,\qquad
\alpha^{E,\mathrm{free}}=a_1u_1+a_2u_2.
\]
Anchor: `main.tex:3317`.

Finite stabilizer Borel class:
\[
\widetilde\beta^H_{R,S}\in H^2_H(S;\mathbb F_2),
\]
with point-stabilizer edge class valid only after mixed Borel terms,
stabilizer action, and differentials vanish. Anchors:
`main.tex:13513`, `main.tex:4144`.

Degree-one finite linearization:
after the degree-two class is killed, linearizations form an
\(H^1\)-torsor and the zero character is extra data. For \(E[2]\),
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,\quad
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2),
\]
and
\[
\lambda=\lambda_1x_1+\lambda_2x_2,\quad
\rho_1=\lambda_1,\ \rho_2=\lambda_2,\ \rho_3=\lambda_1+\lambda_2.
\]
Anchor: `main.tex:13525`.

Higher even \(N\):
\[
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
\]
\[
\beta=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2,
\]
with \(A_{12}^{(N)}\) invisible to cyclic tests. Anchor:
`main.tex:13544`.

Overlap, correspondence, flag, and transition compatibility are required
explicitly. Anchors: `main.tex:13575`, `main.tex:13623`,
`main.tex:4180`.

Thom-Sebastiani is separate from orientation descent:
\(\mu^{\mathrm{or}}_{R,e}\) and two-step flag coherences are part of the
finite quotient-orientation system. Anchor: `main.tex:4154`.

## Soft Vulnerabilities

`main.tex:13623` compresses overlap/correspondence/flag/transition
gluing into "total degree-one defect." This is acceptable as criterion
language, but a future patch should name the separate defects
explicitly.

`main.tex:13685` says \(Q_{E,R}\) is "obtained by applying" equivariant
BM chains and orientation descent. Read with `main.tex:13641`, this is
conditional; alone it risks hiding the quotient pseudofunctor package
flagged by A033.

`main.tex:13036` starts from "reduced orientation lines fixed." Safe only
as supplied data after the gerbe/descent package, not as a gerbe-first
construction.

## Recommendation

Claim status: conditional-safe criterion. Do not promote to constructed
O1/O1+/O2 theorem. Preserve the present separation; future healing
should name the Cech-Borel overlap/correspondence/flag/transition defect
tuple and make \(Q_{E,R}\) pseudofunctoriality visibly supplied.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, `ls`, and
`git status --short`; no build.
