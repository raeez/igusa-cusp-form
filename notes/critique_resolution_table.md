# Critique Resolution Table

Date: 2026-04-28.

This is an internal audit ledger for the reconstitution of `main.tex`.
The manuscript remains standalone and must not refer to this file.

| Objection | Resolution in `main.tex` | Current status |
|---|---|---|
| The square root was being read as an analytic branch of `Delta_5^2`. | Recast as Dirac/Pfaffian: first-order datum, orientation line, primitive algebra, normal-ordered descent. Scalar OP/DT square is orientation-forgetful. | Wording repaired; `D0`, `(O1)`, `(O1)+`, `(O2)` remain construction data. |
| The Pfaffian theorem sounded like an existence theorem for `mathfrak D_X`. | Theorem `thm:dirac-pfaffian-recognition-conditional` now assumes `D0` explicitly and states certificate consequences only. | Wording repaired; existence remains open. |
| The OP scalar minus sign was being used as orientation evidence. | Constants section and Pfaffian theorem now state that the OP minus is scalar normalization and does not determine Hall reflection monodromy. | Wording repaired; orientation construction remains open. |
| A Maass-character computation could still be misread as constructing Hall orientation monodromy. | The former second proof was recast as an automorphic target check: it computes `nu_{Delta_5}` only. Equality with the Hall character is conditional on `(O1)`, `(O1)+`, and `(O2)`. | Wording repaired; Hall character construction remains open. |
| The Mukai dictionary used fourfold/Todd-correction language. | Lemma `lem:mukai-vector-ideal-sheaf-sxe` is now the CY3 D6-D2-D0 Mukai-Gram computation with `Pi_X(Q_Y,P_Y)=(h-1,n,d-1)`. | Mathematical computation repaired. |
| Connected `BE` and finite `BE[N]` were conflated. | Lemma `lem:E-equivariant-descent-obstruction` separates `BE\simeq BT^2` from finite stabilizers; `H^1(BE;F_2)=0`; `H^2(BE[2];F_2)` is rank three. | Obstruction typing repaired; finite linearization remains open. |
| Translation invariance was treated as equivariant linearization. | Lemma `lem:bmu2-klein-four-vanishing` now separates degree-two Klein-four gerbe bits from degree-one `E[2]` linearization characters; both must vanish. | Obstruction typing repaired; proof of trivial linearization remains open. |
| Raw Gram pushforward concealed the non-additivity of `Pi_X`. | Part `Physical charge and normal-ordered descent` proves the cocycle, the normal-ordered homomorphism, and the raw-descent no-go theorem. | Formal lattice theorem repaired; compact Hall realization remains open. |
| Chain-level `Theta` descent was presented as the first explanation of the fix. | `Theta` is now a categorification of the lattice-level normal ordering; theorem/open problem language says this explicitly and adds finite-fibre HN topology via `mathfrak o_Theta^top`. | Statement repaired; full chain-level construction remains open. |
| The normal-ordering theorem did not yet force anything. | Theorem `thm:raw-gram-descent-no-go` proves raw descent cannot realize full BKM real-root strings. | Formal obstruction repaired. |
| The manuscript lacked a claim-strength ledger. | Introduction now contains theorem-status ledger: proved/imported, proved lattice, proved no-go, conditional/open, imported scalar. | Wording repaired; compact source construction remains open. |
| Section order let the scalar square explain the paper. | Reordered to determinant -> physical charge/normal ordering -> denominator algebra -> scalar square -> compact realization synthesis. | Structure repaired. |
| The D6--D2--D0 dictionary still sat under the automorphic part rather than the physical-charge mechanism. | The `Physical charge and normal-ordered descent` part now begins before `D6--D2--D0 protected-index dictionary`, so the Mukai-Gram theorem is part of the charge spine. | Structure repaired. |
| The chain-level descent notation still looked like raw `Pi_X` pushforward. | The manuscript now writes the corrected descent as `\overline\Pi_{X,*}^{\Theta}` and explicitly ties it to the homomorphism `\overline\Pi_X:\widehat\Gamma_X\to\Gamma_gram`. | Wording repaired; chain-level construction remains open. |
| The compact realization was packaged as one opaque datum. | Definition `def:compact-igusa-realization-datum` is now a five-level Dirac-Igusa certificate `(L_X,H_X,O_X,D_X,R_X)`, separating charge/local data, hybrid factorization, orientation, descent/Koszul comparison, and primitive recognition. | Structure repaired; certificate entries remain open where listed. |
| The compact-realization part lacked an explicit states-versus-observables separation. | Added section `Compact Dirac--Igusa realization problem`: the formal current envelope is now named as a target observable algebra, not a compact BPS state space. | Wording repaired; compact state construction remains open. |
| Hybrid wrapped locality remained a slogan. | The open problem now asks for a concrete hybrid object with ordered two-sided local/wrapped correspondences, the full eight-word flag atlas, quotient residuals, and protected integration residuals. | Statement partially repaired; construction remains open. |
| Primitive recognition could be mistaken for a dimension count. | Synthesis and recognition theorem state presentation-level obligations: primitive representatives, parities, Serre/orthogonality relations, Hopf pairing, finite-window radical quotient, no-extra-relations, and PBW. The first timelike test is now checked by both the Laurent coefficient `93` and the `29|93` presentation split. | Certificate wording repaired; construction remains open. |

## Remaining proof obligations

1. Construct the compact first-order Dirac-Igusa certificate `D0`.
2. Construct strong reduced orientation `(O1)` beyond the supplied local/projection-finite criteria.
3. Prove the Weyl-equivariant orientation cocycle `(O1)+`.
4. Compute the Pfaffian local model `(O2)` geometrically on type-II walls.
5. Prove the trivial `E[2]`-linearization and the higher even `E[N]` linearization characters by cyclic-sector, Stiefel-Whitney/Wu, and inertia-stack Pin-c routes.
6. Construct the hybrid wrapped factorization object `mathcal F_X^{hyb}` with all ordered mixed correspondences, quotient residuals, and protected integration residuals.
7. Lift normal ordering from lattice level to chain-level Hall descent with `mathfrak o_Theta^top=0`.
8. Prove primitive recognition against `mathfrak g_{Delta_5}` at presentation level, including finite-window radical, no-extra-relations, and PBW.
