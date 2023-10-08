# python-junk

a few years of teaching myself to simulate physics in python. started with a projectile that just falls. the hard part was never the physics, it was the *numbers* -- how you step things forward in time without the whole sim blowing up.

still junk. there's a `scratch/` drawer i never clean, two double-slit files (one wrong), and a `damped/` folder i abandoned mid-reorganize. leaving all of it.

## the gallery (i learned to make gifs!!)

FuncAnimation changed everything, static plots feel dead now.

<table>
<tr>
  <td align="center"><img src="media/nbody.gif" width="260"><br><b>n-body gravity</b><br>softened, vectorized, my favorite</td>
  <td align="center"><img src="media/heat2d.gif" width="260"><br><b>2d heat diffusion</b><br>two hot spots bleeding out</td>
</tr>
<tr>
  <td align="center"><img src="media/solar_system.gif" width="260"><br><b>toy solar system</b><br>inner planets, kepler shows up on its own</td>
  <td align="center"><img src="media/pendulum_phase.gif" width="260"><br><b>pendulum phase space</b><br>riding one of the orbits</td>
</tr>
<tr>
  <td align="center"><img src="media/random_walk.gif" width="260"><br><b>2d random walk</b><br>a drunk man's journey</td>
  <td align="center"><img src="media/lorenz.gif" width="260"><br><b>lorenz attractor</b><br>chaos, the butterfly</td>
</tr>
</table>

## what's in here
- **mechanics** -- projectile, two-body + n-body gravity, toy solar system, the three-body problem (chaotic, no two runs alike), kepler's third law checked
- **oscillators** -- spring, pendulum, damped/driven, resonance, phase space
- **numerical methods** -- euler vs rk4, bisection, newton, integration
- **randomness** -- random walks, monte carlo pi
- **waves + fourier** -- interference, double slit, FFT, gaussian beams, fresnel/brewster
- **pde** -- 1d + 2d heat equation, 1d wave (FDTD), poisson (relaxation). learned the hard way that explicit methods have a speed limit (`pde/stability_note.md`)

## the running lesson
euler will betray you. always check if energy is conserved. and CFL is not a suggestion.

## next
quantum. i want to watch a wavepacket move.
