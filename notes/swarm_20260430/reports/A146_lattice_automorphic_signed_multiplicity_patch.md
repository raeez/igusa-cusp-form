# A146 -- Lattice-Automorphic Signed-Multiplicity Patch

## Claim Attacked

`chapters/theory/gluing/sec_7_lattice_automorphic.tex` said \(C_1(D)\)
gives positive-root multiplicities and wrote
\(\operatorname{mult}(\alpha)=C_1(\cdots)\) despite examples such as
\(C_1(3)=-64\).

## Patch

The text now explicitly rules out the unsigned multiplicity reading.
The target statement is
\[
\operatorname{sdim}\mathfrak g_{\Delta_5,\alpha}=C_1(\cdots).
\]
Parity and ordinary-dimension claims are gated by a target presentation
fixture; compact source interpretations require finite Hall--Borcherds
recognition.

## Verification

```text
git diff --check -- chapters/theory/gluing/sec_7_lattice_automorphic.tex
```

passed. Targeted search found no remaining exact hits for
`positive-root multiplicities` or `mult(\alpha)`.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/gluing/sec_7_lattice_automorphic.tex`
