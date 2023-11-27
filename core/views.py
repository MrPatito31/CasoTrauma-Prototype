from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def horario(request):
    return render(request, 'core/horario.html')

def emergencia(request):
    return render(request, 'core/emergencia.html')