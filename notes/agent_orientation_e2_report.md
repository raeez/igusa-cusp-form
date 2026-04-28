# Agent 3 Orientation and E[2] Report

Internal swarm report for the orientation/E[2] attack-heal pass.

## Claim Attacked

Strong reduced orientation `(O1)` on the compact/wrapped
`K3 x E` sector, including descent through the reduced `E` quotient and
trivial finite `E[2]` linearization on the small-orbit sector.

## Result

No unconditional trivial `E[2]` linearization is proved from the current
sources.  The manuscript now states the exact finite obstruction:

```tex
\alpha^{E,\mathrm{free}}_{\mathcal C}
=a_1(\mathcal C)u_1+a_2(\mathcal C)u_2
\in H^2(BE;\mathbb F_2),
```

and, on the two-torsion small-orbit stratum,

```tex
\beta^{E,E[2]}_{\mathcal C}
=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2
\in H^2(BE[2];\mathbb F_2).
```

For the three nontrivial cyclic subgroups
`\mu_2^{(i)}=<e_i>` with `e_3=e_1+e_2`,

```tex
r_1=b_{20},\qquad r_2=b_{02},\qquad
r_3=b_{20}+b_{11}+b_{02},
```

so

```tex
b_{20}=r_1,\qquad b_{02}=r_2,\qquad
b_{11}=r_1+r_2+r_3.
```

Thus the finite stabilizer obstruction vanishes iff
`r_1=r_2=r_3=0`.

## Three Finite Tests

The same three bits must be computed by:

1. Cyclic-sector character:
   `r_i=(1-\chi_i)/2`, where `\chi_i` is the scalar by which `e_i`
   acts on the linearized orientation line over the inertia sector.
2. Stiefel-Whitney/Wu:
   `res_i w_2^{E[2]}(T^{red}_{\mathcal C})=r_i\tau_i^2`, with
   `w_2=v_2+Sq^1v_1`.
3. Inertia-stack Pin-c:
   the central `ker(Pin^c -> SO)` holonomy plus the mod-2 orbifold
   RR age correction on `I_{e_i}\mathfrak M`.

Agreement with `(0,0,0)` proves the trivial `E[2]` linearization.
Current text records this as a finite check, not a theorem.

## Files Changed

- `main.tex`: orientation clause `(O1)`, Open Problem
  `op:orientation-monodromy-character`, `E`-descent/Klein-four region,
  rank-one Pin-lift sign lemma, and certificate clause `(O_X)`.
- `notes/agent_orientation_e2_report.md`: this report.

## Remaining Obstruction

Compute the five rank-one quotient bits
`a_1,a_2,r_1,r_2,r_3`, then extend the same finite-stabilizer calculation
to even `N>=4` through the two-primary stabilizer.
