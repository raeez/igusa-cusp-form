# Determinant Anchor Translation Weight

This packet records correction row 214.  It imports the normalized
determinant anchor
\[
\lambda^{\det}_{\eta,R}(\mathcal F)
=\det R\pi_{E,*}\mathcal F\otimes \mathcal O_E(-\chi_\eta\cdot 0_E)
\]
and the retained \(E\)-translation action.  For the support-translation
convention
\[
a\cdot\mathcal F=(\operatorname{id}_S\times\tau_a)_*\mathcal F,
\qquad \tau_a(x)=x+a,
\]
it proves
\[
\lambda^{\det}_{\eta,R}(a\cdot\mathcal F)
\simeq
\lambda^{\det}_{\eta,R}(\mathcal F)\otimes
\mathcal O_E(\chi_\eta(a-0_E)).
\]
Thus, under \(\operatorname{Pic}^0(E)\simeq E\), the translation weight
is the homomorphism \([\chi_\eta]:E\to E\).

The packet records the restriction to a finite stabilizer
\(H\subset E[N]\) as \(h\mapsto\chi_\eta h\).  It does not choose the
coherent stabilizer linearization, does not make the weight one by a
finite cover, and does not handle the \(\chi_\eta=0\) degeneracy.  The
zero-Euler degeneracy is separated in
`certificates/hybrid/determinant_anchor_chi_zero_degeneracy`.  This
packet does not add the Jordan-Hoelder extra-anchor data, separated in
`certificates/hybrid/determinant_anchor_extra_anchor_data`, and does
not define \(o^\lambda_R\), separated in
`certificates/hybrid/anchor_residual_definition`.

Run:

```sh
python3 compute/verify_determinant_anchor_translation_weight_obstruction.py \
  --fixture certificates/hybrid/determinant_anchor_translation_weight --check
```

Expected status:

```text
DETERMINANT_ANCHOR_TRANSLATION_WEIGHT_VERIFIED
```
