# Protected integration Pi_X separation

This packet records correction row 262: prove that protected
integration uses the normal-ordered Gram map \(\overline\Pi_X\), not
the geometric support degree \(b_R^{\mathrm{geom}}\).

The certified row supplies a finite lift
\[
\widehat\omega_R:\Gamma_R\to\widehat\Gamma_R
\]
and a zero-defect comparison
\[
g_R\omega_R=\overline\Pi_X\widehat\omega_R .
\]
Together with the Gram-degree row, this gives
\[
\deg_s(\chi_R I_R^{\mathrm{prot}}(x))
=\operatorname{pr}_3\overline\Pi_X(\widehat\omega_R(\gamma))
\]
for \(x\) of charge \(\gamma\).  The geometric map
\(b_R^{\mathrm{geom}}\) remains the local/wrapped support-splitting
degree; it is not the protected integration exponent.

Run:

```sh
python3 compute/verify_protected_integration_pi_x_separation_obstruction.py \
  --fixture certificates/hybrid/protected_integration_pi_x_separation --check
```

Expected status:

```text
PROTECTED_INTEGRATION_PI_X_SEPARATION_VERIFIED
```
