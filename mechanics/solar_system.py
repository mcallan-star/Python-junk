# toy solar system, inner planets. units where earths orbit is r=1 (1 AU) and one
# year is the time unit, which makes G*M_sun = 4*pi^2. distances are roughly real (AU),
# dot sizes are fake. circular orbit speed v = sqrt(GM/r).
#
# the planets actually go around: inner ones whip, mars crawls (keplers law for free)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

GM = 4*np.pi**2
planets = [   # name, radius AU, color, size
    ("Mercury", 0.39, "gray", 5),
    ("Venus",   0.72, "gold", 8),
    ("Earth",   1.00, "tab:blue", 9),
    ("Mars",    1.52, "tab:red", 7),
]

# each planet: pos and vel for a circular orbit, integrate with leapfrog
state = []
for name, r, c, sz in planets:
    pos = np.array([r, 0.0])
    vel = np.array([0.0, np.sqrt(GM/r)])    #circular speed, perpendicular
    state.append([pos, vel, c, sz, name])

def accel(pos):
    d = -pos
    return GM*d/np.linalg.norm(d)**3        #pull toward the sun at origin

dt = 0.002; n = 1400
hist = [np.zeros((n,2)) for _ in state]
accs = [accel(s[0]) for s in state]
for i in range(n):
    for j, s in enumerate(state):
        hist[j][i] = s[0]
        s[0] = s[0] + s[1]*dt + 0.5*accs[j]*dt**2
        a_new = accel(s[0])
        s[1] = s[1] + 0.5*(accs[j] + a_new)*dt
        accs[j] = a_new

# static (orbit rings)
plt.figure(figsize=(7,7))
plt.plot(0,0,"o",color="orange",ms=18)
for j, s in enumerate(state):
    plt.plot(hist[j][:,0], hist[j][:,1], color=s[2], lw=0.7)
plt.axis("equal"); plt.title("toy inner solar system")
plt.savefig("media/solar_system.png", dpi=110)

# animated
fig, ax = plt.subplots(figsize=(7,7))
ax.set_xlim(-1.8,1.8); ax.set_ylim(-1.8,1.8); ax.set_aspect("equal")
ax.set_facecolor("#05060f"); ax.set_title("inner planets going around")
ax.plot(0,0,"o",color="orange",ms=16)
dots, rings = [], []
for j, s in enumerate(state):
    ax.plot(hist[j][:,0], hist[j][:,1], color=s[2], lw=0.5, alpha=0.5)
    dots.append(ax.plot([], [], "o", color=s[2], ms=s[3])[0])

step = 6
def update(frame):
    k = frame*step
    for j in range(len(state)):
        dots[j].set_data([hist[j][k,0]], [hist[j][k,1]])
    return dots

anim = FuncAnimation(fig, update, frames=n//step, blit=True, interval=30)
anim.save("media/solar_system.gif", writer=PillowWriter(fps=30))
plt.show()
