# Fifth Orientation/Weyl Attack-Heal Report

Date: 2026-04-28.

Role: H02.  Worktree:
`/tmp/igusa-fifth-orientation`.  Branch:
`agent/igusa-fifth-orientation-weyl-20260428`.

## Scope

Owned lane: orientation obstruction packages, connected `BE`, finite
`E[N]` stabilizers, finite linearization characters, and
Weyl-equivariant determinant-line transport.  I did not touch the
D0/Pfaffian O2/hybrid/chain-recognition lanes except where the
orientation certificate itself refers to them.

Files changed:

- `main.tex`
- `notes/fifth_orientation_weyl_attack_heal_report.md`

## Stable Cohomology Package

Connected quotient:
```tex
BE\simeq BT^2,\qquad
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2.
```
Thus
```tex
H^1(BE;\mathbb F_2)=0,\qquad
H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2.
```
There is no connected degree-one linearization character; the connected
free quotient obstruction is the degree-two class
```tex
\alpha^{E,\mathrm{free}}_{\mathcal C}
=a_1(\mathcal C)u_1+a_2(\mathcal C)u_2.
```

Two torsion:
```tex
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\quad |x_i|=1,
```
```tex
H^2(BE[2];\mathbb F_2)
=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle.
```
For `E[2]=<e_1,e_2>`, `e_3=e_1+e_2`,
```tex
\beta^{E,E[2]}_{\mathcal C}
=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,
```
```tex
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2).
```
These `r_i` are degree-two gerbe bits.  After
`\beta^{E,E[2]}_{\mathcal C}=0`, the linearizations form
```tex
H^1(BE[2];\mathbb F_2)=\mathbb F_2\langle x_1,x_2\rangle,
```
and the chosen character
```tex
\lambda_{\mathcal C}^{E[2]}=\lambda_1x_1+\lambda_2x_2
```
must vanish.  Its cyclic restrictions are
```tex
\rho_1=\lambda_1,\qquad
\rho_2=\lambda_2,\qquad
\rho_3=\lambda_1+\lambda_2.
```

Higher even stabilizers.  For `2^a || N`, `a >= 2`,
```tex
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
\quad |x_i|=1,\ |y_i|=2,\ x_i^2=0,
```
```tex
H^2=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle,
```
and
```tex
\beta^{E,N}_{\mathcal C,(2)}
=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
```
The mixed coefficient `A_{12}^{(N)}` is invisible to all cyclic
restrictions and is detected only by rank-two quotient data.  After this
degree-two class vanishes, the character
```tex
\lambda_{\mathcal C}^{E,N}
=\lambda_1^{(N)}x_1+\lambda_2^{(N)}x_2
\in H^1(B(\mathbb Z/2^a)^2;\mathbb F_2)
```
must still vanish on the full two-primary generators.

## Valid Attacks And Repairs

`A5-H02-01` valid, healed.  (O1) still let the reader treat the Weyl lift
as part of the base orientation datum.  This blurred the ordinary
Picard-line orientation from the Weyl-equivariant orientation.  Repaired
at `main.tex:934-967`: (O1) is now the ordinary square root plus the
reduced quotient-descent package.  The Weyl lift is explicitly separated
as (O1)+.

`A5-H02-02` valid, healed.  The top-level orientation package and the
finite-stage `D0-Q` tuple named finite degree-two gerbes but did not
carry the residual degree-one finite linearization characters as first
class data.  Repaired at `main.tex:959-967`,
`main.tex:1075-1094`, and `main.tex:7284-7316`: the package now records
`\lambda^{E,N}_{\mathcal C}` and requires the zero character after
`\beta^{E,N}_{\mathcal C}` is null-trivialized.

`A5-H02-03` valid, sharpened.  Even `N>=4` cyclic invisibility was
already correctly stated, but the compact realization clause still
phrased Weyl transport as transport of "finite quotient
null-trivializations" without explicitly naming the zero finite
characters.  Repaired at `main.tex:7945-7959`: the lifted Weyl action
must transport the full quotient package, including
`\lambda^{E,N}_{\mathcal C}=0`, with zero torsor defect.

