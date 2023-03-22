# toy solar system, inner planets. units where earths orbit is r=1 (1 AU) and one
# year is the time unit, which makes G*M_sun = 4*pi^2. the planet distances are roughly
# real (in AU) but the SIZES of the dots are totally fake, you couldnt see them otherwise.
# circular orbit speed is v = sqrt(GM/r).

import numpy as np
import matplotlib.pyplot as plt

GM = 4*np.pi**2
planets = {                # name: (orbit radius AU, color)
    "Mercury": (0.39, "gray"),
    "Venus":   (0.72, "gold"),
    "Earth":   (1.00, "tab:blue"),
    "Mars":    (1.52, "tab:red"),
}

plt.figure(figsize=(7,7))
plt.plot(0, 0, "o", color="orange", ms=18, label="Sun")
th = np.linspace(0, 2*np.pi, 200)
for name, (r, c) in planets.items():
    plt.plot(r*np.cos(th), r*np.sin(th), color=c, lw=0.7)   #orbit ring
    plt.plot(r, 0, "o", color=c, ms=8, label=name)          #planet at start
plt.axis("equal"); plt.legend(loc="upper right")
plt.title("toy inner solar system (distances ~real, sizes fake)")
plt.savefig("media/solar_system.png", dpi=110)
plt.show()
