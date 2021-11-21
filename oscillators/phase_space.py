# phase space! instead of theta vs time, plot theta vs angular velocity.
# for the pendulum each starting energy traces a different loop. low energy = little
# ellipses (basically shm), high energy = the loops stretch out, and if you give it
# enough to go over the top it stops looping and just rotates. so pretty.

import numpy as np
import matplotlib.pyplot as plt

g = 9.8; L = 1.0
dt = 0.005; n = 3000

def trajectory(theta0, w0):
    s = np.array([theta0, w0])
    th = np.zeros(n); w = np.zeros(n)
    for i in range(n):
        th[i], w[i] = s
        a = -(g/L)*np.sin(s[0])
        # rk4
        def d(st): return np.array([st[1], -(g/L)*np.sin(st[0])])
        k1=d(s); k2=d(s+0.5*dt*k1); k3=d(s+0.5*dt*k2); k4=d(s+dt*k3)
        s = s + (dt/6)*(k1+2*k2+2*k3+k4)
    return th, w

plt.figure(figsize=(7,6))
for theta0 in np.linspace(0.3, 3.0, 7):
    th, w = trajectory(theta0, 0.0)
    plt.plot(th, w, lw=1)
plt.xlabel("theta (rad)"); plt.ylabel("angular velocity")
plt.title("pendulum phase space")
plt.grid(True)
plt.savefig("media/pendulum_phase.png", dpi=110)
plt.show()
