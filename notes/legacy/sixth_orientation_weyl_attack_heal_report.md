# Sixth Orientation/Weyl Attack-Heal Report

Date: 2026-04-28.

Role: S02 Orientation/Weyl.  Worktree:
`/tmp/igusa-sixth-orientation`.  Branch:
`agent/igusa-sixth-orientation-construct-20260428`.

## Scope

Owned files:

- `main.tex`
- `notes/sixth_orientation_weyl_attack_heal_report.md`

I did not edit the main worktree, commit, push, stash, rewrite a branch,
or touch files outside the owned writable set.  The requested
`notes/sixth_attack_heal_swarm_20260428.md` was not present in this
worktree.  I read the available integration ledgers instead:
`notes/notes/attack_heal_swarm_20260428.md`,
`notes/notes/fifth_attack_heal_swarm_20260428.md`, and the prior
orientation/Weyl reports.

## Claims Attacked

1. Strong reduced orientation `(O1)` on compact/wrapped sectors could be
   proved from Joyce--Upmeier orientation theory plus ordinary
   translation invariance.
2. The `E[2]` three-bit calculation could be promoted to all finite
   `E[N]` stabilizers.
3. Vanishing of finite degree-two gerbes could be confused with trivial
   finite linearisations.
4. The Weyl-equivariant orientation cocycle `(O1)+` could be reduced to
   the three local signs or to the Maass automorphic character.
5. The `Aut(Poly_II)` chamber-permuting reflections with Maass value
   `+1` could be treated as constructed Hall signs without a semidirect
   Hall lift.

## Verdict

No unconditional proof of `(O1)` or `(O1)+` is available from the present
sources.  The stable repair is obstruction-theoretic:

- `(O1)` is blocked exactly by the ordinary reduced gerbe, connected
  `BE` class, finite `BE[N]` degree-two gerbes, and residual finite
  `H^1(BE[N];F_2)` linearisations.
- `(O1)+` is blocked exactly by the Weyl determinant-line projective
  cocycle, generator relation normalisations, quotient-trivialisation
  torsors, and, for semidirect extension, the corresponding
  `W^(2) semidirect Aut(Poly_II)` cocycle and torsors.
- Scalar automorphic data never enters these obstruction groups.

## Repairs Inscribed

`main.tex` now has a sharpened finite-stabilizer descent criterion in
Lemma `E-equivariant-descent-obstruction`: after
`\beta^{E,N}_{\mathcal C}` is null-trivialized, the selected finite
linearisation still has a degree-one character

```tex
\lambda^{E,N}_{\mathcal C}\in H^1(BE[N];\mathbb F_2)
```

which must vanish.

I added Corollary `finite-stabilizer-o1-obstruction`.  On a small-orbit
stratum with stabilizer `E[N]`, after
`\alpha^{red}_{\mathcal C}` and
`\alpha^{E,free}_{\mathcal C}` have vanished, the finite obstruction
tuple is:

```tex
N odd: H^{>0}(BE[N];F_2)=0.
N=2:  (r_1,r_2,r_3; rho_1,rho_2,rho_3).
2^a||N, a>=2:
(A_1^(N), A_12^(N), A_2^(N); lambda_1^(N), lambda_2^(N)).
```

A non-zero entry obstructs `(O1)` on that stratum.

I added Corollary `semidirect-wall-transport-obstruction`.  An
extension from

```tex
W^{(2)}(\Lambda^{2,1}_{II})
```

to

```tex
W^{(2)}(\Lambda^{2,1}_{II}) \rtimes Aut(Poly_II)
```

requires

```tex
[c_o^G]=0 in H^2(G;F_2)
```

with relation-normalised splitting and zero quotient torsor defects

```tex
omega_{g,C} in
H^1(M^{red}_{gC};F_2) \oplus direct_sum_N H^1(BE[N];F_2).
```

The Maass values `+1` on the chamber-permuting reflections are recorded
as target data only.

## Exact Cohomology Data

Connected quotient:

```tex
BE ~= BT^2,
H^*(BE;F_2)=F_2[u_1,u_2], |u_i|=2,
H^1(BE;F_2)=0,
H^2(BE;F_2)=F_2 u_1 \oplus F_2 u_2.
```

Two torsion:

```tex
H^*(BE[2];F_2)=F_2[x_1,x_2], |x_i|=1,
H^2(BE[2];F_2)=F_2<x_1^2,x_1x_2,x_2^2>.
```

With `E[2]=<e_1,e_2>` and `e_3=e_1+e_2`,

