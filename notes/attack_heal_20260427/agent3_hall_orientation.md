# Agent 3 attack/heal: Hall orientation theory and epsilon_o

## Claim attacked

The manuscript must not claim that the OP/DT Behrend-weighted scalar
branch, the theta-normalized Borcherds determinant, or the Maass
reflection character constructs the compact Hall orientation datum.  The
geometric comparison
\[
\epsilon_o|_{W^{(2)}(\Lambda^{2,1}_{II})}
=
\nu_{\Delta_5}|_{W^{(2)}(\Lambda^{2,1}_{II})}
\]
must remain a required datum until a strong orientation, lifted Weyl
action, and orientation-line monodromy computation have been built.

## Verdict

Safe.  I found no theorem in `main.tex` asserting a constructed compact
Hall orientation theory or deriving \(\epsilon_o=\nu_{\Delta_5}\) from
the determinant or OP scalar branch.

The manuscript consistently separates five layers:

- Behrend-weighted scalar integration:
  \[
  \int_{\mathrm{Hilb}^n(X,(\beta,d))/E}\nu_{\mathrm{Hilb}}\,de,
  \qquad
  Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}=-4096\Delta_5^{-2}.
  \]
- Theta/Borcherds normalization:
  \[
  [q^{1/2}r^{1/2}s^{1/2}]\Delta_5=64,\qquad
  D_5=64^{-1}\Delta_5.
  \]
- OP scalar conversion:
  \[
  \chi_{10}^{\mathrm{OP}}=D_5^2=4096^{-1}\Delta_5^2,\qquad
  Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}.
  \]
- Automorphic reflection character:
  \[
  \Delta_5|_5g=\nu_{\Delta_5}(g)\Delta_5,\qquad
  \nu_{\Delta_5}(s_{\delta_i})=-1,\ i=1,2,3.
  \]
- Open geometric Hall orientation:
  \[
  \epsilon_o:W^{(2)}(\Lambda^{2,1}_{II})\to\{\pm1\}
  \]
  from a strong orientation on the reduced compact critical Hall/CoHA
  theory.

The only notation hazard is `main.tex:728-740`, where
\(\epsilon_{\det}:=\nu_{\Delta_5}\) is named "determinant sign."  The
symbol is not \(\epsilon_o\), and later text explicitly says that the
Hall orientation character is not produced by normalizing \(\Delta_5\).
No manuscript repair is required.

## Local anchors

- `main.tex:94-106`: the abstract identifies the OP sign and \(4096\) as
  scalar normalization, and says neither fixes the automorphic reflection
  character or compact orientation monodromy.
- `main.tex:231-256`: the introduction gives the exact normalization
  chain and states that \(\epsilon_o=\nu_{\Delta_5}\) remains part of the
  open compact realization datum.
- `main.tex:728-740`: \(\epsilon_{\det}:=\nu_{\Delta_5}\) is the
  automorphic determinant sign; this is not the Hall orientation
  character \(\epsilon_o\).
- `main.tex:857-879`: reduced scalar quotient integration lands in
  numbers; it is not a Hall product, CoHA integration map, or orientation
  character.
- `main.tex:912-940`: protected Hall integration would require an
  extension-closed compact Hall/CoHA sector, oriented critical extension
  correspondences, vanishing-cycle coefficients, HN completion, protected
  integration, primitive projection, and lifted Weyl action.
- `main.tex:942-963`: orientation monodromy is an open problem; the task
  is to transport the square root of the determinant line around simple
  diagonal wall reflections and compute the sign.
- `main.tex:1149-1171`: constants \(64\), \(4096\), and the OP minus sign
  are not Hall orientation data.
- `main.tex:1386-1408`: \(\Delta_5\) is a section of
  \(\mathcal L^5\otimes\nu_{\Delta_5}\); its square is scalar in
  \(\mathcal L^{10}\).
