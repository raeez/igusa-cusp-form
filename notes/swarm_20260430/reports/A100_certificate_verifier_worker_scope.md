# A100 certificate verifier worker scope

Read-only inspection completed. No files edited. Current repo has
`compute/verify_lattice.py` and `compute/verify_square_root.py` only;
both are target-side. There is no `tests/` or `certificates/` directory
yet.

## Smallest disjoint package

Future worker owns only:

- `compute/verify_source_fixture.py`
- `compute/tests/test_verify_source_fixture.py`
- `certificates/README.md`
- `certificates/schemas/source_fixture.v1.schema.yaml`
- `certificates/schemas/target_fixture.v1.schema.yaml`
- `certificates/schemas/verifier_run.v1.schema.yaml`
- `certificates/targets/delta5_gn_kac/wle3-v1/**`
- `certificates/fixtures/source_fixture_verifier/**`

Explicitly not owned: `main.tex`, `proj.bib`, `notes/**`, existing
`compute/verify_lattice.py`, existing `compute/verify_square_root.py`,
and `Makefile`.

## Milestones

1. Scaffold CLI:
   `python3 compute/verify_source_fixture.py <packet> --window W_le3 --mode proof --target-dir ... --out-dir ...`.
   Emit `verifier.json` and `verifier-summary.tex`; implement A092 exit
   codes.
2. Implement preflight/firewall gates: manifest loading, hashes, exact
   scalar parsing, `source_kind`, window saturation, target-label
   firewall.
3. Add target fixture reader under `certificates/targets/...`; verify
   \(W_{\le3}\) target rows \(1|0\), \(10|0\), \(1|0\), \(29|93\).
4. Add source algebra gates: sparse exact matrices over \(\mathbb Z\) or
   \(\mathbb Q\), \(B=M-(-1)^{|x||y|}M\mathsf{sw}\), radical \(K\),
   splitting \(Q\), NO7 descent, Hopf adjointness.
5. Add recognition gates: relation rows, comparison maps, generation,
   no-extra kernel equality, PBW associated-graded rank checks, and
   transition/ML strictness.
6. Add fixture suite as verifier tests only, not manuscript evidence and
   not canonical populated source certificates.

## Required tests

```bash
python3 -m unittest discover -s compute/tests -p 'test_*.py'
python3 compute/verify_lattice.py
python3 compute/verify_square_root.py
```

Fixture cases: missing packet, target-only reference, mock source,
bad target-label source, bad float scalar, bad radical, bad NO7, bad
no-extra, bad PBW, \(W_{\le3}\) terminal overclaim, and \(W_{\le7}\)
deferred terminal.

## Certification guardrail

`CERTIFIED` may be emitted only when `mode == proof`,
`source_kind == compact_source_candidate`, the packet is neither mock nor
target-only, all mandatory source gates pass, no forbidden target labels
occur in source tables, and \(M,D,G,K,Q,A\), no-extra, PBW, and transition
data are present and checked. Target arithmetic, signed dimensions,
target PBW ranks, or target basis templates may pass as target reference
checks, but they must never set `certified=true`.

