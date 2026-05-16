# Seventh Orientation/Weyl Attack-Heal Report

Date: 2026-04-28.

Role: S7-O.  Worktree: `/tmp/igusa-seventh-orientation`.  Branch:
`agent/igusa-seventh-orientation-weyl-20260428`.

## Scope

Owned lane: strong reduced orientation `(O1)`, compact/wrapped
finite-stabilizer character systems, all even `E[N]` character issues,
and Weyl-equivariant determinant-line transport `(O1)+`.

Files changed:

- `main.tex`
- `notes/seventh_orientation_weyl_attack_heal_report.md`

I did not edit outside the assigned worktree, did not use destructive git
commands, did not commit, did not push, and did not stage unrelated files.

## Claims Attacked

`A7-O-01`, valid.  Strong reduced orientation on the compact/wrapped
Hall sector is not proved by an ordinary square-root line.  The quotient
needs the ordinary reduced gerbe, connected `BE` class, finite
`BE[N]` gerbes, residual finite `H^1(BE[N];F_2)` characters, and
orientation transport through local, wrapped, mixed, and flag
correspondences.

`A7-O-02`, valid.  The `E[2]` three-bit calculation does not kill all
finite stabilizers.  For `2^a || N`, `a >= 2`, the mixed class
`A_12^(N) x_1 x_2` and the two degree-one characters
`lambda_1^(N), lambda_2^(N)` remain separate.

`A7-O-03`, valid.  Vanishing of a finite degree-two gerbe does not select
the trivial finite linearization.  After null-trivialization, the
linearisations form an `H^1(BE[N];F_2)` torsor.

`A7-O-04`, valid.  A Weyl character is not produced by three local signs
until the projective determinant-line cocycle and quotient-torsor defects
vanish.  The Maass character is target data, not a Hall orientation
construction.

`A7-O-05`, invalid as an unconditional repair.  No source read in this
pass computes all compact/wrapped finite stabilizer tuples or proves the
Weyl determinant-line splitting.  The honest repair is an exact
finite-stage criterion and residual obstruction.

## Repairs Made

`main.tex` now identifies `(O1)` at finite compact/wrapped HN height with
the finite-stage quotient-orientation character system of
`Proposition finite-stage-quotient-orientation-character-system`.

I added `Corollary finite-stage-weyl-cocycle-character-system`.  Given a
finite-stage quotient-orientation character system and simple wall
determinant-line lifts, it constructs the finite action-groupoid
cocycle

```tex
c_{o,R}(w,w';C)
```

and quotient-torsor defects

```tex
omega_{w,R,C}
in H^1(M^{red}_{wC};F_2) + direct_sum_N H^1(BE[N];F_2).
```

The finite-stage Weyl lift exists exactly when the cocycle is killed by
a relation-normalized cochain and the retained simple-reflection torsor
defects vanish.  A cofinal compatible family is `(O1)+`.

I added `Proposition finite-stage-quotient-orientation-character-system`.
It constructs the actual finite quotient-orientation package

```tex
Q_R^or =
({o_{R,S}}, {theta^red_{R,S}}, {theta^{E,free}_{R,S}},
 {theta^{E,N}_{R,S}, lambda^{E,N}_{R,S}=0},
 {mu^or_{R,e}}, {Theta^or_{R,flag}})
```

on object, extension, and flag strata of the compact/wrapped finite HN
stage.  It proves the exact iff criterion: the system exists iff the
ordinary, connected, finite degree-two, finite degree-one, correspondence,
flag, and transition defects all vanish.

I linked `(D0-Q)` and the Dirac--Igusa orientation certificate to this
finite-stage character system, so the compact/wrapped sector no longer
looks like an ordinary Picard-line condition.

## Stable Mathematical Core

Connected quotient:

```tex
H^1(BE;F_2)=0,
H^2(BE;F_2)=F_2 u_1 + F_2 u_2.
```

Two torsion:

```tex
beta^{E,E[2]}_C=b_20 x_1^2+b_11 x_1x_2+b_02 x_2^2,
(b_20,b_11,b_02)=(r_1,r_1+r_2+r_3,r_2).
```

After `beta=0`, the chosen `E[2]` linearization has

