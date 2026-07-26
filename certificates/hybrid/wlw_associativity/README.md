# WLW Associativity

This packet records correction row 235.  It proves the
wrapped--local/wrapped associativity identity on the \(WLW\) two-step
flag stack:
\[
m_{\zeta_{12},\eta_2}^{WW}(m_{\eta_1,\alpha}^{WL}\otimes 1)
=
m_{\eta_1,\zeta_{23}}^{WW}(1\otimes m_{\alpha,\eta_2}^{LW}).
\]

The proof uses the row-229 \(WLW\) flag stack, the mixed functorial
rows supplied in rows 225--227, and the wrapped/wrapped target
admissibility packet.  The wrapped/wrapped base-change,
projection-formula, and reduced Thom--Sebastiani rows remain
hypotheses of this packet; target admissibility alone does not supply
them.

It does not prove the \(WWL\) or \(WWW\) word associativity rows or
the four-input pentagon.

Run:

```sh
python3 compute/verify_wlw_associativity_obstruction.py \
  --fixture certificates/hybrid/wlw_associativity --check
```

Expected status:

```text
WLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
