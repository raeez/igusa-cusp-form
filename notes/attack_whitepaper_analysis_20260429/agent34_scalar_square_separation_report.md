# Agent 34 scalar-square separation report

Date: 2026-04-29

Scope: scalar-square separation in the live manuscript, with attack PDF
material mined through `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`
and cross-checks against Agent 04, Agent 14, Agent 20, Agent 23, and
Agent 28. No source files were edited.

Verdict: the stable theorem is narrow and safe:
Oberdieck--Pixton/Oberdieck--Pandharipande/Oberdieck prove an imported
reduced scalar identity in a specified OP/DT chamber. After the paper's
theta normalization, that identity is
```tex
Z^X_{\mathrm{DT}}(T,Q,P)=Z^X_{\mathrm{OP}}(P,Q,T)
=-4096\,\Delta_5(Z)^{-2}.
```
It is a second-order, orientation-forgetting scalar theorem. It does not
construct a Pfaffian line, a compact Hall source, a first-order operator,
or the character identity `\epsilon_o=\nu_{\Delta_5}`.

## Stable scalar theorem

The theorem should be presented exactly as an imported scalar theorem,
not as an orientation theorem:

```tex
\begin{theorem}[Reduced DT/PT/OP scalar square]
Let \(\beta_h\in H_2(S,\mathbb Z)\) be primitive and non-zero, with
\(\langle\beta_h,\beta_h\rangle=2h-2\).  In the OP chamber and under
the variable map
\[
p=P=e^{iu},\qquad t=Q,\qquad q=T,\qquad
(q_{\mathrm{Bch}},r_{\mathrm{Bch}},s_{\mathrm{Bch}})=(Q,P,T),
\]
one has the equality of Laurent expansions
\[
Z^X_{\mathrm{DT}}(T,Q,P)=Z^X_{\mathrm{OP}}(P,Q,T)
=-4096\,\Delta_5(Z)^{-2}.
\]
\end{theorem}
```

Status:

- `Imported theorem`: the scalar branch comes from OB + OPand + Oberdieck
  reduced PT, with the manuscript only fixing variables, chamber, and the
  `D_5` versus `\Delta_5` normalization.
- `Not constructed`: no compact source category, no CoHA integration map,
  no protected primitive bracket, no Pfaffian line, no Weyl orientation
  lift, no `\mathfrak D_X`.
- `Correct current anchor`: `main.tex:13806-13855`.

Source chain:

- OB: primitive reduced OP/GW branch and
  `Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}`;
  current use at `main.tex:13762-13804`, `13852-13854`; bib at
  `proj.bib:249-260`.
- OPand: variable convention and primitive GW/PT comparison; current use
  at `main.tex:13769-13783`, `13843-13849`; bib at `proj.bib:262-275`.
- Oberdieck reduced PT: quotient Behrend-weighted reduced theory and
  DT/PT comparison for nonzero K3 class; current use at
  `main.tex:2760-2799`, `13833-13842`; bib at `proj.bib:277-288`.

The attack PDF's core demand is already the right one:
OP sees `D_5^2`, not `D_5`; therefore it confirms only the reduced scalar
square and supplies no square-root orientation
(`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:390-442`,
`5665-5687`).

## Normalization chain

Use one chain, and do not skip any link:

1. K3 elliptic genus:
   ```tex
   Z_{\mathrm{K3}}=2\phi_{0,1},\qquad
   \phi_{0,1}=\sum f(n,l)q^nr^l.
   ```
   The Borcherds half-product uses `f(nm,l)`, not `2f(nm,l)`.
   Current anchors: `main.tex:57-81`, `722-740`, `13793-13801`.

2. Theta-normalized Igusa section:
   ```tex
   [q^{1/2}r^{1/2}s^{1/2}]\Delta_5=64.
   ```
   Current anchors: `main.tex:79-81`, `2420-2424`,
   `2537-2558`, `13924-13935`.

3. Monic Borcherds product:
   ```tex
   D_5=64^{-1}\Delta_5
   =q^{1/2}r^{1/2}s^{1/2}
    \prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}.
   ```
   Current anchors: `main.tex:2530-2558`, `2560-2599`,
   Agent 28 `notes/.../agent28_formal_pfaffian_normalization_report.md:37-44`.

4. BKM denominator normalization:
   ```tex
   \operatorname{den}(\mathfrak g_{\Delta_5})
   =D_5(2Z)=64^{-1}\Delta_5(2Z).
   ```
   The `2Z` belongs to the denominator-character convention
   `q^nr^ls^m=\exp(-\pi i(\alpha,z))` versus
   `\exp(-2\pi i(\alpha,z))`. Do not replace it by `D_5(Z)`.
   Current anchors: `main.tex:90-92`, `5368-5394`,
   `5614-5702`, Agent 28 lines 46-58.

