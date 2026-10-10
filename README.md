# EFMW Constants Problem

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/EFMW-Constants-Problem) · [Published page](https://enuminous.github.io/EFMW-Constants-Problem/)

<details>
<summary>Repository indexes (1)</summary>

- [index.html](https://github.com/enuminous/EFMW-Constants-Problem/blob/main/index.html) · [Open page](https://enuminous.github.io/EFMW-Constants-Problem/index.html)

</details>
<!-- ENUMINOUS-NETWORK:END -->

A corrected successor to the 2025 essay **One Paper to Join Them All**.

This repository separates established identities from the open EFMW generative hypothesis.

## Core thesis

The meaningful unification target is not merely to show that physical constants are related. Standard physics already does that. The stronger target is to reduce the number of independent **dimensionless** inputs.

## Contents

- `index.html` — full public paper
- `DEPENDENCY_MAP.md` — identities, inputs, conventions, targets
- `CLAIMS_BOUNDARY.md` — scientific-status boundary
- `EFMWConstants/Core.lean` — Lean 4 formalization
- `EFMWConstants/Main.lean` — export surface
- `verify_constants.py` — numerical sanity checks
- `.github/workflows/lean.yml` — CI

## Build

```bash
lake update
lake build
python verify_constants.py
```

Lean proves consequences of the stated definitions and assumptions. It does not prove that EFMW derives any measured physical constant. In particular, the integer-ratio toy model is only an interface example; independent prespecification of parameters is an empirical/provenance condition outside Lean's object-level proof.

The numerical verifier uses the NIST 2022 CODATA recommended values, currently the latest available CODATA adjustment.
