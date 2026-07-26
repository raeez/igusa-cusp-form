# Higher-Coloured Tree Category Definition

This packet records correction row 239.  It defines the nonunital
higher-coloured hybrid tree category
\(\mathsf{Tree}^{E,\mathrm{hyb}}_R\) and names the six components of
the residual
\[
\mathfrak o^{\mathrm{col}}_R
=(\mathfrak o^{\mathrm{tree}}_R,\mathfrak o^{\mathrm{unit}}_R,
\mathfrak o^{\mathrm{sym}}_R,\mathfrak o^{\mathrm{ref}}_R,
\mathfrak o^{\mathrm{des}}_R,\mathfrak o^{\mathrm{ov}}_R).
\]

It is a definition-only packet.  It does not prove
\(\mathfrak o^{\mathrm{col}}_R=0\), does not supply units, and does
not prove symmetric descent, wrapped order conventions, quotient
descent, transition compatibility, or aggregate population.

Run:

```sh
python3 compute/verify_higher_coloured_tree_category_definition_obstruction.py \
  --fixture certificates/hybrid/higher_coloured_tree_category_definition --check
```

Expected status:

```text
HIGHER_COLOURED_TREE_CATEGORY_DEFINED
```
