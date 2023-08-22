# phase space of the pendulum: theta vs angular velocity.
# each starting energy traces its own loop. low energy = little ellipses (basically
# shm), higher = stretched loops, and over-the-top energy stops looping and just
# rotates forever.
#
# also spits out a gif of a dot riding around one of the orbits (saves the static png too)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

g = 9.8; L = 1.0
dt = 0.005; n = 3000

def d(st):
    return np.array([st[1], -(g/L)*np.sin(st[0])])

def trajectory(theta0, w0):
    s = np.array([theta0, w0])
    th = np.zeros(n); w = np.zeros(n)
    for i in range(n):
        th[i], w[i] = s
        k1=d(s); k2=d(s+0.5*dt*k1); k3=d(s+0.5*dt*k2); k4=d(s+dt*k3)
        s = s + (dt/6)*(k1+2*k2+2*k3+k4)
    return th, w

# --- static figure: a family of orbits ---
fig1 = plt.figure(figsize=(7,6))
orbits = []
for theta0 in np.linspace(0.3, 3.0, 7):
    th, w = trajectory(theta0, 0.0)
    orbits.append((th, w))
    plt.plot(th, w, lw=1)
plt.xlabel("theta (rad)"); plt.ylabel("angular velocity")
plt.title("pendulum phase space")
plt.grid(True)
fig1.savefig("media/pendulum_phase.png", dpi=110)

# --- animated gif: a dot tracing one nice orbit ---
th, w = trajectory(2.4, 0.0)
fig2, ax = plt.subplots(figsize=(6,5))
for o_th, o_w in orbits:
    ax.plot(o_th, o_w, color="0.85", lw=0.8)
ax.plot(th, w, color="tab:blue", lw=1)
dot, = ax.plot([], [], "o", color="crimson", ms=8)
trail, = ax.plot([], [], color="crimson", lw=2, alpha=0.6)
ax.set_xlabel("theta"); ax.set_ylabel("angular velocity")
ax.set_title("riding the phase space orbit")
ax.grid(True)

step = 20
def update(frame):
    j = frame*step
    dot.set_data([th[j]], [w[j]])
    trail.set_data(th[max(0,j-300):j], w[max(0,j-300):j])
    return dot, trail

anim = FuncAnimation(fig2, update, frames=n//step, blit=True, interval=40)
anim.save("media/pendulum_phase.gif", writer=PillowWriter(fps=25))
plt.show()
