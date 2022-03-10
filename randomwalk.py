# random walk, 1d. the drunk man problem. each step is +1 or -1 with a coin flip.
# the cool part: even though each walk is random, on AVERAGE the distance from start
# grows like sqrt(number of steps). thats diffusion hiding in here.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)   #so my plot is the same every time i run it

steps = 500
n_walks = 5

plt.figure(figsize=(10,5))
for w in range(n_walks):
    pos = 0
    path = [0]
    for s in range(steps):
        step = 1 if np.random.rand() < 0.5 else -1     #coin flip
        pos = pos + step
        path.append(pos)
    plt.plot(path, alpha=0.7)

# overlay the +/- sqrt(N) envelope, the typical spread
N = np.arange(steps+1)
plt.plot(N, np.sqrt(N), "k--", lw=1)
plt.plot(N, -np.sqrt(N), "k--", lw=1, label="+/- sqrt(N)")
plt.legend()
plt.xlabel("step"); plt.ylabel("position")
plt.title("1d random walks, they spread like sqrt(N)")
plt.grid(True)
plt.show()
