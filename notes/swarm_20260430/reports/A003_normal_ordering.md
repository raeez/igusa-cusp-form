# A003 report: normal-ordered lattice and raw-descent no-go

Runtime id: `019ddbc4-f580-7420-931d-3461e716c5fa`.
Nickname: Boyle.
Status: completed.
Files changed by agent: none.

## Formula Status

The formal Mukai sector is correctly fenced as
\(\Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S\), not the full
\(N=4\) charge lattice and not compact Hall support.

Anchors:
`main.tex:4415`, `main.tex:4423`, CYQG `AP-CY359`.

The Gram cocycle is elementary and correct. Expanding
\[
\Pi_X(Q+Q',P+P')
\]
gives
\[
\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+
(Q\cdot Q',Q\cdot P'+Q'\cdot P,P\cdot P').
\]
Thus \(B\) is symmetric bilinear, \(B(c,c)=2\Pi_X(c)\),
\(\delta B=0\), and \(B=-\delta\Pi_X\) as an ordinary cochain. The
manuscript correctly says this is not a nonzero ordinary cohomology
class.

Anchors:
`main.tex:4441`, `main.tex:4707`, `main.tex:4812`.

The normal-ordered group law is correct:
\[
(c,T)\star(c',T')=(c+c',T+T'+B(c,c')).
\]
Associativity is bilinearity:
\[
B(a,b)+B(a+b,c)=B(b,c)+B(a,b+c).
\]
Also
\[
\overline\Pi_X((c,T)\star(c',T'))
=\overline\Pi_X(c,T)+\overline\Pi_X(c',T').
\]

Anchors:
`main.tex:4742`, `main.tex:4857`.

Raw fixed-lift descent no-go is valid. A raw
\(\Gamma_{\mathrm{gram}}\)-graded bracket requires \(B(c,c')=0\) on
every nonzero bracket channel. But BKM grading has nonzero strings
\(\delta_i+\delta_j\) and \(2\delta_i+\delta_j\). If
\(B(c_i,c_j)=0\), the second bracket forces
\[
0=B(c_i,c_i+c_j)=B(c_i,c_i)+B(c_i,c_j)=2\Pi_X(c_i)=2\gamma_i\neq0.
\]
This proves the fixed-lift raw no-go, not a no-go for all fibre-summed
raw constructions.

Anchors:
`main.tex:5023`, `main.tex:5072`, `main.tex:14708`, CYQG `AP-CY361`.

## Overclaim Risks

Do not state chain-level descent without "supplied", "input", or "open".
Safe-boundary anchors:
`main.tex:4898`, `main.tex:8641`, `main.tex:9055`,
`main.tex:9178`, `main.tex:9444`.

\(\Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)}\) proves the degree-shadow identity
\[
d_{\mathrm{Hoch}}\Theta_\Pi(c,c')
=-\Pi_X(c)-\Pi_X(c')+\Pi_X(c+c')=B(c,c'),
\]
but it does not prove Hall chain strictification, cyclic compatibility,
Frobenius compatibility, or radical coideal stability.

Anchors:
`main.tex:9362`, `main.tex:9386`, `main.tex:9401`.

## Theorem Boundaries

Lattice theorem:
\(\Pi_X\), \(B\), \(\widehat\Gamma_X\), \(\overline\Pi_X\),
associativity, and raw fixed-lift no-go.

Conditional Hall theorem:
if finite Hall stages, \((P),(E),(O),(\Theta),(F),(\mathrm{Cyc})\),
HN transition compatibility, and radical ideal/coideal stability are
supplied, then \(H^0\) normal-ordered descent is
\(\Gamma_{\mathrm{gram}}\)-graded.

Open problem:
construct \(\Theta_\Pi\) on the reduced compact/wrapped Hall sector and
vanish the seven residuals.

Residuals:
\(\mathfrak o_\Theta^{top}\), \(\mathfrak o_\Theta^{Hoch}\),
\(\mathfrak o_\Theta^{tri}\), \(\mathfrak o_\Theta^{Jac}\),
\(\mathfrak o_F\), \(\mathfrak o_\Theta^{cyc}\),
\(\mathfrak o_\Theta^{rad}\), plus HN closedness of the radical.

Commands run by agent: read-only `sed`, `rg`, `nl -ba`, and final
`git status --short`. No build.
