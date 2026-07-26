# Determinant Anchor Chi-Zero Degeneracy

This packet records correction row 215.  It imports the determinant
anchor translation law
\[
\lambda^{\det}_{\eta,R}(a\cdot\mathcal F)
=\lambda^{\det}_{\eta,R}(\mathcal F)+\chi_\eta a
\]
and specializes it to the branch \(\chi_\eta=0\).  On this branch
\[
\lambda^{\det}_{\eta,R}(a\cdot\mathcal F)
=\lambda^{\det}_{\eta,R}(\mathcal F)
\]
for every translation \(a\in E\).  Since the retained
\(E\)-translation action is free on the finite row, the determinant
anchor is constant on a nontrivial one-dimensional orbit.  It therefore
does not remember relative elliptic position.

This packet handles the degeneracy by recording the orbit-constant
failure and the required repair boundary: the final wrapped anchor on
the \(\chi_\eta=0\) branch needs extra anchor data.  The construction of
the determinant-refining Jordan-Hoelder divisor is row 216, not this
packet.  The anchor-residual definition is row 217.  Full anchor
losslessness, quotient descent, stabilizer linearization, transition
compatibility, and \(o^\lambda_R=0\) are still separate obligations.

Run:

```sh
python3 compute/verify_determinant_anchor_chi_zero_degeneracy_obstruction.py \
  --fixture certificates/hybrid/determinant_anchor_chi_zero_degeneracy --check
```

Expected status:

```text
DETERMINANT_ANCHOR_CHI_ZERO_DEGENERACY_VERIFIED
```
