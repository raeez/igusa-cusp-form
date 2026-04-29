# Agent43 Latest Theorem Spine Report

Scope: proposal-only theorem-spine attacker/healer.  No manuscript files edited.

Sources read:
- `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`
- `main.tex`
- requested `INTEGRATED_DECISION_LEDGER.md`: absent from this checkout.  `find /Users/raeez/igusa-cusp-form -name 'INTEGRATED_DECISION_LEDGER.md' -o -name '*DECISION*LEDGER*.md'` returned no file.  Older ledgers exist only at `notes/sixth_attack_heal_20260428/INTEGRATED_LEDGER.md` and `notes/seventh_attack_heal_20260428/INTEGRATED_LEDGER.md`.

Protocol used: attack-heal stable-core rule from `/Users/raeez/ecosystem/.agents/skills/attack-heal-swarm/references/protocol.md`.  Attacker text is evidence, not authority.  The stable spine below includes only claims with manuscript anchors or explicit imported-source status.  Constructed-compact claims from the latest analysis are marked residual unless `main.tex` actually constructs the object.

## Executive Verdict

Stable core: nonempty, but not yet presented as the platonic theorem spine.

The latest analysis has two layers:

1. Minimum stable spine already largely present in `main.tex`: virtual Borcherds determinant, D6-D2-D0 Mukai-Gram dictionary, normal-ordered charge theorem, raw Gram descent no-go, imported denominator algebra, imported OP scalar square, conditional primitive recognition / Dirac-Igusa realization problem.
2. Platonic ideal spine beyond current `main.tex`: universal algebraic Dirac-Igusa model, geometric pre-Hall source, orientation-gerbe-twisted Hall object, hybrid wrapped source, source Koszul object, primitive comparison.  These are proposed theorem targets in the latest analysis, not current theorems of `main.tex`.

Current `main.tex` violates the spine by burying the stable core under status ledgers, orientation obstruction packages, finite-source certificates, eight-row material, and a late synthesis theorem.  It also orders the denominator algebra after the no-go theorem, although the no-go uses low-degree denominator real-root strings, and it places the D6-D2-D0 dictionary before the formal normal-ordering section but away from the determinant and OP square that it is meant to bridge.

## Maximal Theorem Spine Required

### A. Automorphic Determinant Spine

**T1. Virtual Borcherds determinant theorem.**  
Status: theorem, proved in paper from `K_0` determinant calculation plus imported Borcherds-Gritsenko-Nikulin product.

Statement:
\[
\mathcal D_X(Z)=64q^{1/2}r^{1/2}s^{1/2}
\prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}
=\Delta_5(Z).
\]

Dependencies:
- K3 index and half-index definition: `main.tex:671`, `main.tex:699`, `main.tex:726`.
- Fock trace / superdeterminant: `main.tex:747`.
- normalized determinant: `main.tex:822`.
- imported BGN identification: `main.tex:2534`.

Current label problem: `main.tex:2534` is only a proposition.  The late theorem at `main.tex:14129` restates it, but too late and with unrelated material.

Rewrite action: promote `prop:bgn-identification` into the first theorem after the determinant definitions, or create a named theorem immediately after `main.tex:837` using `main.tex:2534-2562` as proof.

### B. D6-D2-D0 Mukai-Gram Spine

**T2. D6-D2-D0 Mukai-Gram dictionary.**  
Status: theorem, proved in paper.

Statement:
\[
v_X(I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
\qquad
\Pi_X(Q_Y,P_Y)=\left(\frac{\beta^2}{2},n,d-1\right),
\]
and for \(\beta_h^2=2h-2\),
\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
\]

Dependencies:
- Mukai pairing and Kunneth convention inside theorem: `main.tex:2665-2702`.
- proof: `main.tex:2704-2758`.

Current label: correct theorem label.  Current placement after long orientation section is wrong: it should appear before the compact orientation obstruction material and immediately before normal-ordering.

Rewrite action: move `main.tex:2638-2768` directly after the automorphic determinant theorem and before the normal-ordered charge theorem.

