# rhomred_determinant

This packet verifies optimization row 277: the determinant line
\[
\det\operatorname{RHom}_{\mathrm{red}}(F,F)
\]
of the perfect reduced self-Ext complex.

The input is row 276:
\[
\operatorname{RHom}_{\mathrm{red}}(F,F)
\in \operatorname{Perf}(\mathfrak M^{\mathrm{rig}}_{R,c}).
\]
The row applies the Knudsen--Mumford determinant functor and records one
determinant line for each retained finite substack.

This packet does not construct a square-root orientation, does not
compute \(w_2\), and does not supply quotient orientation, transition
compatibility, vanishing cycles, or protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_determinant_fixture.py \
  --fixture certificates/orientation/rhomred_determinant --check
```
