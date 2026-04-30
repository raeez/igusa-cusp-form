# A096 Vol III patch verifier checklist

Read-only verification done. No files edited.

Current checkout is pre-patch for the A084 checklist:
`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`
still has the old construction, the bare coefficient-projection map, and
the product-compatibility claim.

## Post-edit checklist

- `prop:k3e-borcherds-coefficient-recognition-gate` must occur exactly
  once in `chapters/examples/k3e_cy3_programme.tex`.
- `constr:k3e-hcs-hall-borcherds-comparison` must be preserved exactly
  once as an alias in the same proposition.
- `thm:k3e-positive-half-hall-borcherds-criterion` already exists in
  `chapters/examples/k3e_bkm_chapter.tex`.
- Dependent prose at current lines 106, 4201, and 4222 should point to
  the new proposition and the finite criterion theorem, not to a bare
  construction comparison.
- Coefficient extraction may state only target Borcherds
  multiplicities. It must not assert a Hall morphism, Hall bracket
  comparison, product compatibility, radical quotient, PBW comparison, or
  inverse-system compatibility without the finite recognition datum.
- The sentence that product compatibility follows because both products
  are organized by the same cone must be removed.
- The patch must state that coefficient extraction verifies only the
  multiplicity row of
  `Theorem~\ref{thm:k3e-positive-half-hall-borcherds-criterion}`.

## Commands

```bash
cd /Users/raeez/calabi-yau-quantum-groups

rg -n "\\label\\{(prop:k3e-borcherds-coefficient-recognition-gate|constr:k3e-hcs-hall-borcherds-comparison|thm:k3e-positive-half-hall-borcherds-criterion)\\}" chapters/examples/k3e_cy3_programme.tex chapters/examples/k3e_bkm_chapter.tex

rg -n "ref\\{(prop:k3e-borcherds-coefficient-recognition-gate|constr:k3e-hcs-hall-borcherds-comparison|thm:k3e-positive-half-hall-borcherds-criterion)\\}" chapters standalone appendices -g '*.tex'

rg -n "The Hall--Borcherds map is|coefficient projection supplied|respects charge addition|both products are organised|matches local hCS fields|This identifies the positive Hall generators|Hall--Borcherds comparison of Construction|\\\\ThetaHallBorch\\\\colon" chapters/examples/k3e_cy3_programme.tex

rg -n "finite Hall--Borcherds recognition datum|not a morphism from the compact Hall algebra|does not compare Hall products|Theorem~\\\\ref\\{thm:k3e-positive-half-hall-borcherds-criterion\\}|Q_W|no-extra-relations|PBW associated-graded" chapters/examples/k3e_cy3_programme.tex

pytest -q -p no:cacheprovider compute/tests/test_hall_borcherds_gate.py
make check
make fast
make standalone
```

