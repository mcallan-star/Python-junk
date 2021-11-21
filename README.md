# python-junk

teaching myself to simulate physics. started with a projectile that just falls, slowly figuring out that the hard part isn't the physics its the *numbers* -- how you step time forward without the whole thing falling apart.

its called junk for a reason. there's a scratch/ folder that's pure chaos.

## stuff so far
- **projectile motion** -- threw a ball, did euler by hand. works.
- **oscillators** -- spring, pendulum (small angle vs the real nonlinear one, they split apart for big swings). my euler kept *gaining* energy which freaked me out
- **euler vs rk4** -- turns out euler is bad and rk4 is the fix. energy stays flat now
- **root finding + integration** -- bisection, newtons method, trapezoid/simpson, all rolled by hand so i actually understand them

## next
random walks, monte carlo, and waves once i wrap my head around fourier
