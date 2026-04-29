# Agent 51 Dirac Block / Super-Pfaffian Report

Scope: proposal-only review of the latest attack-whitepaper PDF against `main.tex`. No source edits.

Sources read:

- `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf` (latest PDF by filesystem timestamp, Apr 29 19:27).
- `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt` (text extraction of the latest PDF).
- `main.tex`.
- `AGENTS.md`, `CLAUDE.md`, `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`.
- `~/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md`.
- `~/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`.

## Stable core

1. The latest PDF introduces a new finite algebraic construction lane:
   a universal finite Dirac-Igusa Hall source with normal-ordered charge
   grading, finite Hall operations, primitive bracket, orientation-gerbe
   states, hybrid factorization, source coalgebra, Dirac block operator,
   and super-Pfaffian (`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:27848-27879`).
2. The finite Dirac block proposed in the PDF is explicit:
   for each finite primitive degree `gamma`, set
   `V_gamma = g_{Delta_5,gamma}`, `K_gamma = V_gamma \oplus \Pi V_gamma^\vee`,
   `x_gamma=q^n r^l s^m`, and
   `D_gamma = [[0, 1-x_gamma], [1, 0]]`, so
   `D_gamma^2=(1-x_gamma) id`
   (`...revision-1923.txt:29390-29430`).
3. The PDF then defines the finite super-Pfaffian product
   `sPf(D_R)=prod_{gamma in A_R}(1-x_gamma)^{sdim V_gamma}` and normalizes
   it by the Weyl monomial `64 q^{1/2} r^{1/2} s^{1/2}`; using
   `sdim V_(n,l,m)=f(nm,l)` and the Borcherds-Gritsenko-Nikulin product,
   it obtains `Pf=Delta_5` (`...revision-1923.txt:29456-29515`).
4. `main.tex` does not yet contain this `D_gamma` / `sPf` construction.
   It contains the earlier and safer conditional `D_0`/Pfaffian atlas:
   a first-order object and Pfaffian line only after source data are
   supplied (`main.tex:10690-10777`), a finite `K_0`-Pfaffian shadow that is
   not a compact Hall object or first-order operator (`main.tex:10958-11015`),
   and a finite Hall-Dirac atlas/parity-lift obstruction (`main.tex:11380-11580`).
5. `main.tex` is already correct on scalar-square separation:
   OP/DT gives `-4096 Delta_5^{-2}` as a scalar branch; it does not
   construct orientation, Pfaffian line, compact primitives, or Hall
   products (`main.tex:13799-14053`, `main.tex:14209-14231`).

## Valid attacks

### A51-01: "constructed finite compact source object" overstates the PDF construction

Severity: 2.

Target: latest PDF extracted text, `...revision-1923.txt:29620-29677`.

Claim under attack: "This is the constructed finite compact source object" and
`lim Pf_R = Delta_5`.

Broken step: the displayed construction is algebraic and target-seeded. It
uses `V_gamma=g_{Delta_5,gamma}` and the GN multiplicities, then builds a
universal finite model. It is not a compact `K3 x E` Hall source and not a
geometric realization. The PDF itself later states the geometric theorem is
a realization functor into this object (`...revision-1923.txt:29738-29800`).

Main comparison: `main.tex` correctly says the compact source-side objects
and trivializations are not constructed by the lattice calculation,
denominator algebra, or scalar OP square (`main.tex:11744-11757`,
`main.tex:11843-11845`, `main.tex:14233-14244`).

Minimal heal: call the new object "universal finite algebraic source" or
"finite algebraic Dirac-Igusa model", not "compact source object".

### A51-02: `D_gamma` is an algebraic block, not an analytic Dirac operator

Severity: 2.

Target: latest PDF extracted text, `...revision-1923.txt:29390-29430`.

Claim under attack: the block `D_gamma` makes the construction a Dirac
operator.

Broken step: the matrix proves only a finite algebraic first-order square
relation `D_gamma^2=(1-x_gamma) id`. It does not supply a Hilbert
completion, domain, self-adjointness/Fredholm property, heat kernel,
zeta determinant, compact Hall geometry, or source-side BPS operator product.

