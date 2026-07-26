# WLL Associativity

This packet records correction row 233.  It proves the mixed--local/local
associativity identity on the \(WLL\) two-step flag stack:
\[
m_{\zeta_{12},\beta}^{WL}(m_{\eta,\alpha}^{WL}\otimes 1)
=
m_{\eta,\gamma_{23}}^{WL}(1\otimes m_{\alpha,\beta}^{LL}).
\]

The proof uses the row-229 \(WLL\) flag stack and supplied local/mixed
base-change, projection-formula, and reduced Thom--Sebastiani
coefficient identifications.  It does not prove the \(WW\)-dependent
word associativity rows or the four-input pentagon.

Run:

```sh
python3 compute/verify_wll_associativity_obstruction.py \
  --fixture certificates/hybrid/wll_associativity --check
```

Expected status:

```text
WLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
