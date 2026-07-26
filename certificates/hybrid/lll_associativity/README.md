# LLL Associativity

This packet records correction row 230.  It proves the pure local
associativity identity on the \(LLL\) two-step flag stack:
\[
m_{\gamma_{12},\delta}^{LL}(m_{\alpha,\beta}^{LL}\otimes 1)
=
m_{\alpha,\gamma_{23}}^{LL}(1\otimes m_{\beta,\delta}^{LL}).
\]

The proof uses the row-229 \(LLL\) flag stack and the supplied local
base-change, projection-formula, and reduced Thom--Sebastiani
coefficient identifications on that flag square.  It does not prove any
mixed or wrapped word associativity row and does not prove the
four-input pentagon.

Run:

```sh
python3 compute/verify_lll_associativity_obstruction.py \
  --fixture certificates/hybrid/lll_associativity --check
```

Expected status:

```text
LLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
