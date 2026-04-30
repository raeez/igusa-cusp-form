# A023 report: \(B\)-isotropic no-go and BKM real-root strings

Runtime id: `019ddbd9-a6d8-74d3-9419-2354708e0bbc`.
Nickname: McClintock.
Status: completed.
Files changed by agent: none.

## Status

Fixed-lift no-go survives. It proves: strict fixed-lift, channelwise raw
\(\Pi_X\)-descent cannot realize the type-II BKM real-root strings. It
does not prove a no-go for all possible fibre-summed raw constructions.

## Explicit Calculation

Let \(c_i,c_j\) be fixed chosen lifts with
\(\Pi_X(c_i)=\gamma_i\), \(\Pi_X(c_j)=\gamma_j\). Raw graded closure of
\([P_{c_i},P_{c_j}]\) forces
\[
B(c_i,c_j)=0.
\]
The second BKM string requires \([P_{c_i},P_{c_i+c_j}]\neq0\), hence raw
closure forces
\[
B(c_i,c_i+c_j)=0.
\]
But
\[
B(c_i,c_i+c_j)=B(c_i,c_i)+B(c_i,c_j)=2\Pi_X(c_i)=2\gamma_i\neq0.
\]
This is a contradiction in torsion-free \(\Gamma_{\mathrm{gram}}\).

For \(i=1,j=2\), \(\gamma_1=(1,1,0)\), \(\gamma_2=(0,1,1)\). The
desired second degree is
\[
2\gamma_1+\gamma_2=(2,3,1),
\]
while raw physical charge \(2c_1+c_2\) has shadow
\[
4\gamma_1+\gamma_2=(4,5,1)
\]
under the first-bracket isotropy assumption. Difference:
\[
2\gamma_1\neq0.
\]

## Anchors

`main.tex:5023` defines raw/fixed-lift pushforward.
`main.tex:5042` states the no-go.
`main.tex:5072` gives the proof.
`main.tex:5119` gives the fibre-summed caveat.
Low-degree BKM strings: `main.tex:14696`, `main.tex:14748`.

## Wording Recommendations

Keep "strict fixed-lift" in every global summary. Current abstract and
synthesis wording is safe at `main.tex:152` and `main.tex:16253`.

In the theorem proof, reduce notation drift by writing
\(\Pi_X(c_i)=\gamma(\delta_i)\), or simply
\(\gamma_i=\gamma(\delta_i)\), before using both \(\gamma_i\) and
\(\delta_i\).

Add one sentence spelling the fixed-lift assumption: the realized bracket
channel uses the same chosen lift \(c_i\) again and the composite
physical degree \(c_i+c_j\); mixed replacement lifts inside the same
Gram fibre are outside the theorem.

A010's residual stands: low-degree word survival should get a
source-backed Kac/GN citation, since determinant data alone do not prove
the brackets survive the radical.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`,
`python3 compute/verify_lattice.py`, `git status --short`. No build.
