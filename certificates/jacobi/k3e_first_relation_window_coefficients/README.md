# k3e_first_relation_window_coefficients

This fixture is the finite target-arithmetic certificate for the first
relation-closed degree rows.  It recomputes the Jacobi coefficients
\(f(nm,l)=c(nm,l)\) from the theta-series definition of
\(\phi_{0,1}\) used by `compute/verify_square_root.py`, then compares
them with the signed dimensions in the A071 target presentation fixture.
The table `normalization_laws.csv` fixes the leading normalization
\(\phi_{0,1}=r^{-1}+10+r+O(q)\), verifies finite instances of
\(f(n,l)=f(n,-l)\), and checks the index-one discriminant dependence
\(f(n,l)=c(4n-l^2)\) on the first relation-closed window.

The certificate is deliberately narrower than the compact-source first
window.  It proves only the arithmetic equality between the Jacobi
coefficient and the target signed dimension for these rows.  It does not
construct source representatives, parity splits, Hall brackets, pairing
kernels, PBW associated gradeds, or primitive recognition.

Run:

```sh
python3 compute/verify_jacobi_window_fixture.py \
  --fixture certificates/jacobi/k3e_first_relation_window_coefficients \
  --check
```

A positive result is `COEFFICIENT_TABLE_VERIFIED`.
