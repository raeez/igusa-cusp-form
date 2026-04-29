# Agent 35: D6 Degree-Shift Audit

Scope: hostile audit of the D6--D2--D0/Mukai dictionary and every downstream
degree convention that can shift an exponent by one. Sources mined: current
`main.tex`, `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`,
and reports `agent14_d6_d2_d0_descent_report.md`,
`agent24_notation_consistency_report.md`, and
`agent27_wle3_first_timelike_report.md`.

No source edits were made.

## Stable D6 theorem

Status: the mathematical content of the D6--D2--D0 local dictionary is stable.
Its manuscript label and surrounding notation are not yet stable enough.

The repaired statement is:
\[
X=S\times E,\qquad [Y]=(\beta,d),\qquad \chi(\mathcal O_Y)=n,
\]
with \(S\) a K3 surface, \(E\) an elliptic curve, and \(Y\subset X\) a
one-dimensional subscheme. For the ideal sheaf \(\mathcal I_Y\),
\[
v_X(\mathcal I_Y)
=\ch(\mathcal I_Y)\sqrt{\td(X)}
=(1,0,1-d)\otimes 1_E+(0,-\beta,-n)\otimes\omega_E.
\]
Set
\[
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n).
\]
With the K3 Mukai pairing
\[
(r,D,s)\cdot(r',D',s')=D\cdot D'-rs'-r's,
\]
one gets
\[
\left(\frac{Q_Y^2}{2},Q_Y\cdot P_Y,\frac{P_Y^2}{2}\right)
=\left(\frac{\beta^2}{2},n,d-1\right).
\]
For \(\beta=\beta_h=s_1+hF\), \(\beta_h^2=2h-2\), hence
\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
\]

This is the theorem-level bridge from OP/DT rank-one variables to
Borcherds/Gram exponents. It is not a compact Hall construction, not a
microscopic D-brane Hilbert space, and not an orientation statement.

Evidence:

- `main.tex:2661-2750` now proves the CY3 Mukai computation and removes the
  old "fourfold" and "Todd correction" errors attacked at
  `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:4847-4956`
  and `6013-6094`.
- `main.tex:2697-2731` fixes the Todd factor explicitly:
  \(\sqrt{\td(X)}=\pi_S^*(1,0,1)\cup1\), \(\sqrt{\td(E)}=1\).
- `main.tex:2760-2799` correctly keeps the reduced quotient integration
  scalar: no Hall product, no CoHA integration, no orientation character.
- Agent 14 independently records the same stable computation and remaining
  wording bugs at
  `notes/attack_whitepaper_analysis_20260429/agent14_d6_d2_d0_descent_report.md:7-23`
  and `58-67`.

Required status upgrade: promote `lemma` at `main.tex:2661` to a theorem. The
proof is already theorem-grade. Leaving it as a side lemma misplaces the
load-bearing dictionary.

## Degree/variable ledger

Use this ledger as the only safe dictionary.

| Concept | Geometry / source | Borcherds / Gram | OP variable | DT variable |
|---|---|---|---|---|
| K3 curve parameter | \(\beta_h^2=2h-2\) | first Gram coordinate \(N=h-1=Q^2/2\) | \(q_{\mathrm{OP}}^{h-1}\) | \(t_{\mathrm{DT}}^{h-1}\) |
| D0 / Euler index | \(n_0:=\chi(\mathcal O_Y)\) | middle coordinate \(L=n_0=Q\cdot P\) | \(p_{\mathrm{OP}}^{n_0}\) after \(p_{\mathrm{OP}}=e^{iu}\) convention | \((-p_{\mathrm{DT}})^{n_0}\) |
| elliptic curve degree | \(d=\deg(p_E)_*[Y]\) | third coordinate \(M=d-1=P^2/2\) | \(\widetilde q_{\mathrm{OP}}^{d-1}\) | \(q_{\mathrm{DT}}^{d-1}\) |
| Borcherds monomial | not additive Hall charge | \((N,L,M)\in\Gamma_{\mathrm{gram}}\) | identified by variable map | identified by variable map |
| BKM root | target-side only | \(\alpha(N,L,M)=2Nf_2-Lf_3+2Mf_{-2}\) | none | none |
| hybrid support degree | geometric wrapped support | should be separate from \(M\) | none | none |
| hybrid trace exponent | normal-ordered Gram exponent | \(M=\operatorname{pr}_3\overline\Pi_X(\gamma)\) | none | none |

