# finite_hall_bracket_parity

This packet records correction row 357.

It proves the relative parity statement for supplied homogeneous Hall
bracket rows: in a Z/2-graded algebra with even multiplication, the
supercommutator of parity `p` and parity `q` has parity `p + q`.

The packet imports formal bracket rows whose target parity equals the
input parity sum, and it imports the finite parity-pushforward packet
as super-vector-space bookkeeping.  Those imports are not compact
`K3xE` source parity rows.  The current compact source still has no
parity blocks, product rows, primitive bracket rows, or row-357
parity-defect rows.

Run:

```sh
python3 compute/verify_finite_hall_bracket_parity.py \
  --fixture certificates/hall/finite_hall_bracket_parity --check
```

Expected status:

```text
FINITE_HALL_BRACKET_PARITY_OBSTRUCTION_VERIFIED
```
