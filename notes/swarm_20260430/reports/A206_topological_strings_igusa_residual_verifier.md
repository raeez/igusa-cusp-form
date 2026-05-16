# A206 Topological Strings Igusa Residual Verifier

## Findings

No fatal or high findings in `~/topological-strings`. The active firewall
holds: the bound manuscript and `tate-P5-cross-volume.tex` require
matched target data and null-homotopies before any compact CY, MNOP,
Igusa/BKM, or `K3 x E` conclusion.

## Medium Findings

- Source-gate anchors in
  `references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  and `references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  are line-stale after `frontier_mnop_framing_volume.tex` movement.
- `frontier_mnop_framing_volume.tex` keeps BPS/BCOV data guarded, but
  still uses proposition-level packaging for finite quintic evidence
  before local HKQ/CDGP/OSV/GV mirrors exist. Keep it out of theorem
  import until fixtures and the numerical ledger land.

## Checks

- `Phi10`, `Phi_10`, and `H_Delta` searches: no active hits.
- `Delta_5` / BKM hits are guarded.
- `git diff --check` passed at A206's snapshot.
- `git diff --cached --check` passed.

## Status

No theorem-promotion bug found. Anchor maintenance delegated to A211.

