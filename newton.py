# newtons method, way faster than bisection. you follow the tangent line down to
# where it hits zero:  x_new = x - f(x)/f'(x).  needs the derivative though.
# im doing the derivative numerically so i dont have to compute it by hand.

import numpy as np

def deriv(f, x, h=1e-6):
    return (f(x+h) - f(x-h)) / (2*h)     #central difference

def newton(f, x0, tol=1e-10, maxit=50):
    x = x0
    for i in range(maxit):
        fx = f(x)
        if abs(fx) < tol:
            return x, i
        x = x + fx/deriv(f, x)           #step toward the root
    return x, maxit

if __name__ == "__main__":
    root, iters = newton(lambda x: x*x - 2, 1.0)
    print("sqrt(2) ~=", root, " in", iters, "steps")
    # hmm this is not converging to 1.414, it shoots off?? something is wrong