5. OP scalar form:
   ```tex
   \chi_{10}^{\mathrm{OP}}=D_5^2
   =(64^{-1}\Delta_5)^2
   =4096^{-1}\Delta_5^2.
   ```
   Current anchors: `main.tex:117-125`, `13752-13759`,
   `14116-14124`; Agent 04 lines 29-45.

6. Scalar branch:
   ```tex
   Z^X_{\mathrm{OP}}
   =-(\chi_{10}^{\mathrm{OP}})^{-1}
   =-4096\,\Delta_5^{-2}.
   ```
   The decomposition is
   ```tex
   -4096=(-1)_{\mathrm{OP}}\cdot64^2.
   ```
   Here `64^2` is the squared theta-to-monic conversion. The leading
   minus is the OP scalar convention. Neither is an orientation sign,
   a Maass character, a degeneracy, an anomaly, or a Pfaffian datum.
   Current anchors: `main.tex:127-129`, `13868-13876`,
   `13937-13954`, Agent 04 lines 47-53.

Forbidden shorthand:

- Do not write `\chi_{10}^{\mathrm{OP}}=\Delta_5^2`.
- Do not write `-4096` as a source of `(-1)^F` or of
  `\epsilon_o`.
- Do not say OP proves a square root. OP proves a reciprocal scalar
  square after a normalization conversion.

## False implications

1. Scalar square to Pfaffian:
   ```tex
   Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}
   \not\Rightarrow
   \operatorname{Pf}_{\mathrm{prot}}(\mathfrak D_X)=\Delta_5.
   ```
   A scalar reciprocal square can be compatible with a supplied Pfaffian,
   but it cannot construct the Pfaffian line, skew form, section, or
   square map. Agent 28 lines 76-126 and 225-250 are the controlling
   negative statement.

2. OP minus to Hall orientation:
   ```tex
   (-1)_{\mathrm{OP}}
   \not\Rightarrow
   \epsilon_o:W^{(2)}(\Lambda^{2,1}_{II})\to\{\pm1\}.
   ```
   The OP minus is a scalar prefactor. `\epsilon_o` is a monodromy
   character. The attack PDF states the exact repair:
   "The OP scalar sign is a number; epsilon_o is a character"
   (`materials/processed/...txt:5131-5186`, `21084-21099`).

3. Maass character to Hall orientation:
   ```tex
   \nu_{\Delta_5}(s_{\delta_i})=-1
   \not\Rightarrow
   \epsilon_o(s_{\delta_i})=-1.
   ```
   `\nu_{\Delta_5}` is automorphic target data. The compact Hall
   character requires O1 quotient orientation, O1+ Weyl transport, and
   O2 local Pfaffian wall charts. Current anchors: `main.tex:5287-5338`,
   `1754-1784`, `14168-14179`.

4. `D_5^2` to `D_5`:
   OP's theorem sees `D_5^2`. It cannot select `D_5`, `-D_5`, or an
   orientation-lifted branch. The sign character is killed by squaring.

5. Reduced Behrend scalar integration to CoHA/Hall integration:
   Oberdieck's quotient theory lands in numbers coefficient by
   coefficient. It is not a Hall product, not a CoHA integration map,
   not a primitive projection, and not an orientation character.
   Current anchors: `main.tex:2760-2799`, `2817-2844`;
   Agent 14 lines 25-28.

6. Denominator/root supermultiplicity to compact source:
   `\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)`
   imports the GN target algebra. It does not construct compact BPS
   states, operator products, parity dimensions, primitive
   representatives, PBW data, or the Hopf radical. Current anchors:
   `main.tex:5560-5702`, `14087-14109`, `14180-14192`.

7. "Second-order trace" to constructed trace:
   The phrase is safe only as conditional language:
   if a compact Dirac--Igusa first-order object is supplied, then its
   orientation-forgetting second-order scalar shadow is required to match
   the OP branch. It is unsafe if it reads as an actually constructed
   trace on an actually constructed `\mathfrak D_X`.

## Required rewrite language

Use these exact or near-exact sentences.

1. Stable OP theorem:
   "The OP/Oberdieck theorem is imported here only as a reduced scalar
   identity. In the OP chamber and under the stated variable map it gives
   \(Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}=-4096\Delta_5^{-2}\). It does not
   construct a Hall source, a Pfaffian line, or an orientation character."

