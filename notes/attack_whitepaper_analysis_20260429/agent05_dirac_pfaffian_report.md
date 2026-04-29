# Agent 05 Report: Dirac Principle / Pfaffian / Orientation Character

Scope: square root in Dirac sense, first-order protected operator, Pfaffian determinant, orientation line, Maass/reflection character, `epsilon_o = nu_Delta5`, scalar square forgetting orientation, and the precise Joyce-Upmeier / Borisov-Joyce / Oh-Thomas status.

## forced definitions

1. **Dirac square root.** The square root is not an analytic branch of the scalar OP/DT function. It is a first-order protected object whose scalar shadow is the square. The manuscript should say: the scalar branch
   `Z_OP/DT^X = -4096 Delta_5^{-2}`
   is second-order/orientation-forgetting; the Dirac object is a protected chiral/Hall/Pfaffian object `D_X` with `Pf_prot(D_X) = Delta_5` only after a supplied Pfaffian-to-automorphic comparison. This is the "Dirac move" in the April 29 analysis: begin with the first-order object, not with a scalar square root (`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:1903`, `:1934`, `:1979`).

2. **First-order protected operator.** `D_X` must mean a supplied compact protected algebra/operator/module package, including primitive protected states, normal-ordered Gram projection, orientation/Pfaffian line, and source-target comparison. It is not constructed by the virtual `K_0` determinant, by the scalar partition function, or by naming the Pfaffian product. Current `main.tex:882-918` already states the correct target form; theorem prose must not exceed it.

3. **Pfaffian determinant.** The Pfaffian is a square root of the reduced determinant line:
   `o_C^{otimes 2} ~= det RHom_red(C,C)`.
   A protected Pfaffian is a section of a Pfaffian line. Equality with `Delta_5` is meaningful only after a comparison
   `iota_aut: L_Pf,X -> L^5 otimes nu_Delta5`
   compatible with cusp trivialization and squaring (`main.tex:1481-1495`, `:1708-1727`). Without `iota_aut`, the strongest statement is equality of normalized formal Borcherds products at the cusp.

4. **Orientation line / orientation gerbe.** The orientation line is not merely a Picard square root. For the reduced `K3 x E` Hall sector it includes: a square root line, null-trivializations of reduced and equivariant degree-two gerbe obstructions, zero finite-stabilizer linearization characters, and compatibility with extension correspondences and the reduced `E` quotient (`main.tex:1177-1238`). The safer rewrite should introduce the square-root gerbe first: global orientation is a section/trivialization of that gerbe; twisted Hall states can live over the gerbe before O1 is solved (`materials/...analysis.txt:21548-21575`).

5. **Maass/reflection character.** `nu_Delta5` is the automorphic multiplier character of the Igusa cusp form. On the type-II chamber decomposition, Maass/Gritsenko-Nikulin give
   `nu_Delta5(s_delta_i) = -1` for `i=1,2,3`, and `+1` on the three `Aut(Poly_II) ~= S_3` chamber-permuting reflections (`main.tex:5287-5325`; `proj.bib:38-45`, `:100-110`). This is an automorphic character calculation, not a Hall orientation construction and not a scalar normalization.

6. **Hall orientation character.** `epsilon_o` is defined only after O1 supplies quotient orientation, O1+ supplies coherent Weyl transport, and O2 supplies local Pfaffian wall charts. It is the sign by which the lifted reflection acts on the oriented Pfaffian line in the reduced compact Hall sector. The desired theorem is conditional:
   `epsilon_o|_{W^{(2)}(Lambda^{2,1}_{II})} = nu_Delta5|_{W^{(2)}(Lambda^{2,1}_{II})}`.

7. **Why the scalar square forgets orientation.** The scalar branch cannot distinguish `Pf` from `-Pf` or `Delta_5` from `-Delta_5`: `(-Pf)^2 = Pf^2` and `(-Delta_5)^2 = Delta_5^2`. The constant `-4096` and OP sign are scalar normalization data; they cannot determine a Weyl/reflection character (`materials/...analysis.txt:2578-2694`, `:5131-5186`; `main.tex:1729-1752`).

