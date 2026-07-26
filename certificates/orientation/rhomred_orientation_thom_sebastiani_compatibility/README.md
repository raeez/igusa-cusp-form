# rhomred_orientation_thom_sebastiani_compatibility

This packet verifies row 301 as a criterion and obstruction ledger:
Thom--Sebastiani compatibility for orientation lines is the statement
that the Joyce--Upmeier orientation transport is the square root of
the determinant Thom--Sebastiani comparison and tensors with BBDJS
Thom--Sebastiani to give the oriented coefficient-system transport.

The required square is
\[
(\operatorname{TS}^{o}_{\mathfrak E})^{\otimes2}
=\det(\operatorname{TS}^{\mathrm{red}}_{\mathfrak E})
\]
after identifying each orientation line with its determinant square.
The required coefficient-system identity is
\[
\operatorname{TS}^{\Phi\otimes o}_{\mathfrak E}
=\operatorname{TS}^{\Phi,\mathrm{red}}_{\mathfrak E}\otimes
\operatorname{TS}^{o}_{\mathfrak E}.
\]

The current packets do not supply this row.  The mixed
Thom--Sebastiani packet is conditional on orientation transport, and
the four-input pentagon packet treats the orientation pentagon as an
input.

Run:

```sh
python3 compute/verify_rhomred_orientation_thom_sebastiani_compatibility.py \
  --fixture certificates/orientation/rhomred_orientation_thom_sebastiani_compatibility --check
```
