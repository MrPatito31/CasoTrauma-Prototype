from django.shortcuts import *
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *

def home(request):
    emergencias = Emergencia.objects.all()
    return render(request, 'core/index.html', {'emergencias': emergencias})

def login(request):
    return render(request, 'core/login.html')

def logout(request):
    return logout_then_login(request, login_url="login")

def horario(request):
    return render(request, 'core/horario.html')

def emergencia(request):
    return render(request, 'core/emergencia.html')

def register(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/register.html', {'form': registro})

def enviar_emergencia(request):
    if request.method == 'POST':
        npac = request.POST.get('Npaciente', '')
        context = request.POST.get('Context', '')

        # Validación de campos vacíos
        if not npac or not context:
            datos = {'r2': 'Por favor, completa todos los campos.'}
            return render(request, 'core/emergencia.html', datos)

        emer = Emergencia(numero_paciente=npac, contexto_emergencia=context)
        emer.save()
        datos = {'r': 'Registro realizado Correctamente!!'}
        return render(request, 'core/emergencia.html', datos)
    else:
        datos = {'r2': 'No se puede procesar la solicitud!!'}
        return render(request, 'core/emergencia.html', datos)