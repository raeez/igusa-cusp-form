# A056 - Source Basis Provenance Quarantine

## Claim Attacked

Compact-source primitive bases in finite windows, especially
`W_{\le3}`, are source-constructed from retained stacks, orientations,
and vanishing cycles, not imported from target BKM basis labels
`e_i,E_{ij},u_{ij,r},w_s`.

## Verdict

Conditionally safe, but only if the quarantine is enforced. The current
`main.tex` mostly states the correct firewall: target bases are
reference data; source recognition starts only after compact source
bases, pairings, radicals, quotient maps, matrices, PBW, and comparison
maps are supplied. The dangerous point is semantic drift: the target
labels are convenient enough that a future fixture or theorem could
silently relabel them as source primitives.

## Failure Mode

Dimension equality does not construct a basis. In degree

```tex
\tau=\delta_1+\delta_2+\delta_3
```

the target has

```tex
\rootmult_{\bar0}(\tau)=29,\qquad
\rootmult_{\bar1}(\tau)=93,\qquad
29-93=-64=f(1,1),
```

but a compact source basis still needs actual protected primitive
classes. The automorphism group of a `29|93` vector space already
destroys canonical identification. The label `w_s` is only a target
odd-generator name until a source quotient vector maps to it under
`A_{\tau,\bar1}`.

## Local Anchors

- `main.tex` near line 12556: primitive recognition says the data are
  source-side and not inferred from determinant or signed dimensions.
- `main.tex` near lines 12603 and 12627: source representatives and
  Hall relations are required separately.
- `main.tex` near line 15048: target basis labels are introduced as
  target choices.
- `main.tex` near line 15125: the source must then supply compact bases
  and splittings `K\oplus L`.
- `main.tex` near line 15268: the executable finite source criterion
  requires geometric provenance for every basis vector.
- `main.tex` near line 14012: comparison maps `A_{\gamma,\bar p}` are
  assumed after source splitting and radical quotient, not before.
- `main.tex` near lines 14137 and 14345: point-atlas/Dirac normal form
  is target algebraic normal form; geometric realization is a morphism
  to it, not identity with it.

## Critique Anchors

- A006: target arithmetic is not source data; `W_{\le3}` needs
  `M,D,B,G,K,Q,A_\beta`.
- A049: future use of `e_i,E_{ij},u_{ij,r},w_s` must remain target-side
  until compact source bases and `A_{\beta,\bar p}` exist.
- A050: Chevalley rows are target GN/Kac unless checked as compact Hall
  bracket matrices.
- Guide sections 12 and 15 confirm the same firewall and conditional
  retained theorem.
- CYQG AP-CY378/AP-CY384: target arithmetic is not source matrices;
  target basis choice is not canonical source basis.

## Required Provenance

Every source basis vector needs:

```text
basis_id
finite stage R
root/Gram degree beta
parity
normal-ordered charge lift c_hat with overline(Pi_X)(c_hat)=beta
retained stack/stratum or irreducible critical cycle/IC summand
vanishing-cycle complex
orientation gerbe component/line and chosen trivialization
Thom-Sebastiani transport signs
compact-support/protected integration map
stabilizer/quotient-orientation data
positive/negative pairing-dual data
radical status K or complement L
quotient map Q
product/coproduct incidence matrices from retained correspondences
transition image under R' -> R
```

## Quarantine Rule

`e_i,E_{ij},u_{ij,r},Y_{i;ij},T_i,M_{ij,r},w_s` may appear only in
target fixtures and in the codomain columns of
`A_{\beta,\bar p}:L_{\beta,\bar p}\to
\mathfrak g_{\Delta_5,\beta,\bar p}`. They must not be source
`basis_id`s, provenance witnesses, or names of compact primitives before
`Q` and `A` are supplied. Source names should be neutral, for example
`b^X_{R,\beta,\bar p,a}`.

## Claim-Status Recommendation

Keep primitive recognition, Chevalley verification, `W_{\le3}`,
Pfaffian equality, and retained compact Dirac-Igusa realization
conditional. Do not promote until real source basis certificates and
matrices exist for `W_{\le3}\cup(-W_{\le3})\cup\{0\}`, especially the
`29|93` `\tau`-block.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `sed`, `awk`, `rg`, `find`, and `git status --short`.

## Residual Obligations

Construct the actual `W_{\le3}` source fixture; verify `M,D,B,G,K,Q`,
`QB(P\otimes K)=0`, `QB(K\otimes P)=0`, `(Q\otimes Q)DK=0`, Hopf
adjointness, kernel equality, PBW associated-graded isomorphism, and
strict transition/ML compatibility.

