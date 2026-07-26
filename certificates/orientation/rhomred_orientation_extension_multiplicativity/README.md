# rhomred_orientation_extension_multiplicativity

This packet verifies row 300 as a criterion and obstruction ledger:
orientation multiplicativity under extensions is a Joyce--Upmeier
Picard-groupoid isomorphism on the retained extension stack.

For
\[
\mathfrak M_{R,\widehat c}^{\mathrm{red}}\times
\mathfrak M_{R,\widehat c'}^{\mathrm{red}}
\xleftarrow{p}
\overline{\mathfrak E}_{R,\widehat c,\widehat c'}^{\mathrm{red}}
\xrightarrow{q}
\mathfrak M_{R,\widehat c+\widehat c'}^{\mathrm{red}},
\]
the required row is
\[
p_1^*o_{R,\widehat c}\otimes p_2^*o_{R,\widehat c'}
\simeq q^*o_{R,\widehat c+\widehat c'}
\]
with determinant-square compatibility and zero two-step flag pentagon
defect.  Tensoring this orientation isomorphism with BBDJS
Thom--Sebastiani gives the coefficient-system transport used in the
Hall product.

The current finite data do not supply this row.  Retained extension
closure gives middle terms only, and the mixed Thom--Sebastiani packet
is conditional on orientation transport.

Run:

```sh
python3 compute/verify_rhomred_orientation_extension_multiplicativity.py \
  --fixture certificates/orientation/rhomred_orientation_extension_multiplicativity --check
```