2. Normalization:
   "The constant \(64\) is the theta-leading coefficient of the
   theta-normalized Igusa section. OP uses the monic product
   \(D_5=64^{-1}\Delta_5\), hence
   \(\chi_{10}^{\mathrm{OP}}=D_5^2=4096^{-1}\Delta_5^2\). The leading
   minus in \(Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}\) is an
   OP scalar convention."

3. Second-order orientation-forgetting trace:
   "If a compact first-order Dirac--Igusa object is supplied, its
   orientation-forgetting scalar shadow should be the second-order trace
   \(C_{\square,X}\Delta_5^{-2}\); the imported OP theorem fixes the scalar
   normalization \(C_{\square,X}=-4096\) for the reduced OP/DT branch. The
   theorem does not supply the first-order object."

4. Pfaffian:
   "A scalar square is not square-rooted by choosing an analytic branch.
   In the Dirac sense it is square-rooted only by constructing a
   first-order protected algebra/Pfaffian object whose automorphic
   Pfaffian is \(\Delta_5\)."

5. Orientation:
   "The OP minus sign is a number. The orientation character is a
   monodromy character. The equality
   \(\epsilon_o=\nu_{\Delta_5}\) must be proved from orientation-line
   monodromy and type-II Pfaffian wall data, not from \(64\), \(4096\), or
   the OP scalar sign."

6. Boxed slogan requested by the attack PDF:
   "OP/DT proves the scalar square, not the first-order square root."

Avoid these sentences:

- "The OP scalar square gives the Pfaffian."
- "The OP minus supplies the orientation sign."
- "The scalar trace of \(\mathfrak D_X\) is \(-4096\Delta_5^{-2}\)" unless
  the sentence begins with "if \(\mathfrak D_X\) is supplied" or is inside
  a clearly conditional theorem.
- "Choosing the square root of \(\Delta_5^2\)" as the mathematical
  content of the paper.

## OP variable/chamber checks

Keep a single variable table. Use subscripts to prevent collision between
the D0 index `n` and the Borcherds first coordinate.

Safe dictionary:

| Role | Symbol | OP variable | DT variable | Borcherds variable |
|---|---:|---|---|---|
| K3 norm | `h-1=beta_h^2/2` | `q_OP` | `t_DT=Q` | `q_Bch=Q` |
| D0/Fourier index | `n=chi(O_Y)` | `p_OP=e^{iu}` | `p_DT=P`, with `(-P)^n` | `r_Bch=P` |
| Elliptic Gram exponent | `m=d-1` | `\tilde q_OP` | `q_DT=T` | `s_Bch=T` |

D6--D2--D0 check:

```tex
v_X(I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
```
```tex
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n),
```
```tex
\Pi_X(Q_Y,P_Y)
=\left(Q_Y^2/2,Q_Y\cdot P_Y,P_Y^2/2\right)
=\left(\beta^2/2,n,d-1\right).
```
For `\beta_h^2=2h-2`, this is `(h-1,n,d-1)`.
Current anchors: `main.tex:2661-2750`; Agent 14 lines 7-15 and
88-105; attack PDF lines `22400-22477`.

Chamber:

- Borcherds cusp completion:
  ```tex
  0<|s|\ll |q|\ll |r|^{-1}\ll1.
  ```
  Current anchors: `main.tex:650-665`, `766-769`.
- OP re-expansion:
  ```tex
  0<|\widetilde q_{\mathrm{OP}}|
  \ll |q_{\mathrm{OP}}|
  \ll |p_{\mathrm{OP}}|^{-1}\ll1,\qquad r=p_{\mathrm{OP}}.
  ```
  Current anchors: `main.tex:13737-13747`.
- OP product index set:
  ```tex
  h,d\ge0,\qquad h>0\ \mathrm{or}\ d>0,
  \qquad \mathrm{or}\qquad h=d=0,\ k<0.
  ```
  Current anchors: `main.tex:13732-13736`, `13786-13792`.

Checks required in any rewrite:

- State `m=d-1`, not `d`.
- State `n=chi(O_Y)`.
- State `h,d,n` are OP branch variables, not full microscopic charge
  coordinates.
- Keep the line "Only the OP/DT scalar branch requires an elliptically
  fibered K3 surface with a section; the Borcherds determinant uses only
  the universal K3 elliptic genus" (`main.tex:2634-2638`).
- Do not repeat the variable dictionary in multiple forms. Agent 14
  flags this as a remaining hazard at lines 66-67 and 191-195.