### C. Normal-Ordered Charge Spine

**T3. Quadratic polarization and normal-ordered charge theorem.**  
Status: theorem/proposition package; should be a theorem.

Statement:
\[
B(c,c')=(Q\cdot Q',Q\cdot P'+Q'\cdot P,P\cdot P')
\]
is symmetric bilinear, \(B(c,c)=2\Pi_X(c)\),
\[
\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c'),
\]
\[
\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}},
\qquad
(c,T)\star(c',T')=(c+c',T+T'+B(c,c')),
\]
and
\[
\overline\Pi_X(c,T)=\Pi_X(c)-T
\]
is a homomorphism.

Dependencies:
- formal dyonic Mukai lattice: `main.tex:4325-4396`.
- additivity defect: `main.tex:4604-4626`.
- cocycle/central extension theorem in lemma form: `main.tex:4628-4830`.
- extension definition: `main.tex:4852-4892`.
- group law: `main.tex:4894-4912`.
- flag formula: `main.tex:4914-4941`.

Current label problem: the central theorem is split across a definition and lemmas.  The latest analysis asks for a named theorem: Quadratic Polarization / Normal-Ordered Pushforward.  `main.tex` currently makes the core look like supporting algebra rather than the main new theorem.

Rewrite action: replace the cluster `main.tex:4325-4941` by:
- Definition: formal dyonic Mukai lattice and Gram map.
- Theorem: quadratic polarization and normal-ordered charge extension.
- Corollary: normal-ordering flag formula.

### D. Raw Descent No-Go Spine

**T4. Raw Gram descent no-go.**  
Status: theorem, proved in paper.

Statement: strict fixed-lift raw \(\Pi_X\)-pushforward cannot realize the full type-II real-root strings; normal-ordered descent is necessary.

Dependencies:
- T3, especially \(B(c,c)=2\Pi_X(c)\).
- low-degree real-root bracket information: `main.tex:12731` and first window material around `main.tex:13039`.
- theorem/proof: `main.tex:4962-5047`.

Current dependency problem: denominator algebra and low-degree BKM brackets are stated later (`main.tex:5639`, `main.tex:12731`), so the proof points forward.  This is acceptable technically but bad theorem spine.

Rewrite action: move a compact BKM target/real-root string subsection before T4, or move T4 immediately after the denominator-algebra target section.

### E. Denominator Algebra Target Spine

**T5. Gritsenko-Nikulin denominator target.**  
Status: imported theorem plus paper's notation.

Statement:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
\qquad
\operatorname{smult}\mathfrak g_{\Delta_5,\alpha(n,l,m)}=f(nm,l)
\]
on active support.

Dependencies:
- BGN/GN import and root-degree map.
- denominator algebra definition: `main.tex:5669-5691`.
- theorem/proof: `main.tex:5693-5783`.

Current label: correct theorem label.  Placement is too late relative to the no-go theorem.  It should be part of the first half of the paper before compact realization.

Rewrite action: move `main.tex:5639-5783` before or immediately after T3, before T4 if T4 cites real-root strings.

### F. OP Scalar Square Spine

**T6. Reduced DT/PT/OP scalar square.**  
Status: imported theorem/check, not compact orientation.

Statement:
\[
Z^X_{\mathrm{DT}}(T,Q,P)=Z^X_{\mathrm{OP}}(P,Q,T)
=-4096\Delta_5(Z)^{-2}.
\]

Dependencies:
- D6-D2-D0 variable dictionary T2.
- scalar quotient integration: `main.tex:2769-2808`.
- OP normalization: `main.tex:13822-13902`.
- scalar square theorem: `main.tex:13904-13953`.

Current placement problem: scalar square appears at `main.tex:13799`, after thousands of lines of compact-source residuals.  It should be directly after T2 and T5, because it is an imported scalar check, not the end of the proof.

Rewrite action: move `main.tex:13799-14053` into the main theorem spine before compact realization.

### G. Algebraic Current Envelope / Target Model

