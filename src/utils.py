# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Librerías de terceros
import matplotlib.pyplot as plt
import numpy as np


def plot_2d_particles(particles, function, lower_limit, upper_limit, resolution=100):
    """
    Visualiza la función objetivo y la posición de las partículas en 2D.
    """
    if len(particles[0].position) != 2:
        raise ValueError("La visualización 2D requiere funciones de 2 dimensiones.")

    x = np.linspace(lower_limit, upper_limit, resolution)
    y = np.linspace(lower_limit, upper_limit, resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.array([function([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = Z.reshape(X.shape)

    plt.figure(figsize=(8,6))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(label='Fitness')

    # Partículas
    for p in particles:
        plt.scatter(p.position[0], p.position[1], c='red', marker='o')

    plt.title("Visualización 2D de PSO")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()


def plot_3d_surface_with_particles(particles, function, lower_limit, upper_limit, resolution=50):
    """
    Visualiza la función objetivo y la posición de las partículas en 3D.
    """
    if len(particles[0].position) != 2:
        raise ValueError("La visualización 3D requiere funciones de 2 dimensiones.")

    x = np.linspace(lower_limit, upper_limit, resolution)
    y = np.linspace(lower_limit, upper_limit, resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.array([function([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = Z.reshape(X.shape)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    # Partículas
    for p in particles:
        x_p, y_p = p.position
        z_p = function([x_p, y_p])
        ax.scatter(x_p, y_p, z_p, c='red', s=50)

    ax.set_title("Visualización 3D de PSO")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("Fitness")
    plt.show()
