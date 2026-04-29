# Agent54 Intro/Status Latest Report

Scope: proposal-only theorem-status and introduction merger.  No source files edited.  Writable surface limited to this report.

Sources read:
- `AGENTS.md`, `CLAUDE.md`, `~/ecosystem/INVARIANTS.md`, `~/ecosystem/AGENTS-HARNESS.md`.
- Attack-heal skill and protocol: `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/SKILL.md` and `references/protocol.md`.
- `main.tex`, especially abstract and front status tables at `main.tex:57-172`, `main.tex:177-457`.
- 19:23 extracted PDF: `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`, especially lines `27848-27892`, `29390-29800`.
- Reports 42-49 where present: `agent42_latest_revision_delta_report.md` through `agent49_geometric_realization_functor_report.md`.

## Verdict

Stable core: nonempty.

The platonic paper should open with four status layers, in this order:

1. **proved/computed/imported**: protected K3 index, virtual \(K_0\)-determinant, Borcherds--Gritsenko--Nikulin product, and Gritsenko--Nikulin denominator target;
2. **constructed/proved in the manuscript**: the formal dyonic Mukai lattice, polarization defect \(B\), normal-ordered extension \(\widehat\Gamma_X\), normal-ordered Gram homomorphism \(\overline\Pi_X\), and strict fixed-lift raw Gram descent obstruction;
3. **optional algebraic model, only if defined**: a universal algebraic Dirac--Igusa target envelope \(\mathsf{UDI}^{alg}_{\Delta_5,E,L}\), fenced as target-derived finite algebra, not compact geometry;
4. **conditional/open geometry**: compact \(K3\times E\) geometry as a finite-stage realization problem
\[
\mathsf{Real}_{X,R}:\mathfrak H^{geom}_{X,R}\longrightarrow
\mathsf{UDI}^{alg}_{\Delta_5,E,L,R},
\]
only after the geometric source domain and algebraic envelope have both been defined.

The 19:23 PDF tries to replace "assume compact source" by "construct universal finite Dirac--Igusa Hall source" (`revision-1923.txt:27848-27862`, `29517-29732`).  Agent48 and Agent49 correctly block the phrase "compact source" because the proposed \(UDI_R\) is built from \(\mathfrak g_{\Delta_5}\), \(U(\mathfrak g_{\Delta_5})\), the BKM bracket, and GN multiplicities (`revision-1923.txt:29390-29724`).  Therefore front matter may mention \(UDI\) only as \(\mathsf{UDI}^{alg}\), only after the paper gives a real definition, and only with an explicit source/target firewall.

## Exact Abstract Replacement

Replace the abstract from `main.tex:57-172` by the following if the manuscript does **not** yet define \(\mathsf{UDI}^{alg}\):

```tex
\begin{abstract}
For \(X=K3\times E\) the theorem-level physical input used here is the
protected index.  Right-moving localization in the K3 Ramond sector gives
\[
Z_{\mathrm{K3}}=2\phi_{0,1},\qquad
\phi_{0,1}=\sum f(n,l)q^nr^l.
\]
Replacing the protected K3 index by its Borcherds half produces a virtual
\(K_0\)-determinant package.  It does not produce a microscopic Hilbert
space, compact Hall correspondences, or an operator product.  For virtual
super vector spaces \(\mathbb U_{n,l}\) with
\(\sdim\mathbb U_{n,l}=f(n,l)\), set
\(\mathcal V_{(n,l,m)}=\mathbb U_{nm,l}\).  In the Borcherds cusp chamber
\[
\mathcal D_X(Z)
=64q^{1/2}r^{1/2}s^{1/2}
\prod_{(n,l,m)\in\Gamma_{\mathrm{eff}}}
(1-q^nr^ls^m)^{f(nm,l)}
=\Delta_5(Z).
\]
The constant \(64\) is the theta-constant normalization
\([q^{1/2}r^{1/2}s^{1/2}]\Delta_5=64\); the monic Borcherds product is
\(D_5=64^{-1}\Delta_5\).

The same coefficients are the signed root supermultiplicities in the
Gritsenko--Nikulin Borcherds--Kac--Moody denominator algebra.  Under
\[
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}
\]
one has
\[
\operatorname{den}(\mathfrak g_{\Delta_5})
=64^{-1}\Delta_5(2Z),\qquad
\smult\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
\]
on the active support.  Thus the denominator algebra supplies the imported
algebraic target and its target-internal Borcherds bracket.  It does not
supply a compact BPS Hilbert space, compact Hall correspondences, an
orientation, or a BPS local-collision map.

The first construction in the paper is the normal-ordered charge lattice.
For the formal dyonic Mukai lattice
\(\Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S\), the raw Gram map
\[
\Pi_X(Q,P)=\left(Q^2/2,Q\cdot P,P^2/2\right)
\]
is quadratic:
\[
\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c').
\]
Consequently strict fixed-lift raw Gram descent cannot carry the type-II
real-root bracket strings.  The normal-ordered extension
\[
\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T
\]
is the additive replacement.  The paper proves this lattice theorem and
the fixed-lift raw-descent obstruction.

The reduced scalar branch is imported from Oberdieck--Pixton,
Oberdieck--Pandharipande, and Oberdieck:
\[
Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}
=-\left(\chi_{10}^{\mathrm{OP}}\right)^{-1}
=-4096\,\Delta_5^{-2}.
\]
Here \(\chi_{10}^{\mathrm{OP}}=(64^{-1}\Delta_5)^2\).  The factor
\(4096=64^2\) is a normalization conversion and the minus sign is the OP
scalar convention.  Neither fixes the automorphic reflection character,
the compact orientation monodromy, a Pfaffian line, or primitive
recognition.

The compact \(K3\times E\) theorem is therefore not a theorem of this
paper.  It is a realization problem.  One must construct finite compact
Hall--Dirac source data, with finite stacks, normal-ordered degrees,
orientation gerbes, hybrid local/wrapped correspondences, source
coalgebras, first-order Dirac blocks, Pfaffian lines, primitive
representatives, radical/PBW data, and compatible transitions.  Only after
such data exist can one ask for a realization into the algebraic
Gritsenko--Nikulin target and for a geometric Pfaffian equal to
\(\Delta_5\).  The final part records the eight Cl\'ery--Gritsenko
diagonal-divisor rows and the certificate required before any boundary row
becomes a physical host.
\end{abstract}
```