**T7. Formal current envelope.**  
Status: proposition in current paper; theorem/proposition depending on ambition.

Statement:
\[
\mathsf{Den}_{\Delta_5,E}=U_E^{\mathrm{ch}}(\operatorname{Cur}_E(\mathcal A_{\mathrm{den}}))
\]
is the target-side current envelope of the imported denominator algebra.

Dependencies:
- T5.
- BD current/chiral envelope construction.
- definition and proposition: `main.tex:5805-5849`.

Current violation: the latest analysis distinguishes actual algebraic construction from compact source construction.  Current `main.tex` labels this correctly as target-side, but it is buried inside the compact realization problem.

Rewrite action: present it as "Target current envelope" before compact geometry.  Do not let it masquerade as a compact source.

### H. Compact Dirac-Igusa Source Problem

**D1. Dirac-Igusa realization certificate.**  
Status: definition, not theorem.

Statement: a compact realization certificate is
\[
\mathfrak K_X=(L_X,H_X,O_X,D_X,R_X),
\]
with local charge/E3 host, hybrid K3-to-E shadow, orientation, normal-ordered descent/Koszul comparison, and primitive recognition.

Dependencies:
- T2-T7.
- definition: `main.tex:11848-12220`.

Current label: correct as definition.  Current placement wrong: it occurs after long finite source ledgers and before primitive recognition, so the reader meets details before the object.

Rewrite action: move the compact certificate definition immediately after the target current envelope and before finite D0/hybrid/orientation details.

### I. Conditional Normal-Ordered Hall Descent

**T8. Conditional normal-ordered Hall descent certificate.**  
Status: conditional theorem with residual obstruction tuple.

Statement: if the supplied Hall source, reduced quotient, multiplicative orientation, degree-shift cochain, Frobenius pairing, and cyclic lift exist, then \(\overline\Pi_{X,*}^{\Theta}\) produces a \(\Gamma_{\mathrm{gram}}\)-graded Lie superalgebra at \(H^0\), and the seven obstruction classes describe exactly what remains.

Dependencies:
- T3/T4.
- compact source data D1.
- theorem/proof: `main.tex:8688-9215`.

Current label: correct conditional theorem.  Current violation: it appears before the reader has a clean compact certificate definition at `main.tex:11848`.

Rewrite action: move after D1, and compress the obstruction formulas into theorem plus appendix if the main proof becomes unreadable.

### J. Primitive Recognition

**T9. Primitive recognition certificate; no source construction.**  
Status: conditional theorem/certificate theorem.

Statement: if source-side representatives, relations, Hopf pairing/radical, no-extra-relations theorem, generation, PBW, exact completion, and full parity dimensions are supplied, then
\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}
\]
as Gram-graded Lie superalgebras, and with source Koszul data
\[
\Omega_E^{\mathrm{ch}}C_X\simeq\mathsf{Den}_{\Delta_5,E}.
\]

Dependencies:
- T5/T7/T8.
- source certificate D1.
- theorem/proof: `main.tex:12222-12575`.

Current label: correct and admirably honest.  Current violation: finite-window machinery from `main.tex:12577-13372` sits in the main spine and bloats it.

Rewrite action: keep T9 in main text.  Move finite-window certificate, first timelike count, and NO7 source protocol to a "Finite recognition certificates" appendix or compressed subsection.

### K. Dirac-Pfaffian / Orientation Character

**T10. Conditional Dirac-Pfaffian normalization and orientation character.**  
Status: conditional theorem, not constructed.

Statement: if D0/Pfaffian/orientation data are supplied, then the protected Pfaffian identifies with \(\Delta_5\), the scalar square matches OP, and if the compact orientation monodromy exists with the three simple reflection signs, \(\epsilon_o=\nu_{\Delta_5}\) on the type-II Weyl group.

Dependencies:
- T1/T5/T6.
- D1/T8/T9.
- current theorem: `main.tex:1143-?` for conditional Dirac-Pfaffian recognition.
- finite wall signs and Weyl sign extension: `main.tex:924-2326`.

