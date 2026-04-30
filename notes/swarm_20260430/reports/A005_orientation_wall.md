# A005 report: orientation gerbe and type-II wall signs

Runtime id: `019ddbc5-075b-7033-aa50-9730f6f40261`.
Nickname: Laplace.
Status: completed.
Files changed by agent: none.

## Valid Attacks

### Orientation-Gerbe-First Wording

The finite source theorem wording remains vulnerable. `main.tex:13036`
packages `RedOr` as reduced orientation lines and `main.tex:13077`
writes the Darboux-chart line \(\det \operatorname{Ext}^{1,-1}_{red}\).
This is acceptable only as a supplied local section after the
square-root gerbe and quotient descent data vanish. It is not a
construction of global orientation.

Correct boundary:
cite the quotient-orientation character system at `main.tex:4107` as
the actual finite datum.

### Connected/Finite Quotient Orientation

The manuscript mostly heals the old error by separating \(BE\) from
\(BE[N]\): `main.tex:3317`, `main.tex:3390`.

Residual attack:
no use of \(\beta^H\in H^2(BH)\) is valid until mixed Borel terms,
stabilizer action, and spectral-sequence differentials are killed.

Anchors:
`main.tex:3386`, `main.tex:4144`.

### Finite-Stabilizer Linearization

Finite-stabilizer linearization remains a real residual, not a
consequence of translation invariance. The current text correctly says a
fixed underlying line may carry nontrivial character: `main.tex:3433`.

Required calculation:
compute the actual action on reduced trace, semiregularity, anchors,
framings, Thom--Sebastiani, flags, and transition data.

Critique anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:37177`.

### Type-II Pfaffian Wall Signs

The local sign theorem is correctly conditional on chart, splitting,
invariant unit, rank, and transitions: `main.tex:1040`.

The phrase "higher terms do not alter" in the rank-one Ext criterion
needs the explicit equivariant real/parametric Morse lemma and
orientation-unit check. Without that, the Pfaffian block is not derived.

Anchor:
`main.tex:13406`.

### Graph-Isogeny Atoms

Graph-isogeny atoms cannot close the sign theorem. The guide correctly
says \(B_2=i_{\Gamma_\varphi,*}L\) is only a candidate. The stronger
whitepaper claims "actual representative" and "proves each wall atom"
overreach. The Koszul Ext calculation is local/unreduced; it does not
prove semistability, wall equality, full charge matching, reduced normal
quotient, quotient orientation, invariant unit, or atlas compatibility.

Anchors:
`notes/attack_whitepaper_analysis_20260430_guide.md:282`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:35002`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44861`.

## Correct Boundaries

`dirac-pfaffian-recognition` is conditional on supplied
`D0/O1/O1+/O2`, not a compact source construction.

Finite quotient orientation is a Borel--Cech criterion after filtration
splitting, not a vanishing theorem.

Local Pfaffian wall sign proves \(-1\) only after the O2/hybrid residual
vanishes.

Middle wall wrappedness is proved in `main.tex:13419`; graph-isogeny is
only a possible retained atom.

## Residual Obligations

1. Compute \(\alpha_{red}\), \(\alpha_{E,free}\),
   \(\widetilde\beta^H\), and \(\lambda^H\) on every retained object,
   extension, mixed, wrapped, and flag stratum.
2. For \(\delta_2\), prove Liu-heart membership, semistability, exact
   wall equality, full \(\widehat\Gamma\) charge match, anchor law,
   reduced Ext normal quotient, \(s_{\delta_2}\) chart, invariant
   Pfaffian unit, and overlap/transition compatibility.
3. Construct analogous actual atoms for \(\delta_1,\delta_3\).
4. Kill the Weyl determinant-line cocycle \(c_o\) and quotient torsor
   defects \(\omega_{i,C}\); only then do three signs define the global
   character.

Commands run by agent: read-only `sed`, `nl`, `rg`, CYQG AP lookup, and
`git status --short`. No build.
