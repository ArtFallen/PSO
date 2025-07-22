# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Librerías estándar
from math import prod, cos, sqrt, pi

class ObjectiveFunctions:
    # Son las funciones objetivo que queremos evaluar

    def rastrigin_function(self, elements_to_evaluate: list[float]) -> float:
        # Múltiples mínimos periódicos
        evaluated_element = (
            10 * len(elements_to_evaluate) +
            sum(x**2 - 10 * cos(2 * pi * x) for x in elements_to_evaluate)
        )
        return evaluated_element

    def sphere_function(self, elements_to_evaluate: list[float]):
        # Convexa, simple
        evaluated_element = sum(x**2 for x in elements_to_evaluate)
        return evaluated_element

    def griewank_function(self, elements_to_evaluate: list[float]):
        sum_part = sum(x**2 for x in elements_to_evaluate)
        prod_part = prod(
            cos(x / sqrt(i + 1)) for i, x in enumerate(elements_to_evaluate)
        )
        evaluated_element = 1 + sum_part / 4000 - prod_part
        return evaluated_element

    def styblinski_tang_function(self, elements_to_evaluate: list[float]):
        # Múltiples mínimos locales
        evaluated_element = sum(
            x**4 - 16 * x**2 + 5 * x for x in elements_to_evaluate
        ) / 2
        return evaluated_element
