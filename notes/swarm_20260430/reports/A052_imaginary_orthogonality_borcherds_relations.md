# A052 - Imaginary Orthogonality and Borcherds Relations

## Claim Attacked

Imaginary simple-root multiplicities, isotropic/negative-norm Borcherds
relations, super parity, and orthogonality might be read from the
Borcherds product and then treated as compact `K3 x E` source data.

## Verdict

The manuscript mostly keeps the firewall. The target denominator algebra
is imported from Gritsenko-Nikulin/Kac; compact source recognition
remains conditional. The product alone determines only signed root
superdimensions after the root datum is fixed. It does not determine
parity splits, orthogonality relations, brackets, PBW, or the Hopf
radical.

## Failure Mode

```tex
\prod_{\alpha>0}(1-e^{-\alpha})^{\smult(\alpha)}
```

sees only

```tex
\smult(\alpha)
  = \dim\mathfrak g_{\alpha,\bar0}
    - \dim\mathfrak g_{\alpha,\bar1}.
```

The same signed dimensions allow zero bracket, wrong bracket, extra
relations, or added cancelling pairs `M\oplus \Pi M`. Therefore
determinant/product equality cannot identify a source Lie superalgebra.

## Exact Target Formulas Checked

```tex
\alpha(n,l,m)
  =2nf_2-lf_3+2mf_{-2}
  =n\delta_1+m\delta_2+(n+m-l)\delta_3.
```

```tex
((\delta_i,\delta_j)) =
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix},
\qquad
\rho=f_2-\tfrac12 f_3+f_{-2}.
```

```tex
D_5=64^{-1}\Delta_5,\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=D_5(2Z).
```

Negative-norm imaginary simples use
`m(a)=-64^{-1}c_\Delta(n,l,m)`. Isotropic rays use `\tau(ta)=9`.
The parity split `\mu_{\bar0},\mu_{\bar1}` is GN/Kac BKM target data,
not product data.

## Key Local Anchors

- `main.tex` near line 5719: denominator algebra imported as target.
- `main.tex` near line 5817: proof compares GN/Kac algebra with product.
- `main.tex` near line 15586: imaginary simple-root parity split.
- `main.tex` near line 15639: generators and Borcherds-Kac relations.
- `main.tex` near line 15773: denominator determines only signed
  integers.
- `main.tex` near line 15822: determinant forgets bracket, parity, and
  radical.
- `main.tex` near line 12469: primitive recognition requires
  source-built data.
- `main.tex` near line 15004: `W_{\le3}` target window and matrix
  obligations.
- `main.tex` near line 15373: finite `W_{\le3}` NO7 source protocol.

## Low-Degree Attack Result

```tex
\delta_{123}=\delta_1+\delta_2+\delta_3,\qquad
m(\delta_{123})=-93.
```

Target presentation gives `29|93`, so `29-93=-64=f(1,1)`. The signed
exponent `-64` does not determine `29|93`.

For `a_{ij}=\delta_i+\delta_j`,
`(\delta_i,a_{ij})=(\delta_j,a_{ij})=0`, so adjacent
real-isotropic brackets must vanish. For the complementary `\delta_k`,
`(\delta_k,a_{ij})=-4`, so the real-string exponent is `5`. These are
target Borcherds-Kac relations. A compact source must prove them by
Hall bracket matrices.

## Critique Anchors

- A006: source matrices remain conditional.
- A010: GN attribution and low-degree survival citation gap.
- A023: fixed-lift raw descent no-go; low-degree citation residual.
- A030: transition, ML, radical, and PBW conditions.
- Guide section 12: source matrices and `W_{\le3}`.
- CYQG AP-CY368/AP-CY378/AP-CY384: signed dimensions, source matrices,
  and noncanonical bases.

## Claim-Status Recommendation

Retain the denominator algebra as a proved/imported target theorem.
Retain compact primitive recognition only as conditional on source-built
`M,D,B,G,K,Q`, comparison maps `A_\beta`, relation rows, Hopf radical
ideal/coideal, no-extra-relations, PBW, and ML-compatible transitions.
Do not let product exponents substitute for imaginary orthogonality or
Borcherds relations.

## Residual Obligations

Patch the citation near `main.tex` line 5818: GNII Theorem 2.1 is
product-lift data; the algebra construction should cite GN Sections 3-4
or Proposition 3.1, with Kac/Borcherds presentation support. Clarify the
orthogonality relation convention for distinct indices and isotropic
self-brackets. Add a source-side certificate for `W_{\le3}`:
`29|93` bases in `\delta_{123}`, nine `u_{ij,r}`, adjacent
orthogonality zero matrices, complementary real-string rows,
pairing/radical matrices, and PBW/no-extra-relations.

## Files Changed

None by the agent.

## Commands and Checks

Read-only `sed`, `nl -ba`, `rg`, `wc`, `git status --short`;
`python3 compute/verify_lattice.py`; `python3 compute/verify_square_root.py`.

