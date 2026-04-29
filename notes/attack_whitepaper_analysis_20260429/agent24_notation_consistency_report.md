# Agent 24 Notation Consistency Report

Scope: current `main.tex` and the extracted text of
`materials/raw/2026-04-29-attack-whitepaper-analysis.pdf`
(`materials/processed/2026-04-29-attack-whitepaper-analysis.txt`). This is a
notation audit only. No manuscript source is edited here.

## Notation inventory

Observed canonical layers in `main.tex`:

- `\Gamma_X^{\mathrm{form}}`: formal full-Mukai dyonic lattice
  `\Lambda_S \oplus \Lambda_S`; defined at `main.tex:4327-4335`.
- `\Gamma_X^{\mathrm{phys}}`: legacy mnemonic currently identified with
  `\Gamma_X^{\mathrm{form}}`; explicitly not the full four-dimensional
  physical charge lattice and not compact Hall support, `main.tex:4332-4346`.
- `\Gamma_X^{\mathrm{alg}}` and `\Gamma_{X,\sigma}^{\mathrm{eff}}`: actual
  algebraic/effective Hall support inside `\Gamma_X^{\mathrm{form}}`;
  `main.tex:4343-4346`, `main.tex:8313-8316`.
- `\Gamma_{\mathrm{gram}}`: Gram/Fourier-index lattice `\mathbb Z^3`;
  `main.tex:4347-4355`.
- `\Gamma_{\mathrm{ind}}`: automorphic/Fourier alias for
  `\Gamma_{\mathrm{gram}}`; `main.tex:4431-4452`. It must not be read as a
  Hall charge lattice.
- `\Gamma_{\mathrm{eff}}`: cusp-positive product semigroup;
  `main.tex:656-659`.
- `\Gamma_{\mathrm{act}}`: active support where `f(nm,l) != 0`;
  `main.tex:4433-4437`, `main.tex:5399-5402`.
- `\Pi_X`: raw quadratic Gram map
  `(Q,P) -> (Q^2/2,Q.P,P^2/2)`; `main.tex:4351-4356`,
  `main.tex:4513-4519`.
- `B`: symmetric bilinear polarization defect for `\Pi_X`;
  `main.tex:4357-4366`, `main.tex:4590-4601`.
- `\widehat\Gamma_X`: normal-ordered central extension
  `\Gamma_X^{\mathrm{phys}}\oplus_B\Gamma_{\mathrm{gram}}`;
  `main.tex:4370-4377`, `main.tex:4832-4860`.
- `\overline\Pi_X`: additive normal-ordered Gram homomorphism
  `\widehat\Gamma_X -> \Gamma_{\mathrm{gram}}`; `main.tex:4664-4671`,
  `main.tex:4759-4765`.
- `B_{\mathrm{ch}}`: translation-valued Hochschild 2-cocycle
  `\mathsf T_{B(c,c')}`, not the lattice bilinear map itself;
  `main.tex:8387-8413`, `main.tex:8728-8749`.
- `\Theta_\Pi`: normal-ordering 1-cochain with
  `d_{\mathrm{Hoch}}\Theta_\Pi=B_{\mathrm{ch}}`; `main.tex:8326-8337`,
  `main.tex:8392-8413`, `main.tex:9024-9036`.
- `\overline\Pi_{X,*}^{\Theta}`: chain-level corrected descent; the raw
  `\Pi_X` pushforward is not a recognition target, `main.tex:4977-4995`,
  `main.tex:8317-8345`.
- `\mathcal D_X`: virtual `K_0` Borcherds determinant, equal to the
  theta-normalized `\Delta_5`; `main.tex:818-838`, `main.tex:2534-2557`.
- `\mathfrak D_X`: conditional first-order protected operator/algebra; open
  source-side datum, not constructed by `\mathcal D_X`; `main.tex:894-909`,
  `main.tex:10609-10622`.
- `D_5`: monic Borcherds product `64^{-1}\Delta_5`; `main.tex:80-81`,
  `main.tex:2543-2551`, `main.tex:14799-14815`.
- `\Delta_5`: theta-normalized Igusa square root with leading coefficient
  `64`; `main.tex:321-328`, `main.tex:2388-2393`.
