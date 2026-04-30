# A069 - Supremum Primitive Recognition Theorem Ladder

Proposal-only report. No files edited or reverted by the agent.

## Anchors

Core anchors:

- Primitive recognition: `main.tex` near line 12488.
- Cofinal finite datum: `main.tex` near line 12848.
- Global cofinal equivalence: `main.tex` near line 12959.
- Source matrices: `main.tex` near line 13836.
- Comparison maps `A_\beta`: `main.tex` near line 14012.
- `W_{\le3}` window: `main.tex` near line 15004.
- Executable criterion: `main.tex` near line 15268.
- NO7 protocol: `main.tex` near line 15373.
- ML data: `main.tex` near line 11114.
- Compact datum: `main.tex` near line 12111.
- Conditional finite source theorem: `main.tex` near line 14445.
- Guide section 12: `notes/attack_whitepaper_analysis_20260430_guide.md`
  near line 358.

Reports A049-A064 and A067 were read. A065/A066 were not archived when
the agent ran, but they are now archived.

## Theorem 1

Finite `W_{\le3}` Certificate Theorem.

Hypotheses: a compact Hall stage `R` supplies a populated source fixture
on

```tex
S_{\le3}=W_{\le3}\cup(-W_{\le3})\cup\{0\},
\quad
W_{\le3}=\{\sum c_i\delta_i:c_i\ge0,\ 1\le\sum c_i\le3\}.
```

The fixture contains neutral source bases with provenance, full parity
blocks, `M,D,B,G,K,Q`, splittings
`P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p}`,
quotient maps, `A_{\beta,\bar p}:L_{\beta,\bar p}\to
\mathfrak g_{\Delta_5,\beta,\bar p}`, NO7 identities, Hopf adjointness,
quotient-tensor nondegeneracy, finite kernel equality, PBW
associated-graded isomorphism, and strict successor-transition rows.
Target labels `e_i,E_{ij},u_{ij,r},w_s` occur only in target tables or
`A`-codomain columns.

Conclusion: the finite map

```tex
G(\mathscr B_{\Delta_5})_{W_{\le3}}
\to P^{\Pi,\mathrm{red}}_{X,R,W_{\le3}}
```

is an isomorphism of finite Gram-graded Lie superalgebras with parity. It
certifies the `1|0,10|0,1|0,29|93` window, Jacobi
`T_1+T_2+T_3=0`, the 27 mixed maps, NO7 radical descent,
no-extra-relations, and PBW in this window.

Proof skeleton: relation rows put the finite Borcherds-Kac ideal in
`\ker\pi_{R,W}`; NO7 and Hopf adjointness make the radical a Hopf
ideal/coideal; `A_\beta` intertwines bracket, coproduct, pairing, Cartan
action; kernel equality gives injectivity; generation gives
surjectivity; PBW ranks rule out hidden completed relations.

Open data: the actual compact `W_{\le3}` fixture is not populated. The
`29|93` source block, `M,D,B,G,K,Q,A_\beta`, kernel ranks, PBW ranks, and
ML transition ranks remain open.

## Theorem 2

Enlarged `W_{\le7}` Relation-Closure Theorem.

Hypotheses: the `W_{\le3}` certificate extends to the
downward-saturated relation-closure window

```tex
W_{\le7}=\{\sum c_i\delta_i:c_i\ge0,\ 1\le\sum c_i\le7\},
```

with the same source fixture packet on `S_{\le7}`. The verified relation
rows include all terminal rows deferred by `W_{\le3}`: height-four real
Serre terminal rows, doubled-isotropic rows, first `[e_i,w_s]`
height-four maps, height-six `(\operatorname{ad}e_i)^3w_s=0` rows,
odd-odd `\tau` rows required by the chosen GN/Kac presentation, and
height-seven complementary strings
`(\operatorname{ad}e_k)^5u_{ij,r}=0`. It also includes full parity
target dimensions from the imported GN/Kac datum for every
`\beta\in W_{\le7}`, not just signed exponents.