Main comparison: `main.tex` already says "first-order" means the
Pfaffian/primitive object before scalar squaring and does not assert an
analytic Dirac operator on a constructed Hilbert space (`main.tex:10716-10720`).

Minimal heal: state the block as an algebraic Dirac block in finite windows.

### A51-03: "super-Pfaffian" is safe only as a defined convention through a Pfaffian line/gerbe

Severity: 2.

Target: latest PDF extracted text, `...revision-1923.txt:29456-29498`,
`...revision-1923.txt:30018-30023`.

Claim under attack: the product is a Pfaffian without extra structure.

Broken step: the unconditional formal identity is a superdeterminant /
Berezinian-type product depending on signed superdimension. It becomes a
Pfaffian only after a Pfaffian line, square map, orientation-gerbe convention,
and sign/trivialization are part of the finite data. The latest PDF does
name the orientation-gerbe construction (`...revision-1923.txt:28956-29014`);
that must remain attached to every use of "super-Pfaffian".

Main comparison: `main.tex` says the finite formal section from the target
shadow has no orientation line and no skew-adjoint finite operator
(`main.tex:11032-11041`), while the actual Pfaffian line is conditional
data (`main.tex:10722-10777`, `main.tex:11466-11475`).

Minimal heal: define `sPf` explicitly as a finite-window orientation-gerbe
super-Pfaffian convention. Do not use it as an ordinary Pfaffian of a
canonical geometric operator.

### A51-04: minimal parity lift is a source axiom, not a consequence

Severity: 2.

Target: latest PDF extracted text, `...revision-1923.txt:29802-29841`.

Claim under attack: the minimal parity lift is forced by the determinant.

Broken step: the determinant fixes only `sdim V_gamma`. The choice
`(dim V_0, dim V_1)=(f,0)` for `f>=0` and `(0,-f)` for `f<0` imposes
no-hidden-cancellation in the universal source. It is a convention/axiom,
not a theorem from `Delta_5`.

Main comparison: `main.tex` explicitly proves that compact parity lifts
form the affine monoid `{(u,v) in Z_{\ge0}^2 | u-v=a_Delta(gamma)}` and
that the minimal lift is extra source data, not implied by `Delta_5`, the
denominator algebra, the OP scalar square, or equality in `K_0`
(`main.tex:11550-11580`).

Minimal heal: if the universal algebraic source uses the minimal lift, say
"we choose the minimal no-hidden-cancellation lift in the universal model."

### A51-05: scalar-square language must stay quarantined

Severity: 1.

Target: latest PDF extracted text, `...revision-1923.txt:30028-30036`;
`main.tex:13799-14053`.

Claim under attack: the OP scalar square constructs the square-root object
or fixes the Pfaffian sign.

Broken step: OP supplies the scalar branch
`Z^X_OP = -4096 Delta_5^{-2}`. Squaring kills the sign character. The
constant `64`, the constant `4096`, and the OP minus sign are
normalizations, not Hall orientation data.

Main comparison: `main.tex` is already strong here. It says the OP scalar
sign is not an orientation character (`main.tex:14221-14222`) and that the
orientation-monodromy problem requires determinant-line signs on type-II
walls (`main.tex:14268-14279`).

Minimal heal: preserve the quarantine exactly.

## Safe construction wording

Use this wording if the `D_gamma` construction is migrated into `main.tex`:

