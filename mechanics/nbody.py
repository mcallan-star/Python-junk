# N-body gravity. every body pulls on every other body. the naive way is a double loop
# over all pairs but i finally figured out how to VECTORIZE the forces with numpy
# broadcasting -- compute all the pairwise separations at once. so much faster.
# softening (eps) keeps two bodies that get close from blowing up to infinity.

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
G = 1.0
N = 8
eps = 0.1

pos = rng.uniform(-1, 1, size=(N,2))
vel = rng.uniform(-0.1, 0.1, size=(N,2))
mass = rng.uniform(0.5, 1.5, size=N)
vel -= (mass[:,None]*vel).sum(0)/mass.sum()    #zero the total momentum so it doesnt drift

def accel(pos):
    diff = pos[None,:,:] - pos[:,None,:]       #(N,N,2): r_j - r_i
    dist2 = (diff**2).sum(-1) + eps**2
    inv = dist2**-1.5
    np.fill_diagonal(inv, 0.0)                 #a body doesnt pull on itself
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

plt.figure(figsize=(7,7))
for j in range(N):
    plt.plot(trails[:,j,0], trails[:,j,1], lw=0.7)
plt.axis("equal")
plt.title("n-body gravity (vectorized + softened)")
plt.savefig("media/nbody.png", dpi=110)
plt.show()
