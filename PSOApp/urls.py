from django.urls import path
from . import views

urlpatterns = [
    path('', views.pso_form, name='pso_form'),
    path('procesar/', views.procesar_pso, name='procesar_pso'),
]