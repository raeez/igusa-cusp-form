# Agent 1 attack/heal: compact BPS Hilbert space and operator product

## Claim attacked

The manuscript must not claim that the Igusa determinant, the OP/DT scalar
square, or the Gritsenko--Nikulin denominator algebra constructs a
microscopic compact \(K3\times E\) BPS Hilbert space or a compact BPS
operator product.

## Verdict

Safe.  I found no theorem, abstract sentence, introduction sentence, or
recognition statement in `main.tex` asserting such a construction.

The manuscript consistently separates:

- theorem-level protected index:
  \(Z_{\mathrm{K3}}=2\phi_{0,1}\);
- virtual determinant:
  \[
  \mathcal D_X
  =64q^{1/2}r^{1/2}s^{1/2}
  \prod_{(n,l,m)\in\Gamma_{\mathrm{eff}}}
  (1-q^nr^ls^m)^{f(nm,l)}
  =\Delta_5;
  \]
- imported denominator algebra:
  \[
  \operatorname{den}(\mathfrak g_{\Delta_5})
  =64^{-1}\Delta_5(2Z),\qquad
  \smult\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
  \]
  on active support;
- imported scalar branch:
  \[
  Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}=-4096\,\Delta_5^{-2};
  \]
- open compact realization datum:
  \[
  \mathfrak K_X
  =(\mathcal A^{E_3}_X,\mathrm{Sp}^{\mathrm{ch}}_{K3,E},
  \mathcal F_X,\mathcal H_X,C_X,\Theta_{\mathrm{Kos}},\Pi_{\mathrm{rec}}).
  \]

The determinant gives a Grothendieck-class shadow.  It does not determine
parity dimensions, Hall constants, PBW, no-extra-relations, or a compact
operator product.

## Local anchors

- `main.tex:55-120`: abstract states that the Borcherds half gives only a
  virtual one-particle determinant, not a microscopic Hilbert space, and
  that compact Hall/factorization realization is open.
- `main.tex:129-215`: introduction orders the logic and marks compact
  factorization and primitive recognition as open/conditional.
- `main.tex:441-515`: K3 RR Hilbert space is only the supplied worldsheet
  input for the K3 protected index; it is not the compact \(K3\times E\)
  D-brane Hilbert space.  The half-index object is only a \(K_0\)
  representative; no parity lift or operator product is implied.
- `main.tex:611-637`: the virtual determinant proposition explicitly says
  no Hilbert space, vertex algebra, \(E_3\)-factorization algebra, chiral
  factorization algebra, composition maps, operator products, locality, or
  Hilbert completion are constructed.
- `main.tex:830-940`: reduced OP/DT quotient integration lands in numbers;
  it is not Hall product, CoHA integration, or orientation character.
- `main.tex:1842-1844`: the denominator theorem concerns the imported BKM
  algebra; a microscopic BPS Hilbert space and operator product require
  separate construction.
- `main.tex:1917-1995`: the \(E_3\) source is a supplied Stage-1 datum, not
  a functor constructed on \(K3\times E\).
- `main.tex:2097-2180`: positive elliptic degree projects onto all of \(E\);
  naive Ran locality misses the \(s\)-direction and needs a hybrid wrapped
  or mixed local/global Hall repair.
- `main.tex:2272-2367`: the compact Igusa realization datum correctly lists
  the missing \(E_3\), specialization, Hall, orientation, bar-cobar, and
  primitive-recognition data.
- `main.tex:2370-2478`: the primitive recognition theorem is conditional and
  states that no compact Hall object, primitive bracket constants, parity
  dimensions, simple primitives, no-extra-relations theorem, PBW theorem,
  or closed Hall radical is proved.
- `main.tex:2524-2551` and `main.tex:2756-2865`: determinant/product data
  do not determine Hall constants, full parity dimensions, root spaces of
  zero superdimension, or structure constants.
- `main.tex:2916-3066`: main synthesis explicitly says the dictionary is not
  an equality of Hilbert spaces, brackets, or Hall structure constants.
- `main.tex:3128-3333`, `main.tex:4730-4814`, `main.tex:4892-4918`:
  boundary-row language is certificate-based; physical row maps, scalar
  hosts, compact Hall/chiral hosts, and fractional comparison rows remain
  conditional on separate data.

## Primary-source anchors

