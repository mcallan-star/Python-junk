# fresnel equations -- how much light reflects off a surface vs angle, and it depends
# on polarization. we measured this on glass in lab (Brewster angle day). there are two
# polarizations: s (perpendicular) and p (parallel). the magic: at Brewster's angle the
# p reflection drops to ZERO. thats why polarized sunglasses kill glare.

import numpy as np
import matplotlib.pyplot as plt

n1 = 1.0      #air
n2 = 1.5      #glass

theta_i = np.linspace(0, np.pi/2, 500)
# snells law for the transmitted angle
sin_t = n1/n2*np.sin(theta_i)
theta_t = np.arcsin(np.clip(sin_t, -1, 1))

cos_i = np.cos(theta_i); cos_t = np.cos(theta_t)

# amplitude reflection coefficients
rs = (n1*cos_i - n2*cos_t) / (n1*cos_i + n2*cos_t)
rp = (n2*cos_i - n1*cos_t) / (n2*cos_i + n1*cos_t)

Rs = rs**2     #reflectance is amplitude squared
Rp = rp**2

brewster = np.arctan(n2/n1)    #where Rp hits zero

plt.figure(figsize=(8,5))
plt.plot(np.degrees(theta_i), Rs, label="s-pol (perpendicular)")
plt.plot(np.degrees(theta_i), Rp, label="p-pol (parallel)")
plt.axvline(np.degrees(brewster), color="k", ls="--", lw=0.8,
            label=f"Brewster {np.degrees(brewster):.1f} deg")
plt.legend(); plt.grid(True)
plt.xlabel("angle of incidence (deg)"); plt.ylabel("reflectance R")
plt.title("fresnel: p-polarization vanishes at Brewster's angle")
plt.savefig("media/fresnel.png", dpi=110)
plt.show()
