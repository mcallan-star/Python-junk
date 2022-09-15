# two point sources making ripples that overlap. where crests meet crests -> bright,
# crest meets trough -> dark. thats interference. this is basically the optics lab i
# took but in code. each source emits cos(k*r - w*t); i add the fields then square to
# get intensity (intensity ~ |sum of waves|^2).

import numpy as np
import matplotlib.pyplot as plt

wavelength = 0.5
k = 2*np.pi/wavelength          #wavenumber

# grid of points in space
x = np.linspace(-10, 10, 600)
y = np.linspace(-10, 10, 600)
X, Y = np.meshgrid(x, y)

# two sources sitting on the x axis, a few wavelengths apart
sources = [(-2.0, 0.0), (2.0, 0.0)]

field = np.zeros_like(X)
for (sx, sy) in sources:
    r = np.sqrt((X-sx)**2 + (Y-sy)**2)
    field += np.cos(k*r) / np.sqrt(r + 0.1)   #1/sqrt(r) so amplitude falls off a bit

intensity = field**2

plt.figure(figsize=(7,6))
plt.imshow(intensity, extent=[-10,10,-10,10], cmap="inferno", origin="lower")
plt.plot([s[0] for s in sources], [s[1] for s in sources], "c.", ms=10)
plt.title("two source interference (intensity = |sum of waves|^2)")
plt.xlabel("x"); plt.ylabel("y")
plt.savefig("media/interference.png", dpi=110)
plt.show()
