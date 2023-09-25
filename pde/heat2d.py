# 2d heat equation. laplacian uses all four neighbors:
#   u_new = u + r*(up + down + left + right - 4*u)
# stability is tighter in 2d, need r <= 0.25. start with a couple hot squares and let
# them bleed out and merge into a smooth blob.
#
# animated, watching the heat flow beats two static frames

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

N = 120
r = 0.2
u = np.zeros((N, N))
u[25:45, 25:45] = 1.0
u[70:95, 65:90] = 1.0          #two hot squares

def step(u):
    un = u.copy()
    u[1:-1,1:-1] = un[1:-1,1:-1] + r*(
        un[2:,1:-1] + un[:-2,1:-1] + un[1:-1,2:] + un[1:-1,:-2] - 4*un[1:-1,1:-1])
    return u

fig, ax = plt.subplots(figsize=(5,5))
im = ax.imshow(u, cmap="inferno", vmin=0, vmax=1)
ax.axis("off"); ax.set_title("2d heat diffusion")

steps_per_frame = 12
def update(frame):
    global u
    for _ in range(steps_per_frame):
        u = step(u)
    im.set_array(u)
    return [im]

anim = FuncAnimation(fig, update, frames=80, blit=True, interval=50)
anim.save("media/heat2d.gif", writer=PillowWriter(fps=20))
plt.show()
