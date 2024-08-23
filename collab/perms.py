from rest_framework.permissions import BasePermission


def is_author_club(obj=None, request=None):
    # Return True if user is author of club.
    return obj.author == request.user


def is_admin(request=None):
    # Return True if user is staff
    return bool(request.user and request.user.is_staff)


class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return is_author_club(obj, request) or is_admin(request)
