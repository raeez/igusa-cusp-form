# A098 Weyl/root-string and affine citation locator

No files edited.

Verdict: no new bibliography source is required. The strongest route is
already in `proj.bib`: `KAC:1`, `GN`, `GNII`, `BorcherdsGKM88`.

## Weyl transport preserves parity

Use `KAC:1` Lemma 3.8 and Proposition 3.7 for Weyl operators/root-space
transport, and `GN` Appendix Section 6 / Statement 6.4 for the super
version without odd real simple roots. Since the GN real simple generators
are even, the reflection operators are even automorphisms:
\[
\mathfrak g_{\alpha,\bar p}\simeq\mathfrak g_{w\alpha,\bar p}.
\]

Insertion phrase:

```tex
Because the Gritsenko--Nikulin real simple roots are even, Kac's Weyl
operators are even automorphisms of the adapted GN superalgebra; hence
Weyl transport preserves the two root-space parities
\cite[Lemma~3.8, Proposition~3.7]{KAC:1},
\cite[Appendix, Statement~6.4]{GN}.
```

## Terminal support \(C_{k,5}=0|0\)

Use `KAC:1` Proposition 5.1(c), the real-root string theorem, with the GN
super adaptation from `GN` Appendix Section 6. For
\(\alpha=\delta_k\), \(\beta=a_{ij}\), one has
\((\beta,\alpha^\vee)=-4\) and \(\beta-\alpha\notin\Delta\), so the
string stops before \(a_{ij}+5\delta_k\).

## Affine \(A_1^{(1)}\) multiplicity for \(2a_{ij}\)

Use `KAC:1` Theorem 7.4 or Corollary 8.3: in untwisted affine type
\(X_l^{(1)}\), \(\operatorname{mult}(n\delta)=l\). For \(A_1^{(1)}\),
\(l=1\). The submatrix on \(\delta_i,\delta_j\) is
\(\begin{psmallmatrix}2&-2\\-2&2\end{psmallmatrix}\), so
\(a_{ij}=\delta_i+\delta_j\) is the affine null root.

