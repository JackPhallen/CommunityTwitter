from django.db import models


class SettingsModel(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100)
