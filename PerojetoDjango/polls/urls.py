'''from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #^$ Não adicione nada na URL (sempre colocar virgula no final)
    url('', views.cadastro_doenca, name='cadastro_doenca'),
    url('', views.cadastro_epidemiologico, name='cadastro_epidemiologico'),
    url('', views.visualizar_doenca, name='visual_doenca'),
    url('', views.visualizar_epidemio, name='visual_epidemio')
]'''
