# gaussian beam, straight out of my optics lab. a laser beam isnt a pencil-thin line,
# it has a waist w0 at the focus and spreads as you move away:
#   w(z) = w0 * sqrt(1 + (z/zR)^2),   zR = pi*w0^2/lambda  (the rayleigh range)
# near the waist it barely grows, far away it spreads linearly into a cone.

import numpy as np
import matplotlib.pyplot as plt

wavelength = 633e-9     #HeNe red, the laser we actually used
w0 = 0.3e-3            #beam waist, 0.3 mm
zR = np.pi*w0**2/wavelength

z = np.linspace(-6*zR, 6*zR, 600)
w = w0*np.sqrt(1 + (z/zR)**2)

# the 2d intensity I(r,z) = (w0/w)^2 * exp(-2 r^2 / w^2)
r = np.linspace(-3*w0*4, 3*w0*4, 400)
Z, R = np.meshgrid(z, r)
W = w0*np.sqrt(1 + (Z/zR)**2)
I = (w0/W)**2 * np.exp(-2*R**2/W**2)

fig, ax = plt.subplots(figsize=(10,4.5))
ax.imshow(I, extent=[z[0]*1000, z[-1]*1000, r[0]*1000, r[-1]*1000],
          aspect="auto", cmap="hot", origin="lower")
ax.plot(z*1000, w*1000, "c", lw=1, label="beam radius w(z)")
ax.plot(z*1000, -w*1000, "c", lw=1)
ax.axvline(0, color="white", ls=":", lw=0.8)
ax.set_xlabel("z (mm)"); ax.set_ylabel("r (mm)")
ax.set_title(f"gaussian beam, HeNe, waist {w0*1e3:.1f} mm, zR={zR*1e3:.1f} mm")
ax.legend()
fig.savefig("media/gaussian_beam.png", dpi=110)
plt.show()
