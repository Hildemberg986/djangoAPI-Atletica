from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    foto_perfil = models.CharField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    matricula = models.CharField(max_length=100, unique=True, blank=True, null=True)
    curso = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)
    tentativas_login = models.IntegerField(default=0)
    bloqueado = models.BooleanField(default=False)
    token_recuperacao = models.CharField(max_length=255, blank=True, null=True)
    expiracao_token = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome