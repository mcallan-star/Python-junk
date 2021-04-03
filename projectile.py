# my first real physics sim!! a ball thrown off a cliff
# just newton, no air. doing the time stepping by hand so i actually get it

import numpy as np
import matplotlib.pyplot as plt

g = 9.8        #gravity, hardcoded cause why not
v0 = 20.0      #launch speed m/s
angle = 50     #degrees
dt = 0.01      #time step

# turn the angle into x and y speed
vx = v0 * np.cos(angle * np.pi/180)   #have to convert to radians, np.cos wants radians
vy = v0 * np.sin(angle * np.pi/180)

# i dont know how many steps i need ahead of time so just stop when it hits the ground
xs = [0.0]
ys = [0.0]
x, y = 0.0, 0.0

# euler method (i think). update velocity then position every little dt
# the bug before was my loop stopped one step early and left a fake (0,0) at the end.
# now i just keep going until y goes negative, then keep that last point so the curve
# actually reaches the ground
while y >= 0 or len(ys) < 2:
    vy = vy - g*dt             #gravity only pulls down
    x = x + vx*dt
    y = y + vy*dt
    xs.append(x)
    ys.append(y)

plt.plot(xs, ys)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("projectile, no air")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
plt.show()
