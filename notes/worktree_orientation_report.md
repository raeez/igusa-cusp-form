# Worktree Orientation Report

Date: 2026-04-28.

## Claim Attacked

Strong reduced orientation `(O1)` and the proposed trivial `E[2]`
linearization on the rank-one D6--D2--D0 sector.

## Result

The three-bit Klein-four criterion cannot honestly be promoted to a
proof of rank-one `(O1)` from the current manuscript.  It is complete
only for the finite `N=2` stabilizer residual.  Full rank-one quotient
descent also requires the ordinary reduced Pin-c class and the connected
`BE` linearization class.

The exact rank-one obstruction package is:

```tex
\alpha^{\mathrm{red}}_{\mathcal C}
\in H^2(\mathfrak M^{\mathrm{red}}_{\mathcal C};\mathbb F_2),
```

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

For `E[2]=<e_1,e_2>` and `e_3=e_1+e_2`,

```tex
\operatorname{res}_{<e_i>}\beta^{E,E[2]}_{\mathcal C}=r_i\tau_i^2,
```

with

```tex
r_1=b_{20},\qquad r_2=b_{02},\qquad
r_3=b_{20}+b_{11}+b_{02},
```

hence

```tex
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2).
```

The finite `E[2]` residual vanishes iff `r_1=r_2=r_3=0`.  Rank-one
`(O1)` through the two-torsion boundary requires, in addition,
`\alpha^{\mathrm{red}}_{\mathcal C}=0` and `a_1=a_2=0`.

## Three Finite Routes

The same three finite bits must be computed by:

1. cyclic-sector character:
   `r_i=(1-\chi_i)/2`;
2. Stiefel-Whitney/Wu:
   `res_i w_2^{E[2]}(T^{red}_{\mathcal C})=r_i\tau_i^2`,
   with `w_2=v_2+Sq^1v_1`;
3. inertia-stack Pin-c:
   the central `ker(Pin^c -> SO)` holonomy plus the mod-2 orbifold
   RR age correction on `I_{e_i}\mathfrak M`.

Agreement with `(0,0,0)` proves the trivial `E[2]` linearization.
The manuscript now states this as a finite obstruction theorem, not as a
vanishing theorem.

## Files Changed

- `main.tex`
- `notes/worktree_orientation_report.md`

## Theorem Status

- Proved in the manuscript: connected `BE` and finite `BE[N]`
  cohomological separation; Klein-four cyclic restriction detects
  `H^2(BE[2];F_2)`.
- Inscribed now: a theorem-level rank-one `E[2]` obstruction package
  using cyclic-sector, Stiefel-Whitney/Wu, and inertia-stack Pin-c
  formulas.
- Not proved: actual vanishing of `a_1,a_2,r_1,r_2,r_3`, and hence not
  a construction of `(O1)`.

## Remaining Obstruction

Compute the five quotient-linearization bits
`a_1,a_2,r_1,r_2,r_3` on the rank-one sector, then extend the finite
stabilizer calculation to even `N>=4` through the two-primary stabilizer.

## Commands Run

- `sed`/`nl` reads of `CLAUDE.md`, `AGENTS.md`, ecosystem invariants,
  architecture/status notes, `proj.bib`, and the assigned `main.tex`
  regions.
- `rg` scans for orientation, `E[2]`, translation, linearization,
  finite-stabilizer, scalar-square, and orientation-character claims.
- `git diff --check -- main.tex notes/worktree_orientation_report.md`.
- `make`.

The first build exposed bracketed `E[2]` notation inside a theorem
optional title; this was repaired by replacing the title with
`Rank-one two-torsion linearization obstruction package`.  The final
`make` succeeded and rebuilt `out/main.pdf`.
