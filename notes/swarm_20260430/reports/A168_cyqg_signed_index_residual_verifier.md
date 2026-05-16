# A168 -- CYQG Signed-Index Residual Verifier

## Result

Read-only verification found one high-severity residual coefficient-as-count
bug and several medium prose/API traps.

## Findings

- High: `k3_chiral_bialgebra_platonic.tex:3775` still said imaginary
  simple-root multiplicities are \(|c(4nm-\ell^2)|\) and equal to
  \(1/4\)-BPS degeneracies. This reads a signed index as an ordinary
  wall/root count.
- Medium: `k3e_bkm_chapter.tex:1186`, `k3e_bkm_chapter.tex:1343`,
  `k3_yangian_chapter.tex:1370`, and
  `notes/physics_bps_root_multiplicities.tex:320` retained
  `mult = signed coefficient` language that later prose repaired but the
  local sentence still exposed.
- Medium: `notes/physics_bps_root_multiplicities.tex:743` said GV
  primitive invariants count BPS states and are primitive root
  multiplicities; this needs protected/refined-index wording and
  recognition hypotheses for ordinary generator counts.
- Medium: `compute/lib/k3e_coha_structure.py:37` still said
  `dim CoHA = chi(Hilb...)`, and
  `compute/tests/test_k3e_coha_structure.py:547` said \(\chi(K3)=24\)
  means 24 free bosonic generators.
- Low: `compute/lib/k3e_coha_structure.py:217` keeps legacy
  `root_multiplicity()` returning signed \(c(D)\), including negative
  values. The API name remains a trap unless deprecated/fenced.

## Checks

- No files changed by the verifier.
- `git diff --check` over named manuscript/compute/test paths was clean.
- Targeted `rg` sweeps over the named files and tests.
- `pytest compute/tests/test_k3e_coha_structure.py compute/tests/test_elliptic_hall_hocolim.py -q`
  returned `175 passed in 5.84s`.

## Main-Thread Obligation

Patch these anchors so \(c(D)\), \(f(nm,l)\), and GV coefficients are
protected signed/refined indices or superdimensions; ordinary dimensions
and generator counts require a parity fixture or finite Hall--Borcherds
recognition.

