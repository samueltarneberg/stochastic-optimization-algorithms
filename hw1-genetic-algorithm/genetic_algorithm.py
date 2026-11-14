import random
import math

# Initialize population:

def initialize_population(population_size, number_of_genes):
    population = [[random.randint(0,1) for gene_index in range(number_of_genes)] for chromosome_index in range(population_size)]
    return population


# Decode chromosome:

def decode_chromosome(chromosome, number_of_variables, maximum_variable_value):
    gene_length = int(len(chromosome)/number_of_variables)
    decoded_values = []
    for i in range(0,number_of_variables):
        bit_position = 1
        weighted_bit_sum = 0
        bits_to_decode = chromosome[i * gene_length : (i + 1) * gene_length]
        for bit in bits_to_decode:
            weighted_bit_sum += (2**(-bit_position)*bit)
            bit_position += 1          
        x = - maximum_variable_value + (2* maximum_variable_value)/(1-2**(-gene_length))*weighted_bit_sum
        decoded_values.append(x)
    return decoded_values

# Get fitness value
def evaluate_individual(x):
    x1, x2 = x

    term1 = (1.5 - x1 + x1*x2)**2
    term2 = (2.25 - x1 + x1*x2**2)**2
    term3 = (2.625 - x1 + x1*x2**3)**2

    g = term1 + term2 + term3
    g_fitness = (g + 1)**(-1)
    return g_fitness


# Select individuals:
def tournament_select(fitness_list, tournament_probability, tournament_size):
    population_size = len(fitness_list)
    r = random.random()

    list_of_random_indices = [random.randint(0,population_size-1) for int in range(tournament_size)]

    tournament_individuals = [fitness_list[index] for index in list_of_random_indices]

    if r < tournament_probability:
        max_fitness = max(tournament_individuals)
        index_of_max = tournament_individuals.index(max_fitness)
        i_selected = list_of_random_indices[index_of_max]
    else:
        min_fitness = min(tournament_individuals)
        index_of_min = tournament_individuals.index(min_fitness)
        i_selected = list_of_random_indices[index_of_min]
    return i_selected

# Perform crossover
def cross(chromosome1, chromosome2):
    number_of_genes = len(chromosome1)
    cross_point = random.randint(1, number_of_genes-1)
    new_chromosome_1 = chromosome1[:cross_point] + chromosome2[cross_point:]
    new_chromosome_2 = chromosome2[:cross_point] + chromosome1[cross_point:]
    return [new_chromosome_1, new_chromosome_2]


# Mutate individuals:
def mutate(chromosome, mutation_probability):
    number_of_genes = len(chromosome)
    mutated_chromosome = chromosome.copy()
    for gene_index in range(number_of_genes):
        r = random.random()
        if (r < mutation_probability):
            mutated_chromosome[gene_index] = 1-chromosome[gene_index]        
    return mutated_chromosome


#Genetic algorithm
def run_function_optimization(population_size, number_of_genes, number_of_variables, maximum_variable_value, \
                              tournament_size, tournament_probability, crossover_probability,\
                              mutation_probability, number_of_generations):

    population = initialize_population(population_size,number_of_genes)

    for generation_index in range(number_of_generations):
        maximum_fitness = 0
        best_chromosome = []
        best_individual = []
        fitness_list = []
        for chromosome in population:
            individual = decode_chromosome(chromosome,number_of_variables,maximum_variable_value)
            fitness = evaluate_individual(individual)
            if (fitness > maximum_fitness):
                maximum_fitness = fitness
                best_chromosome = chromosome.copy()  
                best_individual = individual.copy()
            fitness_list.append(fitness)

        temp_population = []
        for i in range(0,population_size,2):
            index_1 = tournament_select(fitness_list, tournament_probability, tournament_size)
            index_2 = tournament_select(fitness_list, tournament_probability, tournament_size)
            chromosome1 = population[index_1].copy()
            chromosome2 = population[index_2].copy()
            r = random.random()
            if r < crossover_probability:
                [new_chromosome_1, new_chromosome_2] = cross(chromosome1,chromosome2)
                temp_population.append(new_chromosome_1)
                temp_population.append(new_chromosome_2) 
            else:
                temp_population.append(chromosome1)
                temp_population.append(chromosome2)

        for i in range(population_size):
            original_chromosome = temp_population[i]

            mutated_chromosome = mutate(original_chromosome, mutation_probability)
            temp_population[i] = mutated_chromosome

        temp_population[0] = best_chromosome
        population = temp_population.copy()

    return [maximum_fitness, best_individual]
 