## main.tex anchors

Core safe anchors:

- Abstract scalar/orientation separation: `main.tex:100-129`.
- K3 half-index and `K_0` virtuality: `main.tex:667-740`.
- Fock trace and superdeterminant: `main.tex:743-769`.
- Normalized determinant package: `main.tex:818-823`.
- Dirac/Pfaffian target presently over-labeled as a proposition:
  `main.tex:882-918`.
- Conditional scalar trace step: `main.tex:1729-1752`.
- Theta normalization and Maass character: `main.tex:2383-2424`.
- Orientation line explicitly not constructed: `main.tex:2472-2507`.
- BGN product normalization: `main.tex:2530-2558`.
- Normalization chain table: `main.tex:2560-2599`.
- D6--D2--D0 Mukai--Gram dictionary: `main.tex:2661-2750`.
- Reduced scalar quotient integration: `main.tex:2760-2799`.
- Protected Hall integration criterion: `main.tex:2817-2844`.
- Maass multiplier restriction: `main.tex:5287-5338`.
- Denominator algebra identity: `main.tex:5560-5702`.
- OP variable table and normalization: `main.tex:13714-13804`.
- Reduced scalar theorem: `main.tex:13806-13855`.
- OP normalization branch and constant: `main.tex:13857-13883`.
- Square-root consequence: `main.tex:13885-13922`.
- Constants are not orientation data: `main.tex:13924-13955`.
- Coefficient dictionary / claim-strength synthesis: `main.tex:14031-14265`.

Prior report anchors:

- Agent 04: imported OP/Oberdieck chain and forbidden implications,
  `notes/attack_whitepaper_analysis_20260429/agent04_op_dt_scalar_report.md:7-53`,
  `57-91`, `121-137`.
- Agent 14: D6--D2--D0 dictionary and variable shift,
  `notes/attack_whitepaper_analysis_20260429/agent14_d6_d2_d0_descent_report.md:7-15`,
  `56-68`, `189-195`.
- Agent 20: source-role ledger and OP exact-source debt,
  `notes/attack_whitepaper_analysis_20260429/agent20_bibliography_primary_sources_report.md:17-18`,
  `61-62`, `83-100`, `144-155`.
- Agent 23: theorem-status taxonomy,
  `notes/attack_whitepaper_analysis_20260429/agent23_theorem_status_taxonomy_report.md:23-32`,
  `53-55`, `91-100`, `161-190`.
- Agent 28: formal Pfaffian normalization firewall,
  `notes/attack_whitepaper_analysis_20260429/agent28_formal_pfaffian_normalization_report.md:23-72`,
  `76-126`, `128-145`, `225-256`.

## Patch queue

1. Demote `main.tex:882-918`.
   Change `\begin{proposition}[Dirac/Pfaffian recognition target]` to a
   definition/open problem title such as
   `Open Dirac--Pfaffian first-order target; no operator constructed`.
   It names a missing object and proves no proposition. Agent 23 lines
   91-95 explicitly require this.

2. Rewrite abstract lines `100-107`.
   Current language is mostly safe, but the scalar trace display can still
   read as constructed. Replace with conditional grammar:
   "If such a supplied first-order object exists, its orientation-forgetting
   scalar shadow is required to match the OP/DT branch..."

3. Split the conditional Pfaffian theorem around `main.tex:1139` and
   `1729-1752`.
   Make Step 3 say: OP fixes the scalar normalization of the required
   second-order shadow; it does not create the trace, the Hilbert space,
   or the Pfaffian object. Agent 23 lines 96-100 require this split.

4. Rename `main.tex:13885` from `Square-root consequence`.
   Safer titles:
   `Scalar shadow after the fixed virtual determinant` or
   `Orientation-forgetting scalar consequence`.
   The current title invites the forbidden reading "OP constructs the
   square root."

5. Add the boxed sentence after `main.tex:13806-13855`:
   "OP/DT proves the scalar square, not the first-order square root."
   This directly answers the attack PDF at `materials/processed/...txt:5665-5687`.

6. Keep `main.tex:13924-13955`, but make the character sentence sharper:
   "The OP scalar sign is a number; \(\epsilon_o\) is a character."
   This is the precise attack-PDF repair at `materials/processed/...txt:21084-21099`.

7. Promote `main.tex:2661` from lemma to theorem and move the Mukai pairing
   before the displayed Gram triple. This is not scalar-square decoration;
   it is the bridge proving the OP variables are Mukai Gram variables.
   Agent 14 lines 56-73 and Agent 23 lines 105-114 require it.

