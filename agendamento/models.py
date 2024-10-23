from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Espaco(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f'agendamento de {self.usuario} em {self.data} no {self.espaco}'