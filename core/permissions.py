from rest_framework import permissions

class CombinedPermission(permissions.BasePermission):
    def __init__(self, permissions):
        self.permissions = permissions

    def has_permission(self, request, view):
        return any(permission().has_permission(request, view) for permission in self.permissions)

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'adm' or request.user.is_superuser

class IsPresidente(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'presidente' or request.user.is_superuser

class IsVicePresidente(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'vice_presidente' or request.user.is_superuser

class IsSecretarioGeral(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'secretario_geral' or request.user.is_superuser

class IsTesoureiro(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'tesoureiro' or request.user.is_superuser

class IsDiretorEsportes(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'diretor_esportes' or request.user.is_superuser

class IsDiretorEventos(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'diretor_eventos' or request.user.is_superuser

class IsDiretorMarketing(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'diretor_marketing' or request.user.is_superuser

class IsDiretorProdutosVendas(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.cargo == 'diretor_produtos_vendas' or request.user.is_superuser