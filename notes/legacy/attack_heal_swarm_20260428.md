# Attack-Heal Swarm

Date: 2026-04-28.

Internal integration ledger.  The manuscript remains standalone.

## Integration Rule

The main thread integrates.  Agents provide evidence and patches, not
authority.  No agent result is accepted until the affected theorem,
definition, or proof is read in context and checked against the
architecture:

1. no compact construction claim without constructed data;
2. no scalar sign used as orientation monodromy;
3. no raw `Pi_X` pushforward replacing normal ordering;
4. no hidden transfer from a target denominator algebra to a compact
   Hall source;
5. no boundary row treated as physical without a row certificate.

## Agent Ownership

1. `D0`: compact first-order Dirac-Igusa certificate and Pfaffian source.
   Worktree: `/tmp/igusa-agent-d0`; branch:
   `agent/igusa-d0-20260428`.
2. `Hybrid`: `E_3` source, `K3 -> E` specialization, projection-finite
   and wrapped sectors, mixed local/wrapped correspondences.
   Worktree: `/tmp/igusa-agent-hybrid`; branch:
   `agent/igusa-hybrid-20260428`.
3. `Orientation/E[2]`: strong reduced orientation, finite stabilizers,
   trivial `E[2]` linearization or exact obstruction.
   Worktree: `/tmp/igusa-agent-orient`; branch:
   `agent/igusa-orient-20260428`.
4. `Weyl/Pfaffian`: `(O1)+`, `(O2)`, type-II wall signs, Maass target
   comparison with no automorphic-to-geometric overreach.
   Worktree: `/tmp/igusa-agent-weyl`; branch:
   `agent/igusa-weyl-20260428`.
5. `Chain normal ordering`: chain-level `Theta`, Hochschild/cyclic
   representative of `B`, Frobenius/Hopf compatibility.
   Worktree: `/tmp/igusa-agent-chain`; branch:
   `agent/igusa-chain-20260428`.
6. `Primitive recognition`: presentation-level comparison with
   `mathfrak g_{Delta_5}`: generators, parity, relations, Hopf pairing,
   radical quotient, no-extra-relations, PBW.
   Worktree: `/tmp/igusa-agent-recognition`; branch:
   `agent/igusa-recognition-20260428`.

## Acceptance Test

Each accepted patch must make at least one manuscript claim strictly
stronger, more precise, or more honestly fenced.  A patch that only
adds rhetoric is rejected.  A patch that proves an impossible
construction by hiding a hypothesis is rejected.

## Second Swarm After Verified Integration

Launched after `make`, `compute/verify_lattice.py`, and
`compute/verify_square_root.py` passed on the integrated manuscript.
The second swarm starts from `/tmp/igusa-current-tracked-v2.patch`, which
contains the shared manuscript state after the first six worktree patches
were semantically integrated.

1. `Orientation quotient`: strong reduced orientation, connected
   `BE` class, finite stabilizers, rank-one `E[2]`, even `N>=4`, and
   Weyl transport compatibility.
   Agent: `Godel` (`019dd1fe-dcef-7fc0-90d8-2d3233efcc78`).
   Worktree: `/tmp/igusa-next-orientation`; branch:
   `agent/igusa-next-orientation-20260428`.
2. `D0 finite source`: finite supports, transition maps, residual tuple
   `mathfrak O_{D_0,R}`, Pfaffian normalization, source/observable
   comparison, and every later use of `(D0)`.
   Agent: `Archimedes` (`019dd1fe-ddf4-7c01-8330-57154e5dcdfb`).
   Worktree: `/tmp/igusa-next-d0`; branch:
   `agent/igusa-next-d0-20260428`.
3. `Chain descent`: coefficient dg category, central translations,
   Hochschild equation, triple pentagon, Jacobiator, negative-cyclic
   lift, Frobenius/Hopf compatibility, and radical quotient.
   Agent: `Franklin` (`019dd1fe-decc-7231-8f46-4cd01a82e074`).
   Worktree: `/tmp/igusa-next-chain`; branch:
   `agent/igusa-next-chain-20260428`.
4. `Hybrid wrapped object`: finite HN stage, elliptic degree `b_R`,
   rigidified wrapped prequotients, mixed correspondences, flag
   associativity, quotient-after-correspondences `Q_{E,R}`, protected
   integration, and the Igusa `s`-direction.
   Agent: `Kepler` (`019dd1fe-e00e-70a3-977c-c29f4d8a9e86`).
   Worktree: `/tmp/igusa-next-hybrid`; branch:
   `agent/igusa-next-hybrid-20260428`.
5. `Primitive recognition`: generators, parities, Borcherds--Kac
   relations, Hopf pairing, radical quotient, no-extra-relations,
   generation, completed PBW, full parity dimensions, and the
   `delta_1+delta_2+delta_3` signed-multiplicity `-64` channel.
   Agent: `Dalton` (`019dd1fe-e0cd-7fd1-9770-0a02a9410ceb`).
   Worktree: `/tmp/igusa-next-recognition`; branch:
   `agent/igusa-next-recognition-20260428`.
6. `Chiral Koszul/full certificate`: `mathfrak K_X`, the chiral coalgebra
   `C_X`, bar comparison `b_X`, cobar quasi-isomorphism
   `Theta_Kos`, and the relation between local `E_3`, hybrid wrapped
   sectors, and the current envelope `mathsf{Den}_{Delta_5,E}`.
   Agent: `Dirac` (`019dd1fe-e1e2-78c1-a150-f2312645164d`).
   Worktree: `/tmp/igusa-next-koszul`; branch:
   `agent/igusa-next-koszul-20260428`.

## Third Swarm After Second Integration

Launched after the second swarm was semantically merged, older side
branches were audited, `git diff --check`, both compute checks, and
`make` passed on the integrated manuscript.

Integration owner: main thread in `/Users/raeez/igusa-cusp-form`.
All agents work in fresh `/tmp/igusa-third-*` worktrees seeded from the
current manuscript patch.  They may edit their worktrees and stage files,
but must not commit, must not revert other lanes, and must report exact
anchors, formulas, checks, and remaining obstructions.

1. `third-d0-source`: finite-stage construction of `D_{0,R}`,
   transition residuals, source/observable comparison, Pfaffian support,
   and the exact open construction target.
2. `third-orientation`: connected `BE`, all finite `E[N]` stabilizers,
   quotient trivializations, and Weyl transport compatibility.
3. `third-chain`: `Pent_Theta`, `o_F`, negative-cyclic lift, and
   Hopf-radical ideal/coideal stability.
4. `third-hybrid`: concrete hybrid local/wrapped object, rigidified
   wrapped prequotients, mixed stacks, `Q_{E,R}`, and protected
   integration.
5. `third-koszul`: source-side chiral Koszul certificate `C_{X,R}`,
   `b_{X,R}`, `Theta_{Kos,R}`, and finite residual `O_{Kos,R}`.
6. `third-recognition`: presentation-level primitive recognition:
   generators, parities, Serre/Jacobi constants, Hopf pairing, radical
   quotient, no-extra-relations, and PBW.
