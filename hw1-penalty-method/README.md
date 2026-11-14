# Penalty method

Minimises `f(x₁, x₂) = (x₁ − 1)² + 2(x₂ − 2)²` subject to `x₁² + x₂² ≤ 1`.

The constraint is replaced by the penalty term `μ (x₁² + x₂² − 1)²`, which applies only when the constraint is violated. The penalised function is then minimised with gradient descent (η = 10⁻⁴, stopping when |∇| < 10⁻⁷) for increasing μ = 1, 10, 100, 1000, 1100, 1200. As μ grows, the solution approaches the constrained optimum on the unit circle.

```bash
python run_penalty_method.py
```
