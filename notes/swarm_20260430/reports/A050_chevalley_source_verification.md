# A050 report: Chevalley relations source verification

Runtime id: `019ddbf9-01d8-7563-bd9c-dfc9ee7d3fe8`.
Nickname: Sartre.
Status: completed.
Files changed by agent: none.

## Claim Attacked

The retained compact source primitives currently verify the real-root
Chevalley relations and Cartan action for \(\mathfrak g_{\Delta_5}\),
rather than importing those relations from the
Gritsenko-Nikulin/Kac target.

## Verdict

Not proved. The manuscript has the right conditional firewall: target
Chevalley data are imported; compact source recognition begins only after
explicit source matrices are supplied and checked.

Source primitives alone are insufficient. Even with correct \(1|0\)
real-root spaces and signed dimensions, the zero bracket, wrong Cartan
action, or rescaled \([e_i,f_i]\) constants give the same determinant
shadow and fail Chevalley.

## Failure Mode

The target relations are explicit:
\[
[h_i,e_j]=A_{ij}e_j,\quad [h_i,f_j]=-A_{ij}f_j,\quad
[e_i,f_j]=\delta_{ij}h_i,
\]
with
\[
A=((\delta_i,\delta_j))=
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix}.
\]
These are target GN/Kac relations in `main.tex:14723`. The source
theorem requires them as compact Hall bracket checks, not as consequences
of multiplicities: `main.tex:12627`.

The source matrix proposition defines how matrices would be computed
from compact Hall correspondences, but it does not display evaluated
\(W_{\le3}\) source matrices: `main.tex:13836`. The comparison maps
explicitly assume \(A_{\gamma,\bar p}\) and matrix compatibility with
target brackets/coproducts/pairings: `main.tex:14012`. Thus the current
source-to-target Chevalley verification is conditional.

## Exact Matrices Needed

For every \(\beta\in W_{\le3}\cup(-W_{\le3})\cup\{0\}\) and parity
block:

- Source bases \(P^X_{R,\beta,\bar p}\), including \(H=P^X_{R,0}\),
  \(e_i^X\in P^X_{\delta_i}\), \(f_i^X\in P^X_{-\delta_i}\).
- Product matrices \(M_{\alpha,\beta}\).
- Bracket matrices
  \[
  B_{\alpha,\beta}
  =M_{\alpha,\beta}-(-1)^{|x||y|}M_{\beta,\alpha}\tau.
  \]
- Pairing matrices \(G_{\beta,\bar p}\).
- Radical blocks
  \[
  K_{\beta,\bar p}=\ker G_{\beta,\bar p}\cap
  \ker G_{-\beta,\bar p}^{t}.
  \]
- Splittings \(P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus
  L_{\beta,\bar p}\) and quotient maps \(Q_{\beta,\bar p}\).
- Coproduct matrices \(D^{\mu,\nu}_\rho\).
- Source-to-target identifications
  \(A_{\beta,\bar p}:L_{\beta,\bar p}\to
  \mathfrak g_{\Delta_5,\beta,\bar p}\), with \(A_0=\iota_H\).
- Transition matrices preserving \(K\), \(G\), \(D\), bracket rows, and
  PBW filtrations.

Primary criterion: `main.tex:15268`. NO7 protocol: `main.tex:15373`.

## Finite \(W_{\le3}\) Checks Needed

The first window has target dimensions:
\[
\delta_i:1|0,\quad \delta_i+\delta_j:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\delta_{123}:29|93.
\]
Anchor: `main.tex:15004`.

The source must check, after quotient by \(K\):

- Cartan rows: \([h,h']=0\),
  \([h_i,e_j]=A_{ij}e_j\), \([h_i,f_j]=-A_{ij}f_j\).
- Chevalley rows: \([e_i,f_j]=\delta_{ij}h_i\).
- Real-root brackets:
  \(B_{\delta_i,\delta_j}=c_0\),
  \(B_{\delta_j,\delta_i}=-c_0\).
- Adjacent isotropic rows killing \(u_{ij,r}\).
- Complementary mixed maps \([e_k,u_{ij,r}]\) into the \(29\)-dimensional
  even \(\delta_{123}\)-block.
- Jacobi \(T_1+T_2+T_3=0\).
- Hopf radical descent:
  \(QB(P\otimes K)=QB(K\otimes P)=0\),
  \((Q\otimes Q)DK=0\).
- No-extra-relations and PBW associated-graded isomorphism.

## Claim Status Recommendation

Retain as a conditional finite source matrix recognition criterion.

Do not state that retained source primitives verify Chevalley or Cartan
action until \(M,D,B,G,K,Q,A_\beta\) are explicitly supplied from compact
Hall geometry and the rows above pass.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, `git status --short`;
`python3 compute/verify_lattice.py`; `python3 compute/verify_square_root.py`.
The computations confirmed target finite-window arithmetic, not compact
source matrices.
