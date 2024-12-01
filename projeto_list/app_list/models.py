from django.db import models

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=100)
    descricao = models.TextField(max_length=15)
    