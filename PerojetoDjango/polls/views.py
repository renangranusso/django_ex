from django.shortcuts import render, redirect
from .models import Doenca, Epidemiologico
from .forms import doencaForm, epidemioForm
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
    form = epidemioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'cadastro_epidemiologico.html', {'form': form})

def visualizar_doenca(request):
    doenca = Doenca.objects.all()
    return render(request, 'visualizacao_doencas.html', {'doenca': doenca})

def visualizar_epidemio(request):
    epidemio = Epidemiologico.objects.all() #select * from
    return render(request, 'visualizacao_epidemiologica.html', {'epidemio': epidemio})