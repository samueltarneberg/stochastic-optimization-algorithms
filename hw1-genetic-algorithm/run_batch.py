import math
from genetic_algorithm import run_function_optimization
import matplotlib.pyplot as plt

number_of_runs = 100                # Do NOT change
population_size = 100               # Do NOT change
maximum_variable_value = 5          # Do NOT change: (x_i in [-a,a], where a = maximumVariableValue)
number_of_genes = 50                # Do NOT change
number_of_variables = 2  	         # Do NOT change
tournament_size = 2                 # Do NOT change
tournament_probability = 0.75       # Do NOT change
crossover_probability = 0.8         # Do NOT change
number_of_generations = 2000        # Do NOT change


mutation_probability_list = [0.000, 0.005, 0.010, 0.020, 0.050, 0.100] # Add more values in this list; see the problem sheet


def median(list):
    list_length = len(list)
    sorted_list = sorted(list)
    return (sorted_list[list_length//2-1]/2.0+sorted_list[list_length//2]/2.0, sorted_list[list_length//2])[list_length % 2] if list_length else None

median_fitness_value = []
for mutation_probability in mutation_probability_list:
   fitness_val = []
   print("=====================================")
   print(f"mutation probability: {mutation_probability:.3f}")
   print("=====================================")
   for run_index in range(number_of_runs):
      [maximum_fitness, x_best] = run_function_optimization(population_size, number_of_genes, number_of_variables, maximum_variable_value, tournament_size, \
                                       tournament_probability, crossover_probability, mutation_probability, number_of_generations);
      output = f"Run index: {run_index}, fitness: {maximum_fitness:.4f}, x = ({x_best[0]:.8f},{x_best[1]:.8f})"
      print(output)
      fitness_val.append(maximum_fitness)
   median_fitness_value.append(median(fitness_val))
      
print(median_fitness_value)

fig, ax = plt.subplots()
ax.plot(mutation_probability_list,median_fitness_value)
ax.set_xlabel(r"Mutation probability $p_{\mathrm{mut}}$")
plt.ylabel("Median fitness")
plt.title("Median fitness vs mutation probability")  
plt.show()           



