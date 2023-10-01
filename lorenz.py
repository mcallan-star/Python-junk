# the lorenz attractor. a toy weather model from the 60s that turned out to be chaotic
# and gave us the butterfly effect. three coupled ODEs:
#   x' = sigma (y - x)
#   y' = x (rho - z) - y
#   z' = x y - beta z
# the trajectory never repeats and never escapes, it winds forever around two lobes
# that look like butterfly wings. had to animate this one, its mesmerizing.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

sigma, rho, beta = 10.0, 28.0, 8.0/3.0

def deriv(s):
    x, y, z = s
    return np.array([sigma*(y-x), x*(rho-z)-y, x*y-beta*z])

def rk4(s, dt):
    k1=deriv(s); k2=deriv(s+0.5*dt*k1); k3=deriv(s+0.5*dt*k2); k4=deriv(s+dt*k3)
    return s + (dt/6)*(k1+2*k2+2*k3+k4)

dt = 0.005; n = 6000
pts = np.zeros((n,3))
s = np.array([1.0, 1.0, 1.0])
for i in range(n):
    pts[i] = s; s = rk4(s, dt)

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("black"); fig.patch.set_facecolor("black")
ax.set_axis_off()
ax.set_xlim(-25,25); ax.set_ylim(-30,30); ax.set_zlim(0,55)
ax.set_title("lorenz attractor", color="white")
line, = ax.plot([], [], [], lw=0.7, color="cyan")
head, = ax.plot([], [], [], "o", color="white", ms=3)

step = 25
def update(frame):
    k = frame*step
    line.set_data(pts[:k,0], pts[:k,1]); line.set_3d_properties(pts[:k,2])
    if k > 0:
        head.set_data([pts[k-1,0]], [pts[k-1,1]]); head.set_3d_properties([pts[k-1,2]])
    ax.view_init(elev=20, azim=frame*0.5)     #slowly rotate the camera too
    return line, head

anim = FuncAnimation(fig, update, frames=n//step, blit=False, interval=40)
anim.save("media/lorenz.gif", writer=PillowWriter(fps=25))
plt.show()
