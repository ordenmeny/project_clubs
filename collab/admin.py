from django.contrib import admin
from .models import *

admin.site.register(ClubModel)


class ClubAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'desc')


admin.site.register(Club, ClubAdmin)
