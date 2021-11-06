# damped harmonic oscillator. now theres a friction term -c*v
#   x'' + (c/m) x' + (k/m) x = 0
# depending on c you get underdamped (wiggles that die), critically damped, or
# overdamped (no wiggle, just creeps back). using rk4 now because i know better.

import numpy as np
import matplotlib.pyplot as plt

k = 4.0; m = 1.0

def deriv(state, c):
    x, v = state
    return np.array([v, -(k/m)*x - (c/m)*v])

def rk4_step(state, dt, c):
    k1 = deriv(state, c)
    k2 = deriv(state + 0.5*dt*k1, c)
    k3 = deriv(state + 0.5*dt*k2, c)
    k4 = deriv(state + dt*k3, c)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

dt = 0.02; n = 1000
t = np.arange(n)*dt

# critical damping happens at c = 2*sqrt(k*m)
c_crit = 2*np.sqrt(k*m)
cases = {"underdamped (c=0.5)": 0.5,
         "critical (c=4.0)": c_crit,
         "overdamped (c=9.0)": 9.0}

for label, c in cases.items():
    s = np.array([1.0, 0.0])
    x = np.zeros(n)
    for i in range(n):
        x[i] = s[0]
        s = rk4_step(s, dt, c)
    plt.plot(t, x, label=label)

plt.axhline(0, color="black", lw=0.5)
plt.legend(); plt.grid(True)
plt.xlabel("t"); plt.ylabel("x")
plt.title("damped oscillator, three regimes")
plt.show()
