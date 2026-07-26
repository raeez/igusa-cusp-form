# rhomred_weyl_orientation_torsor_defects

This packet verifies row 313 as a finite computation criterion for the
Weyl torsor defects.  Given a row-306 Weyl lift and populated
quotient-orientation cochains, the torsor-defect cochain is
\[
\Delta^\omega_{i,R,S}
=\Theta^1_{i,R,S}(\eta_{R,S})-\eta_{R,s_{\delta_i}S},
\]
and row 313 records the cohomology class
\[
\omega_{i,R,S}=[\Delta^\omega_{i,R,S}]
\in H^1(\mathfrak M^{\mathrm{red}}_{R,s_{\delta_i}S};\mathbb F_2)
\oplus\bigoplus_H H^1(BH;\mathbb F_2).
\]

The current tree does not supply Weyl-lift rows, quotient Borel
representatives, finite-stabilizer transport rows, linearization
transport rows, \(H^1\)-basis rows, or torsor-defect vectors.  Row 314,
the vanishing of all \(\omega_{i,R,S}\), is not certified here.

Run:

```sh
python3 compute/verify_rhomred_weyl_orientation_torsor_defects.py \
  --fixture certificates/orientation/rhomred_weyl_orientation_torsor_defects --check
```
