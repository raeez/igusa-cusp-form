# A001 report: refreshed ingest provenance and catalogue completeness

Runtime id: `019ddbc4-e39a-70d2-9f7c-94fa8115c966`.
Nickname: Meitner.
Status: completed.
Files changed by agent: none.

## Stable Core

The guide is hash-provenanced and captures the main architecture. It is
not yet a complete claim catalogue for the refreshed 425-page artifact.

## Attacks

### Provenance

Status: stable.

`shasum -a 256` matches the guide:
`7b8212ad43d1562e6f9f90e3d1549bc83abfbeef5c292a4557ad254e6ec60a8c`
for the PDF and
`a99369847508320123491eb70def7766a8881d6522d19c27c3c83c57285f2dd7`
for the text.

Anchors:
`notes/attack_whitepaper_analysis_20260430_guide.md:3`,
`notes/swarm_20260430/plan.md:1`.

### Artifact Prompt Text

Status: valid attack.

The processed critique embeds prompt/control language, including "push
this all the way" and "must go further". The guide says the critique is
not primary literature, but should also explicitly state that prompt text
inside the artifact is not instruction.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43549`,
`notes/attack_whitepaper_analysis_20260430_guide.md:10`,
`notes/attack_whitepaper_analysis_20260430_guide.md:445`.

### Source Freshness and Citation Quality

Status: valid attack.

The PDF text contains non-citable placeholders: `arXiv +1`,
`UBC Mathematics`, `main main`, and "According to a document from April
29, 2026". The guide should require primary-source anchors before any
literature claim enters `main.tex`.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:41`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:370`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43565`.

### Late Construction Catalogue

Status: valid attack.

The guide compresses the final "finite point-stack Hall-Dirac model
versus Perf(\(K3\times E\)) incidence-cycle representability" split.

Anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43559`.

### Retained Liu-Hilbert Proof Obligations

Status: valid attack.

The guide records the class but undercatalogues proof obligations:
noetherian retained heart, openness of semistability, derived Artin
structure, Ext-stack/Postnikov assembly, \(d^2=0\), and
d-critical/vanishing-cycle/six-functor hypotheses.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43620`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:43687`,
`main.tex:10353`, `main.tex:13235`.

### Orientation Finite-Stabilizer Formulae

Status: valid attack.

The guide mentions finite stabilizers but omits formulas:
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,\quad
r_1=b_{20},\quad r_2=b_{02},\quad
r_3=b_{20}+b_{11}+b_{02},
\]
and the even-\(N\) mixed term \(A_{12}\).

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44305`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44467`,
`main.tex:3306`, `main.tex:3393`.

### Hybrid Anchor Data

Status: valid attack.

The guide names colored flags but omits anchor data:
\[
\lambda(F)=\det Rp_{E,*}F\otimes O_E(-\chi(F)0_E)\in\operatorname{Pic}^0(E),
\]
rigidified wrapped stacks, and LL/LW/WL/WW equations.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44501`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44517`,
`main.tex:7357`.

### Type-II Wall Atoms

Status: valid attack.

The guide emphasizes a graph-isogeny candidate; the latest PDF also
gives explicit reducible curve atoms for \(\delta_1,\delta_2,\delta_3\)
plus rank-one Ext/Pfaffian calculations. These remain residual until
global semistability, wall equality, and quotient orientation are proved.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44561`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44773`.

### \(W_{\le3}\) Source Catalogue

Status: valid attack.

The guide says "source matrices" but omits the explicit table:
\(29|93\) at \(\tau=\delta_1+\delta_2+\delta_3\), nine
\(u_{ij,r}\), \(T_1+T_2+T_3=0\), \(V_{k;ij,r}\), \(K=0\),
\(Q=I\), and comparison equations. Source geometry remains unproved.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44977`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:45203`,
`main.tex:12488`.

### Cofinal All-Window Theorem

Status: valid attack.

The guide mentions transition identities but omits exact finite
equations and the \(R^1\lim=0\) Mittag--Leffler condition.

Anchors:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:45626`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:45687`.

Commands run by agent: `sed`, `wc -l`, `shasum -a 256`, targeted `rg`,
`nl -ba main.tex`, `git status --short`. No build.
