from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', logout, name="logout"),
    path('home', home, name="home"),
    path('horario', horario, name="horario"),
    path('emergencia', emergencia, name="emergencia"),
    path('register', register, name="register"),
    path('enviar_emergencia', enviar_emergencia, name='enviar_emergencia'),
]
