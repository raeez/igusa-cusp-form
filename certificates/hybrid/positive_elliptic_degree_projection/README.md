# Positive Elliptic-Degree Projection

This packet records correction row 204.  The curve-theoretic theorem is:
if an effective one-cycle \(Z=\sum_i m_i C_i\) on \(K3\times E\) has
\[
(p_E)_*Z=b[E],\qquad b>0,
\]
then at least one component \(C_i\) maps dominantly to \(E\), hence
\[
p_E(|Z|)=E.
\]

For a retained object \(A\), the theorem applies only after a support
realization row identifies \(\operatorname{cyc}_1(A)\) with the
effective fundamental one-cycle of the one-dimensional support of
\(A\).  A positive value of the numerical coefficient
\(b_R^{\mathrm{geom}}\) alone is not used as a substitute for that
support realization row.

Run:

```sh
python3 compute/verify_positive_elliptic_degree_projection_obstruction.py \
  --fixture certificates/hybrid/positive_elliptic_degree_projection --check
```

Expected status:

```text
POSITIVE_ELLIPTIC_DEGREE_PROJECTION_VERIFIED
```

This status verifies the effective-cycle theorem and records the
missing object-level support rows fail-closed.
