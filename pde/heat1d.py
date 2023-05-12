# first PDE!! the heat equation: u_t = alpha * u_xx. a hot spot spreads out and smooths
# over time. explicit finite difference: each step, every point moves toward the average
# of its neighbors.
#   u_new[i] = u[i] + r*(u[i+1] - 2u[i] + u[i-1]),  r = alpha*dt/dx^2
# BIG lesson: if r > 0.5 the whole thing EXPLODES into garbage (numbers -> nan). thats
# the stability limit (see stability_note.md). keeping r = 0.4 here so it behaves.

import numpy as np
import matplotlib.pyplot as plt

nx = 200
L = 1.0
dx = L/nx
alpha = 1.0
r = 0.4                      #stay under 0.5 or it blows up
dt = r*dx**2/alpha

x = np.linspace(0, L, nx)
u = np.zeros(nx)
u[(x > 0.4) & (x < 0.6)] = 1.0     #start with a hot bar in the middle
# ends held at zero (cold walls)

plt.figure(figsize=(9,5))
snap_steps = [0, 50, 200, 600, 1500, 4000]
step = 0
for target in snap_steps:
    while step < target:
        un = u.copy()
        u[1:-1] = un[1:-1] + r*(un[2:] - 2*un[1:-1] + un[:-2])
        step += 1
    plt.plot(x, u, label=f"step {target}")

plt.legend(); plt.grid(True)
plt.xlabel("x"); plt.ylabel("temperature")
plt.title("1d heat equation: a hot bar smoothing out")
plt.savefig("media/heat1d.png", dpi=110)
plt.show()
