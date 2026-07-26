# ptvv_finite_substack_symplectic

This packet records correction row 271: the PTVV `(-1)`-shifted
symplectic form on the retained finite derived substacks.

It imports `certificates/moduli/retained_derived_enhancements`, checks
the three retained substacks, and records shifted degree `-1`,
cotangent amplitude `[-1,0]`, and zero symplectic defect on each row.

It does not construct the Joyce d-critical truncation, the K3
semiregularity cosection, cosection surjectivity, the reduced self-Ext
complex, the determinant line, a square-root orientation, quotient
orientation, O2 wall-atlas rows, or protected integration.

Verify with:

```bash
python3 compute/verify_ptvv_finite_substack_symplectic_fixture.py \
  --fixture certificates/orientation/ptvv_finite_substack_symplectic --check
```
