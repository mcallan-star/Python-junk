# building a square wave out of sine waves, the classic fourier picture. a square wave
# is just odd harmonics (1, 3, 5, ...) with amplitude 1/n. add more terms = sharper
# corners (and the little overshoot at the edges that never goes away is the Gibbs
# phenomenon). this is the intuition that made the DFT finally click for me.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
plt.figure(figsize=(9,5))
for n_terms in [1, 3, 9, 49]:
    y = np.zeros_like(x)
    for n in range(1, n_terms+1, 2):     #odd harmonics only
        y += (4/(np.pi*n))*np.sin(n*x)
    plt.plot(x, y, label=f"{(n_terms+1)//2} terms")
plt.legend(); plt.grid(True)
plt.title("square wave from sines (watch the Gibbs overshoot at the jumps)")
plt.show()
