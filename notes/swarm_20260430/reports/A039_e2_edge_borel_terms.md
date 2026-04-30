# A039 report: \(E[2]\) degree-two edge classes and global Borel terms

Runtime id: `019ddbec-5a00-70d1-8ba2-14f51cbec6b5`.
Nickname: Zeno.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Whether the \(E[2]\) degree-two restrictions \(r_1,r_2,r_3\) are being
promoted into a global quotient-orientation theorem.

## Verdict

The current manuscript treats them correctly as point-stabilizer edge
tests, not as a global quotient-orientation theorem.

## Failure / Proof

The real obstruction is
\(\widetilde\beta^H_{R,S}\in H^2_H(S;\mathbb F_2)\), filtered by the
Borel spectral sequence. The edge class in \(H^2(BH;\mathbb F_2)\) is
legitimate only after the ordinary \(E_\infty^{0,2}\) term, mixed
\(E_\infty^{1,1}\) term, stabilizer action on \(H^\bullet(S)\), and
total-degree-two differentials have been killed: `main.tex:1200`,
`main.tex:13513`.

For \(E[2]\cong(\mathbb Z/2)^2\),
\[
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\quad |x_i|=1,
\]
and
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2.
\]
Restrictions to
\(\langle e_1\rangle,\langle e_2\rangle,\langle e_1+e_2\rangle\) give
\[
r_1=b_{20},\quad r_2=b_{02},\quad r_3=b_{20}+b_{11}+b_{02},
\]
hence
\[
b_{20}=r_1,\quad b_{02}=r_2,\quad b_{11}=r_1+r_2+r_3.
\]
The mod-2 restriction matrix has determinant \(1\), so \(r_i=0\) is
equivalent to \(\beta=0\) only for the \(N=2\) edge class:
`main.tex:3518`.

The manuscript explicitly separates this from the residual
\(H^1\)-linearization character:
\[
\lambda=\lambda_1x_1+\lambda_2x_2,\quad
\rho_1=\lambda_1,\quad \rho_2=\lambda_2,\quad
\rho_3=\lambda_1+\lambda_2.
\]
Thus \(r_i\) and \(\rho_i\) live in different degrees:
`main.tex:3817`.

For even \(N\ge4\), with \(2^a\parallel N\),
\[
H^2(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle,
\]
\[
\beta=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
\]
Cyclic restrictions miss \(A_{12}^{(N)}\), so the \(E[2]\) test cannot
prove even-\(N\) descent: `main.tex:3925`, `main.tex:3993`.

The stabilizer action is not silently discarded. The current theorem
notes that pure inner conjugation has determinant one, but the retained
line still includes translation pullback, trace/semiregularity
reductions, anchors, framings, Thom-Sebastiani transports, and flag
coherences; their sign is \(\lambda^H_{R,S}\): `main.tex:13585`.

## Claim-Status Recommendation

Keep the current claim conditional. The safe theorem is:
\(r_1=r_2=r_3=0\) kills the \(N=2\) point-stabilizer degree-two edge
class after the Borel filtration has reduced to that edge. It does not
construct (O1), does not kill mixed Borel terms, does not kill residual
\(H^1\)-characters, and says nothing about \(A_{12}^{(N)}\) for
\(N\ge4\).

Commands run by agent:
read-only `sed`, `nl`, `rg`; small Python GF(2) determinant check;
`git status --short`; no build or mutation.