Current violation: orientation/Pfaffian wall machinery starts before the normalized cusp form (`main.tex:886-2326` precedes `main.tex:2387`).  This inverts the theorem spine.

Rewrite action: move orientation/Pfaffian wall material after T1-T9, keeping only one sentence in the introduction: "the Pfaffian sign is conditional on the compact orientation system."

### L. Eight-Row and Spin Material

**R1. Eight diagonal-divisor rows.**  
Status: independent appendix/companion; not part of the N=1 theorem spine unless row certificates are supplied.

Anchors:
- eight-row section begins `main.tex:14369`.
- spin L-factor section begins `main.tex:14658`.
- boundary rows appendix begins `main.tex:14789`.

Rewrite action: remove from main theorem spine.  If retained in this paper, mark `Part IV is independent of Parts I-III` before `main.tex:14369`.

## Claim Taxonomy

Theorem:
- T1 virtual determinant, after promotion from proposition.
- T2 D6-D2-D0 Mukai-Gram dictionary.
- T3 quadratic polarization / normal-ordered charge extension, after consolidation.
- T4 raw Gram descent no-go.
- T5 denominator algebra identity, imported.
- T6 OP scalar square, imported/check.
- T8 conditional normal-ordered Hall descent.
- T9 primitive recognition certificate.
- T10 conditional Dirac-Pfaffian / orientation-character consequence.

Proposition:
- formal current envelope T7 if kept as target-side construction rather than headline theorem.
- finite consequences of hybrid certificate, no quotient-first hybrid repair, finite D0 package, finite recognition windows.
- square-root consequence from scalar square.

Definition:
- K3 half-index representative.
- normalized \(K_0\)-determinant.
- formal dyonic Mukai lattice and Gram map.
- denominator Lie superalgebra.
- target current envelope.
- Dirac-Igusa realization certificate.
- finite certificates: D0, hybrid, normal-ordering coefficient category, cofinal recognition.

Conjecture:
- protected D-brane index: `main.tex:2810`.
- any physical protected Hilbert-space identification not used by scalar theorem.

Residual / Open:
- compact state-side D0 construction: `main.tex:13374`.
- hybrid wrapped factorization: `main.tex:8338`.
- chain-level Hall strictification, finite HN completion, cyclic lift, Hopf radical coideal, exact completion.
- compact orientation monodromy and type-II Pfaffian wall atlas.
- row physical host certificates.

Forbidden as theorem in current paper:
- compact Hall/factorization source exists.
- \(\mathfrak D_X\) constructed from compact geometry.
- \(H^0\Prim_{\mathrm{prot}}(\overline\Pi^\Theta_{X,*}\mathcal F_X)\cong\mathfrak g_{\Delta_5}\) unconditionally.
- scalar square determines orientation.
- determinant determines bracket constants, full parity dimensions, Hopf radical, PBW, or compact Hall constants.
- eight-row physical hosts without row certificates.

## Dependency Graph

T1 depends on K3 half-index + Fock determinant + BGN product.

T2 depends on Mukai vector calculation for ideal sheaves on \(S\times E\).

T3 depends on formal Mukai lattice and the quadratic Gram map.

T5 depends on BGN/GN denominator algebra, root-degree map, and active support.

T4 depends on T3 and the real-root string data from T5.

T6 depends on T2 for variables and on OP/Oberdieck imported scalar theorem.

T7 depends on T5 and BD current/chiral envelope technology.

D1 depends on T2-T7; it is a data definition, not a result.

T8 depends on D1 plus T3/T4; it supplies conditional chain-level normal-ordered descent and obstruction classes.

T9 depends on T5/T7/T8 and source-side primitive data; it is a recognition theorem, not an existence theorem.

T10 depends on T1/T5/T6/T8/T9 plus supplied orientation/Pfaffian wall atlas.

R1 depends on independent Clery-Gritsenko/Govindarajan row inputs; it does not feed T1-T10.

## Current `main.tex` Violations

