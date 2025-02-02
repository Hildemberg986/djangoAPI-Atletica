from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, UsuarioViewSet, CargoViewSet, NoticiaViewSet, JogoViewSet, ProdutoViewSet, NotificacaoViewSet, SaudeBemEstarViewSet, PatrocinadorViewSet, ComentarioFeedbackViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'jogos', JogoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'notificacoes', NotificacaoViewSet)
router.register(r'saude-bem-estar', SaudeBemEstarViewSet)
router.register(r'patrocinadores', PatrocinadorViewSet)
router.register(r'comentarios-feedback', ComentarioFeedbackViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]