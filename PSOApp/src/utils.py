# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 21:14:23 2025

@author: pending

@version = 1.0.0
"""

# Librerías de terceros
import matplotlib
matplotlib.use('Agg')  # <-- usa backend no interactivo

import matplotlib.pyplot as plt
from numpy import array, meshgrid, linspace, ravel
import os
from django.conf import settings  # si estás llamando desde una vista Django
from io import BytesIO
import base64

def plot_2d_particles(particles, function, lower_limit, upper_limit, resolution=100):
    if len(particles[0].position) != 2:
        raise ValueError("La visualización 2D requiere funciones de 2 dimensiones.")

    x = linspace(lower_limit, upper_limit, resolution)
    y = linspace(lower_limit, upper_limit, resolution)
    X, Y = meshgrid(x, y)
    Z = array([function([x, y]) for x, y in zip(ravel(X), ravel(Y))])
    Z = Z.reshape(X.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(label='Fitness')

    for p in particles:
        plt.scatter(p.position[0], p.position[1], c='red', marker='o')

    plt.title("Visualización 2D de PSO")
    plt.xlabel("x1")
    plt.ylabel("x2")

    STATIC_DIR = os.path.join(settings.BASE_DIR, 'PSOApp', 'static', 'plots')
    os.makedirs(STATIC_DIR, exist_ok=True)  # Crea la carpeta si no existe

    output_path = os.path.join(STATIC_DIR, 'grafico_pso.png')
    plt.savefig(output_path)
    plt.close()


def plot_3d_surface_with_particles(particles, function, lower_limit, upper_limit, resolution=50):
    if len(particles[0].position) != 2:
        raise ValueError("La visualización 3D requiere funciones de 2 dimensiones.")

    x = linspace(lower_limit, upper_limit, resolution)
    y = linspace(lower_limit, upper_limit, resolution)
    X, Y = meshgrid(x, y)
    Z = array([function([x_, y_]) for x_, y_ in zip(ravel(X), ravel(Y))])
    Z = Z.reshape(X.shape)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    for p in particles:
        x_p, y_p = p.position
        z_p = function([x_p, y_p])
        ax.scatter(x_p, y_p, z_p, c='red', s=50)

    ax.set_title("Visualización 3D de PSO")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("Fitness")

    # Convertir a imagen en base64 para mostrar en la web
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)
    return image_base64
