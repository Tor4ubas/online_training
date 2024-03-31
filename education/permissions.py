from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модераторы').exists()


class IsAutorOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.groups.filter(name='Модераторы').exists()


class IsAutor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
