from django.db import models

class Doenca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sintomas = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)
        return str(self.sintomas)

'''class Epidemiologico(db.Model):
    __tablename__ = 'Epidemiologico'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    data_coleta = db.Column(db.String(10))
    doenca_associada = db.Column(db.String(100))

    def __init__(self, data_coleta, doenca_associada):
        self.data_coleta = data_coleta
        self.doenca_associada = doenca_associada'''