import sympy as sp

def bisection(f, a, b, tol, max_iterations=100):
    for i in range(max_iterations):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < tol:
            return c
    print("Maximum iterations reached. No convergence.")
    return None

# Kullanıcıdan fonksiyon girdisi al
user_function_str = input("Enter your function (e.g., x**2 - 2): ")
x = sp.Symbol('x')
user_function = sp.sympify(user_function_str)

a = float(input("Enter the left bound: "))
b = float(input("Enter the right bound: "))
tolerance = float(input("Enter the tolerance (e.g., 1e-6): "))

# Kök tahminini hesapla
root_estimate = bisection(user_function, a, b, tolerance)
if root_estimate is not None:
    print("Estimated root:", root_estimate)
else:
    print("Maximum iterations reached. No conve")
