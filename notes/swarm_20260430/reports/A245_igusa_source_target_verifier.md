# A245 Igusa Source-Target Verifier

Runtime id: `019ddcd1-b907-7812-9521-62f5ba1fa41c`.

Verdict:
- Clean for manuscript notation. No edits made.

Checks:
- Exact bad-label sweep over `main.tex`, `compute/verify_source_fixture.py`, `certificates/sources/k3e_compact_hall`, and `certificates/targets/delta5_gn_kac` found no residual source blocks using BKM root labels such as `P^X_{R,\beta}`, `P^\Pi_{R,\alpha}`, `K_\beta`, `Q_\alpha`, `G_\rho`, or raw `P^{\Pi,raw}`.
- Positive gamma-firewall search found expected `\gamma_\alpha`, `\gamma_\beta`, and `\gamma_\rho` source-degree labels.
- `python3 compute/verify_source_fixture.py --check --source certificates/sources/k3e_compact_hall --target certificates/targets/delta5_gn_kac/a071_target_presentation` exited blocked with `schema_complete: false`, as intended.

Hardening recommendation:
- Add an explicit CSV-payload source-degree firewall so future populated packets reject `P^X_{R,\beta}`, `K_\beta`, `Q_\alpha`, or raw `P^{\Pi,raw}` in source CSV values.

Integration:
- The master thread implemented the source-degree firewall in `compute/verify_source_fixture.py` and updated `certificates/sources/k3e_compact_hall/README.md`.
