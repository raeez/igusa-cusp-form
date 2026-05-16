# A265 CYQG H4 Cache Propagation

Runtime id: `019ddceb-854c-7960-a77d-ec5197ba675c`.

Changed:
- `/Users/raeez/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md`.
- `/Users/raeez/calabi-yau-quantum-groups/notes/first_principles_cache_comprehensive.md`.

New cache ids:
- `AP-CY451`.
- `IC-93`.

Recorded adjudication:
- `\operatorname{div}(\Delta_5)=H_1+2H_4`.
- `\operatorname{div}(\Phi_{10}^{\mathrm{un}})=2H_1+4H_4`.
- `[ \Phi_{10}^{\mathrm{un}}/\eta^{24}]^{1/8}` has `H_4` exponent `4/8=1/2`, monodromy `-1`, and order `2`.
- The cache now blocks both the proved-order-16 claim and the `H_1+\frac12H_4` base quotient divisor.

Checks:
- `git diff --check -- notes/antipatterns_catalogue.md notes/first_principles_cache_comprehensive.md` passed in `/Users/raeez/calabi-yau-quantum-groups`.

Residual risk:
- Primitive `\mu_{16}` Kuga--Satake/metaplectic banding remains conditional until a primary-source non-split banding lemma is supplied.
