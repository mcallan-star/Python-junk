"""Time-DEPENDENT Schrodinger equation by the split-step Fourier method.

    i hbar dpsi/dt = [ -(hbar^2/2m) d^2/dx^2 + V(x) ] psi

The trick: the kinetic part is easy in FOURIER space (a derivative is just multiplying
by i k), and the potential part is easy in REAL space (just multiply by V). So each step
I split the evolution into three cheap pieces (Strang splitting):

    1. half a potential kick:   psi *= exp(-i V dt / 2hbar)        [real space]
    2. a full kinetic drift:    FFT -> psi *= exp(-i hbar k^2 dt / 2m) -> IFFT
    3. another half kick:       psi *= exp(-i V dt / 2hbar)        [real space]

This is the same idea I would later build a whole nonlinear (NLSE) fiber solver around
in fibertouch -- there you just add a |psi|^2 term to the potential step. So this little
free-particle demo is honestly where that started.

Run as a script: a free gaussian wavepacket spreading out (no potential) -> wavepacket.gif
"""
import numpy as np


def split_step_evolve(psi, x, V, dt, steps, m=1.0, hbar=1.0, record_every=1):
    """Evolve psi under V for `steps` steps of dt. Returns list of recorded frames."""
    dx = x[1] - x[0]
    N = len(x)
    k = 2*np.pi*np.fft.fftfreq(N, d=dx)        # spatial frequencies
    kin = np.exp(-1j*hbar*k**2*dt/(2*m))       # full kinetic propagator (Fourier space)
    pot_half = np.exp(-1j*V*dt/(2*hbar))       # half potential kick (real space)

    frames = []
    for s in range(steps):
        psi = pot_half*psi                     # 1. half kick
        psi = np.fft.ifft(kin*np.fft.fft(psi)) # 2. drift
        psi = pot_half*psi                     # 3. half kick
        if s % record_every == 0:
            frames.append(psi.copy())
    return frames


def gaussian_packet(x, x0, k0, sigma):
    """A normalized gaussian wavepacket centered at x0 moving with momentum k0."""
    psi = np.exp(-(x-x0)**2/(2*sigma**2)) * np.exp(1j*k0*x)
    dx = x[1]-x[0]
    psi /= np.sqrt(np.sum(np.abs(psi)**2)*dx)
    return psi


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation, PillowWriter

    N = 1024
    x = np.linspace(-50, 50, N)
    V = np.zeros(N)                            # free particle, no potential
    psi0 = gaussian_packet(x, x0=-15, k0=2.0, sigma=2.0)

    frames = split_step_evolve(psi0, x, V, dt=0.02, steps=2000, record_every=10)

    fig, ax = plt.subplots(figsize=(9,4.5))
    ax.set_xlim(-50, 50); ax.set_ylim(0, 0.6)
    ax.set_xlabel("x"); ax.set_title("free wavepacket spreading (split-step)")
    prob, = ax.plot([], [], color="tab:blue")
    ax.fill_between(x, 0, 0, alpha=0.2)

    def update(i):
        prob.set_data(x, np.abs(frames[i])**2)
        return [prob]

    anim = FuncAnimation(fig, update, frames=len(frames), blit=True, interval=30)
    anim.save("media/wavepacket.gif", writer=PillowWriter(fps=30))
    plt.show()
