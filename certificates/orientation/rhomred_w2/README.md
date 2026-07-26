# rhomred_w2

This packet verifies the row-279 formula and obstruction ledger for the
second Stiefel--Whitney class of the reduced determinant line.

For the complex determinant line \(\mathcal L^{\det}_F\),
\[
w_2((\mathcal L^{\det}_F)_{\mathbb R})=c_1(\mathcal L^{\det}_F)\bmod 2.
\]
The determinant-of-cohomology input needed to evaluate \(c_1\) is the
degree-one Grothendieck--Riemann--Roch pushforward of the reduced kernel.

This packet records the formula and verifies that no retained-stratum
\(c_1\), GRR expansion, mod-\(2\) reduction, or \(w_2\)-value row is
present.  It does not prove \(w_2=0\), construct a square-root
orientation, or supply quotient orientation, transition compatibility,
vanishing cycles, or protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_w2_obstruction.py \
  --fixture certificates/orientation/rhomred_w2 --check
```