- `\Delta_{10}`: scalar square `\Delta_5^2`; `main.tex:2388-2392`,
  `main.tex:14563-14566`.
- `\chi_{10}^{\mathrm{OP}}`: Oberdieck--Pixton monic scalar product,
  `D_5^2=4096^{-1}\Delta_5^2`; `main.tex:13752-13759`.
- `\mathsf{Den}_{\Delta_5,E}`: formal BD current envelope on `E` built from
  the target denominator algebra; `main.tex:5727-5740`.
- `C_X`: source chiral coalgebra; it is not the target bar coalgebra of
  `\mathsf{Den}_{\Delta_5,E}`; `main.tex:6357-6373`,
  `main.tex:6404-6435`, `main.tex:12049-12083`.
- `\mathcal F_X^{(0)}`: projection-finite chiral shadow after supplied
  `K3`-to-`E` specialization; `main.tex:226-243`.
- `\mathcal F_X^{\mathrm{hyb}}`: full hybrid local/wrapped source after the
  finite hybrid certificate is supplied; `main.tex:242-258`,
  `main.tex:8294-8300`.
- `\mathfrak K_X=(L_X,H_X,O_X,D_X,R_X)`: five-part realization certificate;
  `main.tex:11750-12121`.
- Row forms `F_j`: present order
  `(Delta_5, Delta_2, Delta_1, Delta_{1/2}, nabla_3, nabla_2,
  nabla_{3/2}, Q_1)`, `main.tex:14352-14372`, with a separate
  Clery--Gritsenko source order at `main.tex:14692-14710`.
- OP/DT variables: the manuscript uses Borcherds variables
  `(q,r,s)`, OP variables `(q_{\mathrm{OP}},p_{\mathrm{OP}},
  \widetilde q_{\mathrm{OP}})`, and DT variables
  `(q_{\mathrm{DT}},t_{\mathrm{DT}},p_{\mathrm{DT}})`; see
  `main.tex:13709-13759`.
- Elliptic curve degree: curve degree is `d`; Borcherds third Gram
  coordinate is `m=d-1`, `main.tex:2661-2694`, `main.tex:13717-13720`.

## Collisions/ambiguities

1. `\Gamma_X^{\mathrm{phys}}` still appears as if it were the microscopic
   physical charge lattice, even though the manuscript says it is only the
   formal full-Mukai bookkeeping lattice. The attack PDF correctly attacks
   this at processed lines `83-170`. In current `main.tex`, the danger is
   reduced but not eliminated: the primitive bracket still writes
   `c,c'\in\Gamma_X^{\mathrm{phys}}` near `main.tex:260-275` and
   `main.tex:532-537`.

2. `\Gamma_{\mathrm{gram}}:=\Gamma_{\mathrm{ind}}:=\mathbb Z^3` is useful
   locally but dangerous globally. The attack PDF reads `\Gamma_{\mathrm{ind}}`
   as a would-be Hall grading at processed lines `92-103`. The manuscript's
   repair at `main.tex:4431-4452` is correct, but every later use of
   `\Gamma_{\mathrm{ind}}` must remain automorphic/Fourier-only.

3. The attack PDF proposes bare `\Gamma_X` for the normal-ordered extension
   at processed lines `22177-22224`. Current `main.tex` uses
   `\widehat\Gamma_X`. Do not import the bare attack notation. Bare
   `\Gamma_X` collides with `\Gamma_X^{\mathrm{form}}`,
   `\Gamma_X^{\mathrm{phys}}`, and source support.

4. The attack PDF extraction visually collapses the raw and corrected maps:
   processed lines `20944-20950`, `21191-21198`, and `22221-22231` use
   `Pi_X` for both maps. Current `main.tex` correctly separates raw
   `\Pi_X` from corrected `\overline\Pi_X`. This distinction is load-bearing.

5. `B`, `B_{\mathrm{ch}}`, `B_{\mathrm C}`, and
   `\bar B_E^{\mathrm{ch}}` sit close together. Current `main.tex` mostly
   separates them, but any prose saying "the B-cocycle" without target
   category is ambiguous. `B` is lattice-valued; `B_{\mathrm{ch}}` is
   translation-valued; `B_{\mathrm C}` is Connes; `\bar B_E^{\mathrm{ch}}`
   is chiral bar.

