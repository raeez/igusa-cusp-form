# A090 Vol III patch ranges and text

No files edited by the agent. Line numbers are from the then-current
checkout of `/Users/raeez/calabi-yau-quantum-groups`.

## Ranges

Replace
`chapters/examples/k3e_cy3_programme.tex:177-207` with a proposition
titled
`\texorpdfstring{$K3\times E$}{K3xE} hCS--Hall map, Borcherds coefficient extraction, and finite recognition gate`.
The proposition should preserve label
`constr:k3e-hcs-hall-borcherds-comparison`, state the compact hCS--Hall
map, state separately that the Gritsenko--Nikulin denominator theorem
supplies only the target coefficient function \(m_{\Delta_5}\), and
define a finite Hall--Borcherds comparison on \(W\) as a recognition datum
with neutral compact source bases, provenance, full parity blocks,
\((M,D,B,G,K,Q,A_\beta)\), Borcherds--Kac relation rows, Hopf
radical/coideal descent, kernel equality, PBW associated-graded
comparison, and strict Mittag--Leffler transition data.

Replace `k3e_cy3_programme.tex:1216-1232` so that the BKM row records
target arithmetic and \(G(K3\times E)\) is a conditional comparison
target, not an object produced by coefficient projection.

Replace `k3e_cy3_programme.tex:4201` so the Stage-2 specialization
assumes the finite Hall--Borcherds recognition datum of
`Proposition~\ref{constr:k3e-hcs-hall-borcherds-comparison}` on the
positive BKM windows.

Replace `k3e_cy3_programme.tex:4222-4224` so the positive-half sector is
not obtained by calling the BKM object a Yangian and not obtained by
coefficient projection. The text must keep the hCS--Hall source map and
the Gritsenko--Nikulin target coefficient function separate until the
finite recognition datum is supplied.

## Dependencies

Keep AP-CY423, IC-65, AP-CY424, and IC-66 out of manuscript prose.
Mathematical citations already exist in CYQG:
`GritsenkoNikulin1998`, `Borcherds1998`, `Borcherds1995`,
`Kac1990InfiniteDim`.

## Verification already run read-only

```bash
cd /Users/raeez/calabi-yau-quantum-groups
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider compute/tests/test_hall_borcherds_gate.py

cd /Users/raeez/igusa-cusp-form
PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py
PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py
```

Results: `test_hall_borcherds_gate.py` passed `8 passed`; both Igusa
scripts passed and verify target arithmetic only.

