# rhomred_definition

This packet verifies optimization row 275: the cone definition of
\(\operatorname{RHom}_{\mathrm{red}}(F,F)\).

The definition is
\[
\operatorname{RHom}_{\mathrm{red}}(F,F)
=
\operatorname{fib}\!\left(
\operatorname{RHom}_X(F,F)
\xrightarrow{(\operatorname{tr},\operatorname{CS}_F)}
R\Gamma(X,\mathcal O_X)\oplus H^2(S,\mathcal O_S)[-1]
\right)
=\operatorname{Cone}(\Theta_F)[-1].
\]

This packet does not prove that the cone is perfect, does not define
its determinant line, and does not construct a square-root orientation.
Those are rows 276--278.

The cone formula uses the cosection map.  Surjectivity is not needed to
form the cone; it is needed later to identify this cone with the
Kiem--Li reduced obstruction theory on the retained branch.

Verify with:

```sh
python3 compute/verify_rhomred_definition_fixture.py \
  --fixture certificates/orientation/rhomred_definition --check
```