6. `\mathcal D_X`, `\mathfrak D_X`, `D_X`, and `D_5` are four different
   objects. The attack PDF frequently writes bare `DX`; see processed lines
   `21055-21069`, `21814`, `22036`, `23032-23034`, `23719-23775`. Current
   `main.tex` adds a certificate component `(D_X)` at `main.tex:11989-12104`,
   which collides visually with both `\mathcal D_X` and `\mathfrak D_X`.

7. `D_0` and `D_5` are visually close and semantically unrelated:
   `D_0` is a finite first-order certificate (`main.tex:9973-10269`);
   `D_5` is the monic Borcherds product. No prose should shorten `D_0` to
   `D` or `D_X`.

8. `\Phi` has at least five meanings: BBDJS perverse sheaf `\Phi_c`,
   placeholder `\Phi^{\mathrm{FA}}_3`, row scalar form `\Phi_j`, sourced CHL
   scalar forms such as `\Phi_6^{(1,2)}`, and formal comparison symbols
   `\Phi^{\mathrm{cmp}}_j`. The row section correctly warns that
   `\Phi^{\mathrm{cmp}}_j` is not a row label, `main.tex:15893-16055`.

9. `\mathsf{Den}_{\Delta_5,E}` is target-internal. The attack PDF introduces
   `\mathrm{Den}^{\mathrm{alg}}_{\Delta_5,C,L}` and `D^{alg}` at processed
   lines `21840-21848`, `22868-22912`, `23032-23034`, and `24357`. Current
   `main.tex` does not define this notation. Importing it without a new
   notation box would create a second denominator target that looks like the
   existing one.

10. `Hpre` and `Htw` are attack-PDF objects, not current manuscript
    notation. Processed lines `21859-21895` and `23051-23167` propose a
    pre-Hall correspondence object and a twisted protected object. Current
    `main.tex` has `\mathcal H_X` inside `(O_X)`, not
    `\mathcal H_X^{\mathrm{pre}}` or `\mathcal H_X^{\mathrm{tw}}`.

11. The five certificate labels `L_X,H_X,O_X,D_X,R_X` are too bare. `H_X`
    collides with the actual Hall object `\mathcal H_X`; `D_X` collides with
    determinant/operator notation; `O_X` resembles the structure sheaf. They
    should remain parenthesized labels only or be renamed to explicit
    `K`-subscripts.

12. The row labels `F_j` depend on order. Current `main.tex` has both
    present order and source order. The attack PDF repeatedly asks for a row
    map discipline. The safe rule is: `F_j` always means the present
    manuscript order; any Clery--Gritsenko source order or triple order must
    be named every time.

13. OP variables are not physical charge variables. Lowercase `p` is
    overloaded by OP `p_{\mathrm{OP}}`, DT `p_{\mathrm{DT}}`, parity maps
    `p`, and physical magnetic charge `P`. Current `main.tex:13717-13720`
    helps, but `main.tex:13810-13819` reintroduces uppercase `(T,Q,P)`.

14. Elliptic degree drift remains a high-risk inference. The curve degree is
    `d`; the Borcherds third exponent is `m=d-1`; the source wrapped degree
    `b_R` is geometric and must state whether it records `d` or the shifted
    `m`. The attack PDF explicitly asks for this at processed lines
    `21147-21156`.

## Mandatory canonical notation

- Formal dyonic lattice: `\Gamma_X^{\mathrm{form}}`.
- Legacy alias: `\Gamma_X^{\mathrm{phys}}:=\Gamma_X^{\mathrm{form}}` only
  inside explicit legacy warnings and old formula compatibility. New prose
  should not introduce unqualified `\Gamma^{\mathrm{phys}}`.
- Actual Hall support: `\Gamma_{X,\sigma}^{\mathrm{eff}}\subset
  \Gamma_X^{\mathrm{alg}}\subset\Gamma_X^{\mathrm{form}}`.
