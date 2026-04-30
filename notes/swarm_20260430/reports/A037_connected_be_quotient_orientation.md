# A037 report: connected \(BE\) quotient-orientation firewall

Runtime id: `019ddbea-5a76-7fb1-9e81-7841cc68ea6e`.
Nickname: Einstein.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Connected \(BE\) quotient-orientation firewall: whether ordinary
\(E\)-translation invariance, \(E\)-linearization, Borel obstruction
classes, and actual descent of reduced orientation lines/gerbes are
correctly separated.

## Verdict

The firewall mostly holds. Keep every quotient-orientation statement
conditional. Do not promote finite stabilizer tests, OP scalar signs, or
ordinary translation invariance to actual reduced \(E\)-quotient
orientation descent.

## Failure Mode / Proof

Connected \(E\) and finite \(E[N]\) are different obstruction spaces. For
\(E^{\mathrm{top}}\simeq T^2\),
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,
\]
so
\[
H^1(BE;\mathbb F_2)=0,\qquad
H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2.
\]
Thus there is no connected \(H^1\)-character, but there is still a
degree-two connected quotient class
\[
\alpha^{E,\mathrm{free}}=a_1u_1+a_2u_2.
\]
Anchors: `main.tex:3278`, `main.tex:3317`, `main.tex:3439`.

For \(E[2]\cong(\mathbb Z/2)^2\),
\[
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\quad |x_i|=1,
\]
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,\qquad
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2).
\]
After \(\beta=0\), a separate degree-one character remains:
\[
\lambda=\lambda_1x_1+\lambda_2x_2,\qquad
\rho_1=\lambda_1,\ \rho_2=\lambda_2,\ \rho_3=\lambda_1+\lambda_2.
\]
The \(r_i\) are degree-two gerbe bits; the \(\rho_i\) are degree-one
linearization bits. They cannot be identified. Anchors:
`main.tex:3482`, `main.tex:3800`.

For even \(N\ge4\), with \(2^a\parallel N\),
\[
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
\]
\[
\beta=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
\]
Order-two cyclic tests do not see \(A_{12}^{(N)}\), and the residual
character
\[
\lambda^{E,N}=\lambda_1^{(N)}x_1+\lambda_2^{(N)}x_2
\]
must be checked on full two-primary generators. Anchor: `main.tex:3902`.

## Local Anchors

O1 correctly defines descent as ordinary gerbe, connected \(BE\)-class,
finite Borel classes, and zero finite \(H^1\)-characters:
`main.tex:1166`.

Translation invariance is explicitly not enough:
`main.tex:1303`, `main.tex:3434`.

Point-stabilizer classes are valid only after mixed Borel terms,
stabilizer action, and spectral-sequence differentials vanish:
`main.tex:1200`, `main.tex:13513`, `main.tex:4144`.

Actual finite-stage descent requires compatible null-trivializations on
strata, correspondences, flags, and transitions:
`main.tex:4107`, `main.tex:4178`.

Weyl transport is separate: kill \(c_o\) and quotient torsor defects
\(\omega_{i,\mathcal C}\): `main.tex:2167`.

## Proposal-Only Heal

Add or preserve one sentence wherever \(\alpha^{E,\mathrm{free}}\) is
used: it is the actual Borel/edge class of the equivariant reduced
determinant complex, not a consequence of \(H^1(BE)=0\) or ordinary
translation invariance. If \(H^1(S)\neq0\), the connected-free spectral
sequence should be read at the \(E_\infty\)/edge level, with incoming
\(d_2:E_2^{0,1}\to E_2^{2,0}\) ambiguity ruled out or included in the
computed class.

## Status Recommendation

Conditional-safe criterion, not a constructed O1 theorem. Actual descent
remains open until all listed classes and compatibilities are computed.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, and `git status --short`; no
build, staging, or mutation.
