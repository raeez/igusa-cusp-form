# wrel_degree_closure

This fixture certifies the finite target degree set
\[
W_{\mathrm{rel}}^+
=W_{\le3}^{act}\cup R_4\cup I_4\cup C_{\le7}\cup\{2\delta_{123}\}.
\]

It contains 35 rows: 13 rows from \(W_{\le3}\), six real-Serre
terminal rows \(3\delta_i+\delta_j\), three doubled isotropic rows
\(2a_{ij}\), twelve complementary-string rows \(C_{k,s}\) with
\(2\le s\le5\), and \(2\delta_{123}\).  The verifier recomputes the
coordinates, norms, heights, signed Jacobi coefficients, and the
terminal Kac exponents.

The `downward_saturation.csv` table is an audit, not a positive
saturation certificate.  It recomputes every proper componentwise
subdegree below the 35 rows.  The only nonzero subdegree defects are
\[
D_1=\delta_1+2a_{23},\qquad
D_2=\delta_2+2a_{13},\qquad
D_3=\delta_3+2a_{12},
\]
all below \(2\delta_{123}\), with signed multiplicity \(-513\).  Thus
\(W_{\mathrm{rel}}^+\) is relation-closed for the recorded terminal
checks, but it is not a downward-saturated primitive-recognition
window.

The `saturation_extension.csv` table records the minimal nonzero
extension.  It verifies that adjoining \(D_1,D_2,D_3\) gives a
38-row target window with no remaining nonzero proper-subdegree
defect.  These three rows are present in the A071 target-presentation
fixture as signed-only rows: \(m(D_k)=54\), but no full parity split,
pairing block, radical block, or PBW row is supplied.

The `post_saturation_real_string_obligations.csv` table audits the
real-root strings forced after the \(D_k\) rows are adjoined.  The
38-row saturated extension is not a full relation-closed target window:
the A071 simple-generator rows force 21 terminal codomains outside
\(W_{\mathrm{sat}}^+\), and 10 of those terminal codomains have
nonzero signed multiplicity.  These are relation-presentation
obligations, not compact-source rows.

The `post_saturation_terminal_layer.csv` table groups those 21
obligations into 21 distinct terminal degrees.  If adjoined, this layer
is not downward saturated: it creates 114 nonzero subdegree-defect
incidences, with 26 distinct missing subdegrees.  This is evidence of a
closure cascade, not a finite source theorem.

The `terminal_layer_saturation_extension.csv` table records those 26
distinct missing subdegrees.  Adjoining them to
\[
W_{\mathrm{rel}}^+\cup\{D_1,D_2,D_3\}
\]
and to the 21 post-saturation terminal degrees gives an 85-row target
degree set with zero remaining nonzero proper-subdegree defects.  This
closes the downward-saturation audit for the displayed terminal layer;
it does not close the real-string relation audit or supply compact
source rows.

The `terminal_layer_saturation_real_string_obligations.csv` table is a
conditional real-string audit for those 26 saturation-extension rows.
If they are promoted to target-generator rows, the real roots force 55
terminal checks.  Of these terminal codomains, 54 lie outside the
85-row target degree set, and 12 of the missing codomains have nonzero
signed multiplicity.  Thus the 85-row set is downward saturated but not
relation-closed.

The `terminal_layer_saturation_real_string_defect_summary.csv` table
audits the next downward-saturation defect if those 55 terminal
codomains are adjoined as a layer.  The layer has 55 distinct terminal
degrees, one already in the 85-row set and 54 new degrees.  Adjoining
it creates 546 nonzero proper-subdegree defect incidences across 98
distinct subdegrees.

The `terminal_layer_saturation_real_string_defect_layer.csv` table
records those 98 subdegrees.  Adjoining the 98-row defect layer to the
85-row set and to the 55 real-string terminal codomains gives a 237-row
target degree set with zero remaining nonzero proper-subdegree defects.
This closes downward saturation for that layer only; relation closure
still requires the next real-string audit.

The
`terminal_layer_saturation_real_string_defect_layer_real_string_summary.csv`
table records that next audit.  The associated obligations table
records the exact 206 real-string checks.  Their terminal-layer table
has 206 distinct terminal codomains; 24 already lie in the 237-row set
and 182 are new.  Among the new terminal codomains, 24 have nonzero
signed multiplicity.  The associated saturation-extension table records
the 50 distinct nonzero proper subdegrees created by adjoining that
terminal layer, with 624 incidences.  Adjoining the 206 terminal degrees
and those 50 subdegrees to the 237-row set gives a 469-row target degree
set with zero remaining nonzero proper-subdegree defects for that layer.
The real-string audit for the newly adjoined 50-row layer is also
recorded exactly.  It has 96 terminal checks, 96 distinct terminal
codomains, six already in the 469-row set, 90 new terminal degrees, and
no missing nonzero terminal degree.  Adjoining the 96 terminal degrees
creates 44 nonzero proper-subdegree defect incidences across 12
distinct subdegrees.  The associated 12-row saturation extension gives a
571-row target degree set with zero remaining nonzero proper-subdegree
defects for that layer.  The real-string audit for this 12-row layer has
20 terminal checks, 20 new terminal degrees, and no nonzero terminal
degree.  Adjoining the 20 terminal degrees creates 8 nonzero
proper-subdegree defect incidences across 6 distinct subdegrees.  The
associated 6-row saturation extension gives a 597-row target degree set
with zero remaining nonzero proper-subdegree defects for that layer.
The real-string audit for this 6-row layer has 10 terminal checks, 10
new terminal degrees, and no nonzero terminal degree.  Adjoining the 10
terminal degrees creates 18 nonzero proper-subdegree defect incidences
across 6 distinct subdegrees.  The associated 6-row saturation
extension gives a 613-row target degree set with zero remaining
nonzero proper-subdegree defects for that layer.  The real-string audit
for the next 6-row layer has 10 terminal checks, 10 new terminal
degrees, and no nonzero terminal degree.  Adjoining the 10 terminal
degrees creates 8 nonzero proper-subdegree defect incidences across 6
distinct subdegrees.  The associated 6-row saturation extension gives a
629-row target degree set with zero remaining nonzero proper-subdegree
defects for that layer.  The real-string audit for the next 6-row layer
has 10 terminal checks, 10 new terminal degrees, and no nonzero terminal
degree.  Adjoining the 10 terminal degrees creates 18 nonzero
proper-subdegree defect incidences across 6 distinct subdegrees.  The
associated 6-row saturation extension gives a 645-row target degree set
with zero remaining nonzero proper-subdegree defects for that layer.
The separate `wrel_tail_staircase` packet proves the symbolic tail
`A_N -> B_N -> A_{N+2}` for every even `N >= 14`.  Thus the finite
row-adjoining target-degree audit has an infinite six-row staircase
after the `A_14` layer.  Its `unbounded_tail.csv` table records a
strictly increasing coordinate subsequence, so no finite prefix of this
target-only audit is a relation-closed compact-source theorem.

This is a target degree-closure certificate only.  It is not a compact
source theorem and does not prove primitive recognition.

Run:

```sh
python3 compute/verify_wrel_degree_closure_fixture.py \
  --fixture certificates/targets/delta5_gn_kac/wrel_degree_closure \
  --check
```

A positive result is `WREL_DEGREE_CLOSURE_VERIFIED`.
