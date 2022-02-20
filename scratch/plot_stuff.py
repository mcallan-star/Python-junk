# just fighting with matplotlib styling, dont mind me
# trying to figure out colormaps and how to make plots not look default-ugly
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
plt.style.use("default")
for i, cmap in enumerate(["viridis", "plasma", "magma"]):
    plt.plot(x, np.sin(x + i), label=cmap)
plt.legend()
plt.title("which colors do i like")
plt.show()
# note to self: viridis is the nice perceptual one everybody uses
