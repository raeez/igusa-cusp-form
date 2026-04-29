# Agent50 PBW/Radical/Kac-Presentation Latest Report

Scope: proposal-only PBW / radical / Kac-presentation adversary.  No source files edited.

Writable surface used: this report only.

Sources read:

- `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`, sha256 `d5b3f0dce64b3f979f3a0011c1e41250aba2ae67500af6e19edc791f3e0992d1`.
- Extracted text: `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`.
- `main.tex`, sha256 `fc0d8293ad0d08239122ce37e28a309ed6d4bc727f423333d15b8e236e290280`.
- Prior reports: `agent08_primitive_recognition_report.md`, `agent43_latest_theorem_spine_report.md`, `agent45_finite_source_certificate_latest_report.md`.
- Protocol: local `AGENTS.md`, `CLAUDE.md`, `.claude/commands/attack-heal-swarm-loop.md`, ecosystem invariants/harness.

## Executive Verdict

The latest PDF's \(UDI_R\) construction can honestly claim PBW, invariant form, radical quotient, primitive Lie bracket, and Gritsenko--Nikulin multiplicities only as target-side consequences of importing the Borcherds--Kac / Gritsenko--Nikulin denominator algebra.

It cannot honestly claim these as a new compact finite Hall--Dirac source.  The proposed \(UDI_R\) reuses the target algebra as the source:

\[
p_R=\bigoplus_{\gamma\in A_R}\mathfrak g_{\Delta_5,\gamma},\qquad
H_R=U(\mathfrak g_{\Delta_5})_{\le R},\qquad
P_R=p_R,
\]

with bracket, pairing, PBW basis, radical quotient, and multiplicities inherited from \(\mathfrak g_{\Delta_5}\).  That is a valid target reference tower.  It is circular if called the missing source object.

The current `main.tex` already has the correct firewall: the denominator algebra is target (`main.tex:5639-5783`), the formal current envelope is target-side and not compact BPS states (`main.tex:5788-5797`, `main.tex:5805-5849`), and primitive recognition requires independently supplied source data (`main.tex:12203-12218`, `main.tex:12268-12291`, `main.tex:12408-12486`, `main.tex:12682-12685`).

## Latest PDF Construction Attacked

The latest PDF says to construct a universal finite Dirac--Igusa Hall source \(UDI_R\) (`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:27848-27863`), with primitive bracket, orientation-gerbe states, source coalgebra, Pfaffian, PBW/radical tests (`:27861-27879`), and then make \(K3\times E\) geometry a realization functor into it (`:27923-27948`).

The actual algebraic core is:

- finite windows \(A_R\) in the Borcherds active support (`:28211-28293`);
- \(p_R=\bigoplus_{\gamma\in A_R}\mathfrak g_\gamma\), where \(\mathfrak g_{\Delta_5}\) is the GN denominator algebra (`:28295-28335`);
- bracket \([x,y]_R=[x,y]_{\mathfrak g_{\Delta_5}}\) (`:28350-28389`);
- pre-BKM presentation, then quotient by the radical of the invariant form (`:28391-28518`);
- \(H_R=U(\mathfrak g_{\Delta_5})_{\le R}\) as PBW truncation (`:28522-28576`);
- primitive subspace \(P_R=\{x:\Delta x=x\otimes1+1\otimes x\}=p_R\) by PBW (`:28629-28644`);
- radical compatibility built in by quotienting before forming \(U(\mathfrak g_{\Delta_5})\), so the universal-source radical is zero (`:28761-28777`, `:28931-28954`);
- central theorem: PBW, radical quotient, primitive bracket, and multiplicity formula hold by Kac/GN import (`:29622-29724`).

This is not a construction of compact Hall geometry.  It is the target algebra with a finite-window bookkeeping wrapper.

## Claim-Status Table

| Claim | Honest for \(UDI_R\)? | Status |
|---|---:|---|
| PBW basis | Yes, for \(U(\mathfrak g_{\Delta_5})\) or its finite PBW windows. | Imported target theorem / formal enveloping-algebra consequence.  Not evidence for compact source PBW. |
| Invariant form | Yes, for the Borcherds--Kac prequotient and its standard quotient. | Imported target structure.  Does not construct a Hall positive-negative Hopf pairing. |
| Radical quotient | Yes, if \(g_{\Delta_5}=g_{\Delta_5}^{pre}/\operatorname{Rad}\) is the definition. | Tautological after quotienting first.  It does not compute the compact source radical. |
| Primitive Lie bracket | Yes, as the BKM bracket of \(\mathfrak g_{\Delta_5}\); primitives of the standard enveloping Hopf algebra recover \(g\) in the target model. | Target bracket.  Not a Hall correspondence bracket. |
| GN multiplicities | Yes for visible signed supermultiplicities \(\operatorname{smult}=f(nm,l)\) on active support, and for whatever full parity data are fixed by the imported GN/Kac superdatum. | Product gives signed data; full parity dimensions are presentation-level target data, not determinant consequences. |

