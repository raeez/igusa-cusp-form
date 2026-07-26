# Determinant Anchor Construction

This packet records correction row 213. Given a retained universal
perfect complex \(\mathcal F_{\eta,R}\) on the wrapped prequotient row
and the projection \(\pi_{E,T}:X\times T\to E\times T\), it constructs
the normalized determinant anchor
\[
\lambda^{\det}_{\eta,R}(\mathcal F_{\eta,R})
=\det R\pi_{E,T,*}\mathcal F_{\eta,R}
\otimes \mathcal O_E(-\chi_\eta\cdot 0_E).
\]
The determinant line has relative degree \(\chi_\eta\) on the elliptic
curve, so the normalization has degree zero and defines a \(T\)-point
of \(\operatorname{Pic}^0(E)\simeq E\). The determinant functor is used
only for this construction and base-change functoriality.

This packet does not compute the \(E\)-translation weight; that row is
separated in `certificates/hybrid/determinant_anchor_translation_weight`.
It does not make the weight one by a finite cover.  The \(\chi=0\)
degeneracy is separated in
`certificates/hybrid/determinant_anchor_chi_zero_degeneracy`.  This
packet does not add the extra anchor data distinguishing
\(\mathcal O_E^{\oplus2}\) from \(L\oplus L^{-1}\); that row is
separated in
`certificates/hybrid/determinant_anchor_extra_anchor_data`.  It does
not define \(o^\lambda_R\); that row is separated in
`certificates/hybrid/anchor_residual_definition`.

Run:

```sh
python3 compute/verify_determinant_anchor_construction_obstruction.py \
  --fixture certificates/hybrid/determinant_anchor_construction --check
```

Expected status:

```text
DETERMINANT_ANCHOR_CONSTRUCTION_VERIFIED
```
