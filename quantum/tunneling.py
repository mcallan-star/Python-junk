"""Quantum tunneling: throw a wavepacket at a barrier it classically can't pass.

Reuses my split-step solver. The packet has energy a bit BELOW the barrier height, so a
classical particle would just bounce. But the quantum packet leaks: part of it reflects,
part of it tunnels straight through and keeps going on the other side. You can watch the
probability split at the wall. This is the coolest plot in the whole repo and the reason
i kept going with the split-step method.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from split_step import split_step_evolve, gaussian_packet   # my own solver, same folder

hbar = 1.0; m = 1.0
N = 2048
x = np.linspace(-80, 80, N)

# a barrier near the origin
V = np.zeros(N)
barrier_height = 2.2
V[(x > 0) & (x < 1.5)] = barrier_height

# packet coming in from the left, energy ~ k0^2/2 just under the barrier
k0 = 2.0
psi0 = gaussian_packet(x, x0=-30, k0=k0, sigma=4.0)
print("packet energy ~", 0.5*k0**2, " | barrier height", barrier_height)

frames = split_step_evolve(psi0, x, V, dt=0.01, steps=3000, record_every=15)

fig, ax = plt.subplots(figsize=(9,4.5))
ax.set_xlim(-80, 80); ax.set_ylim(0, 0.12)
ax.fill_between(x, 0, (V/barrier_height)*0.11, color="0.85", label="barrier")
ax.set_xlabel("x"); ax.set_title("quantum tunneling: it leaks through the wall")
prob, = ax.plot([], [], color="crimson")
ax.legend(loc="upper right")

def update(i):
    prob.set_data(x, np.abs(frames[i])**2)
    return [prob]

anim = FuncAnimation(fig, update, frames=len(frames), blit=True, interval=30)
anim.save("media/tunneling.gif", writer=PillowWriter(fps=30))
plt.show()

# how much got through? integrate probability on the far side at the end
dx = x[1]-x[0]
transmitted = np.sum(np.abs(frames[-1][x > 3])**2)*dx
print(f"transmitted fraction (tunneled): {transmitted:.3f}")
