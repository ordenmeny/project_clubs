from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('collab.urls')),
    # ckeditor
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # path('api/clubs/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),  # new
    path('api/auth-token/', include('djoser.urls.authtoken')),  # new
]

# Djoser urls:
# POST: /api/auth/users/ - создание нового пользователя
# POST: /api/auth-token/token/login/ - возвращает токен

# Процесс авторизации:
# шаг 0: Создание нового пользователя по url /api/auth/users/
# c указанием обязательных полей (username, password).
# -----------------------------------
# 1) Войти с login, password; будет выдан token (его необходимо сохранить)
# 2) Теперь можно делать запрос, например, на /api/clubs/change/45/.
# В HEADERS указать key(Authorization) -> value(Token 9a956...)

urlpatterns += debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
