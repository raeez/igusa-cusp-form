# Compact-Support Exceptional Pushforward Model

This packet records correction row 224.  For a retained finite
correspondence map
\[
f:\mathfrak E\to Z
\]
with coefficient complex \(K_{\mathfrak E}\), the model is a chosen
compactification
\[
\mathfrak E\xhookrightarrow{j_f}\overline{\mathfrak E}_f
\xrightarrow{\overline f} Z,
\qquad \overline f \text{ proper},
\]
and the definition
\[
f^{\mathrm{cs}}_!K_{\mathfrak E}
:=\overline f_*j_{f,!}K_{\mathfrak E}.
\]

If \(f\) is proper, the identity compactification is allowed and the
model gives \(f^{\mathrm{cs}}_!=f_*\).  This packet defines the
compact-support model; it does not prove independence of
compactification choices, populate every correspondence map, or prove
base change, projection formula, Thom--Sebastiani transport, symmetric
descent, quotient descent, transition compatibility, or associativity.

Run:

```sh
python3 compute/verify_compact_support_exceptional_pushforward_model_obstruction.py \
  --fixture certificates/hybrid/compact_support_exceptional_pushforward_model --check
```

Expected status:

```text
COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED
```
