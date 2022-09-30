# FIRST double slit attempt and its kinda wrong, keeping it as a lesson.
# i just added two cosines of the path difference and called it a day. it gives
# fringes but theyre all the same height -- real double slit fringes get dimmer
# away from the center because of the single-slit diffraction envelope, which i
# totally forgot here. the fixed version is in double_slit.py (with the underscore).
import numpy as np
import matplotlib.pyplot as plt

d = 20.0          #slit separation (units of wavelength-ish, im being sloppy)
screen = np.linspace(-0.5, 0.5, 1000)   #angle on the screen, radians

# path difference between the two slits = d*sin(theta) ~ d*theta for small angle
delta = d*screen
I = (np.cos(np.pi*delta))**2     #just the two-slit part, NO envelope. wrong-ish

plt.plot(screen, I)
plt.title("double slit (first try -- fringes dont fade, thats not right)")
plt.xlabel("angle"); plt.ylabel("intensity")
plt.show()
