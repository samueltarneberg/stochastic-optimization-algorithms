import numpy as np
import matplotlib.pyplot as plt

def get_objective_function(x1,x2):
    term1 = (x1**2+x2-11)**2 
    term2 = (x1+x2**2-7)**2
    f = term1 + term2
    return f

def initialize_positions(number_of_particles,n_dimensions,x_min,x_max):
    initial_particle_position = []
    for _ in range(number_of_particles):
        particle_positions=[]
        for _ in range(n_dimensions):
            r = np.random.rand()
            position_value = x_min + r*(x_max - x_min)
            particle_positions.append(position_value)
        initial_particle_position.append(particle_positions)
    return np.array(initial_particle_position)

def initialize_velocities(number_of_particles,n_dimensions,alpha,delta_t,x_min,x_max,v_max):
    initial_velocities = []
    for _ in range(number_of_particles):
        particle_velocity=[]
        for _ in range(n_dimensions):
            r = np.random.rand()
            velocity_component = alpha/delta_t * (-(x_max-x_min)/2 + r*(x_max-x_min))
            particle_velocity.append(velocity_component)
    initial_velocities.append(particle_velocity)
    return np.clip(initial_velocities,-v_max,v_max)

def update_velocities(particle_positions, particle_velocities,
                       cognitive_coefficient, social_coefficient, 
                       particle_best, swarm_best,
                        delta_t, inertia_weight, v_max):
    q = np.random.rand(number_of_particles,1)
    r = np.random.rand(number_of_particles,1)

    swarm_best = [swarm_best for _ in range(len(particle_positions))]

    term1 = cognitive_coefficient*r*((particle_best-particle_positions) / delta_t)
    term2 = social_coefficient*q*((swarm_best-particle_positions) / delta_t)

    particle_velocities = inertia_weight*particle_velocities + term1 + term2
    return np.clip(particle_velocities,-v_max,v_max)

def update_positions(particle_positions,particle_velocities,delta_t):
    particle_positions += particle_velocities*delta_t
    return particle_positions

def plot_particles(plt, particle_positions, color):
  x = []
  y = []
  for particle_index in range(len(particle_positions)):
    x.append(particle_positions[particle_index][0])
    y.append(particle_positions[particle_index][1])
  plt.scatter(x,y,color=color)

def plot(particle_positions,swarm_best,number_of_contour_levels,x_min,x_max,pause):
    plt.cla()
    coordinate_values = np.linspace(x_min, x_max)
    X1, X2 = np.meshgrid(coordinate_values, coordinate_values)
    Z = get_objective_function(X1, X2)
    contour_levels = np.linspace(0.1,1000,number_of_contour_levels)
    plt.contour(X1,X2,Z,levels=contour_levels)
    plot_particles(plt,particle_positions,color='red')
    plt.scatter(swarm_best[0],swarm_best[1],color='blue',s=160,edgecolors='black',)
    plt.xlim(x_min, x_max)
    plt.ylim(x_min, x_max)
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.pause(pause)
    plt.show()

#############################################
# MAIN
############################################

number_of_particles = 40
n_dimensions = 2
x_min = -5
x_max = 5
delta_t = 1
cognitive_coefficient = 2
social_coefficient = 2
alpha = 1
inertia_weight = 1.4
beta = 0.99
v_max = 2

particle_positions = initialize_positions(number_of_particles,n_dimensions,x_min,x_max)
particle_velocities = initialize_velocities(number_of_particles, n_dimensions, alpha, delta_t, x_min, x_max, v_max)

swarm_best = particle_positions[0].copy()
particle_best = particle_positions.copy()
best_x = []
best_fitness = []

plt.ion()
fig, ax = plt.subplots(figsize=(6, 5))

for iteration in range(100):
    number_of_particles = len(particle_positions)
    function_values = []
    for particle, i in zip(particle_positions, range(number_of_particles)):
        objective_function = get_objective_function(particle[0],particle[1])
        function_values.append(objective_function)
        if objective_function < get_objective_function(particle_best[i][0],particle_best[i][1]):
            particle_best[i] = particle
        if objective_function < get_objective_function(swarm_best[0],swarm_best[1]):
            swarm_best[0] = particle[0]
            swarm_best[1] = particle[1]
    minimum_objective_value = min(function_values)
    best_fitness.append(minimum_objective_value)
    i = best_fitness.index(minimum_objective_value)
    best_x.append(swarm_best)
    if inertia_weight > 0.4:
        inertia_weight *= beta
    particle_velocities = update_velocities(particle_positions, particle_velocities,
                                    cognitive_coefficient, social_coefficient, particle_best ,swarm_best ,
                                    delta_t, inertia_weight, v_max) 
    particle_positions = update_positions(particle_positions,particle_velocities,delta_t) 
    plot(particle_positions,swarm_best,number_of_contour_levels=100,x_min=5,x_max=-5,pause=0.1)
    print(f"Iteration {iteration+1}/{100}, Best Position = {swarm_best},Best Fitness = {get_objective_function(swarm_best[0],swarm_best[1])}")
plt.ioff()
plt.show()
objective_function_smallest_value = min(best_fitness)
i = best_fitness.index(objective_function_smallest_value)
best_position = best_x[i]
print(f"Best overall position: {best_position}, and best overall fitness: {objective_function_smallest_value}")