- `main.tex:1442-1464`, `main.tex:1533-1551`: Maass signs on the relevant
  reflection classes are stated.  Type-II simple reflections have sign
  \(-1\); the three chamber automorphism classes listed there have sign
  \(+1\).
- `main.tex:2272-2367`: the compact Igusa datum includes orientation
  lines with chosen square roots, Thom--Sebastiani coherence, protected
  integration, local/wrapped extension correspondences, and the required
  comparison with \(\nu_{\Delta_5}\).  It also says constructing the
  domain of \(\epsilon_o\) is part of the datum.
- `main.tex:2949-3057`: the synthesis theorem separates determinant,
  denominator, scalar square, open microscopic comparison, orientation
  monodromy, parity dimensions, PBW, no-extra-relations, and Hall
  brackets.
- `appendices/boundary_compatibility_conditions.tex:20-43` and
  `appendices/boundary_compatibility_conditions.tex:91-105`: the boundary
  table treats the orientation character as required geometric monodromy,
  not a scalar normalization.

## Primary literature anchors

- `proj.bib:244-251`: Behrend 2009.  Behrend proves DT-type invariants
  are weighted Euler characteristics of moduli spaces; this supports the
  scalar Behrend branch, not a Hall orientation character.  Source:
  https://annals.math.princeton.edu/2009/170-3/p06
- `proj.bib:253-263`: Kontsevich--Soibelman 2011 CoHA/motivic DT source.
  Their broader stability-structures paper has Section 5.2 "Orientation
  data" and Section 6 on motivic DT invariants; orientation data is a
  separate input for motivic Hall integration, not a scalar constant.
  Source: https://www.ihes.fr/~maxim/TEXTS/stability_structures_49.pdf
- `proj.bib:265-275`: Davison--Meinhardt 2020.  Their critical CoHA is
  built from vanishing cycles and yields PBW/BPS Lie-algebra structures
  for quivers with potential; it supplies general CoHA technology, not
  the compact \(K3\times E\) Hall atlas.  Source:
  https://link.springer.com/article/10.1007/s00222-020-00961-y
- `proj.bib:219-230`: Oberdieck 2018.  The reduced \(S\times E\)
  theorem compares quotient Behrend-weighted stable-pair invariants and
  reduced DT/PT series; it is scalar.  Source:
  https://arxiv.org/abs/1605.04631
- `proj.bib:191-218`: Oberdieck--Pixton and
  Oberdieck--Pandharipande fix the Igusa scalar branch and variables.
  They do not define \(\epsilon_o\).
- `proj.bib:15-21`, `main.tex:676-692`: Maass supplies
  \(\nu_{\Delta_5}\), the automorphic character.  This is theorem-level
  automorphic data, not the compact Hall orientation.
- `proj.bib:64-98`, `main.tex:2696-2716`: Gritsenko--Nikulin supplies the
  denominator identity.  The denominator theorem fixes the target
  reflection sign and signed root supermultiplicities inside the BKM
  datum; it does not construct compact Hall orientation-line monodromy.

## Safety checks

The manuscript passes the requested separations.

- Orientation vs. Behrend sign: safe.  `main.tex:857-879` makes the
  Behrend branch scalar and explicitly not an orientation character.
- Orientation vs. OP scalar normalization: safe.  `main.tex:1149-1171`
  says \(64\), \(4096\), and the OP minus sign are not Hall orientation
  data.
- Orientation vs. theta-characteristic/Maass character: safe.  The
  theta-product and Maass sign determine \(\nu_{\Delta_5}\); they do not
  define \(\epsilon_o\).  The expected Pfaffian normal-mode explanation
  remains a criterion/open mechanism.
- Orientation vs. Borcherds determinant: safe.  The determinant gives
  \(D_5\) and the automorphic character.  It does not provide determinant
  line square roots on a compact Hall stack.
- Orientation vs. BKM denominator: safe.  The denominator identity fixes
  the target reflection character and signed multiplicities after the
  Gritsenko--Nikulin datum is fixed.  It does not supply compact Hall
  extension correspondences, protected integration, or monodromy.

