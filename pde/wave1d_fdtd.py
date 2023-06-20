# 1d wave equation, u_tt = c^2 u_xx. unlike heat, waves dont smooth out -- they travel
# and bounce. i step it with the leapfrog stencil that uses the two previous time slices:
#   u_next = 2u - u_prev + (c dt/dx)^2 * (u[i+1]-2u[i]+u[i-1])
# the courant number C = c*dt/dx has to be <= 1 or it goes unstable (CFL again).
# fixed ends, so the pulse reflects and flips.

import numpy as np
import matplotlib.pyplot as plt

nx = 400
dx = 1.0/nx
c = 1.0
C = 0.9                      #courant number, keep <= 1
dt = C*dx/c

x = np.linspace(0, 1, nx)
# initial pulse: a little gaussian bump, at rest
u_prev = np.exp(-((x-0.3)/0.04)**2)
u = u_prev.copy()            #zero initial velocity -> u at t=dt equals t=0 (roughly)

plt.figure(figsize=(9,5))
snaps = [0, 120, 240, 380, 520]
step = 0
for target in snaps:
    while step < target:
        u_next = np.zeros_like(u)
        u_next[1:-1] = (2*u[1:-1] - u_prev[1:-1]
                        + C**2*(u[2:] - 2*u[1:-1] + u[:-2]))
        u_prev = u; u = u_next      #ends stay 0 (fixed boundary)
        step += 1
    plt.plot(x, u, label=f"step {target}")

plt.legend(); plt.grid(True)
plt.xlabel("x"); plt.ylabel("u")
plt.title("1d wave: a pulse travels and reflects (CFL: C<=1)")
plt.savefig("media/wave1d.png", dpi=110)
plt.show()
