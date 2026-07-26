# Finite Test Window Definition

This packet records the definition of the finite target test window
\(\Gamma_R^{\mathrm{test}}\).  For a finite HN charge set
\(\Gamma_R^{HN}\) and finite normal-ordering translate sets
\(\mathcal T_R(c)\), the window is
\[
\Gamma_R^{\mathrm{test}}
=\overline\Pi_X(\widehat\Gamma_R)
=\{\Pi_X(c)+T\mid c\in\Gamma_R^{HN},\ T\in\mathcal T_R(c)\}
\subset \Gamma_{\mathrm{gram}} .
\]

Run:

```sh
python3 compute/verify_finite_test_window_definition_obstruction.py \
  --fixture certificates/charge/finite_test_window --check
```

Expected status:

```text
FINITE_TEST_WINDOW_DEFINITION_VERIFIED
```

This status verifies the definition row and the obstruction ledger.  It
does not supply HN charge rows, normal-ordered lift orbits,
test-window membership rows, finiteness witnesses, transition rows, or
the row-200 statement that every relation-closed target degree appears
at finite \(R\).  Row 200 is tracked separately by
`certificates/charge/relation_closed_target_finite_R_exhaustion`.
