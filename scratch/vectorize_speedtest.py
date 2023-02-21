# proving to myself that vectorizing actually matters before i rewrote nbody. compute
# all pairwise gravitational forces two ways -- python double loop vs numpy broadcasting
# -- and time them. the numpy one is embarrassingly faster.
import numpy as np
import time

rng = np.random.default_rng(0)
N = 400
pos = rng.uniform(-1, 1, size=(N, 2))
mass = rng.uniform(0.5, 1.5, size=N)
eps = 0.1

def forces_loop(pos):
    a = np.zeros_like(pos)
    for i in range(N):
        for j in range(N):
            if i == j: continue
            d = pos[j] - pos[i]
            a[i] += mass[j]*d/(d@d + eps**2)**1.5
    return a

def forces_vectorized(pos):
    diff = pos[None,:,:] - pos[:,None,:]
    dist2 = (diff**2).sum(-1) + eps**2
    inv = dist2**-1.5; np.fill_diagonal(inv, 0.0)
    return (mass[None,:,None]*diff*inv[:,:,None]).sum(1)

t0 = time.time(); a1 = forces_loop(pos); t1 = time.time()
a2 = forces_vectorized(pos); t2 = time.time()
print(f"double loop:  {t1-t0:.3f} s")
print(f"vectorized:   {t2-t1:.4f} s")
print(f"speedup:      ~{(t1-t0)/(t2-t1):.0f}x")
print("same answer?  ", np.allclose(a1, a2))
