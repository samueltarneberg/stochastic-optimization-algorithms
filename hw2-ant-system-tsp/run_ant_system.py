###########################
#
# Ant System (AS) for TSP
#
###########################

import math
import numpy as np
import matplotlib.pyplot as plt
import os
from city_data import city_locations


def save_best_path(path, filename="best_result_found.py"):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path =  os.path.join(script_directory,filename)
    with open(file_path, "w") as file:
        file.write(f"best_path = {path}\n")

def initialize_pheromone_levels(number_of_cities, tau_0):
    initialize_pheromones = [[tau_0 for i in range(number_of_cities)] for j in range(number_of_cities)]
    return initialize_pheromones

def get_visibility(city_locations):
   visibility_matrix = []
   for city_i in city_locations:
      row = []
      for city_j in city_locations:
          x1_ij = (city_i[0] - city_j[0])
          x2_ij = (city_i[1] - city_j[1])
          distance = np.sqrt((x1_ij)**2 + (x2_ij)**2)
          if distance == 0:
              visibility_value = 0
          else:
            visibility_value = float(1 / distance)
          row.append(visibility_value)
      visibility_matrix.append(row)
   return visibility_matrix

def generate_path(pheromone_levels, visibility, alpha, beta):

    number_of_cities = len(pheromone_levels)
    random_start_city = np.random.randint(0,number_of_cities)
    visited_cities = [random_start_city]
    if len(visited_cities) < number_of_cities:
      while len(visited_cities) < number_of_cities:
        nominators = []
        current_city = visited_cities[-1]
        list_of_possible_cities = [i for i in range(number_of_cities) if i not in visited_cities]
        for index in list_of_possible_cities:
            if len(list_of_possible_cities) > 1:
              pheromone_level = pheromone_levels[current_city][index] 
              visibility_value = visibility[current_city][index]
              nominator = pheromone_level**alpha * visibility_value**beta
              nominators.append(nominator)
            else:
              nominators.append(1)
        
        denominator = sum(nominators)
        if denominator == 0:
          probabilities = [1/len(nominators) for i in range(len(nominators))]
        else:
          probabilities = [(tau_eta/denominator) for tau_eta in nominators]

        next_city = np.random.choice(list_of_possible_cities,p=probabilities)
        visited_cities.append(int(next_city))

    return visited_cities
       
def get_path_length(path, city_locations):
    path_length = 0
    i = len(path)-1
    while i >= 0:
        current_city = city_locations[path[i]]
        next_city = city_locations[path[i-1]]
        x1_ij = (current_city[0] - next_city[0])
        x2_ij = (current_city[1] - next_city[1])
        d_ij = np.sqrt((x1_ij)**2 + (x2_ij)**2)
        path_length += d_ij
        i -= 1
    return path_length        

def compute_delta_pheromone_levels(path_collection, path_length_collection):
   n = len(path_collection[0])
   delta_tau = np.zeros((n,n))
   for length,path in zip(path_length_collection,path_collection):
        for i in range(0,len(path)):
          delta_tau[path[i]][path[(i+1) % len(path)]] += 1/length
   return delta_tau
    
def update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho):
    pheromone_levels = (1-rho)*np.array(pheromone_levels) + delta_pheromone_levels
    return pheromone_levels

def plot_cities(plt, city_locations):
  x = []
  y = []
  for city_index in range(len(city_locations)):
    x.append(city_locations[city_index][0])
    y.append(city_locations[city_index][1])
  plt.scatter(x,y,zorder=1,color='red')

def plot_path(plt, path):
  connections_x = []
  connections_y = []
  for index in path:
    location_x = city_locations[index][0]
    connections_x.append(location_x)
    location_y = city_locations[index][1]
    connections_y.append(location_y)
  start_location_x = city_locations[path[0]][0]
  start_location_y = city_locations[path[0]][1]
  connections_x.append(start_location_x)
  connections_y.append(start_location_y)
  plt.plot(connections_x,connections_y,color='blue',zorder=0)

def plot(path,city_locations,pause,plot_range):
      plt.cla()
      plot_cities(plt,city_locations)
      plot_path(plt,path)
      plt.pause(pause)
      plt.xlim(0,plot_range)
      plt.ylim(0,plot_range)
      ax = plt.gca()
      ax.set_aspect('equal', adjustable='box')
      plt.show(block=False)
      plt.ion()

# # #####################################
# # # Main program:
# # #####################################

# # ###########################
# # # Data:
# # ###########################
from city_data import city_locations
number_of_cities = len(city_locations)

# # ###########################
# # # Parameters:
# # ###########################
number_of_ants = 50 ## Changes allowed.
alpha = 1.0         ## Changes allowed.
beta = 5.0          ## Changes allowed.
rho = 0.5           ## Changes allowed.
tau_0 = 0.1         ## Changes allowed.

target_path_length = 99.9999999

# #################################
# # Initialization:
# #################################

pheromone_levels = initialize_pheromone_levels(number_of_cities, tau_0)
visibility = get_visibility(city_locations)

# # #################################
# # # Main loop:
# # #################################

iteration_index = 0
minimum_path_length = math.inf
path_length = math.inf
best_path = None

while (minimum_path_length > target_path_length):
  iteration_index += 1
  path_collection = []
  path_length_collection = []
  for ant_index in range(number_of_ants):  
    # Generate paths:
    path = generate_path(pheromone_levels, visibility, alpha, beta) 
    path_length = get_path_length(path, city_locations) 
    if (path_length < minimum_path_length):
      minimum_path_length = path_length
      print(f"Current shortest path: {minimum_path_length}")
      best_path = path.copy()
      plot(path,city_locations,pause=0.1,plot_range=20)
    path_collection.append(path)
    path_length_collection.append(path_length)
  # Update pheromone levels:
  delta_pheromone_levels = compute_delta_pheromone_levels(path_collection,path_length_collection)
  pheromone_levels = update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho)
save_best_path(best_path)
input(f'Press return to exit')
