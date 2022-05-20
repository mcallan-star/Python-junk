# quick sanity check before i trust np.fft. one pure 10 Hz sine, does the peak land
# exactly on the 10 Hz bin? (yes). just making sure i understand rfftfreq.
import numpy as np
fs = 200; t = np.arange(0, 1, 1/fs)
x = np.sin(2*np.pi*10*t)
f = np.fft.rfftfreq(len(t), 1/fs)
P = np.abs(np.fft.rfft(x))
print("peak frequency bin:", f[np.argmax(P)], "Hz  (should be 10)")
