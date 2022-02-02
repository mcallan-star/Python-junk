# rolling my own numerical integration. area under a curve = add up little slices.
# trapezoid: approximate each slice as a trapezoid.
# simpson: fit little parabolas instead, much more accurate for the same number of
# points (as long as n is even).

import numpy as np

def trapezoid(f, a, b, n=100):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    # ends count once, everything in the middle counts twice
    return h*(0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))

def simpson(f, a, b, n=100):
    if n % 2 == 1:
        n += 1                  #simpson needs an even number of intervals
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    # pattern is 1,4,2,4,2,...,4,1
    return (h/3)*(y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))

if __name__ == "__main__":
    # integral of sin from 0 to pi should be exactly 2
    print("trapezoid:", trapezoid(np.sin, 0, np.pi, 50))
    print("simpson:  ", simpson(np.sin, 0, np.pi, 50))
    print("exact:     2.0")
    # gaussian, integral over the real line ~ sqrt(pi)
    g = lambda x: np.exp(-x**2)
    print("gaussian (simpson, -6..6):", simpson(g, -6, 6, 200), " vs sqrt(pi) =", np.sqrt(np.pi))
