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

steps = 500
x = np.zeros(steps)
y = np.zeros(steps)

# euler method (i think). update velocity then position every little dt
for i in range(steps-1):       #stop one early so i dont go out of bounds
    vy = vy - g*dt             #gravity only pulls down
    x[i+1] = x[i] + vx*dt
    y[i+1] = y[i] + vy*dt

plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("projectile, no air")
plt.grid(True)
plt.axhline(0, color="black", linewidth=0.5)
# why does it keep going below zero forever lol. and the very last point dips weird
plt.show()
