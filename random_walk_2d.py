# 2d random walk. now each step picks a random direction. yes the file name is
# random_walk_2d but the 1d one is randomwalk.py with no underscores, i KNOW, my
# naming is a mess, leaving it.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
steps = 4000

def walk2d(steps):
    x = np.zeros(steps); y = np.zeros(steps)
    for i in range(1, steps):
        ang = np.random.rand()*2*np.pi      #random direction
        x[i] = x[i-1] + np.cos(ang)
        y[i] = y[i-1] + np.sin(ang)
    return x, y

plt.figure(figsize=(7,7))
for _ in range(4):
    x, y = walk2d(steps)
    plt.plot(x, y, lw=0.8)
    plt.plot(x[-1], y[-1], "o")            #mark where it ended up
plt.plot(0, 0, "k*", ms=12, label="start")
plt.legend()
plt.axis("equal")
plt.title("2d random walks")
plt.savefig("media/random_walk.png", dpi=110)
plt.show()