`A5-H02-04` valid, healed.  (O1)+ named the projective Weyl cocycle
`c_o`, but the proof target did not isolate the exact obstruction theorem
for ordinary line action versus quotient-orientation action.  Added
Lemma `weyl-quotient-orientation-obstruction` at `main.tex:1637-1712`.
It separates:
```tex
[c_o]\in H^2(W^{(2)}(\Lambda^{2,1}_{II});\mathbb F_2),
```
the killing cochain
```tex
b\in C^1(W;\mathbb F_2),\qquad
\widetilde\tau_w=(-1)^{b(w)}\tau_w,
```
the generator lift constraints
```tex
\widetilde\tau_i^2=1,
```
and the quotient torsor defects
```tex
\omega_{i,\mathcal C}\in
H^1(\mathfrak M^{\mathrm{red}}_{s_{\delta_i}\mathcal C};\mathbb F_2)
\oplus\bigoplus_{N\ge2}H^1(BE[N];\mathbb F_2).
```
The lemma uses the already-proved type-II Coxeter presentation
`W=(Z/2)*(Z/2)*(Z/2)`: once the projective cocycle is killed, the only
relation constraints are the generator squares; torsor defects then
propagate by the word cocycle law.

`A5-H02-05` valid, sharpened in proof.  The theorem proof now states
that three Hall signs become a character only after the projective
determinant-line cocycle and quotient-trivialization torsors vanish.
Anchor: `main.tex:1322-1336`.  The Maass character remains target
evidence only.

## Attacks That Remain Open

No computation in this pass proves (O1).  The exact open package remains
```tex
\alpha^{\mathrm{red}}_{\mathcal C}=0,\qquad
a_1(\mathcal C)=a_2(\mathcal C)=0,
```
```tex
\beta^{E,N}_{\mathcal C}=0,\qquad
\lambda^{E,N}_{\mathcal C}=0
```
for every finite stabilizer appearing in the compact/wrapped Hall
atlas, compatibly with finite HN height and transition maps.

No computation in this pass proves (O1)+.  The exact open package is
```tex
[c_o]=0,\qquad
\widetilde\tau_i^2=1,\qquad
\omega_{i,\mathcal C}=0
```
with Coxeter coherence and finite-character transport on Weyl-related
charge strata.

The automorphic Maass values
`\nu_{\Delta_5}(s_{\delta_i})=-1` remain target checks only.  They do
not construct the Hall orientation line, the reduced quotient
linearization, the finite `E[N]` zero characters, or the Weyl
determinant-line cocycle splitting.

## Commands Run

- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`, the orientation notes, the
  semantic merge audit, and the O1/O1+/finite-stabilizer regions of
  `main.tex`.
- `rg` scans for `O1`, `O1+`, `orientation`, `E[`, `BE`,
  `linearization`, `cocycle`, `Weyl`, `finite stabilizer`, `Picard`,
  `gerbe`, and `determinant`.
- `nl -ba main.tex` for the file anchors recorded above.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fifth-orientation-texcheck main.tex`
  passed as a one-pass TeX syntax check.  It produced expected one-pass
  undefined-reference and undefined-citation warnings because BibTeX and
  later LaTeX passes were not run.
- `git diff --check -- main.tex` passed before this report was added.
- `git diff --check -- main.tex notes/fifth_orientation_weyl_attack_heal_report.md`
  passed after this report was added.

## Residuals

The construction target is now sharper but still conditional.  The next
mathematical work is not a scalar or Maass-sign comparison; it is a
geometric computation of the ordinary reduced gerbe, connected
`BE` class, finite `E[N]` gerbes and degree-one characters, followed by a
construction of the Weyl determinant-line splitting and quotient-torsor
transport on the reduced compact/wrapped sector.
