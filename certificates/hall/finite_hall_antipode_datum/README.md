This packet records row 351: the finite Hall antipode datum required
before any finite Hall Hopf-algebra claim is made.

An antipode datum consists of either explicit homogeneous matrices
\[
S_{R,\gamma}:\mathcal H_{R,\gamma}\to\mathcal H_{R,\iota(\gamma)}
\]
for a retained charge involution \(\iota\), or a connected
conilpotent filtration for which the standard recursive antipode
terminates.  In both cases the left and right convolution identities
\[
m_R(S_R\otimes\mathrm{id})\Delta_R=\eta_R\epsilon_R,\qquad
m_R(\mathrm{id}\otimes S_R)\Delta_R=\eta_R\epsilon_R
\]
must be supplied as zero-defect rows, and the antipode must be
compatible with HN transitions.

The present repository state does not supply antipode matrices,
charge-involution rows, connected-conilpotent-recursion rows,
convolution identity rows, or transition-antipode rows.  This packet
therefore verifies the definition and obstruction ledger, not a Hopf
algebra claim.

Run:

```sh
python3 compute/verify_finite_hall_antipode_datum.py \
  --fixture certificates/hall/finite_hall_antipode_datum --check
```

The expected status is
`FINITE_HALL_ANTIPODE_DATUM_OBSTRUCTION_VERIFIED`.
