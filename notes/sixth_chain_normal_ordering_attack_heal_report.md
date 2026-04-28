# Sixth Chain Normal-Ordering Attack-Heal Report

Date: 2026-04-28.
Role: S04 Chain Normal-Ordering.
Worktree: `/tmp/igusa-sixth-chain-normal`.
Branch: `agent/igusa-sixth-chain-normal-20260428`.

## Claim Attacked

Obligation (6): construct, or sharply isolate the obstruction to
constructing, the chain-level normal-ordering descent
`\overline\Pi_{X,*}^{\Theta}`, the negative-cyclic lift
`\Theta_\Pi^{-}`, the finite-fibre HN topology, and the obstruction
package
`\mathfrak o_\Theta^{top}`,
`\mathfrak o_\Theta^{Hoch}`,
`\mathfrak o_\Theta^{tri}`,
`\mathfrak o_\Theta^{Jac}`,
`\mathfrak o_F`,
`\mathfrak o_\Theta^{cyc}`,
`\mathfrak o_\Theta^{rad}`.

The requested `notes/sixth_attack_heal_swarm_20260428.md` was not present
in this worktree.  I used `notes/notes/fifth_attack_heal_swarm_20260428.md`,
`notes/notes/attack_heal_swarm_20260428.md`, and the prior chain reports.

## Valid Attacks

1. Central-extension attack.  The formula
   `\Theta_\Pi(c)=\mathsf T_{-\Pi_X(c)}` is formal once the finite
   coefficient dg category exists.  It does not by itself act on compact
   Hall correspondence targets, orientation lines, quotient stacks, cyclic
   complexes, or finite HN transitions.
2. Negative-cyclic attack.  Forgetting
   `(b+uB_C)\Theta_\Pi^-=B_{\mathrm{ch}}^-` to Hochschild cochains can
   recover the Hochschild boundary equation, but it does not construct the
   `S^1`-equivariant lift and does not imply Frobenius cyclicity.
3. Finite-topology attack.  A fibre product over
   `\overline\Pi_X` is legitimate only at finite HN height.  The inverse
   limit exists only if finite fibre, product, coproduct, and pairing
   transition squares commute.
4. Frobenius attack.  Non-degeneracy of the Hopf pairing detects a proved
   Frobenius identity after quotienting by the radical.  It does not
   construct the identity.
5. Radical attack.  Frobenius implies Lie-ideal stability of the radical,
   but not coideal stability and not closedness in the HN topology.
6. Certificate attack.  `D0-N` and `(D_X)` named the seven obstruction
   classes, but did not give a finite verification diagram list sharp
   enough to prevent a false inverse-limit or non-degeneracy transfer.

## Repair Inscribed

- `main.tex`: Definition `normal-ordering-coefficient-dg-category` now
  separates the formal central translation cochain from its non-formal
  compact Hall realization.
- `main.tex`: Theorem `thm:ptvv-joyce-pi-descent` now states the same
  separation inside the hypothesis `(Theta)`.
- `main.tex`: Added Proposition
  `prop:finite-normal-ordering-verification-diagrams`, giving finite
  diagrams `(NO1)--(NO7)` for:
  finite fibres; product/coproduct/pairing transitions; Hochschild and
  negative-cyclic equations; triple flag coherence; Jacobi; Frobenius;
  Lie-ideal radical stability; and Hopf coideal radical stability.
- `main.tex`: `D0-N`, `(D_X)`, and the open `D0` descent obligation now
  reference the finite verification diagrams.

## Exact Finite Obstruction Diagrams

The new finite topology diagram is
```tex
\rho^\Pi_{R^+R}\overline\Pi_{R^+,*}^{\Theta_{R^+}}
=
\overline\Pi_{R,*}^{\Theta_R}\rho_{R^+R}.
```

The finite product and coproduct diagrams are
```tex
\rho^\Pi_{R^+R}m_{R^+}^{\Theta}
=
m_R^{\Theta}(\rho^\Pi_{R^+R}\otimes\rho^\Pi_{R^+R}),

(\rho^\Pi_{R^+R}\otimes\rho^\Pi_{R^+R})\Delta_{R^+}^{\Theta}
=
\Delta_R^{\Theta}\rho^\Pi_{R^+R}.
```

The finite cyclic equations are
```tex
d_{\mathrm{Hoch}}\Theta_{\Pi,R}=B_{\mathrm{ch},R},
\qquad
(b+uB_C)\Theta_{\Pi,R}^{-}=B_{\mathrm{ch},R}^{-}.
```

The finite radical coideal test is
```tex
(\bar q_{\Pi,R}\otimes\bar q_{\Pi,R})\Delta_R^\Theta(r)=0,
\qquad r\in\operatorname{Rad}_R^\Pi.
```

This is independent of the Lie-ideal test
```tex
\langle[x,r]_\Theta,z\rangle_R=0.
```

## Claim Status

Proved: the lattice normal-ordering extension
`\widehat\Gamma_X` and additive map
`\overline\Pi_X(c,T)=\Pi_X(c)-T`; the formal central translation cochain
inside the finite coefficient dg category.

Conditional: chain descent on compact Hall primitives, negative-cyclic
lift, finite-fibre topology, Frobenius cyclicity, and Hopf radical
quotient.  The new proposition gives the finite verification diagrams.

Open: construction of the compact finite-HN Hall/factorization source,
the reduced compact/wrapped orientation and cyclic model, the Serre or
Hall-side cyclic trace proving `\mathfrak o_F=0`, and transition-compatible
closed Hopf radical coideals.

## Commands Run

- `pwd && git status --short --branch`
- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`, ecosystem voice/rubric
  excerpts, and the `chriss-ginzburg-rectify` skill.
- `rg --files` and `rg -n` scans for chain normal-ordering,
  `D0-N`, `(D_X)`, `Theta`, finite topology, Hochschild, cyclic,
  Frobenius, and radical terms.
- `sed -n` / `nl -ba` reads of the lattice normal-ordering theorem,
  coefficient dg category, `thm:ptvv-joyce-pi-descent`, `D0-N`, `(D_X)`,
  and open `D0` descent regions.
- Reads of prior chain reports and swarm ledgers under `notes/notes/`.
- `git diff --check -- main.tex notes/sixth_chain_normal_ordering_attack_heal_report.md`
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-sixth-chain-normal-texcheck-S04 main.tex`
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-sixth-chain-normal-texcheck-S04/main.log`
- `git diff --no-index --check /dev/null notes/sixth_chain_normal_ordering_attack_heal_report.md`

## Verification

- `git diff --check -- main.tex notes/sixth_chain_normal_ordering_attack_heal_report.md`
  passed.
- One-pass `pdflatex` passed and wrote
  `/tmp/igusa-sixth-chain-normal-texcheck-S04/main.pdf`.  It reported
  expected first-pass undefined references and citations because BibTeX
  and reruns were not invoked.
- The fatal-error log scan found no `Undefined control sequence`,
  `Emergency stop`, `Fatal error`, or TeX `!` error lines.
- The no-index whitespace check on the new untracked report emitted no
  whitespace errors.

## Residual

The obstruction is not killed.  It is finite-stage sharp.  To kill it one
must supply `(NO1)--(NO7)` at every successor HN arrow, with composite
non-successor compatibility, then pass to the completed inverse limit.
The scalar determinant, target denominator algebra, and pairing
non-degeneracy do not imply these diagrams.
