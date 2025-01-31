from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from .models import Usuario
from .serializers import UsuarioSerializer

class AdicionarUsuarioAoGrupoView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Apenas administradores autenticados podem usar

    def post(self, request):
        usuario_id = request.data.get('usuario_id')
        grupo_nome = request.data.get('grupo_nome')

        try:
            usuario = Usuario.objects.get(id=usuario_id)
            grupo = Group.objects.get(name=grupo_nome)
            usuario.groups.add(grupo)
            return Response({'status': 'Usuário adicionado ao grupo com sucesso'}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Group.DoesNotExist:
            return Response({'error': 'Grupo não encontrado'}, status=status.HTTP_404_NOT_FOUND)