# bisection root finder. when you cant solve f(x)=0 by hand you can still FIND the
# root if you bracket it: pick a,b where f changes sign, then keep halving.
# slow but it literally cannot fail if you start with a sign change.

import numpy as np

def bisection(f, a, b, tol=1e-8, maxit=100):
    fa = f(a); fb = f(b)
    if fa*fb > 0:                 #same sign on both ends = no guaranteed root
        raise ValueError("f(a) and f(b) need opposite signs, dummy")
    for i in range(maxit):
        mid = 0.5*(a+b)
        fmid = f(mid)
        if abs(fmid) < tol:
            return mid, i
        if fa*fmid < 0:           #root is in the left half
            b = mid; fb = fmid
        else:                     #root is in the right half
            a = mid; fa = fmid
    return 0.5*(a+b), maxit

if __name__ == "__main__":
    # find sqrt(2) by solving x^2 - 2 = 0
    root, iters = bisection(lambda x: x*x - 2, 0, 2)
    print("sqrt(2) ~=", root, "  (took", iters, "steps)")
    print("real sqrt(2) =", np.sqrt(2))

    # a transcendental one: cos(x) = x
    root2, _ = bisection(lambda x: np.cos(x) - x, 0, 1)
    print("cos(x)=x at x ~=", root2)
