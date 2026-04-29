# Agent 01 stable-core extraction report

Source mined: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`.

Scope: core stable-core extraction only.  Attacker prose is treated as adversarial testimony, not proof.  A claim is marked stable only when it is either present in `main.tex` with a local argument, or present in `main.tex` as an explicitly imported theorem with a named citation route in `proj.bib`.  I did not independently reprove the imported Gritsenko--Nikulin, Oberdieck--Pandharipande, Clery--Gritsenko, Govindarajan, or Andrianov results.

Status tags:

- `stable/current`: current `main.tex` already states the attack-stable version.
- `imported/current`: current `main.tex` imports the result from cited literature; primary-source verification remains separate.
- `conditional/current`: current `main.tex` correctly leaves the item as a certificate, criterion, or open problem.
- `missing`: the attack demands a replacement object or theorem not currently present.
- `stale-risk`: current `main.tex` contains quarantined or older material that may still confuse the theorem spine.
- `unverified`: attacker-supplied claim not established by the files I checked.

## 1. Stable core

| ID | Stable claim | Current status | Main anchors | Verification grade |
|---|---|---|---|---|
| SC-01 | The K3 protected elliptic genus is the input: \(Z_{\mathrm{K3}}=2\phi_{0,1}\).  The Borcherds lift uses only a Grothendieck \(K_0\) half-index representative, not a canonical half-Hilbert space. | stable/current | `main.tex:214`, `main.tex:405`, `main.tex:722` | TeX-local formulation checked; no physical Hilbert claim allowed. |
| SC-02 | The virtual one-particle determinant attached to the \(K_0\) half-index is a normalized Borcherds product \(D_X\), and \(D_X=\Delta_5\). | imported/current | `main.tex:640`, `main.tex:818`, `main.tex:833`, `main.tex:2530`, `main.tex:2601` | Imported through Borcherds/Gritsenko--Nikulin route; primary-source check not performed here. |
| SC-03 | The monic normalization is \(D_5=64^{-1}\Delta_5\), so the denominator normalization is \(D_5(2Z)=64^{-1}\Delta_5(2Z)\). | imported/current | `main.tex:2530`, `main.tex:2560`, `main.tex:5614`, `main.tex:13543` | Imported/current; constants match attack-stable form. |
| SC-04 | The denominator algebra target is the Gritsenko--Nikulin BKM Lie superalgebra with signed multiplicities and denominator \(64^{-1}\Delta_5(2Z)\). | imported/current | `main.tex:298`, `main.tex:5560`, `main.tex:5590`, `main.tex:5614`, `main.tex:13416`, `main.tex:13543` | Imported; does not prove compact Hall brackets, source states, or parity dimensions. |
| SC-05 | Denominator equality determines signed superdimensions only.  It does not determine a compact Hall algebra, brackets, PBW/no-extra-relations, Hopf radical, or even/odd dimensions. | stable/current | `main.tex:13603`, `main.tex:13652`, `main.tex:12804`, `main.tex:14181` | TeX-local separation checked. |
| SC-06 | The first timelike \(29\mid 93\) datum is target-side denominator/presentation data, not a compact-source computation. | stable/current, with source verification open | `main.tex:12838`, `main.tex:13158`, `main.tex:13209` | Current text marks target-side/certificate dependency; arithmetic/source check still needed. |
| SC-07 | OP/reduced DT/PT supplies a scalar square \(Z_{\mathrm{OP}}=-4096\,\Delta_5^{-2}\) in the stated normalization. | imported/current | `main.tex:13724`, `main.tex:13806`, `main.tex:13857`, `main.tex:13957`, `main.tex:14031` | Imported through OP/DT/PT route; primary-source check not performed here. |
| SC-08 | The scalar \(-4096\), the factor \(64^2\), and the OP square do not determine orientation data, Pfaffian signs, or the reflection-sign character \(\epsilon_o\). | stable/current | `main.tex:312`, `main.tex:13857`, `main.tex:13885`, `main.tex:13924` | TeX-local separation checked. |
| SC-09 | The D6--D2--D0 dictionary uses the Mukai--Gram triple \((\beta^2/2,n,d-1)\), and for \(\beta_h^2=2h-2\) this is \((h-1,n,d-1)\). | stable/current | `main.tex:2634`, `main.tex:2661` | TeX-local lemma checked; this repairs the attacked fourfold/Todd misstatement. |
| SC-10 | The formal dyonic charge sector used here is \(\Lambda_S\oplus\Lambda_S\) with Gram projection \(\Pi_X(Q,P)=(Q^2/2,Q\cdot P,P^2/2)\).  It is not the full four-dimensional \(\mathcal N=4\) charge lattice. | stable/current | `main.tex:4310`, `main.tex:4316`, `main.tex:4340` | TeX-local caveat checked. |
| SC-11 | Raw Gram projection is not additive.  The additive repair is the normal-ordered central extension by the symmetric bilinear \(B\), with \(\overline{\Pi}_X(c,T)=\Pi_X(c)-T\). | stable/current | `main.tex:4590`, `main.tex:4614`, `main.tex:4832`, `main.tex:4863` | TeX-local algebra checked at statement level. |
| SC-12 | Every Gram triple has a primitive formal lift in two hyperbolic planes, but this proves only formal/lattice surjectivity, not effective compact Hall support. | stable/current | `main.tex:4523`, `main.tex:4977` | TeX-local formulation checked. |
| SC-13 | Strict fixed-lift raw Gram descent cannot realize the type-II real-root strings; normal ordering is forced. | stable/current | `main.tex:146`, `main.tex:4883` | TeX-local theorem checked.  Caveat retained: special isolated \(B\)-isotropic channels or fibre-summed raw constructions are not ruled out. |
| SC-14 | The correct primitive-recognition target is after normal-ordered charge descent and primitive/Hopf/radical recognition, not raw \(H^0\operatorname{Prim}\) by itself. | conditional/current | `main.tex:260`, `main.tex:11750`, `main.tex:12124`, `main.tex:12479`, `main.tex:12590` | Current text leaves this as a certificate/open comparison. |
| SC-15 | A Dirac--Igusa realization requires data \((L_X,H_X,O_X,D_X,R_X)\), not only a product identity, scalar square, formal current envelope, or orientation line. | conditional/current | `main.tex:882`, `main.tex:11750`, `main.tex:13276` | Current text correctly treats compact realization as open/certificated. |
| SC-16 | The formal current envelope on \(E\) is a target/internal object, not a compact microscopic BPS source. | stable/current | `main.tex:5704`, `main.tex:5724`, `main.tex:5743`, `main.tex:6404`, `main.tex:6452` | TeX-local source/target firewall checked. |
| SC-17 | Positive elliptic degree is a projection-to-\(E\) support-locality obstruction: ordinary projection-finite \(\operatorname{Ran}(E)\) sees only finite projection support, while positive elliptic degree projects to all of \(E\). | stable/current | `main.tex:160`, `main.tex:240`, `main.tex:498`, `main.tex:7039`, `main.tex:7082`, `main.tex:7103`, `main.tex:7121` | TeX-local statement checked. |
| SC-18 | The finite-first/hybrid wrapped repair is the admissible shape for compact source work: finite windows, finite kernels, projection-finite local sector plus wrapped/global elliptic-degree data. | conditional/current | `main.tex:6192`, `main.tex:6281`, `main.tex:7039`, `main.tex:7121`, `main.tex:8254`, `main.tex:9973`, `main.tex:11518` | Current text states certificates/protocols; construction remains open. |
| SC-19 | Connected \(E\)-descent and finite-stabilizer descent must be separated.  For connected \(E\), the relevant \(BE\) cohomology correction gives no \(H^1(BE)\) obstruction; finite \(E[N]\) and \(E[2]\) require separate linearization criteria. | stable/current | `main.tex:3197`, `main.tex:3395` | TeX-local correction checked. |
| SC-20 | Eight-row diagonal-divisor material and CHL/fractional rows require per-row certificates and are separate from the \(N=1\) theorem spine unless explicitly certified. | conditional/current | `main.tex:14269`, `main.tex:14289`, `main.tex:14461`, `main.tex:14473`, `main.tex:14505`, `main.tex:15866`, `main.tex:16028` | Current text has certificate separation. |
| SC-21 | The spin \(L\)-factor computation, if retained, is independent of the BKM/compact-construction spine. | stale-risk/current | `main.tex:14558`, `main.tex:14678` | Current appendix states independence, but the attack repeatedly recommends moving or quarantining it harder. |
| SC-22 | The strongest honest paper spine is a normalization-and-separation theorem: \(K_0\) determinant \(\to \Delta_5\), GN denominator target, OP scalar square, normal-ordered charge algebra, compact realization open/conditional. | stable/current | `main.tex:58`, `main.tex:177`, `main.tex:390`, `main.tex:14031` | Current abstract/status table mostly matches this spine. |

## 2. Destroyed/forbidden claims

The following claims are forbidden by the attack analysis and should not survive in prose, theorem names, diagrams, abstracts, or conclusion-level implication chains.

| ID | Destroyed or forbidden claim | Current map |
|---|---|---|
| DC-01 | \((n,l,m)\) is an additive physical Hall charge. | Replaced by formal/physical charge lattice plus Gram projection at `main.tex:4316`, `main.tex:4431`, `main.tex:4590`. |
| DC-02 | The \(K_0\) half-index is a canonical physical half-Hilbert space, canonical parity split, or one-particle compact BPS Hilbert space. | Rejected at `main.tex:214`, `main.tex:722`, `main.tex:772`, `main.tex:853`. |
| DC-03 | The determinant constructs a compact BPS operator, compact Pfaffian, or compact Hilbert model. | Rejected at `main.tex:853`, `main.tex:5704`, `main.tex:13652`. |
| DC-04 | The paper gives a new independent construction of \(\Delta_5\) rather than recognizing the GN/Borcherds product under the chosen normalization. | Current text imports/recognizes at `main.tex:2530`, `main.tex:5614`. |
| DC-05 | \(D_X=\Delta_5\) implies the compact Dirac--Igusa object \(\mathfrak D_X\). | Rejected by certificate/open-problem framing at `main.tex:882`, `main.tex:11750`, `main.tex:13276`. |
| DC-06 | \(\Delta_5^2\), \(-4096\), or \(64^2\) implies orientation, Pfaffian sign, or \(\epsilon_o\). | Rejected at `main.tex:312`, `main.tex:13885`, `main.tex:13924`. |
| DC-07 | Denominator equality implies compact Hall brackets, PBW/no-extra-relations, primitive source equality, Hopf radical identification, or even/odd dimensions. | Rejected at `main.tex:12124`, `main.tex:13603`, `main.tex:13652`. |
| DC-08 | Raw \(\Pi_X\)-pushforward of compact Hall primitives is the recognition theorem. | Rejected by normal-ordered target and raw no-go at `main.tex:4614`, `main.tex:4883`, `main.tex:4977`. |
| DC-09 | \(m=0\) terms are microscopic one-particle K3 states. | Replaced by bulk/cusp split at `main.tex:772` and cusp/Weyl-boundary language at `main.tex:782`-`main.tex:815`. |
| DC-10 | `Sp_4` is the full physical U-duality group for the compact problem. | Caveated at `main.tex:265` and `main.tex:4340`: formal sector is not full \(\mathcal N=4\) charge lattice. |
| DC-11 | Connected \(E\)-equivariance automatically descends all quotient categories, or \(H^1(BE)\) supplies the attacked obstruction. | Replaced by `main.tex:3197` and finite-stabilizer criteria at `main.tex:3395`. |
| DC-12 | A small-orbit gerbe vanishing lemma proves finite \(E[2]\)-descent without explicit linearization data. | Replaced by the Klein-four criterion at `main.tex:3395`; source construction still conditional. |
| DC-13 | Bott periodicity, a Grothendieck--Witt sign convention, or choice of Bott element explains \(B(c,c)=2\Pi_X(c)\). | Current text explicitly denies this at `main.tex:2523`. |
| DC-14 | Underdefined "holomorphic \(E_3\)" or "K3-to-\(E\) specialization" proves compact factorization. | Current text treats these as layered placeholders/certificates/open constructions at `main.tex:5770`, `main.tex:5981`, `main.tex:6024`, `main.tex:6317`. |
| DC-15 | The locality problem is a generic failure of six-dimensional locality. | Replaced by projection-to-\(E\) support-locality obstruction at `main.tex:7082`. |
| DC-16 | Formal current envelope equals compact microscopic source. | Rejected at `main.tex:5709`, `main.tex:5743`, `main.tex:6452`. |
| DC-17 | Row maps, fractional roots, or diagonal-divisor extensions are valid without row-specific physical-host certificates. | Current row section adds certificate levels at `main.tex:14289`, `main.tex:14473`, `main.tex:15866`, `main.tex:16028`. |
| DC-18 | Spin \(L\)-factor material is part of the core BKM/compact construction. | Current text says independent at `main.tex:14678`; attack still recommends removal/quarantine. |
| DC-19 | Orientation existence alone constructs protected Hall integration. | Current text separates orientation, integration, and primitive recognition at `main.tex:2801`, `main.tex:2817`, `main.tex:2914`, `main.tex:11750`. |
| DC-20 | A source Koszul/bar object may be defined by pulling it from the target current envelope. | Current text states source-target separation at `main.tex:6404`, `main.tex:6452`, `main.tex:6506`. |

## 3. Required replacement claims

| ID | Required replacement | Current status |
|---|---|---|
| RC-01 | Replace one-lattice prose with a layered lattice ontology: formal dyonic/Mukai charge \(\Gamma_X^{\mathrm{form}}\), Gram lattice \(\Gamma_{\mathrm{gram}}\cong\mathbb Z^3\), normal-ordered extension \(\widehat\Gamma_X\) or equivalent, effective Hall support, and separate full \(\mathcal N=4\) charge lattice. | Mostly present at `main.tex:4316`, `main.tex:4431`, `main.tex:4614`, `main.tex:4832`; notation could be normalized. |
| RC-02 | Replace raw Gram descent by normal-ordered charge descent using the \(B\)-cocycle; treat \(\Theta\) as categorified normal-ordering data, not scalar sign magic. | Present at `main.tex:4614`, `main.tex:4832`, `main.tex:8348`, `main.tex:8460`, `main.tex:8603`. |
| RC-03 | Replace "compact BPS partition function" by "virtual Borcherds determinant" unless a compact-source certificate is actually supplied. | Present in spirit at `main.tex:818`, `main.tex:853`, `main.tex:13652`; no `Z_{\mathrm{BPS}}` string found in current draft. |
| RC-04 | Replace "half-index Hilbert space" by arbitrary Grothendieck representative with prescribed superdimension. | Present at `main.tex:722`. |
| RC-05 | Replace "OP square proves orientation" by scalar-square theorem plus separate orientation-character/Pfaffian-sign open problem. | Present at `main.tex:13806`, `main.tex:13885`, `main.tex:13924`. |
| RC-06 | Replace attacked D6-D2-D0/Todd/fourfold statement with the Mukai--Gram dictionary \((\beta^2/2,n,d-1)\). | Present at `main.tex:2661`; should remain a headline theorem if the manuscript is reorganized. |
| RC-07 | Replace equivariant-descent shortcuts by connected \(E\)-descent plus finite-stabilizer linearization criteria. | Present at `main.tex:3197`, `main.tex:3395`. |
| RC-08 | Replace "primitive recognition theorem" by a recognition certificate requiring simple-root lifts/parities, bracket constants, BK relations, Hopf pairing/radical, generation, PBW, exact completion, and full parity dimensions. | Present at `main.tex:12124`; finite/cofinal version at `main.tex:12479`, `main.tex:12590`. |
| RC-09 | Replace "source constructed from target current envelope" by a source-target firewall: target bar-cobar/counit is internal; source Koszul data must be supplied independently. | Present at `main.tex:6404`, `main.tex:6452`, `main.tex:6506`, `main.tex:6970`. |
| RC-10 | Replace generic factorization-locality prose by hybrid wrapped factorization: projection-finite local sectors plus wrapped positive-elliptic-degree sectors. | Present/conditional at `main.tex:7039`, `main.tex:7082`, `main.tex:7121`, `main.tex:8254`. |
| RC-11 | Replace infinite completed assertions by finite-first certificates: finite windows, finite kernels, finite residuals, inverse-system/exact-completion passage only after hypotheses. | Present/conditional at `main.tex:9973`, `main.tex:11518`, `main.tex:12479`. |
| RC-12 | Add or strengthen a forbidden-implications table: \(D_X=\Delta_5\not\Rightarrow\mathfrak D_X\), \(\Delta_5^2\not\Rightarrow\epsilon_o\), \(g_{\Delta_5}\not\Rightarrow\) compact Hall source. | Partly present in prose at `main.tex:13603`, `main.tex:13885`, `main.tex:14031`; attack wants this as an explicit structural table. |
| RC-13 | Latest attack replacement: construct a curve-universal algebraic Dirac--Igusa object \(D^{\mathrm{alg}}_{\Delta_5,C,L}\) directly from the GN BKM algebra and normal-ordered charge extension, with a specified curve \(C\) and linear lift \(L\). | missing.  `rg` found formal-current-envelope language but no `D^{alg}`, `Dalg`, `curve-universal`, or `linear lift` object in `main.tex`. |
| RC-14 | Latest attack replacement: construct a geometric normal-ordered pre-Hall correspondence source \(H^{\mathrm{pre}}_{X,\Gamma}\) from derived moduli stacks and exact-triangle correspondences before orientation/integration. | missing/stale.  Current text has source interfaces/certificates, not a named constructed `Hpre` object. |
| RC-15 | Latest attack replacement: construct an orientation-gerbe-twisted protected Hall object \(H^{\mathrm{tw}}_{X,\Gamma}\) over the square-root gerbe, without requiring global orientation trivialization. | missing.  `rg` found no `Htw`, `twisted protected`, or `orientation-gerbe` constructed object. |
| RC-16 | Put the actual compact Dirac--Igusa realization only after the twisted source has a normal-ordered primitive algebra and a source-to-target comparison theorem. | Current text is conditional/open at `main.tex:11750`, `main.tex:12124`, `main.tex:13276`; latest attack wants the predecessor objects constructed first. |
| RC-17 | Treat comparison \(\Pi_{X,*}H^0\operatorname{Prim}_{\mathrm{prot}}(H^{\mathrm{tw}})/\operatorname{Rad}\cong\mathfrak g_{\Delta_5}\) as a theorem to prove, not a definition. | Missing in this exact object language; analogous certificate appears at `main.tex:12124`. |
| RC-18 | Keep eight-row, CHL, fractional-root, and spin \(L\)-factor material outside the core theorem spine unless row certificates are supplied. | Partly present; appendix still a stale-risk at `main.tex:14558`. |

## 4. Current `main.tex` anchors

High-signal anchors for the stable-core integration owner:

- Abstract/status spine: `main.tex:58`, `main.tex:177`, `main.tex:214`, `main.tex:226`, `main.tex:260`, `main.tex:298`, `main.tex:312`, `main.tex:339`, `main.tex:390`.
- K3 \(K_0\) determinant: `main.tex:640`, `main.tex:667`, `main.tex:695`, `main.tex:722`, `main.tex:743`, `main.tex:772`, `main.tex:818`, `main.tex:833`, `main.tex:853`, `main.tex:882`.
- Normalized cusp/GN product: `main.tex:2383`, `main.tex:2530`, `main.tex:2560`, `main.tex:2601`.
- D6--D2--D0 and equivariant descent: `main.tex:2634`, `main.tex:2661`, `main.tex:2760`, `main.tex:2801`, `main.tex:2817`, `main.tex:2914`, `main.tex:3197`, `main.tex:3395`.
- Charge descent and normal ordering: `main.tex:4310`, `main.tex:4316`, `main.tex:4431`, `main.tex:4489`, `main.tex:4523`, `main.tex:4590`, `main.tex:4614`, `main.tex:4832`, `main.tex:4863`, `main.tex:4883`, `main.tex:4977`.
- Denominator algebra: `main.tex:5560`, `main.tex:5590`, `main.tex:5614`, `main.tex:12804`, `main.tex:12838`, `main.tex:13416`, `main.tex:13543`, `main.tex:13603`, `main.tex:13652`.
- Compact/source interfaces: `main.tex:5704`, `main.tex:5724`, `main.tex:5743`, `main.tex:5770`, `main.tex:5981`, `main.tex:6024`, `main.tex:6142`, `main.tex:6192`, `main.tex:6234`, `main.tex:6281`, `main.tex:6317`.
- Source-target firewall and hybrid locality: `main.tex:6404`, `main.tex:6452`, `main.tex:6506`, `main.tex:6731`, `main.tex:6970`, `main.tex:7039`, `main.tex:7082`, `main.tex:7103`, `main.tex:7121`, `main.tex:8254`.
- Normal-ordered protected source certificates: `main.tex:8305`, `main.tex:8348`, `main.tex:8460`, `main.tex:8603`, `main.tex:9973`, `main.tex:11518`.
- Dirac--Igusa and primitive recognition certificates: `main.tex:11750`, `main.tex:12124`, `main.tex:12479`, `main.tex:12590`, `main.tex:13276`.
- Scalar square: `main.tex:13701`, `main.tex:13724`, `main.tex:13806`, `main.tex:13857`, `main.tex:13885`, `main.tex:13924`, `main.tex:13957`, `main.tex:14031`.
- Rows/appendix: `main.tex:14269`, `main.tex:14289`, `main.tex:14339`, `main.tex:14461`, `main.tex:14473`, `main.tex:14505`, `main.tex:14558`, `main.tex:14678`, `main.tex:14986`, `main.tex:15470`, `main.tex:15582`, `main.tex:15841`, `main.tex:15866`, `main.tex:15893`, `main.tex:15952`, `main.tex:15972`, `main.tex:16028`.

Absence checks performed:

- No current `main.tex` occurrence of `D^{alg}`, `Dalg`, `H^{pre}`, `Hpre`, `H^{tw}`, `Htw`, `curve-universal`, `linear lift`, `orientation-gerbe`, or `twisted protected`.
- No current `main.tex` occurrence of `Z_{\mathrm{BPS}}`.
- Current `main.tex` still has a spin \(L\)-factor appendix beginning at `main.tex:14558`, with independence caveat at `main.tex:14678`.
- Current `main.tex` denies Bott-periodicity/sign-convention explanation of \(B(c,c)=2\Pi_X(c)\) at `main.tex:2523`.

## 5. Exact rewrite consequences

1. The core theorem spine should stay as a normalization-and-separation spine: \(K_0\) half-index determinant, GN/Borcherds product, GN denominator target, normal-ordered charge algebra, OP scalar square, and compact realization as certificate/open theorem.

2. Any prose that says or suggests "compact BPS partition function", "compact BPS Hilbert space", "operator determinant", or "Pfaffian" must be rewritten to "virtual Borcherds determinant" unless the compact-source certificate is explicitly supplied in the same statement.

3. Any implication chain
   \[
   D_X=\Delta_5\Rightarrow \mathfrak D_X,\qquad
   \Delta_5^2\Rightarrow \epsilon_o,\qquad
   \mathfrak g_{\Delta_5}\Rightarrow\text{compact Hall source}
   \]
   must be deleted or converted into a forbidden-implications table.

4. The \(m=0\) part of the product must remain a cusp/Weyl-boundary datum, not a microscopic one-particle K3 state sector.

5. The charge discussion must keep the raw physical/formal lattice, the Gram lattice, and the normal-ordered extension distinct.  The correct recognition target is after normal-ordered descent and radical/PBW/parity certificate, not raw \(\Pi_X\)-pushforward.

6. The no-go theorem for strict fixed-lift raw Gram descent should remain close to the normal-ordered construction.  It is the reason normal-ordering is forced, not an optional embellishment.

7. The D6--D2--D0 Mukai--Gram dictionary should be promoted or preserved as a headline theorem/lemma.  It repairs a high-severity attacked error and supplies the variable dictionary for later scalar-square comparison.

8. The OP scalar-square section must remain after the determinant/denominator normalization and must explicitly say the scalar square is orientation-forgetful.

9. The E-equivariant descent section must keep connected \(E\), finite \(E[N]\), and \(E[2]\) linearization separate.  No quotient-before-correspondence shortcut should be reintroduced.

10. The compact source sections must maintain finite-first discipline: finite Hall windows, finite kernels, finite residuals, and only then exact/completed limits.

11. If the latest attack program is adopted, the manuscript needs a new object-level split before the compact realization theorem:
    - \(D^{\mathrm{alg}}_{\Delta_5,C,L}\): algebraic/curve-universal target object from GN BKM plus normal-ordered charge extension.
    - \(H^{\mathrm{pre}}_{X,\Gamma}\): geometric normal-ordered pre-Hall correspondence source before orientation.
    - \(H^{\mathrm{tw}}_{X,\Gamma}\): orientation-gerbe-twisted protected Hall object before global orientation trivialization.
    - Only after these may one state the compact Dirac--Igusa comparison as a theorem to prove.

12. The formal current envelope should not be allowed to function as the missing \(D^{\mathrm{alg}}_{\Delta_5,C,L}\) unless it is renamed/rebuilt with the curve \(C\), lift \(L\), and universal algebraic structure specified.

13. The source Koszul/bar construction must not be defined from the target current envelope.  It must be an independent source-side datum with a later comparison.

14. Hybrid wrapped factorization must be stated as projection-finite local plus wrapped/global positive-elliptic-degree structure.  Avoid generic "locality obstruction" language.

15. Eight-row, CHL, fractional-root, and spin \(L\)-factor material should be either moved to companion/appendix status or guarded by explicit row-level certificates.  The spin \(L\)-factor appendix is currently quarantined but still a narrative liability.

16. The label/prose around Bott normalization should stay in the negative form currently at `main.tex:2523`; do not reintroduce Bott as an explanation for the Gram cocycle.

## 6. Residual obligations

| ID | Obligation | Current state |
|---|---|---|
| RO-01 | Primary-source verification of the exact GN/Borcherds normalization \(D_X=\Delta_5\) and \(64^{-1}\Delta_5(2Z)\). | Not done by Agent 01; `proj.bib` has GN/Borcherds entries. |
| RO-02 | Primary-source verification of OP/DT/PT scalar normalization \(Z_{\mathrm{OP}}=-4096\Delta_5^{-2}\). | Not done by Agent 01; `proj.bib` has OP-related entries. |
| RO-03 | Independent verification of the first timelike \(29\mid 93\) target count and any finite-window compact source residuals. | Not done; current text marks as target/certificate dependent. |
| RO-04 | Actual construction of \(D^{\mathrm{alg}}_{\Delta_5,C,L}\), if the latest attack repair is adopted. | Missing. |
| RO-05 | Actual construction of \(H^{\mathrm{pre}}_{X,\Gamma}\) as a derived-moduli/exact-triangle correspondence source before orientation. | Missing/stale; current text has interfaces and certificates. |
| RO-06 | Actual construction of \(H^{\mathrm{tw}}_{X,\Gamma}\) over the square-root orientation gerbe without assuming global orientation trivialization. | Missing. |
| RO-07 | Source-to-target comparison theorem \(\Pi_{X,*}H^0\operatorname{Prim}_{\mathrm{prot}}(H^{\mathrm{tw}})/\operatorname{Rad}\cong\mathfrak g_{\Delta_5}\). | Open/certificate only. |
| RO-08 | Compact orientation character \(\epsilon_o\): local Pfaffian signs, reflection values, and monodromy character. | Open at `main.tex:2914` and related scalar-square caveats. |
| RO-09 | Chain-level normal-ordered Hall/factorization descent, not just formal charge extension. | Conditional at `main.tex:8305`, `main.tex:8603`. |
| RO-10 | Hybrid wrapped compact source construction for positive elliptic degree. | Open/certificate at `main.tex:8254`. |
| RO-11 | Source-side Koszul/bar coalgebra independent of target current envelope. | Certificate framework exists; construction/comparison remains residual. |
| RO-12 | Full parity dimensions, simple representatives, bracket constants, BK relations, no-extra-relations, PBW, Hopf radical, generation, and exact completion for primitive recognition. | All required by `main.tex:12124`; not supplied globally. |
| RO-13 | Decide whether fibre-summed raw descent or special \(B\)-isotropic raw channels have any limited admissible role. | Raw fixed-lift no-go does not rule these out. |
| RO-14 | Decide the role of the spin \(L\)-factor appendix in the final paper. | Current text declares independence; attack recommends moving/quarantining harder. |
| RO-15 | Decide whether row/fractional-root material is core, appendix, or companion. | Current text has certificates but remains large relative to core theorem spine. |
| RO-16 | Verify that no future edits reintroduce destroyed claims through theorem names, captions, abstract prose, or section summaries. | Requires post-integration grep/review. |

## 7. Verification needed

1. Run a post-integration grep for banned implication language:
   - `compact BPS Hilbert`
   - `operator determinant`
   - `Pfaffian` near `Delta_5` or `-4096`
   - `orientation` near `64` or `-4096`
   - `raw pushforward`
   - `full U-duality`
   - `one-particle K3`

2. Run a post-integration grep for required replacement objects if the latest attack program is accepted:
   - `D^{alg}` or an agreed TeX spelling of \(D^{\mathrm{alg}}_{\Delta_5,C,L}\)
   - `H^{pre}` or an agreed TeX spelling of \(H^{\mathrm{pre}}_{X,\Gamma}\)
   - `H^{tw}` or an agreed TeX spelling of \(H^{\mathrm{tw}}_{X,\Gamma}\)
   - `orientation gerbe`
   - `linear lift`
   - `curve-universal`

3. Verify imported constants against primary sources:
   - Borcherds/Gritsenko--Nikulin normalization for \(\Delta_5\) and \(64^{-1}\Delta_5(2Z)\).
   - OP/DT/PT branch and scalar sign for \(-4096\Delta_5^{-2}\).
   - Clery--Gritsenko/Govindarajan row formulas if rows remain.
   - Andrianov spinor \(L\)-factor if appendix remains.

4. Verify the mathematical proof of the normal-ordered extension, especially associativity, commutativity, inverse, and the homomorphism property of \(\overline{\Pi}_X\), after any notation normalization.

5. Verify that the D6--D2--D0 Mukai--Gram dictionary remains consistent with every later variable table and scalar-square substitution.

6. Verify the finite-stabilizer \(E[N]\)/\(E[2]\) criteria against the actual moduli-stack correspondences, not only group cohomology bookkeeping.

7. Verify that all source-side compact claims are finite-first: finite Hall stages first, finite residual checks, exact completion only after transition compatibility.

8. Verify that the final build succeeds after any integration edits.  Agent 01 did not edit `main.tex` and therefore did not run a TeX build.
