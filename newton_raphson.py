import math

def f(x):
    return x - math.exp(-x)

def df(x):
    return 1 + math.exp(-x)

def newton_raphson(x0, tol=0.001, max_iter=100):
    print(f"{'i':<4}{'x_(i-1)':<14}{'x_i':<14}{'|x_i - x_(i-1)|':<16}")
    x_prev = x0
    for i in range(1, max_iter + 1):
        x_new = x_prev - f(x_prev) / df(x_prev)
        error = abs(x_new - x_prev)
        print(f"{i:<4}{x_prev:<14.3f}{x_new:<14.3f}{error:<16.4f}")
        if error < tol:
            return x_new
        x_prev = x_new
    return x_prev

raiz = newton_raphson(0.5)
print(f"\nRaíz aproximada: {raiz:.3f}")

print(f"x      = {raiz:.3f}")
print(f"e^(-x) = {math.exp(-raiz):.3f}")
print(f"f(x)   = {f(raiz):.3e}")
