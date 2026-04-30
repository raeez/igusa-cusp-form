# A079 - Vol III Coefficient-Projection Patch Plan

No files edited by the agent.

## Patch Plan

The overclaim is in
`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`
near line 177. Replace lines 177-207 as one unit. The false lift happens
near lines 190-200 where a coefficient assignment is named a
Hall-Borcherds map, and near line 206 where shared cone support is used
as product compatibility.

Replacement shape:

```tex
\begin{proposition}[Borcherds coefficient extraction and finite Hall--Borcherds recognition gate]
...
The Gritsenko--Nikulin denominator formula supplies only the target
supermultiplicity function
\[
m_{\Delta_5}(\gamma)
=
c_{\phi_{0,1}}\!\left(-\tfrac12(\gamma,\gamma),\ell_\gamma\right).
\]
This is Borcherds target arithmetic for
\(\mathfrak g_{\Delta_5}\). It is not a morphism from the compact Hall
algebra, and it does not compare Hall products, brackets, radicals, PBW
filtrations, or transition maps.

A Hall--Borcherds comparison on a finite downward-saturated window \(W\)
is supplied only after a finite source fixture
\[
(M,D,B,G,K,Q,A_\beta)
\]
is given, together with relation rows, Hopf radical/coideal descent,
kernel equality, PBW associated-graded comparison, and strict
Mittag--Leffler transition data. Under those hypotheses the induced
source quotient identifies with the Gritsenko--Nikulin/Kac target on
\(W\).
\end{proposition}
```

Then replace the proof paragraph near line 206 with: coefficient
extraction proves root supermultiplicity on the target BKM side only;
product compatibility is exactly the missing finite source-recognition
datum.

Dependent prose:

- Near line 4201: change "Hall--Borcherds comparison" to "finite
  Hall--Borcherds recognition datum of Proposition ...".
- Near line 4222: replace "This identifies the positive Hall
  generators..." with "This identifies only the target Borcherds
  multiplicity shadow unless the finite recognition datum is supplied."

## Internal Citations

Do not put AP-CY423 or IC-65 in manuscript prose. Cite them only in the
patch report / notes:

- AP-CY423:
  `/Users/raeez/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md`
  near line 5493.
- IC-65:
  `/Users/raeez/calabi-yau-quantum-groups/appendices/first_principles_cache.md`
  near line 724.
- A074 diagnosis:
  `notes/swarm_20260430/reports/A074_vol3_primitive_recognition_consistency.md`.

Manuscript citations should stay mathematical: Gritsenko-Nikulin /
Borcherds for the denominator coefficients, Kac/PBW for the target
presentation, and the local finite-recognition proposition for the source
comparison.

## Verification

`pytest -q -p no:cacheprovider compute/tests/test_hall_borcherds_gate.py`
passed, `8 passed`. The gate remains open when only denominator /
root-multiplicity data are supplied.

