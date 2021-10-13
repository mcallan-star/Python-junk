# driven damped oscillator -- this one got orphaned in damped/ when i reorganized
# into oscillators/. i moved damped.py but never bothered to move this one. classic.
# anyway: push the oscillator with F0*cos(wd*t) and watch it lock onto the drive freq.
import numpy as np
import matplotlib.pyplot as plt

k=4.0; m=1.0; c=0.5
F0=1.0
wd=1.8   #drive frequency, try changing this toward sqrt(k/m)=2 for resonance

def deriv(s,t):
    x,v=s
    return np.array([v, (-(k)*x - c*v + F0*np.cos(wd*t))/m])

def rk4(s,t,dt):
    a=deriv(s,t)
    b=deriv(s+0.5*dt*a, t+0.5*dt)
    cc=deriv(s+0.5*dt*b, t+0.5*dt)
    d=deriv(s+dt*cc, t+dt)
    return s+(dt/6)*(a+2*b+2*cc+d)

dt=0.02; n=2000
s=np.array([0.0,0.0])
X=[]; T=[]
for i in range(n):
    t=i*dt
    X.append(s[0]); T.append(t)
    s=rk4(s,t,dt)

plt.plot(T,X)
plt.title("driven, it settles into the drive frequency after a transient")
plt.xlabel("t"); plt.grid(True)
plt.show()
