#!/usr/bin/env python3
"""Numerical sanity checks using the current NIST 2022 CODATA recommended values.

This script checks standard identities only. It is not an EFMW derivation of the constants.
"""

import math

# Exact SI defining constants.
c = 299_792_458.0
e = 1.602176634e-19
h = 6.62607015e-34
hbar = h / (2 * math.pi)

# 2022 CODATA measured/recommended values (NIST).
eps0 = 8.8541878188e-12
G = 6.67430e-11
alpha_codata = 7.2973525643e-3
alpha_inv_codata = 137.035999177

alpha_from_identity = e**2 / (4 * math.pi * eps0 * hbar * c)
lP = math.sqrt(hbar * G / c**3)
tP = math.sqrt(hbar * G / c**5)
mP = math.sqrt(hbar * c / G)

print("NIST 2022 CODATA sanity check")
print(f"alpha from identity = {alpha_from_identity:.13g}")
print(f"alpha CODATA        = {alpha_codata:.13g}")
print(f"1/alpha             = {1/alpha_from_identity:.12f}")
print(f"1/alpha CODATA      = {alpha_inv_codata:.12f}")
print(f"|delta alpha|       = {abs(alpha_from_identity-alpha_codata):.3e}")
print(f"Planck length       = {lP:.12e} m")
print(f"Planck time         = {tP:.12e} s")
print(f"Planck mass         = {mP:.12e} kg")
print(f"lP/(c*tP)           = {lP/(c*tP):.12g}")

# Loose tolerance reflects the rounded eps0 and alpha values copied from CODATA tables.
assert abs(alpha_from_identity - alpha_codata) < 5e-13
assert abs((1 / alpha_from_identity) - alpha_inv_codata) < 5e-8
assert abs(lP / (c * tP) - 1.0) < 1e-12
