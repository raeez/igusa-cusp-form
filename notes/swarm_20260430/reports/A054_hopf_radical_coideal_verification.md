# A054 - Hopf Radical and Coideal Verification

## Claim Attacked

Whether the retained compact source proves that the Hopf radical is both
an ideal and a coideal for the source product/coproduct, rather than
assuming this through finite source matrix data.

## Verdict

Not proved unconditionally. The manuscript contains a valid finite
algebraic test for radical descent, but the retained source has not yet
supplied the actual source matrices `M,D,B,G,K,Q`, quotient-tensor
nondegeneracy, or transition-compatible radical kernels. Safe status:
conditional finite matrix criterion, not established source theorem.

## Failure Mode

The good algebraic implication is:

```tex
K_{\beta,\bar p}
  =\ker G_{\beta,\bar p}\cap\ker G_{-\beta,\bar p}^{t},
\qquad
P^X_{R,\beta,\bar p}=K_{\beta,\bar p}\oplus L_{\beta,\bar p},
\qquad
Q_{\beta,\bar p}=[0\ I].
```

With source product/bracket/coproduct matrices

```tex
B_{\alpha,\beta}
  =M_{\alpha,\beta}
   -(-1)^{|x||y|}M_{\beta,\alpha}\tau,
```

NO7 requires

```tex
QB(P\otimes K)=0,\qquad QB(K\otimes P)=0,\qquad
(Q_\mu\otimes Q_\nu)D^\mu_{\rho,\nu}K_\rho=0,
```

plus Hopf adjointness

```tex
M_{\alpha,\beta}^{t}G_{\alpha+\beta}
  =(G_\alpha\otimes G_\beta)D_{\alpha+\beta}^{\alpha,\beta}.
```

Given adjointness and nondegeneracy of the quotient tensor pairing, the
coideal square follows: for `r in K`,

```tex
\langle x\otimes y,\Delta r\rangle
  =\langle M(x,y),r\rangle=0,
```

so `(Q\otimes Q)\Delta(r)=0`. Frobenius gives the Lie-ideal half. This
is proved as a conditional algebra lemma near `main.tex` line 9742.

The missing point is source verification: no retained `W_{\le3}` source
`G`-matrices, radical bases `K_\beta`, quotient maps `Q_\beta`,
coproduct matrices `D`, or transition matrices are actually computed in
the manuscript or `compute/`.

## Local Anchors

- `main.tex` near line 9275: radical obstruction is split into Lie and
  coideal parts.
- `main.tex` near line 9416: Frobenius gives Lie ideal but not coideal;
  coideal and closedness are separate.
- `main.tex` near line 9581: NO7 finite matrix test.
- `main.tex` near line 12680: primitive recognition S5 assumes closed
  radical ideal/coideal and transition-compatible finite kernels.
- `main.tex` near line 12903: R4 requires pairing matrices, kernels
  stable under brackets, coideals for finite coproduct, and transition
  maps.
- `main.tex` near line 15268: source matrix criterion requires
  `M,D,B,G,K,Q`, kernel equality, PBW, and ML transitions.
- `main.tex` near line 15373: `W_{\le3}` NO7 protocol states the finite
  obstruction example `(Q\otimes Q)D(k) != 0`.

## Risk Anchor

The proposition "Primitive matrices from the compact Hall source"
defines `M,D,G,K,Q` and then says base change gives adjunction, hence
the radical is a Lie ideal and coideal. This is safe only as a
conditional statement once the retained compact source, base-change
square, quotient tensor nondegeneracy, and transition-compatible kernels
are supplied. As written, it can read stronger than the available
evidence.

## Critique Anchors

- Guide section 12: `W_{\le3}` needs source `M,D,B,G,K,Q,A_\beta`, not
  target arithmetic.
- Guide section 15: retained theorem is conditional on matrix and
  transition identities.
- CYQG AP-CY378/AP-CY382/AP-CY384: source matrices, good limits, and
  source bases are not automatic.
- A006, A030, A049, and A053 agree: source radical/coideal/PBW remain
  conditional.

## Exact Constants Checked

Local scripts verify target arithmetic only:

```tex
\delta_i:1|0,\quad
\delta_i+\delta_j:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\delta_{123}:29|93.
```

Also `29-93=-64=f(1,1)`, height-four gaps `108|90|18`, and doubled
isotropic gaps `10|9|1`. These do not compute `G,K,Q,D`.

## Claim-Status Recommendation

Retain the Hopf radical statement as: proved after supplied finite
source matrices satisfy NO7, Hopf adjointness, quotient tensor
nondegeneracy, and transition-compatible closedness. Do not state that
the retained source has proved it yet.

If "Hopf ideal" means associative Hall-product ideal, add explicit
`QM(P\otimes K)=QM(K\otimes P)=0` checks, or state that the current
quotient is only the primitive Lie/coLie radical quotient.

## Files Changed

None by the agent.

## Commands and Checks

Read-only audit. The agent read `CLAUDE.md`, `AGENTS.md`, the requested
skill files, `main.tex` regions, A006/A016/A030/A049/A053, guide
sections 12 and 15, and CYQG AP-CY378/AP-CY382/AP-CY384. It ran `rg`,
`sed`, `nl -ba`, `find`, `git status --short`,
`python3 compute/verify_lattice.py`, and
`python3 compute/verify_square_root.py`.

## Residual Obligations

Construct actual compact `W_{\le3}` source bases; compute
`M,D,B,G,K,Q`; verify `QB`, `QD`, Hopf adjointness, quotient tensor
nondegeneracy, source-to-target `A_\beta`, no-extra-relations, PBW
associated gradeds, and transition preservation of radicals/PBW with
`R^1\varprojlim=0`.