```tex
lambda_C^{E[2]}=lambda_1 x_1+lambda_2 x_2,
rho_1=lambda_1, rho_2=lambda_2, rho_3=lambda_1+lambda_2.
```

Higher even stabilizers:

```tex
H^2(B(Z/2^a)^2;F_2)=F_2<y_1,x_1x_2,y_2>,
beta^{E,N}_{C,(2)}=
A_1^(N)y_1+A_12^(N)x_1x_2+A_2^(N)y_2.
```

The mixed coefficient is invisible to cyclic restrictions.  After the
degree-two class vanishes, the character

```tex
lambda_C^{E,N}=lambda_1^(N)x_1+lambda_2^(N)x_2
```

must still vanish on the full two-primary generators.

Weyl lift:

```tex
w'^* tau_{w,R,w'C} o tau_{w',R,C}
= (-1)^{c_{o,R}(w,w';C)} tau_{ww',R,C}.
```

The quotient defect satisfies

```tex
omega_{ww',R,C}=w'^* omega_{w,R,C}+omega_{w',R,C}.
```

These are determinant-line and quotient-torsor data.  The Maass
character does not map to these obstruction groups.

## Manuscript Anchors

- `(O1)` finite-stage character-system reference:
  `main.tex`, theorem `dirac-pfaffian-recognition-conditional`.
- Finite-stage Weyl cocycle:
  `main.tex`, corollary `finite-stage-weyl-cocycle-character-system`.
- Compact/wrapped quotient-orientation character system:
  `main.tex`, proposition
  `finite-stage-quotient-orientation-character-system`.
- `(D0-Q)` finite-stage orientation package:
  `main.tex`, item `(D0-Q)` in the first-order certificate.
- Dirac--Igusa certificate orientation entry:
  `main.tex`, item `(O_X)`.

## Commands Run

```bash
sed -n '1,260p' AGENTS.md
sed -n '1,260p' CLAUDE.md
sed -n '1,260p' /Users/raeez/ecosystem/INVARIANTS.md
sed -n '1,280p' /Users/raeez/ecosystem/AGENTS-HARNESS.md
sed -n '1,260p' /Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md
sed -n '1,280p' /Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md
sed -n '1,220p' /Users/raeez/igusa-cusp-form/.agents/skills/chriss-ginzburg-rectify/SKILL.md
git status --short --branch
rg -n 'O1|O1\+|orientation|finite stabilizer|finite-stabilizer|stabilizer|Weyl-equivariant|equivariant lift|E\[|torsion|character' main.tex
rg -n 'compact/wrapped|wrapped|finite-stage|D0-Q|orientation character system|quotient-orientation package|Weyl determinant-line cocycle|omega_' main.tex
nl -ba main.tex | sed -n '930,1225p'
nl -ba main.tex | sed -n '1670,1858p'
nl -ba main.tex | sed -n '2440,3495p'
nl -ba main.tex | sed -n '5875,6265p'
nl -ba main.tex | sed -n '8120,8275p'
nl -ba main.tex | sed -n '9128,9245p'
```

Final checks:

```bash
git diff --check -- main.tex notes/seventh_orientation_weyl_attack_heal_report.md
```

passed.

```bash
mkdir -p /tmp/igusa-seventh-orientation-texcheck
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/igusa-seventh-orientation-texcheck main.tex
```

passed as a one-pass TeX syntax check.  It produced expected one-pass
undefined-reference and undefined-citation warnings because BibTeX and
later LaTeX passes were not run.

## Residual Obligations

Unproved `(O1)`: compute and null-trivialize, for every compact/wrapped
finite HN stage and every object, extension, and flag stratum,

```tex
alpha^{red}_{R,S},
alpha^{E,free}_{R,S},
beta^{E,N}_{R,S},
lambda^{E,N}_{R,S}.
```

Unproved `(O1)+`: construct finite-stage determinant-line lifts and prove

```tex
[c_{o,R}]=0,
tau_i^2=1,
omega_{i,R,C}=0
```

compatibly with HN transitions.  If chamber automorphisms are used, the
semidirect cocycle and `S_3` relation coherences remain additional data.

Unproved wall signs: `(O2)` must still compute the three local Pfaffian
normal modes.  Only after `(O1)`, `(O1)+`, and `(O2)` are supplied can the
Hall orientation character be identified with the Maass target character.
