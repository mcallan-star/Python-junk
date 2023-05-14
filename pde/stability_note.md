# why my heat sim exploded (a note to myself)

spent a whole afternoon on this so i'm writing it down.

i had the 1d heat equation working, then i bumped up `dt` to make it run faster and suddenly everything turned into `nan` and the plot looked like static. i thought i broke the code. i did not break the code. the code was fine. the *method* has a speed limit.

## the rule

for explicit finite-difference heat (u_t = alpha u_xx) the thing that matters is

```
r = alpha * dt / dx^2
```

- **1d:** need `r <= 0.5`
- **2d:** need `r <= 0.25` (more neighbors, tighter limit)

if you go over that, tiny rounding errors get AMPLIFIED every step instead of damped, and they double and double until the numbers overflow. that's it. its not random, its the stability condition.

## the fix

don't just crank `dt`. pick `r` safely (i use 0.4 in 1d, 0.2 in 2d) and let `dt = r*dx^2/alpha` fall out of it. if you want more speed, either accept it, or learn an *implicit* method (Crank-Nicolson) that doesn't have this limit. (todo someday.)

## the same idea shows up everywhere

the wave equation has its own version of this called the **CFL condition** (Courant number `C = c*dt/dx <= 1`). basically: in one time step, information can't be allowed to jump more than one grid cell. once i understood that, half my "bugs" stopped being bugs.
