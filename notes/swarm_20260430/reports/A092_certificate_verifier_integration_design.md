# A092 certificate verifier integration design

No files edited. The agent inspected `CLAUDE.md`, the rectify skill,
A067/A072/A076/A081/A086, current `compute/`, and confirmed that
`certificates/` does not exist. Current `compute/verify_lattice.py` and
`compute/verify_square_root.py` are target-side only.

## Smallest integration

Add only these path families:

```text
compute/verify_source_fixture.py
compute/tests/test_verify_source_fixture.py

certificates/README.md
certificates/schemas/source_fixture.v1.schema.yaml
certificates/schemas/target_fixture.v1.schema.yaml
certificates/schemas/verifier_run.v1.schema.yaml

certificates/targets/delta5_gn_kac/wle3-v1/
certificates/wle3/<certificate_id>/
certificates/fixtures/
```

`certificates/fixtures/` must be verifier tests, not manuscript evidence.

## CLI

```bash
python3 compute/verify_source_fixture.py \
  certificates/wle3/<certificate_id> \
  --window W_le3 \
  --mode proof \
  --target-dir certificates/targets/delta5_gn_kac/wle3-v1 \
  --out-dir certificates/wle3/<certificate_id>/verification/<run_id>
```

Modes: `--mode proof`, `--allow-mock`, `--dry-run`, `--run-id <id>`,
and `--strict`.

Exit policy:

```text
0  CERTIFIED, or mock plumbing passed under --allow-mock with certified=false
1  mathematical verifier failure
2  schema/preflight failure
3  proof refused: missing, mock, or target-only source
4  internal verifier error
```

## Verifier gates

Certification requires preflight/hash/source-kind checks, exact scalar
firewall, window/downward saturation, source provenance, pair and
decomposition coverage, \(M,D,G\) construction, \(B\) supercommutator,
radical kernel and splitting, NO7 bracket and coproduct descent, Hopf
adjointness, relation rows, \(A\) comparison maps, generation,
no-extra kernel equality, PBW associated-graded comparison, and strict
transition/Mittag--Leffler compatibility.

For \(W_{\le3}\), height-four and height-seven terminal rows may be
deferred only when explicitly outside the window. For \(W_{\le7}\), those
same rows must be certified.

## Manuscript reference rule

Do not `\input` generated verifier summaries into `main.tex`. After a
real `CERTIFIED` run, add only an artifact sentence near the finite
source criterion naming `verifier.json` and `verifier-summary.tex`. Until
then, `main.tex` should continue to say the existing scripts verify
target arithmetic only. Target arithmetic alone must never produce
`CERTIFIED`.

