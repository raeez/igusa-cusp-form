# A119 -- BPS Positive-Geometry Criterion Patch

## Claim Attacked

`chapters/theory/bps_positive_geometry_closure.tex` stated a
Hall--Borcherds quotient isomorphism too unconditionally.

## Patch

The theorem is now an Igusa boundary recognition criterion. The finite
datum \(R_W\) explicitly includes compact provenance, parity blocks,
\(M,D,B,G,K,Q,A\), ideal/coideal descent, kernel/no-extra-relations,
PBW, and Mittag--Leffler data. The quotient comparison is conditional on
a cofinal compatible tower.

The finite obstruction morphism now uses Hall--Borcherds recognition
rather than automorphic-radical shorthand. The raw \(K3\times E\) row
requires \(o_{\mathrm{HB}}=0\) and \(K=0\), and the residual vector is
renamed to \(o_{\mathrm{HB}}\) with the requested coordinates.

## Verification

```text
git diff --check -- chapters/theory/bps_positive_geometry_closure.tex
```

passed. Targeted search found no remaining stale
`\operatorname{Rad}`, `o_{\mathrm{rad}}`, `V_{\mathrm{rad}}`,
`automorphic-radical`, or "radical vector" language. Remaining
`isomorphism` hits are conditional finite/PBW language or unrelated hCS
quasi-isomorphism language.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/bps_positive_geometry_closure.tex`
