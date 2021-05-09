# simple harmonic motion, a mass on a spring
# F = -k*x  so  a = -(k/m)*x
# i want to check my euler stepping against the real answer which is just a cosine

import numpy as np
import matplotlib.pyplot as plt

k = 4.0      #spring constant
m = 1.0      #mass
x0 = 1.0     #start pulled out to 1
v0 = 0.0     #start at rest
dt = 0.05
T_total = 20.0

omega = np.sqrt(k/m)     #angular frequency, this is the thing that sets the period

n = int(T_total/dt)
t = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)
x[0] = x0
v[0] = v0

# euler again
for i in range(n-1):
    a = -(k/m)*x[i]
    v[i+1] = v[i] + a*dt
    x[i+1] = x[i] + v[i]*dt      #using old v, thats just how euler goes
    t[i+1] = t[i] + dt

# the exact answer, x(t) = x0*cos(omega*t) since it starts at rest
exact = x0*np.cos(omega*t)

plt.plot(t, x, label="my euler")
plt.plot(t, exact, "--", label="exact cos")
plt.legend()
plt.xlabel("t (s)"); plt.ylabel("x (m)")
plt.title("spring: euler vs the real cosine")
plt.grid(True)
# heads up: my euler one slowly grows!! the amplitude creeps up. something is leaking
plt.show()
