from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def cadastro_doenca(request):
    return render(request, 'cadastro_doenca.html')

def cadastro_epidemiologico(request):
    return render(request, 'cadastro_epidemiologico.html')

def visualizar_doenca(request):
    return render(request, 'visualizacao_doencas.html')

def visualizar_epidemio(request):
    return render(request, 'visualizacao_epidemiologica.html')