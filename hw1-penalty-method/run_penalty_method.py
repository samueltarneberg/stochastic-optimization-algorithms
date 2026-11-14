import math
import numpy as np 

# ==============================
# run_gradient_descent function:
# ==============================
def run_gradient_descent(x_start, mu, eta, gradient_tolerance):
  iterations = 0
  x = [x_start]
  gradient = [compute_gradient(x[iterations],mu)]
  while (np.sqrt(gradient[iterations][0]**2 + gradient[iterations][1]**2) >= gradient_tolerance):    
    x_next1 = x[iterations][0] - eta*gradient[iterations][0]
    x_next2 = x[iterations][1] - eta*gradient[iterations][1]
    x.append([x_next1,x_next2])
    iterations += 1
    gradient_next = compute_gradient(x[iterations],mu)
    gradient.append(gradient_next)
  return x[-1]


# ==============================
# compute_gradient function:
# ==============================
def compute_gradient(x, mu):
  x1, x2 = x
  if (x[0]**2 + x[1]**2 - 1) <= 0:
    grad_f = [2*(x1-1), 4*(x2-2)]
    return grad_f
  else:
    grad_f = [2*(x1-1) + mu*4*x1*(x1**2 + x2**2 - 1), 4*(x2-2) + mu*4*x2*(x1**2 + x2**2 - 1)]
    return grad_f


# ==============================
# Main program:
# ==============================
mu_values = [1, 10, 100, 1000, 1100, 1200]
eta = 0.0001
x_start = [1, 2] 
gradient_tolerance = 0.0000001

for mu in mu_values:
   x = run_gradient_descent(x_start, mu, eta, gradient_tolerance)
   output = f"x = ({x[0]:.4f}, {x[1]:.4f}), mu = {mu:.1f}"
   print(output)