1. **The theorem spine is visible only in the abstract and late synthesis, not in section order.**  
   `main.tex:57-172` and `main.tex:194-210` know the dependency chain.  But the actual sections run: physical question, local schema, determinant, orientation/Pfaffian target, normalized cusp form, D6-D2-D0, long orientation obstruction, normal-ordered charge, Weyl chamber, denominator, compact source, scalar square, synthesis, eight rows.  The stable theorem order is not the document order.

2. **Orientation appears before the automorphic theorem spine closes.**  
   `main.tex:886-2326` introduces Dirac/Pfaffian recognition targets and wall certificates before the normalized cusp theorem at `main.tex:2387` and denominator target at `main.tex:5639`.  This violates the latest analysis instruction to move automorphic determinant proof before physical speculation.

3. **T1 is under-labeled.**  
   The product identity `main.tex:2534-2562` is a proposition, while the latest analysis makes it Theorem A / Theorem 1.  The late synthesis theorem `main.tex:14129` is too broad and too late to fix this.

4. **T3 is split into too many local lemmas.**  
   `main.tex:4325-4941` contains the paper's main new algebraic theorem, but it is distributed across definitions and lemmas.  The latest analysis calls this the mathematical core and asks for named Quadratic Polarization / Normal-Ordered Pushforward theorems.

5. **T4 depends on denominator data stated later.**  
   Raw descent no-go at `main.tex:4962-5047` uses type-II real-root strings and points to `main.tex:12731`, after the denominator algebra and primitive recognition.  This creates a forward dependency in the proof spine.

6. **The OP scalar theorem is misplaced.**  
   The scalar square `main.tex:13799-14053` is an imported scalar check and should sit near T2/T5, not after the compact realization machinery.

7. **Compact certificate definition is too late.**  
   The compact realization section begins at `main.tex:5785`, but the actual five-part certificate is not defined until `main.tex:11848`.  Thousands of lines of finite source, hybrid, and normal-ordering data precede the object they are meant to support.

8. **Finite certificate ledgers overload the main spine.**  
   Hybrid certificate `main.tex:7202-8336`, normal-ordering obstruction theorem `main.tex:8688-9215`, finite D0 certificate `main.tex:11616-11846`, and finite recognition windows `main.tex:12577-13372` are valuable.  In the current order they obscure T1-T9.

9. **The late synthesis theorem is not the clean theorem package.**  
   `main.tex:14129-14365` mixes determinant, normal-ordering, denominator, scalar square, compact realization consequences, orientation, primitive recognition, and row certificate logic.  It should become a final theorem-status ledger, not the first place where a reader sees the spine.

10. **Eight-row and spin material remains too close to the main result.**  
    `main.tex:14369-16129` is independent row/spin material.  The latest analysis repeatedly says move it to appendix/companion unless used.  It is not used by T1-T10.

## Concrete Reorder / Rewrite Plan

### New Section Order

1. **Introduction and theorem-status page.**  
   Use `main.tex:57-172` and `main.tex:177-457`, but compress.  Replace the current dependency array with the T1-T10 package.  Move detailed status tables to a boxed "How to read this paper" page.

2. **Virtual Borcherds determinant.**  
   Move/keep `main.tex:644-884`.  Insert promoted theorem from `main.tex:2534-2562` immediately after `main.tex:837-855`.  Keep `main.tex:2387-2634` as automorphic normalization after the theorem, but move orientation-line definitions out.

3. **Mukai-Gram dictionary and scalar variables.**  
   Move `main.tex:2638-2808` here.  Include only the protected index conjecture if needed as a marked conjecture; do not open orientation descent here.

4. **Normal-ordered charge theorem.**  
   Move `main.tex:4318-5055` here.  Consolidate `main.tex:4628-4830` and `main.tex:4894-4941` into one named theorem.

5. **Denominator algebra target.**  
   Move `main.tex:5238-5783` here, including Weyl chamber and real-root data needed for T4.  Keep the imported status explicit.

6. **Raw descent no-go.**  
   Place `main.tex:4962-5047` after denominator real-root data if not already included in Section 4.  This removes the forward dependency.

