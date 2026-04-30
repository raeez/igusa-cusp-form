# A006 report: \(W_{\le3}\), source matrices, chiral coalgebra, Pfaffian blocks

Runtime id: `019ddbc5-10a4-7340-bea9-30668e81cb73`.
Nickname: Turing.
Status: completed.
Files changed by agent: none.

## Verdict

Recognition is still conditional. Target arithmetic gives the
Gritsenko--Nikulin/Kac reference table and the Borcherds product. It
does not give compact source primitives, source products, coproducts,
pairings, radicals, PBW, or no-extra-relations. The manuscript states
this boundary correctly; theorem-level recognition begins only after the
finite source matrix certificate is supplied from retained geometry.

## Attacks

### Signed Dimensions Fail Recognition

The same \(\operatorname{sdim}=f(nm,l)\) can carry zero bracket, wrong
bracket, hidden cancelling parity, or extra relations.

Anchors:
`main.tex:12469`, CYQG `AP-CY368`.

### \(W_{\le3}\) Target Table Is Not Source Data

The target table has
\(\delta_i:1|0\), \(\delta_i+\delta_j:10|0\),
\(2\delta_i+\delta_j:1|0\), and \(\delta_{123}:29|93\). Source
recognition needs compact bases on
\(W_{\le3}\cup(-W_{\le3})\cup\{0\}\) plus all matrices. The \(29|93\)
block is the first hard obstruction.

Anchors:
`main.tex:15004`, `main.tex:15268`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:42385`.

### Source/Target Bar-Cobar Firewall

\(\Omega B(\mathrm{Den})\to\mathrm{Den}\) reconstructs the imported
target. It cannot define \(C_X\). The source coalgebra must be
\(\bar B_E^{ch}\) of the supplied geometric hybrid source, with source
collision coproduct and source transitions.

Anchors:
`main.tex:6722`, `main.tex:13737`, `main.tex:14118`, CYQG `AP-CY380`.

### Finite Dirac Blocks Are Algebraic Blocks

The block with square \(1-x_\beta\) proves only a finite Pfaffian model
after a Pfaffian convention. It is not a compact geometric Dirac
operator without source primitives, parity lift, Pfaffian line,
orientation square root, wall atoms, and transition compatibility.

Anchors:
`main.tex:5944`, `main.tex:14137`, CYQG `AP-CY381`.

## Exact Finite Matrix Checklist

For every \(\beta\in W_{\le3}\cup(-W_{\le3})\cup\{0\}\) and parity
block:

1. Compact source bases \(B^X_{\beta,p}\) with retained-stratum,
   vanishing-cycle, and orientation provenance.
2. Product matrices \(M_{\alpha,\beta}\) from compact Hall pull-push.
3. Bracket matrices
   \(B_{\alpha,\beta}=M_{\alpha,\beta}
   -(-1)^{|x||y|}M_{\beta,\alpha}\tau\).
4. Coproduct matrices \(D^{\mu,\nu}_\rho\) from source splitting
   correspondences.
5. Positive-negative pairing matrices \(G_{\beta,p}\).
6. Radical bases
   \(K_{\beta,p}=\ker G_{\beta,p}\cap\ker G_{-\beta,p}^t\).
7. Splittings \(P^X_{\beta,p}=K_{\beta,p}\oplus L_{\beta,p}\) and
   quotient maps \(Q_{\beta,p}\).
8. Source-to-target maps \(A_{\beta,p}:L_{\beta,p}\to
   \mathfrak g_{\Delta_5,\beta,p}\) preserving parity, pairing,
   bracket, coproduct, Cartan, and transitions.
9. Matrix identities:
   \(QB(P\otimes K)=0\), \(QB(K\otimes P)=0\),
   \((Q\otimes Q)DK=0\), and \(M^tG=(G\otimes G)D\).
10. Relation rows: Chevalley, real Serre, isotropic orthogonality,
    super signs, Jacobi \(T_1+T_2+T_3=0\), six real-string rows, and
    the 27 mixed maps \([e_k,u_{ij,r}]\).
11. No-extra-relations:
    \(\ker\pi_W=(J_{BK}+\operatorname{Rad}_{GN})_W\).
12. PBW:
    \[
    \operatorname{gr}_{PBW}U(P_X^{red})_{\le W}\to
    \operatorname{gr}_{PBW}U(\mathfrak g_{\Delta_5})_{\le W}
    \]
    is an isomorphism.
13. Transitions preserve \(K\), pairings, coproducts, PBW filtrations,
    and satisfy finite-slice Mittag--Leffler stable image, hence
    \(R^1\lim=0\).

Primary anchor:
`main.tex:15268`.
NO7 anchor:
`main.tex:15373`.

## Theorem Boundaries

Proved/target:
Borcherds product, target denominator algebra, target finite normal
form, target Pfaffian reference tower.

Conditional/source:
retained compact Dirac-Igusa realization, primitive recognition, source
chiral coalgebra, and Pfaffian equality. These become theorem-level only
after finite source matrices, source coalgebra, source-to-target
comparison, radical quotient, PBW/no-extra-relations, and strict
transition system are constructed.

Anchor:
`main.tex:14445`.

## Residual Obligations

Actual compact Borel--Moore/vanishing-cycle bases; actual integration
matrices \(M,D,G\); radical coideal checks; \(A_\beta\) labels for the
noncanonical \(93\) odd directions; source-built \(C_X\);
source-internal cobar counit plus geometric \(\vartheta_R\); Pfaffian
line/orientation data; type-II wall atoms; cofinal transitions and
\(R^1\lim=0\).

Commands run by agent: read-only `sed`, `rg`, and `nl -ba | sed -n`.
No git-mutating commands.
