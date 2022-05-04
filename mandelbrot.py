# not physics really but i couldnt resist. the mandelbrot set.
# for each point c in the complex plane, iterate z -> z^2 + c starting at z=0.
# if it stays bounded, c is in the set (black). if it escapes, color it by HOW FAST
# it ran away. first time i used numpy on a whole complex grid at once instead of loops.

import numpy as np
import matplotlib.pyplot as plt

W, H = 800, 600
xmin, xmax = -2.2, 0.8
ymin, ymax = -1.2, 1.2
max_iter = 80

re = np.linspace(xmin, xmax, W)
im = np.linspace(ymin, ymax, H)
C = re[np.newaxis, :] + 1j*im[:, np.newaxis]    #the whole complex grid in one array

Z = np.zeros_like(C)
escape = np.zeros(C.shape, dtype=int)
alive = np.ones(C.shape, dtype=bool)

for i in range(max_iter):
    Z[alive] = Z[alive]**2 + C[alive]
    escaped_now = alive & (np.abs(Z) > 2)       #just crossed the escape radius
    escape[escaped_now] = i
    alive[escaped_now] = False
escape[alive] = max_iter                        #never escaped = in the set

plt.figure(figsize=(9, 6.5))
plt.imshow(escape, extent=[xmin, xmax, ymin, ymax], cmap="magma", origin="lower")
plt.axis("off")
plt.title("mandelbrot (my first vectorized numpy, no loops over pixels!)")
plt.savefig("media/mandelbrot.png", dpi=110, bbox_inches="tight")
plt.show()
