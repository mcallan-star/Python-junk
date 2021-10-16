# resonance!! sweep the drive frequency and measure the steady state amplitude.
# when you drive near the natural frequency the response blows up. this is why
# soldiers break step on bridges. the peak sits near sqrt(k/m) and gets sharper
# for less damping.

import numpy as np
import matplotlib.pyplot as plt

k = 4.0; m = 1.0; F0 = 1.0
w0 = np.sqrt(k/m)   #natural frequency

def steady_amplitude(wd, c):
    # integrate long enough to kill the transient, then measure the swing
    def deriv(s, t):
        x, v = s
        return np.array([v, (-k*x - c*v + F0*np.cos(wd*t))/m])
    dt = 0.01; n = 4000
    s = np.array([0.0, 0.0])
    xs = []
    for i in range(n):
        t = i*dt
        k1 = deriv(s, t)
        k2 = deriv(s+0.5*dt*k1, t+0.5*dt)
        k3 = deriv(s+0.5*dt*k2, t+0.5*dt)
        k4 = deriv(s+dt*k3, t+dt)
        s = s + (dt/6)*(k1+2*k2+2*k3+k4)
        if i > n//2:            #only look at the second half, after transient dies
            xs.append(s[0])
    return (max(xs) - min(xs))/2.0

wds = np.linspace(0.3, 3.5, 80)
for c in [0.2, 0.5, 1.0]:
    amp = [steady_amplitude(wd, c) for wd in wds]
    plt.plot(wds, amp, label=f"c={c}")

plt.axvline(w0, color="black", ls="--", lw=0.7, label="natural freq")
plt.legend(); plt.grid(True)
plt.xlabel("drive frequency"); plt.ylabel("steady amplitude")
plt.title("resonance curves -- less damping = taller sharper peak")
plt.savefig("media/resonance.png", dpi=110)
plt.show()