- Gram/Fourier lattice: `\Gamma_{\mathrm{gram}}`. Use
  `\Gamma_{\mathrm{ind}}` only in the automorphic/Fourier index section and
  immediately identify it with `\Gamma_{\mathrm{gram}}`.
- Raw map: `\Pi_X:\Gamma_X^{\mathrm{form}}\to\Gamma_{\mathrm{gram}}`.
- Corrected lattice: `\widehat\Gamma_X`, not bare `\Gamma_X`.
- Corrected additive map: `\overline\Pi_X:\widehat\Gamma_X\to
  \Gamma_{\mathrm{gram}}`.
- Chain descent: `\overline\Pi_{X,*}^{\Theta}`.
- Lattice cocycle: `B`. Chain/Picard cocycle: `B_{\mathrm{ch}}`. Connes
  operator: `B_{\mathrm C}`. Chiral bar: `\bar B_E^{\mathrm{ch}}`.
- Virtual determinant: `\mathcal D_X`. First-order operator/algebra:
  `\mathfrak D_X`. Certificate descent component: do not write bare `D_X`
  in running prose; use `\textup{(D_X)}` as a label or rename.
- Monic Borcherds product: `D_5=64^{-1}\Delta_5`.
- Theta-normalized Igusa square root: `\Delta_5`.
- Scalar square: `\Delta_{10}=\Delta_5^2`.
- OP scalar product: `\chi_{10}^{\mathrm{OP}}=D_5^2`.
- Target current envelope: `\mathsf{Den}_{\Delta_5,E}`.
- If the attack-PDF algebraic curve-universal target is imported, use
  `\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}` and define it once before
  `\mathsf{Den}_{\Delta_5,E}` is mentioned in the same section.
- Source coalgebra: `C_X` and finite stages `C_{X,R}` only after source
  construction; never define them from the target bar coalgebra.
- Hybrid source: `\mathcal F_X^{\mathrm{hyb}}`; projection-finite shadow:
  `\mathcal F_X^{(0)}`; first-order certificate source object:
  `\mathcal F_X^{D_0}`.
- If attack-PDF `Hpre/Htw` is imported, write
  `\mathcal H_X^{\mathrm{pre}}` and `\mathcal H_X^{\mathrm{tw}}` and define
  their relation to current `\mathcal H_X`.
- Row labels: `F_j` in present manuscript order only:
  `F_1=\Delta_5`, `F_2=\Delta_2`, `F_3=\Delta_1`,
  `F_4=\Delta_{1/2}`, `F_5=\nabla_3`, `F_6=\nabla_2`,
  `F_7=\nabla_{3/2}`, `F_8=Q_1`.
- OP/DT variables: always subscripted in prose and tables:
  `q_{\mathrm{OP}},p_{\mathrm{OP}},\widetilde q_{\mathrm{OP}}`,
  `q_{\mathrm{DT}},t_{\mathrm{DT}},p_{\mathrm{DT}}`.
- Borcherds variables: if there is any local risk of collision, use
  `q_{\mathrm{Bch}},r_{\mathrm{Bch}},s_{\mathrm{Bch}}`.
- Elliptic curve degree: `d`. Borcherds third coordinate: `m=d-1`.

## Replacement map

Use this map before importing any attack-PDF prose.

