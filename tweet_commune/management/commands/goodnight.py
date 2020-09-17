from django.core.management.base import BaseCommand

from ...twitter_api import TwitterAPI
from ...logger.tweet_logger import TweetLogger
from database_settings.settings_manager import SettingsManager


class Command(BaseCommand):
    """
    Management command to post a goodnight message
    """

    help = "Say goodnight"

    def handle(self, *args, **options):
        try:
            api = TwitterAPI(
                SettingsManager.get_value('consumer_key'),
                SettingsManager.get_value('consumer_secret'),
                SettingsManager.get_value('access_key'),
                SettingsManager.get_value('access_secret'),
            )
            goodnight_message = 'Good night comrades! See you tomorrow.\nhttps://www.youtube.com/watch?v=lT40nTFax7U'
            api.post(goodnight_message)
            TweetLogger.success(goodnight_message)
        except Exception as e:
            TweetLogger.critical(e)
