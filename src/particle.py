# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Librerías de terceros
from numpy.random import rand, uniform
from numpy import clip


class Particle:

    def __init__(self, lower_limit: float, upper_limit:float, dimensions) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.dimensions = dimensions
        self.position = uniform(lower_limit, upper_limit, dimensions)
        self.pbest_position = self.position.copy()
        self.pbest_value = float('inf') #es el valor calculado con la función
        self.velocity = uniform(-0.1 * abs(upper_limit - lower_limit),
        0.1 * abs(upper_limit - lower_limit), dimensions)


    def update_velocity(self, gbest_position: float, inertia_weight = 0.5,
    cognitive_coefficient = 1.5, social_coefficient = 1.5) -> None:
        rp = rand(self.dimensions)
        rg = rand(self.dimensions)
        cognitive_component = cognitive_coefficient * rp * (self.pbest_position
        - self.position)
        social_component = social_coefficient * rg * (gbest_position - self.position)
        self.velocity = (inertia_weight * self.velocity + cognitive_component +
        social_component)


    def update_position(self):
        self.position += self.velocity
        self.position = clip(self.position, self.lower_limit, self.upper_limit)

    def __repr__(self):
        return f"""Particle(position={self.position}, pbest={self.pbest_position}, 
        velocity={self.velocity})"""
