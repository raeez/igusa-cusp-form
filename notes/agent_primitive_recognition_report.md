# Agent 6 Primitive Recognition Report

Date: 2026-04-28.

## Claim Attacked

The attacked shortcut was:
\[
H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)
\quad\hbox{has signed dimensions } f(nm,l)
\quad\Longrightarrow\quad
H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)
\cong \mathfrak g_{\Delta_5}.
\]

The shortcut fails.  The determinant and the Gritsenko--Nikulin
denominator identity determine signed root supermultiplicities in the
fixed target datum.  They do not determine compact Hall brackets, parity
dimensions, simple primitive representatives, the Hopf pairing, the
closed radical, no-extra-relations, or completed PBW.

## Files Changed

- `main.tex`
- `notes/agent_primitive_recognition_report.md`
- `out/main.pdf` was rebuilt by `make`.

## Exact Relations And Constants Inscribed

- Target presentation:
  \[
  G(\mathscr B_{\Delta_5})
  =\widehat{\mathfrak F}(\mathscr B_{\Delta_5})/
  \overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}}
  =\mathfrak g_{\Delta_5}.
  \]
- Compact recognition object:
  \[
  P_X^{\Pi,\mathrm{red}}
  =
  H^0\Prim_{\mathrm{prot}}(\overline\Pi_{X,*}^{\Theta}\mathcal F_X)/
  \overline{\operatorname{Rad}\langle\,\cdot\,,\,\cdot\,\rangle_X}.
  \]
- Real Cartan matrix:
  \[
  ((\delta_i,\delta_j))=
  \begin{pmatrix}2&-2&-2\\-2&2&-2\\-2&-2&2\end{pmatrix}.
  \]
- Degree and norm:
  \[
  \alpha(n,l,m)=n\delta_1+m\delta_2+(n+m-l)\delta_3,\qquad
  (\alpha,\alpha)=-2(4nm-l^2).
  \]
- Real Serre exponent for \(i\ne j\):
  \[
  (\operatorname{ad}e_i)^3e_j=0.
  \]
- Low-degree denominator constants:
  \[
  [h_i,e_j]=A_{ij}e_j,\quad [h_i,f_j]=-A_{ij}f_j,\quad
  [e_i,f_j]=\delta_{ij}h_i,
  \]
  \[
  [f_i,[e_i,e_j]]=2e_j,\qquad [f_j,[e_i,e_j]]=-2e_i.
  \]
- Isotropic primitive accounting:
  \[
  \smult(\delta_i+\delta_j)=10=1+9,\qquad \tau(t(\delta_i+\delta_j))=9.
  \]
- First fatal compact-Hall gap:
  \[
  \smult(\delta_1+\delta_2+\delta_3)=f(1,1)=-64,
  \]
  but the constants \([e_k,u_{ij,r}]\) require a compact basis and parity
  split of that root space.

## Theorem Status

The recognition theorem is conditional and presentation-level.  If the
compact construction supplies normal-ordered bracket descent, Cartan
identification, simple primitive representatives, full parity dimensions,
Borcherds--Kac relations, continuous Hopf pairing, the same closed
radical quotient, no-extra-relations, generation, and completed PBW, then
\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}
\]
as Gram-graded Lie superalgebras, with denominator
\(64^{-1}\Delta_5(2Z)\).

What follows from Gritsenko--Nikulin: the target BKM datum, real roots,
imaginary simple-root multiplicity/parity convention, Weyl denominator,
and signed multiplicities.

What must be supplied by compact Hall theory: compact representatives,
actual Hall structure constants, full protected parity dimensions,
primitive projection, Hopf pairing, radical quotient, no-extra-relations,
and completed PBW.

## Remaining Obstruction

Construct the compact finite-first oriented Hall/factorization object on
\(K3\times E\), including mixed local/wrapped correspondences before the
reduced \(E\)-quotient, then compute the protected primitive brackets and
pairing-radical matrices at finite height.  The first concrete unresolved
test is the \(\delta_1+\delta_2+\delta_3\) channel: the denominator gives
signed size \(-64\), but not a compact basis, parity split, or constants
for \([e_k,u_{ij,r}]\).

## Commands Run

- `sed` reads of `CLAUDE.md`, `AGENTS.md`, the three 2026-04-28 notes, and
  assigned `main.tex` regions.
- `rg` audits for primitive-recognition, denominator, PBW, radical, and
  low-degree bracket anchors.
- `nl -ba` inspections of the primitive-recognition theorem, low-degree
  proposition, denominator-forgets lane, and synthesis theorem.
- `git status --short`
- `git diff --check -- main.tex`
- fixed-string `rg` checks for stale theorem item references and new
  presentation notation.
- `make`
