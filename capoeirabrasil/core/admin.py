# coding: utf-8

from django.contrib import admin
from capoeirabrasil.core.models import Capoeirista, Event, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class CapoeiristaAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'graduation', 'belt', 'phone', 'email', 'created_at')


class EventAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ('title', 'date', 'capoeirista', 'created_at')

admin.site.register(Capoeirista, CapoeiristaAdmin)
admin.site.register(Event, EventAdmin)
