# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Módulos propios
from .swarm import Swarm

def main():
    n_particles = 30
    max_iter = 100
    lower_limit = -5.12
    upper_limit = 5.12
    function_selector = "rastrigin"  # Opciones: rastrigin, sphere, griewank, styblinski
    dimensions = 2

    swarm = Swarm(n_particles, max_iter, lower_limit, upper_limit, function_selector, dimensions)
    best_position, best_value = swarm.iterating_the_process()

    print(f"Mejor posición encontrada: {best_position}")
    print(f"Mejor valor encontrado: {best_value}")

if __name__ == "__main__":
    main()
