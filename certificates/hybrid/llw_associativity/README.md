# LLW Associativity

This packet records correction row 231.  It proves the local/local--mixed
associativity identity on the \(LLW\) two-step flag stack:
\[
m_{\gamma_{12},\eta}^{LW}(m_{\alpha,\beta}^{LL}\otimes 1)
=
m_{\alpha,\zeta_{23}}^{LW}(1\otimes m_{\beta,\eta}^{LW}).
\]

The proof uses the row-229 \(LLW\) flag stack and supplied local/mixed
base-change, projection-formula, and reduced Thom--Sebastiani
coefficient identifications.  It does not prove the remaining word
associativity rows or the four-input pentagon.

Run:

```sh
python3 compute/verify_llw_associativity_obstruction.py \
  --fixture certificates/hybrid/llw_associativity --check
```

Expected status:

```text
LLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
