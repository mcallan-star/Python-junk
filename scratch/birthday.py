# probability detour, the birthday paradox by monte carlo. in a room of 23 people
# theres already a >50% chance two share a birthday, which feels impossible. so i just
# SIMULATED it a bunch of times instead of trusting the formula. (it checks out.)
import numpy as np

rng = np.random.default_rng(0)
def has_match(n_people, trials=20000):
    hits = 0
    for _ in range(trials):
        bdays = rng.integers(0, 365, n_people)
        if len(np.unique(bdays)) < n_people:    #some collision happened
            hits += 1
    return hits/trials

for n in [10, 23, 30, 50]:
    print(f"{n} people: P(shared birthday) ~= {has_match(n):.3f}")
# 23 should land around 0.51. wild.