| Attack/current ambiguous form | Replace with | Reason |
|---|---|---|
| `\Gamma^{\mathrm{phys}}`, `\Gamma_{\mathrm{phys}}` | `\Gamma_X^{\mathrm{form}}` or explicit actual support | Avoid false microscopic Hall charge claim. |
| `\Gamma_X^{\mathrm{phys}}` in new prose | `\Gamma_X^{\mathrm{form}}` | Current `phys` is legacy mnemonic only. |
| `\Gamma_{\mathrm{ind}}` as Hall grade | `\Gamma_{X,\sigma}^{\mathrm{eff}}` upstairs, then `\overline\Pi_X` descent | `\Gamma_{\mathrm{ind}}` is Gram/Fourier only. |
| Bare `\Gamma_X` for corrected extension | `\widehat\Gamma_X` | Current manuscript canonical notation. |
| `\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}` | `\overline\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}` | Preserve raw/corrected split. |
| `\Pi_{X,*}` or `\Pi_*` for descent | `\overline\Pi_{X,*}^{\Theta}` | Raw pushforward is not recognition target. |
| `B` for chiral transport | `B_{\mathrm{ch}}` | `B` is lattice-valued. |
| `B` for Connes operator | `B_{\mathrm C}` | Avoid collision with Gram cocycle. |
| `DX=\Delta_5` | `\mathcal D_X=\Delta_5` | `D_X` collides with certificate slot and operator. |
| `Pf_{\mathrm{prot}}(D_X)` | `\operatorname{Pf}_{\mathrm{prot}}(\mathfrak D_X)` | First-order operator is fraktur. |
| `D_X` as certificate entry in prose | `\textup{(D_X)}` or `\mathsf K_X^{\mathrm{desc}}` | Prevent determinant/operator collision. |
| `D5` | `D_5` | Monic Borcherds product. |
| `\Delta_5` for monic product | `D_5=64^{-1}\Delta_5` | Main reserves `\Delta_5` for theta normalization. |
| `\chi_{10}` or `\Phi_{10}` for OP scalar | `\chi_{10}^{\mathrm{OP}}` | OP normalization is specific and monic. |
| `\Phi_j=F_j^2` without source | `\Phi_j` only inside a row certificate | Scalar square is not a row map. |
| `\Phi^{\mathrm{cmp}}_j=F_j` | ban | False by weight for displayed comparison slots. |
| `Den_{\Delta_5,E}` | `\mathsf{Den}_{\Delta_5,E}` | Match current target-envelope style. |
| `Denalg_{\Delta,C,L}` | `\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}` | Only if a new algebraic target section is added. |
| `Hpre_X` | `\mathcal H_X^{\mathrm{pre}}` | Attack-PDF notation needs TeX definition. |
| `Htw_X` | `\mathcal H_X^{\mathrm{tw}}` | Distinguish from current `\mathcal H_X`. |
| `FXhyb` | `\mathcal F_X^{\mathrm{hyb}}` | Current manuscript notation. |
| OP `q,r,s,p` bare | subscript OP/DT/Bch variables | Prevent variable collision. |
| `m=d` or `elliptic degree m` | `m=d-1`; `d` is curve degree | Todd/vacuum shift is load-bearing. |

## main.tex anchors

- Abstract normalization: `\mathcal D_X=\Delta_5`, `D_5=64^{-1}\Delta_5`,
  OP scalar branch, and raw/corrected Gram map: `main.tex:73-154`.
- Early compact-factorization warning and `\Gamma_X^{\mathrm{phys}}`
  legacy warning: `main.tex:226-295`.
- Product semigroup and active support warning:
  `main.tex:455-460`.
- Initial Gram-index lattice and cusp-positive semigroup:
  `main.tex:640-665`.
- Virtual determinant package:
  `main.tex:770-855`.
- Conditional `D_0` theorem data:
  `main.tex:1147-1171`.
- D6--D2--D0 Mukai--Gram dictionary:
  `main.tex:2661-2755`.
- Formal dyonic lattice and raw Gram map:
  `main.tex:4316-4382`.
- Gram-index alias and warning against Hall grading by `\Gamma_{\mathrm{ind}}`:
  `main.tex:4431-4452`.
- Normal-ordered central extension and additive homomorphism:
  `main.tex:4590-4689`, `main.tex:4832-4881`.
- Correct recognition route:
  `main.tex:4977-4995`.
- Target current envelope:
  `main.tex:5727-5755`.
- Source coalgebra vs target counit firewall:
  `main.tex:6357-6435`.
- Normal-ordering cochain and `B_{\mathrm{ch}}`:
  `main.tex:8305-8415`, `main.tex:8460-8535`,
  `main.tex:8728-8752`, `main.tex:8803-8815`,
  `main.tex:8894-8934`, `main.tex:9024-9036`.
- First-order `D_0` certificate:
  `main.tex:9973-10754`.
- Five-part realization certificate:
  `main.tex:11750-12121`.
- Primitive recognition certificate:
  `main.tex:12124-12444`.