The dangerous sentence is not "PBW holds"; it is "therefore \(UDI_R\) is the missing source."  PBW holds because \(UDI_R\) was defined from \(U(\mathfrak g_{\Delta_5})\).  The compact source still has to map to this target with independent representatives, brackets, pairings, radicals, and PBW transition data.

## Circularity

The circular move is:

1. The manuscript needs a source primitive algebra \(P_X^{\Pi,\mathrm{red}}\) whose bracket, pairing, radical quotient, PBW filtration, and multiplicities can be compared to \(\mathfrak g_{\Delta_5}\).
2. The latest PDF defines the proposed finite source by setting its primitive piece equal to \(\mathfrak g_{\Delta_5}\) and its state object equal to \(U(\mathfrak g_{\Delta_5})_{\le R}\).
3. It then verifies PBW, radical quotient, bracket, and GN multiplicities by invoking the same \(\mathfrak g_{\Delta_5}\) presentation.

This proves only:

\[
\mathfrak g_{\Delta_5}\cong\mathfrak g_{\Delta_5}.
\]

It does not prove:

\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}.
\]

The latter is exactly the primitive recognition problem.  `main.tex` states this correctly: the target-side presentation
\[
G(\mathscr B_{\Delta_5})
=\widehat{\mathfrak F}(\mathscr B_{\Delta_5})/
\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}}
=\mathfrak g_{\Delta_5}
\]
is imported and "not a compact Hall construction" (`main.tex:12222-12266`).  The compact source assumptions begin only after this firewall (`main.tex:12268-12291`).

The same problem occurs for the Pfaffian claim.  The PDF promotes the already imported Borcherds product equality to the Pfaffian of \(UDI\) (`materials/processed/...revision-1923.txt:29507-29515`, `:29721-29732`).  If the Dirac block is manufactured so that its super-Pfaffian is
\[
\prod_\gamma (1-x^\gamma)^{\operatorname{sdim}\mathfrak g_\gamma},
\]
then \(\operatorname{Pf}(UDI)=\Delta_5\) restates the Borcherds product.  It is a target reference determinant, not a compact Dirac/Pfaffian theorem.

## Minimal Honest Definitions

The following can be defined now.

**Definition: Borcherds--Kac target datum.**  Keep the current imported datum \(\mathscr B_{\Delta_5}\), relation ideal \(J_{\mathrm{BK}}\), standard invariant pairing, radical \(\operatorname{Rad}_{\mathrm{GN}}\), and quotient
\[
G(\mathscr B_{\Delta_5})=\mathfrak g_{\Delta_5}.
\]
This is already present at `main.tex:12222-12266`, with denominator identity at `main.tex:5693-5783`.

**Definition: finite target reference tower.**  For a downward-saturated finite active set \(A_R\), define
\[
\mathfrak g_R^{\mathrm{tar}}
=\bigoplus_{\gamma\in A_R}\mathfrak g_{\Delta_5,\gamma},
\qquad
U_R^{\mathrm{tar}}
=\operatorname{span}\{ \hbox{PBW monomials of total degree in }A_R\}.
\]
If a linear lift \(s_L:\Gamma_{\mathrm{gram}}\to\widehat\Gamma_X\) is used, say it is bookkeeping for target labels, not a geometric charge lift.

**Definition: target reference Hopf tower.**  Multiplication and coproduct are inherited from \(U(\mathfrak g_{\Delta_5})\), with maps
\[
U_R^{\mathrm{tar}}\otimes U_{R'}^{\mathrm{tar}}\to U_{R+R'}^{\mathrm{tar}}.
\]
Fixed finite windows are not closed Hopf algebras; the tower carries the structure.

**Definition: realization functor.**  A compact \(K3\times E\) realization is a system
\[
R_{X,R}:H_{X,R}^{\mathrm{geom}}\to U_R^{\mathrm{tar}}
\]
preserving degrees, extension correspondences, coproducts, orientations, primitive representatives, pairings, radical kernels, PBW filtrations, source coalgebras, and Pfaffian lines.  This remains an open/conditional theorem until \(H_{X,R}^{\mathrm{geom}}\) and the finite matrices exist.