- `proj.bib:51-56`: Eichler--Zagier normalization for
  \(Z_{\mathrm{K3}}=2\phi_{0,1}\).
- `proj.bib:64-98`: Gritsenko--Nikulin denominator-algebra sources.
- `proj.bib:170-189`: Borcherds product sources.
- `proj.bib:191-230`, `proj.bib:306-317`: Oberdieck--Pixton,
  Oberdieck--Pandharipande, Oberdieck, Bryan for the reduced scalar
  curve-counting branch.
- `proj.bib:253-275`: Kontsevich--Soibelman and Davison--Meinhardt supply
  CoHA language, not this compact \(K3\times E\) datum.
- `proj.bib:277-304`: Costello--Gwilliam supplies factorization-algebra
  language for observables; the compact \(K3\times E\) \(E_3\) source is
  still a construction problem here.
- `proj.bib:37-42`: Beilinson--Drinfeld supplies chiral-algebra language
  for collision maps, not a compact BPS source.
- `proj.bib:339-347`: Harvey--Moore is only used as external physical
  interpretation of BPS algebras.

## Cross-repo consistency

`~/calabi-yau-quantum-groups/FRONTIER.md` agrees with the manuscript's
separation.  It marks bracket-level BPS \(\cong\) BKM as open
(`FRONTIER.md:81`) and says the Hall--Drinfeld/BKM real-root completion
and comparison data remain open beyond the abelian Heisenberg/Miki core
(`FRONTIER.md:198`).  Its chain-level
\(\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\) and sharpened
\(\mathbf H_{\Delta_5}\) targets (`FRONTIER.md:9-11`) are programme
targets, not facts imported into `main.tex`.

## Failure mode tested

The only possible ambiguity is rhetorical, not mathematical: the abstract
says the denominator algebra supplies the "algebraic square root target"
(`main.tex:90-92`).  A hostile reader could ask whether the BKM bracket is
being advertised as the compact BPS operator product.  The surrounding
sentences already block that reading, and later sections state the
distinction repeatedly.  No fatal overclaim follows.

## Exact repair, if the main thread wants a sharper abstract

Optional replacement for `main.tex:90-92`:

```tex
Thus the denominator algebra supplies the algebraic square-root target
and its target-internal Borcherds bracket; it does not supply a compact
BPS Hilbert space, compact Hall correspondences, an orientation, or a
BPS operator product/local collision map.
```

This strengthens the boundary without demoting the proved/imported
Gritsenko--Nikulin bracket.

## Claim-status recommendation

Keep the current claim strength.  The abstract, introduction, determinant
section, recognition theorem, and row ledger are mathematically honest.
At most add the abstract sharpening above to make the target-internal
Borcherds bracket versus compact BPS operator product distinction visible
on the first page.

## Files changed

- Added `notes/attack_heal_20260427/agent1_bps_hilbert_operator_product.md`.
- No manuscript files changed.

## Computations and builds

- Ran targeted `rg` searches for `BPS`, `Hilbert`, `operator product`,
  `OPE`, `primitive`, `protected`, `local observables`, `Hall`,
  `orientation`, `wrapped`, `factorization`, `E_3`, row maps, and
  fractional comparisons.
- Read `CLAUDE.md`, `INVARIANTS.md` section IV, `AGENTS-HARNESS.md`
  section VIII, `main.tex`, `proj.bib`, and the relevant
  `FRONTIER.md` anchors.
- No build run; this was a read-only attack/heal report except for the
  disjoint notes file.

## Remaining open obligations

- Construct an honest compact one-particle object with the stated
  superdimensions, if it exists.
- Construct the finite-first holomorphic \(E_3\)-factorization algebra on
  \(K3\times E\), including descent, QME/anomaly control, formality point,
  \(S^3\)-framing, and HN completion.
- Construct the hybrid wrapped or mixed local/global Hall theory for
  positive elliptic degree.
- Construct the strong orientation and prove
  \(\epsilon_o=\nu_{\Delta_5}\) on the type-II Weyl group.
- Prove primitive representatives, Hall bracket constants, full parity
  dimensions, no-extra-relations, completed PBW, and radical compatibility.
- For rows \(5\)--\(8\) and fractional comparison symbols, construct
  separate physical host, cover, character, scalar, and compact Hall/chiral
  certificates before any physical row-map claim.
