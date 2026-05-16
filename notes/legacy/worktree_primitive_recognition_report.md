# Worktree primitive recognition report

Date: 2026-04-28.

## Claim attacked

The attacked shortcut was:
\[
\text{Gritsenko--Nikulin target denominator data}
\quad\Longrightarrow\quad
\text{compact Hall primitive recognition}.
\]

The shortcut is false.  The GN/Kac presentation supplies the target
Borcherds--Cartan datum, denominator algebra, signed root
supermultiplicities, and target-side low-degree constants.  A compact
\(K3\times E\) Hall source must separately supply generators, parities,
relations, Hopf pairing, radical quotient, no-extra-relations, completed
PBW, and full parity dimensions.

## Files changed

- `main.tex`
- `notes/worktree_primitive_recognition_report.md`

## Theorem status

The primitive recognition theorem is now explicitly presentation-level
and conditional.  It first fixes the imported target
\(\mathscr B_{\Delta_5}\), then lists the compact source hypotheses
\((S1)\)--\((S9)\).  Under those hypotheses,
\[
P_X^{\Pi,\mathrm{red}}
\cong
\mathcal A_{\mathrm{den}}
=\mathfrak g_{\Delta_5}
\]
as Gram-graded Lie superalgebras, with denominator
\(64^{-1}\Delta_5(2Z)\).  Without those hypotheses the determinant fixes
only a Grothendieck-class shadow.

## Exact constants and relations inscribed

- Target real Cartan matrix:
\[
((\delta_i,\delta_j))=
\begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}.
\]
- Degree map:
\[
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}
=n\delta_1+m\delta_2+(n+m-l)\delta_3.
\]
- Real Serre exponent for \(i\ne j\):
\[
(\operatorname{ad}e_i)^3e_j=0.
\]
- Chevalley constants:
\[
[h_i,e_j]=A_{ij}e_j,\quad
[h_i,f_j]=-A_{ij}f_j,\quad
[e_i,f_j]=\delta_{ij}h_i.
\]
- First real commutator constants, for
\(\{i,j,k\}=\{1,2,3\}\):
\[
E_{ij}=[e_i,e_j],\quad E_{ji}=-E_{ij},
\]
\[
[h_i,E_{ij}]=[h_j,E_{ij}]=0,\quad
[h_k,E_{ij}]=-4E_{ij},
\]
\[
[f_i,E_{ij}]=2e_j,\quad
[f_j,E_{ij}]=-2e_i,\quad
[f_k,E_{ij}]=0.
\]
- Height-three real-string constants:
\[
E_{iij}=[e_i,E_{ij}],\quad
[e_i,E_{iij}]=0,\quad
[f_i,E_{iij}]=2E_{ij},\quad
[f_j,E_{iij}]=0.
\]
- Isotropic primitive split:
\[
\smult(\delta_i+\delta_j)=10=1+9,\qquad
\tau(t(\delta_i+\delta_j))=9\quad(t\ge1),
\]
with one even real-real commutator direction and nine even GN isotropic
simple directions.
- Orthogonality for isotropic simple directions:
\[
[e_i,u_{ij,r}]=[e_j,u_{ij,r}]=0,\qquad
[f_i,u_{ij,r}]=[f_j,u_{ij,r}]=0.
\]
- First unresolved compact test channel:
\[
\delta_{123}=\delta_1+\delta_2+\delta_3,\qquad
\gamma=(1,1,1),\qquad
\smult(\delta_{123})=f(1,1)=-64.
\]
The compact source must refine this to parity-homogeneous bases
\[
v^{\overline0}_1,\ldots,v^{\overline0}_{d_0},\qquad
v^{\overline1}_1,\ldots,v^{\overline1}_{d_1},\qquad d_0-d_1=-64,
\]
and compute Hall constants
\[
[e_k^X,u^X_{ij,r}]
=\sum_a C^{\overline0}_{k;ijr,a}v^{\overline0}_a.
\]
It must also verify \(T_1^X+T_2^X+T_3^X=0\), the Serre consequences, and
the Hopf-radical quotient.

## Remaining obstruction

Construct the compact Hall/factorization source and pass the
presentation test.  The first finite test is the
\(\delta_1+\delta_2+\delta_3\) channel: the GN product gives signed
size \(-64\), but not the compact basis, parity split, Hall constants,
Jacobi/Serre verification, completed Hopf pairing, or radical quotient.

## Commands run

- `pwd`
- `git branch --show-current`
- `sed -n` reads of the local rectify skill, `CLAUDE.md`, `AGENTS.md`,
  assigned notes, appendix, and targeted `main.tex` regions.
- `rg` scans for primitive recognition, low-degree brackets, PBW,
  radical, Hopf pairing, theorem references, and new anchors.
- `git status --short`
- `git diff --check`
- targeted fixed-string `rg` scans for `thm:primitive-recognition`,
  `prop:low-degree-denominator-brackets`, `def:imaginary-simple-roots`,
  `P_X^{\Pi,\mathrm{red}}`, and `delta_{123}`
- `make`
- `git add main.tex out/main.pdf notes/worktree_primitive_recognition_report.md`
- `git diff --cached --stat`
- `git diff --cached --check`

The whitespace check passed and `make` rebuilt `out/main.pdf`
successfully.