Do not call \(U_R^{\mathrm{tar}}\) a Hall source.  The safe names are "Borcherds--Kac target reference tower", "target PBW tower", or "universal target model."  The unsafe names are "universal compact source", "finite Hall--Dirac source", and "constructed compact source object."

## Minimal Honest Theorems

The following theorem can go into `main.tex` now, if desired, as a target-side theorem.

**Theorem: finite Borcherds--Kac target reference tower.**  Let \(A_R\) be a finite downward-saturated active window and let \(U_R^{\mathrm{tar}}\) be the PBW span inside \(U(\mathfrak g_{\Delta_5})\).  Then:

1. the primitive target space is \(\mathfrak g_R^{\mathrm{tar}}\);
2. the bracket is the Borcherds--Kac bracket;
3. the standard invariant form is inherited from the Borcherds--Kac presentation;
4. the radical has already been quotiented in \(\mathfrak g_{\Delta_5}\); in the prequotient it is the standard invariant-form radical;
5. PBW monomials give the target finite-window basis;
6. the visible signed multiplicities are \(f(nm,l)\) on active support.

Proof: Kac PBW plus the imported Borcherds/Gritsenko--Nikulin denominator algebra identity.  The proof must end with: "This constructs no compact Hall source and proves no primitive recognition theorem."

The following theorem cannot go into `main.tex` as proved:

**False if stated now:** \(UDI_R\) is the compact finite Hall--Dirac source whose PBW, radical quotient, primitive bracket, and GN multiplicities solve the Dirac--Igusa realization problem.

The proof would be circular because \(UDI_R\) is defined from \(\mathfrak g_{\Delta_5}\).

## What Can Go Into `main.tex` Now

Safe insertions:

- A compact target reference subsection immediately after `main.tex:5849`.
- Rename \(UDI_R\) to something like \(\mathsf{BKRef}_{R,L}\), \(\mathsf{TDI}_{R,L}\), or \(\mathsf{DenRef}_{R,L}\).
- State finite windows, PBW target spans, multiplication-to-larger-window maps, primitive target bracket, standard invariant form, and target radical quotient.
- State that this target reference model is the object a geometric source must realize.
- State that \(K3\times E\) geometry remains a realization problem:
  \[
  H_{X,R}^{\mathrm{geom}}\longrightarrow \mathsf{BKRef}_{R,L}.
  \]
- Keep the existing primitive-recognition certificate theorem as the source-side theorem (`main.tex:12222-12575`) and finite-window certificate (`main.tex:12577-12729`).

Unsafe insertions:

- "universal finite Hall--Dirac source" for an object defined as \(U(\mathfrak g_{\Delta_5})_{\le R}\);
- "constructed finite compact source object" without geometric Hall correspondences;
- "NO1--NO7 now actual finite source checks" when they are target tautologies;
- "orientation-gerbe-first twisted states" if the orientation gerbe is trivialized by finite algebraic design rather than computed from compact determinant lines;
- "source coalgebra" if it is the bar coalgebra of the target/artificial hybrid object;
- "Pfaffian of the compact source equals \(\Delta_5\)" when the Pfaffian is manufactured from target signed multiplicities.

## Recommended Main-Text Wording

Use:

> The Borcherds--Kac presentation gives a finite-window target reference tower.  It has PBW bases, the standard invariant form, the standard radical quotient, the target primitive bracket, and the Gritsenko--Nikulin signed multiplicities by construction.  This tower is not a compact Hall source.  A Dirac--Igusa realization is a source-side functor into this target tower preserving the Hall product, coproduct, orientation data, primitive representatives, Hopf pairing, radical kernels, PBW filtration, and Pfaffian line.

Do not use:

> We construct the missing compact finite Hall--Dirac source \(UDI_R\) by taking \(H_R=U(\mathfrak g_{\Delta_5})_{\le R}\).

That sentence is the circularity.

## Remaining Open Obligation

The hard theorem is unchanged:

\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}
\]

must be proved from independent compact source data: representatives, protected Hall bracket constants, positive-negative Hopf pairing matrices, radical kernels, no-extra-relations, PBW finite-window comparison, exact completion, and full parity dimensions.  The current `main.tex` states precisely this requirement at `main.tex:12408-12486` and `main.tex:12620-12685`.

Claim-status recommendation: import the Borcherds--Kac presentation as target reference data; quarantine \(UDI_R\) language unless renamed and demoted to a target reference tower.
