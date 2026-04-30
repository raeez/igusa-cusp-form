# A024 report: global notation collision firewall

Runtime id: `019ddbda-0abd-74d0-b91e-9117005ed650`.
Nickname: Aquinas.
Status: completed.
Files changed by agent: none.

## Verdict

Notation collisions are mostly firewalled in prose, but several line
anchors still invite false transfer if copied into theorem statements.

| Symbol family | Role firewall | Highest-risk anchors | Recommended rename/firewall |
|---|---|---|---|
| \(\mathcal D_X,D_5,\mathfrak D_X,D_X\) | \(\mathcal D_X=\Delta_5\) is the virtual determinant; \(D_5=64^{-1}\Delta_5\) is the monic Borcherds product; \(\mathfrak D_X\) is the conditional first-order operator; bare \(D_X\) is currently also a compact datum entry. | `main.tex:12116`, `main.tex:12353`, `main.tex:14512`, `notes/attack_whitepaper_analysis_20260430_guide.md:71`, `notes/attack_whitepaper_analysis_20260430_guide.md:505` | Replace guide \(D_X=\Delta_5\) by \(\mathcal D_X=\Delta_5\). Rename datum entry \((D_X)\) to \((\mathsf{Desc}_X)\) or \((\Theta_X^{\mathrm{desc}})\). |
| \(m_R,m\) | \(m_R=\operatorname{pr}_3\overline\Pi_X\) is trace/\(s\)-degree in some places; \(m_R\) is Hall multiplication elsewhere. \(m_{\mathrm{Bch}}=d_E-1\) only on the OP branch. | `main.tex:8008`, `main.tex:10601`, `main.tex:10827`, `main.tex:13165`, `main.tex:14265` | Keep \(m_R\) for Hall multiplication. Rename trace exponent to \(\deg_R^s\) or \(m_R^{\mathrm{Bch}}\). Do not classify local/wrapped support by \(m\); use \(b_R^{\mathrm{geom}}\) or \(d_{E,R}^{\mathrm{geom}}\). |
| \(n\) | In D6/OP, \(n=\chi(\mathcal O_Y)\). In Gram triples, first coordinate \(n=Q^2/2\). | `main.tex:2742`, `main.tex:2766`, `main.tex:4553`, `main.tex:16007` | Use \(\chi_Y\) or \(n_{\mathrm{D0}}\) for Euler/D0 index; use \(n_{\mathrm{Bch}}\) for the first Gram coordinate. Dictionary: \((n_{\mathrm{Bch}},\ell_{\mathrm{Bch}},m_{\mathrm{Bch}})=(h-1,\chi_Y,d_E-1)\). |
| \(P,Q,T\) | \(P,Q\) are Mukai charge components; \(T\) is a Gram matrix and also normal-ordering coordinate; OP uses uppercase \(P,Q,T\) for scalar variables. | `main.tex:4511`, `main.tex:4595`, `main.tex:4938`, `main.tex:15982`, `main.tex:14778` | Use OP-labelled variables \(P_{\mathrm{OP}},Q_{\mathrm{OP}},T_{\mathrm{OP}}\) or lowercase \(p_{\mathrm{OP}},q_{\mathrm{OP}},t_{\mathrm{OP}}\). Rename normal-ordering coordinate to \(T_{\mathrm{no}}\) or \(\tau\). |
| \(R_{X,R}\) | Primitive-recognition datum at finite height \(R\); visually collides with the height index \(R\) and tuple entry \(R_X\). | `main.tex:14549`, `main.tex:14676` | Rename to \(\mathsf{Rec}_{X,R}\), with global entry \(\mathsf{Rec}_X\). |
| \(\Gamma_X^{\mathrm{phys/form}}\) | The manuscript says \(\Gamma_X^{\mathrm{phys}}=\Gamma_X^{\mathrm{form}}\) as a mnemonic formal Mukai sector, not full \(4d\ \mathcal N=4\) charge lattice. Formal lifts do not imply Hall support. | `main.tex:260`, `main.tex:4600`, `main.tex:4625`, `main.tex:4670`, `main.tex:5140` | Prefer \(\Gamma_X^{\mathrm{form}}\) in formulas. Reserve \(\Gamma_X^{\mathrm{phys}}\) only as a deprecated mnemonic with the caveat repeated nearby. |

CYQG locks confirm the live risks: AP-CY391 forbids
\(m_{\mathrm{Bch}}=0\Rightarrow\) locality, AP-CY393 separates
\(\mathcal D_X,D_5,\mathfrak D_X,D_X\), and AP-CY394 forbids upgrading
formal Mukai lifts to Hall support.

## Residual Obligations

A patch pass should rename the datum-level \(D_X\), trace-degree
\(m_R\), OP \(P,Q,T\), and \(R_{X,R}\); then grep for bare
\(D_X=\Delta_5\), `local color when \(m=0\)`, and unqualified
\(\Gamma_X^{\mathrm{phys}}\).

Commands run by agent:
read-only `pwd`, `rg --files`, fixed-string `rg -n -F`, `sed`, and
`nl -ba ... | sed` over `CLAUDE.md`, `main.tex`, A007/A014/A015/A018,
the 2026-04-30 guide, and CYQG antipattern/cache anchors. One broad
regex `rg` failed on LaTeX escapes; it was rerun as fixed-string search.
