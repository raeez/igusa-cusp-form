# A088 recognition section build-risk audit

No files edited by the agent.

## Claim attacked

Recognition theorem ladder around `main.tex:12491`, `main.tex:15011`,
`main.tex:15275`, `main.tex:15380`, and `main.tex:15451`.

## Hazards

1. A078 snippets must replace existing theorem/proposition blocks, not be
   inserted next to them. Existing labels include
   `prop:first-saturated-primitive-recognition-window`,
   `thm:executable-finite-source-matrix-criterion`, and
   `prop:finite-wlethree-no7-source-protocol`.

2. If the first-window proposition becomes a theorem, prose references at
   `main.tex:12681` and `main.tex:15368` must be updated.

3. The current first-window proposition includes both target arithmetic
   and the height-four obstruction. Integration should split the logical
   content, not delete the obstruction.

4. Report language such as "A067 source fixture" must be replaced by an
   internal manuscript definition: source certificate packet with
   \(M,D,B,G,K,Q,A\), relation rows, NO7, no-extra, PBW, and transition
   rows.

5. \(\tau\) is overloaded: height-three root, isotropic multiplicity
   function, and tensor flip. Use \(\delta_{123}\) for the root and
   \(\mathsf{sw}_{\alpha,\beta}\) for the flip.

6. The A071 packet is relation-minimal, not the same as the downward
   saturated cofinal windows of
   `def:cofinal-primitive-recognition-datum`.

7. Full target parity is still missing for some A071 rows. Product
   coefficients are not parity data.

8. Matrix quantifiers in the finite verifier must name retained pair and
   decomposition sets, as in the NO7 protocol.

## Safe patch order

1. Add the proof ledger after `main.tex:12851` as compact prose or a
   short list, not a large table.
2. Split the first-window text into target arithmetic, conditional
   \(W_{\le3}\) certificate, and height-four obstruction.
3. Insert the A071 status only after target parity-source rows are
   stated. Weyl transport handles \(C_{k,3}\) and \(C_{k,4}\); signed-only
   rows remain blocked until target presentation computation or citation.
4. Sharpen the finite verifier and keep NO7 as a sub-verifier.

## Constants to preserve

\[
\gamma(c_1,c_2,c_3)=(c_1,c_1+c_2-c_3,c_2),
\qquad
D_5=64^{-1}\Delta_5,
\]
\(m(\delta_{123})=-93\), \(29|93\), \(29-93=-64=f(1,1)\),
height-four \(m=90\), \(\smult=108\), residual \(18\), doubled isotropic
\(10|9|1\), real-string exponents \(3,5,3\), A071 has \(35\) positive
degrees and \(71\) signed blocks, \(m(2\delta_{123})=-540\), and
\(\smult(2\delta_{123})=4016\).

