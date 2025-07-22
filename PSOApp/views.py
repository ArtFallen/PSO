from django.shortcuts import render
from django.http import HttpResponse
from .src.main import main  # asegúrate que esta ruta sea correcta

def pso_form(request):
    return render(request, 'pso_form.html')

def procesar_pso(request):
    if request.method == 'POST':
        funcion = request.POST.get('funcion')
        iteraciones = int(request.POST.get('iteraciones'))
        particulas = int(request.POST.get('particulas'))
        minimo = float(request.POST.get('minimo'))
        maximo = float(request.POST.get('maximo'))
        dimension = int(request.POST.get('dimension'))

        best_position, best_value, plot_url_1, image_base64 = main(particulas, iteraciones, minimo, maximo, funcion, dimension)

        context = {
            'funcion': funcion,
            'iteraciones': iteraciones,
            'particulas': particulas,
            'minimo': minimo,
            'maximo': maximo,
            'dimension': dimension,
            'best_position': best_position,
            'best_value': best_value,
            'plot_url_1': plot_url_1,  
            'image_base64': image_base64,
        }

        return render(request, 'results.html', context)

    return HttpResponse("Método no permitido", status=405)
