# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Librerías de terceros
import numpy as np


# Módulos propios
from src.swarm import Swarm
from src.utils import plot_2d_particles, plot_3d_surface_with_particles

def test_swarm():
    swarms = [
        Swarm(50, 300, -5.12, 5.12, "rastrigin", 1),
        Swarm(30, 300, -800, 800, "sphere", 1),
        Swarm(30, 300, -5, 5, "styblinski", 1),
        Swarm(30, 300, -5, 5, "griewank", 1),
        Swarm(50, 300, -5.12, 5.12, "rastrigin", 2),
        Swarm(30, 300, -800, 800, "sphere", 2),
        Swarm(30, 300, -5, 5, "styblinski", 2),
        Swarm(30, 300, -5, 5, "griewank", 2),
    ]

    for i, swarm in enumerate(swarms, 1):
        gbest_position, gbest_value = swarm.iterating_the_process()

        print(f"Swarm {i}: Best Position: {gbest_position}, Best Value: {gbest_value}")

        # Verificaciones básicas:
        assert isinstance(gbest_position, (list, np.ndarray)), f"""
        Swarm {i}: gbest_position no es lista o ndarray."""

        assert isinstance(gbest_value, float), f"Swarm {i}: gbest_value no es float."

        assert len(gbest_position) == swarm.dimensions, f"""
        Swarm {i}: Dimensión de posición incorrecta."""

        # Visualización solo si es 2D
        if swarm.dimensions == 2:
            plot_2d_particles(swarm.complete_swarm, swarm.fitness_function, -5, 5)
            plot_3d_surface_with_particles(swarm.complete_swarm, swarm.fitness_function, -5, 5)


if __name__ == "__main__":
    test_swarm()
