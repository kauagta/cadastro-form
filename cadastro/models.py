from encodings import search_function
from django.db import models



class usuarios(models.Model):
    nome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    senha = models.CharField(max_length=20)
