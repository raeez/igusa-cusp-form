# A085 relation-closed window status table

No edits made by the agent. Existing tracked worktree was already dirty
and was left untouched. Arithmetic checks passed locally.

Suggested insertion point: after the proof of
`prop:first-saturated-primitive-recognition-window`, before
`thm:executable-finite-source-matrix-criterion`.

```tex
\begin{remark}[Relation-closed finite window status]
\label{rem:relation-closed-window-status}
Write
\[
a_{ij}=\delta_i+\delta_j,\qquad
\tau=\delta_1+\delta_2+\delta_3,\qquad
C_{k,s}=a_{ij}+s\delta_k
\quad(\{i,j,k\}=\{1,2,3\}).
\]
The relation-minimal positive window used for the next finite recognition
test is
\[
W_{\mathrm{rel}}^+
=
W_{\le3}\cup R_4\cup I_4\cup C_{\le7}\cup\{2\tau\},
\]
where
\[
R_4=\{3\delta_i+\delta_j:i\ne j\},\qquad
I_4=\{2a_{ij}:i<j\},\qquad
C_{\le7}=\{C_{k,s}:1\le k\le3,\ 2\le s\le5\}.
\]
The signed packet is
\[
S_{\mathrm{rel}}=W_{\mathrm{rel}}^+\cup(-W_{\mathrm{rel}}^+)\cup\{0\}.
\]
Its positive part has \(35\) degree blocks, hence the signed matrix
packet has \(71\) blocks.  The status ledger is as follows.

\begin{center}
\begingroup
\setlength{\tabcolsep}{3pt}
\scriptsize
\begin{tabular}{@{}p{0.15\textwidth}p{0.25\textwidth}p{0.33\textwidth}p{0.21\textwidth}@{}}
\hline
degree family & reason retained & target status and parity source &
source certificate status \\
\hline
\(\delta_i\) &
real simple roots &
known \(1|0\); Gritsenko--Nikulin/Kac base row &
not supplied; source representatives, pairings, and comparison maps remain
part of the compact certificate \\

\(a_{ij}\) &
primitive isotropic fibres and first real-real brackets &
known \(10|0=E_{ij}\oplus\langle u_{ij,r}\rangle_{r=1}^9\);
Gritsenko--Nikulin/Kac base row &
not supplied; source bases, radical blocks, and bracket matrices required \\

\(2\delta_i+\delta_j\), \(i\ne j\) &
first real-string descendants in \(W_{\le3}\) &
known \(1|0\); Kac real-string target row &
not supplied; finite source relation rows and PBW comparison required \\

\(\tau\) &
first timelike block; Jacobi and mixed real-isotropic rows &
known \(29|93\); target presentation count, with
\(29-93=-64=f(1,1)\) &
not supplied; the \(29|93\) compact source block, pairings, radicals,
and \(27\) mixed maps are open \\

\(R_4=\{3\delta_i+\delta_j\}\) &
terminal real-Serre outputs &
known \(0|0\); terminal Serre zero row &
not supplied; terminal source Serre matrices must be checked \\

\(I_4=\{2a_{ij}\}\) &
doubled isotropic-copy brackets &
signed target data \(10\), isotropic simple contribution \(9\), residual
\(1\); full parity needs a rank-two target computation or citation, not
the product alone &
blocked until the full target parity row is fixed; compact doubled-ray
source rows remain open \\

\(C_{k,2}\) &
first complementary/timelike height-four outputs &
signed target data \(108\), additive coefficient \(m=90\), residual
\(18\); full parity is not determined by the product &
blocked until finite target presentation parity is computed; source maps,
radicals, and PBW rows remain open \\

\(C_{k,3}=s_k(\tau)\) &
next real-Weyl translate of the timelike block &
known \(29|93\) if the parity-preserving real Weyl action is imported;
Weyl transport, not product arithmetic &
target row usable after the Weyl-transport citation; compact source
comparison maps remain open \\

\(C_{k,4}=s_k(a_{ij})\) &
nonzero block receiving the \(\tau\)-string terminal zero map &
known \(10|0\) if the parity-preserving real Weyl action is imported;
Weyl transport, not product arithmetic &
target row usable after the Weyl-transport citation; source must also
verify that the terminal \(\tau\)-string map is zero into this nonzero
block \\

\(C_{k,5}\) &
terminal complementary-string output &
target \(0|0\); terminal support-zero row, justified by GN/Kac support
rather than by the product alone &
not supplied; source zero block and terminal relation row remain open \\

\(2\tau\) &
odd-odd \(\tau\)-block interactions &
signed target data \(f(4,2)=4016\) and simple coefficient
\(m(2\tau)=-540\); full parity requires a finite target presentation &
blocked until the full target parity row is computed; compact odd-odd
source relations, radicals, and PBW rows remain open \\
\hline
\end{tabular}
\endgroup
\end{center}

Rows with only signed target data cannot be used for target bases,
PBW comparison, or source comparison maps until their two parity
dimensions are supplied by a target presentation computation, Weyl
transport, or a cited Gritsenko--Nikulin/Kac theorem.
\end{remark}
```
