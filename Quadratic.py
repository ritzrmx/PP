import cmath

def find_roots(a, b, c):
    d = b**2 - 4*a*c
    r = cmath.sqrt(abs(d))
    roots = [(-b + r) / (2 * a), (-b - r) / (2 * a)]

    if d > 0: print(f"Real and different roots: {roots}")
    elif d == 0: print(f"Real and same root: {roots[0]}")
    else: print(f"Complex roots: {roots}")

a, b, c = map(float, input('Enter coefficients a, b, c separated by space: ').split())
if a == 0: print("Input correct quadratic equation (a cannot be 0)")
else: find_roots(a, b, c)
