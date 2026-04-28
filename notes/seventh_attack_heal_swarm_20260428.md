# Seventh Attack-Heal Swarm Ledger

Integration owner: main thread in `/Users/raeez/igusa-cusp-form`.

Base branch: `master`.
Base commit: `b7c7a2b`.

All worktrees were seeded with the current tracked manuscript patch for
`main.tex` and `compute/verify_square_root.py`, plus local notes/materials
context. Agents may read broadly, but write only inside their assigned
worktree and owned manuscript lane. Subagents provide evidence, not
authority; the main thread performs the semantic merge.

Forbidden commands for all agents: `git reset`, `git checkout`,
`git switch`, `git restore`, `git stash`, `git clean`, `git rebase`,
history rewrite, worktree removal, branch deletion, commits, and pushes.

## Agent lanes

| Lane | Worktree | Branch | Owned mathematical obligation |
|---|---|---|---|
| S7-D0 | `/tmp/igusa-seventh-d0` | `agent/igusa-seventh-d0-source-20260428` | Construct the compact finite-stage D0 Hall/Dirac source, including compact Pfaffian line and parity pieces on cofinal target windows. |
| S7-O | `/tmp/igusa-seventh-orientation` | `agent/igusa-seventh-orientation-weyl-20260428` | Prove strong reduced orientation on compact/wrapped sectors, finite-stabilizer characters, and the Weyl-equivariant lift (O1)+. |
| S7-H | `/tmp/igusa-seventh-o2-hybrid` | `agent/igusa-seventh-o2-hybrid-20260428` | Compute the O2 type-II wall local model geometrically and construct the hybrid local/wrapped factorization object. |
| S7-NO | `/tmp/igusa-seventh-chain-normal` | `agent/igusa-seventh-chain-normal-20260428` | Realize chain-level normal ordering on Hall correspondences and attack/heal NO1--NO7. |
| S7-K | `/tmp/igusa-seventh-koszul` | `agent/igusa-seventh-koszul-cobar-20260428` | Construct the source Koszul coalgebra after the hybrid source and prove the source-to-target cobar comparison where possible. |
| S7-R | `/tmp/igusa-seventh-recognition` | `agent/igusa-seventh-recognition-global-20260428` | Prove primitive recognition globally: representatives, relations, pairing, radical quotient, no-extra-relations, completed PBW. |

## Runtime agent IDs

| Lane | Agent ID | Nickname |
|---|---|---|
| S7-D0 | `019dd2c2-ba5d-7620-bfa5-3551e456dbe5` | Hegel |
| S7-O | `019dd2c2-bc0b-7460-88f9-bddb07df9b9c` | Feynman |
| S7-H | `019dd2c2-bdc8-7003-a4f4-a1089e752a5c` | Anscombe |
| S7-NO | `019dd2c2-be97-74e3-bd03-29eb5936ad71` | Copernicus |
| S7-K | `019dd2c2-c0b7-7593-8f5c-9dd7c7d6bcdd` | Hubble |
| S7-R | `019dd2c2-bfd2-7662-88b6-b54c2b2964ce` | Wegener |

## Evidence standard

Mathematical theorem claims require proof from definitions, verified
hypotheses of named theorems, or explicit computation. A citation alone
does not prove a new compact source claim. If a construction cannot be
closed without new external mathematics, the agent must inscribe the
strongest true finite-stage theorem or obstruction, not a false existence
claim.

Each report must include:

- claims attacked;
- valid attacks and false attacks;
- repairs inscribed;
- exact manuscript anchors;
- exact formulas/constants where relevant;
- files changed;
- commands run and results;
- residual obligations with deciding evidence.

## Main-thread verification plan

After all agents return, integrate by reading every diff hunk against
`main.tex`, preserving all mathematically substantive content. Then run:

```bash
git diff --check
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
make
```

Convergence requires every spawned agent to return or be explicitly
closed, every severity 1--3 attack to be healed, refuted, or placed
outside the stable core, and every surviving manuscript claim to carry
the correct proof-strength label.
