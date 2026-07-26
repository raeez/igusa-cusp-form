# rhomred_perfectness

This packet verifies optimization row 276: perfectness of the
cosection-reduced self-Ext cone
\[
\operatorname{RHom}_{\mathrm{red}}(F,F)
=\operatorname{fib}\!\left(
\operatorname{RHom}_X(F,F)
\xrightarrow{\Theta_F}
R\Gamma(X,\mathcal O_X)\oplus H^2(S,\mathcal O_S)[-1]
\right).
\]

The proof imports the retained universal perfect complex
\(\mathcal U_{R,c}\), applies proper perfect pushforward to
\(R\mathcal Hom(\mathcal U_{R,c},\mathcal U_{R,c})\), and uses closure of
perfect complexes under fibres.  The packet checks the three retained
rows and records zero perfectness defect.

This packet does not prove cosection surjectivity, does not define
\(\det\operatorname{RHom}_{\mathrm{red}}\), and does not construct a
square-root orientation.  Those are separate rows.

Verify with:

```sh
python3 compute/verify_rhomred_perfectness_fixture.py \
  --fixture certificates/orientation/rhomred_perfectness --check
```