If a new section actually defines \(\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}\), replace the fourth paragraph above by:

```tex
If the finite algebraic envelope
\(\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}\) is defined from finite
normal-ordered windows of the imported Gritsenko--Nikulin/Kac denominator
algebra, its PBW/radical data, a formal hybrid color table, a source-named
but target-derived chiral coalgebra, and formal first-order Dirac blocks,
then its normalized formal Pfaffian is \(\Delta_5\).  This is a
finite-window restatement of the Borcherds--Gritsenko--Nikulin product in
an algebraic target envelope.  It is not a compact \(K3\times E\) source
and carries no geometric quotient-orientation content until source
provenance and a realization functor are supplied.
```

and replace the fifth paragraph by:

```tex
The compact \(K3\times E\) theorem is then a conditional realization
problem.  At finite height \(R\) the geometric domain, if constructed, is
a compact Hall--Dirac source datum \(\mathfrak H^{geom}_{X,R}\).  A
realization is a functor
\[
\mathsf{Real}_{X,R}:\mathfrak H^{geom}_{X,R}
\longrightarrow\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}
\]
preserving normal-ordered degrees, Hall product and coproduct
correspondences, orientation-gerbe twists, hybrid local/wrapped operations,
source coalgebras, first-order Dirac blocks, Pfaffian lines with leading
cusp trivialization, primitive representatives, radical/PBW data, and
finite-window transitions.  If a compatible pro-realization exists, the
geometric Pfaffian is pulled back from the algebraic identity.  Existence
of \(\mathsf{Real}_X\) is open.
```

## Exact Introduction Dependency Chain

Replace the display at `main.tex:194-209` by:

```tex
Thus the exposition follows the dependency chain
\[
\begin{array}{rcl}
\hbox{protected K3 index} & \rightsquigarrow_{\mathrm{computes}} &
\hbox{virtual }K_0\hbox{-determinant},\\
\hbox{Borcherds--Gritsenko--Nikulin} & \rightsquigarrow_{\mathrm{imports}} &
\hbox{Igusa product and denominator target},\\
\hbox{formal Mukai charge and }B & \rightsquigarrow_{\mathrm{proves}} &
\hbox{normal-ordered Gram map and raw-descent obstruction},\\
\hbox{algebraic finite envelope, if defined} &
\rightsquigarrow_{\mathrm{target\ model}} &
\hbox{formal Pfaffian normalization},\\
\hbox{compact }K3\times E\hbox{ Hall data} &
\rightsquigarrow_{\mathrm{conditional}} &
\hbox{realization functor } \mathsf{Real}_{X,R},\\
\hbox{Oberdieck--Pixton/Oberdieck} & \rightsquigarrow_{\mathrm{checks}} &
\hbox{orientation-forgetful scalar square},\\
\hbox{Cl\'ery--Gritsenko rows} & \rightsquigarrow_{\mathrm{certificate}} &
\hbox{boundary host tests}.
\end{array}
\]
```

Then replace `main.tex:211-213` by:

```tex
The scalar OP/DT equality is a check on the square of a supplied or
realized first-order Pfaffian object.  It is not an input to the compact
Hall source, the Pfaffian line, the orientation character, or primitive
recognition.
```

