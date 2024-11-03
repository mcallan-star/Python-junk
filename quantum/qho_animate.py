"""A wavepacket sloshing in the harmonic well.

If you put a gaussian slightly off-center in a parabolic trap, it slides back and forth
forever (a "coherent state") -- the closest quantum thing to a classical ball rolling in
a bowl. I evolve it with the split-step solver and the probability blob just oscillates.
Nice clean periodic motion, a good contrast to the chaotic classical stuff earlier in
this repo.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from split_step import split_step_evolve, gaussian_packet

m = 1.0; w = 0.3
N = 1024
x = np.linspace(-40, 40, N)
V = 0.5*m*w**2*x**2                      # harmonic trap

psi0 = gaussian_packet(x, x0=-12, k0=0.0, sigma=2.5)   # displaced, at rest
frames = split_step_evolve(psi0, x, V, dt=0.02, steps=2400, record_every=12)

fig, ax = plt.subplots(figsize=(9,4.5))
ax.set_xlim(-40, 40); ax.set_ylim(0, 0.22)
ax.plot(x, V*0.02, "k", lw=1, alpha=0.5)   # show the bowl (scaled)
ax.set_xlabel("x"); ax.set_title("coherent state sloshing in a harmonic trap")
prob, = ax.plot([], [], color="tab:green")

def update(i):
    prob.set_data(x, np.abs(frames[i])**2)
    return [prob]

anim = FuncAnimation(fig, update, frames=len(frames), blit=True, interval=30)
anim.save("media/qho.gif", writer=PillowWriter(fps=30))
plt.show()
