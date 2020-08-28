from django.core.management.base import BaseCommand, CommandError

from ...settings_manager import SettingsManager


class Command(BaseCommand):
    """
    Management command to set database settings
    """

    help = "Manage database settings from cli"

    def add_arguments(self, parser):
        parser.add_argument('key', type=str)
        parser.add_argument('value', type=str)
        parser.add_argument(
            '--set',
            action='store_true',
            help='Update or create key value pair in database',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete key value pair from database',
        )

    def handle(self, *args, **options):
        if options['set']:
            self._handle_set(*args, **options)
        elif options['delete']:
            self._handle_delete(*args, **options)
        else:
            self._handle_value(*args, **options)

    def _handle_set(self, *args, **options):
        key = options['key']
        value = options['value']
        SettingsManager.set_value(key, value)

    def _handle_delete(self, *args, **options):
        key = options['key']
        if SettingsManager.exists(key):
            SettingsManager.delete(key)
        else:
            raise CommandError('A setting with key "{0}" does not exist in the database!'.format(key))

    def _handle_value(self, *args, **options):
        key = options['key']
        if SettingsManager.exists(key):
            value = SettingsManager.get_value(key)
            self.stdout.write("{0}".format(value))
        else:
            raise CommandError('A setting with key "{0}" does not exist in the database!'.format(key))