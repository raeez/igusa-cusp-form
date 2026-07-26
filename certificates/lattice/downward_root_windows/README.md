# Downward Root-Window Certificate

This packet records the target-side root-window convention used in the
finite primitive-recognition clauses.

For the positive root set R_+ in the delta-basis, it defines

```text
W_nu = { beta in R_+ : ht(beta) <= nu }.
```

For beta = b1 delta_1 + b2 delta_2 + b3 delta_3, the source degree
preimage is

```text
gamma_beta = (b1, b1 + b2 - b3, b2),
```

so alpha(gamma_beta) = beta for
alpha(n,l,m)=n delta_1 + m delta_2 + (n+m-l) delta_3.  The sector rule
places gamma_beta in the product chamber:

```text
b2>0               -> m_positive
b2=0 and b1>0     -> n_positive_boundary
b1=b2=0 and b3>0  -> negative_l_boundary
```

The finite audit checks the ambient positive-cone windows for
1 <= nu <= 7.  The proof for R_+ is formal: if beta' <= beta and both
are positive roots, then ht(beta') <= ht(beta), so beta in W_nu implies
beta' in W_nu.

This is not a compact-source packet.  It does not construct source
representatives, relation matrices, Hall pairings, PBW rows, Pfaffian
orientations, or protected traces.

Run:

```sh
python3 compute/verify_downward_root_windows_fixture.py \
  --fixture certificates/lattice/downward_root_windows --check
```

Expected status:

```text
DOWNWARD_ROOT_WINDOWS_VERIFIED
```
