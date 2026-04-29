# Agent63 bibliography/citation latest report

Date: 2026-04-29

Control: proposal-only bibliography/citation risk review. I did not edit
`main.tex`, `proj.bib`, or source. This report is the only written file.

Inputs read: `AGENTS.md`, `CLAUDE.md`, the attack-heal skill and protocol,
`main.tex`, `proj.bib`, current `git diff -- main.tex`, Agent20 and Agent37
source-audit reports, and targeted current line ranges around the new
target-reference tower.

## Stable core

Citation-key integrity is clean. Extracting active citation keys from
`main.tex` and comparing against `proj.bib` found 80 active cite keys and
91 bibliography entries, with no missing active key.

The existing bibliography likely covers the imported families needed for
the new tower wording:

| Claim family | Likely existing keys | Coverage status |
|---|---|---|
| GN product, denominator algebra, root multiplicities, `2Z` normalization | `GN`, `GNII`, `Borcherds95` | Covered at key level; theorem/equation anchors still need local insertion at first tower use. |
| Kac/Borcherds-Kac presentation, invariant pairing/radical, PBW language | `KAC:1`, plus GN/GNII for this specific algebra | Covered at key level; current tower definition should not make Kac supply the GN-specific radical unless phrased as standard Kac presentation plus GN specialization. |
| BD current envelope and chiral bar-cobar formalism | `BD` | Covered. |
| Francis-Gaitsgory chiral Koszul duality/conilpotent bar-cobar domain | `FrancisGaitsgoryCKD` | Covered. |
| OP/Oberdieck scalar square and variable convention | `OB`, `OPand`, `OberdieckReducedPT`, `BRYAN` | Covered at key level; OPand exact proposition label remains unresolved from Agent20. |

No new BibTeX entry is strictly required for the target-reference tower.
The needed repair is inline source-role precision and local wording
downgrade where the tower is a constructed formal target package, not an
external theorem.

## Valid citation risks and proposed heals

### A63-01: First tower mention imports GN/Kac/PBW/radical without citation

Target: `main.tex:83-104`, especially `main.tex:99-103`.

Claim under risk: finite windows of the imported target have PBW bases, the
standard target invariant form, target radical quotient, Borcherds-Kac
bracket, formal first-order blocks, and a formal Pfaffian product.

Problem: the paragraph is in the abstract and has no citation or local
cross-reference. It imports GN/Kac target structure and also introduces
formal first-order/Pfaffian packaging. Existing later citations cover parts
of this, but the first theorem-level import is currently unsupported at the
point of use.

Minimal citation heal:

```tex
Equivalently, using the Gritsenko--Nikulin denominator algebra recalled in
Theorem~\ref{thm:denominator-algebra-identity}, one may package finite
windows of this imported target as an algebraic Dirac--Igusa target
reference tower.  Such a tower has PBW bases, the standard target invariant
form, the target radical quotient, and the Borcherds--Kac bracket from the
imported GN/Kac target presentation; it has formal first-order blocks and a
formal super-Pfaffian product only after the finite algebraic convention of
Definition~\ref{def:finite-algebraic-dirac-igusa-target-reference-tower}.
```

If direct citations are preferred in the abstract, add:

```tex
\cite[Theorem~2.1, (2.1)--(2.3)]{GNII},
\cite[Sections~3--4]{GN}, \cite{KAC:1}
```

Better wording downgrade: replace "has ... by construction from
`\mathfrak g_{\Delta_5}`" with "is packaged from the imported target after
choosing finite algebraic conventions." This prevents the reader from
thinking GN/Kac constructed the Dirac block or Pfaffian line.

### A63-02: Tower definition needs exact source-role sentence

Target: `main.tex:5889-5965`, especially `main.tex:5908-5915`.

Claim under risk: the finite truncation has "standard invariant form,
standard radical quotient, and Borcherds--Kac bracket"; PBW monomials in
`U(\mathfrak g_{\Delta_5})` are used as tower data.

Existing keys likely cover it: `GN`, `GNII`, `KAC:1`.

Missing local anchor:

```tex
be the corresponding finite target truncation of the imported
Gritsenko--Nikulin denominator algebra
\cite[Theorem~2.1, (2.1)--(2.3)]{GNII}, \cite[Sections~3--4]{GN},
with the Kac presentation, invariant form, radical quotient, and PBW
convention used in Theorem~\ref{thm:primitive-recognition}.
```

Do not cite Kac alone for the specific radical
`\operatorname{Rad}_{\mathrm{GN}}`; that radical is manuscript/GN-target
notation. Use Kac only for standard presentation/PBW background and route
the GN-specific quotient through the local theorem.

### A63-03: Target normalization uses GN product but has no direct cite

Target: `main.tex:5967-5999`, especially `main.tex:5990-5994`.

Claim under risk:

```tex
Passing through an exhausting compatible sequence of finite windows gives
the monic Borcherds product D_5=64^{-1}\Delta_5 by the imported
Borcherds--Gritsenko--Nikulin product formula.
```

Existing keys likely cover it: `GNII`, `GN`, `Borcherds95`.

Exact missing citation:

```tex
... by the Gritsenko--Nikulin specialization of Borcherds' product theorem
\cite[Theorem~2.1, (2.1)--(2.3), Example~2.4, (2.15)--(2.16)]{GNII},
\cite[Theorem~4.1]{GN}.
```

Do not use `Borcherds95` alone here. Borcherds supplies the general product
mechanism; GN/GNII supply the genus-two `\phi_{0,1}`, `64`, product cone,
and `D_5=64^{-1}\Delta_5` normalization.

