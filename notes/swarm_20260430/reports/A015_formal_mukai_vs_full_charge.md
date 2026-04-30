# A015 report: formal Mukai sector versus full \(N=4\) charge lattice

Runtime id: `019ddbd1-b29b-7591-a09d-f01333840fbc`.
Nickname: Galileo.
Status: completed.
Files changed by agent: none.

## Verdict

Mostly healed. The manuscript explicitly separates the formal Mukai
sector from the full \(4d\ \mathcal N=4\) charge lattice at
`main.tex:260` and `main.tex:4423`. Residual risk is terminology leakage
from legacy \(\Gamma_X^{\mathrm{phys}}\) and phrases like "physical
lifts."

## Valid Attacks

### \(\Gamma_X^{\mathrm{phys}}\) Can Read Too Broadly

Anchors:
`main.tex:4765`, `main.tex:5084`, `main.tex:5140`.
CYQG lock: `first_principles_cache.md:654`.

Safe phrase:
the formal even dyonic Mukai sector
\(\Gamma_X^{\mathrm{form}}=\widetilde H(S,\mathbb Z)\oplus
\widetilde H(S,\mathbb Z)\); where \(\Gamma_X^{\mathrm{phys}}\) is
retained, it is only mnemonic for this sector, not the full
four-dimensional \(\mathcal N=4\) electric-magnetic charge lattice.

### Formal Lift Does Not Imply Hall Support

Anchors:
`main.tex:4625`, `main.tex:4670`, `main.tex:8944`.

Safe phrase:
every Gram triple has a primitive saturated formal Mukai lift; this does
not prove algebraicity, effectivity, stability, nonempty compact moduli,
or Hall support.

### \((n,l,m)\) Is Not a Hall Charge

Anchors:
`main.tex:4400`, `main.tex:4524`, `main.tex:4966`.
CYQG lock: `first_principles_cache.md:642`.

Safe phrase:
\((n,l,m)\) is the Gram/Fourier/root degree
\(\Pi_X(Q,P)=(Q^2/2,Q\cdot P,P^2/2)\), obtained from an additive Mukai
charge only after normal-ordered pushforward through
\(\widehat\Gamma_X\).

### D6-D2-D0/OP Is A Sector

Anchors:
`main.tex:2723`, `main.tex:2737`, `main.tex:4427`.
Critique anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:5258`.

Safe phrase:
in the algebraic even D-brane sector relevant to the D6-D2-D0/OP branch.

### \(\mathrm{Sp}_4(\mathbb Z)\) Is Automorphic Symmetry

Anchors:
`main.tex:5185`, `main.tex:5294`.
Critique anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:616`.

Safe phrase:
\(G_{\mathrm{aut}}=\mathrm{PSp}_4(\mathbb Z)\) is the automorphic
symmetry of the genus-two chemical potential and invariant Gram plane;
it is not asserted to be the full microscopic T-/U-duality group of the
compactification.

### Genus-Two Potential Records Rank-Two Gram Data

Anchors:
`main.tex:4550`, `main.tex:4484`.

Safe phrase:
\(Z\) couples to the Gram invariants of a chosen electric-magnetic pair;
wall-crossing splittings and Hall brackets live upstairs in the additive
charge sector.

## Residual Obligations

Replace isolated "physical lifts/group/pair" wording by "formal Mukai
lifts/sector" unless full \(\mathcal N=4\) data is explicitly supplied.

If the paper asserts an embedding into the full type-II charge lattice,
define that lattice and cite primary physics sources.

Prefer "Automorphic symmetry datum" over "Automorphic duality datum"
unless the paragraph repeats the U-duality caveat.

Commands run by agent:
read-only `sed`, `rg`, and `nl -ba ... | sed -n ...` over `CLAUDE.md`,
skill instructions, `main.tex`, `proj.bib`, guide, processed critique,
and CYQG `appendices/first_principles_cache.md`.
