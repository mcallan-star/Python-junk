# picking colormaps for the animations. inferno/magma read well on black backgrounds,
# viridis for line plots. just eyeballing them side by side. junk file.
import numpy as np
import matplotlib.pyplot as plt

grad = np.linspace(0, 1, 256).reshape(1, -1)
maps = ["viridis", "inferno", "magma", "plasma", "cividis"]
fig, axes = plt.subplots(len(maps), 1, figsize=(6, 4))
for ax, m in zip(axes, maps):
    ax.imshow(grad, aspect="auto", cmap=m)
    ax.set_yticks([]); ax.set_xticks([]); ax.set_ylabel(m, rotation=0, ha="right", va="center")
plt.suptitle("which colormap")
plt.show()
