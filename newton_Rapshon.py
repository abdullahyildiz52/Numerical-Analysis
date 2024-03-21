import sympy as sp
import mpmath
from sympy import sin, cos, csc
from sympy.abc import X


def newton_raphson(f, x0, tol, max_iterations=100):
    x = sp.Symbol('x')
    df = sp.diff(f, x)  # Calculate the derivative of the user-defined function

    for i in range(max_iterations):
        x1 = x0 - f.subs(x, x0) / df.subs(x, x0)
        print(f"Iteration {i+1}: x = {x1}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("Maximum iterations reached. No convergence.")
    return None  # Return None if maximum iterations reached

# Get user-defined function
user_function_str = input("Enter your function (e.g., x**2 - 2): ")
x = sp.Symbol('x')
user_function = eval(user_function_str)

initial_guess = float(input("Enter the initial guess: "))
tolerance = float(input("Enter the tolerance (e.g., 1e-6): "))

root_estimate = newton_raphson(user_function, initial_guess, tolerance)
if root_estimate is not None:
    print("Estimated root:", root_estimate)
else:
    print("Maximum iterations reached. No convergence.")
