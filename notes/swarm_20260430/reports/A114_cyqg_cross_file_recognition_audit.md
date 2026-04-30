# A114 -- CYQG Cross-File Recognition Audit

## Claim Attacked

The Vol III recognition patches might have cleaned local files while
leaving stale target/source collapses elsewhere.

## Findings

The A103/A107-style corrections are locally good in
`chapters/examples/k3e_cy3_programme.tex` and
`chapters/theory/modular_trace.tex`: coefficient extraction is now
target arithmetic only, not a Hall morphism.

Remaining stale claims needing patches:

- `chapters/theory/cy_to_chiral.tex` states
  \(\SpCh_{K3,E}(\PhiFA_3(\cdots)) \simeq
  U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})\) without the finite
  Hall--Borcherds recognition gate.
- `chapters/examples/k3e_cy3_programme.tex` repeats the strong Stage-2
  identification and later says motivic DT invariants are root-space
  dimensions of \(Y^+(\mathfrak g_{\Delta_5})\), with
  \(Y^+=\CoHA(K3\times E)\), without the recognition datum.
- `chapters/theory/gluing/sec_7_lattice_automorphic.tex` converts
  Fourier coefficients into CoHA multiplication / structure constants.
- `chapters/theory/bps_positive_geometry_closure.tex` states a
  Hall--Borcherds quotient isomorphism without radical, bracket, PBW,
  and completion hypotheses.
- `chapters/theory/gluing/sec_10_unifying.tex` maps the quotient to the
  Borcherds positive half from primitive seed / Fourier data alone.

## Verification

```text
git diff --check -- chapters/examples/k3e_cy3_programme.tex chapters/theory/modular_trace.tex
```

passed.

## Files Changed By Agent

None.
