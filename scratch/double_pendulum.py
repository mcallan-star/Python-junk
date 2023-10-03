# double pendulum, the poster child for chaos. two pendulums hooked together and the
# motion goes completely wild. the equations of motion are a NIGHTMARE to derive (i
# looked them up, lagrangian mechanics) so dont ask me to explain every term. point is
# you integrate them with rk4 and trace the tip -- it never repeats. mesmerizing scratch.
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
L1 = L2 = 1.0
m1 = m2 = 1.0

def deriv(s):
    th1, w1, th2, w2 = s
    d = th2 - th1
    den1 = (m1+m2)*L1 - m2*L1*np.cos(d)**2
    a1 = (m2*L1*w1**2*np.sin(d)*np.cos(d)
          + m2*g*np.sin(th2)*np.cos(d)
          + m2*L2*w2**2*np.sin(d)
          - (m1+m2)*g*np.sin(th1)) / den1
    den2 = (L2/L1)*den1
    a2 = (-m2*L2*w2**2*np.sin(d)*np.cos(d)
          + (m1+m2)*(g*np.sin(th1)*np.cos(d) - L1*w1**2*np.sin(d) - g*np.sin(th2))) / den2
    return np.array([w1, a1, w2, a2])

def rk4(s, dt):
    k1=deriv(s); k2=deriv(s+0.5*dt*k1); k3=deriv(s+0.5*dt*k2); k4=deriv(s+dt*k3)
    return s + (dt/6)*(k1+2*k2+2*k3+k4)

s = np.array([np.pi/2, 0, np.pi/2 + 0.01, 0])   #start both near horizontal
dt = 0.005; n = 6000
tip = np.zeros((n,2))
for i in range(n):
    th1, _, th2, _ = s
    x = L1*np.sin(th1) + L2*np.sin(th2)
    y = -L1*np.cos(th1) - L2*np.cos(th2)
    tip[i] = (x, y)
    s = rk4(s, dt)

plt.figure(figsize=(6,6))
plt.plot(tip[:,0], tip[:,1], lw=0.5)
plt.axis("equal"); plt.title("double pendulum tip, pure chaos")
plt.show()
