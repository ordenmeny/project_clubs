from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('collab.urls')),
    # ckeditor
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    # djoser (drf authentication by token)
    path('api/auth/', include('djoser.urls')),

    # POST: api/token-auth/token/login/ - get a token
    path('api/token-auth/', include('djoser.urls.authtoken')),
]

urlpatterns += debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
