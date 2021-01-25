import datetime
import pytz

from .twitter_api import TwitterAPI
from .logger.tweet_logger import TweetLogger
from tweet_commune.submission_validator import SubmissionValidator
from database_settings.settings_manager import SettingsManager


class SubmissionActions:
    """
    Invoke actions on Submission instances
    """

    TZ = pytz.timezone('US/Eastern')

    def __init__(self, submission):
        self.submission = submission

    def validate(self):
        """
        Validate a Submission (returns True if valid)
        """
        validator = SubmissionValidator()
        return validator.validate(self.submission)

    def flag(self):
        """
        Flag a submission as inappropriate
        """
        self.submission.flagged = True
        self.submission.save()

    def post(self):
        """
        Posts a submission to Twitter
        """
        try:
            api = TwitterAPI(
                SettingsManager.get_value('consumer_key'),
                SettingsManager.get_value('consumer_secret'),
                SettingsManager.get_value('access_key'),
                SettingsManager.get_value('access_secret'),
            )
            if self.submission.image:
                api.post(self.submission.text, img_paths=[self.submission.image.path, ])
            else:
                api.post(self.submission.text)
            self.submission.sent = True
            self.submission.date_sent = SubmissionActions.TZ.localize(datetime.datetime.now())
            self.submission.save()
            TweetLogger.success(self.submission.text)
        except Exception as e:
            TweetLogger.tweet_failed(e)