Safe variable line:
\[
q_{\mathrm{Bch}}^{N}r_{\mathrm{Bch}}^{L}s_{\mathrm{Bch}}^{M}
=q_{\mathrm{OP}}^{h-1}p_{\mathrm{OP}}^{n_0}\widetilde q_{\mathrm{OP}}^{d-1}
=t_{\mathrm{DT}}^{h-1}(-p_{\mathrm{DT}})^{n_0}q_{\mathrm{DT}}^{d-1}
\]
with \(N=h-1\), \(L=n_0\), \(M=d-1\), and with the DT minus sign understood
as the DT/stable-pairs convention, not as an orientation sign.

The current theorem uses uppercase \(P,Q,T\) at `main.tex:13810-13819`.
This is arithmetically consistent with the OP/DT map, but it collides with
the Mukai magnetic vector \(P_Y\). In rewrite prose, keep variables
subscripted:
\[
q_{\mathrm{Bch}}=q_{\mathrm{OP}}=t_{\mathrm{DT}},\qquad
r_{\mathrm{Bch}}=p_{\mathrm{OP}}=p_{\mathrm{DT}},\qquad
s_{\mathrm{Bch}}=\widetilde q_{\mathrm{OP}}=q_{\mathrm{DT}}.
\]

The normal-ordered lattice ledger remains:
\[
\Gamma_X^{\mathrm{form}}=\Lambda_S\oplus\Lambda_S,\qquad
\Pi_X(Q,P)=\left(\frac{Q^2}{2},Q\cdot P,\frac{P^2}{2}\right),
\]
\[
B(c,c')=(Q\cdot Q',Q\cdot P'+Q'\cdot P,P\cdot P'),
\]
\[
\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T.
\]
The raw triple is a Gram shadow. It is not the additive Hall support.

## Drift/bug inventory

1. The D6 dictionary is still typed as a `lemma`.
   The attack source explicitly asks for a central theorem
   (`materials/processed/...txt:4956`, `6093-6094`, `21104-21164`).
   Current content at `main.tex:2661-2750` is repaired; the theorem status is
   not.

2. The theorem statement uses \(\Lambda_S=H^*(S,\mathbb Z)\) before the
   Mukai pairing is defined, then later sections use
   \(\widetilde H(S,\mathbb Z)\). The statement should define
   \(\widetilde H(S,\mathbb Z)\) and the pairing before the Gram formula.
   Anchors: `main.tex:2671-2674`, `2733-2736`, `4491-4499`.

3. The manuscript still uses \(n\) for two different things in close
   succession: D0/Euler \(n=\chi(\mathcal O_Y)\), and Borcherds first
   coordinate \(n=Q^2/2\). This is survivable in global notation but unsafe
   inside the D6 rewrite. Use \(n_0\) for D0/Euler and \(N\) for the first
   Gram coordinate whenever both appear.

4. The OP table says "elliptic degree \(d-1\)" at `main.tex:13719`. That is
   imprecise. The elliptic degree is \(d\). The Borcherds/Gram exponent
   attached to that degree is \(d-1\).

5. The hybrid source conflates geometric wrapped degree and Gram exponent.
   At `main.tex:7048-7055`, \(b(A)\) and \(b(\gamma)\) are literal
   elliptic degrees:
   \[
   b(A)=\deg(p_E)_*[\operatorname{Supp}_1A].
   \]
   At `main.tex:7683-7697`, the same symbol is used as the \(s\)-exponent
   and then declared to be \(m=b_R(\gamma)\). These cannot both be true in
   the rank-one D6 branch, where \(m=d-1\).

6. The same bug appears in the abstract, introduction, synthesis theorem,
   and certificate prose:
   `main.tex:249-254`, `500-518`, `7112-7118`, `7732-7735`,
   `8010-8017`, `8061-8064`, `11845-11848`, `14155-14163`.
   Every occurrence of "trace degree \(s^{b_R}\)" is wrong or undefined until
   \(b_R\) is declared to be the Gram exponent rather than geometric degree.

7. The \(\delta_2\) wrapped-wall statements inherit the same off-by-one risk.
   The manuscript writes
   \[
   b_R(\eta)=1,\qquad \overline\Pi_X(\eta)=(0,1,1)
   \]
   at `main.tex:1600-1602`, `6172-6178`, `8192-8194`, and
   `10960-10963`. If \(b_R\) is geometric degree, this says \(d=1\) while
   the Gram exponent says \(m=1\), hence \(d=2\) in the rank-one D6 branch.
   If \(b_R\) is the Gram exponent, it must not be called the elliptic degree.

8. The phrase "positive elliptic degree" is repeatedly equated with positive
   \(s\)-power. Under the D6 dictionary, positive geometric degree \(d=1\)
   gives \(m=0\), not a positive \(s\)-power. Positive \(s\)-power means
   \(m>0\), hence \(d\ge2\) in the rank-one D6 branch. Projection-to-\(E\)
   support locality uses \(d>0\), not \(m>0\). These are distinct tests.

9. Product additivity is stated for \(b_R\) at `main.tex:7167-7171` and then
   used for \(s^{b_R}\) at `main.tex:7704-7710`. If \(b_R=d\), this is
   support-degree additivity but not the D6 Borcherds exponent. If
   \(b_R=m\), it is normal-ordered Gram additivity but not literal geometric
   degree. The manuscript must choose two symbols, not one overloaded symbol.

10. The OP/DT theorem's uppercase \(P,Q,T\) convention at
    `main.tex:13810-13819` is a notational trap because \(P_Y\) is already a
    Mukai vector in the D6 theorem. It should be subordinated to the
    subscripted variable table.

11. Agent 24's warning is correct and should be absorbed: `m=d` and every
    phrase implying "elliptic degree is the Borcherds exponent" must be
    banned. See
    `notes/attack_whitepaper_analysis_20260429/agent24_notation_consistency_report.md:136-143`
    and `390-418`.

12. Agent 27's first timelike audit strengthens the warning: the target
    degree \((1,1,1)\) and \(\delta_2=(0,1,1)\) are target/Gram data. They
    do not by themselves construct a compact source object with a specified
    geometric elliptic degree. See
    `notes/attack_whitepaper_analysis_20260429/agent27_wle3_first_timelike_report.md:30-64`
    and `118-139`.

## Required rewrite language

Use this language, or something formally equivalent.

1. Central theorem header:

```tex
\begin{theorem}[D6--D2--D0 Mukai--Gram dictionary]
\label{thm:d6-d2-d0-mukai-gram-dictionary}
...
\end{theorem}
```

2. Pairing-first setup:

```tex
Let \(\widetilde H(S,\mathbb Z)=H^0(S,\mathbb Z)\oplus H^2(S,\mathbb Z)
\oplus H^4(S,\mathbb Z)\) carry the Mukai pairing
\[
(r,D,s)\cdot(r',D',s')=D\cdot D'-rs'-r's.
\]
```

3. Variable firewall near the D6 theorem and the OP table:

```tex
In the rank-one D6--D2--D0 branch we write
\[
n_0:=\chi(\mathcal O_Y),\qquad
N:=h-1,\qquad L:=n_0,\qquad M:=d-1.
\]
Thus the geometric elliptic degree is \(d\), while the Borcherds third
Gram exponent is \(M=d-1\). The shift is forced by
\(P_Y=(1,0,1-d)\), equivalently by the rank-one D6/Todd contribution in
the Mukai vector.
```

4. OP/DT/Borcherds table language:

```tex
\[
q_{\mathrm{Bch}}=q_{\mathrm{OP}}=t_{\mathrm{DT}},\qquad
r_{\mathrm{Bch}}=p_{\mathrm{OP}}=p_{\mathrm{DT}},\qquad
s_{\mathrm{Bch}}=\widetilde q_{\mathrm{OP}}=q_{\mathrm{DT}}.
\]
The DT expansion uses the convention \((-p_{\mathrm{DT}})^{n_0}\); this
minus sign is part of the scalar DT/PT convention, not an orientation
character.
```

5. Hybrid degree split:

```tex
The hybrid source uses two degree maps. The support map
\[
b_R^{\mathrm{geom}}(\gamma)=\deg(p_E)_*[\operatorname{Supp}_1\gamma]
\]
detects projection-finite versus wrapped sectors. The trace exponent is
\[
m_R(\gamma):=\operatorname{pr}_3\overline\Pi_X(\gamma).
\]
Protected integration is homogeneous as
\[
I_R^{\mathrm{prot}}(x)\in
s^{m_R(\gamma)}\mathbb C[q^{\pm1},r^{\pm1}].
\]
On the rank-one D6--D2--D0 ideal-sheaf branch, \(m_R=d_R-1\). Outside
that branch, any relation between \(m_R\) and geometric degree is part of
the finite source certificate.
```

6. \(\delta_2\) correction:

```tex
For the middle wall \(\delta_2\leftrightarrow(0,1,1)\), the finite source
must contain a wrapped object \(\eta\) with
\[
m_R(\eta)=1,\qquad b_R^{\mathrm{geom}}(\eta)>0,\qquad
\overline\Pi_X(\eta)=(0,1,1).
\]
Do not write \(b_R(\eta)=1\) unless \(b_R\) has been explicitly redefined
as the Gram exponent. In the rank-one D6--D2--D0 branch this Gram exponent
would correspond to geometric elliptic degree \(d=2\).
```

7. Support-locality language:

```tex
Positive geometric elliptic degree \(b_R^{\mathrm{geom}}>0\) is the
projection-to-\(E\) support-locality obstruction. Positive \(s\)-power is
the separate condition \(m_R>0\). In the rank-one D6 branch these differ
by the shift \(m_R=d_R-1\).
```

## main.tex anchors

- Abstract determinant and scalar-square separation: `main.tex:57-129`.
- Abstract raw/corrected Gram split: `main.tex:131-154`.
- Early hybrid language carrying `s^{b_R}` hazard: `main.tex:226-258`.
- Projection-to-\(E\) locality language carrying "s-degree is elliptic degree"
  hazard: `main.tex:500-518`.
- D6--D2--D0 dictionary: `main.tex:2634-2758`.
- Reduced scalar quotient and protected D-brane conjecture:
  `main.tex:2760-2845`.
- Formal Mukai lattice, raw Gram map, and normal-ordered extension:
  `main.tex:4316-4382`, `4590-4809`, `4832-4881`.
- Raw fixed-lift no-go theorem: `main.tex:4883-4975`.
- Hybrid geometric degree definition: `main.tex:7039-7080`.
- Hybrid protected integration using `s^{b_R}` and `m=b_R`:
  `main.tex:7636-7712`, especially `7683-7697`.
- Hybrid coefficient statement: `main.tex:7730-7736`.
- Hybrid source proposition repeating `s^{b_R}`: `main.tex:7972-8027`.
- Quotient/Fock warning repeating trace degree `s^{b_R}`:
  `main.tex:8058-8064`.
- \(\delta_2\) wall table and wrapped object requirement:
  `main.tex:8083-8252`.
- First wrapped primitive source test:
  `main.tex:10948-10991`.
- Five-part realization certificate repeating elliptic-degree `b_R` as
  homogeneous `s`-degree: `main.tex:11821-11848`.
- OP/DT variable table and scalar square:
  `main.tex:13709-13830`.
- Constants and OP sign firewall: `main.tex:13857-13954`.
- Coefficient dictionary synthesis, including `s^{b_R}` in the compact
  realization consequences: `main.tex:13957-14265`.

Prior reports:

- Agent 14 D6 repair and residual shift warning:
  `notes/attack_whitepaper_analysis_20260429/agent14_d6_d2_d0_descent_report.md:7-23`,
  `58-67`, `191-199`.
- Agent 24 notation ledger and `m=d-1` warning:
  `notes/attack_whitepaper_analysis_20260429/agent24_notation_consistency_report.md:1-143`,
  `390-418`.
- Agent 27 target/source firewall for first timelike and \(\delta_2\):
  `notes/attack_whitepaper_analysis_20260429/agent27_wle3_first_timelike_report.md:30-64`,
  `118-139`, `174-221`.

## Patch queue

P0. Promote `main.tex:2661` from lemma to theorem and rename references:
`D6--D2--D0 Mukai--Gram dictionary`.

P0. In the theorem statement, define \(\widetilde H(S,\mathbb Z)\) and the
Mukai pairing before defining \(P_Y,Q_Y\) and the Gram triple.

P0. Introduce \(n_0\) for \(\chi(\mathcal O_Y)\), \(N=h-1\), \(L=n_0\),
\(M=d-1\). Use these names in the D6 theorem and OP variable table wherever
both D0 \(n_0\) and Borcherds first coordinate \(N\) occur.

P0. Split hybrid degree notation:
`b_R^{\mathrm{geom}}` for projection-to-\(E\) support degree, and
`m_R=\operatorname{pr}_3\overline\Pi_X` for the \(s\)-exponent. Rewrite all
`s^{b_R}` occurrences to `s^{m_R}` unless the surrounding definition
explicitly redefines \(b_R\) as a Gram exponent.

P0. Repair every \(\delta_2\) line from `b_R(...)=1` to
`m_R(...)=1` plus `b_R^{\mathrm{geom}}(... )>0`. If a rank-one D6 source is
claimed, add the consequence \(d=2\).

P0. Replace "positive elliptic degree supplies positive \(s\)-direction" by
the two-condition statement: \(b_R^{\mathrm{geom}}>0\) supplies wrapped
support; \(m_R>0\) supplies positive \(s\)-power.

P1. Consolidate OP/DT/Borcherds variables into one table. Delete or
cross-reference repeated dictionaries. Subscript all OP, DT, and Borcherds
variables in prose.

P1. Retire uppercase \(P,Q,T\) in the theorem statement or isolate them in a
single display with a warning that \(P\) is not the Mukai vector \(P_Y\).

P1. Add a boundary sentence: in the rank-one D6 branch \(d=0\) maps to
\(m=-1\), and \(d=1\) maps to \(m=0\). These are not positive \(s\)-power
sectors even though \(d=1\) is geometrically wrapped.

P1. Keep \(\Gamma_X^{\mathrm{phys}}\) only inside explicit legacy warnings.
Use \(\Gamma_X^{\mathrm{form}}\) in new degree prose.

P2. Add macros for fragile degree symbols:
`\nDzero` or `\nEuler`, `\Ngram`, `\Lgram`, `\Mgr`, `\bgeomR`, `\mgramR`,
`\qBch`, `\rBch`, `\sBch`. This is mechanical but will stop future drift.

## Residual checks

Run these after the patch set.

```bash
rg -n -F -e 's^{b_R}' -e 's^{\,b_R' -e 'trace degree \(s^{b_R}' main.tex
rg -n -F -e 'elliptic degree \(m' -e 'elliptic degree is \(m' -e 'm=b_R' main.tex
rg -n -F -e 'b_R(\eta)=1' -e 'b_R(\delta_2)=1' -e 'b_R(\\eta_2)=1' main.tex
rg -n -F -e 'elliptic degree \(d-1\)' -e 'elliptic-degree \(d-1\)' main.tex
rg -n -F -e 'positive elliptic degree' -e 'positive \(s\)-direction' main.tex
rg -n -F -e 'q_{\mathrm{DT}}^{d-1}' -e '\widetilde q_{\mathrm{OP}}^{d-1}' main.tex
rg -n -F -e 'p=P=e^{iu}' -e 't=Q' -e 'q=T' main.tex
rg -n -F -e '\Gamma_X^{\mathrm{phys}}' main.tex
```

Expected post-patch interpretation:

- No surviving hit may use `s^{b_R}` unless \(b_R\) is explicitly the Gram
  exponent in that local paragraph.
- No surviving hit may state or imply `m=d`; the rank-one D6 branch must say
  \(m=d-1\).
- Hits for `positive elliptic degree` must concern support locality only.
  Hits for positive \(s\)-power must use \(m_R>0\).
- Every \(\delta_2\) source requirement must ask for
  \(m_R=1\) and wrapped support, not unqualified geometric degree one.
- OP/DT variables must remain subscripted, and the DT \((-p)^n\) minus must
  stay separate from orientation.
- `\Gamma_X^{\mathrm{phys}}` may survive only where the sentence says it is a
  legacy mnemonic for \(\Gamma_X^{\mathrm{form}}\).

Residual mathematical check after the notation patch: verify that the D6
rank-one branch, the hybrid source certificate, and the \(\delta_2\) wall can
all be read simultaneously without forcing \(d=1\) and \(m=1\) for the same
object. If that contradiction remains, the source rewrite is still corrupt.
