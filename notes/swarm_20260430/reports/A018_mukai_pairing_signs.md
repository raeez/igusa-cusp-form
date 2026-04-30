# A018 report: Mukai-pairing sign conventions

Runtime id: `019ddbd3-3f5f-72b1-89c2-961639e84f25`.
Nickname: Lorentz.
Status: completed.
Files changed by agent: none.

## Formula Status

Sound as written under the manuscript's fixed Mukai convention.

The paper fixes
\[
(r,D,s)\cdot(r',D',s')=D\cdot D'-rs'-r's
\]
at `main.tex:2750` and again in the physical charge lattice at
`main.tex:4411`.

For a curve \(Y\subset S\times E\),
\[
\operatorname{ch}(\mathcal I_Y)=1-\operatorname{ch}(\mathcal O_Y),
\]
with
\[
\operatorname{ch}(\mathcal O_Y)
=(0,0,d)\otimes 1_E+(0,\beta,n)\otimes\omega_E.
\]
Multiplication by \(\sqrt{\operatorname{td}(S)}=(1,0,1)\) gives
\[
v_X(\mathcal I_Y)
=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
\]
as stated at `main.tex:2756` and proved at `main.tex:2797`.

With
\[
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n),
\]
direct pairing gives
\[
Q_Y^2=(-\beta)^2=\beta^2,
\]
\[
Q_Y\cdot P_Y=(-\beta)\cdot0-0(1-d)-1(-n)=n,
\]
\[
P_Y^2=0-2(1)(1-d)=2(d-1).
\]
Hence
\[
\Pi_X(Q_Y,P_Y)=\left(\frac{\beta^2}{2},n,d-1\right),
\]
and for \(\beta_h^2=2h-2\),
\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
\]

Anchors:
`main.tex:2760`, `main.tex:2813`.

## Convention-Dependent Signs

1. The minus signs in \(Q_Y=(0,-\beta,-n)\) come from using the ideal
   sheaf \(I_Y=O_X-O_Y\), not from the Mukai form.
2. The \(+n\) in \(Q_Y\cdot P_Y=n\) depends on the paper's Mukai pairing
   sign. With the opposite pairing \(rs'+r's-D\cdot D'\), the triple
   becomes \((1-h,-n,1-d)\) unless \(\Pi\) is also negated.
3. The shift \(d-1\) depends on using the Mukai vector with
   \(\sqrt{\operatorname{td}(S)}=(1,0,1)\). Using only
   \(\operatorname{ch}\) would give \(d\), not \(d-1\).
4. The order \(c=(Q,P)\) is essential. Swapping \(Q,P\) swaps the first
   and third Gram coordinates.
5. The OP/DT scalar convention \((-p_{\mathrm{DT}})^n\) is separate
   from the Mukai pairing sign; it should not be used to replace
   \(Q\cdot P=n\) by \(-n\). Anchors: `main.tex:15886`,
   `main.tex:4253`.

## Physical Charge Lattice Check

Consistent. The formal sector is explicitly
\[
\Gamma_X^{\mathrm{phys}}=\Gamma_X^{\mathrm{form}}
=\Lambda_S\oplus\Lambda_S,\quad c=(Q,P),
\]
with
\[
\Pi_X(Q,P)=\left(Q^2/2,Q\cdot P,P^2/2\right)
\]
at `main.tex:4582`. The text correctly warns this is not the full
\(N=4\) electric-magnetic lattice at `main.tex:4420`.

## Correction Risks

No sign correction recommended. Main risk is importing formulas from
sources using the opposite Mukai signature or from physics \(Q,P\)
conventions without an explicit conversion line. Secondary risk:
confusing geometric elliptic degree \(d\) with Borcherds/Gram exponent
\(m=d-1\).

Commands run by agent:
targeted `rg`; targeted `nl -ba ... | sed -n ...` reads of `main.tex`,
guide, processed critique, `proj.bib`, and `compute/verify_lattice.py`;
`python3 compute/verify_lattice.py`. The script passed, but it verifies
the Pfaffian/Gram lattice side, not the D6 Mukai decomposition itself.

Residual obligation:
if this theorem is later compared directly to a primary physics charge
convention, add an explicit conversion table for pairing sign, \(Q/P\)
order, and \((-p)^n\).
