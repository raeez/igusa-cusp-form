# A121 -- Igusa Signed-Shadow Wording Verifier

## Claim Attacked

The Pfaffian \(D_0\) lane might still let the split signed
\(K_0\)-representative be mistaken for true target root-space parity or
compact source recognition.

## Findings

Medium: the phrase "the compact identification is to identify it ... with
actual source primitive spaces" could still sound as if the
signed-shadow representative itself is source recognition.

Low: the proof phrase "the minimal model" was less guarded than the
new proposition title.

Low/source hygiene: the internal label
`prop:cofinal-target-window-parity-model` still contains "parity". This
is not typeset; the main thread kept it stable to avoid reference churn.

## Main-Thread Action

The main thread replaced "the minimal model" by the split representative
\(\mathsf P^{\min}_{\Delta,R,\gamma}\), and rewrote the later sentence
as a remaining compact-source recognition task: supply actual source
primitive spaces whose signed class is the representative, or a
non-minimal lift, and prove no-hidden-cancellation if the split
representative is used.

## Files Changed By Agent

None.
