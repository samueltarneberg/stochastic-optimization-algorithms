# Newton–Raphson

Finds a stationary point of a polynomial with the Newton–Raphson update `x ← x − f'(x) / f''(x)`. The polynomial and its derivatives are represented as coefficient lists. The iterations are plotted on top of the function.

The example in the script uses `f(x) = 10 − 2x − x² + x³` and starts at x = 2, with tolerance 10⁻⁵.

```bash
python newton_raphson.py
```
