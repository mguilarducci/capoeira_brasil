# coding: utf-8

from django.contrib import admin
from capoeirabrasil.core.models import Capoeirista


class CapoeiristaAdmin(admin.ModelAdmin):
    list_display = ('name', 'graduation', 'phone', 'email', 'created_at')

admin.site.register(Capoeirista, CapoeiristaAdmin)


