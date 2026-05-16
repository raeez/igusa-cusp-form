# Next Orientation Attack-Heal Report

Date: 2026-04-28.

## Claims Attacked

1. Strong reduced orientation `(O1)` on the compact/wrapped sector.
2. Promotion of ordinary translation invariance to quotient
   linearization.
3. Promotion of the rank-one `E[2]` three-bit calculation to full
   rank-one `(O1)`.
4. Use of the `E[2]` residual as evidence for even `N >= 4`
   finite-stabilizer descent.
5. Weyl transport of the ordinary square-root line without compatibility
   with the reduced quotient-descent package.

## Survivors

The connected `BE` computation survives:

```tex
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\qquad |u_i|=2,
```

so the free quotient has no `E_2^{1,1}` obstruction, but it still has
the two degree-two coefficients

```tex
\alpha^{E,\mathrm{free}}_{\mathcal C}
=a_1(\mathcal C)u_1+a_2(\mathcal C)u_2.
```

The rank-one two-torsion obstruction survives exactly as an `N=2`
finite-stabilizer theorem:

```tex
\beta^{E,E[2]}_{\mathcal C}
=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,
```

with

```tex
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2).
```

Thus `N=2` finite descent is equivalent to
`r_1=r_2=r_3=0`, once the cyclic fixed-sector models are supplied.

## Demotions

Full rank-one `(O1)` is not proved.  It requires

```tex
\alpha^{\mathrm{red}}_{\mathcal C}=0,\qquad
a_1(\mathcal C)=a_2(\mathcal C)=0,\qquad
\beta^{E,N}_{\mathcal C}=0\quad\text{for every even }N.
```

For `2^a || N`, `a >= 2`, the residual is not the `E[2]` class.  It
lives in

```tex
H^2(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle,
\qquad |x_i|=1,\quad |y_i|=2,\quad x_i^2=0.
```

The `E[2]` vector does not determine this class.

Weyl transport `(O1)+` is not just transport of an ordinary line.  It
must preserve

```tex
(\alpha^{\mathrm{red}}_{\mathcal C},
 \alpha^{E,\mathrm{free}}_{\mathcal C},
 \{\beta^{E,N}_{\mathcal C}\}_{N\ge2})
```

and the chosen trivializations on Weyl-related strata.  Without this,
the reflection sign is not a character of the reduced quotient
orientation.

## Files Changed

- `main.tex`
- `notes/next_orientation_attack_heal_report.md`

## Remaining Open Obligations

Compute the ordinary reduced Pin-c gerbe
`\alpha^{\mathrm{red}}_{\mathcal C}`, the connected coefficients
`a_1,a_2`, the rank-one `E[2]` vector `r_1,r_2,r_3`, and the even
`N >= 4` two-primary residuals.  Then construct the Weyl-equivariant
determinant-line transport preserving those quotient trivializations.