### A63-04: BD/FG citations mostly present, but one recurrence needs local anchor

Targets: `main.tex:5853-5882`, `main.tex:6657-6676`,
`main.tex:6691-6696`, `main.tex:7128-7130`.

Status: the formal current envelope cites BD at `main.tex:5853-5854`; the
target-internal bar-cobar proposition cites Kac, BD, and Francis-Gaitsgory
at `main.tex:6672-6676`; its proof cites BD at `main.tex:6691-6696`.

Residual citation risk: the later phrase "Beilinson--Drinfeld/Francis--
Gaitsgory bar--cobar domain" at `main.tex:7128-7130` has no direct citation
in that corollary. It can rely on the preceding proposition, but the
sentence is a theorem-level source boundary and should carry a local cite.

Minimal heal:

```tex
First, the supplied hybrid source must itself lie in the
Beilinson--Drinfeld/Francis--Gaitsgory bar--cobar domain
\cite[\S3.7]{BD}, \cite[Theorem~6.2.2]{FrancisGaitsgoryCKD}.
```

Wording is otherwise safe because the manuscript repeatedly says these are
target/formalism sources and do not construct the compact source.

### A63-05: OP scalar square first mentions lack citations

Targets: `main.tex:123-135`, `main.tex:332-351`,
`main.tex:410-415`.

Claim under risk: OP/Oberdieck give
`Z^X_DT=Z^X_OP=-4096\Delta_5^{-2}` and
`\chi_{10}^{OP}=D_5^2`.

Existing keys likely cover it: `OB`, `OPand`, `OberdieckReducedPT`,
`BRYAN`. Later proofs cite them at `main.tex:14039-14079` and
`main.tex:14109-14130`.

Minimal abstract/introduction heal:

```tex
The scalar Behrend-weighted branch, recalled in
Theorem~\ref{thm:op-square} from
Oberdieck--Pixton, Oberdieck--Pandharipande, and Oberdieck, is ...
```

If direct citations are inserted at first mention:

```tex
\cite[Theorem~1]{OB},
\cite[Section~2]{OPand},
\cite[Theorem~3(i)]{OberdieckReducedPT}
```

Do not cite `OPand` as "Proposition 5" until the Agent20 discrepancy is
resolved against the primary source. Use `\cite[Section~2]{OPand}` or the
local theorem cross-reference for now.

### A63-06: GN additive coefficient citation appears too coarse

Target: `main.tex:13121-13129`, proof at `main.tex:13453-13456`.

Claim under risk: `m(\delta_{123})=-93`, the conversion
`m(a)=-64^{-1}c_\Delta(...)`, and isotropic `\tau` constants.

Current citation at `main.tex:13456` is `\cite[Theorem~2.1]{GN}`. Agent37
reports the source role more precisely: GN Theorem 2.3 and its proof on
pp. 10-11 carry the additive correction coefficients `m(a)`, `m(0)=-1`,
and `\tau`.

Exact citation heal:

```tex
... converted to Gritsenko--Nikulin \(m(a)\) by the additive correction
coefficient formula of \cite[Theorem~2.3 and proof, pp.~10--11]{GN};
```

If page references are avoided until published-page verification:

```tex
\cite[Theorem~2.3]{GN}
```

Wording downgrade if not source-checked:

```tex
using the GN additive-correction convention for \(m(a)\), pending final
published-page verification;
```

### A63-07: `formal Pfaffian product` should remain convention-dependent

Targets: `main.tex:99-103`, `main.tex:399-403`,
`main.tex:466-471`, `main.tex:5925-5948`.

Claim under risk: "formal Pfaffian product" can sound like an externally
proved Pfaffian line or geometric orientation theorem.

No new external citation is needed if the text keeps it as an internal
finite algebraic convention. The definition already says "After a finite
algebraic super-Pfaffian convention is fixed" at `main.tex:5942`.

Wording downgrade:

```tex
formal first-order blocks and a formal super-Pfaffian product after choosing
a finite algebraic convention
```

Use this wording at the abstract/table mentions. Do not cite OP, BBDJS, or
Joyce-Upmeier for this target package; those sources do not construct the
target-reference tower.

## No-action items

No new bibliography key is needed for GN/Kac/BD/FG/OP coverage.

Do not add citations to internal attack reports from `main.tex`.

Do not cite `Borcherds95` for `64`, `D_5`, `\Delta_5`, `2Z`, OP scalar
normalization, or GN parity/radical data.

Do not cite OP/Oberdieck for orientation, Pfaffian sign, compact Hall
source, PBW, radical quotient, or primitive recognition.

Do not cite BD/Francis-Gaitsgory as constructing the compact source
coalgebra. They cover formal chiral/bar-cobar technology; the source
construction remains conditional.

## Residual obligations

1. Insert local source-role citations or cross-references at the first
abstract/introduction occurrences of the tower, GN target, and OP scalar
claims.
2. In the tower definition/proposition, cite GN/GNII for the target and
product normalization; cite Kac only for standard presentation/PBW
background or cross-reference the manuscript's primitive-recognition
theorem.
3. Add the BD/FG cite at the later "bar-cobar domain" phrase if that
corollary is meant to stand alone.
4. Replace the coarse GN additive-coefficient citation with Theorem 2.3
source-role wording.

Bottom line: the current bibliography covers the tower. The current wording
needs citation placement and source-role downgrades so the reader sees a
formal target-reference package, not a claimed compact source theorem.
