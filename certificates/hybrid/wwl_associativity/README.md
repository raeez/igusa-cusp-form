# WWL Associativity

This packet records correction row 236.  It proves the
wrapped--wrapped/local associativity identity on the \(WWL\) two-step
flag stack:
\[
m_{\zeta_{12},\alpha}^{WL}(m_{\eta_1,\eta_2}^{WW}\otimes 1)
=
m_{\eta_1,\zeta_{23}}^{WW}(1\otimes m_{\eta_2,\alpha}^{WL}).
\]

The proof uses the row-229 \(WWL\) flag stack, the mixed functorial
rows supplied in rows 225--227, and the wrapped/wrapped target
admissibility packet.  The wrapped/wrapped base-change,
projection-formula, and reduced Thom--Sebastiani rows remain
hypotheses of this packet; target admissibility alone does not supply
them.

It does not prove the \(WWW\) word associativity row or the four-input
pentagon.

Run:

```sh
python3 compute/verify_wwl_associativity_obstruction.py \
  --fixture certificates/hybrid/wwl_associativity --check
```

Expected status:

```text
WWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
