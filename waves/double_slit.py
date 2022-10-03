# double slit DONE RIGHT this time. the real pattern is two things multiplied:
#   1. the two-slit interference: cos^2(pi d sin(theta)/lambda)  -> the fast fringes
#   2. the single-slit diffraction envelope: sinc^2(pi a sin(theta)/lambda)  -> the
#      slowly-fading brightness because each slit has a finite width a.
# multiply them and you get the classic pattern: evenly spaced fringes that fade out.

import numpy as np
import matplotlib.pyplot as plt

wavelength = 500e-9      #500 nm green light
a = 20e-6               #slit width
d = 100e-6             #slit separation (d > a)
L = 1.0               #distance to screen (m)

# positions on the screen, convert to angle
ys = np.linspace(-0.03, 0.03, 2000)
theta = np.arctan(ys/L)
s = np.sin(theta)

beta = np.pi*a*s/wavelength      #single slit phase
alpha = np.pi*d*s/wavelength     #two slit phase

# np.sinc(x) is sin(pi x)/(pi x), so i divide the arg by pi to get plain sinc
envelope = (np.sinc(beta/np.pi))**2
fringes = (np.cos(alpha))**2
I = envelope * fringes

fig, ax = plt.subplots(2, 1, figsize=(9, 6), sharex=True,
                       gridspec_kw={"height_ratios":[3,1]})
ax[0].plot(ys*1000, I, color="tab:green")
ax[0].plot(ys*1000, envelope, "k--", lw=0.8, label="diffraction envelope")
ax[0].set_ylabel("intensity"); ax[0].legend()
ax[0].set_title("double slit: fringes under a fading envelope (the right way)")

# fake the actual screen as a brightness strip
ax[1].imshow(I[np.newaxis,:], extent=[ys[0]*1000, ys[-1]*1000, 0, 1],
             aspect="auto", cmap="gray")
ax[1].set_yticks([]); ax[1].set_xlabel("position on screen (mm)")
fig.tight_layout()
fig.savefig("media/double_slit.png", dpi=110)
plt.show()
