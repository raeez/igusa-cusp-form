# k3_semiregularity_cosection

This packet verifies row 273 of the K3 x E optimization ledger: the
K3 semiregularity cosection on the obstruction sheaf of each retained
finite classical truncation.

It imports the PTVV finite-substack input and the Joyce d-critical
truncation rows, then records the Atiyah-class formula induced by
\(p_S^*\sigma_S\):
\[
\operatorname{CS}_F(\xi)=\int_X p_S^*\sigma_S\wedge
\operatorname{Tr}((\xi\otimes 1_{\Omega_X^1})\circ\operatorname{At}(F)).
\]

It does not prove cosection surjectivity, filtered Hall additivity,
reduced self-Ext perfectness, determinant lines, square-root
orientations, quotient orientation, transition compatibility, BBDJS
vanishing cycles, or protected integration.

Verify with:

```sh
python3 compute/verify_k3_semiregularity_cosection_fixture.py \
  --fixture certificates/orientation/k3_semiregularity_cosection --check
```
