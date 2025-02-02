from rest_framework import serializers
from .models import Evento, Usuario, Cargo, Noticia, Jogo, Produto, Notificacao, SaudeBemEstar, Patrocinador, ComentarioFeedback

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'matricula', 'curso', 'atletica', 'cargo']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'

class SaudeBemEstarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaudeBemEstar
        fields = '__all__'

class PatrocinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrocinador
        fields = '__all__'

class ComentarioFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioFeedback
        fields = '__all__'
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'