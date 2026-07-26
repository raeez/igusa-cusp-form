# joyce_dcritical_truncation

This packet records correction row 272: the Joyce d-critical structure
on the classical truncation of each retained finite derived substack.

It imports `certificates/orientation/ptvv_finite_substack_symplectic`
and applies the BBDJS d-critical truncation theorem to the three
retained rows.  The packet records a d-critical structure on each
classical truncation and zero d-critical defect.

It does not construct BBDJS vanishing-cycle complexes, the K3
semiregularity cosection, cosection surjectivity, the reduced self-Ext
complex, the determinant line, a square-root orientation, quotient
orientation, transition compatibility, or protected integration.

Verify with:

```bash
python3 compute/verify_joyce_dcritical_truncation_fixture.py \
  --fixture certificates/orientation/joyce_dcritical_truncation --check
```
