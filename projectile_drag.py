# same as projectile.py but now with air drag
# honestly i basically copy pasted projectile.py and added the drag term oops
# drag force is -b*v, opposite the velocity. so it slows down

import numpy as np
import matplotlib.pyplot as plt

g = 9.8
v0 = 20.0
angle = 50
dt = 0.01
b = 0.15      #drag coefficient, made up. bigger = more air resistance

vx = v0 * np.cos(angle * np.pi/180)
vy = v0 * np.sin(angle * np.pi/180)

xs = [0.0]
ys = [0.0]
x, y = 0.0, 0.0

# drag pulls on BOTH x and y now, proportional to speed in that direction
while y >= 0 or len(ys) < 2:
    vx = vx - b*vx*dt              #drag on x
    vy = vy - g*dt - b*vy*dt       #gravity + drag on y
    x = x + vx*dt
    y = y + vy*dt
    xs.append(x)
    ys.append(y)

# plot the no-drag one too so i can see the difference
vx2 = v0 * np.cos(angle*np.pi/180)
vy2 = v0 * np.sin(angle*np.pi/180)
xs2, ys2, x2, y2 = [0.0], [0.0], 0.0, 0.0
while y2 >= 0 or len(ys2) < 2:
    vy2 = vy2 - g*dt
    x2 = x2 + vx2*dt
    y2 = y2 + vy2*dt
    xs2.append(x2); ys2.append(y2)

plt.plot(xs2, ys2, "--", label="no drag")
plt.plot(xs, ys, label="with drag")
plt.legend()
plt.xlabel("x (m)"); plt.ylabel("y (m)")
plt.title("does air resistance matter? (yes)")
plt.grid(True)
plt.show()
