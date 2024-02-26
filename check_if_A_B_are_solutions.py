import sympy as sp

j = sp.symbols('j')

A = 3*(j / (1728 - j))
B = 2*(j / (1728 - j))

LHS = 4 * (1728 * A**3) / (4 * A**3 + 27 * B**2)

RHS = j

diff = sp.simplify(LHS - RHS)

if diff == 0:
    print("The solution is correct.")
else:
    print("The solution is no correct.")