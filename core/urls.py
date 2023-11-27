from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    path('home', home, name="home"),
    path('horario', horario, name="horario"),
    path('emergencia', emergencia, name="emergencia"),
]
