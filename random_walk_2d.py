# 2d random walk. each step picks a random direction. yes the file name is
# random_walk_2d but the 1d one is randomwalk.py with no underscores, i KNOW, my
# naming is a mess, leaving it.
#
# UPDATE: animated this one. watching the walk actually wander is way more fun than
# the static spaghetti. saves both the png and a gif now.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

np.random.seed(3)
steps = 4000

def walk2d(steps):
    x = np.zeros(steps); y = np.zeros(steps)
    for i in range(1, steps):
        ang = np.random.rand()*2*np.pi
        x[i] = x[i-1] + np.cos(ang)
        y[i] = y[i-1] + np.sin(ang)
    return x, y

# static: a few walks
plt.figure(figsize=(7,7))
for _ in range(4):
    x, y = walk2d(steps)
    plt.plot(x, y, lw=0.8)
    plt.plot(x[-1], y[-1], "o")
plt.plot(0, 0, "k*", ms=12, label="start")
plt.legend(); plt.axis("equal")
plt.title("2d random walks")
plt.savefig("media/random_walk.png", dpi=110)

# animated: one walk drawing itself
x, y = walk2d(steps)
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(x.min()-2, x.max()+2); ax.set_ylim(y.min()-2, y.max()+2)
ax.set_aspect("equal"); ax.set_title("a drunk man's journey")
line, = ax.plot([], [], lw=1.0, color="tab:purple")
head, = ax.plot([], [], "o", color="crimson")
ax.plot(0, 0, "k*", ms=10)

step = 25
def update(frame):
    j = frame*step
    line.set_data(x[:j], y[:j])
    if j > 0:
        head.set_data([x[j-1]], [y[j-1]])
    return line, head

anim = FuncAnimation(fig, update, frames=steps//step, blit=True, interval=30)
anim.save("media/random_walk.gif", writer=PillowWriter(fps=30))
plt.show()