7. **OP scalar square.**  
   Move `main.tex:13799-14053` here.  Present it as imported scalar square and orientation-forgetful check.

8. **Target current envelope.**  
   Move `main.tex:5785-5849` here, renamed "Target current envelope, not source geometry."

9. **Compact Dirac-Igusa realization problem.**  
   Move `main.tex:11848-12220` here before the finite details.  Then include a short theorem-status table: D0, hybrid, orientation, source Koszul, primitive recognition.

10. **Conditional normal-ordered Hall descent.**  
    Keep `main.tex:8433-9215`, but compress main text to statement/proof idea and push finite diagrams after it.

11. **Primitive recognition.**  
    Keep `main.tex:12222-12575` after normal-ordered Hall descent.  Move `main.tex:12577-13372` to finite recognition appendix.

12. **Conditional Dirac-Pfaffian and orientation character.**  
    Move `main.tex:886-2326` here, after the automorphic and compact-source prerequisites.  Keep it conditional.  Do not let it introduce the paper before T1.

13. **Final theorem package and residual ledger.**  
    Rewrite `main.tex:14055-14365` as a final summary, not a mega-theorem.  It should list proved/imported/conditional/open results with references to T1-T10.

14. **Appendices / companion material.**  
    Move finite certificates, long obstruction ledgers, eight-row rows, spin L-factor, sign conventions, Fourier conventions, and automorphic-line computations here.  At `main.tex:14369`, insert: "This part is independent of the N=1 Dirac-Igusa theorem spine."

### Surgical Line-Anchored Edits

- Replace `main.tex:177-457` with a shorter claim-status page keyed to T1-T10.
- Move `main.tex:886-2326` after primitive recognition, not before `main.tex:2387`.
- Promote `main.tex:2534-2562` from proposition to theorem and place after `main.tex:837-855`.
- Move `main.tex:2638-2768` directly after the determinant theorem.
- Consolidate `main.tex:4325-4941` into one theorem block with definitions preceding.
- Move `main.tex:5639-5783` before raw no-go or move raw no-go after it.
- Move `main.tex:13799-14053` before compact realization.
- Move `main.tex:11848-12220` immediately after target current envelope.
- Keep `main.tex:8688-9215` after the certificate definition, not before it.
- Keep `main.tex:12222-12575` in main; move `main.tex:12577-13372` to appendix.
- Rewrite `main.tex:14112-14365` as final status ledger, not theorem.
- Demote `main.tex:14369-16129` to appendix/companion or mark independent.

## Minimal Platonic Clean Package

If the paper must be made clean without constructing new compact geometry, the theorem package should be:

1. Theorem: Virtual Borcherds determinant \(\mathcal D_X=\Delta_5\).
2. Theorem: D6-D2-D0 Mukai-Gram dictionary.
3. Theorem: Normal-ordered charge extension and pushforward.
4. Theorem: Raw Gram descent no-go.
5. Theorem: Gritsenko-Nikulin denominator target.
6. Theorem: OP scalar square.
7. Proposition: target current envelope.
8. Definition: compact Dirac-Igusa certificate.
9. Conditional Theorem: normal-ordered Hall descent.
10. Conditional Theorem: primitive recognition.
11. Conditional Theorem/Open Problem: Dirac-Pfaffian orientation character.

Everything else is appendix, finite certificate, source-construction residual, or companion atlas.

## Residual Obligations

1. Locate or create the missing `INTEGRATED_DECISION_LEDGER.md`; this report could not use it because it is absent.
2. Decide whether the paper is allowed to add the latest analysis's "universal algebraic Dirac-Igusa model" as a constructed theorem.  Current `main.tex` has a formal current envelope, not the full universal finite Hall-Dirac source described near the end of the latest analysis.
3. If the platonic ideal requires constructed compact source objects, the current manuscript cannot honestly claim them.  It can only state the certificate and residual obstruction classes.
4. Run a TeX build only after manuscript edits.  This report made no manuscript edits.