## Cross-repo consistency

Vol III remains compatible.  `FRONTIER.md` marks bracket-level
BPS \(\cong\) BKM as open and the Hall--Drinfeld/BKM real-root
completion as open beyond the abelian core.  In
`calabi-yau-quantum-groups/chapters/theory/cy3_chain_level_bridge.tex:522-674`,
the oriented hCS--Hall comparison starts only after orientation, trace,
twist, completion, product, and coherence data are supplied.
`cy3_chain_level_bridge.tex:1099-1211` treats determinant-line
square-root mismatch as a \(\mathbb Z/2\) obstruction component, not as
an automatic consequence of a scalar partition function.

One cross-repo note outside this manuscript,
`chiral-bar-cobar/notes/wave17_spoils_dossier_20260424.md:169`, uses
"graded-dim identification" language for \(K3\times E\) while keeping
the bracket-level identification open.  That is not imported into
`main.tex`.  If propagated later, it should be restated as a signed
Grothendieck-class/character identification, not as a compact Hall
orientation or bracket theorem.

## Claim-status recommendation

Keep the manuscript claim strength.

- Theorem: \(\nu_{\Delta_5}\) is the automorphic/reflection character of
  the theta-normalized Igusa square root; on the type-II Weyl group it is
  the determinant sign.
- Theorem/imported: OP/DT scalar branch
  \(Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}=-4096\Delta_5^{-2}\).
- Conditional/open: existence of the compact Hall/CoHA orientation datum
  and the proof that \(\epsilon_o=\nu_{\Delta_5}\) on
  \(W^{(2)}(\Lambda^{2,1}_{II})\).
- Expected mechanism: each simple type-II reflection reverses one
  Pfaffian normal mode, so the square root changes sign.  This is not yet
  a proof.
- False: deriving \(\epsilon_o\) from \(64\), \(4096\), the OP minus sign,
  \(\Delta_5^2\), or scalar Behrend weighting.

## Files changed

- Added `notes/attack_heal_20260427/agent3_hall_orientation.md`.
- No manuscript files changed.

## Checks and computations

- Read `CLAUDE.md`, `AGENTS.md`, `INVARIANTS.md`, `AGENTS-HARNESS.md`,
  `main.tex`, `proj.bib`, `appendices/boundary_compatibility_conditions.tex`,
  and the local orientation/Hall agent-material files.
- Searched for `orientation`, `Behrend`, `epsilon`, `nu`, `character`,
  `theta`, `square`, `Hall`, `determinant`, `reflection`, `parity`, `PBW`,
  and `extra-relations`.
- Checked Vol III orientation and frontier anchors for silent promotion of
  \(\epsilon_o=\nu_{\Delta_5}\).  None found.
- No build run; this is a disjoint notes report and no TeX source was
  integrated into `main.tex`.

## Remaining open obligations

- Construct the extension-closed compact critical Hall/CoHA sector for
  the reduced \(K3\times E\) problem.
- Construct an \(E\)-equivariant strong orientation: determinant-line
  square roots, exact-triangle coherence, and Thom--Sebastiani transport.
- Build the mixed local/wrapped Hall correspondences before quotienting by
  \(E\), so positive elliptic degree is included in the domain.
- Construct protected integration compatible with HN completion and wall
  crossing.
- Lift the type-II Weyl action to the oriented completed Hall object.
- Compute the three simple type-II determinant-line signs and prove the
  reflection relations, hence
  \[
  \epsilon_o|_{W^{(2)}(\Lambda^{2,1}_{II})}
  =
  \nu_{\Delta_5}|_{W^{(2)}(\Lambda^{2,1}_{II})}.
  \]
- Keep this orientation problem separate from the later primitive
  recognition obligations: full parity dimensions, simple primitives,
  Hall bracket constants, no-extra-relations, completed PBW, and radical
  quotient.