8. **Joyce-Upmeier / Borisov-Joyce / Oh-Thomas status.** These references supply orientation technology and analogues, not the theorem needed here. Joyce-Upmeier and Joyce-Tanaka-Upmeier concern CY3 orientation data and gauge-theoretic orientation frameworks; Borisov-Joyce, Cao-Gross-Joyce, Oh-Thomas, Bojko, and Cao-Kool-Monavari concern CY4 virtual-cycle/orientation packages and related sign conventions (`proj.bib:512-604`, `:566-584`). They do not prove the cosection-reduced `K3 x E` quotient orientation, its `E[2]` linearization, finite-stabilizer descent for all even `N`, or the type-II Weyl-equivariant lift (`main.tex:1632-1655`). Any sentence implying otherwise is an unsupported orientation theorem.

## theorem/proposition replacements

1. **Replace the current all-in-one conditional theorem with four statements.**
   - Definition: a Dirac-Igusa datum consists of the protected source object/algebra, compact primitive sector, Gram projection, orientation/Pfaffian package, orientation monodromy character, and recognition comparison.
   - Theorem A: Pfaffian determinant conditional on recognition. If a Dirac-Igusa datum exists and its protected primitive superdimensions are `f(nm,l)`, then after `iota_aut`, `Pf_prot(D_X)` maps to `Delta_5`.
   - Theorem B: Scalar square. If `Pf_prot(D_X)` maps to `Delta_5`, then the OP scalar branch is `-4096 Pf_prot(D_X)^{-2}` under the OP normalization; this statement is orientation-forgetting.
   - Theorem C: Local Pfaffian sign. If O1/O1+/O2 hold at a type-II wall and the normal Pfaffian rank is `N_delta^Pf`, then `epsilon_o(s_delta) = (-1)^{N_delta^Pf}`; for the supplied rank-one type-II charts, this gives `-1`.
   - Theorem D: Orientation character. If `epsilon_o` is an honest character on `W^{(2)}(Lambda^{2,1}_{II})` and `epsilon_o(s_delta_i) = -1` for the three simple reflections, then `epsilon_o = nu_Delta5` on that reflection group. This is the clean group-theoretic step (`materials/...analysis.txt:6500-6665`).

2. **Replace "constructs `D_X`" with "recognizes the Pfaffian of a supplied first-order datum."** The proof at `main.tex:1678-1706` is honest in saying it does not construct `D_X`; the theorem statement should match that. Orientation data plus Pfaffian local models do not construct a chiral protected module, compact primitive states, primitive bracket, source factorization object, or the mode decomposition whose exponents are `f(nm,l)` (`materials/...analysis.txt:4708-4781`).

3. **State a separate universal algebraic Dirac-Igusa target if desired.** The April 29 analysis allows an algebraic construction from `Delta_5`, its Weyl character, and a finite/generic reflection set, but that object is automorphic/formal. It is not the compact `K3 x E` Hall geometry. Label it "algebraic target" or "automorphic Dirac-Igusa datum", then make geometric realization a comparison theorem.

4. **Turn O1/O1+/O2 into an appendix-level obstruction package.** Main text should carry the short theorem and a precise list of hypotheses. The detailed quotient gerbe, finite-stabilizer, Weyl cocycle, torsor, and local normal-mode calculations should be grouped as construction targets.

5. **Do not assert Hall signs on the `S_3` chamber-permuting reflections.** The Maass values there are `+1`, but a Hall orientation sign on these reflections requires extension of the oriented Hall action from `W^{(2)}(Lambda^{2,1}_{II})` to the semidirect product (`main.tex:1517-1522`).

## overclaims

