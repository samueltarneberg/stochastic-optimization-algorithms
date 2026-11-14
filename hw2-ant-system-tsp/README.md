# Ant System for the travelling salesman problem

Solves a 50-city TSP with the Ant System (AS), the original ant colony optimization algorithm.

- Each ant builds a tour, choosing the next city with probability ∝ τᵢⱼ^α · ηᵢⱼ^β, where η = 1/distance.
- After each iteration, pheromones evaporate (rate ρ), and every ant deposits 1/L on the edges of its tour.
- Parameters: 50 ants, α = 1, β = 5, ρ = 0.5, τ₀ = 0.1.
- The best tour is plotted live as it improves. The run stops once a tour shorter than 100 is found, and that tour is saved to `best_result_found.py`.

| File | Purpose |
|---|---|
| `run_ant_system.py` | The algorithm and live plot |
| `city_data.py` | City coordinates |
| `best_result_found.py` | Best tour found (list of city indices) |

```bash
python run_ant_system.py
```
