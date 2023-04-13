# checking keplers third law: T^2 is proportional to a^3 (period squared ~ radius cubed).
# i put planets on circular orbits at different radii, measure how long one lap takes,
# then plot T^2 vs a^3 and see if its a straight line through the origin. (it is.)

import numpy as np
import matplotlib.pyplot as plt

GM = 4*np.pi**2     #earth units again

def period(r):
    pos = np.array([r, 0.0]); vel = np.array([0.0, np.sqrt(GM/r)])
    def accel(p): return -GM*p/np.linalg.norm(p)**3
    dt = 0.0005; a = accel(pos); t = 0.0; prev_y = 0.0
    for i in range(2_000_000):
        pos = pos + vel*dt + 0.5*a*dt**2
        a2 = accel(pos); vel = vel + 0.5*(a+a2)*dt; a = a2
        t += dt
        # detect one full lap: crossed y=0 going up after having gone around
        if i > 10 and prev_y < 0 and pos[1] >= 0:
            return t
        prev_y = pos[1]
    return t

radii = np.array([0.4, 0.7, 1.0, 1.5, 2.0])
Ts = np.array([period(r) for r in radii])

print("radius (AU) | period (yr) | T^2/a^3 (should be ~1)")
for r, T in zip(radii, Ts):
    print(f"  {r:.2f}      |   {T:.3f}    |  {T**2/r**3:.3f}")

plt.plot(radii**3, Ts**2, "o-")
plt.xlabel("a^3"); plt.ylabel("T^2")
plt.title("kepler III: T^2 vs a^3 is a straight line")
plt.grid(True)
plt.show()