1. **Unsupported construction of first-order geometry.** Any claim that O1/O1+/O2 imply existence of `D_X` is too strong. They are orientation and local-sign hypotheses, not a compact factorization/Hall construction.

2. **Unsupported determinant equality.** The line in the proof saying
   `iota_aut^{otimes 2}(Pf_prot(D_X)^2) = det RHom_red(C,C)|_tot = Delta_5^2`
   is risky (`main.tex:1729-1737`). The safe statement is:
   `iota_aut^{otimes 2}(Pf_prot(D_X)^2) = Delta_5^2`.
   The middle determinant equality is not a bare theorem unless "total determinant under the supplied comparison and compact realization" is explicitly part of the hypothesis.

3. **OP minus sign as orientation data.** The draft must not say the cosection parity flip sources the OP scalar minus or determines `epsilon_o`. The current safety sentence at `main.tex:1667-1670` is good and should be enforced globally.

4. **Automorphic divisor order as Pfaffian crossing count.** `d_aut = 1` is an automorphic divisor fact. `N_delta^Pf = 1` is a local Hall/Pfaffian normal-mode hypothesis. They can agree in the desired model, but one does not prove the other (`main.tex:1426-1437`, `:1805-1885`).

5. **Maass character as Hall orientation proof.** Maass/Gritsenko-Nikulin prove the automorphic target character. They do not kill the Weyl determinant-line cocycle `c_o`, the quotient torsor defects `omega_{i,C}`, or finite-stabilizer characters.

6. **Known orientation literature as reduced quotient theorem.** Joyce-Upmeier, Borisov-Joyce, Oh-Thomas, and related sources do not prove the reduced `K3 x E` quotient orientation or Weyl lift. They should be cited as technology/analogues only (`main.tex:1639-1655`; `materials/...analysis.txt:8010-8190`, `:21527-21633`).

7. **Scalar trace as algebra reconstruction.** A trace cannot reconstruct the algebra or orientation character. The Dirac framing must start with observables/source/factorization and only then take the trace (`materials/...analysis.txt:1998-2010`).

8. **Chamber-permuting reflection signs.** The text is correct at `main.tex:1517-1522`; preserve it. Any later prose saying `epsilon_o` has the `+1` values on `S_3` without semidirect Hall action is unsupported.

## exact residual orientation calculations

1. **O1 reduced quotient obstruction package.** On each Hall stratum, O1 requires simultaneous vanishing of:
   - `alpha_C^red in H^2(M_C^red; F_2)`.
   - `alpha_C^{E,free} = a_1(C)u_1 + a_2(C)u_2 in H^2(BE; F_2)`, with `H^*(BE; F_2)=F_2[u_1,u_2]`, `|u_i|=2`.
   - finite-stabilizer degree-two classes `beta_C^{E,N} in H^2(BE[N]; F_2)`, more precisely the Borel classes `tilde beta_{R,S}^{E,N} in H^2_{E[N]}(S; F_2)`.
   A point-stabilizer calculation is insufficient until mixed Borel terms, stabilizer action on `H^*(S;F_2)`, and spectral-sequence differentials vanish (`main.tex:1195-1227`).

2. **Residual finite-stabilizer characters.** After degree-two gerbes vanish, choices of finite-stabilizer linearization form an `H^1(BE[N];F_2)` torsor. O1 requires the zero character:
   `lambda_C^{E,N} in H^1(BE[N];F_2)` must vanish for every finite stabilizer used by the Hall correspondences (`main.tex:1223-1235`).

3. **Exact `E[2]` calculation.** With `E[2]=<e_1,e_2>` and `e_3=e_1+e_2`,
   `beta_C^{E,E[2]} = b_20 x_1^2 + b_11 x_1 x_2 + b_02 x_2^2`,
   where
   `(b_20,b_11,b_02) = (r_1, r_1+r_2+r_3, r_2)`,
   and
   `res_{<e_i>} beta_C^{E,E[2]} = r_i tau_i^2`.
   If this class vanishes, the residual character is
   `lambda_C^{E[2]} = lambda_1 x_1 + lambda_2 x_2`,
   with cyclic restrictions
   `rho_1=lambda_1`, `rho_2=lambda_2`, `rho_3=lambda_1+lambda_2`.
   Trivial `E[2]` linearization means `rho_1=rho_2=rho_3=0`. The `r_i` are degree-two bits; the `rho_i` are degree-one bits (`main.tex:1239-1265`).

