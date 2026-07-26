# rhomred_square_root

This packet verifies the row-278 obstruction ledger for the square root
of the reduced determinant line.

For a determinant line \(\mathcal L^{\det}_F\), a square root is a line
\[
o_F
\]
together with an isomorphism
\[
o_F^{\otimes 2}\simeq \mathcal L^{\det}_F .
\]
Equivalently, \(\mathcal L^{\det}_F\) lies in the image of the squaring
map on the Picard groupoid.  The present reduced-orientation packet
contains no such rows.

This packet does not construct a square-root orientation, does not
compute \(w_2\), and does not supply quotient orientation, transition
compatibility, vanishing cycles, or protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_square_root_obstruction.py \
  --fixture certificates/orientation/rhomred_square_root --check
```
