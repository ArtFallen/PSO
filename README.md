# Particle Swarm Optimization (PSO) - Python Implementation

## Descripción

Este proyecto implementa el algoritmo **Particle Swarm Optimization (PSO)** desde cero utilizando **Programación Orientada a Objetos (POO)** en Python.  
El sistema permite optimizar diferentes funciones objetivo clásicas de benchmarking de optimización matemática.

El diseño es modular, claro y extensible, facilitando futuras mejoras como nuevas funciones, topologías o estrategias de actualización de partículas.

---

## Características

- Implementación de PSO con:
  - Configuración flexible de partículas, dimensiones, límites y funciones.
  - Actualización de velocidades y posiciones por iteración.
  - Condiciones de parada: número de iteraciones, estancamiento y límite de tiempo.

- **Funciones objetivo incluidas**:
  - Rastrigin
  - Sphere
  - Griewank
  - Styblinski-Tang

- Visualización 2D y 3D de la posición de las partículas (en desarrollo en `utils.py`).

- Tests unitarios básicos incluidos (`tests/test_swarm.py`).

---

## Estructura del proyecto

- pso_project/
- │
- ├── src/
- │ ├── particle.py # Clase Particle: representa una partícula individual.
- │ ├── swarm.py # Clase Swarm: representa y gestiona el enjambre completo.
- │ ├── objective_functions.py # Funciones objetivo (Rastrigin, Sphere, Griewank, Styblinski-Tang).
- │ ├── utils.py # (Opcional) Funciones de visualización 2D y 3D.
- │ └── main.py # Script principal para ejecutar experimentos PSO.
- │
- ├── tests/
- │ └── test_swarm.py # Pruebas unitarias para Swarm y Particle.
- │
- └── README.md # Este archivo.

---

## Requisitos

- Python 3.8+
- Numpy
- Matplotlib (para visualizaciones)
- Pytest (para correr tests)

Instalación de dependencias (opcional):

```bash
pip install numpy matplotlib pytest
```

## Ejecución

Para correr el ejemplo principal:

```bash
python -m src.main
```

Esto inicializa varios enjambres con diferentes funciones objetivo y dimensiones, ejecutando PSO para cada uno.

## Tests
Para correr los tests unitarios:
```cmd
pytest tests/test_swarm.py
```
o
```cmd
python -m tests.test_swarm
```
Esto valida:

Correcta ejecución de PSO en:

- 1 dimensión (funciones: Rastrigin, Sphere, Griewank, Styblinski-Tang).

- 2 dimensiones (funciones: Rastrigin, Sphere, Griewank, Styblinski-Tang).

Convergencia esperada (mínimos locales o globales conocidos).

## Visualización

Las funciones de visualización están disponibles en `utils.py`:

```python
plot_2d_particles(swarm.complete_swarm, swarm.fitness_function, lower_limit, upper_limit)
plot_3d_surface_with_particles(swarm.complete_swarm, swarm.fitness_function, lower_limit, upper_limit)
```
Estas permiten graficar:

- La posición actual de las partículas en el espacio de búsqueda.
- La función objetivo evaluada en 2D o 3D junto a las partículas.

## Fuentes de consulta: 
https://en.wikipedia.org/wiki/Particle_swarm_optimization
