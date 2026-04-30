# A004 report: hybrid local/wrapped and compactified correspondences

Runtime id: `019ddbc4-fe65-7c71-90ca-8aabf7964a93`.
Nickname: Plato.
Status: completed.
Files changed by agent: none.

## Attacks

### Projection locality

Status: invalid attack.

The refreshed text correctly distinguishes locality on \(X=K3\times E\)
from support-locality after projection to \(E\). The obstruction is
\(p_E(C)=E\) for positive elliptic degree, not nonlocality on \(X\).

Anchors:
`main.tex:7357`, `main.tex:7400`, `main.tex:7421`;
CYQG `AP-CY367`.

### Quotient order

Status: invalid attack against current `main.tex`.

The manuscript requires local, mixed, wrapped, and flag
correspondences before the reduced \(E\)-quotient, with \(Q_{E,R}\) a
functor on the finite correspondence/BM category, not a quotient of
object stacks.

Anchors:
`main.tex:7893`, `main.tex:8377`, `main.tex:13691`.

### Compactified retained Hall correspondences

Status: partially valid.

The plan names the right object: closed-filtration / flag-Quot
compactifications with \(q\) proper or exceptional compact-support
admissible, d-critical data, vanishing cycles, and orientation
coefficients. But `main.tex` has not fully replaced retained full
numerical class by the stronger retained Liu-Hilbert class
\(\Xi=(\gamma,[a,b],(P_i),N)\).

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43620`,
`main.tex:13002`, `main.tex:13235`, CYQG `AP-CY375`.

### Eight binary words versus full factorization

Status: valid.

`main.tex` says the eight words give only binary associativity and keeps
higher colored configurations, units, symmetry/order, refinement maps,
descent, and overlaps as \(\mathfrak o^{\mathrm{col}}_R\), not as
constructed colored tree/flag-stack data. The critique sketches finite
colored trees \(T\), but construction-level data are still missing in
`main.tex`.

Anchors:
`main.tex:7832`, `main.tex:7887`, `main.tex:8118`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44547`,
CYQG `AP-CY376`.

## Finite Construction Obligations

1. Define retained classes \(\Xi\), finite schedules \(X_R\), and
   closure under subobjects, quotients, extensions, duals,
   local/wrapped anchors, and tree refinements.
2. Define \(\mathfrak E^{ret}_{\Xi_A,\Xi_B;\Xi_C}\) as a closed derived
   flag-Quot/filtration stack over \(\mathfrak M^{ss}_{\Xi_C}\), with
   input map \(p\), output map \(q\), and \(q\) proper/projective in the
   compactified model.
3. Define a colored tree category \(\mathrm{Tree}^{col}_R\), not only
   words in \(\{L,W\}^3\).
4. For every colored tree \(T\), define
   \(\mathfrak F^{T,\mathrm{hyb}}_{\Xi_\bullet;\Xi_T}\), source/root
   maps, contraction/refinement maps, unit/vacuum maps, symmetry or
   ordered conventions, overlap descent, and common-refinement
   comparison maps.
5. Put d-critical structures, BBDJS vanishing cycles, orientation
   gerbes, Thom-Sebastiani maps, quotient \(Q_{E,R}\), and protected
   integration on these tree stacks, compatibly in \(R\).

## Manuscript Recommendation

Keep the projection-to-\(E\) locality lemma and the
\(b_R^{geom}\) versus \(m_R=\operatorname{pr}_3\overline\Pi_X\) split.
Insert retained Liu-Hilbert finite-stage definitions before the Hall
source theorem. Replace the eight-word paragraph by a colored-tree /
flag-stack definition; demote the eight words to the arity-three shadow.
Keep the full compact theorem conditional until colored-tree coherences,
quotient descent, orientation gerbes, and source matrices are
constructed.

Commands run by agent: read-only `sed`, `nl -ba | sed`, and `rg`.
