# LWL Associativity

This packet records correction row 232.  It proves the ordered
mixed--mixed associativity identity on the \(LWL\) two-step flag stack:
\[
m_{\zeta_{12},\beta}^{WL}(m_{\alpha,\eta}^{LW}\otimes 1)
=
m_{\alpha,\zeta_{23}}^{LW}(1\otimes m_{\eta,\beta}^{WL}).
\]

The proof uses the row-229 \(LWL\) flag stack and supplied mixed
base-change, projection-formula, and reduced Thom--Sebastiani
coefficient identifications.  It does not prove the remaining word
associativity rows or the four-input pentagon.

Run:

```sh
python3 compute/verify_lwl_associativity_obstruction.py \
  --fixture certificates/hybrid/lwl_associativity --check
```

Expected status:

```text
LWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
