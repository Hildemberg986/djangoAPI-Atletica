from rest_framework import viewsets, permissions
from .models import Usuario, Cargo, Noticia, Jogo, Produto, Notificacao, SaudeBemEstar, Patrocinador, ComentarioFeedback, Evento
from .serializers import UsuarioSerializer, CargoSerializer, NoticiaSerializer, JogoSerializer, ProdutoSerializer, NotificacaoSerializer, SaudeBemEstarSerializer, PatrocinadorSerializer, ComentarioFeedbackSerializer, EventoSerializer
from .permissions import IsAdmin, IsPresidente, IsVicePresidente, IsSecretarioGeral, IsTesoureiro, IsDiretorEsportes, IsDiretorEventos, IsDiretorMarketing, IsDiretorProdutosVendas, CombinedPermission

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdmin]

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAdmin]

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsSecretarioGeral,
                IsTesoureiro,
                IsDiretorEsportes,
                IsDiretorEventos,
                IsDiretorMarketing,
                IsDiretorProdutosVendas,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsDiretorEsportes,
                IsDiretorMarketing,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsDiretorMarketing,
                IsDiretorProdutosVendas,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsSecretarioGeral,
                IsTesoureiro,
                IsDiretorEsportes,
                IsDiretorEventos,
                IsDiretorMarketing,
                IsDiretorProdutosVendas,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class SaudeBemEstarViewSet(viewsets.ModelViewSet):
    queryset = SaudeBemEstar.objects.all()
    serializer_class = SaudeBemEstarSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsDiretorMarketing,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class PatrocinadorViewSet(viewsets.ModelViewSet):
    queryset = Patrocinador.objects.all()
    serializer_class = PatrocinadorSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsDiretorMarketing,
                IsDiretorProdutosVendas,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class ComentarioFeedbackViewSet(viewsets.ModelViewSet):
    queryset = ComentarioFeedback.objects.all()
    serializer_class = ComentarioFeedbackSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsDiretorMarketing,
                IsDiretorProdutosVendas,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [CombinedPermission([
                IsPresidente,
                IsVicePresidente,
                IsDiretorEventos,
                IsAdmin
            ])]
        return [permissions.IsAuthenticated()]