```tex
\begin{definition}[Finite algebraic Dirac block]
Fix a finite cusp-positive window \(A_R\).  For each
\(\gamma=(n,l,m)\in A_R\), choose a finite super vector space
\(V_\gamma\) with
\[
\sdim V_\gamma=f(nm,l),
\qquad x^\gamma=q^nr^ls^m.
\]
Set
\[
K_\gamma:=V_\gamma\oplus \Pi V_\gamma^\vee .
\]
On \(K_\gamma\) define the odd algebraic block
\[
D_\gamma=
\begin{pmatrix}
0&1-x^\gamma\\
1&0
\end{pmatrix}.
\]
Then
\[
D_\gamma^2=(1-x^\gamma)\operatorname{id}_{K_\gamma}.
\]
After choosing the finite orientation-gerbe/Pfaffian convention on
\(\bigoplus_{\gamma\in A_R}K_\gamma\), define the finite algebraic
super-Pfaffian section by
\[
\operatorname{sPf}_R(D)
:=\prod_{\gamma\in A_R}(1-x^\gamma)^{\sdim V_\gamma}.
\]
With the theta-normalized Weyl monomial,
\[
\operatorname{Pf}_R
=64q^{1/2}r^{1/2}s^{1/2}\operatorname{sPf}_R(D).
\]
This is a finite-window algebraic model of the Pfaffian product.  It is
not a compact \(K3\times E\) Hall object and not an analytic Dirac
operator.  A compact geometric theorem requires a realization functor
from the \(K3\times E\) Hall source into this algebraic finite source,
preserving degrees, Hall operations, orientation-gerbe data, Dirac
blocks, Pfaffian lines, and the cusp trivialization.
\end{definition}
```

Safe theorem wording:

```tex
The finite algebraic source constructed from the Gritsenko--Nikulin
denominator algebra has a normalized super-Pfaffian product equal to
\(\Delta_5\).  This is an algebraic source model, seeded by the known
denominator algebra and the chosen finite parity lift.  It does not
construct the compact \(K3\times E\) Hall source.  The compact theorem is
the separate realization problem: construct finite geometric realization
functors into this algebraic source, compatible in \(R\).
```

Safe scalar-square wording:

```tex
The Oberdieck--Pixton/Oberdieck branch proves the scalar identity
\[
Z^X_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}.
\]
This checks the orientation-forgetting square of a supplied first-order
Pfaffian object.  It does not construct the Pfaffian line, the
orientation character, the primitive Hall bracket, or the compact
source.  The constants \(64\), \(4096\), and the OP minus sign are
normalization data, not Hall orientation signs.
```

## Forbidden overclaims

Do not write:

1. "The compact `K3 x E` Dirac-Igusa source is constructed" unless the
   geometric Hall source, quotient orientation, hybrid wrapped
   factorization, Pfaffian line, and transition diagrams are actually
   built.
2. "`D_gamma` is the compact Dirac operator" or "the analytic Dirac
   operator"; safe phrase: "finite algebraic Dirac block".
3. "The super-Pfaffian follows from the determinant"; safe phrase:
   "after the finite orientation-gerbe/Pfaffian convention is supplied,
   the finite super-Pfaffian product is defined by ...".
4. "The determinant determines parity"; safe phrase: "the determinant
   determines only signed superdimension; the minimal lift is a chosen
   no-hidden-cancellation axiom of the universal model."
5. "OP/DT constructs the square root"; safe phrase: "OP/DT supplies the
   scalar square, which forgets the orientation character."
6. "`64`, `4096`, or the OP minus sign fixes the Pfaffian orientation";
   safe phrase: "these are normalization constants; orientation must come
   from determinant-line/Pfaffian monodromy."
7. "The denominator algebra reconstructs the compact Hall bracket"; safe
   phrase: "the denominator algebra supplies the target bracket; a compact
   source bracket requires a realization certificate."

## Residual obligations

1. If the new `D_gamma` block is adopted, `main.tex` needs a new section
   separating three objects:
   virtual `K_0` determinant, universal finite algebraic source, compact
   `K3 x E` realization functor.
2. The notation must not collide with the existing conditional
   `\mathfrak D_{X,R}`. Use `D_{\gamma}^{alg}` or a similarly explicit
   finite algebraic symbol unless the whole `D_0` section is refactored.
3. The phrase "super-Pfaffian" must be defined before theorem use and
   tied to the orientation gerbe/Pfaffian line convention. Otherwise use
   `\sdet` / Berezinian language.
4. The minimal parity lift must be marked as a universal-model axiom.
   Compact parity remains a geometric realization condition.
5. The scalar square section in `main.tex` should remain after the
   determinant/denominator material and should keep the current quarantine
   language.

## Verification still needed

No TeX build was run. This was a proposal-only review. Before migrating
the construction into `main.tex`, run a targeted grep for every occurrence
of "constructed finite compact source", "super-Pfaffian", "Dirac block",
"minimal parity lift", and "scalar square", then compile once after the
text is edited.
