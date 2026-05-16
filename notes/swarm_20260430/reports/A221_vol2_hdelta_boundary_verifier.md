# A221 -- Vol II `H_{\Delta_5}` boundary verifier

## Claim attacked

Vol II `w-algebras-conditional.tex` still read as if
\(\mathbf H_{\Delta_5}\) were constructed by Vol II.

## Finding

High:

- `chapters/examples/w-algebras-conditional.tex:1680-1695` said that
  \(\mathbf H_{\Delta_5}\) admits a chiral-algebra presentation and that
  the decoupled limit is the standalone chiral bialgebra, without the
  Vol III/source-recognition guard.

Clean:

- `bv_brst.tex` uses \(\delta_{\Delta_5}\) as a supplied lattice label and
  says \(\Delta_5\) is a scalar automorphic image, not a lattice vector.
- Direct \(H^2(\mathfrak g_{\Delta_5})\) language occurs only in explicit
  denial/comparison text.

## Integration

The main thread rewrote the decoupling remark as a target criterion:
\(\mathbf H_{\Delta_5}\) must satisfy it after Vol III/source recognition;
Vol II does not construct the object.

## Verification

A226 verified the repair with no remaining fatal/high/medium findings in
the patched `w-algebras-conditional.tex` band.
