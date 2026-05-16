# Tenth reconstitution attack-heal: late-PDF construction extraction

Date: 2026-04-28.

Source under attack: `materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt`.

## Construction anchors extracted

- Finite charge window: lines 13840-13896 and 15153-15203.  Input
  \((X=S\times E,\sigma,S,R)\); compute finite semistable charge set
  \(F_{\sigma,S}(R)\), HN words, total charge \(c\), normal-ordering
  counterterm \(T=\sum_{i<j}B(c_i,c_j)\), finite
  \(\widehat\Gamma_R\), and \(\Gamma_R^\Pi\).
- Finite moduli stacks: lines 13918-13961 and 15208-15241.  Use
  \(\mathfrak M_{R,c,T}=\mathfrak M^{ss}_{\sigma,S,R,c}\times\{T\}\);
  the singleton \(\{T\}\) is coefficient-system data, not a new brane
  moduli factor.
- Hybrid wrapped source: lines 13996-14231 and 15246-15276.  Positive
  elliptic degree is wrapped, with anchor
  \(\lambda(A)=\det Rp_{E,*}A\otimes{\cal O}_E(-\chi(A)0_E)\in
  \operatorname{Pic}^0(E)\), rigidified before quotient, and eight
  binary words \(LLL,\ldots,WWW\).
- Orientation package: lines 14236-14460 and 15281-15337.  The sketch
  lists orientation gerbes, connected \(E\)-descent, finite stabilizer
  gerbes, cyclic restrictions, and multiplicativity checks.  Attack
  status: this must be upgraded from point-stabilizer data to full Borel
  equivariant obstruction classes and determinant-line wall transport.
- Normal-ordered pushforward: lines 14505-14696.  Central translation
  functors \(T_\eta\), \(B_{\mathrm{ch}}(c,c')=T_{B(c,c')}\), and
  \(\Theta_{\Pi,R}(c)=T_{-\Pi_X(c)}\) make degree additivity a finite
  coefficient-system problem.  Attack status: geometric compatibility
  with correspondences, orientations, cyclic structures, and radicals
  remains conditional.
- Source Koszul/cobar: lines 14703-14785 and 15445-15480.  The source is
  built from the finite hybrid Hall/factorization object; it is not a
  target bar-cobar counit.
- Dirac/Pfaffian block: lines 14819-14942 and 15384-15441.  For a
  primitive mode \(V_{R,\gamma}\), the elementary block
  \(\begin{psmallmatrix}0&1-x^\gamma\\1&0\end{psmallmatrix}\) contributes
  \(1-x^\gamma\).  This proves the finite product only after source
  primitive signed dimensions and Pfaffian line data are supplied.
- Wall sign normal form: lines 14948-15073.  The local wall model
  \(K_i^{\mathrm{nor}}\simeq [R\xrightarrow{u_i}R]\) with
  \(s_{\delta_i}(u_i)=-u_i\) gives a local sign \(-1\).  Attack status:
  line comparison, quotient orientation, atlas gluing, and group
  linearization remain separate.
- Primitive recognition: lines 15082-15145 and 15485-15510.  The PDF
  itself records the zero-bracket counterexample: signed dimensions do
  not identify \(\mathfrak g_{\Delta_5}\).
- Conditional theorem and final architecture: lines 15518-15802.  If
  Algorithms 1--8 are carried out for every \(R\) with compatible
  transitions, then the inverse limit is a compact Dirac-Igusa object.
  The theorem is conditional on those finite constructions and
  transition residuals.

## What the PDF constructions close

- They close the finite formal recipe for \(\widehat\Gamma_R\) from HN
  words, including the normal-ordering counterterm \(T\).
- They close the degree-level explanation of why the Hall source must be
  built on the normal-ordered charge extension rather than by a raw
  \(\Pi_X\)-pushforward.
- They supply the correct finite-stage direction of construction:
  source geometry first, normal-ordering/coefficient data second, target
  comparison third.
- They give the elementary Dirac/Pfaffian block algebra once primitive
  modes and line data are already supplied.
- They state the primitive recognition obligation correctly: dimensions
  and products are not enough.

## What remains conditional

- Algebraic/effective Hall support in the full \(K3\times E\) source.
- Functorial no-overcount for \((c,T)\) labels.
- Mixed-lift or fibre-summed raw descent.
- Full colored factorization beyond the eight binary length-three words.
- Construction of \(Q_{E,R}\) as a correspondence pseudofunctor.
- Full Borel equivariant orientation classes and determinant-line wall
  transports.
- Glued type-II wall atlas, quotient orientation, and Pfaffian line
  comparison with the automorphic weight-five line.
- Source computation of primitive exponents and full primitive
  recognition, including generation, PBW, radical, parity, and no extra
  relations.
- Source-support theorem relating HN height to automorphic target
  windows.

## Manuscript repair order

1. Install typed status language before theorem statements.
2. Split formal full-Mukai lattice arithmetic from algebraic/effective
   compact Hall support.
3. Record the wedge torsion-one computation only for the displayed formal
   primitive lift.
4. Rename the raw no-go as a strict fixed-lift obstruction and leave
   fibre-summed raw descent open.
5. Treat \(T\) as normal-ordering coefficient data, not a new brane
   degree.
6. Split the finite geometric source kernel from downstream protected
   integration and normal-ordering data.
7. Fence target windows as tests inside source-covered finite stages.
8. Require Pfaffian-to-automorphic line comparison before any
   section-level equality.
9. Keep \(\mathcal Z_{\mathrm{Borch}}^{\mathrm{vir}}=\mathcal D_X^{-1}\)
   fixed; attach signs only to supplied orientation/Pfaffian lifts.
