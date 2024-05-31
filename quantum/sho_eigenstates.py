"""Quantum harmonic oscillator eigenstates, same finite-difference + diagonalize trick.

Potential is V(x) = 1/2 m w^2 x^2 (a parabola). The famous result is that the energy
levels are perfectly evenly spaced:

    E_n = (n + 1/2) hbar w

so the spacing is always hbar*w. My grid solver should reproduce that ladder, and it
does -- the first few come out at 0.5, 1.5, 2.5, ... in units of hbar*w. Plotting each
eigenstate sitting at its own energy on top of the parabola gives the classic textbook
picture.
"""
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

hbar = 1.0; m = 1.0; w = 1.0
N = 800
x = np.linspace(-8, 8, N)
dx = x[1]-x[0]

V = 0.5*m*w**2*x**2
main = np.full(N, -2.0); off = np.full(N-1, 1.0)
T = -(hbar**2/(2*m))*(np.diag(main)+np.diag(off,1)+np.diag(off,-1))/dx**2
H = T + np.diag(V)

E, psi = la.eigh(H)

print("n | numeric E_n | (n+1/2)hbar w")
for n in range(6):
    print(f"{n} |   {E[n]:.4f}    |     {(n+0.5):.4f}")

plt.figure(figsize=(8,6))
plt.plot(x, V, "k", lw=1, alpha=0.6)
for n in range(5):
    wf = psi[:, n]
    wf = wf/np.sqrt(np.sum(wf**2)*dx)
    plt.plot(x, 1.4*wf + E[n])              #scale + lift to its level
    plt.axhline(E[n], color="0.85", lw=0.6)
plt.ylim(-0.3, 6)
plt.xlabel("x"); plt.ylabel("energy")
plt.title("harmonic oscillator: evenly spaced ladder, E_n=(n+1/2)")
plt.savefig("media/sho_eigenstates.png", dpi=110)
plt.show()