If \(\mathsf{UDI}^{alg}\) is not defined in the paper, do not use the
phrase "universal finite Hall--Dirac source" in the introduction.  Use
"algebraic finite envelope, if defined" until the definition exists.

## Exact First Status Table Replacement

Replace the table at `main.tex:361-392` by:

```tex
\begin{center}
\small
\begin{tabular}{p{0.22\textwidth}p{0.22\textwidth}p{0.46\textwidth}}
\hline
Structural level & Claim strength & Content \\
\hline
Virtual determinant &
computed/imported &
\(\mathcal D_X=\Delta_5\) from the \(K_0\)-half-index and the
Borcherds--Gritsenko--Nikulin product.  No canonical half-Hilbert space,
operator product, compact Hall correspondence, or Pfaffian line is
constructed. \\
Gritsenko--Nikulin target &
imported theorem &
\(\mathfrak g_{\Delta_5}\), its signed root supermultiplicities, and
\(\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)\).  This
is target algebra, not compact geometry. \\
Normal-ordered lattice &
proved in this paper &
The formal dyonic Mukai lattice, polarization defect \(B\),
\(\widehat\Gamma_X\), \(\overline\Pi_X\), and the strict fixed-lift raw
Gram descent obstruction are constructed/proved.  Algebraic/effective Hall
support is not constructed by this lattice theorem. \\
Universal algebraic envelope &
definition/proposition only if supplied &
An object \(\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}\) may be introduced only
after finite windows, target BKM/Kac data, PBW/radical conventions, formal
hybrid operations, coalgebra conventions, Dirac blocks, Pfaffian
normalization, and transitions are defined.  It is target-derived unless
source provenance is supplied. \\
Compact \(K3\times E\) realization &
conditional/open &
The geometric source \(\mathfrak H^{geom}_{X,R}\) and functor
\(\mathsf{Real}_{X,R}\) require finite Hall stacks, orientation gerbes,
hybrid local/wrapped correspondences, protected integration, source
coalgebras, Pfaffian lines, primitive representatives, radical/PBW data,
and compatible transitions. \\
Scalar Behrend square &
imported orientation-forgetful check &
Oberdieck--Pixton, Oberdieck--Pandharipande, and Oberdieck give
\(Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}=-4096\Delta_5^{-2}\).  This does not
construct \(\mathfrak D_X\), \(\epsilon_o\), or compact primitive
recognition. \\
Eight-row host certificates &
framework; mostly open &
The catalogue and denominator rows are imported where cited.  Physical
row maps and scalar squares require row-by-row certificates. \\
\hline
\end{tabular}
\end{center}
```

## Exact Second Status Table Replacement

Replace the table at `main.tex:403-457` by:

```tex
\begin{center}
\small
\begin{tabular}{p{0.19\textwidth}p{0.17\textwidth}p{0.54\textwidth}}
\hline
Result & Status & Dependencies and exclusions \\
\hline
Protected K3 index and \(K_0\) half-index &
proved/imported/defined &
Right-moving localization gives \(Z_{\mathrm{K3}}=2\phi_{0,1}\).  The
half-index \(\mathbb U_{n,l}\) is a \(K_0\)-representative with
\(\sdim\mathbb U_{n,l}=f(n,l)\), not a canonical half-Hilbert space,
operator product, or compact D-brane state space. \\
Virtual determinant \(\mathcal D_X=\Delta_5\) &
computed/imported &
Computed from the \(K_0\)-half-index and identified with the
theta-normalized Borcherds product by the imported
Borcherds--Gritsenko--Nikulin theorem.  No compact source, orientation
gerbe, or Pfaffian line is supplied. \\
Denominator algebra &
imported &
Gritsenko--Nikulin give \(\mathfrak g_{\Delta_5}\), the active signed root
supermultiplicities \(f(nm,l)\), and
\(\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)\).  This
is the target bracket, not a compact Hall bracket. \\
Lattice normal ordering &
proved &
The formal Mukai lattice, cocycle \(B\), central extension
\(\widehat\Gamma_X\), homomorphism \(\overline\Pi_X\), raw lift
\(i_0\), split zero-Gram section, and flag formula are lattice algebra.
The fixed-lift raw Gram descent obstruction is proved. \\
\(\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}\) &
undefined unless inserted; target-derived if inserted &
May be claimed only after a finite algebraic definition is written.  Its
Pfaffian equality with \(\Delta_5\) is a formal packaging of the imported
GN product unless independent source data are supplied.  Do not call it a
compact source. \\
Compact geometric realization &
conditional/open &
Requires \(\mathfrak H^{geom}_{X,R}\) and
\(\mathsf{Real}_{X,R}\) preserving normal-ordered degrees, products,
coproducts, orientations, hybrid operations, source coalgebras, Dirac
blocks, Pfaffian line/cusp trivialization, primitive representatives,
radical/PBW data, and transitions.  Existence is open. \\
Scalar OP/DT square &
imported/check &
Oberdieck--Pixton, Oberdieck--Pandharipande, and Oberdieck identify the
Behrend-weighted reduced scalar branch with
\(-4096\Delta_5^{-2}\).  This checks an orientation-forgetful square and
does not construct \(\mathfrak D_X\), \(\epsilon_o\), a Hall Pfaffian sign,
or primitive recognition. \\
Eight-row host certificates &
certificate/open &
The automorphic products and denominator rows are imported where cited.
Physical row maps and scalar squares require row-by-row host
certificates. \\
\hline
\end{tabular}
\end{center}
```