8. Add a one-line variable warning near `main.tex:13714-13721`:
   "Here geometric elliptic degree is \(d\), Borcherds/Gram exponent is
   \(m=d-1\), and D0/Fourier index is \(n=\chi(\mathcal O_Y)\)."
   Then remove or harmonize any later duplicated variable dictionary.

9. Convert `main.tex:14031-14265` from theorem to theorem-status ledger,
   or split it into separate theorem statements plus a ledger. It currently
   packages determinant, normal-ordering, GN denominator, OP scalar, open
   compact realization, and row extension in one theorem environment.
   Agent 23 lines 148-150 require demotion/splitting.

10. Preserve the source firewall:
    every time OP/Oberdieck appears near Pfaffian, orientation, Hall,
    CoHA, primitive recognition, or compact source language, add the
    boundary phrase "scalar only" or "orientation-forgetful scalar branch."

11. Do not introduce `D^{alg}_{\Delta_5,C,L}` as compact or source-side.
    If it is added, follow Agent 28 lines 60-72 and 202-215: it is a
    target regrading/formal product package only, not `\mathfrak D_X`.

12. Do not edit `proj.bib` until the primary-source audit resolves OPand
    Proposition 5 versus the "proposition after Conjecture D" conflict
    noted by Agent 20 lines 41-42 and 154-155.

## Residual primary-source checks

Priority 0:

1. OB exact theorem check.
   Verify in Oberdieck--Pixton, Invent. Math. 213 (2018), arXiv:1706.10100:
   Theorem 1, equation (3), equation (56) if retained, the product index
   chamber, the variables `(p,q,\tilde q)`, and the sign
   `Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}`.

2. OPand exact comparison check.
   Resolve whether the current citation should be `Proposition 5`,
   Section 2, or the proposition after Conjecture D. Check the hypotheses:
   primitive `\beta_h`, elliptically fibered K3 with section, `P=e^{iu}`,
   and `y=-p_{\mathrm{OP}}`.

3. Oberdieck reduced PT check.
   Verify Theorem 1 and Theorem 3(i): quotient-by-`E` reduced
   stable-pair invariant, agreement with reduced virtual-class/incidence
   definition, nonzero K3-class hypothesis, and reduced DT/PT comparison.

4. Bryan convention check.
   Verify the `q/\tilde q` interchange, ordinary DT vanishing due to the
   `E` action, and the Hilbert-scheme normalization used at
   `main.tex:13779-13783` and `2789-2791`.

5. GN/GNII normalization check.
   Verify published theorem/equation anchors for
   `D_5=64^{-1}\Delta_5`, the `64^{-1}\Delta_5(2Z)` denominator, the
   `Z -> 2Z` convention, and the active multiplicities `f(nm,l)`.

6. Maass/GN character check.
   Verify the six reflection values at `main.tex:5287-5338`, but keep the
   result explicitly automorphic. It is not a Hall orientation proof.

Priority 1:

7. Negative-source audit.
   Confirm directly that OB, OPand, Oberdieck reduced PT, Bryan, Behrend,
   and Thomas do not construct compact Hall/CoHA sources, Pfaffian
   orientation lines, type-II Weyl orientation lifts, or first-order
   Dirac--Igusa operators.

8. Notation audit.
   Check the whole manuscript for conflations among
   `\chi_{10}`, `\chi_{10}^{\mathrm{OP}}`, `\Delta_5^2`, and
   `\Delta_{10}^{\theta}`. Safe convention:
   ```tex
   \Delta_{10}^{\theta}=\Delta_5^2,\qquad
   \chi_{10}^{\mathrm{OP}}=2^{-12}\Delta_{10}^{\theta}=D_5^2.
   ```

9. Chamber audit.
   If a compact Hall source is ever asserted, require a stability/HN
   chamber statement and wall-crossing compatibility with the OP expansion.
   The scalar equality alone is an equality of Laurent expansions in the
   OP chamber.

10. Orientation-technology audit.
    PTVV, BBDJS, Joyce--Upmeier, Borisov--Joyce, and Oh--Thomas may supply
    technology/analogies. They do not supply O1/O1+/O2 for reduced
    `K3\times E`; every such use must remain conditional or open.

Bottom line: keep the scalar theorem strong by keeping it narrow. The
paper may call the OP branch the second-order, orientation-forgetting
shadow only after saying "if the first-order compact object is supplied."
Without that supplied data, OP/Oberdieck gives exactly one thing:
the reduced scalar square \(-4096\Delta_5^{-2}\) in the stated chamber
and normalization.
