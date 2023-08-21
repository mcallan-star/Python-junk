# notes to self

stuff i keep forgetting and have to look up, so future me stops googling the same five things every week (present me does this a lot).

## exporting gifs from a jupyter notebook
this took me embarrassingly long to get right so here it is for next time.

the recipe that actually works (no imagemagick needed, pillow ships with matplotlib's writer):

```python
from matplotlib.animation import FuncAnimation, PillowWriter

fig, ax = plt.subplots()
def update(frame):
    ...                      # redraw whatever changes this frame
    return artists           # (only matters if blit=True)

anim = FuncAnimation(fig, update, frames=200, blit=True, interval=40)
anim.save("media/thing.gif", writer=PillowWriter(fps=25))
```

gotchas i actually hit:
- **"no display" / backend errors when running headless:** force the Agg backend before you plot -> `import matplotlib; matplotlib.use("Agg")`, or run the whole thing with the env var `MPLBACKEND=Agg`.
- **the gif lands in the wrong folder:** when you run a notebook with
`jupyter nbconvert --execute`, the kernel's working directory is the NOTEBOOK's folder, not the repo root, so `media/` gets created right next to the notebook. fix: run from the repo root, or drive it with `nbclient` and pass `resources={"metadata": {"path": REPO_ROOT}}` so the kernel cwd is the root.
- **gif is gigantic (>5 MB):** lower the fps, cut the frame count, or shrink figsize. a full-color `imshow` animation with 120+ frames balloons fast.
- **blit=True** is faster but doesn't redraw the axes/title each frame. turn it OFF for 3d plots or anything where the whole frame redraws.
- want an mp4 instead? `writer="ffmpeg"` and save as `.mp4` (needs ffmpeg installed).
- to preview inline in the notebook instead of saving a file:
`from IPython.display import HTML; HTML(anim.to_jshtml())`

## interactive sliders (ipywidgets)
- wrap any function in a quick slider UI:
  ```python
  from ipywidgets import interact, FloatSlider
  interact(my_plot, amp=FloatSlider(min=0, max=2, step=0.1, value=1))
  ```
- if the widgets don't render, the package isn't installed in that kernel ->
`pip install ipywidgets`, then restart the kernel.

## git i always forget
- see what's changed:             `git status` / `git diff`
- undo last commit, keep work:   `git reset --soft HEAD~1`
- fix the last commit message:   `git commit --amend`
- throw away changes to a file:  `git checkout -- file.py`
- stash it for later:            `git stash`  then  `git stash pop`
- whoops wrong branch:           `git switch main`

## docs i keep open
- numpy: https://numpy.org/doc/stable/
- matplotlib: https://matplotlib.org/stable/  (the gallery is gold for stealing plots)
- matplotlib animation api: https://matplotlib.org/stable/api/animation_api.html
- scipy: https://docs.scipy.org/doc/scipy/
- ipywidgets: https://ipywidgets.readthedocs.io/
- python itself: https://docs.python.org/3/
- stack overflow, obviously

## stuff i learned the hard way
- put `np.random.seed(0)` at the top or your plots change every single run
- euler integration quietly leaks energy. use rk4 or leapfrog for anything orbiting
- explicit heat/wave sims blow up if dt is too big -- that's the CFL/stability limit, pick the stability number first and let dt fall out of it
- check conservation (energy / momentum) as a sanity test, it catches so many bugs
- `plt.show()` blocks the script. use `plt.savefig()` if you just want the picture
