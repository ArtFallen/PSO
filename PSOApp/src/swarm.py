# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Librerías estándar
import time

# Módulos propios
from .objective_functions import ObjectiveFunctions
from .particle import Particle

class Swarm:

    def __init__(self, n_particles: int, max_iter: int, lower_limit: float,
        upper_limit: float, function_selector: str, dimensions: int) -> None:
        self.n_particles = n_particles
        self.max_iter = max_iter
        self.instanciated_fitness_function = ObjectiveFunctions()
        self.dimensions = dimensions
        function_map = {
            "rastrigin": self.instanciated_fitness_function.rastrigin_function,
            "sphere": self.instanciated_fitness_function.sphere_function,
            "griewank": self.instanciated_fitness_function.griewank_function,
            "styblinski": self.instanciated_fitness_function.styblinski_tang_function
        }

        if function_selector in function_map:
            self.fitness_function = function_map[function_selector]
        else:
            raise ValueError("Select a valid function (sphere, rastrigin, griewank, styblinski)")

        #self.fitness_function almacena métodos

        self.gbest_position = None
        self.gbest_value = float("inf")

        self.complete_swarm = [Particle(lower_limit, upper_limit, dimensions)
        for _ in range(self.n_particles)]


    def update_gbest_and_pbest(self) -> None:
        for particle in self.complete_swarm:
            particle_actual_position_value = self.fitness_function(particle.position)

            if particle_actual_position_value < particle.pbest_value:
                particle.pbest_position = particle.position.copy()  # Copia segura
                particle.pbest_value = particle_actual_position_value

            if particle_actual_position_value < self.gbest_value:
                self.gbest_position = particle.position.copy()  # Copia segura
                self.gbest_value = particle_actual_position_value


    def update_velocity_to_move_particles(self, weight) -> None:
        for particle in self.complete_swarm:
            particle.update_velocity(self.gbest_position, weight)
            particle.update_position()


    def iterating_the_process(self) -> tuple[list[float], float]:
        w_max = 0.9
        w_min = 0.4
        previous_best_value = float('inf')
        start_time = time.time()
        no_improvement_steps = 0
        tolerance = 1e-6

        for x in range(self.max_iter):
            current_time = time.time()
            w = w_max * (w_min / w_max) ** (x / self.max_iter)

            self.update_gbest_and_pbest()
            self.update_velocity_to_move_particles(w)

            # Parada por tiempo (correcta)
            if current_time - start_time > 120:
                break

            # Chequeo de mejora
            if abs(self.gbest_value - previous_best_value) < tolerance:
                no_improvement_steps += 1
            else:
                no_improvement_steps = 0
                previous_best_value = self.gbest_value

            # Parada por falta de mejora
            if no_improvement_steps >= 15:
                break

        return self.gbest_position, self.gbest_value