# THE showdown. euler keeps leaking energy on my oscillators so i finally learned rk4.
# both integrate the same spring (x'' = -(k/m) x) and i plot the energy over time.
# rk4 evaluates the slope 4 times per step and weights them, way more accurate.

import numpy as np
import matplotlib.pyplot as plt

k = 4.0; m = 1.0
omega = np.sqrt(k/m)

def deriv(state):
    # state = [x, v], returns [x', v'] = [v, -(k/m)x]
    x, v = state
    return np.array([v, -(k/m)*x])

def euler_step(state, dt):
    return state + deriv(state)*dt

def rk4_step(state, dt):
    k1 = deriv(state)
    k2 = deriv(state + 0.5*dt*k1)
    k3 = deriv(state + 0.5*dt*k2)
    k4 = deriv(state + dt*k3)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

dt = 0.05
n = 800
t = np.arange(n)*dt

s_e = np.array([1.0, 0.0]); s_r = np.array([1.0, 0.0])
xe = np.zeros(n); xr = np.zeros(n)
Ee = np.zeros(n); Er = np.zeros(n)

def energy(s):
    x, v = s
    return 0.5*m*v**2 + 0.5*k*x**2

for i in range(n):
    xe[i] = s_e[0]; xr[i] = s_r[0]
    Ee[i] = energy(s_e); Er[i] = energy(s_r)
    s_e = euler_step(s_e, dt)
    s_r = rk4_step(s_r, dt)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
ax1.plot(t, xe, label="euler", alpha=0.8)
ax1.plot(t, xr, label="rk4", alpha=0.8)
ax1.plot(t, np.cos(omega*t), "k--", lw=0.8, label="exact")
ax1.set_title("position"); ax1.set_xlabel("t"); ax1.legend(); ax1.grid(True)

ax2.plot(t, Ee, label="euler")
ax2.plot(t, Er, label="rk4")
ax2.set_title("total energy (should be flat!)")
ax2.set_xlabel("t"); ax2.legend(); ax2.grid(True)

fig.suptitle("euler bleeds energy, rk4 holds it. lesson learned")
fig.tight_layout()
fig.savefig("media/euler_vs_rk4.png", dpi=110)
plt.show()
