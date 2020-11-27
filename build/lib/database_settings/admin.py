from django.contrib import admin

from .models import SettingsModel


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


admin.site.register(SettingsModel, SettingsAdmin)