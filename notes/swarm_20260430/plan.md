# 2026-04-30 attack-heal swarm plan

Source critique: `materials/raw/2026-04-30-attack-whitepaper-analysis.pdf`.
Extracted text: `materials/processed/2026-04-30-attack-whitepaper-analysis.txt`.
Intake guide: `notes/attack_whitepaper_analysis_20260430_guide.md`.

Protocol: 204 proposal-only explorer agents, six agents at a time.
Main thread is integration owner. Agents may inspect shared checkouts but
must not write. Write-capable healing requires later isolated worktrees.

Every agent uses:

- `~/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`;
- `~/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`;
- `~/calabi-yau-quantum-groups/.agents/skills/chriss-ginzburg-rectify/SKILL.md`;
- `~/calabi-yau-quantum-groups/.agents/skills/vol3-chriss-ginzburg-rectification/SKILL.md`.

Every report must return:

1. claim attacked;
2. failure mode or proof;
3. local file anchors;
4. critique anchors;
5. formulas/constants;
6. claim-status recommendation;
7. files changed, which must be `none` for proposal-only waves;
8. checks or computations run;
9. residual obligation.

## Wave Topology

Each wave launches exactly six agents. Later waves may be reordered by
main-thread synthesis, but the concurrency cap remains six.

| Wave | Agents | Scopes |
|---|---:|---|
| 1 | A001-A006 | Provenance/injection; retained Liu-Hilbert boundedness; normal-ordered lattice; hybrid local/wrapped; orientation gerbe; \(W_{\le3}\) matrices. |
| 2 | A007-A012 | Borcherds normalization; \(\phi_{0,1}\) coefficients; \(\Delta_5/D_5/\Phi_{10}\); GN denominator; Maass character; OP scalar square. |
| 3 | A013-A018 | D6-D2-D0 Mukai vector; OP variable dictionary; \(m=d-1\) firewall; algebraic Mukai sector; full \(N=4\) charge warning; rank-one sector closure. |
| 4 | A019-A024 | Gram cocycle; raw/split/cochain notation; \(\Theta_\Pi\); HN finite-fibre conditions; B-isotropic no-go; fixed-lift real-root strings. |
| 5 | A025-A030 | Compactified extension stacks; flag stacks; properness; d-critical structures; vanishing cycles; six-functor admissibility. |
| 6 | A031-A036 | Hybrid base definitions; local colors; wrapped anchors; quotient-after-correspondence; higher colored trees; overlap descent. |
| 7 | A037-A042 | Connected \(BE\); finite \(BE[N]\); \(E[2]\) classes; degree-one characters; translation linearization; quotient orientation. |
| 8 | A043-A048 | Type-II walls \(\delta_1,\delta_2,\delta_3\); graph-isogeny wall candidate; local Ext normal form; Pfaffian rank; Weyl sign. |
| 9 | A049-A054 | Primitive recognition; Chevalley relations; Serre relations; imaginary orthogonality; PBW; no-extra-relations. |
| 10 | A055-A060 | \(W_{\le3}\) target arithmetic; source bases; \(29|93\) block; product matrices; coproduct matrices; radical kernels. |
| 11 | A061-A066 | Source chiral coalgebra; target bar-cobar firewall; \(\Theta_{\mathrm{Kos}}\); BD/FG current envelope; source-to-target comparison. |
| 12 | A067-A072 | Dirac blocks; finite Pfaffian; parity spaces; \(K_0\) vs actual supervector spaces; orientation-forgetful scalar square; first-order operator status. |
| 13 | A073-A078 | Retained cofinal schedules; closure under subobject/quotient/extension; duals; anchors; flag refinements; Mittag-Leffler transitions. |
| 14 | A079-A084 | Manuscript architecture; theorem spine; section order; false implications box; status ledger; Chriss-Ginzburg rewrite targets. |
| 15 | A085-A090 | Boundary rows; Clery-Gritsenko catalogue; row order; diagonal divisor forms; row certificates; split-paper decision. |
| 16 | A091-A096 | Bibliography/source-role audit; Borcherds; Gritsenko-Nikulin; Igusa; Oberdieck-Pandharipande; Liu; Piyaratne-Toda. |
| 17 | A097-A102 | Cross-repo Vol III consistency; no authority transfer; \(kappa\)-stratification; Igusa row; CYQG cache propagation; conflict ledger. |
| 18 | A103-A108 | Topological-strings/BCOV consistency; protected traces; compactification physics; locality; wall crossing; anomalies. |
| 19 | A109-A114 | Compute harness audit; `compute/verify_square_root.py`; `compute/verify_lattice.py`; coefficient checks; target/source distinction; reproducibility. |
| 20 | A115-A120 | Low-degree examples; \(\phi_{0,1}\) first coefficients; first roots; first wall atoms; first retained matrix examples; degenerations. |
| 21 | A121-A126 | Notation firewall; \(m\) versus \(d\); \(D_X\) versus \(D_5\); \(\Pi\) versus \(\overline\Pi\); target/source symbols; process-language scrub. |
| 22 | A127-A132 | Claim-status audit; proved/computed/imported/conditional/open labels; theorem names; conjecture demotion; no rhetoric outruns proof. |
| 23 | A133-A138 | Dyonic Mukai lattice; torsion-one primitive descent; duality invariance; physical U-duality underspecification; orbit representatives. |
| 24 | A139-A144 | Hall algebra assumptions; extension closure; semistability chambers; wall-crossing dependence; protected integration; primitive extraction. |
| 25 | A145-A150 | Orientation-Pfaffian local algebra; determinant line; square-root gerbe; Weyl transport; finite stabilizers; scalar sign quarantine. |
| 26 | A151-A156 | Retained source theorem attack; finite-type proof details; Quot construction; relative Ext stack; openness in heart; hidden hypotheses. |
| 27 | A157-A162 | Hybrid wall construction attack; wrapped middle wall geometry; graph isogeny; semistability; charge matching; no-extra-normal directions. |
| 28 | A163-A168 | \(W_{\le3}\) source table construction attack; basis provenance; pairing nondegeneracy; radical ideal/coideal; quotient comparison. |
| 29 | A169-A174 | Infinite limit attack; cofinality; stable images; \(R^1\lim\); PBW filtration preservation; transition compatibility. |
| 30 | A175-A180 | Reader-facing TeX scrub; no critique-process language; no phase labels; no internal cache markers; standalone manuscript register. |
| 31 | A181-A186 | Adversarial synthesis against retained theorem; weakest hidden assumption; counterexamples; missing sources; exact blockers. |
| 32 | A187-A192 | Heal proposals for `main.tex` Part I-II; automorphic/lattice rewrite sequence; source anchors; minimal patch plan. |
| 33 | A193-A198 | Heal proposals for compact-source Part III; retained finite stages; orientation; hybrid; source matrices; minimal patch plan. |
| 34 | A199-A204 | Final referee wave; independent convergence audit; unresolved fatal attacks; stable core; next theorem obligations. |
