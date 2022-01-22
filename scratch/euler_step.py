# pulling the integrator step out into its own tiny thing so i stop copy-pasting it
# into every file. didnt end up importing it everywhere but here it is.
import numpy as np

def euler_step(state, deriv, dt):
    return state + deriv(state)*dt

def rk4_step(state, deriv, dt):
    k1 = deriv(state)
    k2 = deriv(state + 0.5*dt*k1)
    k3 = deriv(state + 0.5*dt*k2)
    k4 = deriv(state + dt*k3)
    return state + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)

if __name__ == "__main__":
    # decay test: y' = -y, exact answer e^-t
    d = lambda s: -s
    y = np.array([1.0]); t = 0; dt = 0.1
    while t < 1.0:
        y = rk4_step(y, d, dt); t += dt
    print("rk4 at t=1:", y[0], " exact:", np.exp(-1))
