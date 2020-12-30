from django.db import models

class Doenca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sintomas = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)
        return str(self.sintomas)

class Epidemiologico(models.Model):
    id = models.AutoField(primary_key=True)
    data_coleta = models.CharField(max_length=10)
    doenca_associada = models.CharField(max_length=100)

    def __str__(self):
       return str(self.data_coleta)
       return str(self.doenca_associada)