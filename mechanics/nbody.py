# N-body gravity. every body pulls on every other body. the naive way is a double loop
# over all pairs but i finally figured out how to VECTORIZE the forces with numpy
# broadcasting -- compute all the pairwise separations at once. so much faster.
# softening (eps) keeps two bodies that get close from blowing up to infinity.
#
# also makes an animated gif with fading orbit trails, my favorite output in here

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

rng = np.random.default_rng(7)
G = 1.0
N = 8
eps = 0.1

pos = rng.uniform(-1, 1, size=(N,2))
vel = rng.uniform(-0.1, 0.1, size=(N,2))
mass = rng.uniform(0.5, 1.5, size=N)
vel -= (mass[:,None]*vel).sum(0)/mass.sum()

def accel(pos):
    diff = pos[None,:,:] - pos[:,None,:]
    dist2 = (diff**2).sum(-1) + eps**2
    inv = dist2**-1.5
    np.fill_diagonal(inv, 0.0)
    return G*(mass[None,:,None]*diff*inv[:,:,None]).sum(1)

dt = 0.005; n = 3000
trails = np.zeros((n, N, 2))
a = accel(pos)
for i in range(n):
    trails[i] = pos
    pos = pos + vel*dt + 0.5*a*dt**2
    a_new = accel(pos)
    vel = vel + 0.5*(a + a_new)*dt
    a = a_new

# static
plt.figure(figsize=(7,7))
for j in range(N):
    plt.plot(trails[:,j,0], trails[:,j,1], lw=0.7)
plt.axis("equal"); plt.title("n-body gravity (vectorized + softened)")
plt.savefig("media/nbody.png", dpi=110)

# animated, with trails
fig, ax = plt.subplots(figsize=(6.5,6.5))
lo = trails.min()*1.1; hi = trails.max()*1.1
ax.set_xlim(lo, hi); ax.set_ylim(lo, hi); ax.set_aspect("equal")
ax.set_facecolor("black"); ax.set_title("n-body, my favorite one")
colors = plt.cm.plasma(np.linspace(0.1, 0.95, N))
lines = [ax.plot([], [], lw=1.0, color=colors[j])[0] for j in range(N)]
dots = [ax.plot([], [], "o", color=colors[j], ms=3+4*mass[j])[0] for j in range(N)]

tail = 220; step = 12
def update(frame):
    k = (frame+1)*step           #start past zero so the first frame already has trails
    for j in range(N):
        lo_k = max(0, k-tail)
        lines[j].set_data(trails[lo_k:k+1, j, 0], trails[lo_k:k+1, j, 1])
        if k > 0:
            dots[j].set_data([trails[k, j, 0]], [trails[k, j, 1]])
    return lines + dots

anim = FuncAnimation(fig, update, frames=n//step - 1, blit=True, interval=40)
anim.save("media/nbody.gif", writer=PillowWriter(fps=25))
plt.show()
