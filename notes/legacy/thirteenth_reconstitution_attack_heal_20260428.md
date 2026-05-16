# Thirteenth reconstitution attack-heal: manuscript proper

Date: 2026-04-28.

Scope: six-agent adversarial attack on the manuscript proper after the
Attack Whitepaper criticism was absorbed.  Main integration owner: current
thread.  Agents supplied evidence only; no truth was accepted by vote.

## Agents and lanes

1. A13-STATUS-STANDALONE: attacked standalone status, process language, and
   proof-strength labels.
2. A13-LATTICE-NORMALORDER: attacked normal-ordering labels, target-window
   support, and source-overcount gaps.
3. A13-ORIENTATION-PFAFFIAN: attacked Borel/orientation classes, Pfaffian
   line comparison, and Maass-character notation.
4. A13-HYBRID-O2-QUOTIENT: attacked the hybrid wrapped atlas and O2 wall
   quotient compatibility.
5. A13-D0-KOSZUL-RECOGNITION: attacked the D0 Pfaffian half, finite Hopf
   source kernel, bar augmentation, and primitive recognition completion.
6. A13-AUTOMORPHIC-SOURCE-CROSS: checked automorphic-source boundary claims;
   no additional fatal manuscript repair survived integration.

## Surviving attacks and repairs

- Status/proof strength: the type-II local-sign theorem is now explicitly
  conditional; K3xE finite-wall technology is stated as supplied datum; the
  scalar-square appendix remark is standalone prose; the eight-row row 1 now
  records computed/imported status rather than "constructed here."
- Orientation: finite stabilizer classes now pass first through Borel
  equivariant classes; Weyl orientation obstruction is first a finite action
  groupoid cocycle; the Maass parity cochain is named
  `\varepsilon_{\Delta}^{\mathrm{aut}}`; rank-one sign fixing no longer
  claims generation of all rank-one components.
- Pfaffian line: the D0 summary now distinguishes formal cusp expansion from
  section-level equality and requires the supplied `\iota_{\mathrm{aut}}`.
- Hybrid/O2: the hybrid tuple now contains the higher colored residual
  `\mathfrak o^{\mathrm{col}}_R`; O2/hybrid residuals now include component,
  boundary, and overlap wall-atlas compatibility.
- Lattice/normal-ordering: the D0 certificate now records a no-overcount
  residual for `(c,T)` labels, compares brackets using
  `\overline\Pi_X(c,T)`, and separates target-window exhaustion from source
  coverage.
- D0/Koszul/recognition: the Pfaffian support/parity test is restricted to
  the cusp-positive half; the two-term Pfaffian block is skew; source
  exponent derivation is an open problem; the finite Hall source kernel now
  includes explicit bialgebra primitive data; source bar construction uses
  an augmentation ideal; primitive recognition now includes exact completion.

## Verification

- `python3 compute/verify_lattice.py` passed.
- `python3 compute/verify_square_root.py` passed.
- `git diff --check -- main.tex` passed.
- `make` passed and rebuilt `out/main.pdf`.

## Remaining open obligations

- Construct the compact Hall source kernels, hybrid wrapped certificates,
  O2 wall atlases, and finite Hall--Dirac atlases.
- Derive the Igusa exponents from source correspondences rather than testing
  supplied source parity data against the imported Borcherds product.
- Prove the full positive/negative primitive-recognition package with exact
  completion, radical quotient, PBW compatibility, and full parity dimensions.
