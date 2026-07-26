# Protected integration Gram degree

This packet records correction row 261: prove that the protected
integration target has formal Gram monomial degree \(q^n r^l s^m\).

The certified row supplies a monomialization
\[
\chi_R(e_{\omega_R(\gamma)})
=q^{n_R(\gamma)}r^{l_R(\gamma)}s^{m_R(\gamma)}
\]
and proves
\[
(\chi_R I_R^{\mathrm{prot}})(x)
\in
\mathbb C q^{n_R(\gamma)}r^{l_R(\gamma)}s^{m_R(\gamma)}
\]
for \(x\) of charge \(\gamma\).

The comparison \(g_R\omega_R=\overline\Pi_X\widehat\omega_R\), and the
exclusion of \(b_R^{\mathrm{geom}}\) as protected-integration exponent,
are supplied separately by
`certificates/hybrid/protected_integration_pi_x_separation`.

Run:

```sh
python3 compute/verify_protected_integration_gram_degree_obstruction.py \
  --fixture certificates/hybrid/protected_integration_gram_degree --check
```

Expected status:

```text
PROTECTED_INTEGRATION_GRAM_DEGREE_VERIFIED
```
