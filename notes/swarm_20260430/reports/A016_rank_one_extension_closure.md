# A016 report: rank-one sector extension-closure

Runtime id: `019ddbd1-bbb8-7280-a28f-d36167748306`.
Nickname: Socrates.
Status: completed.
Files changed by agent: none.

## Verdict

No live theorem in `main.tex` assumes the rank-one D6-D2-D0 branch is an
extension-closed Hall category. The repair is mostly present: Hall
multiplication is moved upstairs to additive physical charge /
\(\widehat\Gamma_X\), and actual Hall sources are retained finite stages
with extension stacks. Two wording risks remain.

## Safe Anchors

Rank-one D6-D2-D0 is scalar/physical enumeration, not Hall source:
`main.tex:2723`, `main.tex:2832`, `main.tex:2841`, `main.tex:2877`,
`main.tex:15976`.

Gram degree is explicitly not Hall charge:
`main.tex:4400`, `main.tex:4524`, `main.tex:4966`, `main.tex:5042`.

Finite Hall source is additive/retained, not rank-one:
`main.tex:10233`, `main.tex:11353`, `main.tex:11661`,
`main.tex:13002`, `main.tex:13121`.

Rank-one factors are only orientation/HN graded pieces, not a generated
Hall locus:
`main.tex:4237`, `main.tex:4324`.

## Near-Risk Anchors

`main.tex:2904`:
"an extension-closed compact Hall/CoHA sector" appears immediately after
the rank-one D6-D2-D0 scalar branch. It is conditional and not rank-one,
but should say "full algebraic/effective support sector" explicitly.

`main.tex:2914`:
\(\operatorname{sdim}\operatorname{Prim}_{(n,l,m)}\) should be rewritten
as the normal-ordered pushforward form already used at `main.tex:449`.

`main.tex:3863`:
"rank-one ... sector is closed" should be "orientation descent ... is
closed/achieved"; avoid "closed" near Hall closure.

`main.tex:4362`:
"already-oriented rank-one sector" should be "already-oriented rank-one
strata/components."

## Corrected Boundaries

`thm:d6-d2-d0-mukai-gram-dictionary`:
only Mukai-vector and Gram-shadow computation.

`def:protected-hall-integration-criterion`:
conditional full Hall source criterion, graded by physical charge or
\(\widehat\Gamma_X\), then pushed to Gram degree.

`thm:finite-geometric-k3xe-hall-dirac-source`:
finite retained theorem from supplied `(Bnd/Rig/dCrit/RedOr/Six)` data,
not unrestricted compact realization.

Rank-one wall/orientation results:
local normal/Pfaffian/orientation base cases only.

## Critique Alignment

The critique's rank-one closure attack is correctly identified at
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:153`.
The guide's repair lanes match the manuscript:
physical charge versus Gram degree at
`notes/attack_whitepaper_analysis_20260430_guide.md:75`;
retained Liu-Hilbert stages at
`notes/attack_whitepaper_analysis_20260430_guide.md:196`;
compactified retained correspondences at
`notes/attack_whitepaper_analysis_20260430_guide.md:241`.

Commands run by agent:
`sed`, `nl -ba`, `rg`, `wc -l`, `find`, `git status --short`.
No build.
