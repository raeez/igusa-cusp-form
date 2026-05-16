# A217 -- Chiral `w_algebras_deep` postpatch verifier

## Claim attacked

The chiral-bar-cobar synthesis needed a postpatch check for overclaiming
\(\mathbf H_{\Delta_5}\) as an already constructed W-algebraic object.

## Findings

Fatal: none.

High: none.

Medium:

- `/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5686`
  still said the Andrianov decomposition "splits W-algebraic Hecke
  spectrum on \(\mathbf H_{\Delta_5}\)" without the R1--R5 conditional
  guard.

## Files changed by agent

None. The main thread replaced the sentence with target-comparison
language.

## Verification

Commands reported:

```bash
git diff --check -- chapters/examples/w_algebras_deep.tex compute/tests/test_cy_bkm_algebra_engine.py
PYTHONDONTWRITEBYTECODE=1 ./.venv/bin/python -m unittest compute.tests.test_cy_bkm_algebra_engine
```

Status after integration: diff check clean; `138` tests passed.

## Residual obligation

Chiral-bar-cobar may compare to the \(\Delta_5\) Hecke/BKM target only
after the source gates R1--R5. It must not assert construction of
\(\mathbf H_{\Delta_5}\) inside Vol I.