Conclusion: the source is isomorphic to the GN/Kac target on
`W_{\le7}`, and every defining relation whose first nontrivial prefixes
occur in `W_{\le3}` has been closed by an actual terminal source row. The
`W_{\le3}` theorem is then not merely a visible-prefix certificate; it is
relation-closed through the first real-string and timelike terminal
obstructions.

Proof skeleton: apply the finite source matrix recognition criterion to
`W_{\le7}`. Downward saturation makes every needed word finite.
No-extra kernel equality absorbs precisely the BK ideal plus GN radical.
PBW associated-graded ranks prove that the height-four/six/seven rows
introduce no hidden source relations beyond the target presentation.

Open data: the full `W_{\le7}` target parity table, source relation row
list, compact bases, source matrices, radical/PBW ranks, and transition
certificates are still open. Verified arithmetic only confirms target
numbers: `29|93`, height-four `108|90|18`, doubled-isotropic `10|9|1`,
real-real exponent `3`, complementary isotropic exponent `5`, and
`\delta_i`-`\tau` exponent `3`.

## Theorem 3

Cofinal ML Completion Theorem.

Hypotheses: a countable cofinal HN subsystem `R_0<R_1<...` and cofinal
downward-saturated windows `W_\nu` are supplied, starting with the
`W_{\le7}` relation-closed packet. For every `R_\nu,W_\nu`, the finite
source certificate above holds. Transition matrices preserve
`M,D,B,G,K,Q,A_\beta`, radical kernels, source coalgebras, PBW
filtrations, kernels/cokernels, cones, parity pieces, and orientation
data strictly. Finite-slice ML stable-image rank equalities hold for
every declared tower.

Conclusion:

```tex
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}
```

as completed Gram-graded Lie superalgebras. If the chiral Koszul source
datum is also supplied, then

```tex
\Omega_E^{\mathrm{ch}}C_X\simeq\mathsf{Den}_{\Delta_5,E}.
```

Proof skeleton: finite certificates give isomorphisms on every `W_\nu`.
Strict transitions commute with quotients, radicals, PBW gradeds, and
kernels. ML gives `R^1\varprojlim=0`. Cofinality exhausts `\mathcal R_+`.
No relation, radical element, generator, or parity-cancelling summand
appears only after completion.

Open data: the cofinal retained schedule, transition matrices,
stable-image ranks, closed radical proof, exact triangular completion,
and chamber/wall compatibility remain open.

## Corollary

Compact Dirac-Igusa Realization Corollary.

Hypotheses: the compact `K3 x E` datum
`\mathfrak K_X=(L_X,H_X,O_X,D_X,R_X)` is actually constructed: finite
Hall stacks and correspondences, quotient orientation gerbes, type-II
wall Pfaffian charts, hybrid local/wrapped atlas, protected integration,
first-order Dirac blocks, Pfaffian line and line comparison, source
chiral coalgebra, Koszul comparison, and the cofinal primitive
certificate of Theorem 3.

Conclusion:

```tex
\epsilon_o|_{W^{(2)}(\Lambda^{2,1}_{II})}
  =\nu_{\Delta_5}|_{W^{(2)}(\Lambda^{2,1}_{II})},
\quad
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5},
\quad
\Omega_E^{\mathrm{ch}}C_X\simeq\mathsf{Den}_{\Delta_5,E},
```

and the normalized Pfaffian cusp expansion is

```tex
\operatorname{pf}_X|_{\mathfrak c_\infty}
=
64q^{1/2}r^{1/2}s^{1/2}
\prod(1-q^nr^ls^m)^{f(nm,l)}
=\Delta_5(Z).
```

Proof skeleton: `D_0` supplies the finite Hall/Pfaffian state object;
orientation data fixes the Weyl character; Theorem 3 identifies
primitives with `\mathfrak g_{\Delta_5}`; Koszul data identifies the
source current envelope; the imported Borcherds product gives the final
`\Delta_5` equality.

Residual obstruction: every geometric source object in this corollary
remains to be constructed. The target reference tower and point-atlas
normal form do not prove compact realization.

## Commands Run

Read-only `sed`, `nl -ba`, `rg`, `find`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`;
`git status --short`. The arithmetic scripts passed.

