# rhomred_finite_stabilizer_linearization_character

This packet verifies the row-288 obstruction ledger for computing the
finite-stabilizer linearization character
\[
\lambda^H_{\mathcal C,S}\in H^1(BH;\mathbb F_2).
\]

After the degree-two finite-stabilizer gerbe is trivialized, a choice
of linearization on the orientation line differs by a sign character of
\(H\).  Row 288 computes this character from an actual
orientation-line action, generator-basis provenance for the retained
finite stabilizer, and character values on those generators.  Row 289
is the later assertion that the computed character is zero.

This packet imports the row-287 beta-nulltrivialization packet, the
reduced-orientation obstruction ledger, and the determinant-anchor
translation-weight packet.  It records that the current tables supply
no orientation-line action rows, no generator-basis rows, no character
values, and no \(H^1\)-coordinate rows.  The translation-weight packet
computes \(h\mapsto\chi_\eta h\) on classes but marks coherent
stabilizer linearization as not certified.

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_linearization_character_obstruction.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_linearization_character --check
```