- OP/DT variable dictionary and scalar square:
  `main.tex:13709-13825`, `main.tex:13857-13900`.
- Row-label certificate and present order:
  `main.tex:14290-14440`.
- Source order versus present order:
  `main.tex:14689-14726`.
- Comparison row warnings:
  `main.tex:15893-16055`.

## Patch queue

P0. Add a single notation firewall box near `main.tex:455-460` or immediately
after `main.tex:4431-4452`. It must list:
`\Gamma_X^{\mathrm{form}}`, `\Gamma_{X,\sigma}^{\mathrm{eff}}`,
`\Gamma_{\mathrm{gram}}`, `\Gamma_{\mathrm{ind}}`, `\Pi_X`,
`\widehat\Gamma_X`, `\overline\Pi_X`, `B`, `B_{\mathrm{ch}}`,
`\Theta_\Pi`, `\mathcal D_X`, `\mathfrak D_X`, `D_5`, `\Delta_5`,
`\chi_{10}^{\mathrm{OP}}`.

P0. Replace non-legacy `\Gamma_X^{\mathrm{phys}}` occurrences in compact
source prose by `\Gamma_X^{\mathrm{form}}` or by the actual support
`\Gamma_{X,\sigma}^{\mathrm{eff}}`. Keep `phys` only where the sentence
explicitly says it is a legacy mnemonic.

P0. Protect the five-part certificate notation. Either rename
`\mathfrak K_X=(L_X,H_X,O_X,D_X,R_X)` to
`\mathfrak K_X=(K_X^{\mathrm{loc}},K_X^{\mathrm{hyb}},
K_X^{\mathrm{or}},K_X^{\mathrm{desc}},K_X^{\mathrm{rec}})`, or require
parenthesized labels `\textup{(L_X)}` etc. in all prose. The current `D_X`
label is the most dangerous collision.

P0. Ban attack-PDF bare `\Gamma_X` for the corrected extension. If attack
material is integrated, map every such use to `\widehat\Gamma_X`.

P0. Ban attack-PDF bare `DX`. Every occurrence must choose exactly one:
`\mathcal D_X`, `\mathfrak D_X`, `D_5`, or certificate label
`\textup{(D_X)}`.

P1. Consolidate OP/DT/Borcherds variables into one table and delete or
cross-reference repeat dictionaries. The table must state
`q_{\mathrm{Bch}}=q_{\mathrm{OP}}=t_{\mathrm{DT}}`,
`r_{\mathrm{Bch}}=p_{\mathrm{OP}}=p_{\mathrm{DT}}`,
`s_{\mathrm{Bch}}=\widetilde q_{\mathrm{OP}}=q_{\mathrm{DT}}`, with
`m=d-1`.

P1. Add a sentence wherever `b_R` is introduced: `b_R` records geometric
wrapped elliptic degree; the Borcherds third exponent is the shifted Gram
coordinate `m=d-1` unless a finite-stage convention explicitly shifts it.

P1. If the attack-PDF `Hpre/Htw` architecture is imported, define it before
the five-part certificate:
`\mathcal H_X^{\mathrm{pre}}` for pre-orientation derived correspondences,
`\mathcal H_X^{\mathrm{tw}}` for the orientation-gerbe-twisted object.
Then say exactly how current `\mathcal H_X` in `(O_X)` relates to them.

P1. If a curve-universal algebraic target is imported, introduce
`\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}` in a separate algebraic-target
subsection. Do not silently rename current `\mathsf{Den}_{\Delta_5,E}`.

P1. Add a row-label convention sentence before the first row table:
`F_j` always means the present manuscript order. Any source-order or triple
order list is not an `F_j` list unless reindexed by the displayed
permutation.

P2. Add TeX macros for the most fragile symbols. Proposed macro family:
`\Gform`, `\Ggram`, `\GhatX`, `\PiRaw`, `\PiNO`, `\Dvirt`, `\Dop`,
`\DenE`, `\Fhyb`. This is mechanical but reduces future drift.

## Banned symbol aliases

- `\Gamma_{\mathrm{phys}}`, `\Gamma^{\mathrm{phys}}`: no unindexed physical
  lattice.
