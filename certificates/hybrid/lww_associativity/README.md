# LWW Associativity

This packet records correction row 234.  It proves the
local--wrapped/wrapped associativity identity on the \(LWW\) two-step
flag stack:
\[
m_{\zeta_{12},\eta_2}^{WW}(m_{\alpha,\eta_1}^{LW}\otimes 1)
=
m_{\alpha,\zeta_{23}}^{LW}(1\otimes m_{\eta_1,\eta_2}^{WW}).
\]

The proof uses the row-229 \(LWW\) flag stack, the mixed functorial
rows supplied in rows 225--227, and the wrapped/wrapped target
admissibility packet.  The wrapped/wrapped base-change,
projection-formula, and reduced Thom--Sebastiani rows remain
hypotheses of this packet; target admissibility alone does not supply
them.

It does not prove the \(WLW\), \(WWL\), or \(WWW\) word associativity
rows or the four-input pentagon.

Run:

```sh
python3 compute/verify_lww_associativity_obstruction.py \
  --fixture certificates/hybrid/lww_associativity --check
```

Expected status:

```text
LWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
