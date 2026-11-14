import math
import matplotlib.pyplot as plt 


# ============================================
# get_polynomial_value:
# ============================================
def get_polynomial_value(x, polynomial_coefficients):
    polynomial_sum = 0
    power = 0
    for coefficient in polynomial_coefficients:
        polynomial_sum += coefficient * x ** power
        power += 1
    return polynomial_sum


# ============================================
# differentiate_polynomial:
# ============================================
def differentiate_polynomial(polynomial_coefficients, derivative_order):
    derived_coefficients = []
    for power in range(derivative_order,len(polynomial_coefficients)):
        factor = power
        derivative_coefficient = polynomial_coefficients[power]
        while factor > (power - derivative_order):
                derivative_coefficient *= factor
                factor -=1
        derived_coefficients.append(derivative_coefficient)
    return derived_coefficients
        

# ============================================
# step_newton_raphson:
# ============================================
def step_newton_raphson(x, f_prime, f_double_prime):
    x_next = x - (f_prime/f_double_prime)
    return x_next


# ============================================
# run_newton-raphson:
# ============================================
def run_newton_raphson(polynomial_coefficients, starting_point, tolerance, maximum_number_of_iterations):
    x_values = [starting_point]
    function_values = [get_polynomial_value(starting_point,polynomial_coefficients)]
    iteration = 0
    iteration_index = 1
    first_derivative_coefficients = differentiate_polynomial(polynomial_coefficients,1)
    second_derivative_coeffients = differentiate_polynomial(polynomial_coefficients,2)
    while iteration <= maximum_number_of_iterations:
        f_prime = get_polynomial_value(x_values[iteration], first_derivative_coefficients)
        f_double_prime = get_polynomial_value(x_values[iteration], second_derivative_coeffients)        
        if len(polynomial_coefficients) <= 2:
            print("Polynomial degree (len(polynomial_coefficients)) is less than or equal to 2.\n"
                  "Newton-Raphson step cannot be calculated because division with zero is not possible.")
            quit()
        elif f_double_prime == 0 :
            print("Second derivative (f_double_prime) is zero.\n "
                  "Newton-Raphson step cannot be calculated because division with zero is not possible.")
            quit() 
        else:                   
            x_next = step_newton_raphson(x_values[iteration], f_prime, f_double_prime)
            function_value = get_polynomial_value(x_next,polynomial_coefficients)        
            x_values.append(x_next)
            function_values.append(function_value)
            iteration += 1
            if abs(x_values[iteration_index]-x_values[iteration_index-1]) < tolerance:
                break
            else:
                iteration_index += 1
    return [x_values,function_values]


# ============================================
# plot_iterations:
# ============================================
def plot_iterations(polynomial_coefficients,iterations):
    x_values = []
    function_values = []   
    plot_start = iterations[0][0] - 2
    plot_end = iterations[0][0] + 2
    x = plot_start
    for i in range(0,100):
        x_values.append(x)
        function_values.append(get_polynomial_value(x,polynomial_coefficients))
        x_step = (plot_end-plot_start)/100
        x = x + x_step
       
    fig, ax = plt.subplots()
    ax.plot(x_values,function_values)             # Plot curve
    ax.plot(iterations[0],iterations[1],'o')      # Plot Newton-Raphson steps
    plt.show()                           


# ============================================
# Main loop
# ============================================
tolerance = 0.00001
maximum_number_of_iterations = 10

polynomial_coefficients = [10,-2,-1,1]
starting_point = 2

iterations = run_newton_raphson(polynomial_coefficients, starting_point, tolerance, maximum_number_of_iterations)
plot_iterations(polynomial_coefficients, iterations)