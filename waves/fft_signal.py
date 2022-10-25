# now that i get the DFT (see the notebook), use numpys FFT for real: take a messy
# signal thats a few sine waves buried in noise, and recover the frequencies. the
# FFT basically asks "how much of each frequency is in here" and the peaks pop right
# out even though you cant see them in the raw wiggle.

import numpy as np
import matplotlib.pyplot as plt

fs = 500.0               #sample rate, samples per second
T = 2.0                  #seconds
t = np.arange(0, T, 1/fs)

# three tones + noise
signal = (1.0*np.sin(2*np.pi*7*t)      # 7 Hz
        + 0.5*np.sin(2*np.pi*23*t)     # 23 Hz
        + 0.8*np.sin(2*np.pi*61*t))    # 61 Hz
signal += 0.6*np.random.randn(len(t))  #white noise to hide them

spectrum = np.fft.rfft(signal)
freqs = np.fft.rfftfreq(len(t), 1/fs)
power = np.abs(spectrum)

fig, ax = plt.subplots(2, 1, figsize=(9,6))
ax[0].plot(t, signal, lw=0.6)
ax[0].set_title("raw signal -- good luck seeing the tones in here")
ax[0].set_xlabel("t (s)")
ax[1].plot(freqs, power, color="tab:red")
ax[1].set_xlim(0, 100)
ax[1].set_title("FFT -- there they are: 7, 23, 61 Hz")
ax[1].set_xlabel("frequency (Hz)")
fig.tight_layout()
fig.savefig("media/fft_signal.png", dpi=110)
plt.show()
