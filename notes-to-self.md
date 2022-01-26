# notes to self

stuff i keep forgetting and have to look up, so future me stops googling the same five things every week (present me does this a lot).

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
- scipy: https://docs.scipy.org/doc/scipy/
- python itself: https://docs.python.org/3/
- stack overflow, obviously

## stuff i learned the hard way
- put `np.random.seed(0)` at the top or your plots change every single run
- euler integration quietly leaks energy. use rk4 or leapfrog for anything orbiting
- check conservation (energy / momentum) as a sanity test, it catches so many bugs
- `plt.show()` blocks the script. use `plt.savefig()` if you just want the picture
