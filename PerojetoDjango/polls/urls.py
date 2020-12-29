from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #^$ Não adicione nada na URL (sempre colocar virgula no final)
    url('cad_doenca', views.cadastro_doenca),
    url('cad_epidemio', views.cadastro_epidemiologico),
    url('visual_doenca', views.visualizar_doenca),
    url('visual_epidemio', views.visualizar_epidemio),
]
