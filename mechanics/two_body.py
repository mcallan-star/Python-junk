# two body gravity. two masses pulling on each other with F = G m1 m2 / r^2.
# give the small one a sideways kick and it orbits!! first time i saw an orbit come
# out of just newton + a loop i was so happy. using leapfrog (velocity verlet) because
# it keeps orbits from spiraling the way euler did to my spring.

import numpy as np
import matplotlib.pyplot as plt

G = 1.0
m1, m2 = 1.0, 0.001        #a sun and a little planet

# start: sun at origin, planet out to the right, moving up for a circular-ish orbit
r1 = np.array([0.0, 0.0]); v1 = np.array([0.0, 0.0])
r2 = np.array([1.0, 0.0]); v2 = np.array([0.0, 1.0])   #v ~ sqrt(G m1 / r) = 1

def accel(ra, rb, mb):
    d = rb - ra
    return G*mb*d/np.linalg.norm(d)**3

dt = 0.002; n = 4000
path = np.zeros((n,2))
a2 = accel(r2, r1, m1)
for i in range(n):
    path[i] = r2
    # velocity verlet
    r2 = r2 + v2*dt + 0.5*a2*dt**2
    a2_new = accel(r2, r1, m1)
    v2 = v2 + 0.5*(a2 + a2_new)*dt
    a2 = a2_new

plt.figure(figsize=(6,6))
plt.plot(path[:,0], path[:,1], lw=1)
plt.plot(0, 0, "yo", ms=14, label="sun")
plt.axis("equal"); plt.legend()
plt.title("two body orbit (it actually orbits!!)")
plt.show()
