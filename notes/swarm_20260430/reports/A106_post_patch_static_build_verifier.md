# A106 post-patch static/build verifier

No source edits made by the agent. It ran `make -B` and regenerated build
outputs.

## Fresh checks

- Static parser over `main.tex` plus
  `appendices/boundary_compatibility_conditions.tex`:
  labels `199`, refs `110`, cites `82`, BibTeX entries `92`.
- Duplicate labels: `0`.
- Undefined refs: `0`.
- Duplicate BibTeX keys: `0`.
- Undefined citations: `0`.
- `make -B`: passed, produced `out/main.pdf`.
- Fatal/undefined/rerun/multiply-defined scan: no matches.
- BibTeX: `warning$ -- 0`.
- Nonfatal amsrefs warnings remain at input lines 488 and 512.
- `python3 compute/verify_lattice.py`: passed.
- `python3 compute/verify_square_root.py`: passed.

## Overfull boxes near the patched region

Fresh pass4 log had 23 total overfulls. Around the requested region:

- `.build_logs/main-pass4.log:692`: `175.6327pt` at `main.tex:13123`,
  finite retained \(K3\times E\) sector datum array after the
  proof-ledger/cofinal block.
- `.build_logs/main-pass4.log:738`: `4.62976pt` at `main.tex:15152`,
  target bracket display.
- `.build_logs/main-pass4.log:753`: `10.65419pt` at
  `main.tex:15339--15354`, height-four coefficient paragraph.
- No overfull was logged inside the provenance gate or finite source
  matrix criterion.

## Theorem-strength flags

No unfenced source-recognition overclaim was found. The manuscript leaves
open the compact Dirac--Igusa realization, full parity rows for
\(C_{k,2}\) and \(2\tau_{123}\), and compact source bases/pairings/
radicals/coproducts/PBW matrices.

The agent flagged that the provenance gate was theorem-styled without a
proof. The master thread added a proof after this report.

