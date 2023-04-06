# the three body problem. with three masses theres no clean formula, and worse, its
# CHAOTIC -- nudge the start by a hair and the whole future changes. i show that by
# running two sims that start almost identical (one body moved by 1e-9) and watching
# the distance between them blow up exponentially. no two runs alike.

import numpy as np
import matplotlib.pyplot as plt

G = 1.0; eps = 1e-3

def run(pos, vel, mass, dt=0.002, n=6000):
    pos = pos.copy(); vel = vel.copy()
    def accel(p):
        diff = p[None,:,:] - p[:,None,:]
        dist2 = (diff**2).sum(-1) + eps**2
        inv = dist2**-1.5; np.fill_diagonal(inv, 0.0)
        return G*(mass[None,:,None]*diff*inv[:,:,None]).sum(1)
    hist = np.zeros((n, len(mass), 2))
    a = accel(pos)
    for i in range(n):
        hist[i] = pos
        pos = pos + vel*dt + 0.5*a*dt**2
        a2 = accel(pos); vel = vel + 0.5*(a+a2)*dt; a = a2
    return hist

mass = np.array([1.0, 1.0, 1.0])
pos = np.array([[-1.0, 0.0], [1.0, 0.0], [0.0, 0.5]])
vel = np.array([[0.0, -0.3], [0.0, 0.3], [0.3, 0.0]])

A = run(pos, vel, mass)
pos2 = pos.copy(); pos2[2,0] += 1e-9            #tiny nudge to body 3
B = run(pos2, vel, mass)

sep = np.sqrt(((A - B)**2).sum(-1)).max(axis=1)  #worst-case separation over time

fig, ax = plt.subplots(1, 2, figsize=(12,5))
for j in range(3):
    ax[0].plot(A[:,j,0], A[:,j,1], lw=0.7)
ax[0].axis("equal"); ax[0].set_title("three body dance")
ax[1].semilogy(sep)
ax[1].set_title("two near-identical starts diverge (chaos)")
ax[1].set_xlabel("step"); ax[1].set_ylabel("separation (log)")
ax[1].grid(True, which="both")
fig.tight_layout()
fig.savefig("media/three_body.png", dpi=110)
plt.show()
