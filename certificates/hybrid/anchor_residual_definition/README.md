# Anchor Residual Definition

This packet records correction row 217.  It defines the finite anchor
residual
\[
\mathfrak o^\lambda_R=
(\mathfrak o^{\lambda,\mathrm{ex}}_R,
\mathfrak o^{\lambda,\mathrm{unit}}_R,
\mathfrak o^{\lambda,\mathrm{loss}}_R,
\mathfrak o^{\lambda,\mathrm{multi}}_R,
\mathfrak o^{\lambda,\mathrm{tr}}_{R'R})
\]
for repaired wrapped anchors.  The repaired target is
\[
\mathcal A_{\eta,R}=\operatorname{Sym}^{r_\eta}\operatorname{Pic}^0(E),
\]
with Abel-sum projection to \(\operatorname{Pic}^0(E)\simeq E\).  The
Jordan-Hoelder divisor from row 216 is the extra-anchor component on
the degree-zero vector-bundle row.  The \(E\)-valued source/target
anchors are only Abel-sum shadows of this repaired target.

The packet defines the zero condition for each residual component.  It
does not prove first-window vanishing, global losslessness, quotient
descent, stabilizer linearization, finite-stage population, or
transition compatibility.  The current first-window obstruction is
recorded in `certificates/hybrid/anchor_residual_first_window_obstruction`.

Run:

```sh
python3 compute/verify_anchor_residual_definition_obstruction.py \
  --fixture certificates/hybrid/anchor_residual_definition --check
```

Expected status:

```text
ANCHOR_RESIDUAL_DEFINITION_VERIFIED
```
