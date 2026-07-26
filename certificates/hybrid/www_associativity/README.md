# WWW Associativity

This packet records correction row 237.  It proves the
wrapped--wrapped/wrapped associativity identity on the \(WWW\)
two-step flag stack:
\[
m_{\zeta_{12},\eta_3}^{WW}(m_{\eta_1,\eta_2}^{WW}\otimes 1)
=
m_{\eta_1,\zeta_{23}}^{WW}(1\otimes m_{\eta_2,\eta_3}^{WW}).
\]

The proof uses the row-229 \(WWW\) flag stack and the
wrapped/wrapped target admissibility packet.  The wrapped/wrapped
base-change, projection-formula, and reduced Thom--Sebastiani rows
remain hypotheses of this packet; target admissibility alone does not
supply them.

Together with the previous seven packets this completes the
length-three wordwise associativity list.  It does not prove the
four-input pentagon.

Run:

```sh
python3 compute/verify_www_associativity_obstruction.py \
  --fixture certificates/hybrid/www_associativity --check
```

Expected status:

```text
WWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED
```
