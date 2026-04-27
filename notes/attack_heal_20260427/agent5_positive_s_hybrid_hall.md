# Agent 5: Positive \(s\)-Direction and Hybrid Hall Obstruction

Date: 2026-04-27.
Scope: read-only attack/heal audit. Only this report was created.

## Claim Attacked

The attacked shortcut is:

> ordinary support-local factorization on \(\operatorname{Ran}(E)\), possibly after appending a Fock/Hecke determinant factor, realizes the positive elliptic-degree \(s\)-direction of the Igusa product and therefore supplies the compact Hall/chiral primitive bracket.

This shortcut is false. The manuscript already heals it. The positive elliptic-degree sector is global over \(E\), not finite-support local over \(\operatorname{Ran}(E)\). A Fock/Hecke product can reproduce a determinant shadow, but it does not give mixed local/wrapped Hall brackets unless actual mixed correspondences are constructed before quotienting by \(E\).

## Verdict

No fatal overclaim found in `main.tex`.

The current manuscript correctly states:

- no microscopic compact BPS Hilbert space/operator product is constructed;
- no compact finite-first holomorphic \(E_3\)-factorization algebra on \(K3\times E\) is constructed;
- naive \(\operatorname{Ran}(E)\) locality sees only projection-finite sectors;
- positive elliptic degree requires global Fock/Hecke modes with mixed Hall action, or a hybrid local/global wrapped theory;
- both repair paths remain open;
- the determinant/product does not determine Hall constants, parity dimensions, PBW/no-extra-relations, or compact local physics.

## Geometric Obstruction

Anchor: `main.tex:2085-2115`.

Let \(p_E:K3\times E\to E\). If \(C\subset K3\times E\) is one-dimensional and
\[
(p_E)_*[C]=b[E],\qquad b>0,
\]
then \(p_E(C)=E\). If the image were zero-dimensional, the pushforward one-cycle would vanish. Since \(p_E\) is proper, the image is closed; a one-dimensional closed subset of the irreducible curve \(E\) is all of \(E\). For reducible or nonreduced \(C\), positive pushforward means at least one curve component dominates \(E\), hence the support image is still \(E\).

Repair recommendation: optional micro-edit only. In the proof of Lemma `lem:elliptic-degree-locality-obstruction`, add the words "since \(p_E\) is proper" before using closedness of \(p_E(C)\). The argument is otherwise sound.

## Local Anchors

- `CLAUDE.md:19-21`: cross-repo consistency and honest epistemic status are required.
- `main.tex:90-92`: denominator algebra does not supply compact Hall correspondences, orientation, or collision maps.
- `main.tex:108-118`: compact realization would require \(E_3\), \(K3\)-to-\(E\) specialization, mixed local/wrapped correspondences, and primitive bracket; this is open.
- `main.tex:170-191`: compact/hybrid factorization paragraph explicitly marks the positive \(s\)-direction repair as open.
- `main.tex:335-371`: \(\Phi^{\mathrm{FA}}_3(X)\) is only a placeholder; positive elliptic degree projects to all \(E\); Fock/Hecke or hybrid repair is required.
- `main.tex:546-588`: the \(m>0\) Hecke-DMVV/Fock sector is a \(K_0\)-level virtual determinant construction.
- `main.tex:617-657`: the determinant does not construct Hilbert space, vertex algebra, \(E_3\)-factorization, chiral factorization, locality, operator products, or Hilbert completion.
- `main.tex:1917-1990`: the compact \(E_3\) source and \(K3\)-to-\(E\) specialization are open finite-chain data; positive elliptic-degree repair is listed as a required item.
- `main.tex:2072-2180`: projection-finite/wrapped definitions, locality obstruction lemma, naive Ran corollary, repair alternatives, and open problem `op:hybrid-wrapped-factorization`.
- `main.tex:2298-2309`: global Fock/Hecke or hybrid wrapped-sector data are part of the compact datum, not operations constructed from the determinant.
- `main.tex:2323-2327`: Hall atlas must include local-local, wrapped-wrapped, and mixed local/wrapped correspondences before quotienting by \(E\).
- `main.tex:2467-2550`: recognition theorem does not prove compact Hall constants, parity dimensions, simple representatives, BKM relations, PBW, or radical closedness; determinant does not encode these.
- `main.tex:2553-2567`: compact \(E_3\), Hall, and chiral Koszul realization is an open problem.
- `main.tex:2801-2818`: index equality is not a state-space or operator-product identification.
- `main.tex:3028-3048`: synthesis theorem repeats the \(s\)-direction obstruction and orientation requirement.
- `main.tex:3101-3115`: proof states compact comparison is not used; Ran obstruction and missing Hall data remain separate.

