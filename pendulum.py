# pendulum! the small angle one is easy (its just shm) but the REAL one is nonlinear
# because of the sin(theta). small angle assumes sin(theta) ~ theta which is only
# true for tiny swings. lets see when they fall apart

import numpy as np
import matplotlib.pyplot as plt

g = 9.8
L = 1.0          #length of the pendulum in meters
dt = 0.01
T_total = 10.0
n = int(T_total/dt)

theta0 = 1.2     #start angle in RADIANS (about 70 deg, pretty big on purpose)

# --- the full nonlinear one --- theta'' = -(g/L) sin(theta)
th = np.zeros(n); w = np.zeros(n); t = np.zeros(n)
th[0] = theta0
for i in range(n-1):
    a = -(g/L)*np.sin(th[i])
    w[i+1] = w[i] + a*dt
    th[i+1] = th[i] + w[i]*dt
    t[i+1] = t[i] + dt

# --- small angle approx --- theta'' = -(g/L) theta, so its a cosine
omega = np.sqrt(g/L)
small = theta0*np.cos(omega*t)

plt.plot(t, th, label="full (with sin)")
plt.plot(t, small, "--", label="small angle approx")
plt.legend()
plt.xlabel("t (s)"); plt.ylabel("theta (rad)")
plt.title("pendulum: they diverge for big swings!!")
plt.grid(True)
plt.show()
# yep. they start together then drift apart, the real pendulum is SLOWER for big angles
