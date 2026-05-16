# A178 -- Igusa Signed-Shadow / Source-Gate Verifier

## Result

Read-only verification found no blocking issue in the Igusa theorem lane.

## Checks

- Targeted `rg` over `main.tex` for `signed-shadow`, `K_0`, `Pfaffian`,
  `SCHEMA_COMPLETE`, `target presentation`, `source fixture`,
  `primitive recognition`, `minimal split`, and proof-strength language.
- `git diff --check -- main.tex` passed.

## Findings

- Signed \(K_0\)/Pfaffian shadow is fenced as target-only around
  `11244`, `11592`, `11838`, and `12027`.
- Target presentation rows are target arithmetic, not compact Hall data,
  around `12882`, `15131`, `15440`, and `15447`.
- `SCHEMA_COMPLETE` and source fixture checks are fail-closed
  schema/status/payload gates, not compact-source certification, around
  `12895`, `15483`, and `15670`.
- Actual primitive recognition is reserved for compact-source provenance
  plus source matrices, radicals, PBW, and transitions around `15459`,
  `15514`, `15635`, and `15738`.

## Residual Obligation

Compact source parity and primitive recognition still require retained
compact source representatives, provenance, \(M,D,B,G,K,Q,A\) matrices,
radical kernels, no-extra relations, PBW comparison, strict transitions,
and for \(W_{\le3}\) explicit \(29|93\) compact source primitives in degree
\(\delta_{123}\). No inspected sentence lets signed coefficients, target
rows, `SCHEMA_COMPLETE`, or minimal split \(K_0\) representatives discharge
those obligations.