## Bibliography Anchors

- `proj.bib:253-275`: Kontsevich-Soibelman and Davison-Meinhardt provide CoHA language, not this compact \(K3\times E\) Hall object.
- `proj.bib:277-304`: Costello and Costello-Gwilliam provide factorization/BV language used for the open finite-chain requirements.
- `proj.bib:319-347`: DMVV and Harvey-Moore support the second-quantized/Fock and BPS-index background; they do not supply mixed compact Hall correspondences.

## Vol III Cross-Check

Exact search in `~/calabi-yau-quantum-groups/FRONTIER.md` for `positive elliptic`, `elliptic-degree`, `s-direction`, `projection-finite`, `support-local`, `mixed local/wrapped`, `Hecke/Fock`, and `Fock/Hecke` returned no hits. The explicit obstruction is therefore carried by this manuscript, not by a Vol III theorem.

Relevant Vol III anchors:

- `FRONTIER.md:9-17`: Vol III targets still ask for chain-level \(\mathrm{Sp}^{\mathrm{ch}}_{K3,E}\) and non-abelian hCS pushforward; they are targets, not completed compact Hall data.
- `FRONTIER.md:81`: bracket-level BPS \(\cong\) BKM remains open beyond the abelian Heisenberg-Miki core.
- `FRONTIER.md:98-110`: Hall-Drinfeld language is the architectural target; non-abelian BKM appears only after vertex-operator closure.
- `FRONTIER.md:197-211`: real-root completion, comparison data, and precise factorization-homology theorem remain open.
- `FRONTIER.md:688-690`: the \(K3\times E\) reduction gives a K3-fibre/Heisenberg-to-Borcherds route on the principal locus, not compact hCS-to-Hall comparison or Hall-Drinfeld construction.
- `FRONTIER.md:710-724`: checked K3 current/Yangian data do not supply the completed Hall-Drinfeld/BKM object, quasi-Hopf coproduct, associator, or \(R\)-matrix.

No cross-volume contradiction found. The manuscript correctly prevents false transfer from Vol III architectural language into an existence theorem here.

## Attack-Heal Status

Failure mode attacked: ordinary \(\operatorname{Ran}(E)\) locality plus a decoupled Fock/Hecke determinant factor.

Result: fatal for the shortcut, non-fatal for the manuscript. The manuscript already states the healed theorem shape:

1. projection-finite local Hall/chiral factorization on \(\operatorname{Ran}(E)\) plus global Fock/Hecke modes coupled by mixed Hall actions; or
2. a hybrid local/global wrapped factorization theory with \(\mathcal M^{\mathrm{loc}}\), \(\mathcal M^{\mathrm{wr}}\), and \(\mathfrak E^{\mathrm{hyb}}\), associative over flags, Thom-Sebastiani oriented, compatible with protected integration, and constructed before the reduced \(E\)-quotient.

Recommendation: no substantive manuscript repair required for Agent 5. Optional improvement: insert the properness phrase in the locality-obstruction proof and retain all current open-problem language.

## Tests and Searches Run

- `rg` for `s-direction`, `elliptic degree`, `wrapped`, `mixed`, `Hecke`, `Fock`, `projection`, `Ran(E)`, `support-local`, `positive elliptic`, `local/wrapped`, `Hall`, `BPS`, `factorization`.
- `sed`/`nl` reads of `CLAUDE.md`, `main.tex`, `proj.bib`, `~/ecosystem/INVARIANTS.md §IV`, `~/ecosystem/AGENTS-HARNESS.md §VIII`, and `~/calabi-yau-quantum-groups/FRONTIER.md`.
- No build run. No tests needed; this is a textual/proof-status audit.

## Remaining Open Questions

1. Construct actual Hecke/Fock functors, not just exponents, and prove their mixed Hall action on projection-finite sectors.
2. Build the wrapped moduli \(\mathcal M^{\mathrm{wr}}\) and mixed extension stacks \(\mathfrak E^{\mathrm{hyb}}\) before quotienting by \(E\).
3. Prove associativity over two-step local/wrapped flags with Thom-Sebastiani orientation transport.
4. Compute the first nontrivial mixed primitive brackets and compare them with the denominator-algebra constants.
