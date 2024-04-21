"""Time-independent Schrodinger equation, infinite square well, by brute force.

I discretize x on a grid and write the Hamiltonian as a matrix:

    H = -(hbar^2 / 2m) d^2/dx^2 + V(x)

The second derivative becomes the tridiagonal (1, -2, 1)/dx^2 stencil, V(x) goes on
the diagonal, and then I just hand the whole matrix to an eigensolver. The eigenvalues
ARE the allowed energies and the eigenvectors ARE the standing-wave states. For the
infinite well the answer is known -- E_n proportional to n^2 -- so it's a great check.
"""
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

hbar = 1.0; m = 1.0
N = 600
L = 1.0
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# kinetic energy: -(hbar^2/2m) * second-derivative stencil
main = np.full(N, -2.0)
off = np.full(N-1, 1.0)
T = -(hbar**2/(2*m)) * (np.diag(main) + np.diag(off, 1) + np.diag(off, -1)) / dx**2

V = np.zeros(N)            # zero inside, walls enforced by the grid ends being fixed
H = T + np.diag(V)

# fixed (Dirichlet) walls: drop the boundary points so psi=0 there
E, psi = la.eigh(H[1:-1, 1:-1])

# analytic: E_n = n^2 pi^2 hbar^2 / (2 m L^2)
print("n |   numeric E   |  analytic E")
for n in range(1, 6):
    En = n**2 * np.pi**2 * hbar**2 / (2*m*L**2)
    print(f"{n} | {E[n-1]:12.4f} | {En:10.4f}")

plt.figure(figsize=(8,6))
xx = x[1:-1]
for n in range(4):
    wf = psi[:, n]
    wf = wf/np.sqrt(np.sum(wf**2)*dx)       #normalize
    plt.plot(xx, wf + E[n], lw=1.5)         #offset each state up to its energy
    plt.axhline(E[n], color="0.8", lw=0.6)
plt.xlabel("x"); plt.ylabel("energy + wavefunction")
plt.title("infinite square well: first 4 eigenstates (numeric)")
plt.savefig("media/well_eigenstates.png", dpi=110)
plt.show()
