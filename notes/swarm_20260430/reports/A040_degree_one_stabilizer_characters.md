# A040 report: degree-one stabilizer characters and linearization tests

Runtime id: `019ddbec-6378-7502-9320-ff0d1be2b6aa`.
Nickname: Chandrasekhar.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Finite degree-one stabilizer characters \(\lambda^H\) might be killed by
connected \(E\)-translation invariance, by \(H^1(BE)=0\), or by
degree-two \(\beta\)-vanishing.

## Verdict

The attack fails against the current manuscript. The split is kept
correctly. The claim remains conditional/open as a construction target:
\(\lambda^H=0\) must be checked or supplied on the actual finite
stabilizers.

## Failure / Proof

Connected \(E\):
\(E^{\mathrm{top}}\simeq T^2\), so \(BE\simeq BT^2\),
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,
\]
hence \(H^1(BE;\mathbb F_2)=0\). This kills only connected-torus
degree-one characters. It leaves the connected degree-two class
\(\alpha^{E,\mathrm{free}}\). Anchor: `main.tex:3317`.

Finite stabilizers:
after
\(\widetilde\beta^H_{R,S}\in H^2_H(S;\mathbb F_2)\) is
null-trivialized, linearizations form an \(H^1(BH;\mathbb F_2)\)-torsor
after the Borel mixed terms and stratum terms are killed. The zero
character is extra data. Anchors: `main.tex:1214`, `main.tex:4144`,
`main.tex:4093`.

For \(E[2]=\langle e_1,e_2\rangle\),
\[
\lambda^{E[2]}=\lambda_1x_1+\lambda_2x_2,
\]
with \(\rho_1=\lambda_1\), \(\rho_2=\lambda_2\),
\(\rho_3=\lambda_1+\lambda_2\). Trivial linearization means
\(\rho_1=\rho_2=\rho_3=0\). The \(r_i\) are degree-two \(\beta\)-bits,
not \(\rho_i\). Anchors: `main.tex:1243`, `main.tex:3817`.

For even \(N\ge4\), \(2^a\parallel N\), the two-primary class is
\[
A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2,
\]
and the residual character is
\[
\lambda_1^{(N)}x_1+\lambda_2^{(N)}x_2.
\]
The order-two cyclic tests miss \(A_{12}^{(N)}\) and do not detect the
degree-one character. Anchor: `main.tex:3902`.

The manuscript explicitly does not infer \(\lambda^H=0\) from
translation invariance or \(\beta=0\). Anchors: `main.tex:3085`,
`main.tex:3433`, `main.tex:3602`, `main.tex:3697`.

## Strata Requirement

\(\lambda^H=0\) is required on every object, extension, mixed/wrapped,
and two-step flag stratum used by the quotient Hall source, with
overlap/correspondence/flag/transition compatibility. Anchors:
`main.tex:1538`, `main.tex:4107`, `main.tex:13454`, `main.tex:8544`.

## Recommendation

Keep the current conditional formulation. Do not promote
finite-stabilizer descent to a theorem until \(\widetilde\beta^H\) and
\(\lambda^H\) are computed on the actual retained strata and
transitions.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, and `git status --short`; no build or
mutation.
