from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Нельзя изменять чужой контент!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user == obj.author)
