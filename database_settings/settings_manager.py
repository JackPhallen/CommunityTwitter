from .models import SettingsModel


class SettingsManager:

    @staticmethod
    def exists(key):
        return SettingsModel.objects.all().filter(key=key).exists()

    @staticmethod
    def get_value(key):
        return SettingsModel.objects.all().get(key=key).value

    @staticmethod
    def set_value(key, value):
        SettingsModel.objects.update_or_create(
            key=key,
            defaults={'value': value}
        )

    @staticmethod
    def delete(key):
        SettingsModel.objects.get(key=key).delete()
