# Agent 6 report: rows F5-F8 and fractional comparison rows

## Claim attacked

Attacked implication:

```tex
Clery--Gritsenko product
  + Govindarajan CHL/WKB denominator
  + fractional comparison notation
=> compact physical row map / reduced CY-DT host / compact Hall-chiral host.
```

Status: false at the present level of data.  The manuscript currently keeps
the separation.  Rows `F5`--`F8` have theorem-level automorphic products and
imported CHL/WKB denominator identities.  They do not have compact CY/DT
scalar hosts, compact Hall/chiral hosts, or physical row-map certificates.
The fractional comparison symbols remain formal comparison symbols unless a
separate parent, cover, cocycle, character root, divisor, and host are
constructed.

## Local anchors

- `main.tex:258-274`: opening certificate discipline.  Rows `1`--`4` have
  Gritsenko--Nikulin denominator theorems; rows `5`--`8` have
  Clery--Gritsenko products and Govindarajan CHL/WKB denominator theorems.
  A physical host still requires group/cover, character, divisor, product
  lattice, Weyl data, physical charge lattice, one-particle index,
  orientation, reduced scalar theorem if claimed, and primitive algebra
  comparison.
- `main.tex:3149-3197`: definition of a five-level physical-host
  certificate `(A_j,D_j,S_j,Z_j,H_j)`.  It explicitly states that product
  row, denominator row, dyon square, reduced scalar host, and compact
  Hall/chiral host are separate structures.
- `main.tex:3199-3224`: Clery--Gritsenko eight-row table: groups, weights,
  characters/multipliers.
- `main.tex:3273-3300`: row ledger.  For `F5`--`F8`, reduced CY/DT and
  compact Hall/chiral columns are explicitly "no certificate".
- `main.tex:3306-3321`: certificate ledger warning; neither Govindarajan
  denominator data nor the `Q_1` twisted CHL row supplies a reduced CY/DT
  scalar host or compact Hall/chiral certificate.
- `main.tex:3968-4069`: Clery--Gritsenko congruence products for
  `F5`--`F8`; the displays pin automorphic products only and explicitly do
  not construct BKM chamber, parity, or Weyl sum.
- `main.tex:4072-4190`: product-degree lattices and cusp-labelled degree
  maps.  For `F7`, the `c_{7,M}/2` exponent is only sourced on the
  `mu_4` multiplier-cover normalization.
- `main.tex:4338-4446`: Govindarajan CHL/WKB denominator theorem for
  `F5`--`F8`.  It constructs real roots, Weyl chambers, reflection
  character, and imaginary-root data, but states this is not a physical row
  map and not a CY/DT/chiral host.
- `main.tex:4448-4463`: `F7` is a `mu_4`-cover denominator identity; the
  scalar square does not carry reflection sign, parity, Weyl chamber, or
  Weyl-alternating side.
- `main.tex:4757-4814`: comparison row systems.  The tuple
  `(5,2,1,1,1/2,1,1/4,0)` is not the Clery--Gritsenko row system and gives
  no physical atlas.  Direct identifications of comparison symbols with
  `F5,F7,F8` are false by weight.
- `main.tex:4816-4919`: fractional-branch test and open problem.  Formal
  roots do not become modular or chiral objects without cover/character
  data and the five-level physical-host certificate.
- `calabi-yau-quantum-groups/FRONTIER.md:43-45`: Vol III records only the
  eight-row `kappa_BKM = c_N(0)/2` computation and cover stratification; it
  also states that the catalogue has no weight-0 or quarter-weight row.
- `calabi-yau-quantum-groups/FRONTIER.md:63`: Vol III separates the CHL
  trace scope from the Clery--Gritsenko eight-form catalogue.

## Primary source anchors

- Clery--Gritsenko, *The Siegel modular forms of genus 2 with the simplest
  divisor*, PLMS 2011, arXiv:0812.3962.  Local bib: `proj.bib:100-110`.
  Manuscript cites Theorem 1.4 for the eight-row classification and
  Theorem 3.1 plus Section 3 product displays for `nabla_3`, `nabla_2`,
  `nabla_{3/2}`, and `Q_1`.
- Govindarajan, *BKM Lie superalgebras from counting twisted CHL dyons*,
  JHEP 2011, arXiv:1006.3472.  Local bib: `proj.bib:148-158`.  Manuscript
  uses Sections 4.2-4.3, Table 3, and Appendices C-D for the CHL/WKB
  denominator rows.
- Cheng--Dabholkar, *Borcherds--Kac--Moody symmetry of N=4 dyons*, CNTP
  2009, arXiv:0809.4258.  Local bib: `proj.bib:136-146`.  Used for the
  common CHL Weyl chamber/root-lattice mechanism.
- Govindarajan--Gopala Krishna, *Generalized Kac--Moody Algebras from CHL
  dyons*, JHEP 2009, arXiv:0807.4451, and composite `N=4` sequel,
  arXiv:0907.1410.  Local bib: `proj.bib:112-134`.  Used for scalar
  square-root and CHL denominator normalizations.

ArXiv cross-check: the Clery--Gritsenko abstract states exactly eight
genus-2 Siegel modular forms vanishing along the diagonal; the Govindarajan
abstract states that the square roots of the twisted CHL Siegel modular forms
are the Clery--Gritsenko dd-modular forms and arise as WKB denominator
formulae.  Neither abstract claims compact CY/DT or Hall/chiral hosts.

## Exact row data

Present Igusa order:

