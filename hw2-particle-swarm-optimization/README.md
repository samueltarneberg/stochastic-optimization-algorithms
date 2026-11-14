# Particle swarm optimization

Minimises Himmelblau's function, `f(x₁, x₂) = (x₁² + x₂ − 11)² + (x₁ + x₂² − 7)²`, on [−5, 5]². The function has four global minima, all with f = 0.

- 40 particles; cognitive and social coefficients c₁ = c₂ = 2
- Inertia weight starts at 1.4 and decays by a factor 0.99 per iteration down to 0.4, moving the swarm from exploration to exploitation
- Velocities are clamped to |v| ≤ 2
- The swarm is animated over a contour plot for 100 iterations

```bash
python run_pso.py
```

Different runs converge to different minima depending on the random initialisation.
