# A175 -- CYQG Cache / Executable Consistency Verifier

## Result

Read-only verification found no high or medium issues in the cache and
executable CoHA guardrails.

## Findings

- Cache entries are consistent across
  `appendices/first_principles_cache.md:737`,
  `notes/first_principles_cache_comprehensive.md:5340`, and
  `notes/antipatterns_catalogue.md:5619`.
- Executable CoHA wording matches IC-79/AP-CY437: \(|c(D)|\) is a
  signed-character magnitude/statistic, and dimension APIs require
  parity/source fixtures.
- Tests enforce that discipline in the scoped CoHA/Hall tests.

## Low Residual

`compute/tests/test_k3e_coha_structure.py:763` said “The identification is
with \(g_{\Delta_5}\).” The main thread tightened this docstring to the
signed-character BKM target label.

## Checks

- `git diff --check` over the three cache files, two compute libraries,
  and two tests passed.
- Targeted `rg` found no stale `coha_as_bkm_positive_half`,
  `verify_coha_dim_vs_phi01`, `coha_dimensions`, or `dim CoHA = |c(D)|`
  promotion in the scoped files.
- `pytest compute/tests/test_elliptic_hall_hocolim.py compute/tests/test_k3e_coha_structure.py`
  returned `175 passed in 5.93s`.

## Residual Obligation

Finite Hall--Borcherds recognition remains open: source maps, parity
fixtures, brackets, PBW, and completion data are still required before
coefficient matches can be promoted to compact Hall--Borcherds
identification.

