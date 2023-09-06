from sympy import symbols, Eq, solve

a, b, c, d, e = symbols('a b c d e')

eq1 = Eq(a*e*d*b, -10.5)
eq2 = Eq(c + e*a + d, 12.5)
eq3 = Eq(b*a*e, -1.5)
eq4 = Eq(c + e, 4.5)
eq5 = Eq(b + a, 2)
eq6 = Eq(b + c + e, 3.5)
eq7 = Eq(d * e * b + a, -0.5)

solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7), (a, b, c, d, e))
print(solution)
