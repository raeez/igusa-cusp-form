# A141 -- Topological-Strings OP Normalization Patch

## Claim Attacked

An archival cross-volume report used the normalization
\(Z^{DT,red}=-1/\Phi_{10}=-1/\Delta_5^2\), which conflicts with the
current Igusa/OP scalar normalization.

## Patch

The archival formula now uses
\[
-(\chi_{10}^{\mathrm{OP}})^{-1}=-4096\,\Delta_5^{-2}.
\]
The surrounding text states that this normalization is scalar,
orientation-forgetful, not compact Hall recognition, and not source
primitive recognition.

## Verification

```text
git diff --check -- reconstitution/phase4-exec-W5-X1-cross-volume-2026-04-28.md
```

passed. Targeted search found `4096` and `compact Hall` guardrails, with
no remaining `Phi_10` or `Delta_5^2` stale hits.

## Changed Paths

- `/Users/raeez/topological-strings/reconstitution/phase4-exec-W5-X1-cross-volume-2026-04-28.md`
