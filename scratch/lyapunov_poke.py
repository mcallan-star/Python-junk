# poking at "how chaotic is the lorenz system, really". run two trajectories that start
# 1e-8 apart and watch the gap grow. on a log plot the early growth is a straight line,
# and its SLOPE is (roughly) the largest lyapunov exponent. positive slope = chaos.
# very rough, not a real estimator, just building intuition.
import numpy as np
import matplotlib.pyplot as plt

sigma, rho, beta = 10.0, 28.0, 8/3
def deriv(s):
    x,y,z=s
    return np.array([sigma*(y-x), x*(rho-z)-y, x*y-beta*z])
def rk4(s,dt):
    k1=deriv(s);k2=deriv(s+.5*dt*k1);k3=deriv(s+.5*dt*k2);k4=deriv(s+dt*k3)
    return s+(dt/6)*(k1+2*k2+2*k3+k4)

dt=0.005; n=4000
a=np.array([1.,1.,1.]); b=a+np.array([1e-8,0,0])
gap=[]
for i in range(n):
    a=rk4(a,dt); b=rk4(b,dt)
    gap.append(np.linalg.norm(a-b))

plt.semilogy(np.arange(n)*dt, gap)
plt.xlabel("time"); plt.ylabel("separation (log)")
plt.title("lorenz: tiny difference explodes -> positive lyapunov")
plt.grid(True, which="both")
plt.show()
