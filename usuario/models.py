from enum import UNIQUE

from django.db import models
from django.db.models import CharField


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

def __str__(self):
    return f'{self.nome} + {self.senha} + {self.email}'