```tex
beta^{E,E[2]}_C=b_20 x_1^2+b_11 x_1x_2+b_02 x_2^2,
(b_20,b_11,b_02)=(r_1,r_1+r_2+r_3,r_2).
```

After `beta=0`, the character is

```tex
lambda_C^{E[2]}=lambda_1 x_1+lambda_2 x_2,
rho_1=lambda_1, rho_2=lambda_2, rho_3=lambda_1+lambda_2.
```

Higher even stabilizers:

```tex
H^*(B(Z/2^a)^2;F_2)=Lambda(x_1,x_2) tensor F_2[y_1,y_2],
|x_i|=1, |y_i|=2, x_i^2=0,
H^2=F_2<y_1,x_1x_2,y_2>.
```

The class is

```tex
beta^{E,N}_{C,(2)}=A_1^(N)y_1+A_12^(N)x_1x_2+A_2^(N)y_2.
```

The coefficient `A_12^(N)` is invisible to cyclic restrictions and is
detected by the rank-two quotient.  After degree-two vanishing, the
character

```tex
lambda_C^{E,N}=lambda_1^(N)x_1+lambda_2^(N)x_2
```

must vanish on the full two-primary generators.

## Attack Results

Joyce--Upmeier route: useful but insufficient.  Joyce--Upmeier and
Joyce--Tanaka--Upmeier supply multiplicative orientation formalism once
the reduced sector, square-root line, and quotient descent data exist.
They do not compute `alpha^{red}`, `alpha^{E,free}`, `beta^{E,N}`, or
`lambda^{E,N}` on the reduced `K3 x E` quotient.

Determinant-line torsor route: exact.  Square-root gerbes live in
degree two.  After null-trivialisation, choices of finite stabilizer
linearisations form an `H^1` torsor.  The report and manuscript now keep
these degrees separate.

Finite stabilizer spectral sequence route: exact obstruction.  The
Borel descent spectral sequence places the finite square-root obstruction
in total degree two; the residual linearisations are degree one.  Odd
stabilizers vanish by transfer; even stabilizers reduce to the
two-primary part.

Weyl cocycle route: exact obstruction.  The type-II Weyl group has
presentation `C_2 * C_2 * C_2`, so once `(O1)+` supplies an honest
quotient-compatible action, the three generator signs define a
character.  Before `[c_o]=0` and `omega_{i,C}=0`, there is only a
projective determinant-line action and no Hall orientation character.

Semidirect route: obstructed.  Extending to the chamber-permuting
`S_3` requires a new projective cocycle on the semidirect group and
quotient torsor transport for the full package.  Maass `+1` values do
not construct those data.

Counterexample route: stable.  A nonzero
`lambda^{E,N}_C in H^1(BE[N];F_2)` gives a fixed ordinary line whose
stabilizer acts by a nontrivial character.  Its square and any scalar
automorphic character are unchanged, but the quotient orientation does
not descend trivially.  This blocks every attempted scalar proof of
`(O1)`.

## Verification

Commands run before final verification:

```bash
rg --files | rg '(^|/)(attack|sixth|orientation|weyl|report|protocol|proj\.bib|main\.tex|appendices)'
rg -n 'O1|orientation|Weyl|E\[N\]|E\[2\]|linearization|cocycle|quotient' main.tex notes proj.bib
nl -ba main.tex | sed -n '800,1425p'
nl -ba main.tex | sed -n '1520,1835p'
nl -ba main.tex | sed -n '2268,3450p'
```

Final checks:

```bash
git diff --check -- main.tex notes/sixth_orientation_weyl_attack_heal_report.md
```

passed.

```bash
mkdir -p /tmp/igusa-sixth-orientation-texcheck
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/igusa-sixth-orientation-texcheck main.tex
```

passed as a one-pass TeX syntax check.  It produced expected one-pass
undefined-reference and undefined-citation warnings because BibTeX and
later LaTeX passes were not run.

## Residual Obligations

Compute and trivialize, on every compact/wrapped Hall stratum and every
finite HN stage:

```tex
alpha^{red}_C,
alpha^{E,free}_C,
beta^{E,N}_C,
lambda^{E,N}_C.
```

Then construct the Weyl determinant-line splitting:

```tex
[c_o]=0, tau_i^2=1, omega_{i,C}=0,
```

and, if chamber automorphisms are needed, the semidirect package:

```tex
[c_o^G]=0, omega_{g,C}=0
```

with all `S_3` relation coherences.  Only after this and the O2 wall
charts are supplied can the Hall orientation character be identified
with the Maass character.
