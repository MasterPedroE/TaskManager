from enum import UNIQUE
from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

def __str__(self):
    return self.username