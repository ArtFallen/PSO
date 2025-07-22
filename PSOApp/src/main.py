# main.py
from .swarm import Swarm
from .utils import plot_2d_particles, plot_3d_surface_with_particles  # asegúrate que está bien importado
import os

def main(particulas, iteraciones, minimo, maximo, funcion, dimension):
    funciones = {"gr": 'griewank', "sp": 'sphere', "ra": 'rastrigin', "st": 'styblinski'}
    swarm = Swarm(particulas, iteraciones, minimo, maximo, funciones.get(funcion), dimension)

    best_position, best_value = swarm.iterating_the_process()

    plot_path = None
    if dimension == 2:
        plot_filename = "grafico_pso.png"
        plot_dir = os.path.join("static")  # Django sirve estáticos desde /static/
        os.makedirs(plot_dir, exist_ok=True)
        plot_path = os.path.join(plot_dir, plot_filename)

        # guardar gráfica
        plot_2d_particles(swarm.complete_swarm, swarm.fitness_function, minimo, maximo)
        imagen = plot_3d_surface_with_particles(swarm.complete_swarm, swarm.fitness_function, minimo, maximo)

    return best_position, best_value, f"/static/plots/{plot_filename}" if plot_path else None, imagen
