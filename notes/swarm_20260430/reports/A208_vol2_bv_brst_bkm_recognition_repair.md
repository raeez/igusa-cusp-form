# A208 -- Vol II BV/BRST BKM recognition repair

## Claim attacked

Vol II was at risk of treating \(H_{\Delta_5}\), the BKM algebra, and
the Bruinier divisor coefficients as constructed Vol II objects rather
than conditional target-recognition data.

## Result

No fatal obstruction after repair. The three-loop theorem is recast as
a source BV obstruction followed by a scalar Bruinier map. The all-order
\(c_n\) statement is guarded by the comparison equation
\[
\chi_{\mathrm{Heg}}(c_n^{\mathrm{BV}})
= c_{\phi_{-2,1}}(n)[H_n],
\]
with the comparison hypotheses explicit.

## Files changed

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex`

## Verification

Targeted scans found no surviving direct \(c_n\in H^2\), no unguarded
\(\chi_{\mathrm{BKM}}\), and no hCS source algebra identified with
\(\mathfrak g_{\Delta_5}\).

Commands reported:

```bash
git diff --check -- chapters/connections/bv_brst.tex
```

Status: diff check clean.

## Residual obligation

Vol II may mention \(H_{\Delta_5}\) only as a target recognition object.
The source algebra remains a cyclic dg Lie/\(L_\infty\) object until the
comparison package is constructed.
