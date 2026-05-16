# A159 -- BKM CE Signed-Dimension Patch

## Claim Attacked

`chapters/examples/k3e_bkm_chapter.tex` used
\(\dim \mathfrak g_{v_i+v_j}=c(D(v_i+v_j))\) inside a CE differential
proof, and had local table drift with \(|c(D)|\) as multiplicity.

## Patch

The OPE table now records \(\operatorname{sdim}\) and \(c(D)\), with a
parity-fixture guardrail. The Serre table tail now has \(c(D)\) in the
\(c(D)\) column. The `182` generator statement explicitly depends on the
target parity fixture. The CE proof now uses
\[
\operatorname{sdim}\mathfrak g_{v_i+v_j}=c(D(v_i+v_j)),
\]
and states that ordinary dimensions/source counts require a parity
fixture or finite Hall--Borcherds recognition.

## Verification

```text
git diff --check -- chapters/examples/k3e_bkm_chapter.tex
```

passed. Targeted search found no exact bad local forms for
`\dim ... = c`, table `|c(D)|`, or `\mult` table drift.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex`