4. **Even `N >= 4` residual.** If `2^a || N` and `a >= 2`,
   `E[N]_(2) ~= (Z/2^a)^2` and
   `H^2(B(Z/2^a)^2;F_2) = F_2<y_1, x_1 x_2, y_2>`.
   Write
   `beta_{C,(2)}^{E,N} = A_1^{(N)} y_1 + A_12^{(N)} x_1 x_2 + A_2^{(N)} y_2`.
   Order-two cyclic restrictions see `A_1^{(N)}`, `A_2^{(N)}`, and `A_1^{(N)}+A_2^{(N)}`, but not `A_12^{(N)}`. Therefore `E[2]` tests do not compute `beta_C^{E,N}` for even `N >= 4`. Even after this degree-two residual vanishes, `H^1(B(Z/2^a)^2;F_2)=F_2<x_1,x_2>` remains and must be killed (`main.tex:1266-1313`).

5. **O1+ Weyl lift residuals.** A choice of determinant-line lifts gives a projective action with cocycle
   `c_o in Z^2(W^{(2)}(Lambda^{2,1}_{II}); F_2)`,
   `w'^* tau_w circ tau_{w'} = (-1)^{c_o(w,w')} tau_{ww'}`.
   O1+ requires `[c_o]=0`, a killing `1`-cochain, and normalization `tau_i^2=1`. It must transport the entire quotient-orientation package
   `(alpha_C^red, alpha_C^{E,free}, {(beta_C^{E,N}, lambda_C^{E,N})}_{N>=2})`,
   not only the line. For each simple reflection, the quotient torsor defect is
   `omega_{i,C} in H^1(M^red_{s_delta_i C};F_2) direct-sum_{N>=2} H^1(BE[N];F_2)`;
   all `omega_{i,C}` must vanish (`main.tex:1316-1404`).

6. **O2 local Pfaffian wall residuals.** At a type-II wall, O2 requires local wall charts with tangent/normal splitting, local equation `u_delta`, reflection action `s_delta(u_delta)=-u_delta`, invariant unit, and normal determinant complex
   `K_delta^nor ~= direct-sum_{j=1}^{N_delta^Pf} [R --u_delta--> R]`.
   The Pfaffian section is `u_delta^{N_delta^Pf}` times a unit. For the three simple type-II walls, the supplied model has
   `N_delta1^Pf = N_delta2^Pf = N_delta3^Pf = 1` (`main.tex:1407-1437`).

7. **Exact local sign formula.** Once O1 supplies quotient orientation, O1+ supplies normalized lift, and O2/hybrid residuals vanish, the local loop gives
   `M_l(upsilon_i u_i) = upsilon_i(-u_i) = -upsilon_i u_i`,
   hence
   `epsilon_{o,R}(s_delta_i) = (-1)^{N_delta_i,R^Pf}`.
   Rank one gives `epsilon_{o,R}(s_delta_i)=-1`. It becomes compact Hall monodromy only after quotient-orientation classes, `[c_o]`, `omega_{i,C}`, finite-stabilizer characters `lambda^{E,N}`, O2/hybrid residuals, and `O_hyb,R` vanish compatibly in `R` (`main.tex:1438-1476`).

8. **Automorphic target values.** The Maass target is:
   `nu_Delta5(s_delta_i)=-1` for `i=1,2,3`;
   `nu_Delta5(s_{f_-2-f_2}) = nu_Delta5(s_{f_2-f_3}) = nu_Delta5(s_{f_2+f_3}) = +1`.
   These values are independent of multiplying `Delta_5` by a nonzero scalar (`main.tex:5287-5325`).

