# A145 -- Chiral-Bar-Cobar Coefficient API Patch

## Claim Attacked

The chiral-bar-cobar BKM compute engine conflated Jacobi coefficients,
signed Borcherds product exponents, and super root multiplicities, and
the tests described hardcoded finite checks as broad recognition.

## Patch

The coefficient/root terminology was split in:

- `compute/lib/cy_bkm_algebra_engine.py`
- `compute/tests/test_cy_bkm_algebra_engine.py`

The module now presents itself as a finite sanity engine, not a
denominator/root-system recognition engine.

## Verification

```text
python3 -m py_compile compute/lib/cy_bkm_algebra_engine.py compute/tests/test_cy_bkm_algebra_engine.py
pytest compute/tests/test_cy_bkm_algebra_engine.py
git diff --check -- compute/lib/cy_bkm_algebra_engine.py compute/tests/test_cy_bkm_algebra_engine.py
```

Compile passed, pytest passed with `138 passed`, and diff check passed.
`python -m py_compile` failed only because `python` is not installed;
`python3` was used successfully.

## Residual Caveat

The module remains finite sanity machinery. It does not prove
denominator/root-system recognition.
