from django.urls import path
from .views import AdicionarUsuarioAoGrupoView

urlpatterns = [
    path('adicionar-usuario-ao-grupo/', AdicionarUsuarioAoGrupoView.as_view(), name='adicionar-usuario-ao-grupo'),
]