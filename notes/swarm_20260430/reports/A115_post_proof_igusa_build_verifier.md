# A115 -- Post-Proof Igusa Build Verifier

## Verification

`make -B` succeeded and refreshed `out/main.pdf`:

```text
236 pages
1333043 bytes
2026-04-30 04:42:45 SAST
```

Static checks over `main.tex` and
`appendices/boundary_compatibility_conditions.tex` found:

```text
labels=199
refs=440
cite_keys=298
bib_keys=92
```

No duplicate labels, undefined references, undefined citations,
duplicate BibTeX keys, fatal TeX errors, rerun warnings,
multiply-defined labels, duplicate destinations, or BibTeX warnings were
reported in the final logs.

## Computation Checks

`compute/verify_lattice.py` passed, including the type-II Gram matrix
\([[2,-2,-2],[-2,2,-2],[-2,-2,2]]\) and
\(\rho=(1,-1/2,1)\).

`compute/verify_square_root.py` passed, including \(29|93\),
\(m(\delta_{123})=-93\), height-four gaps \(108|90|18\), doubled
isotropic gaps \(10|9|1\), and real-string exponents \(3\) and \(5\).

## Warnings

Only general warnings remained:

- `amsrefs` recommends `\cites` form.
- two inspected overfull boxes remained outside the new
  A071/provenance-gate/finite-source criterion block.

## Theorem-Strength Result

No fatal overclaim was detected in the provenance-gate addition. Compact
source recognition remains conditional on actual source provenance and
matrices. The A071 parity rows remain stronger than the coefficient
script: signed arithmetic is verified by computation, while the full
parity transport for the promoted rows rests on the cited Kac /
Gritsenko--Nikulin target presentation statements.

## Files Changed By Agent

None.
