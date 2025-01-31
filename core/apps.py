from django.apps import AppConfig
from django.db.models.signals import post_migrate

def criar_grupos_e_permissoes(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from core.models import Evento  # Substitua pelo seu modelo

    # Cria grupos iniciais
    grupos = ['Administradores', 'Usuários Comuns']
    for grupo_nome in grupos:
        Group.objects.get_or_create(name=grupo_nome)

    # Atribui permissões ao grupo 'Administradores'
    grupo_admin = Group.objects.get(name='Administradores')
    content_type = ContentType.objects.get_for_model(Evento)  # Substitua pelo seu modelo
    permissoes = Permission.objects.filter(content_type=content_type)
    grupo_admin.permissions.set(permissoes)

class MyappConfig(AppConfig):
    name = 'core'

    def ready(self):
        post_migrate.connect(criar_grupos_e_permissoes, sender=self)