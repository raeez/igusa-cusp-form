# Six-agent attack/heal integration

Date: 2026-04-27.
Integration owner: main thread.

## Verdict

No fatal overclaim survives.

The manuscript keeps the determinant, denominator algebra, scalar
OP/DT square, compact \(E_3\)/Hall realization, orientation monodromy,
positive elliptic-degree repair, and boundary-row physical hosts in
separate claim classes.

## Agent axes

| agent | axis | result |
| --- | --- | --- |
| 1 | microscopic compact BPS Hilbert space and operator product | safe; abstract sharpened to separate target-internal Borcherds bracket from compact BPS OPE |
| 2 | compact finite-first holomorphic \(E_3\)-factorization algebra | safe; \(\mathcal A_X^{E_3}\), \(\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\), formality, framing, QME/anomaly, descent, and HN data remain supplied/open |
| 3 | Hall orientation and \(\epsilon_o=\nu_{\Delta_5}\) | safe; Behrend weighting, OP normalization, Maass character, and Hall orientation monodromy remain separate |
| 4 | determinant/product versus Hall brackets, parity, PBW, no-extra-relations | safe; low-degree bracket constants are quarantined as denominator-algebra constants |
| 5 | positive elliptic-degree \(s\)-direction | safe; Ran locality sees projection-finite sectors only; proof tightened with properness of \(p_E\) |
| 6 | rows \(5\)--\(8\), physical row maps, fractional comparison rows | safe; rows \(5\)--\(8\) remain product plus CHL/WKB denominator only; fractional rows remain conditional on parent, cover, character, branch, and host data |

## Manuscript repairs

1. Abstract: the denominator algebra now supplies the algebraic
   square-root target and target-internal Borcherds bracket, but not a
   compact BPS Hilbert space or BPS operator product/local collision map.
2. Elliptic-degree locality lemma: the proof now explicitly uses
   properness of \(p_E:K3\times E\to E\) when concluding that \(p_E(C)\)
   is closed.

## Remaining obligations

The open obligations are unchanged:

- construct the compact one-particle object, if it exists;
- construct the finite-first holomorphic \(E_3\)-source and
  chain-level \(K3\)-to-\(E\) specialization;
- build mixed local/wrapped Hall correspondences for positive elliptic
  degree before quotienting by \(E\);
- construct the strong orientation and prove
  \(\epsilon_o|_{W^{(2)}}=\nu_{\Delta_5}|_{W^{(2)}}\);
- prove primitive representatives, compact Hall bracket constants, full
  parity dimensions, no-extra-relations, completed PBW, and radical
  compatibility;
- for rows \(5\)--\(8\) and fractional comparison symbols, construct
  row-specific host, cover, character, scalar, and compact Hall/chiral
  certificates before making a physical row-map claim.

## Reports

- `agent1_bps_hilbert_operator_product.md`
- `agent2_e3_factorization.md`
- `agent3_hall_orientation.md`
- `agent4_determinant_not_brackets.md`
- `agent5_positive_s_hybrid_hall.md`
- `agent6_rows5_8_fractional.md`
