# A074 - Vol III Primitive Recognition Consistency Audit

Read-only audit. No files edited, staged, reverted, or cleaned by the
agent. Both repos were already dirty.

## Verdict

Igusa A049-A068 and CYQG AP-CY416-AP-CY422 / IC-58-IC-64 agree on the
core theorem: `W_{\le3}` arithmetic is target Borcherds/GN/Kac data only.
Primitive recognition requires an actual compact source fixture:
representatives, parity blocks, `M,D,B,G,K,Q,A_\beta`, relation rows,
Hopf radical/coideal, kernel equality, PBW, and strict ML transitions.

## Live Contradiction / Overclaim

Vol III has one unpropagated overclaim:

- `k3e_cy3_programme.tex` near line 177 defines a Hall-Borcherds
  comparison map by coefficient projection.
- `k3e_cy3_programme.tex` near line 206 says this projection respects
  charge addition because both products use the same cone.

This conflicts with AP-CY416, AP-CY417, and AP-CY418. A coefficient
projection is not a Hall product/bracket matrix comparison and does not
prove Borcherds-Serre rows, radical descent, no-extra-relations, or PBW.

This contradiction was already diagnosed locally in
`frontier_resolution_swarm_20260424_hall_bkm_algebra.md` near line 96,
but not propagated into the chapter.

## Consistent Anchors

Igusa `main.tex` is already in the stronger conditional form:

- Primitive recognition is not determinant data: `main.tex` near line
  12469.
- Target denominator algebra is imported, not compact Hall: `main.tex`
  near line 12531.
- Source data are not inferred from product or signed dimensions:
  `main.tex` near line 12556.
- No-extra-relations is separate: `main.tex` near line 12714.
- PBW is separate: `main.tex` near line 12743.
- `W_{\le3}` target table is target-only: `main.tex` near line 15004.
- Finite source matrix criterion: `main.tex` near line 15268.
- Scripts verify target arithmetic only: `main.tex` near line 15360.

CYQG's cache matches this at `first_principles_cache.md` near line 717.

## Missing Propagation

Igusa reports A049-A062 mostly cite older AP names
AP-CY368/AP-CY378/AP-CY382/AP-CY384. The normalized Vol III cache rows
are now AP-CY416-AP-CY422 / IC-58-IC-64. Only A063/A064 mention
AP-CY416/AP-CY418; A058 explicitly says AP-CY416 was not yet present.
This is a ledger propagation gap, not a mathematical contradiction.

## Stronger Vol III Theorem Form

The strongest consistent theorem is:

A finite downward-saturated window `W` is recognized only from a source
fixture containing neutral source basis IDs with provenance, target
fixture IDs, matrices `M,D,B,G,K,Q,A,T`, relation-row certificates, Hopf
radical/coideal checks, no-extra kernel equality, PBW associated-graded
isomorphism, and strict transition/ML ranks. Then and only then the
compact source quotient identifies with the GN/Kac target on `W`.
Cofinal compatible fixtures give global primitive recognition.

This is exactly the direction proposed by A067 and demanded by AP-CY421.

## Verification

Ran `PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py` and
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`; both
passed and produced target arithmetic only.

