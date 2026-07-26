# Mixed Correspondence Thom--Sebastiani Transport

This packet records correction row 227.  For the one-sided mixed
orders \(LW\) and \(WL\), it records the binary reduced
Thom--Sebastiani transport
\[
\operatorname{TS}^{\mathrm{red},o}:
(p^o)^*K^o_{\mathrm{src}}\simeq K^o_{\mathfrak E}.
\]

The proof is conditional on supplied additive d-critical charts,
compatibility with the reduced K3 semiregularity cosection, and
zero-defect Joyce--Upmeier orientation transport.  It proves transport
from those data; it does not construct the orientation line or
discharge \((O1)\).  Quotient descent is supplied separately by
`certificates/hybrid/quotient_after_correspondence_thom_sebastiani`.
Transition compatibility and the two-step flag pentagon remain open.

Run:

```sh
python3 compute/verify_mixed_correspondence_thom_sebastiani_obstruction.py \
  --fixture certificates/hybrid/mixed_correspondence_thom_sebastiani --check
```

Expected status:

```text
MIXED_THOM_SEBASTIANI_TRANSPORT_CONDITIONAL_VERIFIED
```
