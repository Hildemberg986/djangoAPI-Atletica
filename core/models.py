from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    CARGO_CHOICES = [
        ('adm', 'Administrador'),
        ('presidente', 'Presidente'),
        ('vice_presidente', 'Vice-Presidente'),
        ('secretario_geral', 'Secretário Geral'),
        ('tesoureiro', 'Tesoureiro'),
        ('diretor_esportes', 'Diretor de Esportes'),
        ('diretor_eventos', 'Diretor de Eventos'),
        ('diretor_marketing', 'Diretor de Marketing'),
        ('diretor_produtos_vendas', 'Diretor de Produtos e Vendas'),
    ]
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    atletica = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES, default='membro')

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Jogo(models.Model):
    esporte = models.CharField(max_length=100)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.esporte} - {self.local}"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Notificacao(models.Model):
    mensagem = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem[:50]

class SaudeBemEstar(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Patrocinador(models.Model):
    nome = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=200, blank=True, null=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class ComentarioFeedback(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username}"
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=200)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_responsavel')

    def __str__(self):
        return self.titulo