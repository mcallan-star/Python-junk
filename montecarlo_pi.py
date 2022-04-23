# estimating pi by throwing darts!! throw random points in a 1x1 square. the fraction
# that land inside the quarter circle is (area of quarter circle)/(area of square) =
# (pi/4). so pi ~= 4 * (inside / total). more darts = better estimate.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
N = 5000
x = np.random.rand(N)
y = np.random.rand(N)
inside = (x**2 + y**2) <= 1.0          #is the dart inside the unit circle?

pi_est = 4*np.sum(inside)/N
print("pi estimate with", N, "darts:", pi_est, "  (real pi =", np.pi, ")")

plt.figure(figsize=(6,6))
plt.scatter(x[inside], y[inside], s=3, color="tab:blue", label="inside")
plt.scatter(x[~inside], y[~inside], s=3, color="tab:red", label="outside")
th = np.linspace(0, np.pi/2, 100)
plt.plot(np.cos(th), np.sin(th), "k", lw=1.5)
plt.axis("equal"); plt.legend()
plt.title(f"monte carlo pi ~= {pi_est:.4f}")
plt.savefig("media/montecarlo_pi.png", dpi=110)
plt.show()
