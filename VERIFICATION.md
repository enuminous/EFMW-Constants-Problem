# Reproducible Lean verification

The package uses the committed Lean 4.28.0 toolchain and dependency manifest.
The root `EFMWConstants.lean` imports the existing export module, so `lake build` checks
both the theorem source and export surface. No theorem statement or scientific
claim is changed by this package/workflow repair.

```sh
lake exe cache get
lake build
lake env lean -DwarningAsError=true Audit.lean
python3 scripts/test_axiom_audit.py
python3 verify_constants.py
```

The workflow restores Mathlib and GitHub caches and permits 45 minutes. It
records the exact commit/run URL in the successful job summary and checks that
the toolchain, Lake file and dependency manifest were not modified by the build.

The audit traverses every safe declaration in the project namespace, including
private declarations, and allows only `propext`, `Classical.choice` and
`Quot.sound`. Regression controls require rejection of a custom axiom, a private
axiom, a placeholder proof, and native evaluation in a proof.

These checks establish consequences of the definitions and supplied hypotheses.
They do not establish that the model assumptions are physical laws.

## Compilation repairs after restoring the package

The first complete build exposed division-cancellation tactic failures and an extra tactic after a solved goal. Proofs now use explicit cancellation lemmas; all theorem statements and hypotheses are unchanged.