- `\Gamma_X` for `\widehat\Gamma_X`: banned in current manuscript notation.
- `\Gamma_{\mathrm{ind}}` as compact Hall charge support.
- `\Gamma_{\mathrm{eff}}` as compact Hall support.
- `\Pi_X` for the corrected additive map.
- `\Pi_{X,*}` or `\Pi_*` for the chain-level descent.
- `B` for `B_{\mathrm{ch}}`, `B_{\mathrm C}`, or `\bar B_E^{\mathrm{ch}}`.
- `\Theta` for `\Theta_\Pi` or `\Theta_{\mathrm{Kos}}` unless the local
  theorem has already fixed the notation.
- Bare `DX`.
- `D_X` for the virtual determinant.
- `D_X` for the first-order operator.
- `D_5` for the theta-normalized form.
- `\Delta_5` for the monic product.
- `\chi_{10}` without `^{\mathrm{OP}}` in the OP normalization section.
- `\Phi_{10}` as a synonym for `\chi_{10}^{\mathrm{OP}}`.
- `\Phi^{\mathrm{cmp}}_j=F_j`.
- `\Phi_j` as a row label; it is a scalar square object only after a row
  certificate.
- `Den_{\Delta_5,E}` without `\mathsf`.
- `Den_{\Delta_5,E}^{\mathrm{alg}}` unless a curve-universal algebraic
  target is formally defined.
- `Hpre`, `Htw`, `FXhyb`, `PRPi`, `DXR` in manuscript prose; use TeX
  superscripts/subscripts.
- Bare OP variables `q,p,\widetilde q` after the variable dictionary.
- Bare DT variables `q,t,p` after the variable dictionary.
- `m=d` and any phrase implying that the elliptic curve degree is literally
  the Borcherds exponent. The correct line is `m=d-1`.

## Residual consistency grep plan

Run these after the notation patch, not before, because several are expected
to hit current legacy text.

```bash
rg -n -F 'Gamma_X^{\mathrm{phys}}' main.tex
rg -n -F -e '\Gamma_{\mathrm{ind}}' -e '\Gamma_{\mathrm{eff}}' main.tex
rg -n -F -e '\Pi_X:' -e '\Pi_{X,*}' -e '\Pi_*' main.tex
rg -n -F -e '\overline\Pi_X' -e '\overline\Pi_{X,*}^{\Theta}' main.tex
rg -n -F -e 'B_{\mathrm{ch}}' -e 'B_{\mathrm C}' -e '\bar B_E^{\mathrm{ch}}' main.tex
rg -n -F -e '\mathcal D_X' -e '\mathfrak D_X' -e 'D_X' -e 'D_5' main.tex
rg -n -F -e '\chi_{10}' -e '\chi_{10}^{\mathrm{OP}}' -e '\Phi_{10}' main.tex
rg -n -F -e '\mathsf{Den}_{\Delta_5,E}' -e 'Denalg' -e 'Den^{\mathrm{alg}}' main.tex
rg -n -F -e 'Hpre' -e 'Htw' -e 'FXhyb' -e 'PRPi' -e 'DXR' main.tex
rg -n -F -e 'm=d' -e 'm = d' -e 'elliptic degree \(m' -e 'elliptic degree is \(m' main.tex
rg -n -F -e '\Phi^{\mathrm{cmp}}_5=F_5' -e '\Phi^{\mathrm{cmp}}_7=F_7' -e '\Phi^{\mathrm{cmp}}_8=F_8' main.tex
```

Expected interpretation:

- Hits for `\Gamma_X^{\mathrm{phys}}` are allowed only in explicit legacy
  warnings and old formula compatibility blocks.
- Hits for `\Gamma_{\mathrm{ind}}` are allowed only in automorphic/Fourier
  index sections, never as Hall support.
- Hits for `D_X` must be inspected one by one. Parenthesized certificate
  labels are acceptable; determinant/operator meanings are not.
- Hits for `\Phi^{\mathrm{cmp}}_j=F_j` must occur only in false-equality
  warning text, never as asserted identifications.
- No hit may imply `m=d`; the surviving language must say `m=d-1`.
