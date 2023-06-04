# 2d heat equation now. same idea but the laplacian uses all four neighbors:
#   u_new = u + r*(up + down + left + right - 4*u)
# stability is tighter in 2d, need r <= 0.25. start with a hot square and watch it
# bleed out into a smooth blob. for now i just show the start and end frames, havent
# learned to animate yet.

import numpy as np
import matplotlib.pyplot as plt

N = 120
r = 0.2
u = np.zeros((N, N))
u[50:70, 50:70] = 1.0          #hot square

def step(u):
    un = u.copy()
    u[1:-1,1:-1] = un[1:-1,1:-1] + r*(
        un[2:,1:-1] + un[:-2,1:-1] + un[1:-1,2:] + un[1:-1,:-2] - 4*un[1:-1,1:-1])
    return u

start = u.copy()
for _ in range(800):
    u = step(u)

fig, ax = plt.subplots(1, 2, figsize=(10,5))
ax[0].imshow(start, cmap="inferno"); ax[0].set_title("start")
ax[1].imshow(u, cmap="inferno"); ax[1].set_title("after 800 steps")
for a in ax: a.axis("off")
plt.suptitle("2d heat diffusion")
plt.show()