## current anchors

1. `main.tex:100-115`: abstract already states the correct certificate posture: scalar OP/DT branch is orientation-forgetful; `D_X` construction remains open unless orientation system, Weyl transport, and type-II Pfaffian atlas are supplied.

2. `main.tex:882-918`: "Dirac/Pfaffian recognition target" correctly says `K_0` determinant does not produce the operator and scalar OP does not fix square-root orientation.

3. `main.tex:921-1121`: local sign subcertificate and local obstruction certificate. Keep conditionality: automorphic divisor/Maass do not prove Hall Pfaffian charts.

4. `main.tex:1139-1539`: main conditional theorem. This is the central target for rewrite: split into supplied first-order datum, Pfaffian comparison, scalar-square, and orientation-character statements.

5. `main.tex:1177-1476`: O1/O1+/O2 residuals are strong and should be preserved, likely moved out of the main theorem body.

6. `main.tex:1632-1674`: excellent status paragraph. Preserve and enforce: existing CY3/CY4 orientation literature supplies technology/partial inputs, not the reduced `K3 x E` quotient orientation, `E[2]` linearization, or type-II Weyl lift.

7. `main.tex:1729-1752`: scalar-square proof. Tighten determinant equality as noted above; keep OP `-4096` separate from orientation.

8. `main.tex:5287-5325`: automorphic Maass character anchor.

9. `proj.bib:38-45`, `:100-110`, `:512-604`, `:566-584`: bibliography anchors for Maass/Gritsenko-Nikulin and orientation analogues.

10. `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:1903-1995`, `:2578-2694`, `:4708-4839`, `:5131-5186`, `:6500-6665`, `:21548-21663`: attack-analysis anchors for the forced rewrite.

## rewrite plan

1. In the introduction, define the "Dirac principle" explicitly: first-order protected object first; scalar trace second; no analytic square root of the OP scalar branch.

2. In the main theorem, remove any language that says O1/O1+/O2 construct `D_X`. State "given a compact Dirac-Igusa datum" or "assuming the first-order protected object of D0".

3. Split the current theorem into:
   - Dirac-Igusa datum definition.
   - Pfaffian recognition conditional on primitive superdimensions and `iota_aut`.
   - Scalar-square/OP normalization theorem.
   - Local type-II Pfaffian sign proposition.
   - Group-theoretic character lemma `epsilon_o=nu_Delta5` on `W^{(2)}(Lambda^{2,1}_{II})`.

4. Move the long O1/O1+/O2 obstruction package to an appendix or construction-target subsection. Keep the main text summary short but include the exact residual names: `alpha_red`, `alpha^{E,free}`, `beta^{E,N}`, `lambda^{E,N}`, `c_o`, `omega_{i,C}`, `N_delta^Pf`.

5. Add a square-root gerbe paragraph before global orientations: twisted Hall states live over the gerbe; O1 is its trivialization/descent problem. This avoids pretending the global orientation line is already built.

6. Enforce the sign separation everywhere:
   - OP minus and `4096` are scalar normalization.
   - Maass character is automorphic multiplier data.
   - `epsilon_o` is Hall orientation monodromy after O1/O1+/O2.
   - Scalar squares cannot determine orientation characters.

7. Rewrite orientation-literature citations with exact status language: "technology and analogues" only; no reduced `K3 x E` quotient/Weyl theorem is imported from Joyce-Upmeier, Borisov-Joyce, or Oh-Thomas.

8. Keep `d_aut` and `N_delta^Pf` distinct in notation and prose. Say agreement is a target/check after the local Pfaffian model is supplied, not a proof of that model.

9. Do not extend `epsilon_o` to the `S_3` chamber-permuting reflections unless a semidirect Hall action and coherent orientation lift are explicitly added as hypotheses.
