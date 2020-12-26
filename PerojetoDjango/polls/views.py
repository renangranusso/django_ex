from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def cadastro_doenca(request):
    return render(request, 'cadastro_doenca.html')