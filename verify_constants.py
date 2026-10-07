#!/usr/bin/env python3
import math

c = 299_792_458.0
e = 1.602176634e-19
hbar = 1.054571817e-34
eps0 = 8.8541878128e-12
G = 6.67430e-11

alpha = e**2/(4*math.pi*eps0*hbar*c)
lP = math.sqrt(hbar*G/c**3)
tP = math.sqrt(hbar*G/c**5)
mP = math.sqrt(hbar*c/G)

print(f"alpha        = {alpha:.12g}")
print(f"1/alpha      = {1/alpha:.12g}")
print(f"Planck length= {lP:.12e} m")
print(f"Planck time  = {tP:.12e} s")
print(f"Planck mass  = {mP:.12e} kg")
print(f"lP/(c*tP)   = {lP/(c*tP):.12g}")
