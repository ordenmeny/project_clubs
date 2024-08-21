from rest_framework.permissions import BasePermission, SAFE_METHODS


# Все пользователи независимо от операции должны быть авторизованы.
# Изменение, удаление - только для авторов клуба.
# Просмотр всех или отдельных клубов, создание новых клубов - для авторизованных

class IsAuthorPerm(BasePermission):
    # После проверки IsAuthenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Для POST, DELETE, PUT
        return obj.author == request.user
