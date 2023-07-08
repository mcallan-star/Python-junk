# solving for the electric potential in a box with Poisson's equation: laplacian(V) = -rho.
# theres no time here, its an equilibrium problem, so i RELAX into the answer: repeatedly
# set each cell to the average of its neighbors (plus the source) until it stops changing.
# thats Jacobi iteration. put a + and - charge in the box and watch the potential form.

import numpy as np
import matplotlib.pyplot as plt

N = 100
V = np.zeros((N, N))
rho = np.zeros((N, N))
rho[30, 35] = 1.0       #positive charge
rho[70, 65] = -1.0      #negative charge

# walls grounded at V=0 (already zero on the border, and we never update the border)
for it in range(4000):
    Vn = V.copy()
    V[1:-1,1:-1] = 0.25*(Vn[2:,1:-1] + Vn[:-2,1:-1]
                         + Vn[1:-1,2:] + Vn[1:-1,:-2]
                         + rho[1:-1,1:-1])
    if it % 1000 == 0:
        change = np.abs(V - Vn).max()
        print(f"iter {it}: max change {change:.2e}")

plt.figure(figsize=(7,6))
plt.imshow(V, cmap="RdBu_r", origin="lower")
plt.colorbar(label="potential V")
plt.contour(V, levels=20, colors="k", linewidths=0.4)   #field/equipotential lines
plt.title("poisson: potential of a + and - charge (Jacobi relaxation)")
plt.savefig("media/poisson2d.png", dpi=110)
plt.show()
