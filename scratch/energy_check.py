# suspicious that my euler sims are leaking/gaining energy
# total energy of a pendulum = KE + PE = 0.5*m*L^2*w^2 + m*g*L*(1-cos(theta))
# if my integrator is good this should stay flat. lets see (spoiler: it doesnt)
import numpy as np
import matplotlib.pyplot as plt

g = 9.8; L = 1.0; m = 1.0; dt = 0.01
th = 1.0; w = 0.0
E = []
for i in range(3000):
    a = -(g/L)*np.sin(th)
    w = w + a*dt
    th = th + w*dt
    ke = 0.5*m*L**2*w**2
    pe = m*g*L*(1-np.cos(th))
    E.append(ke+pe)

plt.plot(E)
plt.xlabel("step"); plt.ylabel("total energy (J)")
plt.title("energy should be flat... its NOT, it climbs")
plt.grid(True)
plt.show()
# so euler is pumping energy in. need a better integrator. (foreshadowing: rk4)
