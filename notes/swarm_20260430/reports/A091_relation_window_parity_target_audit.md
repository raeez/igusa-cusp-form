# A091 relation-window parity target audit

No files edited. The agent inspected A071, A080, A085, `CLAUDE.md`,
the rectify skill, `main.tex`, and ran `compute/verify_square_root.py`
read-only.

Conventions:
\[
\gamma(c_1,c_2,c_3)=(c_1,c_1+c_2-c_3,c_2),\qquad
\smult(\beta)=f(nm,l).
\]
The product gives only \(\smult=d_{\bar0}-d_{\bar1}\), not parity.

| row | status | derivation | manuscript implication |
|---|---|---|---|
| \(I_4=\{2a_{ij}\}\) | full target \(10|0\), but needs explicit citation/computation | \(\smult(2a_{ij})=10\), \(\tau(2a_{ij})=9\); residual \(1\) is the even \(A_1^{(1)}\) rank-two real subalgebra contribution. | Mark signed-only until a Kac affine multiplicity citation or finite target reducer is inserted. |
| \(C_{k,2}=a_{ij}+2\delta_k\) | signed-only | \((C_{k,2},C_{k,2})=-8\), \((C_{k,2},\delta_k)=0\); verifier gives \(\smult=108\), \(m=90\), residual \(18\). | Requires finite GN/Kac presentation computation in this degree. |
| \(C_{k,3}=a_{ij}+3\delta_k\) | full target \(29|93\) | \(s_k(\delta_{123})=\delta_{123}+2\delta_k=C_{k,3}\). Real Weyl action is even and preserves root-space parity. | Usable with explicit Kac/GN real-Weyl transport citation. |
| \(C_{k,4}=a_{ij}+4\delta_k\) | full target \(10|0\) | \(s_k(a_{ij})=a_{ij}+4\delta_k=C_{k,4}\). | Nonzero \(10|0\) target row; keep separate from terminal zero relation for the odd \(\delta_{123}\)-string. |
| \(C_{k,5}=a_{ij}+5\delta_k\) | full target \(0|0\) | \(s_k(C_{k,5})=a_{ij}-\delta_k\), outside \(Q_+\cup(-Q_+)\); equivalently the Kac root string terminates after \(C_{k,4}\). | Defensible by Kac root-string/Weyl support, not by \(\smult=0\). |
| \(2\delta_{123}\) | signed-only | \(\gamma(2\delta_{123})=(2,2,2)\), \(\smult=f(4,2)=4016\), \(m(2\delta_{123})=-540\). | Requires finite target presentation through \(2\delta_{123}\), including odd-odd brackets, lower PBW words, BK relations, GN radical, and no-extra check. |

Bottom line: \(C_{k,3}\), \(C_{k,4}\), and \(C_{k,5}\) can be promoted
by Weyl/root-string reasoning; \(C_{k,2}\) and \(2\delta_{123}\) remain
signed-only until finite target presentation computation. \(I_4\) needs
an explicit affine rank-one citation or computation before manuscript
promotion.

