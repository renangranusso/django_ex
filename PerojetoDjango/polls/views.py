from django.shortcuts import render, redirect
from .models import Doenca
from .forms import doencaForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')

def cadastro_doenca(request):
    form = doencaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'cadastro_doenca.html', {'form': form})

def cadastro_epidemiologico(request):
    return render(request, 'cadastro_epidemiologico.html')

def visualizar_doenca(request):
    doenca = Doenca.objects.all()
    return render(request, 'visualizacao_doencas.html', {'doenca': doenca})

def visualizar_epidemio(request):
    #epidemio = epidemio.objects.all()
    return render(request, 'visualizacao_epidemiologica.html')