Add immediately after this table:

```tex
\[
\Delta_5^2\not\Rightarrow \epsilon_o,\qquad
-4096\not\Rightarrow \text{Hall Pfaffian sign},\qquad
\nu_{\Delta_5}\not\Rightarrow [c_o]=0,\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})\not\Rightarrow
\mathfrak H^{geom}_{X,R}.
\]
The left sides are scalar or automorphic target data; the right sides are
reduced quotient-orientation, Weyl-transport, local Hall/Pfaffian, or
compact source constructions.
```

## Forbidden Phrases And Replacements

| Forbidden phrase | Replacement wording |
|---|---|
| `constructed finite compact source object` | `constructed universal algebraic finite model, if defined; not a compact \(K3\times E\) source until source provenance and a realization functor are supplied` |
| `universal finite Dirac--Igusa Hall source` | `universal algebraic Dirac--Igusa target envelope` unless finite source provenance exists |
| `\(\operatorname{Pf}(\mathsf{UDI})=\Delta_5\)` without qualifier | `the normalized formal Pfaffian of \(\mathsf{UDI}^{alg}\), after its finite target-envelope definition and Pfaffian convention, restates the Borcherds--Gritsenko--Nikulin product` |
| `the compact geometric Igusa theorem follows` | `if a compatible pro-realization exists, the geometric Pfaffian identity follows by preservation of the Pfaffian line and leading cusp trivialization` |
| `\(R_X:H_X^{geom}\to UDI\)` | `\(\mathsf{Real}_{X,R}:\mathfrak H^{geom}_{X,R}\to\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}\)` |
| `\(H_X^{geom}\)` without definition | `\(\mathfrak H^{geom}_{X,R}\), a finite compact Hall--Dirac source datum, if constructed` |
| `NO1--NO7 hold` | `NO1--NO7 are finite verification obligations unless the finite matrices, cochains, diagrams, and transitions are supplied` |
| `the radical quotient is already taken` | `the target radical quotient is imported/defined; the compact source radical quotient requires pairing matrices, kernels, ideal/coideal checks, and transition compatibility` |
| `source coalgebra constructed` | `source coalgebra constructed only if the finite hybrid source functor is defined independently of the target bar--cobar counit` |
| `orientation gerbe constructed` | `orientation gerbe defined after finite determinant lines/source stacks exist; global orientation is a trivialization condition` |
| `OP minus sign fixes the Pfaffian sign` | `the OP minus sign is a scalar convention and fixes neither Hall Pfaffian sign nor compact orientation monodromy` |
| `GN denominator constructs compact Hall source` | `GN denominator supplies the imported target bracket and multiplicities; compact Hall source construction remains separate` |

## Integration Order

1. Front-load the virtual determinant and GN target.
2. State the normal-ordered lattice theorem before any compact Hall, Dirac, Pfaffian, or realization language.
3. Mention \(\mathsf{UDI}^{alg}\) only after a definition exists.  If no definition is added, remove it from the abstract and status tables.
4. State compact \(K3\times E\) geometry as \(\mathsf{Real}_{X,R}\), a conditional realization functor.  Do not reuse \(R_X\), because `main.tex` already uses \(R_X\) for primitive recognition data.
5. Keep OP scalar square as an imported orientation-forgetful check.

## Residual Obligations

- If the main thread wants \(UDI\) in the platonic paper, it must first define \(\mathsf{UDI}^{alg}_{\Delta_5,E,L,R}\) with finite windows, BKM/Kac target data, PBW/radical conventions, formal hybrid operations, source/target coalgebra firewall, Dirac blocks, Pfaffian convention, and transition maps.
- If the main thread wants a compact theorem, it must supply \(\mathfrak H^{geom}_{X,R}\), source provenance, finite Hall correspondences, gerbe-lifted operations, protected integration, primitive representatives, pairing/radical/PBW data, Pfaffian lines, and \(\mathsf{Real}_{X,R}\).
- Until then, the front matter should say exactly: virtual determinant and GN target are proved/imported; normal-ordered lattice is constructed; \(UDI^{alg}\) is optional and target-derived if defined; compact \(K3\times E\) geometry is a conditional realization problem.
