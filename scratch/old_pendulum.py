# this is my FIRST pendulum attempt before pendulum.py
# its worse, i was updating theta with the new w by accident and also degrees/radians
# confusion everywhere. keeping it so i remember how i used to do it
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
L = 1
dt = 0.01
theta = 0.5
w = 0
ths = []
for step in range(1000):
    w = w + (-g/L*np.sin(theta))*dt
    theta = theta + w*dt    #oops i think using the brand new w here is a different method
    ths.append(theta)

plt.plot(ths)
plt.title("old pendulum, looks ok actually?")
plt.show()