| row | form | `(t,N)` | group/cover | weight | `c(0)` | status |
| --- | --- | --- | --- | --- | --- | --- |
| `F5` | `nabla_3` | `(1,2)` | `Gamma_0^(2)(2)`, `chi_2^(2) x v_H` | `3` | `6` | CG product; Govindarajan `G_1(2)` denominator; scalar square `nabla_3^2 = Phi_6`; no CY/DT or Hall/chiral host |
| `F6` | `nabla_2` | `(1,3)` | `Gamma_0^(2)(3)`, `chi_2^(3) x v_H` | `2` | `4` | CG product; Govindarajan `G_1(3)` denominator; scalar square `nabla_2^2 = Phi_4`; no CY/DT or Hall/chiral host |
| `F7` | `nabla_{3/2}` | `(1,4)` | `Gamma_0^(2)(4)` on `mu_4` multiplier cover, `chi_4^(4) x v_H` | `3/2` | `3` | CG product; Govindarajan `G_1(4)` denominator on cover; scalar square only after cover/branch; no CY/DT or Hall/chiral host |
| `F8` | `Q_1` | `(2,2)` | `Gamma_2(2)`, `chi_4^(2) x v_H` | `1` | `2` | CG product; Govindarajan `G_2(4)` denominator; twisted square `Q_1^2 = Phi_2^(2,4)`; no CY/DT or Hall/chiral host |

Triple order weights and constants agree with Vol III:

```tex
(1,1),(2,1),(1,2),(3,1),(1,3),(4,1),(1,4),(2,2)
weights: 5,2,3,1,2,1/2,3/2,1
c(0):    10,4,6,2,4,1,3,2
kappa_BKM = c(0)/2.
```

Present `F`-order weights:

```tex
(5,2,1,1/2,3,2,3/2,1).
```

The product lattices and Weyl data are:

- `F5,F6,F7`: `L=M_1=U(4) + <2>`, `rho=alpha_1(1/2,1/2,1/2)`,
  `P={(0,-1,0),(1,1,0),(0,1,1)}`, reflection character `det`.
- `F8`: `L=M_2=U(8) + <2>`, `rho=alpha_2(1/4,1/2,1/4)`,
  `P={(0,-1,0),(1,1,0),(1,3,1),(0,1,1)}`, reflection character `det`.
- Cusp-labelled product maps are those in `main.tex:4088-4107`; the
  `F7` middle cusp carries `tilde c_{7,M}=c_{7,M}/2` only on the sourced
  `mu_4` cover.

## Fractional comparison rows

The manuscript correctly rejects the direct identifications

```tex
Phi_cmp_5 = F5,   Phi_cmp_7 = F7,   Phi_cmp_8 = F8.
```

Reason: the comparison weights `(5,2,1,1,1/2,1,1/4,0)` are not the
Clery--Gritsenko row weights.  The catalogue has no weight-`1/4` row and
no weight-`0` row.  The `mu_4` cover of `F7` of weight `3/2` is not a
quarter-weight modular-root certificate.  A weight-0 comparison symbol has
only a formal logarithmic branch until a divisor divisibility theorem and a
finite-order character/cocycle root are constructed.

## Overclaim search result

No active overclaim found in `main.tex` or `FRONTIER.md` for this task.
The current text consistently marks:

- rows `F5`--`F8`: automorphic product plus CHL/WKB denominator only;
- scalar squares: sourced scalar identities, not row maps;
- `F7`: cover-sensitive `mu_4` denominator identity, not a physical
  comparison row;
- fractional comparison symbols: conditional/formal until separate host,
  cover, character, and branch data are constructed.

Vol III `FRONTIER.md:83` says CHL models at orders `{2,3,4,6}` admit
rigorous Borcherds-host inscriptions.  This should continue to be read as
denominator/Borcherds-host status, not as a compact CY/DT or Hall/chiral
physical row-map theorem.

## Status recommendation

Keep the manuscript status unchanged:

```tex
F5-F8: product theorem + CHL/WKB denominator theorem.
No reduced CY/DT scalar host.
No compact Hall/chiral host.
No physical row map.
Fractional comparison rows: formal/conditional only.
```

Do not promote scalar squares or Vol III `kappa_BKM` computations to physical
row maps.  Any future promotion must fill the five certificate entries of
Definition `physical-host-certificate`.

## Files changed

- Created this disjoint report:
  `notes/attack_heal_20260427/agent6_rows5_8_fractional.md`.

No shared manuscript, bibliography, compute file, or git state was mutated.

## Tests and computations

Read/grep audit only:

- `sed`/`nl -ba` reads of `CLAUDE.md`, ecosystem invariants, `main.tex`,
  `proj.bib`, Vol III `FRONTIER.md`, and relevant `agent_material` audits.
- `rg` searches for `Clery/Gritsenko`, `row`, `fractional`, `cover`,
  `character`, `host`, `physical`, `compact Hall`, `CY/DT`, `quarter`,
  and `weight-0`.
- Web/arXiv title/abstract check for arXiv:0812.3962 and arXiv:1006.3472.

No `make` run: this is a standalone markdown report.

## Remaining open obligations

For each of `F5,F6,F7,F8`, construct:

1. A host `X_j` or CHL/orbifold background with oriented reduced
   obstruction theory, if a scalar host is claimed.
2. A physical charge lattice and chamber mapping to the same product lattice
   and cusp-labelled degree maps as the Clery--Gritsenko product.
3. A protected one-particle index with signed superdimensions equal to all
   cusp-labelled product coefficients, including `F7` on the `mu_4` cover.
4. An orientation/reflection character compatible with the automorphic
   character and the CHL Weyl determinant.
5. A primitive compact Hall/chiral bracket comparison to the Govindarajan
   denominator algebra preserving `P_j`, `M_j`, `W_j`, `epsilon_j`,
   `rho_j`, `mu_j`, and `N_j(a)`.
6. For fractional comparison symbols, a separate modular-root certificate:
   parent form, root exponent, exact group or cover, character-root order,
   automorphy cocycle, divisor multiplicities, branch, and source theorem.
